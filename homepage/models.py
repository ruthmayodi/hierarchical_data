from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Name(MPTTModel):
    firstcase = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MTTPMeta:
        order_insertion_by = ['firstcase']
    
    def __str__(self):
        return self.firstcase

