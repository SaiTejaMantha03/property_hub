from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Advertisement(models.Model):
    CATEGORY_CHOICES = [
        ('property', 'Property'),
        ('vehicles', 'Vehicles'),
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('clothing', 'Clothing'),
        ('services', 'Services'),
        ('jobs', 'Jobs'),
        ('education', 'Education'),
        ('pets', 'Pets'),
        ('other', 'Other'),
    ]
    
    AD_TYPE_CHOICES = [
        ('sell', 'For Sale'),
        ('buy', 'Want to Buy'),
        ('rent', 'For Rent'),
        ('service', 'Service Offered'),
        ('job', 'Job Posting'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200, help_text="Brief title for your ad")
    description = models.TextField(help_text="Detailed description of your item/service")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    ad_type = models.CharField(max_length=10, choices=AD_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Leave blank if not applicable")
    
    # Contact Information
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    
    # Location
    location = models.CharField(max_length=200, help_text="City, State or Area")
    address = models.CharField(max_length=300, blank=True, help_text="Optional detailed address")
    
    # Additional Details
    condition = models.CharField(max_length=50, blank=True, help_text="e.g., New, Used, Like New")
    brand = models.CharField(max_length=100, blank=True, help_text="Brand name if applicable")
    
    # Meta Information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    
    # User who posted the ad (optional)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.location}"
    
    def get_absolute_url(self):
        return reverse('ad_detail', kwargs={'pk': self.pk})

class AdImage(models.Model):
    advertisement = models.ForeignKey(Advertisement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad_images/')
    caption = models.CharField(max_length=200, blank=True)
    is_main = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"Image for {self.advertisement.title}"

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condominium'),
        ('villa', 'Villa'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]
    
    LISTING_TYPES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    
    # Location details
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    # Property details
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    area_sqft = models.IntegerField(help_text="Area in square feet")
    
    # Contact information
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    
    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.city}, {self.state}"
    
    def get_absolute_url(self):
        return reverse('property_detail', kwargs={'pk': self.pk})

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    caption = models.CharField(max_length=200, blank=True)
    is_main = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']
    
    def __str__(self):
        return f"Image for {self.property.title}"
