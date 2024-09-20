from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from datetime import datetime
from group.models import *
import random

# Create your views here.

def index(request):
        return render (request,"index.html")

# login and sign up related views
