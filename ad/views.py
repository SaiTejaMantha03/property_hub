from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Property, Advertisement

def home(request):
    """Home page showing featured ads and properties"""
    # Featured advertisements
    featured_ads = Advertisement.objects.filter(is_featured=True, is_active=True)[:6]
    recent_ads = Advertisement.objects.filter(is_active=True)[:8]
    
    # Featured properties (keeping original functionality)
    featured_properties = Property.objects.filter(is_featured=True, is_active=True)[:6]
    recent_properties = Property.objects.filter(is_active=True)[:8]
    
    context = {
        'featured_ads': featured_ads,
        'recent_ads': recent_ads,
        'featured_properties': featured_properties,
        'recent_properties': recent_properties,
    }
    return render(request, 'ad/home.html', context)

def property_list(request):
    """List all properties with filtering and pagination"""
    properties = Property.objects.filter(is_active=True)
    
    # Filtering
    property_type = request.GET.get('property_type')
    listing_type = request.GET.get('listing_type')
    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    bedrooms = request.GET.get('bedrooms')
    
    if property_type:
        properties = properties.filter(property_type=property_type)
    if listing_type:
        properties = properties.filter(listing_type=listing_type)
    if city:
        properties = properties.filter(city__icontains=city)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    if bedrooms:
        properties = properties.filter(bedrooms__gte=bedrooms)
    
    # Pagination
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique cities for filter dropdown
    cities = Property.objects.filter(is_active=True).values_list('city', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'cities': cities,
        'current_filters': {
            'property_type': property_type,
            'listing_type': listing_type,
            'city': city,
            'min_price': min_price,
            'max_price': max_price,
            'bedrooms': bedrooms,
        }
    }
    return render(request, 'ad/property_list.html', context)

def property_detail(request, pk):
    """Detail view for a single property"""
    property = get_object_or_404(Property, pk=pk, is_active=True)
    related_properties = Property.objects.filter(
        city=property.city,
        property_type=property.property_type,
        is_active=True
    ).exclude(pk=property.pk)[:4]
    
    context = {
        'property': property,
        'related_properties': related_properties,
    }
    return render(request, 'ad/property_detail.html', context)

def search(request):
    """Search properties"""
    query = request.GET.get('q')
    properties = Property.objects.filter(is_active=True)
    
    if query:
        properties = properties.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(address__icontains=query) |
            Q(city__icontains=query) |
            Q(state__icontains=query)
        )
    
    paginator = Paginator(properties, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'ad/search_results.html', context)

def advertisement_list(request):
    """List all advertisements with filtering"""
    advertisements = Advertisement.objects.filter(is_active=True)
    
    # Filtering
    category = request.GET.get('category')
    ad_type = request.GET.get('ad_type')
    location = request.GET.get('location')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if category:
        advertisements = advertisements.filter(category=category)
    if ad_type:
        advertisements = advertisements.filter(ad_type=ad_type)
    if location:
        advertisements = advertisements.filter(location__icontains=location)
    if min_price:
        advertisements = advertisements.filter(price__gte=min_price)
    if max_price:
        advertisements = advertisements.filter(price__lte=max_price)
    
    # Pagination
    paginator = Paginator(advertisements, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique locations for filter dropdown
    locations = Advertisement.objects.filter(is_active=True).values_list('location', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'locations': locations,
        'current_filters': {
            'category': category,
            'ad_type': ad_type,
            'location': location,
            'min_price': min_price,
            'max_price': max_price,
        }
    }
    return render(request, 'ad/advertisement_list.html', context)

def advertisement_detail(request, pk):
    """Detail view for a single advertisement"""
    advertisement = get_object_or_404(Advertisement, pk=pk, is_active=True)
    
    # Increment view count
    advertisement.views_count += 1
    advertisement.save()
    
    # Get related advertisements
    related_ads = Advertisement.objects.filter(
        category=advertisement.category,
        is_active=True
    ).exclude(pk=advertisement.pk)[:4]
    
    context = {
        'advertisement': advertisement,
        'related_ads': related_ads,
    }
    return render(request, 'ad/advertisement_detail.html', context)
