from tkinter import *
import application
import tkinter as tk
from tkinter import ttk
from pyupdater.client import Client
from client_config import ClientConfig

from application.main import Application


class Updater(Tk):

    HEIGHT = 600
    WIDTH = 600

    def __init__(self):
        super(Updater, self).__init__()
        self.title("Application updater")
        self.minsize(self.WIDTH, self.HEIGHT)
        self.wm_iconbitmap('./assets/icons/icon.ico')

        self.client = Client(ClientConfig(), progress_hooks=[self.print_status_info])
        self.client.refresh()
        self.pb = None
        self.frame_updater = None
        self.label = None
        self.waiting_image = None
        self.lib_update = self.client.update_check('Application', application.__version__)

    def run(self):
        global_frame = tk.Frame(self, height=self.HEIGHT, width=self.WIDTH, bg="#222222")
        global_frame.place(x=0, y=0, relwidth=1, relheight=1)

        frame_top = tk.Frame(self, bg="#990033")
        frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        attention_image = tk.PhotoImage(file='./assets/images/attention.png')

        label = tk.Label(frame_top, text=" Programme Updater", bg="#990033", foreground="#ffffff", image=attention_image, compound="left", font=60)
        label.config(font=(None, 21))
        label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.frame_updater = tk.Frame(self, bg="#555555")
        self.frame_updater.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)

        self.waiting_image = tk.PhotoImage(file='./assets/images/waiting.png')

        self.label = tk.Label(self.frame_updater, text=" Checking for update", bg="#999999", foreground="#ffffff", image=self.waiting_image, compound="left", font=60)
        self.label.config(font=(None, 12))
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.4)
        self.pb = ttk.Progressbar(self.frame_updater, orient="horizontal", length=200, mode="determinate", value=0, maximum=100)
        self.pb.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)

        self.after(500, self.update)

    def update(self):
        if self.lib_update is not None:
            self.lib_update.cleanup()
            self.client.refresh()
            self.label['text'] = ' Downloading update'
            self.after(100, self.download)
            self.lib_update.download()
        else:
            self.pb.destroy()
            self.waiting_image = tk.PhotoImage(file='./assets/images/ok.png')
            self.label['image'] = self.waiting_image
            self.label['text'] = ' No update needed'
            self.after(1000, self.execute_app)

    def download(self):
        if self.lib_update is not None and self.lib_update.is_downloaded():
            self.label['text'] = ' Installing update & restart'
            # self.pb['value'] = 100
            self.after(1000, self.restart)

    def restart(self):
        self.lib_update.extract_restart()

    def print_status_info(self, info):
        total = info.get(u'total')
        percent_complete = info.get(u'percent_complete')
        downloaded = info.get(u'downloaded')
        status = info.get(u'status')
        self.pb['value'] = percent_complete
        print(downloaded, total, status, percent_complete)

    def execute_app(self):
        self.destroy()
        app = Application()
        app.run()
        app.mainloop()
