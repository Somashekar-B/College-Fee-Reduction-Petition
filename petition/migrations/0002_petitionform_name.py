# Generated by Django 3.0.6 on 2020-08-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petitionform',
            name='name',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]