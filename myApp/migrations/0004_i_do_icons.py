# Generated by Django 4.0.6 on 2023-01-31 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_i_do_options_alter_i_do_job_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='i_do',
            name='icons',
            field=models.ImageField(default=2, upload_to='media'),
            preserve_default=False,
        ),
    ]
