# Generated by Django 4.2.10 on 2024-02-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmpModel",
            fields=[
                ("eid", models.IntegerField(primary_key=True, serialize=False)),
                ("ename", models.CharField(max_length=25)),
                ("ecity", models.CharField(max_length=25)),
                ("esal", models.FloatField()),
                ("eemail", models.EmailField(max_length=254)),
                ("edept", models.CharField(max_length=25)),
            ],
        ),
    ]
