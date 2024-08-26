from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import subprocess
import platform
import sys
import os

app = Flask(__name__)
CORS(app)  # Initialize CORS for the app

@app.route('/', methods=['GET'])
def launch_browser():
    try:
        # Optionally add to startup (platform-specific)
        if platform.system() == 'Windows':
            add_to_startup()

        # Launch the PyQt5 GUI application as a separate process
        subprocess.Popen(['python', 'launch_browser_gui.py'])

        return jsonify({"status": "Browser launched successfully!"})
    except Exception as e:
        return jsonify({"status": "Failed to launch browser.", "error": str(e)}), 500

def add_to_startup():
    if platform.system() == 'Windows':
        import winreg as reg
        exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.realpath(__file__)
        key = reg.HKEY_CURRENT_USER
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

        with reg.OpenKey(key, key_path, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, "BlockerApp", 0, reg.REG_SZ, exe_path)

if __name__ == '__main__':
    app.run(debug=True)
