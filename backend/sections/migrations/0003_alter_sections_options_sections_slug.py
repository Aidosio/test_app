# Generated by Django 4.0.6 on 2022-07-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_sectionscontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sections',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='sections',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]