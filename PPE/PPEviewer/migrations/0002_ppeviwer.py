# Generated by Django 3.2.4 on 2021-06-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PPEviewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ppeviwer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('missed_ppe', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('date', models.IntegerField(default=50)),
            ],
        ),
    ]
