
# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server
import RPi.GPIO as GPIO

led = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
# Function that is ran when a http request comes in
def simple_app(env, start_response):



    ##  set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    # What did the user ask for?
    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
        GPIO.output(led, True)
        return "got on"

    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")
        GPIO.output(led, False)
        return "got off"
    else:
        print("user asked for something else")
        return "<html><body><a href=\"/on\">ON!</a><a href=\"/off\">off</a></bo$

# Create a small python server
httpd = make_server("", 8000, simple_app)
print "Serving on port 8000..."
print "You can open this in the browser http://192.168.1.xxx:8000 where xxx is $"
print "Or if you run this server on your own computer then http://localhost:800$"
httpd.serve_forever()

