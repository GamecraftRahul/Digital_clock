
import mysql.connector
from datetime import datetime
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import random

# ---------------------- DATABASE CONFIG ----------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'RAHUL123',
    'database': 'digital_clock_db'
}

# ---------------------- DATABASE FUNCTIONS ------------------
def get_all_users():
    try:
        with mysql.connector.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT username FROM settings")
                return [row[0] for row in cursor.fetchall()]
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return []

def get_user_settings(username):
    try:
        with mysql.connector.connect(**DB_CONFIG) as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM settings WHERE username=%s", (username,))
                return cursor.fetchone()
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
        return None

# ---------------------- MAIN APPLICATION --------------------
class DigitalClockApp(tb.Window):
    def __init__(self):
        super().__init__(title="🕒 Digital Clock", themename="darkly")
        self.geometry("520x350")
        self.resizable(False, False)

        self.app_style = tb.Style("darkly")
        self.selected_user = tb.StringVar()
        self.user_data = None
        self.running = False  # clock loop control

        self.create_user_selector()

    # ---------------------- USER SELECTION ----------------------
    def create_user_selector(self):
        self.clear_widgets()
        tb.Label(self, text="Select User", font=("Helvetica", 14, "bold")).pack(pady=20)

        users = get_all_users()
        if not users:
            messagebox.showerror("Error", "No users found in database!")
            self.destroy()
            return

        user_combo = tb.Combobox(self, textvariable=self.selected_user, values=users,
                                 state="readonly", font=("Helvetica", 12))
        user_combo.pack(pady=10)
        user_combo.current(0)

        tb.Button(self, text="Load Settings", command=self.load_user,
                  bootstyle="info-outline").pack(pady=15)

    # ---------------------- LOAD USER SETTINGS ------------------
    def load_user(self):
        username = self.selected_user.get()
        self.user_data = get_user_settings(username)
        if not self.user_data:
            messagebox.showerror("Error", "Failed to load user settings.")
            return

        self.app_style.theme_use(self.user_data['theme'])
        self.build_clock_ui()

    # ---------------------- BUILD CLOCK UI ---------------------
    def build_clock_ui(self):
        self.clear_widgets()
        self.username = self.user_data['username']
        self.time_format = self.user_data['time_format']
        self.city = self.user_data['city']

        tb.Label(self, text=f"Welcome, {self.username}", font=("Helvetica", 16, "bold")).pack(pady=10)
        self.time_label = tb.Label(self, text="", font=("ds-digital", 60, "bold"), bootstyle="info")
        self.time_label.pack(pady=20)

        tb.Label(self, text=f"📍 City: {self.city}", font=("Helvetica", 14)).pack(pady=5)

        tb.Button(self, text="Change Theme", command=self.change_theme, bootstyle="warning-outline").pack(pady=5)
        tb.Button(self, text="Switch User", command=self.reset_to_selector, bootstyle="secondary-outline").pack(pady=5)
        tb.Button(self, text="Exit", command=self.destroy, bootstyle="danger").pack(pady=10)

        self.running = True
        self.update_time()

    # ---------------------- UPDATE CLOCK ----------------------
    def update_time(self):
        if not self.running:
            return

        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p") if self.time_format == "12hr" else now.strftime("%H:%M:%S")
        if hasattr(self, 'time_label') and self.time_label.winfo_exists():
            self.time_label.config(text=current_time)
            self.after(1000, self.update_time)
        else:
            self.running = False

    # ---------------------- CHANGE THEME ----------------------
    def change_theme(self):
        themes = ["darkly", "superhero", "flatly", "cosmo", "cyborg", "journal", "minty"]
        new_theme = random.choice(themes)
        self.app_style.theme_use(new_theme)
        messagebox.showinfo("Theme Changed", f"Theme changed to {new_theme}!")

    # ---------------------- SWITCH USER ------------------------
    def reset_to_selector(self):
        self.running = False
        self.create_user_selector()

    # ---------------------- HELPER FUNCTION -------------------
    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

# ---------------------- RUN APPLICATION ---------------------
if __name__ == "__main__":
    app = DigitalClockApp()
    app.mainloop()
