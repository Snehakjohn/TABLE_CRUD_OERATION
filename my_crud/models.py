from django.db import models

# Create your models here.
class Player(models.Model):
	ID=models.IntegerField(null=True)
	Player_Name=models.CharField(max_length=100,null=True)
	Player_Email=models.EmailField(max_length=100,null=True)
	Country=models.CharField(max_length=50,null=True)
	No_of_Games=models.CharField(max_length=50,null=True)
	Total_Score=models.IntegerField(null=True)
	class Meta:
		db_table="Players"
