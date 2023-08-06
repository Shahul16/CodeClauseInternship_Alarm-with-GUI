import tkinter as tk
import time
import pygame

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x200")

        # Custom color theme
        self.root.configure(bg="#354458")
        self.time_label = tk.Label(root, text="Alarm Time:", bg="#354458", fg="white")
        self.time_label.pack()

        self.alarm_time = tk.StringVar()
        self.alarm_time.set("12:00:00")

        self.time_entry = tk.Entry(root, textvariable=self.alarm_time, bg="white", fg="#354458")
        self.time_entry.pack()

        self.am_pm_var = tk.StringVar()
        self.am_pm_var.set("AM")

        self.am_pm_menu = tk.OptionMenu(root, self.am_pm_var, "AM", "PM")
        self.am_pm_menu.config(bg="#FECB2F", activebackground="#FFD24D", fg="#354458")
        self.am_pm_menu.pack()

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm, bg="#FECB2F", activebackground="#FFD24D", fg="#354458")
        self.set_button.pack()

    def set_alarm(self):
        alarm_time = self.alarm_time.get()
        am_pm = self.am_pm_var.get()

        try:
            # Convert the entered time to seconds
            alarm_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(alarm_time.split(":"))))
            if am_pm == "PM":
                alarm_seconds += 12 * 3600  # Add 12 hours in seconds for PM times
            current_time = time.localtime()
            current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec

            # Calculate the time remaining until the alarm goes off
            time_remaining = alarm_seconds - current_seconds

            if time_remaining <= 0:
                raise ValueError("The entered time has already passed.")

            self.root.after(time_remaining * 1000, self.play_alarm)
            self.set_button.config(state="disabled")
        except ValueError as e:
            self.display_error(str(e))

    def play_alarm(self):
        # Initialize pygame mixer
        pygame.mixer.init()
        # Load a sound file (replace "alarm_sound.wav" with your own sound file)
        alarm_sound = pygame.mixer.Sound("alarm_sound.wav")
        # Play the sound
        alarm_sound.play()

        # Show a message box when the alarm goes off
        tk.messagebox.showinfo("Alarm", "Time's up!")

        # Reset the GUI after the alarm goes off
        self.alarm_time.set("12:00:00")
        self.am_pm_var.set("AM")
        self.set_button.config(state="active")

    def display_error(self, message):
        tk.messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
