# Generated by Django 4.1.5 on 2023-01-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_rename_predresults_predictedresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=512)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]