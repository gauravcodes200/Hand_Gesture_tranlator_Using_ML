# 🇮🇳 Indian Sign Language (ISL) to Hindi Translator
<b>
<br>
A Deep Learning-based project that translates Indian Sign Language hand gestures into **Hindi text and speech** using **MediaPipe**, a trained classifier, and **gTTS** for Hindi voice output. This tool aims to assist speech- and hearing-impaired individuals in daily communication.<br>

---

## 📌 Features<br>

- 🔍 Real-time hand gesture detection using **MediaPipe Hands**<br>
- 🧠 Gesture classification using a trained Deep Learning model (CNN/RNN)<br>
- 📝 Output translated Hindi text<br>
- 🔊 Hindi speech using **gTTS (Google Text-to-Speech)**<br>
- 💡 High societal impact and practical utility<br>

---

## 🏗️ Architecture<br>
[Camera Input] → [MediaPipe Hand Tracker] → [Gesture Classifier] → [Hindi Text] → [Hindi Speech Output]<br>


---

## 🛠️ Installation<br>

### 1. Clone the Repository<br>

```bash
git clone https://github.com/your-username/isl-hindi-translator.git<br>
cd isl-hindi-translator<br>
```

📦 Requirements<br>
Python 3.8+ <br>
OpenCV<br>
MediaPipe<br>
NumPy<br>
gTTS<br>

🚀 Run the Translator<br>
```
bash
python3 Main.py
```
<br>
Press Q to exit the webcam stream.<br>
Ensure you're in a well-lit environment.<br>

🔧 How it Works<br>
MediaPipe detects 21 landmarks of the hand.<br>
The landmarks are flattened into a feature vector.<br>
A pre-trained model predicts the gesture class.<br>
The label is mapped to a Hindi sentence.<br>
gTTS converts Hindi text into spoken audio.<br>

🧠 Model Training<br>
Model loading is mocked for now. You must:<br>
Prepare a dataset of labeled ISL gestures (images or keypoints).<br>
Train a CNN or LSTM model on the data.<br>
Save and load the model in load_model() function.<br>

<h1>Output</h1>
</b>

https://github.com/user-attachments/assets/e884d067-c5c5-4279-8d83-782ca3ea180d
