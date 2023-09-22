from rest_framework import authentication
from oda.models import Event,Event,Event
from .serializers import EventSerializer,EventSerializer,EventSerializer
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Event.objects.all()