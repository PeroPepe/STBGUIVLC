from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
import vlc

class STB_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STB Interface")
        self.setGeometry(0, 0, 1280, 720)  # Adjust for your screen
        self.setWindowFlags(Qt.FramelessWindowHint)  # Fullscreen
        self.setCursor(QCursor(Qt.BlankCursor))  # Hide cursor

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        layout = QVBoxLayout()
        self.play_button = QPushButton("Play IPTV Channel 1")
        self.play_button.clicked.connect(self.play_stream)
        layout.addWidget(self.play_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def play_stream(self):
        media = self.instance.media_new("http://your-iptv-url")
        self.player.set_media(media)
        self.player.play()

app = QApplication([])
window = STB_UI()
window.showFullScreen()
app.exec_()
