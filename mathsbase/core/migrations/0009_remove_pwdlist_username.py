# Generated by Django 4.2.3 on 2024-02-26 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_remove_profile_user_delete_questionp1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pwdlist",
            name="username",
        ),
    ]