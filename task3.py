import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
import requests

def extract_song_lyrics():
    global artist, song
    artistName = str(artist.get()).lower()
    songName = str(song.get()).lower() 
    link = "https://api.lyrics.ovh/v1/"+artistName.replace(' ', '%20')+'/'+songName.replace(' ', '%20')

    req = requests.get(link)
    json_data = json.loads(req.content)

    try:
        lyrics = json_data["lyrics"]
        print(lyrics)
        messagebox.showinfo("Lyrics Extracted", "The lyrics of the song  {} have been extracted successfully".format(songName.upper()))

    except Exception as e:
        print(e)
        messagebox.showerror("Error","Song not found. Ensure that the Song name and Artist's anem is correct.")

# Window Initialization
window = Tk()
window.title("Song Lyric Extractor")
window.geometry("680x220")  # Set initial size of the window
window.resizable(False, False)  # Disable window resizing
window.configure(bg="red")  # Set background color for the window

# Creating Labels and Entries
heading_label = tk.Label(window, text="Lyric Extractor", font=("Algerian", 18, "bold"), bg="red", fg="black")
heading_label.grid(row=0, column=0, columnspan=2, sticky=tk.N, padx=10, pady=10)

song_name_label = tk.Label(window, text="Song Name: ", font=("Times New Roman", 18,"bold"), bg="red", fg="black")
song_name_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

song = StringVar()
song_name_Entry = tk.Entry(window, width=40, textvariable=song, font=("Courier", 14, "italic","bold"))
song_name_Entry.grid(row=1, column=1, padx=10, pady=10, ipadx=3, ipady=3)

artist_name_label = tk.Label(window, text="Artist Name: ", font=("Times New Roman", 18,"bold"), bg="red", fg="black")
artist_name_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

artist = StringVar()
artist_name_entry = tk.Entry(window, width=40, textvariable=artist, font=("Courier", 14, "italic","bold"))
artist_name_entry.grid(row=2, column=1, padx=10, pady=10, ipadx=3, ipady=3)

Extract_Button = tk.Button(window, text='Extract', font=("Algerian", 15, "bold"), width=15, command=extract_song_lyrics, bg="black", fg="white")
Extract_Button.grid(row=3, column=0, columnspan=2, pady=20,sticky=tk.S)

window.mainloop()
