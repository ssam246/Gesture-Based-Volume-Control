# **Gesture-Based Volume Control**

A fun, innovative, and interactive Python-based application that allows you to control your system's volume using hand gestures. This project leverages **Mediapipe** for hand tracking and **PyCaw** for audio control, enabling a touch-free way to adjust volume levels. Perfect for tech enthusiasts, musicians, and anyone looking for a modern, hands-on (or hands-off!) approach to controlling their audio.

![image](https://github.com/user-attachments/assets/fffcc13a-a38e-4c92-b6fa-b8c8d23e0cf7)

---

## **Features**

### **Gesture-Based Control**
Adjust the volume intuitively:
- Move your **thumb and index fingers closer together** to decrease the volume.
- Move your **thumb and index fingers farther apart** to increase the volume.

### **Dynamic Feedback**
- Real-time volume percentage displayed as:
  - A vertical progress bar.
  - A textual percentage.

### **Gesture Toggle Mode**
- Enable or disable gesture-based volume control using a **thumbs-up gesture**.
- Visual feedback shows whether gesture control is `ON` or `OFF`.

### **Interactive UI**
- Visual markers and glowing effects for enhanced interactivity.
- A responsive design ensures smooth hand tracking.

### **Real-Time Processing**
- Powered by Mediapipe for accurate and seamless hand tracking.
- Provides a natural and lag-free user experience.

---

## **Requirements**

### **Hardware**
- A functional webcam for real-time video capture.

### **Software**
1. **Python 3.x** (3.8 or later recommended).
2. Install the following Python libraries:
   - `opencv-python`
   - `mediapipe`
   - `numpy`
   - `pycaw`
   - `comtypes`

### **Install Dependencies**
Run the following command to install all dependencies:
```bash
pip install -r requirements.txt
```

---

## **Project Structure**

```plaintext
├── gesture_volume_control.py  # Main script
├── requirements.txt           # Required Python libraries
├── README.md                  # Documentation
```

---

## **Setup Instructions**

### **1. Clone the Repository**
Download the project files from GitHub:
```bash
git clone https://github.com/ssam246/Gesture-Based-Volume-Control.git
cd gesture-volume-control
```

### **2. Install Dependencies**
Install the required libraries:
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Start the application:
```bash
python gesture_volume_control.py
```

---

## **How to Use**

1. **Launch the Application**:
   - Ensure your webcam is functional and accessible.
   - Run the script to start the video feed.

2. **Control Volume**:
   - Place your **thumb and index finger** in view of the camera.
   - Adjust the distance between them to:
     - **Decrease volume**: Bring fingers closer together.
     - **Increase volume**: Move fingers farther apart.

3. **Toggle Gesture Control**:
   - Show a **thumbs-up gesture** to enable or disable volume control gestures.
   - The screen will display:
     - `Gesture Control: ON`  
     - `Gesture Control: OFF`

4. **Exit the Application**:
   - Press `q` to close the application.

---

## **Example Workflow**

1. **Launch the Application**:
   Start the program:
   ```bash
   python gesture_volume_control.py
   ```

2. **Adjust Volume**:
   - Hold your hand in front of the camera.
   - Use your thumb and index finger to control the volume level.

3. **Toggle Gesture Mode**:
   - Use a thumbs-up gesture to turn gesture control on or off.

4. **Exit**:
   Press `q` to quit.

---

## **Output Example**

### **Volume Control Visualization**
- **Progress Bar**:
  - The vertical bar on the left side of the screen dynamically updates with volume levels.
- **Percentage Display**:
  - Volume percentage is shown at the bottom of the bar (e.g., `50%`).

### **Gesture Mode Feedback**
- `Gesture Control: ON` or `OFF` is displayed at the top of the screen.

### **Interactive Effects**
- **Glow Effect**:
  - A glowing effect highlights the thumb and index finger when they are close (indicating low volume).

---

## **Troubleshooting**

1. **Camera Not Detected**:
   - Ensure your webcam is functional and permissions are granted.

2. **Laggy Performance**:
   - Close other resource-heavy applications to free up CPU and GPU resources.
   - Reduce `min_detection_confidence` and `min_tracking_confidence` values in the script for faster processing.

3. **Volume Control Not Working**:
   - Check if the `pycaw` library is correctly installed and your system's audio device supports it.

4. **Gesture Control Toggle Not Responding**:
   - Ensure the thumbs-up gesture is clearly visible in the video feed.

---

## **Future Improvements**

- **Multi-Gesture Support**:
  - Add more gestures for features like muting, unmuting, and skipping tracks.

- **Custom Gesture Mapping**:
  - Allow users to define and configure gestures for specific actions.

- **Support for Multiple Hands**:
  - Add functionality for dual-hand gestures.

- **GUI Enhancements**:
  - Include a configuration panel for adjusting tracking sensitivity and gestures.

---

## **Disclaimer**

This project is intended for **educational and personal use only**.  
Ensure proper permissions and compliance with local laws when using this application.

---

### **Acknowledgments**

- **Mediapipe**: For providing robust and efficient hand tracking.
- **PyCaw**: For simplifying audio control integration.

---

### **Made with 💻, 🤖, and 🎶 by Stephen Sam**
