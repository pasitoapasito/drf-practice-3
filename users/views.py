from rest_framework.views       import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response    import Response
from drf_yasg.utils             import swagger_auto_schema

from users.serializers          import SingupSerializers

    
class UserSignupView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(request_body=SingupSerializers, responses={201: SingupSerializers})
    def post(self, request):
        serializer = SingupSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class UserinfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(responses={200: 'user authorization success'})
    def get(self, request):
        user = request.user
        return Response({'message' : f'{user.nickname} Authorization success'}, status=200)