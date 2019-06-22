from rest_framework import serializers
from .models import Profile

class demoserialzer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'address' )