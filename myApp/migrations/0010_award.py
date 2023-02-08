# Generated by Django 4.0.6 on 2023-02-01 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_portfolio_title_alter_portfolio_explain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_title', models.CharField(blank=True, max_length=500, null=True)),
                ('award_explain', models.TextField()),
                ('time', models.DateField()),
                ('award_picture', models.ImageField(upload_to='media/awardPicture')),
                ('name_job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.i_do')),
            ],
        ),
    ]