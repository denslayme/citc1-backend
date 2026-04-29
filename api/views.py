from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Procedure, FAQ, Request
from .serializers import *

# Create your views here.

# REGISTER
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, status=201)
    return Response(serializer.errors, status=400)

# LOGIN
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=400)

# PROCEDURES - GET ALL
@api_view(['GET'])
def get_procedures(request):
    procedures = Procedure.objects.all()
    serializer = ProcedureSerializer(procedures, many=True)
    return Response(serializer.data)

# PROCEDURE - UPDATE
@api_view(['PUT', 'PATCH'])
def update_procedure(request, pk):
    try:
        procedure = Procedure.objects.get(pk=pk)
    except Procedure.DoesNotExist:
        return Response({'error': 'Procedure not found'}, status=404)
    serializer = ProcedureSerializer(procedure, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# PROCEDURE - DELETE
@api_view(['DELETE'])
def delete_procedure(request, pk):
    try:
        procedure = Procedure.objects.get(pk=pk)
    except Procedure.DoesNotExist:
        return Response({'error': 'Procedure not found'}, status=404)
    procedure.delete()
    return Response({'message': 'Procedure deleted successfully'}, status=204)

# FAQs - GET ALL
@api_view(['GET'])
def get_faqs(request):
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data)

# FAQ - UPDATE
@api_view(['PUT', 'PATCH'])
def update_faq(request, pk):
    try:
        faq = FAQ.objects.get(pk=pk)
    except FAQ.DoesNotExist:
        return Response({'error': 'FAQ not found'}, status=404)
    serializer = FAQSerializer(faq, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# FAQ - DELETE
@api_view(['DELETE'])
def delete_faq(request, pk):
    try:
        faq = FAQ.objects.get(pk=pk)
    except FAQ.DoesNotExist:
        return Response({'error': 'FAQ not found'}, status=404)
    faq.delete()
    return Response({'message': 'FAQ deleted successfully'}, status=204)

# SUBMIT REQUEST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_request(request):
    serializer = RequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# TRACK REQUESTS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def track_requests(request):
    user_requests = Request.objects.filter(user=request.user)
    serializer = RequestSerializer(user_requests, many=True)
    return Response(serializer.data)