import tkinter as tk

class LEDSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Simulation")
        self.led_status = False  # LED dastlab o'chirilgan

        # LED indikator (yorqinlik holati)
        self.led_canvas = tk.Canvas(root, width=100, height=100, bg="black")
        self.led_canvas.pack(pady=10)
        self.led_circle = self.led_canvas.create_oval(10, 10, 90, 90, fill="green")

        # Tugma yaratish
        self.toggle_button = tk.Button(root, text="`O`CHIRISH/YOQISH", command=self.toggle_led)
        self.toggle_button.pack(pady=10)

        # LED holatini ko'rsatuvchi matn
        self.status_label = tk.Label(root, text="CHIROQ O`CHIQ", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

    def toggle_led(self):
        # Tugma bosilganda LED holatini o'zgartirish
        self.led_status = not self.led_status
        if self.led_status:
            self.led_canvas.itemconfig(self.led_circle, fill="red")
            self.status_label.config(text="CHIROQ YONIQ")
        else:
            self.led_canvas.itemconfig(self.led_circle, fill="gray")
            self.status_label.config(text="CHIROQ O`CHIQ")

# Asosiy oynani yaratish
root = tk.Tk()
app = LEDSimulation(root)
root.mainloop()
