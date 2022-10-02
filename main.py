from pytube import YouTube

link = input("Enter Link of Youtube Video: ")
yt = YouTube(link)

stream = yt.streams.get_highest_resolution()
stream.download()
print("Download has been completed!")