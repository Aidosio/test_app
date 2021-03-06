# Generated by Django 4.0.6 on 2022-07-15 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionsContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('sections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sectionsContent', to='sections.sections')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
