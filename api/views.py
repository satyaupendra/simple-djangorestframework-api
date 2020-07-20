from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import StatusSerializer,StatusDetailSerializer
from .models import Status
from rest_framework.response import Response
class StatusListView(APIView):
    def get(self,request):
        queryset=Status.objects.all()
        serializer=StatusSerializer(queryset,many=True)
        return Response(serializer.data) 
    def post(self,request):
        serializer=StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        data=StatusSerializer(Status.objects.all(),many=True)
        return Response(data) 
class StatusListUsersView(APIView):
    def get(self,request,**kwargs):
        queryset=Status.objects.all()
        user = self.kwargs['user']
        data=StatusSerializer(queryset.filter(user=user),many=True)
        return Response(data.data)

class StatusListDetailsView(APIView):
    def get(self,request,**kwargs):
        queryset=Status.objects.all()
        content=self.kwargs['content']
        data=StatusDetailSerializer(queryset.filter(content__icontains=content),many=True)
        return Response(data.data)

    
