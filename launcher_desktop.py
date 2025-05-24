#!/usr/bin/env python3
import sys
import subprocess
import pathlib
import os
import PySimpleGUI as sg

SCRIPTS = [
    ("skrypt_1.py", "success"),
    ("skrypt_2.py", "success"),
    ("skrypt_3.py", "fail"),
    ("skrypt_4.py", "success"),
    ("skrypt_5.py", "success"),
]

def run_script(file, arg):
    """Starts script and returns (exit_code, stdout+stderr)."""
    result = subprocess.run(
        [sys.executable, file, arg],
        text=True,
        capture_output=True
    )
    return result.returncode, result.stdout + result.stderr

def main():
    sg.theme("DarkBlue3")
    layout = [
        [sg.Text("Tasks queue:"), sg.Listbox(values=[f"{f} {a}" for f, a in SCRIPTS],
                                               size=(30,5), disabled=True, key="-LIST-")],
        [sg.Multiline(size=(80,20), key="-LOG-")],
        [sg.Button("Start"), sg.Button("Close")]
    ]
    window = sg.Window("Launcher – workflow 5 scripts", layout, finalize=True)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, "Close"):
            break
        if event == "Start":
            window["-LOG-"].update("")
            for idx, (fname, arg) in enumerate(SCRIPTS, start=1):
                window["-LOG-"].print(f"\n ({idx}/5) {fname} {arg}")
                code, output = run_script(fname, arg)
                window["-LOG-"].print(output)
                if code == 0:
                    window["-LOG-"].print("Finished with success\n")
                else:
                    window["-LOG-"].print(f"Error (code {code}) – stopping pipeline")
                    break
            window["-LOG-"].print("\n--- End ---")
    window.close()

if __name__ == "__main__":
    # Ścieżka robocza = folder, w którym leży launcher,
    # dzięki czemu relative paths działają po dwukliku
    os.chdir(pathlib.Path(__file__).parent)
    main()