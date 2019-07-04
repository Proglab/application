from tkinter import *
import application
import tkinter as tk
import warnings
import os
import logging
from dsdev_utils.app import app_cwd, FROZEN
from dsdev_utils.logger import logging_formatter
from pyupdater import settings, __version__


warnings.simplefilter("always", DeprecationWarning)

log = logging.getLogger(__name__)
log_path = os.path.join(app_cwd, "pyu.log")

print(log_path)

if os.path.exists(log_path):  # pragma: no cover
    ch = logging.FileHandler(os.path.join(app_cwd, "pyu.log"))
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging_formatter)
    log.addHandler(ch)
log.debug("PyUpdater Version %s", __version__)


class Application(Tk):

    HEIGHT = 600
    WIDTH = 600

    def __init__(self):
        super(Application, self).__init__()
        self.title("Ma belle application")
        self.minsize(self.WIDTH, self.HEIGHT)
        self.wm_iconbitmap('./assets/icons/icon.ico')

        log.debug('Initialisation du programme')
        self.image = None

    def run(self):
        """
        Create the app and run its main loop to process events.

        If being called by automated testing, the main loop
        won't be run and the app will be returned.
        """

        global_frame = tk.Frame(self, height=self.HEIGHT, width=self.WIDTH, bg="#222222")
        global_frame.place(x=0, y=0, relwidth=1, relheight=1)

        button = tk.Button(self, text=application.__version__)
        button.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.1)

        self.image = PhotoImage(file='./assets/images/troll.png')

        label = tk.Label(global_frame, text=" ", foreground="#ffffff", image=self.image, compound="left")
        label.config(font=(None, 21))
        label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        return self
