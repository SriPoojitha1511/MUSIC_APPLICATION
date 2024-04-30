import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x200")

        self.folder_path = ""
        self.playlist = []
        self.current_index = 0
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Music Player", font=("Arial", 16))
        self.label.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_button.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.next)
        self.next_button.pack()

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev)
        self.prev_button.pack()

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path = folder_path
            self.playlist = [file for file in os.listdir(self.folder_path) if file.endswith('.mp3')]
            if not self.playlist:
                tk.messagebox.showerror("Error", "No MP3 files found in the selected folder.")
                return
            self.current_index = 0
            self.play_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.NORMAL)
            self.prev_button.config(state=tk.NORMAL)
            tk.messagebox.showinfo("Success", "Folder selected successfully.")

    def play(self):
        if not self.playlist:
            tk.messagebox.showerror("Error", "Please select a folder with MP3 files.")
            return
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.folder_path, self.playlist[self.current_index]))
        pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            if self.paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            self.paused = not self.paused

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
