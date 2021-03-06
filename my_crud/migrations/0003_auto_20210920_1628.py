# Generated by Django 3.1.2 on 2021-09-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crud', '0002_auto_20210920_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='No_of_Games',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Player_Email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Player_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Total_Score',
            field=models.IntegerField(null=True),
        ),
    ]
