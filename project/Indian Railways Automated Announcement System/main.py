import os
import pandas as pd 
from pydub import AudioSegment
from gtts import gTTS


def textTospeech(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    """This function returns pydubs audio segment"""
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)

    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1 Genenrate kripya dhyan dey
    start = 88000
    finish = 90200
    audioprocessed = audio[start:finish]
    audioprocessed.export("1_hindi.mp3",format = "mp3")

    # 2 from city
    # 3 - se chalkar
    start = 91000
    finish = 92200
    audioprocessed = audio[start:finish]
    audioprocessed.export("3_hindi.mp3",format = "mp3")
    # 4 via-city

    # 5 ke raste
    start = 94000
    finish = 95000
    audioprocessed = audio[start:finish]
    audioprocessed.export("5_hindi.mp3",format = "mp3")

    #6 to city
    #7 generte ko jane wali gaadi sankhya
    start = 96000
    finish = 98900
    audioprocessed = audio[start:finish]
    audioprocessed.export("7_hindi.mp3",format = "mp3")

    # 8 train no and name

    # 9 generate kuch hi samay me
    start = 105500
    finish = 108200
    audioprocessed = audio[start:finish]
    audioprocessed.export("9_hindi.mp3",format = "mp3")

    # 10 platform no

    # 11 generatepar aa rahi hai
    start = 109000
    finish = 112250
    audioprocessed = audio[start:finish]
    audioprocessed.export("11_hindi.mp3",format = "mp3")




def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        # 2 generate from city
        textTospeech(item['from'],'2_hindi.mp3')
        #4
        textTospeech(item['via'], '4_hindi.mp3')
        #6
        textTospeech(item['to'], '6_hindi.mp3')
        #8
        textTospeech(item['train_no']+" "+item['train_name'], '8_hindi.mp3')
        #10
        textTospeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        announcements = mergeAudios(audios)
        announcements.export(f'announcement_{index+1}.mp3',format='mp3')



if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement('announce_hindi.xlsx')