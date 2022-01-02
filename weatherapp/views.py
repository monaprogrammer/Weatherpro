from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def description(request):
    return Response({'city': 'California'})

@api_view()
def the_weather(request):
    the_weather = Weatherapi.abjects.all()
    ser_data = Weatherapiserializer(the_weather, many=True)
    return Response(ser_data.data)
