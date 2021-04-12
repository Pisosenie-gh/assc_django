# Generated by Django 3.1.4 on 2021-02-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveField(
            model_name='articles',
            name='create_date',
        ),
        migrations.AddField(
            model_name='articles',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]