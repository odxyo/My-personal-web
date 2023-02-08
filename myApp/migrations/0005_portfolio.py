# Generated by Django 4.0.6 on 2023-01-31 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_i_do_icons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_work', models.CharField(max_length=200, null=True)),
                ('explain', models.CharField(max_length=200)),
                ('port_pic', models.ImageField(upload_to='media/picture')),
                ('job_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.i_do')),
            ],
        ),
    ]