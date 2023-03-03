from pytube import YouTube

link = input("Please enter the link of the YouTube video: ")
yt = YouTube(link)

stream = yt.streams.get_highest_resolution()
stream.download()
print("Your download has been completed!")
