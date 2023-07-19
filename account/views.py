from rest_framework.views import APIView
from .serializers import RegisterSerializer, ActivationSerializer
from rest_framework.response import Response
from .send_email import send_confirmation_email
from rest_framework import generics


class RegistrationView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(user.email, 'http://127.0.0.1:8000/api/account/activate/?activation_code='+str(user.activation_code))
            except:
                return Response({'message': 'Registered, but wasnt able to send activation code',
                                 'data': serializer.data}, status=201)

        return Response(serializer.data, status=201)


class ActivationView(generics.GenericAPIView):
    serializer_class = ActivationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully activated', status=200)
