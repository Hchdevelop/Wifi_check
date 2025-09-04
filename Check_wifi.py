# step1_show_netsh.py
import subprocess, locale

enc = locale.getpreferredencoding(False) or "utf-8"

try:
    p = subprocess.run(
        ["netsh", "wlan", "show", "interfaces"],
        capture_output=True, text=True
    )
    print(p.stdout if p.stdout else p.stderr)
except Exception as e:
    print(f"[ERREUR] Impossible d'exécuter netsh: {e}")
