# Generated by Django 3.2.5 on 2022-12-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerPersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('education', models.CharField(max_length=150)),
                ('marital_status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LandDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('area', models.FloatField()),
                ('latitude', models.CharField(max_length=150)),
                ('longitude', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LandProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_marketibility', models.CharField(choices=[('1', 'International'), ('2', 'National'), ('3', 'State level'), ('4', 'District level'), ('5', 'Village level')], default='1', max_length=20)),
            ],
        ),
    ]
