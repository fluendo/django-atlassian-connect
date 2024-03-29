# Generated by Django 3.2.14 on 2023-02-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_atlassian_connect", "0003_securitycontext_oauth_client_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="securitycontext",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="securitycontext",
            name="installed",
            field=models.BooleanField(default=True),
        ),
    ]
