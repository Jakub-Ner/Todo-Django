import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class Time(APIView):
    def get(self, _):
        date_time = datetime.datetime.now()
        return Response({'time': date_time.strftime('%Y-%m-%d %H:%M:%S')})


@api_view(['GET'])
def time(_):
    date_time = datetime.datetime.now()
    return Response({'time': date_time.strftime('%Y-%m-%d %H:%M:%S')})

