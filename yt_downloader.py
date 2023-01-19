#!/usr/bin/env python3

import tkinter
import customtkinter
from pytube import YouTube

# Function to start the video download process
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download error", text_color="red")    
    
# Callback function for updating the progress bar and percentage
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text= per + "%")
    pPercentage.update()

    #Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)


# Set the appearance mode and color theme for the GUI
customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")

#Create main frame for the GUI
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#Label for displaying the video title
title = customtkinter.CTkLabel(app, text="Insert a YT link")
title.pack(padx=10, pady=10)

#Create an input field for the user to enter the YouTube link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Display the download status
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Display the download progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()

