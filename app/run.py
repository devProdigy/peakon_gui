import tkinter as tk

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from screens.questions_screen import QuestionsScreen
from screens.results_screen import ResultsScreen
from screens.welcome_screen import WelcomeScreen


class ScreenManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomeScreen, QuestionsScreen, ResultsScreen):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomeScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = ScreenManager()
app.title("Quiz")
app.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

app.mainloop()
