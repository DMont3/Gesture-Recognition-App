import cv2
import mediapipe as mp
import time
import pyautogui


def initialize_media_pipe():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=2, static_image_mode=False, min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils
    return hands, mp_draw


def is_hand_open(hand_landmarks):
    landmarks = hand_landmarks.landmark
    thumb_tip = landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks[mp.solutions.hands.HandLandmark.THUMB_IP]
    thumb_mcp = landmarks[mp.solutions.hands.HandLandmark.THUMB_MCP]
    thumb_cmc = landmarks[mp.solutions.hands.HandLandmark.THUMB_CMC]
    index_tip = landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    middle_tip = landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_mcp = landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP]
    ring_tip = landmarks[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    ring_mcp = landmarks[mp.solutions.hands.HandLandmark.RING_FINGER_MCP]
    pinky_tip = landmarks[mp.solutions.hands.HandLandmark.PINKY_TIP]
    pinky_mcp = landmarks[mp.solutions.hands.HandLandmark.PINKY_MCP]

    return (thumb_tip.y < thumb_ip.y < thumb_mcp.y < thumb_cmc.y and
            index_tip.y < index_mcp.y and
            middle_tip.y < middle_mcp.y and
            ring_tip.y < ring_mcp.y and
            pinky_tip.y < pinky_mcp.y)


def get_gesture(hand_landmarks, last_action_time, current_time):
    landmarks = hand_landmarks.landmark
    thumb_tip = landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks[mp.solutions.hands.HandLandmark.THUMB_IP]
    thumb_mcp = landmarks[mp.solutions.hands.HandLandmark.THUMB_MCP]
    thumb_cmc = landmarks[mp.solutions.hands.HandLandmark.THUMB_CMC]
    index_tip = landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    middle_tip = landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_mcp = landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP]
    ring_tip = landmarks[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]
    ring_mcp = landmarks[mp.solutions.hands.HandLandmark.RING_FINGER_MCP]
    pinky_tip = landmarks[mp.solutions.hands.HandLandmark.PINKY_TIP]
    pinky_mcp = landmarks[mp.solutions.hands.HandLandmark.PINKY_MCP]

    # Resetar gesto
    gesto, action_key = "Nenhum Gesto", None

    # Gestos básicos com controle de tempo
    if is_hand_open(hand_landmarks):
        if current_time - last_action_time['space'] > 3:
            last_action_time['space'] = current_time
            gesto, action_key = "Mão Aberta", 'space'
    elif index_tip.y < index_mcp.y and all(other.y > index_mcp.y for other in [middle_tip, ring_tip, pinky_tip]):
        if current_time - last_action_time['up'] > 1:
            last_action_time['up'] = current_time
            gesto, action_key = "Indicador Para Cima", 'up'
    elif index_tip.y > index_mcp.y and all(other.y > index_mcp.y for other in [middle_tip, ring_tip, pinky_tip]):
        if current_time - last_action_time['down'] > 1:
            last_action_time['down'] = current_time
            gesto, action_key = "Indicador Para Baixo", 'down'
    elif index_tip.y < index_mcp.y and middle_tip.y < middle_mcp.y and all(
            other.y > middle_mcp.y for other in [ring_tip, pinky_tip]):
        if current_time - last_action_time['right'] > 1:
            last_action_time['right'] = current_time
            gesto, action_key = "Dois Dedos Para Cima", 'right'
    elif thumb_tip.y < thumb_ip.y < thumb_mcp.y < thumb_cmc.y and pinky_tip.y < pinky_mcp.y and all(
            tip.y > mcp.y for tip, mcp in [(index_tip, index_mcp), (middle_tip, middle_mcp), (ring_tip, ring_mcp)]):
        if current_time - last_action_time['left'] > 1:
            last_action_time['left'] = current_time
            gesto, action_key = "Hang Loose", 'left'
    elif index_tip.y < index_mcp.y and pinky_tip.y < pinky_mcp.y and all(
            other.y > middle_mcp.y for other in [middle_tip, ring_tip]):
        if current_time - last_action_time['rock'] > 1:
            last_action_time['rock'] = current_time
            gesto = "Rock"

    return gesto, action_key


def process_frame(img, hands, mp_draw, last_action_time, last_gesture, last_gesture_time):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    current_time = time.time()
    gesto, action_key = "Nenhum Gesto", None
    if results.multi_hand_landmarks:
        if len(results.multi_hand_landmarks) == 2:
            if all(is_hand_open(hand) for hand in results.multi_hand_landmarks):
                if current_time - last_action_time['f'] > 3:
                    last_action_time['f'] = current_time
                    gesto = "Duas Mãos Abertas"
                    action_key = 'f'
                    print(f"Pressing key: {action_key} for gesture: {gesto}")  # Mensagem de depuração
                    pyautogui.press(action_key)
        else:
            for hand_landmarks in results.multi_hand_landmarks:
                gesto, action_key = get_gesture(hand_landmarks, last_action_time, current_time)
                mp_draw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                if action_key:
                    print(f"Pressing key: {action_key} for gesture: {gesto}")  # Mensagem de depuração
                    pyautogui.press(action_key)
                break  # Processar apenas a primeira mão detectada

    if gesto != "Nenhum Gesto":
        last_gesture = gesto
        last_gesture_time = current_time
    elif current_time - last_gesture_time > 1:
        last_gesture = "Nenhum Gesto"

    print(f"Detected gesture: {last_gesture}")  # Log do gesto detectado

    return img, last_gesture, last_gesture_time


def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Largura
    cap.set(4, 480)  # Altura
    cap.set(cv2.CAP_PROP_FPS, 15)  # Ajustar FPS se necessário

    hands, mp_draw = initialize_media_pipe()
    last_action_time = {'space': 0, 'up': 0, 'down': 0, 'left': 0, 'right': 0, 'rock': 0, 'f': 0}
    last_gesture = "Nenhum Gesto"
    last_gesture_time = time.time()

    while True:
        success, img = cap.read()
        if not success:
            continue

        img, last_gesture, last_gesture_time = process_frame(
            img, hands, mp_draw, last_action_time, last_gesture, last_gesture_time
        )

        cv2.putText(img, f'Gesto: {last_gesture}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

