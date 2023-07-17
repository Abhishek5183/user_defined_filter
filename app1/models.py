from django.db import models

# Create your models here.
class Agents(models.Model):
    agent_code = models.IntegerField(primary_key=True)
    agent_mobile = models.CharField(max_length=100)
    agent_name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.agent_name
    
class Customer(models.Model):
    cust_name = models.CharField(max_length=100)
    cust_code = models.IntegerField(max_length=100, primary_key=True)
    cust_mobile = models.CharField(max_length = 100)
    agent_name = models.ForeignKey(Agents, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.cust_name
    
    
