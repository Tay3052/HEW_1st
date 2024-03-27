from django.db import models
from django.utils import timezone

# Create your models here.

class userTable(models.Model):

    id = models.CharField(primary_key="True", verbose_name="ユーザID", blank="False", max_length=20)
    password = models.CharField(verbose_name="パスワード", null="False", max_length=20)
    password_check = models.CharField(verbose_name="パスワード(確認)", null="False", max_length=20)
    mail = models.EmailField(verbose_name="E-Mail", null="True" )
    create_at = models.TimeField(verbose_name="作成日付", default = timezone.now)

class loginTable(models.Model):
    id = models.CharField(primary_key="True", verbose_name="ユーザID", blank="False", max_length=20)
    password = models.CharField(verbose_name="パスワード", null="False", max_length=20)
    
class chatTable(models.Model):

    userName = models.CharField(verbose_name="ユーザ名", max_length=20)
    title = models.CharField(verbose_name="タイトル", max_length=20)
    text = models.TextField(verbose_name="コメント", blank="True")
    img = models.ImageField(verbose_name="画像ファイル", blank="True", upload_to="image/")
    create_at = models.TimeField(verbose_name="作成日付", default = timezone.now)
    genre = models.CharField(verbose_name="ジャンル", max_length=20)

    def __str__(self):
        return self.title