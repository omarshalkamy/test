from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import location
from .serializers import locationSerializer

class locationview(APIView):
    def get(self, request, format=None):
        users = location.objects.all()
        serializer = locationSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = locationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class locationdetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return location.objects.get(pk=pk)
        except location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loc = self.get_object(pk)
        loc = locationSerializer(loc)
        return Response(loc.data)

    def put(self, request, pk, format=None):
        loc = self.get_object(pk)
        serializer = locationSerializer(loc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        loc = self.get_object(pk)
        loc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






















