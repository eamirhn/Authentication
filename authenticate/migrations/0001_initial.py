# Generated by Django 4.1.2 on 2022-10-06 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicine",
            fields=[
                ("medicineID", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "organizationID",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("roleID", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=45)),
                ("type", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                ("testID", models.IntegerField(primary_key=True, serialize=False)),
                ("dateTime", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("userID", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "Organization",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authenticate.organization",
                    ),
                ),
                (
                    "Role_IDrole",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authenticate.role",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Therapy_List",
            fields=[
                (
                    "therapy_listID",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=45)),
                (
                    "Medicine_IDmedicine",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authenticate.medicine",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Therapy",
            fields=[
                ("therapyID", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "TherapyList_IDtherapylist",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authenticate.therapy_list",
                    ),
                ),
                (
                    "User_IDpatient",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Test_Session",
            fields=[
                (
                    "test_SessionID",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("test_type", models.IntegerField()),
                ("DataURL", models.CharField(max_length=255)),
                (
                    "Test_IDtest",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authenticate.test",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="test",
            name="Therapy_IDtherapy",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="authenticate.therapy",
            ),
        ),
        migrations.CreateModel(
            name="Note",
            fields=[
                ("noteID", models.IntegerField(primary_key=True, serialize=False)),
                ("note", models.TextField()),
                (
                    "Test_Session_IDtest_session",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authenticate.test_session",
                    ),
                ),
                (
                    "User_IDmed",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
