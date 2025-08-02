from django.db import models
class Jobs(models.Model):
    jobId=models.IntegerField()
    jobname=models.CharField()
    description=models.CharField()
    salary=models.FloatField()
    link=models.URLField()
    