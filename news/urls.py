from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^news_today/$', views.news_today, name = 'newsToday'),
  url(r'^archives/(\d{4}-\d{1}-\d{2})/$', views.past_news, name = 'pastnews'),
  url(r'^search/', views.search_results, name = 'search_results'),
  url(r'^article/(\d+)/$', views.articles_ind, name = 'articles_ind')
]