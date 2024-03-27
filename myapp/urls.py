from django.urls import path
from . import tests
from . import views

app_name = "myapp"
urlpatterns = [
    path("", tests.test, name="test"),
    path("index/",views.indexView.as_view() , name="index"),
    path("login/",views.loginView.as_view(), name="login"),
    path("login/success/",views.loginSuccessView.as_view(), name="login_success"),
    path("login/register/",views.registerView.as_view(), name="register"),
    path("chat/",views.chatView.as_view(), name="chat"),
    path("chat/say/",views.chatSayView.as_view(), name="chat_say"),
    
]