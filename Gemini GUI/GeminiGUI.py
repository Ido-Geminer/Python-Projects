import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
import google.generativeai as genai

class ChatGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.context = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Chat with Gemini')
        self.setGeometry(200, 200, 800, 400)

        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setFontPointSize(14)
        self.chat_input = QLineEdit()
        self.send_button = QPushButton('Send')
        self.status_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.chat_history)
        layout.addWidget(self.chat_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        self.status_label.setText("Sending message...")
        self.repaint()  # Force the label to update

        # model setup
        genai.configure(api_key="")
        model = genai.GenerativeModel("gemini-pro")

        message = self.chat_input.text()
        prompt = message if self.context is None else f"{self.context}\n{message}"
        self.chat_history.append(f"You: {message}\n")
        self.chat_input.clear()
        self.repaint()  # Force the label to update

        try:
            # send prompt and receive message
            response = model.generate_content(prompt)
            self.status_label.setText("Response received.")
            self.repaint()  # Force the label to update
            self.chat_history.append(f"Gemini: {response.text}\n")
            # Update context
            self.context = f"{self.context}\n{response.text}" if self.context else response.text
        except Exception as error_in_response:
            self.status_label.setText(f"Error: {error_in_response}")
            self.repaint()  # Force the label to update

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ChatGUI()
    sys.exit(app.exec_())
