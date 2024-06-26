from rest_framework import serializers
from check_net_speed.models import UserInternetSpeedData
from validate_email import validate_email
from rest_framework.exceptions import ValidationError

class UserInternetSpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInternetSpeedData
        fields = '__all__'

    def validate_email(self, email):
        if validate_email(email):
            return email
        raise ValidationError('invalid email.')
    
    def validate(self, attrs):
        attributes = ['download_speed', 'upload_speed', 'latency']
        for attr in attrs:
            if attr in attributes:
                if not attrs.get(attr) or attrs[attr] <= 0:
                    raise ValidationError('invalid values.')
        return super().validate(attrs)