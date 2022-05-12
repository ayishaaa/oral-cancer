from django.db import models
class healthworker(models.Model):
    worker_id = models.CharField(primary_key=True, max_length=25)
    Name=models.CharField(max_length=10)
    Email=models.CharField(max_length=20)
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=30)
    District=models.CharField(max_length=20)
    Pincode=models.IntegerField()
    Category=models.CharField(max_length=20)
    IDcardno=models.IntegerField()
    status=models.CharField(max_length=20)
    class Meta:
        db_table="healthworker"
        
class expert(models.Model):
    expert_id = models.CharField(primary_key=True, max_length=25)
    Name=models.CharField(max_length=10)
    Email=models.CharField(max_length=20)
    Mobile=models.IntegerField()
    Designation=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    Qualification=models.CharField(max_length=30)
    MCIDCIRegno=models.CharField(max_length=10)
    MoUsigned=models.CharField(max_length=10)
    status=models.CharField(max_length=20)
    class Meta:
        db_table="expert"  

class tbl_idgen(models.Model):
    
    wid=models.IntegerField()
    eid=models.IntegerField()
    pid=models.IntegerField()
    class Meta:
        db_table="tbl_idgen"  

class tbl_log(models.Model):
    Username=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Category=models.CharField(max_length=10)
    class Meta:
        db_table="tbl_log"

class patient_dtl(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=25)
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Sex=models.CharField(max_length=10)
    Mobile=models.IntegerField()
    Place=models.CharField(max_length=30)
    District=models.CharField(max_length=20)
    LSGD=models.CharField(max_length=20)
    Occupation=models.CharField(max_length=20)
    Aadharno=models.IntegerField()
    class Meta:
        db_table="patient_dtl"

# Create your models here.
