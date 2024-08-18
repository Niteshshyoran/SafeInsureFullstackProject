from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer,CompanySerializer,ClaimSerializer,PolicySerializer,PaymentSerializer
from .models import Company,Policy,Claim,Payment,Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
import jwt,datetime
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# class PasswordResetRequestView(APIView):
#     def post(self,requst):
#         email = requst.data['email']
#         return Response('ok')


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            profile = Profile(user=user, user_type = request.data.get('user_type'))
            profile.save()
            # serializer.save()
            return Response({'message':'Signup Sucessfull',"userdetails":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message':'Invalid Credentials'}, status=status.HTTP_406_NOT_ACCEPTABLE)



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')



        user = authenticate(username=username,password=password) # User.objects.filter(username = username).first()
        # print(user)
        if user is None:
            return Response({'detail':'user not register, please signup'}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.check_password(password):
            return Response({'detail':'wrong password, please try again'},status=status.HTTP_400_BAD_REQUEST)
        
        # login(request,user)
        # return Response({'message':"login Sucessfull"},status=status.HTTP_200_OK)

        ## creating token

        payload = {
            'id':user.id,
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(datetime.UTC)
        }
        token = jwt.encode(payload, 'cap01',algorithm='HS256')
        response = Response()
        response.data = {'message':'login sucessfull','token':token}
        response.status=status.HTTP_200_OK
        response.set_cookie(
            key='jwt',
            value=token,
            httponly=True, # frontend ke lea true karna hoga
            samesite=None,
            secure=None,
        )
        return response



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # If you are using a blacklist, you would add the token to the blacklist here
        # For simplicity, we'll just return a response indicating the user is logged out
        response = Response()
        response.data = {"message": "Successfully logged out"}
        return response



class CompanyRegisterView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class CompanyUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class PolicyRegisterView(CreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class PolicyUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class ClaimRegisterView(CreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class PaymentRegisterView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
