# Generated by Django 4.1.2 on 2022-10-09 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authenticate", "0002_user_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="Test_Session_IDtest_session",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.test_session",
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="User_IDmed",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="test",
            name="Therapy_IDtherapy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.therapy",
            ),
        ),
        migrations.AlterField(
            model_name="test_session",
            name="Test_IDtest",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.test",
            ),
        ),
        migrations.AlterField(
            model_name="therapy",
            name="TherapyList_IDtherapylist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.therapy_list",
            ),
        ),
        migrations.AlterField(
            model_name="therapy",
            name="User_IDpatient",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="therapy_list",
            name="Medicine_IDmedicine",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.medicine",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="Organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.organization",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="Role_IDrole",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.role",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="User",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
