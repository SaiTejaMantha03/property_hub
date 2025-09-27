from django.contrib import admin
from .models import Advertisement, AdImage, Property, PropertyImage

class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 3
    fields = ['image', 'caption', 'is_main', 'order']

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'ad_type', 'price', 'location', 'contact_name', 'is_active', 'is_featured', 'created_at']
    list_filter = ['category', 'ad_type', 'location', 'is_active', 'is_featured', 'created_at']
    search_fields = ['title', 'description', 'location', 'contact_name', 'contact_phone']
    list_editable = ['is_active', 'is_featured']
    inlines = [AdImageInline]
    readonly_fields = ['views_count', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Ad Information', {
            'fields': ('title', 'description', 'category', 'ad_type', 'price')
        }),
        ('Contact Details', {
            'fields': ('contact_name', 'contact_phone', 'contact_email')
        }),
        ('Location', {
            'fields': ('location', 'address')
        }),
        ('Additional Info', {
            'fields': ('condition', 'brand', 'posted_by'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_active', 'is_featured')
        }),
        ('Statistics', {
            'fields': ('views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(AdImage)
class AdImageAdmin(admin.ModelAdmin):
    list_display = ['advertisement', 'caption', 'is_main', 'order']
    list_filter = ['is_main', 'advertisement__category']
    list_editable = ['is_main', 'order']

# Keep existing Property models
admin.site.register(Property)
admin.site.register(PropertyImage)
