# Generated by Django 5.0.3 on 2024-03-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='demoLink',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='githubLink',
            field=models.URLField(default=''),
        ),
    ]
