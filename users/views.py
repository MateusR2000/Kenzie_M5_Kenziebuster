from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner, IsAdminOrReadOnly

class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data["is_employee"]:
            serializer.validated_data["is_superuser"] = True
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly | IsAccountOwner]

    def get(self, req: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, found_user)
        serializer = UserSerializer(found_user)
        return Response(serializer.data)

    def patch(self, req: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, found_user)
        serializer = UserSerializer(found_user, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)