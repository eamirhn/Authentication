# Generated by Django 4.1.2 on 2022-10-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0013_alter_therapy_therapylist_idtherapylist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="Therapy_IDtherapy",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.therapy",
            ),
            preserve_default=False,
        ),
    ]