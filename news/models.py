from django.db import models
import datetime as dt

# Create your models here.


class Editor(models.Model):
  first_name =models.CharField(max_length= 30)
  last_name = models.CharField(max_length=20)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10, blank=True)

  def __str__(self):
      return self.first_name
    
  
  def save_editor(self):
    self.save()

  def delete_editor(self):
    self.delete()

  @classmethod
  def display_items(cls):
    all_editors = Editor.objects.all()
    return all_editors
  

class Tag(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Article(models.Model):
  title = models.CharField(max_length=60)
  post = models.TextField()
  editor = models.ForeignKey(Editor, on_delete=models.SET_DEFAULT, default='Anonymous')
  tags = models.ManyToManyField(Tag)
  date_posted = models.DateTimeField(auto_now_add = True)
  article_image = models.ImageField(upload_to='articles/')

  
  def __str__(self):
    return self.title


  @classmethod
  def todays_news(cls):
    today = dt.date.today()
    news = cls.objects.filter(date_posted__date = today)
    return news
  
  @classmethod
  def past_days_news(cls, date):
    news = cls.objects.filter(date_posted = date)
    return news

  @classmethod
  def search_results_by_article(cls, titlearg):
    articles = cls.objects.filter(title = titlearg)
    return articles
