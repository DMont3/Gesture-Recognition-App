import cv2
import mediapipe as mp
import pyautogui
import time

def inicia_mediapipe():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils
    return hands, mp_draw

def processa_frame(img, hands, mp_draw, last_space_press_time, intervalo_tempo):
    img = cv2.flip(img, 1)  # Inverte a imagem
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    gesture = "Nao Definido"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            finger_positions = get_finger_positions(img, hand_landmarks)
            gesture = identify_gesture(finger_positions)

            current_time = time.time()
            if current_time - last_space_press_time >= intervalo_tempo:
                print(f"Gesture Detected: {gesture} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
                last_space_press_time = current_time

            mp_draw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            cv2.putText(img, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return img, gesture, last_space_press_time

def get_finger_positions(img, hand_landmarks):
    h, w, c = img.shape
    finger_positions = [(id, int(lm.x * w), int(lm.y * h)) for id, lm in enumerate(hand_landmarks.landmark)]
    return finger_positions

def identify_gesture(finger_positions):
    if is_hand_open(finger_positions):
        pyautogui.press('k')  # Adicionado comando pyautogui
        return "Mao Aberta"

    index_tip = finger_positions[8]
    middle_tip = finger_positions[12]
    ring_tip = finger_positions[16]
    pinky_tip = finger_positions[20]
    thumb_tip = finger_positions[4]
    index_base = finger_positions[5]
    middle_base = finger_positions[9]

    if index_tip[2] < index_base[2] and middle_tip[2] < middle_base[2] and \
       all(finger_tip[2] > middle_base[2] for finger_tip in [ring_tip, pinky_tip]):
        pyautogui.press('<')  # Adicionado comando pyautogui
        return "V de Vitória"

    if thumb_tip[2] < finger_positions[2][2] and pinky_tip[2] < finger_positions[17][2] and \
        index_tip[2] > index_base[2] and middle_tip[2] > middle_base[2] and ring_tip[2] > finger_positions[13][2]:
        pyautogui.press('>')  # Adicionado comando pyautogui
        return "Hang Loose"

    if index_tip[2] < index_base[2] and pinky_tip[2] < finger_positions[17][2] and \
       middle_tip[2] > middle_base[2] and ring_tip[2] > middle_base[2]:
        pyautogui.press('volumeup')  # Adicionado comando pyautogui
        return "Rock"

    if index_tip[2] < index_base[2] and all(finger_tip[2] > index_base[2] for finger_tip in [middle_tip, ring_tip, pinky_tip]):
        pyautogui.press('m')  # Adicionado comando pyautogui
        return "Indicador Para Cima"

    thumb_tip_x = thumb_tip[1]
    index_tip_x = index_tip[1]
    middle_base_x = middle_base[1]
    ring_base_x = ring_tip[1]
    pinky_base_x = pinky_tip[1]

    if thumb_tip_x < index_tip_x and pinky_tip[2] < ring_tip[2]:
        pyautogui.press('j')  # Adicionado comando pyautogui
        return "Apontar Esquerda"
    elif all(finger_positions[i][2] < finger_positions[i + 4][2] for i in range(5, 17, 4)):
        average_x = (middle_base_x + ring_base_x + pinky_base_x) / 3
        if index_tip_x < average_x:
            pyautogui.press('volumedown')  # Adicionado comando pyautogui
            return "Legal"
        else:
            pyautogui.press('l')  # Adicionado comando pyautogui
            return "Apontar Direita"

    return "Nao Definido"

def is_hand_open(finger_positions):
    return all(finger_positions[i][2] < finger_positions[i - 3][2] for i in range(8, 21, 4)) and \
           finger_positions[4][2] < finger_positions[2][2]

def main():
    cap = cv2.VideoCapture(0)
    hands, mp_draw = inicia_mediapipe()
    last_space_press_time = 0
    intervalo_tempo = 2

    while True:
        success, img = cap.read()
        if not success:
            continue

        img, gesture, last_space_press_time = processa_frame(img, hands, mp_draw, last_space_press_time, intervalo_tempo)

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
