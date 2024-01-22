from django.shortcuts import render
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer, ListingDetailSerializer
from datetime import datetime, timezone, timedelta


class ListingListView(ListAPIView):
    permission_classes =(permissions.AllowAny, )
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingSerializer
    lookup_field = 'slug'


class ListingView(RetrieveAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'


class SearchListingView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer

    def post(self, request, format=None):
        data = self.request.data 
        queryset = Listing.objects.order_by('-list_date').filter(is_published=True)

        sale_type = data.get('sale_type', 'For Sale')
        queryset = queryset.filter(sale_type__iexact=sale_type)

        price = int(data.get('price', '-1')) 
        if price != -1:
            queryset = queryset.filter(price__gte=price)

        bedrooms = data.get('bedrooms', [])
        bedrooms = [int(x) for x in bedrooms]
        if bedrooms != []:
            queryset = queryset.filter(bedrooms__in=bedrooms)

        sqft = int(data.get('sqft', '0'))  
        if sqft != 0:
            queryset = queryset.filter(sqft__gte=sqft)  

        home_type = data.get('home_type', 'House')
        queryset = queryset.filter(home_type__iexact=home_type)

        days_passed = data.get('days_passed', 'Any')
        if days_passed == 'Within 1 day':
            days_passed = 1
        elif days_passed == 'Within a week':
            days_passed = 7 
        elif days_passed == 'Within a month':
            days_passed = 31
        elif days_passed == 'Any':
            days_passed = 0

        if days_passed != 0:
            queryset = queryset.annotate(num_days=(datetime.now(timezone.utc) - 'list_date').days)
            queryset = queryset.filter(num_days__lte=days_passed)
            # for query in queryset:
            #     num_days = (datetime.now(timezone.utc) - query.list_date).days  
            #     if num_days > days_passed:
            #         slug = query.slug 
            #         queryset = queryset.exclude(slug__iexact=slug)  


        has_photos = data.get('has_photos', False)
        if has_photos == True:
            queryset = queryset.annotate(num_photos=Count('photos')).filter(num_photos__gte=0)

        keywords = data.get('keywords', '') 
        if keywords != '':
            queryset = queryset.filter(description__icontains=keywords)

        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)           







