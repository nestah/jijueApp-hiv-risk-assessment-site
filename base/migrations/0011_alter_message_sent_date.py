# Generated by Django 4.1.3 on 2023-01-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_sent_date_predresults_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]