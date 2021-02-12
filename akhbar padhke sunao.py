import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)
# bf904cd0c1c74004b9a4467a8441efe1
if __name__ == '__main__':
    apiKey = input("enter your API keyprovided you from newsapi.org ")
    speak("News for today...Lets begin")
    url = f"http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={apiKey}"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arts = news_dict['articles']
    for articles in arts:
        speak(articles['title'])
        speak("moving on to the next news")
    speak("Thanks for listening")