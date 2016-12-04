import json
import requests

from django.http.response import HttpResponse

def news(request):
    response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
    news_dict = json.loads(response.text)

    content = "<h1>News</h1>"+\
            "<p>News Page</p>"+\
            "".join([
                 "<h2>{title}</h2><img src={image_src}/><p>{content}<p>".format(
                     title = news.get("title"),
                     image_src = news.get("image"),
                     content = news.get("content"),
                     )
                 for news
                 in news_dict.get("news")
                 ])


    return HttpResponse(
            content)
