from django.shortcuts import render
from django.views import View
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.decorators import api_view
from check_net_speed.models import UserInternetSpeedData
from rest_framework.exceptions import ValidationError
from check_net_speed.serializers import UserInternetSpeedSerializer
from validate_email import validate_email
import os

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class Ping(GenericAPIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        return Response({'status': 200,
                             'message': 'pong'})
    
class OpenSpeedTest(View):
    def get(self, request):
        return render(request, 'check_speed.html')    

class DownloadSpeed(GenericAPIView):
    def get(self, request):
        file_path = os.path.join('media', 'test100mb.txt')
        try:
            file = open(file_path, 'rb')
            response = FileResponse(file, as_attachment=True, filename='test100msb.txt')
            return response
        except FileNotFoundError:
            return Response(status=404, data={'error': 'File not found'})

class UploadSpeed(GenericAPIView):
    def post(self, request):
        return Response({'status': 200,
                'message': 'upload success'})

class UserInternetSpeed(ListCreateAPIView):
    queryset = UserInternetSpeedData.objects.all()
    throttle_classes = [AnonRateThrottle]
    serializer_class = UserInternetSpeedSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        if not email:
            raise ValidationError('email field not provided.')
        if not validate_email(email):
            raise ValidationError('invalid email provided.')
        return UserInternetSpeedData.objects.filter(email=email).all()
    