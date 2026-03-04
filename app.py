import tkinter as tk
from tkinter import messagebox
import platform
import sys

def show_info():
    info = (
        f"OS : {platform.system()} {platform.release()}\n"
        f"Architecture : {platform.machine()}\n"
        f"Python : {sys.version.split()[0]}"
    )
    messagebox.showinfo("Infos système", info)

def main():
    root = tk.Tk()
    root.title("Test App - PyInstaller")
    root.geometry("300x200")
    root.resizable(False, False)

    # Couleur de fond
    root.configure(bg="#1e1e2e")

    label = tk.Label(
        root,
        text="🚀 Test PyInstaller",
        font=("Helvetica", 16, "bold"),
        bg="#1e1e2e",
        fg="#cdd6f4"
    )
    label.pack(pady=30)

    btn = tk.Button(
        root,
        text="Voir les infos système",
        command=show_info,
        font=("Helvetica", 12),
        bg="#89b4fa",
        fg="#1e1e2e",
        relief="flat",
        padx=10,
        pady=6,
        cursor="hand2"
    )
    btn.pack(pady=10)

    btn_quit = tk.Button(
        root,
        text="Quitter",
        command=root.destroy,
        font=("Helvetica", 10),
        bg="#f38ba8",
        fg="#1e1e2e",
        relief="flat",
        padx=10,
        pady=4,
        cursor="hand2"
    )
    btn_quit.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
