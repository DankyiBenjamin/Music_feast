# serializers take takes a model and converts it to a JSON format 
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # Specify the fields to be included in the serialized output
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
        read_only_fields = ('id', 'created_at')