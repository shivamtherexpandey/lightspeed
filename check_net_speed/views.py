from django.shortcuts import render
from django.views import View
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from django.http import FileResponse
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from check_net_speed.models import UserInternetSpeedData
from rest_framework.exceptions import ValidationError
from check_net_speed.serializers import UserInternetSpeedSerializer
from validate_email import validate_email
import os
from django.http import StreamingHttpResponse

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class Ping(APIView):
    throttle_classes = [AnonRateThrottle]
    def get(self, request):
        return Response({'status': 200,
                             'message': 'pong'})

def generate_large_file(size_in_mb):
    chunk_size = 1024 * 1024
    for _ in range(size_in_mb):
        yield b'0' * chunk_size

class DownloadSpeed(APIView):
    throttle_classes = [AnonRateThrottle]
    
    def get(self, request):
        file_path = os.path.join('media', 'test20mb.pdf')
        try:
            file = open(file_path, 'rb')
            response = FileResponse(file, as_attachment=True, filename='test20mb.pdf')
            return response
        except FileNotFoundError:
            return Response(status=404, data={'error': 'File not found'})
        # response = StreamingHttpResponse(generate_large_file(100), content_type='application/octet-stream')
        # response['Content-Disposition'] = 'attachment; filename="testfile.bin"'
        # return response

class UploadSpeed(APIView):
    throttle_classes = [AnonRateThrottle]
    def post(self, request):
        uploaded_file = request.FILES['file']
        # print(f'File Received {uploaded_file.size} Bytes')
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
    
class OpenSpeedTest(View):
    def get(self, request):
        return render(request, 'check_speed.html') 