import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import momir


class IntegerImageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up main layout
        main_layout = QHBoxLayout(self)

        # Left layout for integer display, buttons, and submit button
        left_layout = QVBoxLayout()
        self.integer_label = QLabel("1")
        self.integer_label.setStyleSheet("font-size: 40px;")
        self.integer_label.setAlignment(Qt.AlignCenter)

        increment_button = QPushButton("Increment")
        increment_button.setStyleSheet("font-size: 24px;")
        increment_button.clicked.connect(self.increment_integer)

        decrement_button = QPushButton("Decrement")
        decrement_button.setStyleSheet("font-size: 24px;")
        decrement_button.clicked.connect(self.decrement_integer)

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("font-size: 24px;")
        submit_button.clicked.connect(self.on_submit)

        # Add widgets to the left layout
        left_layout.addWidget(self.integer_label)
        left_layout.addWidget(increment_button)
        left_layout.addWidget(decrement_button)
        left_layout.addWidget(submit_button)

        # Right layout for the image
        right_layout = QVBoxLayout()
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("sample.jpg"))  # Initial sample image
        self.image_label.setScaledContents(True)
        right_layout.addWidget(self.image_label)

        # Add both layouts to the main layout
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setWindowTitle("Integer Image App")
        self.resize(800, 400)

    def increment_integer(self):
        current_value = int(self.integer_label.text())
        if current_value < 16:  # Limit to 16
            current_value += 1
            self.integer_label.setText(str(current_value))

    def decrement_integer(self):
        current_value = int(self.integer_label.text())
        if current_value > 1:  # Limit to 1
            current_value -= 1
            self.integer_label.setText(str(current_value))

    def on_submit(self):
        current_value = self.integer_label.text()
        # Call the external function to get a new image path
        new_image_path = self.handle_submission(current_value)
        # Update the image on the right side
        self.image_label.setPixmap(QPixmap(new_image_path))

    def handle_submission(self, value):
        # Example function to handle submission and return an image path
        print(f"Submitted value: {value}")
        # Replace this logic with your custom logic to return the appropriate image
        # For this example, images are named '1.jpg', '2.jpg', etc.
        return momir.gui_momir(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IntegerImageApp()
    window.show()
    sys.exit(app.exec_())
