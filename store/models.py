from django.db.models import * 
from autoslug import AutoSlugField

# Create your models here.


class Categorey(Model):
    name = CharField(max_length=100 , db_index=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
    


class Product(Model):
    name        = CharField(max_length=100 , db_index=True)
    price       = DecimalField(max_digits=5 , decimal_places=2 ,db_index=True)
    description = TextField(max_length=400 ,blank=True ,null=True)
    image       = ImageField(upload_to="static\img", height_field=None, width_field=None, max_length=None)    
    slug        = AutoSlugField(populate_from='name')
    created_at  = DateTimeField(auto_now_add=True)
    updated_at  = DateTimeField(auto_now=True)
    avilable    = BooleanField(default=True)

    categorey   = ForeignKey(Categorey, on_delete=CASCADE , related_name="products")

    def __str__(self):
        return self.name
    
