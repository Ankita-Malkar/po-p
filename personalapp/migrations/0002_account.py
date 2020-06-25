# Generated by Django 3.0.7 on 2020-06-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]