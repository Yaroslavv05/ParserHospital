# Generated by Django 4.2.2 on 2023-06-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='name_cite',
        ),
        migrations.AlterField(
            model_name='links',
            name='links_on_hospital',
            field=models.CharField(max_length=300),
        ),
    ]
