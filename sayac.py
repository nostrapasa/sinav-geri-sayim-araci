#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer, Qt, QSize

class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Geri Sayım Aracı')
        self.setGeometry(200, 200, 800, 300)
        self.setStyleSheet("background-color: #f0f0f0;")  # Arka plan rengini açık gri yaptık

        self.layout = QVBoxLayout()

        # Dakika giriş metin kutusu
        self.minute_layout = QHBoxLayout()
        self.minute_label = QLabel('Dakika:', self)
        self.minute_label.setStyleSheet("color: #0000ff; font-size: 48px;")  # Metin rengini mavi yaptık, font boyutunu 48'e çıkardık
        self.minute_layout.addWidget(self.minute_label)

        self.minute_input = QLineEdit(self)
        self.minute_input.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")  # Arka plan ve metin rengini beyaz, font boyutunu 48'e çıkardık, köşeleri yuvarladık
        self.minute_layout.addWidget(self.minute_input)

        self.layout.addLayout(self.minute_layout)

        # Hazır dakika butonları
        self.button_layout = QHBoxLayout()

        self.button_165 = QPushButton('TYT', self)
        self.button_165.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")  # Arka plan ve metin rengini beyaz yaptık, font boyutunu 48'e çıkardık, köşeleri yuvarladık
        self.button_165.clicked.connect(lambda: self.start_countdown(165, 'TYT SINAVI'))
        self.button_layout.addWidget(self.button_165)

        self.button_180 = QPushButton('AYT', self)
        self.button_180.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")
        self.button_180.clicked.connect(lambda: self.start_countdown(180, 'AYT SINAVI'))
        self.button_layout.addWidget(self.button_180)

        self.button_120 = QPushButton('YDS', self)
        self.button_120.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")
        self.button_120.clicked.connect(lambda: self.start_countdown(120, 'YDS SINAVI'))
        self.button_layout.addWidget(self.button_120)

        self.button_lgs1 = QPushButton('LGS1', self)  # LGS butonunu LGS1 olarak değiştirdik
        self.button_lgs1.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")
        self.button_lgs1.clicked.connect(lambda: self.start_countdown(75, 'LGS1 SINAVI'))  # Süreyi 75 dakika olarak ayarladık
        self.button_layout.addWidget(self.button_lgs1)

        self.button_lgs2 = QPushButton('LGS2', self)  # Yeni LGS2 butonunu ekledik
        self.button_lgs2.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")
        self.button_lgs2.clicked.connect(lambda: self.start_countdown(80, 'LGS2 SINAVI'))  # Süreyi 80 dakika olarak ayarladık
        self.button_layout.addWidget(self.button_lgs2)

        self.button_40 = QPushButton('YAZILI SINAV', self)  # Etiketi "YAZILI SINAV" olarak değiştirildi
        self.button_40.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")
        self.button_40.clicked.connect(lambda: self.start_countdown(40, 'Yazılı SINAV'))
        self.button_layout.addWidget(self.button_40)

        self.layout.addLayout(self.button_layout)

        self.start_button = QPushButton('Başlat', self)
        self.start_button.setStyleSheet("background-color: #ffffff; color: #0000ff; border-radius: 5px; font-size: 48px;")
        self.start_button.clicked.connect(self.start_custom_countdown)
        self.layout.addWidget(self.start_button)

        # Geri sayım label'ı
        self.countdown_layout = QVBoxLayout()
        self.countdown_layout.setAlignment(Qt.AlignCenter)  # Label'ı ortaladık

        self.countdown_label = QLabel('', self)
        self.countdown_label.setAlignment(Qt.AlignCenter)
        self.countdown_label.setStyleSheet("color: #0000ff; font-size: 250px; font-weight: bold;")  # Yazı rengini mavi, büyük ve kalın yaptık
        self.countdown_layout.addWidget(self.countdown_label)

        self.layout.addLayout(self.countdown_layout)

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)

        self.remaining_time = 0

    def start_countdown(self, minutes, message):
        self.remaining_time = minutes * 60
        self.timer.start(1000)
        self.countdown_label.setText('')
        self.layout.update()  # Layout'u güncelledik

    def start_custom_countdown(self):
        try:
            minutes = int(self.minute_input.text())
            self.remaining_time = minutes * 60
            self.timer.start(1000)
        except ValueError:
            QMessageBox.critical(self, 'Hata', 'Geçersiz giriş. Lütfen bir sayı girin.')

    def update_countdown(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.timer.stop()
            self.countdown_label.setText('Süre Bitti.')
        else:
            hours = self.remaining_time // 3600
            minutes = (self.remaining_time % 3600) // 60
            seconds = self.remaining_time % 60
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.countdown_label.setText(time_str)

    def sizeHint(self):
        return QSize(800, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    countdown_app = CountdownApp()
    countdown_app.show()
    sys.exit(app.exec_())

