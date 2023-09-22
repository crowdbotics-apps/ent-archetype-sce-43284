from rest_framework import serializers
from oda.models import Event,Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"