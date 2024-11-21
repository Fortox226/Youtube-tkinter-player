import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Wszystkie wymagane biblioteki zostały zainstalowane!")
    except subprocess.CalledProcessError as e:
        print(f"Błąd podczas instalacji zależności: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
