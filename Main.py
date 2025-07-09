# Indian Sign Language (ISL) Translator - Hindi Output

import cv2
import mediapipe as mp
import numpy as np
from gtts import gTTS
import os
import time

# Gesture labels map - Customize with your dataset
GESTURE_MAP = {
    'hello': 'नमस्ते',
    'thank_you': 'धन्यवाद',
    'yes': 'हाँ',
    'no': 'नहीं',
    'i_love_you': 'मैं तुमसे प्यार करता हूँ'
}

# Load your trained model (placeholder here)
def load_model():
    # Replace with actual model load (e.g., tf.keras.models.load_model())
    return lambda landmarks: 'hello'  # Dummy output for testing

# Text to speech in Hindi
def speak_hindi(text):
    tts = gTTS(text=text, lang='hi')
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"start {filename}" if os.name == 'nt' else f"mpg123 {filename}")

# Extract features from landmarks (flattened array)
def extract_landmark_features(landmarks):
    return np.array([[lm.x, lm.y, lm.z] for lm in landmarks]).flatten()

# Main function
def main():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=1,
                           min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    model = load_model()
    prev_gesture = ""
    last_spoken = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                features = extract_landmark_features(hand_landmarks.landmark)
                gesture = model(features)

                if gesture != prev_gesture and time.time() - last_spoken > 2:
                    prev_gesture = gesture
                    hindi_text = GESTURE_MAP.get(gesture, "")
                    if hindi_text:
                        print(f"Gesture: {gesture} → Hindi: {hindi_text}")
                        speak_hindi(hindi_text)
                        last_spoken = time.time()

        cv2.imshow("ISL Translator", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()