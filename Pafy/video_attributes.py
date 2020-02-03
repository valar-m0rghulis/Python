
import pafy

url = "https://www.youtube.com/watch?v=TtUz514rXKo"

#Creates a new Pafy object
video = pafy.new(url)

#Pafy Object
print(video)

#Pafy object has following attributes
print("----------Video Information------------")

print("Title:",video.title)             #The title of the video (str)
print("URL:",url)
print("Duration:",video.duration)       #The duration of the stream (string formatted as HH:MM:SS)
print("Rating:",video.rating)           #The rating of the video (0-5), (float)
print("Author:",video.author)           #The author of the video (str)
print("Length:",video.length)           #The duration of the streams in seconds (int)
print("Keywords:",video.keywords)       #A list of the video’s keywords (not always available) ([str])
print("Video Id:",video.videoid)        #The 11-character video id (str)
print("View Count:",video.viewcount)    #The viewcount of the video (int)
print("Category:",video.category)       #The category of the video (str)
print("Description:",
      video.description.encode("utf8")) #The video description text (str)
print("Dislikes:",video.dislikes)       #The number of dislikes received for the video (int)
print("Likes:",video.likes)             #The number of likes received for the video (int)
print("Pulished on:",video.published)   #The upload date of the video (e.g., 2012-10-02 17:17:24) (str)
print("Thumbnail:",video.thumb)         #The url of the video’s thumbnail image (str)
print("Username:",video.username)       #The username of the uploader (str)
