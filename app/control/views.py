from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
from django.views.decorators.csrf import csrf_protect
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
PIN1 = 11
#p0
PIN2 = 12
#p5
PIN3 = 13
#p3
PIN4 = 23
#p4
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

PIN1_STATUS = False
PIN2_STATUS = False
PIN3_STATUS = False
PIN4_STATUS = False

GPIO.output(PIN1, PIN1_STATUS)
GPIO.output(PIN2, PIN2_STATUS)
GPIO.output(PIN3, PIN3_STATUS)
GPIO.output(PIN4, PIN4_STATUS)

GPIO.cleanup()

def controller(request):
    if request.method == 'GET':
        return render(request, 'controler/index.html',{})
    else:
        return statusHandler(request)

def statusHandler(request):
    if request.method == 'POST':
        command = request.POST['command']
        status = request.POST["status"]
        pinHandler(command=command,status=status)
        res = json.dumps({'status':"success"})
        return HttpResponse(res,content_type="application/json")
    else:
        return HttpResponse({"message":"error"},content_type="application/json")
        # raise Http404

def pinHandler(request,command,status):
    if command == "forward" and status == "on":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "forward" and status == "off":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "backward" and status == "on":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "backward" and status == "off":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "right_go" and status == "on":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "right_go" and status == "off":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "right_back" and status == "on":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "right_back" and status == "off":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "left_go" and status == "on":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "left_go" and status == "off":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "left_back" and status == "on":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    elif command == "left_back" and status == "off":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    else:
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
    return
