from django.db import models
# Create your models here.

"""
from django.db import models

class CrawledData(models.Model):
    title = models.CharField(max_length=5000)
    content = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.title
"""



"""
class Category(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'category'

    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=45)
    post_content = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    post_img = models.CharField(max_length=45, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
"""



























# class MyModel(models.Model):
#     column1 = models.CharField(max_length=100)
#     column2 = models.IntegerField()

