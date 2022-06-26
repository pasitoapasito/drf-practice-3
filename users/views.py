from rest_framework.views            import APIView
from rest_framework.permissions      import AllowAny, IsAuthenticated
from rest_framework.response         import Response

from users.serializers               import SingupSerializers

    
class UserSignupView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SingupSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)