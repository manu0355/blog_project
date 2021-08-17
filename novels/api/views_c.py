from novels.models import Post
from novels.api.serializer import Postserializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class Detailpostview(APIView):
    # authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        postobj = Post.objects.all()
        postserializer = Postserializer(postobj, many=True)
        return Response(postserializer.data, status = status.HTTP_200_OK)

    def post(self,request,*args, **kwargs):
        postserializer = Postserializer(data= request.data)
        if postserializer.is_valid():
            postserializer.save()



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def blogview(request):
    postobj = Post.objects.all()
    postserializer = Postserializer(postobj, many = True)
    return Response(postserializer.data, status = status.HTTP_200_OK)


class Detailpost_page(generics.ListAPIView):
    queryset= Post.objects.all()
    serializer_class = Postserializer
    pagination_class = PageNumberPagination