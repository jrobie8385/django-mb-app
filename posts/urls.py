from django.conf.urls import url
from . import views

app_name = "posts"

urlpatterns = [
    url("", views.ViewPosts.as_view(), name = "all")
]
