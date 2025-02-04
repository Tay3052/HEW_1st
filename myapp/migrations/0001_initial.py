# Generated by Django 4.1.5 on 2023-03-01 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="chatTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "userName",
                    models.CharField(max_length=20, null="False", verbose_name="表示名"),
                ),
                (
                    "title",
                    models.CharField(max_length=20, null="False", verbose_name="タイトル"),
                ),
                ("text", models.TextField(blank="True", verbose_name="コメント")),
                ("img", models.ImageField(upload_to="image/", verbose_name="画像ファイル")),
                (
                    "create_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 3, 1, 5, 39, 8, 974303, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="作成日付",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="userTable",
            fields=[
                (
                    "id",
                    models.CharField(
                        blank="False",
                        max_length=20,
                        primary_key="True",
                        serialize=False,
                        verbose_name="ユーザID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=20, null="False", verbose_name="パスワード"),
                ),
                (
                    "password_check",
                    models.CharField(
                        max_length=20, null="False", verbose_name="パスワード(確認)"
                    ),
                ),
                (
                    "mail",
                    models.EmailField(
                        max_length=254, null="True", verbose_name="E-Mail"
                    ),
                ),
                (
                    "create_at",
                    models.TimeField(
                        default=datetime.datetime(
                            2023, 3, 1, 5, 39, 8, 974303, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="作成日付",
                    ),
                ),
            ],
        ),
    ]
