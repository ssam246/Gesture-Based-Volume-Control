import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize Mediapipe and Audio API
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Initialize Volume Control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]
volBar, volPer = 400, 0

# Webcam Setup
wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)

# State variables
gestureControlActive = True  # Gesture mode toggle

# Mediapipe Hand Tracking
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:

    while cam.isOpened():
        success, image = cam.read()
        if not success:
            print("Failed to grab frame. Exiting...")
            break

        # Flip image for a mirror view
        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                # Extract hand landmark positions
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, _ = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

        # Gesture Volume Control Logic
        if len(lmList) != 0:
            # Thumb and Index Finger Coordinates
            x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip
            x2, y2 = lmList[8][1], lmList[8][2]  # Index finger tip
            length = math.hypot(x2 - x1, y2 - y1)

            # Toggle Gesture Control with Thumbs-Up Gesture
            if lmList[4][1] < lmList[3][1] and lmList[8][1] > lmList[6][1]:  # Thumbs-Up
                gestureControlActive = not gestureControlActive
                cv2.putText(image, "Gesture Control Toggled", (100, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if gestureControlActive:
                # Draw markers
                cv2.circle(image, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                cv2.circle(image, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

                # Volume Adjustment
                vol = np.interp(length, [30, 220], [minVol, maxVol])
                volBar = np.interp(length, [30, 220], [400, 150])
                volPer = np.interp(length, [30, 220], [0, 100])
                volume.SetMasterVolumeLevel(vol, None)

                # Volume Bar Visualization
                cv2.rectangle(image, (50, 150), (85, 400), (0, 0, 0), 3)
                cv2.rectangle(image, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

                # Fun Feedback (Glow effect)
                if length < 50:
                    cv2.circle(image, (x1, y1), 25, (0, 255, 255), cv2.FILLED)
                    cv2.circle(image, (x2, y2), 25, (0, 255, 255), cv2.FILLED)

        # Show feedback on gesture mode
        statusText = "Gesture Control: ON" if gestureControlActive else "Gesture Control: OFF"
        cv2.putText(image, statusText, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        # Display
        cv2.imshow('Gesture Volume Control', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Cleanup
cam.release()
cv2.destroyAllWindows()

