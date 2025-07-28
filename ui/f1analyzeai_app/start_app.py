"start_app.py"
import subprocess
import os


def main():
    """Start the Streamlit app for F1 Analyze AI."""
    os.chdir("src/f1analyzeai_app")
    subprocess.run(["streamlit", "run", "app.py"], check=True)
