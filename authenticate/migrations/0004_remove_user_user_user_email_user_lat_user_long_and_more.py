# Generated by Django 4.1.2 on 2022-10-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0003_alter_note_test_session_idtest_session_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="User",),
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user", name="lat", field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name="user", name="long", field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name="user",
            name="provider",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="userID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
