import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

class LiveBackgroundProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize variables
        self.cap = None
        self.custom_background = None
        self.is_capturing = False
        self.current_mode = "normal"  # Initial mode
        
        # Set up the UI
        self.init_ui()
        
        # Initialize camera
        self.setup_camera()
        
    def init_ui(self):
        # Main window setup
        self.setWindowTitle("Live Background Processing App")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Video display
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.video_label)
        
        # Button layout
        button_layout = QHBoxLayout()
        
        # Buttons
        self.normal_mode_btn = QPushButton("Normal Mode")
        self.normal_mode_btn.clicked.connect(lambda: self.set_mode("normal"))
        
        self.subtract_mode_btn = QPushButton("Background Subtraction")
        self.subtract_mode_btn.clicked.connect(lambda: self.set_mode("subtract"))
        
        self.blur_mode_btn = QPushButton("Blur Background")
        self.blur_mode_btn.clicked.connect(lambda: self.set_mode("blur"))
        
        self.replace_mode_btn = QPushButton("Replace Background")
        self.replace_mode_btn.clicked.connect(lambda: self.set_mode("replace"))
        
        self.load_custom_bg_btn = QPushButton("Load Custom Background")
        self.load_custom_bg_btn.clicked.connect(self.load_custom_background)
        
        # Add buttons to layout
        button_layout.addWidget(self.normal_mode_btn)
        button_layout.addWidget(self.subtract_mode_btn)
        button_layout.addWidget(self.blur_mode_btn)
        button_layout.addWidget(self.replace_mode_btn)
        button_layout.addWidget(self.load_custom_bg_btn)
        
        main_layout.addLayout(button_layout)
        
        # Status label
        self.status_label = QLabel("Status: Ready")
        main_layout.addWidget(self.status_label)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Timer for video update
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        
    def setup_camera(self):
        # Initialize the webcam
        self.cap = cv2.VideoCapture(4)  # Try 0 first, can be changed to other camera indices
        if not self.cap.isOpened():
            self.status_label.setText("Error: Could not open webcam at index 0, trying index 4...")
            # Try alternative camera index
            self.cap = cv2.VideoCapture(4)
            if not self.cap.isOpened():
                self.status_label.setText("Error: Could not open any webcam")
                return
        
        # Start the timer to update frames
        self.is_capturing = True
        self.timer.start(30)  # Update every 30ms (approx. 33 fps)
        
        # Try to load default background image
        try:
            bg_path = "new_background.png"
            self.custom_background = cv2.imread(bg_path)
            if self.custom_background is not None:
                self.status_label.setText(f"Loaded default background: {bg_path}")
            else:
                self.status_label.setText(f"Warning: Could not load default background from {bg_path}")
        except Exception as e:
            self.status_label.setText(f"Warning: {str(e)}")
    
    def load_custom_background(self):
        # Load custom background for replacement
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Custom Background Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            try:
                self.custom_background = cv2.imread(file_path)
                if self.custom_background is None:
                    self.status_label.setText("Error: Could not load custom background")
                else:
                    self.status_label.setText(f"Custom background loaded from: {file_path}")
            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")
    
    def set_mode(self, mode):
        self.current_mode = mode
        self.status_label.setText(f"Mode changed to: {mode}")
    
    def update_frame(self):
        if not self.is_capturing:
            return
        
        # Read frame from camera
        ret, frame = self.cap.read()
        if not ret:
            self.status_label.setText("Error: Could not read frame from camera")
            return
        
        # Flip the frame horizontally for more natural interaction
        frame = cv2.flip(frame, 1)
        
        # Process frame based on current mode
        if self.current_mode == "normal":
            processed_frame = frame
        elif self.current_mode == "subtract":
            processed_frame = self.subtract_background_live(frame)
        elif self.current_mode == "blur":
            processed_frame = self.blur_background_live(frame)
        elif self.current_mode == "replace":
            processed_frame = self.replace_background_live(frame)
        else:
            processed_frame = frame
        
        # Convert frame to QImage and display
        rgb_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        q_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.video_label.setPixmap(pixmap.scaled(self.video_label.width(), self.video_label.height(), Qt.KeepAspectRatio))
    
    def get_foreground_mask_edge_based(self, frame):
        """
        Creates a foreground mask using edge detection and flood fill method
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply slight blur to reduce noise
        blurred_gray = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Detect edges
        edges = cv2.Canny(blurred_gray, 50, 150)
        
        # Dilate edges to connect gaps
        dilated_edges = cv2.dilate(edges, np.ones((5, 5), np.uint8), iterations=3)
        
        # Create a mask using flood fill to get the full silhouette
        h, w = dilated_edges.shape
        mask = dilated_edges.copy()
        mask_fill = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(mask, mask_fill, (0, 0), 255)
        
        # Invert the mask (0 for foreground, 255 for background)
        mask_inv = cv2.bitwise_not(mask)
        
        # Apply morphological operations to clean up the mask
        kernel = np.ones((5, 5), np.uint8)
        mask_inv = cv2.morphologyEx(mask_inv, cv2.MORPH_OPEN, kernel, iterations=1)
        mask_inv = cv2.morphologyEx(mask_inv, cv2.MORPH_CLOSE, kernel, iterations=2)
        
        return mask_inv
    
    def subtract_background_live(self, frame):
        # Get foreground mask
        fg_mask = self.get_foreground_mask_edge_based(frame)
        
        # Convert to 3-channel for display
        mask_3ch = cv2.cvtColor(fg_mask, cv2.COLOR_GRAY2BGR)
        
        # Create a white background
        white_bg = np.ones_like(frame) * 255
        
        # Get foreground (person)
        person = cv2.bitwise_and(frame, frame, mask=fg_mask)
        
        # Get background (white) where the person is not
        bg_mask = cv2.bitwise_not(fg_mask)
        white_part = cv2.bitwise_and(white_bg, white_bg, mask=bg_mask)
        
        # Combine the person and white background
        result = cv2.add(person, white_part)
        
        return result
    
    def blur_background_live(self, frame):
        # Get foreground mask using edge detection
        fg_mask = self.get_foreground_mask_edge_based(frame)
        
        # Create a heavily blurred version of the entire frame
        blurred_frame = cv2.GaussianBlur(frame, (35, 35), 0)
        
        # Extract the person from the original frame
        person = cv2.bitwise_and(frame, frame, mask=fg_mask)
        
        # Extract the background from the blurred frame
        bg_mask = cv2.bitwise_not(fg_mask)
        blurred_bg = cv2.bitwise_and(blurred_frame, blurred_frame, mask=bg_mask)
        
        # Combine person and blurred background
        result = cv2.add(person, blurred_bg)
        
        return result
    
    def replace_background_live(self, frame):
        # Get foreground mask using edge detection
        fg_mask = self.get_foreground_mask_edge_based(frame)
        
        # Check if we have a custom background
        if self.custom_background is None:
            # Try to load the default background
            try:
                bg_path = "new_background.png"
                self.custom_background = cv2.imread(bg_path)
                if self.custom_background is None:
                    self.status_label.setText(f"Error: Could not load default background at {bg_path}")
                    return frame
            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")
                return frame
        
        # Resize custom background to match frame
        custom_bg = cv2.resize(self.custom_background, (frame.shape[1], frame.shape[0]))
        
        # Extract the person from the original frame
        person = cv2.bitwise_and(frame, frame, mask=fg_mask)
        
        # Extract the custom background where the person is not
        bg_mask = cv2.bitwise_not(fg_mask)
        custom_bg_part = cv2.bitwise_and(custom_bg, custom_bg, mask=bg_mask)
        
        # Combine person and custom background
        result = cv2.add(person, custom_bg_part)
        
        return result
    
    def closeEvent(self, event):
        # Clean up resources when closing
        if self.cap is not None:
            self.cap.release()
        self.timer.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveBackgroundProcessingApp()
    window.show()
    sys.exit(app.exec_())