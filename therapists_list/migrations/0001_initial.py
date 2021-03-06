# Generated by Django 3.2.8 on 2021-11-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Therapists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='firstname')),
                ('lastname', models.CharField(max_length=255, verbose_name='lastname')),
                ('phone', models.CharField(max_length=255, verbose_name='phone')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('experience', models.IntegerField(verbose_name='experience')),
                ('degree', models.CharField(max_length=255, verbose_name='education')),
                ('about', models.TextField(verbose_name='about')),
                ('age', models.IntegerField(verbose_name='age')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('sex', models.CharField(max_length=6, verbose_name='sex')),
                ('photo', models.ImageField(verbose_name='photo')),
            ],
        ),
    ]
