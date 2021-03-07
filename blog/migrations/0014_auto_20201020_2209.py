# Generated by Django 3.1.1 on 2020-10-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201020_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='Name',
            new_name='City',
        ),
        migrations.RemoveField(
            model_name='query',
            name='Email_id',
        ),
        migrations.AddField(
            model_name='query',
            name='First_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='query',
            name='Last_name',
            field=models.CharField(default='tarun', max_length=100),
            preserve_default=False,
        ),
    ]
