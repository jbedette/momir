import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit
)
from PyQt5.QtCore import Qt

class BluetoothManagerApp(QWidget):
    def __init__(self, connection_status):
        super().__init__()
        self.connection_status = connection_status
        self.init_ui()

    def init_ui(self):
        # Set up main layout
        main_layout = QVBoxLayout(self)

        # Header for connection status
        self.status_label = QLabel(f"Connection Status: {self.connection_status}")
        self.status_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Display area for logs/output
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        main_layout.addWidget(self.output_display)

        # Input field for device address
        self.device_input = QLineEdit()
        self.device_input.setPlaceholderText("Enter Device Address")
        main_layout.addWidget(self.device_input)

        # Buttons for Bluetooth actions
        button_layout = QHBoxLayout()

        discover_button = QPushButton("Discover Devices")
        discover_button.clicked.connect(self.discover_devices)
        button_layout.addWidget(discover_button)

        pair_button = QPushButton("Pair Device")
        pair_button.clicked.connect(self.pair_device)
        button_layout.addWidget(pair_button)

        connect_button = QPushButton("Connect Device")
        connect_button.clicked.connect(self.connect_device)
        button_layout.addWidget(connect_button)

        main_layout.addLayout(button_layout)

        self.setWindowTitle("Bluetooth Manager")
        self.resize(600, 400)

    def run_bluetoothctl_command(self, command):
        """Run a bluetoothctl command and return the output."""
        try:
            process = subprocess.Popen(
                ["bluetoothctl"] + command.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            output, error = process.communicate()
            if error:
                self.output_display.append(f"Error: {error.decode().strip()}")
            return output.decode().strip()
        except Exception as e:
            self.output_display.append(f"Exception: {str(e)}")
            return ""

    def discover_devices(self):
        """Discover available Bluetooth devices."""
        self.output_display.append("Discovering devices...")
        output = self.run_bluetoothctl_command("devices")
        self.output_display.append(output)

    def pair_device(self):
        """Pair with a specified Bluetooth device."""
        device_address = self.device_input.text().strip()
        if not device_address:
            self.output_display.append("Please enter a device address.")
            return

        self.output_display.append(f"Pairing with {device_address}...")
        output = self.run_bluetoothctl_command(f"pair {device_address}")
        self.output_display.append(output)

    def connect_device(self):
        """Connect to a specified Bluetooth device."""
        device_address = self.device_input.text().strip()
        if not device_address:
            self.output_display.append("Please enter a device address.")
            return

        self.output_display.append(f"Connecting to {device_address}...")
        try:
            process = subprocess.Popen(
                ["sudo", "rfcomm", "connect", "0", device_address],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            output, error = process.communicate()
            if output:
                self.output_display.append(output.decode().strip())
            if error:
                self.output_display.append(f"Error: {error.decode().strip()}")
        except Exception as e:
            self.output_display.append(f"Exception: {str(e)}")


def initialize_bluetooth_connection():
    """Run bluetoothctl commands to pair and connect."""
    try:
        subprocess.run(["bluetoothctl", "power", "on"], check=True)
        subprocess.run(["bluetoothctl", "agent", "on"], check=True)
        subprocess.run(["bluetoothctl", "default-agent"], check=True)
        print("Bluetooth initialized. Waiting for pairing and connection.")
        return "Initialized, Awaiting Connection"
    except subprocess.CalledProcessError as e:
        print(f"Error initializing Bluetooth: {e}")
        return "Error during Initialization"


if __name__ == "__main__":
    connection_status = initialize_bluetooth_connection()
    app = QApplication(sys.argv)
    window = BluetoothManagerApp(connection_status)
    window.show()
    sys.exit(app.exec_())
