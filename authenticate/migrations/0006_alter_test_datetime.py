# Generated by Django 4.1.2 on 2022-10-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0005_user_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="dateTime",
            field=models.DateField(auto_now_add=True),
        ),
    ]
