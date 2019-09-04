from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, CharField
from django.contrib.auth.hashers import make_password,is_password_usable,check_password
import string
import random 
from django.forms import BaseModelFormSet
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import MinimumLengthValidator, validate_password, password_validators_help_text_html
from django.shortcuts import render,redirect
from datetime import *
from django.http import HttpResponseRedirect, HttpResponse,QueryDict






	


