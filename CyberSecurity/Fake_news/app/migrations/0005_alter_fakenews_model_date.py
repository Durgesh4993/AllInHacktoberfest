# Generated by Django 4.1 on 2023-09-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_fakenews_model_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fakenews_model",
            name="date",
            field=models.CharField(max_length=10),
        ),
    ]