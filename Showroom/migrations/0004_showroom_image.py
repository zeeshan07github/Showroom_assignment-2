# Generated by Django 4.2.3 on 2023-07-29 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Showroom", "0003_showroom_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="showroom",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]