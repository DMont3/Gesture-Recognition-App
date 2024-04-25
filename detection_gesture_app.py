import cv2
import mediapipe as mp
import time
import pyautogui

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

            # Atualiza a impressão do gesto a cada intervalo de tempo definido
            current_time = time.time()
            if current_time - last_space_press_time >= intervalo_tempo:
                print(f"Gesture Detected: {gesture} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
                if gesture == "Legal":
                    pyautogui.press('space')  # Simula a tecla de espaço para pausar o vídeo
                last_space_press_time = current_time

            mp_draw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            cv2.putText(img, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return img, gesture, last_space_press_time

def get_finger_positions(img, hand_landmarks):
    h, w, c = img.shape
    finger_positions = [(id, int(lm.x * w), int(lm.y * h)) for id, lm in enumerate(hand_landmarks.landmark)]
    return finger_positions

def identify_gesture(finger_positions):
    # Acessa as coordenadas y de cada dedo relevante
    thumb_tip_y = finger_positions[4][2]
    index_tip_y = finger_positions[8][2]
    middle_tip_y = finger_positions[12][2]
    ring_tip_y = finger_positions[16][2]
    pinky_tip_y = finger_positions[20][2]

    # Acessa as coordenadas x dos dedos para determinar gestos horizontais
    thumb_tip_x = finger_positions[4][1]
    index_tip_x = finger_positions[8][1]
    middle_base_x = finger_positions[9][1]
    ring_base_x = finger_positions[13][1]
    pinky_base_x = finger_positions[17][1]


    if index_tip_y < middle_tip_y and index_tip_y < ring_tip_y and middle_tip_y > ring_tip_y and ring_tip_y > pinky_tip_y:
        return "Vitória"
    elif thumb_tip_x < index_tip_x and pinky_tip_y < ring_tip_y:
        return "Apontar Esquerda"
    elif index_tip_y < middle_tip_y and index_tip_y < ring_tip_y and index_tip_y < pinky_tip_y:
        average_x = (middle_base_x + ring_base_x + pinky_base_x) / 3
        if index_tip_x < average_x:
            return "Legal"
        else:
            return "Apontar Direita"

    return "Nao Definido"


def main():
    cap = cv2.VideoCapture(0)
    hands, mp_draw = inicia_mediapipe()
    last_space_press_time = 0
    intervalo_tempo = 2  # Intervalo em segundos para imprimir o gesto detectado


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
