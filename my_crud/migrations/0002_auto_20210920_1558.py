# Generated by Django 3.1.2 on 2021-09-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='No_of_Games',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='Player_Email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
