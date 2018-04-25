from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   #path('kuka/',views.kuka,name='kuka'),
   path('zapol/',views.zapol,name='zapol'),
   #path('result/',views.result,name='res'),
   path('signup/', views.signupform, name='sign'),
   path('syllabus/', views.syllabus, name='syl'),
   path('subform/', views.subform, name='sub'),
   path('takform/', views.takform, name='tak'),
   path('adform/', views.adform, name='ad'),
   path('zertform/', views.zertform, name='zert'),
   path('kesteform/', views.kesteform, name='keste'),



]