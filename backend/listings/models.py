from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class HomeType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'Town House'   

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    # will set the slug field blank for now and 
    # will slugify title and store here later using a pre_save function
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=100, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    home_type = models.CharField(max_length=150, choices=HomeType.choices, default=HomeType.HOUSE)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    # here main_photo is linked to Photo class below and it will be set to null 
    # when the photo linked to this field is deleted
    main_photo = models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True, related_name='main_photo_listing', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    realtor = models.ForeignKey('realtors.Realtor', on_delete=models.SET_NULL, null=True, related_name='listings')

    def __str__(self):
        return self.title
    
# pre_save function to change slug value based on title if slug is nil    
@receiver(pre_save, sender=Listing)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    
    

""" Here a listing can have many photos and each photo belongs to a  
 particular Listing
""" 
class Photo(models.Model):
    image = models.ImageField(upload_to='listing_photos/')
    # related_name param indicates the field name for this model in 
    # Listing model. Here it will be photos field in Listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='photos')

    def __str__(self) -> str:
        return f'Listing: {self.listing}, Photo {self.pk}'


