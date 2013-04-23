from django.db import models
from django.contrib.auth.models import User
#from test.test_imageop import MAX_LEN


class Link(models.Model):
    url = models.URLField(unique=True)
    
    
class hs_test(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)
    

