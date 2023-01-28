from PIL import Image, ImageDraw, ImageFont
import numpy as np
import moviepy.editor as mp
from textwrap import wrap
from moviepy.editor import *
from gtts import gTTS
# Create a black video with 9:16 ratio
width = 1080
height = 1920
duration = 59 # in seconds

# Create black image
def create_video(title_main,content):
    img = Image.new('RGB', (width, height), color = (0, 0, 0))

    draw = ImageDraw.Draw(img)
    title =  "My boyfriend \u2018cheated\u2019 on me and now it feels like I can\u2019t trust him"
    title_font = ImageFont.truetype("arial.ttf", 60)
    title_lines = wrap(title, width=int(width/40))
    title_height = 0
    for line in title_lines:
        w, h = draw.textsize(line, font=title_font)
        draw.text(((width-w)/2, title_height), line, font=title_font, fill=(0,255,0))
        title_height += h

    paragraph = "So, i have been in a relationship with my boyfriend for 10 months, he\u2019s been a amazing boyfriend most of the time and we\u2019re always having fun together.. but in the beginning of our relationship i found out he was cheating on me, at least it was something I thought was cheating and he didn\u2019t feel the same way about it. It wasn\u2019t that he was fucking another woman, he sent text messages, sexual texts messages to woman all over the world. I forgave him because he never had a real relationship before so i guess he thought it was something he could still do\u2026 I\u2019ve always had trust issues so it was hard for me to fully trust him again. But things were going great. I started to trust him again because he didn\u2019t do anything that i was uncomfortable with, he even started living with me for a few months, i never wanted to leave him, i still don\u2019t want to because he makes me the happiest girl i\u2019ve ever been. But last December on my birthday i found out he cheated again\u2026 this time it wasn\u2019t just text\u2019s, there also were nudes. I confronted him about this and he was like so emotional and I\u2019ve never seen him like this\u2026 i once again forgave him\u2026 it\u2019s been almost 2 months now since I\u2019ve found out and we\u2019re doing great.. but something in me just needs to constantly check if he isn\u2019t cheating and it\u2019s driving me crazy. But it just sucks because we talk about it al the time and i know he isn\u2019t cheating.. but now idk what to do because he really is the person i want to grow old with and i just think I\u2019m overreacting."
    paragraph_font = ImageFont.truetype("arial.ttf", 55)
    paragraph_lines = wrap(paragraph, width=int(width/27))
    paragraph_height = title_height + 20
    for line in paragraph_lines:
        w, h = draw.textsize(line, font=paragraph_font)
        draw.text(((width-w)/2, paragraph_height), line, font=paragraph_font, fill=(255,255,255))
        paragraph_height += h

    video = mp.ImageClip(np.array(img), duration=duration)
    print("gen audio")
    tts = gTTS(title+paragraph)
    tts.save('main.mp3')
    print("audio save")
    audio = AudioFileClip("main.mp3")
    audio = audio.subclip(0, 59)
    video = video.set_audio(audio)
    video.write_videofile("video.mp4",fps=30)
#create_video("","")
