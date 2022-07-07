"""kursovaya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include, re_path
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import routers, serializers, viewsets, status, pagination, generics, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from crud.models import Equipment_models, Records, Cities
from django.conf import settings

def trigger_error(request):
    division_by_zero = 1 / 0

class RecordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Records
        fields = ['city', 'date', 'temperature', 'humidity', 'windspeed',]

    def validate_humidity(self, humidity):
        if (humidity < 0):
            raise ValidationError('Влажность не может быть меньше нуля')
        return humidity

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Records
        fields = ['temperature',]

class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer
    action_serializers = {
        'change_temperature': TemperatureSerializer
    }
    @action(methods=['GET'], detail=False)
    def zero_temperature(self, request):
        zero_records = Records.objects.filter(Q(temperature = 0))
        page = self.paginate_queryset(zero_records)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(zero_records, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def change_temperature(self, request, pk = None):
        record = self.get_object()
        serializer = TemperatureSerializer(data = request.data)
        print(record)
        if (serializer.is_valid()):
            temperature = serializer.validated_data['temperature']
            record.temperature = temperature
            record.save()
            return Response({
                'status': 'Температура изменена'
            })
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(MyModelViewSet, self).get_serializer_class()



    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']


class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cities
        fields = ['city', 'city_coords',]

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'city_coords',]

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment_models
        fields = ['equipment_type', 'equipment_cost', 'equipment_model']
        
        

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment_models.objects.all()
    serializer_class = EquipmentSerializer

    filter_backends = (filters.OrderingFilter,)
    ordering = ('equipment_model')


api_router = routers.DefaultRouter()
api_router.register(r'records', RecordsViewSet)
api_router.register(r'cities', CitiesViewSet)
api_router.register(r'equipment_models', EquipmentViewSet)

urlpatterns = [
    re_path(r'^api-auth/', include(api_router.urls)),
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('data/', include('crud.urls')),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

