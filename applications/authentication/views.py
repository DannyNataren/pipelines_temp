from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.tokens import RefreshToken
from applications.users.serializers import UserSerializer
from utils.response import ResponseModel


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = UserSerializer(user, context={'request': request})
        data = user_serializer.data
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        refresh_token = str(refresh)
        data.pop("password")
        data["token"] = token
        data["refresh_token"] = refresh_token
        response = ResponseModel.post_respond(data, True, title="loggeado")
        return Response(response)

