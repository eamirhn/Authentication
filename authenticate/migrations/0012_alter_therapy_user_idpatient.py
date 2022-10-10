# Generated by Django 4.1.2 on 2022-10-10 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authenticate", "0011_alter_therapy_list_medicine_idmedicine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="therapy",
            name="User_IDpatient",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]