# Generated by Django 4.1.5 on 2023-03-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_chattable1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chattable1",
            name="img",
            field=models.ImageField(
                blank="True", upload_to="image/", verbose_name="画像ファイル"
            ),
        ),
    ]
