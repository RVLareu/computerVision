# pip install opencv-python
import cv2
# pip install mediapipe
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands

# false to detect/track so it doesnt slow down (default are OK)
hands =  mpHands.Hands()

mpDraw = mp.solutions.drawing_utils


pTime = 0
cTime = 0

while True:
    # Capture frame-by-frame
    success, frame = cap.read()
    # frame to rgb
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # for each hand
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(frame, "FPS: " + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)

    # show the frame
    cv2.imshow("frame", frame)
    # framerate
    cv2.waitKey(1)

