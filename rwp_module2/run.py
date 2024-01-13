import os
import sys

import streamlit.web.cli as stcli

APP_FILE_NAME = "streamlit_app.py"


def start():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(src_dir, APP_FILE_NAME)
    execute_streamlit_app(app_path)


def execute_streamlit_app(file_path):
    try:
        print(f"Running streamlit app from {file_path}")
        sys.argv = ["streamlit", "run", file_path]
        sys.exit(stcli.main())

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")


if __name__ == "__main__":
    print("MAIN!")
    start()
