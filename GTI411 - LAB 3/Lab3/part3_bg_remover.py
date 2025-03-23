import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

class LiveBackgroundProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.cap = None
        self.custom_background = None
        self.is_capturing = False
        self.current_mode = "normal"
        
        self.init_ui()
        
        self.setup_camera()
        
    def init_ui(self):
        self.setWindowTitle("bg_remover")
        self.setGeometry(100, 100, 800, 600)
        
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.video_label)
        
        button_layout = QHBoxLayout()
        
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
        
        button_layout.addWidget(self.normal_mode_btn)
        button_layout.addWidget(self.subtract_mode_btn)
        button_layout.addWidget(self.blur_mode_btn)
        button_layout.addWidget(self.replace_mode_btn)
        button_layout.addWidget(self.load_custom_bg_btn)
        
        main_layout.addLayout(button_layout)
        
        self.status_label = QLabel("Status: Ready")
        main_layout.addWidget(self.status_label)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        
    def setup_camera(self):
        self.cap = cv2.VideoCapture(4)
        
        self.is_capturing = True
        self.timer.start(30)
    
    def load_custom_background(self):
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
        
        ret, frame = self.cap.read()
        if not ret:
            self.status_label.setText("Error: Could not read frame from camera")
            return
        
        frame = cv2.flip(frame, 1)
        
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
        
        rgb_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        q_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)

        self.video_label.setPixmap(pixmap.scaled(self.video_label.width(), self.video_label.height(), Qt.KeepAspectRatio))
    
    def get_foreground_mask_edge_based(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Image cleaning with filters + dilatation...
        blurred_gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred_gray, 50, 150)
        dilated_edges = cv2.dilate(edges, np.ones((5, 5), np.uint8), iterations=3)
        
        #Mask creation
        h, w = dilated_edges.shape
        mask = dilated_edges.copy()
        mask_fill = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(mask, mask_fill, (0, 0), 255)
        mask_inv = cv2.bitwise_not(mask)
        
        #Mask cleaning
        kernel = np.ones((5, 5), np.uint8)
        mask_inv = cv2.morphologyEx(mask_inv, cv2.MORPH_OPEN, kernel, iterations=1)
        mask_inv = cv2.morphologyEx(mask_inv, cv2.MORPH_CLOSE, kernel, iterations=2)
        
        return mask_inv
    
    def subtract_background_live(self, frame):
        fg_mask = self.get_foreground_mask_edge_based(frame)
        
        mask_3ch = cv2.cvtColor(fg_mask, cv2.COLOR_GRAY2BGR)
        white_bg = np.ones_like(frame) * 255
        
        person = cv2.bitwise_and(frame, frame, mask=fg_mask)
        
        bg_mask = cv2.bitwise_not(fg_mask)
        white_part = cv2.bitwise_and(white_bg, white_bg, mask=bg_mask)

        result = cv2.add(person, white_part)
        
        return result
    
    def blur_background_live(self, frame):
        fg_mask = self.get_foreground_mask_edge_based(frame)
        
        blurred_frame = cv2.GaussianBlur(frame, (35, 35), 0)
        person = cv2.bitwise_and(frame, frame, mask=fg_mask)
        
        bg_mask = cv2.bitwise_not(fg_mask)
        blurred_bg = cv2.bitwise_and(blurred_frame, blurred_frame, mask=bg_mask)

        result = cv2.add(person, blurred_bg)
        
        return result
    
    def replace_background_live(self, frame):
        fg_mask = self.get_foreground_mask_edge_based(frame)
        custom_bg = cv2.resize(self.custom_background, (frame.shape[1], frame.shape[0]))
        
        person = cv2.bitwise_and(frame, frame, mask=fg_mask)
        
        bg_mask = cv2.bitwise_not(fg_mask)
        custom_bg_part = cv2.bitwise_and(custom_bg, custom_bg, mask=bg_mask)
        
        result = cv2.add(person, custom_bg_part)
        
        return result
    
    def closeEvent(self, event):
        if self.cap is not None:
            self.cap.release()
        self.timer.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveBackgroundProcessingApp()
    window.show()
    sys.exit(app.exec_())