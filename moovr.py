import tkinter
import mouse
import time


class Moovr(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Moov'r")
        self.width = 300
        self.height = 100
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.pos_width = 0
        self.pos_height = (self.screen_height) - (self.height * 2)
        self.geometry(
            f"{self.width}x{self.height}+{self.pos_width}+{self.pos_height}")
        self.resizable(width=False, height=False)
        self.launch = True
        self.counter = 120
        self.to_left = True
        self.to_right = False

        # Widgets :
        self.frame_title = tkinter.LabelFrame(self)
        self.label_title = tkinter.Label(
            self.frame_title, text="Moov'r", font=("Arial", 16, "bold"))
        self.label_name = tkinter.Label(
            self.frame_title, text="Jean-Nemo Aka YT", font=("Arial", 6))
        self.frame_text = tkinter.LabelFrame(self)
        self.warning = tkinter.Label(self.frame_text, text=f"Mouvement dans :")
        self.count = tkinter.Label(
            self.frame_text, text=f"{str(self.counter)} secondes")
        self.button_exiter = tkinter.Button(
            self, text="Arreter", bg="#c0392b", fg="white", activebackground="#e74c3c", command=self.exiter)

        # Placement
        self.frame_title.pack()
        self.label_title.grid(row=0, column=0)
        self.label_name.grid(row=1, column=0)
        self.frame_text.pack()
        self.warning.grid(row=0, column=0)
        self.count.grid(row=0, column=1)
        self.button_exiter.pack()

        if self.launch == True:
            self.mouv()

    def exiter(self):
        self.launch = False

    def mouv(self):
        if self.counter != 0 and self.launch == True:
            time.sleep(0.5)
            self.counter -= 1
            self.count.config(text=f"{str(self.counter)}")
            print(self.counter)
            if self.counter == 1 and self.to_left == True:
                mouse.move(-100, 0, absolute=False, duration=0.5)
                self.counter = 120
                self.to_left = False
                self.to_right = True
            elif self.counter == 1 and self.to_right == True:
                mouse.move(100, 0, absolute=False, duration=0.5)
                self.counter = 120
                self.to_left = True
                self.to_right = False
        else:
            self.destroy()

        if self.launch == True:
            self.after(1000, self.mouv)


if __name__ == "__main__":
    app = Moovr()
    app.mainloop()
