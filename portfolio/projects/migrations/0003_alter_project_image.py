# Generated by Django 5.0.3 on 2024-03-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='', upload_to='projects/images'),
        ),
    ]