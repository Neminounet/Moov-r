from gui import App
from moovr import Moovr


def main():
    activate = True
    while activate:

        app = App()
        app.mainloop()

        if app.launch == True:
            moovr = Moovr()
            moovr.mainloop()
        else:
            activate = False

        if moovr.launch == False:
            app = App()
            app.mainloop()

        if app.exit == True:
            # app.destroy()
            activate = False


main()
