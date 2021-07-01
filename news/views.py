from django.http.response import Http404
from django.shortcuts import redirect, render
import datetime as dateset
from .models import Article

# Create your views here.
def welcome(request):
  results = Article.objects.all()

  return render(request, 'welcome.html', {'results':results})

def news_today(request):

  today = dateset.date.today()
  news = Article.todays_news()

  title = 'Moringa News Today'

  return render(request, 'all_news/today_news.html', {'today':today, 'title':title, 'news':news})

def past_news(request, past_date):
  try:
    date = dateset.datetime.strptime(past_date, '%Y-%m-%d').date()
  except:
    raise Http404()
    assert False

  title ='Moringa Archives'
  if date == dateset.date.today():
    return redirect(news_today)

  news = Article.past_days_news(date)

  return render(request,'all_news/past_news.html', {'date':date, 'title':title, 'news':news})

def search_results(request):
  if 'article' in request.GET and request.GET['article']:
    search_term = request.GET.get('article')
    searched_articles = Article.objects.filter(title__icontains=search_term)
    message = f'{search_term}'

    return render(request, 'all_news/search_page.html', {'searched_articles':searched_articles, 'message':message})
  
  else:
    message = 'You have not searched for anything'

    return render(request, 'all_news/search_page.html', {'message':message})

def articles_ind(request, article_id):
  try:
    article = Article.objects.get(id=article_id)
  except:
    raise Http404

  return render(request, 'all_news/articles.html', {'article':article})