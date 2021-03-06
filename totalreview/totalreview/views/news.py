import json
import requests

from django.conf import settings
from django.http.response import HttpResponse

from totalreview.views.renderer import render

def news(request):
    search = request.GET.get("search")

    response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
    news_dict = json.loads(response.text)
    news_list = news_dict.get("news")
    
    if search:
        news_list = list(filter(
                    lambda news : search in news.get("title"),
                    news_list))

    count = len(news_list)
    news_content = "".join([
        "<h2>{title}</h2><img src={image_src}/><p>{content}<p>".format(
            title = news.get("title"),
            image_src = news.get("image"),
            content = news.get("content"),
            )
        for news
        in news_list
        ])
    
    return render("news", {"count" : str(count), "news_content" : news_content,} )
