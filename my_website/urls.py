from django.contrib import admin
from django.urls import path
from myweb.views import welcome,home,course,intern

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome,name="welcome"),
    path('home/',home,name="home"),
    path('course/',course,name="course"),
     path('intern/',intern,name="intern"),
]
