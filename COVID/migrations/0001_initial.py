# Generated by Django 3.0.3 on 2020-04-20 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(default='', max_length=200)),
                ('english_name', models.CharField(default='', max_length=200)),
                ('atate_abbreviations', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.CharField(default='', max_length=200)),
                ('new_deaths', models.BigIntegerField()),
                ('cumula_deaths', models.BigIntegerField()),
                ('new_confirmed', models.BigIntegerField()),
                ('cumula_confirmed', models.BigIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='COVID.Country')),
            ],
        ),
    ]