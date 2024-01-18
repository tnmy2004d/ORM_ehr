from django.db import models

class EHR(models.Model):
    ehr_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    folder_id = models.IntegerField()
    folder_name = models.CharField(max_length=100)
    parent_id = models.IntegerField()
    priority = models.IntegerField()

class Documents(models.Model):
    document_id = models.AutoField(primary_key=True)
    ehr_id = models.ForeignKey(EHR, on_delete=models.CASCADE)
    file = models.BinaryField()
