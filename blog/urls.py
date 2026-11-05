from django.urls import path

#from python_advanced.blog_project.blog.urls import urlpatterns
from .views import *

app_name = "blog"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]

