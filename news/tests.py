from django.test import TestCase
from django.test.utils import tag
from .models import Editor
import datetime as dt

# Create your tests here.
class TestEditorClass(TestCase):

  #setup method
  def setUp(self):
    self.Maria = Editor(first_name ='Maria', last_name = 'Adongo', email = 'maria@gmail.com')

  #test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.Maria, Editor))

  #test save method
  def test_save_editor(self):
    self.Maria.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors)>0)

  #test delete method
  def test_delete_editor(self):
    self.Maria.save_editor()
    editor_record = Editor.objects.all()
    self.Maria.delete_editor()
    self.assertTrue(len(editor_record)==0)

  #test displaying all editors
  def test_displaying_editors(self):
    self.Maria.save_editor()
    editors_list = Editor.display_items()
    all_editors = Editor.objects.all()
    self.assertEqual(len(editors_list),len(all_editors))















# class TestEditorClass(TestCase):
#   #set up method
#   def setUp(self):
#     self.Tito = Editor(first_name = 'Tito', last_name = 'Bascon', email = 'tito@gmail.com')

#   #testing class
#   def test_instance(self):
#     self.assertTrue(isinstance(self.Tito, Editor))
  
#   #testing save method
#   def test_save_method(self):
#     self.Tito.save_editor()
#     editors = Editor.objects.all()
#     self.assertTrue(len(editors)>0)

#   #testing delete method
#   def test_delete_method(self):
#     self.Tito.save_editor()
#     self.editor = Editor.objects.filter(first_name = 'Tito')
#     self.Tito.delete_item()
#     editors = Editor.objects.all()
#     self.assertTrue(len(editors)<=0)

# class TestArticlesClass(TestCase):

#   #initial set up
#   def setUp(self):
#     self.Tito = Editor(first_name = 'Tito', last_name = 'Bascon', email = 'tito@gmail.com')
#     self.Tito.save_editor()

#     #creating new tag and saving it
#     self.new_tag = Tag(name = 'testing')
#     self.new_tag.save()

#     #creating new article
#     self.new_article = Article(title = 'Test Article',post = 'This is a random test Post',editor = self.Tito)
#     self.new_article.save()

#     self.new_article.tags.add(self.new_tag)

#   def test_get_news_today(self):
#     today_news = Article.todays_news()
#     self.assertTrue(len(today_news)>0)

#   def test_gt_news_by_date(self):
#     test_date = '2020-2-12'
#     date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#     news_by_date = Article.past_days_news(date)
#     self.assertTrue(len(news_by_date)==0)

#   def teardown(self):
#     Editor.objects.all().delete()
#     Tag.objects.all().delete()
#     Article.objects.all().delete()

  
