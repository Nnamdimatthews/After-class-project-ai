import cv2
import mediapipe as mp
import pyautogui
import time
from math import hypot

# ==============================
# Configuration Parameters
# ==============================
SCROLL_SPEED = 300  # Positive for scroll up, negative for scroll down
SCROLL_DELAY = 1    # Delay in seconds between scrolls
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# ==============================
# Initialize MediaPipe Hands
# ==============================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# ==============================
# Gesture Detection Function
# ==============================
def detect_gesture(hand_landmarks, handedness):
    fingers = []
    finger_tips_ids = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]

    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

    for tip_id in finger_tips_ids:
        finger_tip = hand_landmarks.landmark[tip_id]
        finger_pip = hand_landmarks.landmark[tip_id - 2]
        if finger_tip.y < finger_pip.y:
            fingers.append(1)
        else:
            fingers.append(0)

    if handedness == 'Right':
        fingers.append(1 if thumb_tip.x > thumb_ip.x else 0)
    else:
        fingers.append(1 if thumb_tip.x < thumb_ip.x else 0)

    total_fingers = fingers.count(1)

    if total_fingers == 5:
        return "scroll_up"
    elif total_fingers == 0:
        return "scroll_down"
    else:
        return "none"

# ==============================
# Main Function
# ==============================
def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    pTime = 0
    last_scroll_time = 0

    print("Hand Gesture Scroll Control is running...")
    print("Show an open palm to scroll up.")
    print("Make a fist to scroll down.")
    print("Press 'q' to exit.")

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to grab frame.")
            break

        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        gesture = "none"
        handedness = "Unknown"

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                handedness_label = hand_info.classification[0].label
                handedness = handedness_label

                mp_draw.draw_landmarks(
                    img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2)
                )

                gesture = detect_gesture(hand_landmarks, handedness)
                current_time = time.time()

                if gesture == "scroll_up" and (current_time - last_scroll_time) > SCROLL_DELAY:
                    pyautogui.scroll(SCROLL_SPEED)
                    last_scroll_time = current_time
                elif gesture == "scroll_down" and (current_time - last_scroll_time) > SCROLL_DELAY:
                    pyautogui.scroll(-SCROLL_SPEED)
                    last_scroll_time = current_time

        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime

        cv2.putText(img, f'Gesture: {gesture}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(img, f'FPS: {int(fps)}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(img, f'Hand: {handedness}', (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Hand Gesture Scroll Control", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()