from tkinter import *
from tkinter import filedialog
from pygame import mixer

class player:
    def __init__(self, window):
        window.geometry('320x140')
        window.title('Python Tiny Player')
        window.resizable(0, 0)

        # Load the music icon image
        self.music_icon_image = PhotoImage(file='music_icon.png.png')

        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        stop = Button(window, text='Stop', width=10, font=('Times', 10), command=self.stop)

        # Create a Label widget to display the music icon image
        music_icon_label = Label(window, image=self.music_icon_image)

        Load.place(x=0, y=20)
        play.place(x=110, y=20)
        pause.place(x=220, y=20)
        stop.place(x=110, y=60)

        # Place the music icon image Label
        music_icon_label.place(x=140, y=90)

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):  # corrected method signature
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()

new_root = Tk()
player_app = player(new_root)
new_root.mainloop()
