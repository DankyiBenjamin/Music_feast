from django.db import models
import string
import random

def generate_unique_code():
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # Check if the generated code is unique in the Room model
        if  Room.objects.filter(code=code).count() == 0:
            break

        return code


# Create your models here.

# it is a layer of abstraction that allows you to define the structure of your data,
# including fields, relationships, and constraints, without having to write raw SQL queries.
class Room(models.Model):
    # constraints for the code field
    code = models.CharField(max_length=8, default='', unique=True)
    host = models.CharField(max_length=50, default='', unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)



    
