# Generated by Django 5.2.3 on 2025-07-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_alter_comment_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
