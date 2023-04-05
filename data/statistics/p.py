import csv
import sys
from PyQt6.QtCore import Qt, QFile
from PyQt6.QtGui import QTextDocument
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle("Football Game")

        with open('prediction_result.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                game_date, home_team, away_team, home_score, away_score, result, home_shots, away_shots, shots_diff = row
                game_info = f"{game_date}: {home_team} vs {away_team}, Score: {home_score}-{away_score}, Result: {result}, Shots: {home_shots}-{away_shots}, Shots Difference: {shots_diff}"
                self.textEdit.append(game_info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

