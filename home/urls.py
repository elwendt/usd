from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('papers/', views.PaperListView.as_view, name='papers'),
]

