# **Gesture-Based Volume Control**

A fun and interactive Python-based application that lets you control your system's volume using hand gestures. This project uses **Mediapipe** for hand tracking and **PyCaw** for audio control, creating an intuitive experience for managing volume levels without touching your keyboard or mouse.

---

## **Features**

- **Gesture-Based Control**:  
  Adjust volume by moving your thumb and index fingers closer or farther apart.
  
- **Dynamic Feedback**:  
  Real-time volume percentage display with a progress bar and text.

- **Gesture Toggle Mode**:  
  Enable or disable volume control gestures using a thumbs-up gesture.

- **Interactive UI**:  
  Visual feedback with glowing effects for better interactivity.

- **Real-Time Processing**:  
  Smooth volume adjustment and seamless hand tracking using Mediapipe.

---

## **Requirements**

1. **Python 3.x** (recommended 3.8 or later).  
2. **Camera**: A functional webcam for real-time hand tracking.  
3. **Dependencies**: Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Project Structure**

```plaintext
├── gesture_volume_control.py  # Main script
├── requirements.txt           # Required Python libraries
├── README.md                  # Project documentation
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/ssam246/Gesture-Based-Volume-Control.git
cd gesture-volume-control
```

### **2. Install Dependencies**
Install the required libraries using the following command:
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Launch the application by running:
```bash
python gesture_volume_control.py
```

---

## **How to Use**

1. **Launch the Application**:  
   Ensure your webcam is working and start the script. A window will open displaying the video feed.

2. **Control Volume**:  
   - Bring your **thumb and index finger** closer together to decrease the volume.  
   - Move your **thumb and index finger** farther apart to increase the volume.

3. **Toggle Gesture Control**:  
   - Show a **thumbs-up gesture** to enable or disable gesture-based volume control.  
   - The application will display the current mode:  
     - `Gesture Control: ON`  
     - `Gesture Control: OFF`

4. **Exit the Application**:  
   Press the `q` key to quit.

---

## **Example Workflow**

1. **Start the Script**:  
   Launch the application:
   ```bash
   python gesture_volume_control.py
   ```

2. **Adjust Volume**:  
   - Place your hand in front of the camera.  
   - Adjust the distance between your thumb and index finger to control the volume.  

3. **Toggle Mode**:  
   - Show a thumbs-up gesture to enable or disable gesture control.

4. **Exit**:  
   Press `q` to close the application.

---

## **Output Example**

- **Volume Control**:  
  - A progress bar appears on the left side of the window, indicating the current volume percentage.  
  - Real-time percentage feedback, e.g., `50%`.

- **Gesture Mode**:  
  - Status displayed at the top of the window: `Gesture Control: ON` or `OFF`.

- **Interactive Effects**:  
  - Glow around fingers when volume is at its lowest (close distance between thumb and index finger).

---

## **Troubleshooting**

1. **Camera Issues**:  
   - Ensure your webcam is functional and permissions are granted.  

2. **Laggy Performance**:  
   - Close unnecessary applications that may consume CPU or GPU resources.  
   - Reduce `min_detection_confidence` and `min_tracking_confidence` in the script for faster processing.

3. **Volume Control Not Working**:  
   - Check if `PyCaw` is properly installed and compatible with your audio setup.  
   - Ensure the script has permission to access the audio system.

---

## **Future Improvements**

- Add support for **multi-hand gestures** for more advanced controls.  
- Integrate gesture-based **mute/unmute** functionality.  
- Provide support for **custom gesture mapping** through a configuration file.

---

## **Disclaimer**

This project is intended for **educational purposes** and is provided as-is. Ensure proper usage and permissions when using this application.

---

### **Made with 💻 and 🎶 by Stephen Sam**
