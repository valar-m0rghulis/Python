import pafy

url = "https://www.youtube.com/watch?v=nLwML2PagbY"

#Creates a new Pafy object
v = pafy.new(url)

#Pafy Object
print(v)

stream = v.getbest()
print(stream)
print("url:",stream.url)
stream.download(filepath="/Streams/" + v.title + "." + stream.extension, quiet=True)

video = v.getbestvideo()
print(video)
print("url:",video.url)
video.download(filepath="/Video/"+ v.title + "." + video.extension,quiet=True)

audio = v.getbestaudio()
print(audio)
print("url:",audio.url)
audio.download(filepath="/Audio/"+ v.title + "." + audio.extension, quiet=True)

