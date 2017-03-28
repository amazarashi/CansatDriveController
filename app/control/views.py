from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

## RIGHT
## - go(PIN1:ON,PIN2:OFF)
## - back(PIN1:OFF,PIN2:ON)
PIN1 = 11
#p0
PIN2 = 12
#p5
## LEFT
## - go(PIN3:ON,PIN4:OFF)
## - back(PIN3:OFF,PIN4:ON)
PIN3 = 13
#p3
PIN4 = 15
#p4

GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

# PIN1_STATUS = False
# PIN2_STATUS = False
# PIN3_STATUS = False
# PIN4_STATUS = False
#
# GPIO.output(PIN1, True)
# GPIO.output(PIN2, PIN2_STATUS)
# GPIO.output(PIN3, True)
# GPIO.output(PIN4, PIN4_STATUS)
#
# GPIO.cleanup()

def controller(request):
    if request.method == 'GET':
        return render(request, 'controler/index.html',{})
    else:
        return statusHandler(request)

@csrf_exempt
def statusHandler(request):
    if request.method == 'POST':
        command = request.POST['command']
        status = request.POST["status"]
        pinHandler(request,command=command,status=status)
        res = json.dumps({'status':"success"})
        return HttpResponse(res,content_type="application/json")
    else:
        return HttpResponse({"message":"error"},content_type="application/json")
        # raise Http404

def pinHandler(request,command,status):
    print("## command ## : ",command)
    print("## status ## : ",status)
    ## RIGHT WHEEL
    ## - go(PIN1:ON,PIN2:OFF)
    ## - back(PIN1:OFF,PIN2:ON)
    ## LEFT WHEEL
    ## - go(PIN3:ON,PIN4:OFF)
    ## - back(PIN3:OFF,PIN4:ON)
    if command == "forward" and status == "on":
        print("forward : on")
        PIN1_STATUS = True
        PIN3_STATUS = True
        GPIO.output(PIN3, PIN3_STATUS)
        GPIO.output(PIN1, PIN1_STATUS)
    elif command == "forward" and status == "off":
        print("forward : off")
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
        GPIO.output(PIN1, PIN1_STATUS)
        GPIO.output(PIN2, PIN2_STATUS)
        GPIO.output(PIN3, PIN3_STATUS)
        GPIO.output(PIN4, PIN4_STATUS)
    elif command == "backward" and status == "on":
        PIN2_STATUS = True
        PIN4_STATUS = True
        GPIO.output(PIN1, PIN1_STATUS)
        GPIO.output(PIN2, PIN2_STATUS)
        GPIO.output(PIN3, PIN3_STATUS)
        GPIO.output(PIN4, PIN4_STATUS)
    elif command == "backward" and status == "off":
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
        GPIO.output(PIN1, PIN1_STATUS)
        GPIO.output(PIN2, PIN2_STATUS)
        GPIO.output(PIN3, PIN3_STATUS)
        GPIO.output(PIN4, PIN4_STATUS)
    elif command == "right_go" and status == "on":
        PIN1_STATUS = True
        GPIO.output(PIN1, PIN1_STATUS)
    elif command == "right_go" and status == "off":
        PIN1_STATUS = False
        GPIO.output(PIN1, PIN1_STATUS)
    elif command == "right_back" and status == "on":
        PIN2_STATUS = True
        GPIO.output(PIN2, PIN2_STATUS)
    elif command == "right_back" and status == "off":
        PIN2_STATUS = False
        GPIO.output(PIN2, PIN2_STATUS)
    elif command == "left_go" and status == "on":
        PIN3_STATUS = True
        GPIO.output(PIN3, PIN3_STATUS)
    elif command == "left_go" and status == "off":
        PIN3_STATUS = False
        GPIO.output(PIN3, PIN3_STATUS)
    elif command == "left_back" and status == "on":
        PIN4_STATUS = True
        GPIO.output(PIN4, PIN4_STATUS)
    elif command == "left_back" and status == "off":
        PIN4_STATUS = False
        GPIO.output(PIN4, PIN4_STATUS)
    else:
        PIN1_STATUS = False
        PIN2_STATUS = False
        PIN3_STATUS = False
        PIN4_STATUS = False
        GPIO.output(PIN1, PIN1_STATUS)
        GPIO.output(PIN2, PIN2_STATUS)
        GPIO.output(PIN3, PIN3_STATUS)
        GPIO.output(PIN4, PIN4_STATUS)
    return
