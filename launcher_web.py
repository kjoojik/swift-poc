#!/usr/bin/env python3
import os
import subprocess, sys, pathlib, time, streamlit as st

# --- KONFIGURACJA -----------------------------------------------------------
SCRIPTS = [
    ("skrypt_1.py", "success"),
    ("skrypt_2.py", "success"),
    ("skrypt_3.py", "success"),
    ("skrypt_4.py", "success"),
    ("skrypt_5.py", "success"),
]
# ---------------------------------------------------------------------------

# praca na katalogu, w którym leży launcher  → względne ścieżki działają po dwukliku
os.chdir(pathlib.Path(__file__).parent)

st.set_page_config(page_title="Launcher 5 skryptów", layout="wide")
st.title("Launcher – workflow 5 skryptów")

start = st.button("▶ Start pipeline")
log_box = st.empty()            # placeholder na log w czasie rzeczywistym
status = st.empty()             # aktualny etap / koniec

def run_script(file, arg):
    """Zwraca (kod_wyjścia, stdout+stderr)."""
    res = subprocess.run(
        [sys.executable, file, arg],
        text=True,
        capture_output=True
    )
    return res.returncode, res.stdout + res.stderr

if start:
    log = []
    for idx, (fname, arg) in enumerate(SCRIPTS, start=1):
        status.info(f"Uruchamiam ({idx}/{len(SCRIPTS)}) **{fname} {arg}** …")
        code, output = run_script(fname, arg)

        log.append(f"\n▶ ({idx}/{len(SCRIPTS)}) {fname} {arg}")
        log.append(output)

        if code == 0:
            log.append("✔ Sukces\n")
            log_box.text("\n".join(log))
        else:
            log.append(f"❌ Błąd (kod {code}) – zatrzymuję pipeline\n")
            log_box.text("\n".join(log))
            status.error("Pipeline przerwany")
            break

        # wizualne „oddechy” między skryptami
        time.sleep(0.2)

    else:   # pętla nie przerwana -> wszystkie sukcesy
        status.success("🎉 Wszystkie skrypty zakończone sukcesem!")

    log_box.text("\n".join(log))
