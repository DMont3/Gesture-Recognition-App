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
    if is_pointing_up(finger_positions):
        pyautogui.press('volumemute')  # Desativa/Ativa som
        return "Apontar para Cima"
    elif is_pointing_left(finger_positions):
        pyautogui.press('j')  # Avançar (esquerda)
        return "Apontar Esquerda"
    elif is_pointing_right(finger_positions):
        pyautogui.press('l')  # Avançar (direita)
        return "Apontar Direita"
    elif is_victory(finger_positions):
        pyautogui.press('<')  # Diminuir velocidade
        return "V de Vitória"
    elif is_hang_loose(finger_positions):
        pyautogui.press('>')  # Aumentar velocidade
        return "Hang Loose"
    elif is_rock(finger_positions):
        pyautogui.press('volumeup')  # Aumentar volume
        return "Rock"
    elif is_three(finger_positions):
        pyautogui.press('volumedown')  # Diminuir volume
        return "3"
    elif is_hand_open(finger_positions):
        pyautogui.press('k')  # Pausar
        return "Mao Aberta"

    return "Nao Definido"

def is_pointing_up(finger_positions):
    index_tip = finger_positions[8]
    index_base = finger_positions[5]
    other_tips = [finger_positions[i] for i in [12, 16, 20]]
    return index_tip[2] < index_base[2] and all(tip[2] > index_base[2] for tip in other_tips)

def is_pointing_left(finger_positions):
    index_tip = finger_positions[8]
    thumb_tip = finger_positions[4]
    other_tips = [finger_positions[i] for i in [12, 16, 20]]
    return index_tip[1] < thumb_tip[1] and all(tip[2] > finger_positions[5][2] for tip in other_tips)

def is_pointing_right(finger_positions):
    index_tip = finger_positions[8]
    thumb_tip = finger_positions[4]
    other_tips = [finger_positions[i] for i in [12, 16, 20]]
    return index_tip[1] > thumb_tip[1] and all(tip[2] > finger_positions[5][2] for tip in other_tips)

def is_victory(finger_positions):
    index_tip = finger_positions[8]
    middle_tip = finger_positions[12]
    index_base = finger_positions[5]
    middle_base = finger_positions[9]
    other_tips = [finger_positions[i] for i in [16, 20]]
    return index_tip[2] < index_base[2] and middle_tip[2] < middle_base[2] and all(tip[2] > middle_base[2] for tip in other_tips)

def is_hang_loose(finger_positions):
    thumb_tip = finger_positions[4]
    pinky_tip = finger_positions[20]
    other_tips = [finger_positions[i] for i in [8, 12, 16]]
    return thumb_tip[2] < finger_positions[2][2] and pinky_tip[2] < finger_positions[17][2] and all(tip[2] > finger_positions[5][2] for tip in other_tips)

def is_rock(finger_positions):
    index_tip = finger_positions[8]
    pinky_tip = finger_positions[20]
    index_base = finger_positions[5]
    middle_tip = finger_positions[12]
    ring_tip = finger_positions[16]
    return index_tip[2] < index_base[2] and pinky_tip[2] < finger_positions[17][2] and middle_tip[2] > finger_positions[9][2] and ring_tip[2] > finger_positions[13][2]

def is_three(finger_positions):
    index_tip = finger_positions[8]
    middle_tip = finger_positions[12]
    ring_tip = finger_positions[16]
    pinky_tip = finger_positions[20]
    thumb_tip = finger_positions[4]
    return all(tip[2] < finger_positions[5][2] for tip in [index_tip, middle_tip, ring_tip]) and all(tip[2] > finger_positions[5][2] for tip in [pinky_tip, thumb_tip])

def is_hand_open(finger_positions):
    return all(finger_positions[i][2] < finger_positions[i - 3][2] for i in range(8, 21, 4)) and finger_positions[4][2] < finger_positions[2][2]

def main():
    cap = cv2.VideoCapture(0)
    hands, mp_draw = inicia_mediapipe()
    last_space_press_time = 0
    intervalo_tempo = 2.5

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
