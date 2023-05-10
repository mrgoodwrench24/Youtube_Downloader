import sys
import os
from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable

choice = "0"


def download_video():
    link = input("What is the url?\n")
    type = input("Type 1 for Video and Type 2 for Music")
    if type == '1':
        file_extension = '.mp4'
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.get_highest_resolution()
    elif type == '2':
        file_extension = '.mp3'
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.filter(only_audio=True).get_audio_only()
    else:
        print("Invalid response.  Type 1 for Video and Type 2 for Music")

    custom_name_input = input("Enter File Name:\n")
    filename = custom_name_input + file_extension

    current_directory = os.getcwd()

    try:
        print("Downloading " + youtube_object.title + "\n\n")
        youtube_object.download(output_path=current_directory,filename=filename)
        print(filename + " Download is completed successfully")
    except:
        print("An error has occurred")


def download_playlist():
    link = input("What is the playlist url?\n")
    p = Playlist(link)
    for link in p.video_urls:
        try:
            video = YouTube(link)
        except VideoUnavailable:
            print(f'Video {link} is unavaialable, skipping.')
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            video.streams.get_highest_resolution().download()
            print(video.title + " Download is completed successfully")

while choice != "q":
    choice = input("Youtube Downloader\nWelcome!  Choose a number then hit enter\n1. Download Single Youtube video\n2. Download Playlist\n q to quit\n")
    if choice == "1":
        os.system('cls')
        download_video()
    elif choice == "2":
        download_playlist()
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please try again.")


sys.exit()






