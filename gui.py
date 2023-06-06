import tkinter


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Moov'r")
        self.width = 300
        self.height = 100
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.pos_width = (self.screen_width // 2) - (self.width // 2)
        self.pos_height = (self.screen_height // 2) - (self.height // 2)
        self.geometry(
            f"{self.width}x{self.height}+{self.pos_width}+{self.pos_height}")
        self.resizable(width=False, height=False)
        self.launch = False
        self.exit = False

        # Widgets :
        self.frame_title = tkinter.LabelFrame(self)
        self.label_title = tkinter.Label(
            self.frame_title, text="Moov'r", font=("Arial", 16, "bold"))
        self.label_name = tkinter.Label(
            self.frame_title, text="Jean-Nemo Aka YT", font=("Arial", 6))
        self.button_Frame = tkinter.Frame(self)
        self.button_launcher = tkinter.Button(
            self.button_Frame, text="Lancer", bg="#27ae60", fg="white", activebackground="#2ecc71", command=self.launcher)
        self.button_exiter = tkinter.Button(
            self.button_Frame, text="Quitter", bg="#c0392b", fg="white", activebackground="#e74c3c", command=self.exiter)

        # Placement
        self.frame_title.pack()
        self.label_title.grid(row=0, column=0)
        self.label_name.grid(row=1, column=0)
        self.button_Frame.pack()
        self.button_launcher.grid(row=0, column=0)
        self.button_exiter.grid(row=0, column=1)

    def exiter(self):
        self.exit = True
        self.destroy()

    def launcher(self):
        self.launch = True
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
