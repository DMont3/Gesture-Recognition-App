import cv2
import mediapipe as mp

# Inicializa a captura de vídeo
cap = cv2.VideoCapture(0)

# Configurações do MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Loop principal para captura e processamento de cada frame
while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)  # Inverte a imagem
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Processa a detecção da mão
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Lista para armazenar a posição dos dedos
            finger_positions = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                finger_positions.append((id, cx, cy))

            if finger_positions:
                # Identificar "Vitória"
                if (finger_positions[8][2] < finger_positions[6][2]) and (finger_positions[12][2] < finger_positions[10][2]):
                    gesture = "Vitoria"
                # Identificar "Legal"
                elif (finger_positions[4][1] < finger_positions[3][1]) and (finger_positions[20][2] > finger_positions[18][2]):
                    gesture = "Legal"
                # Apontar para esquerda ou direita
                elif (finger_positions[8][2] < finger_positions[6][2]) and all(finger_positions[4*i+2][2] > finger_positions[4*i][2] for i in range(2, 5)):  # Dedo indicador é o único levantado
                    # Checa se a posição x do dedo indicador é menor que a média das posições x da base dos outros dedos levantados
                    if finger_positions[8][1] < (finger_positions[5][1] + finger_positions[9][1] + finger_positions[13][1] + finger_positions[17][1]) / 4:
                        gesture = "Apontar Esquerda"
                    else:
                        gesture = "Apontar Direita"
                else:
                    gesture = "Nao Definido"

                # Desenha o gesto identificado na tela
                cv2.putText(img, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Desenha as landmarks da mão
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Mostra a imagem resultante
    cv2.imshow("Hand Tracking", img)

    # Fecha o programa quando 'q' é pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e destrói todas as janelas abertas
cap.release()
cv2.destroyAllWindows()
