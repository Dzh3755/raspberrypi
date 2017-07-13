import RPi.GPIO as GPIO
import time
from bluetooth import*
server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)
uuid = "00001101-0000-1000-8000-00805f9b34fc"
advertise_service(server_sock, "ChristinesPiServer",
                  service_id = uuid,
                  service_classes = [uuid, SERIAL_PORT_CLASS],
                  profiles = [SERIAL_PORT_PROFILE],
                 )

while True:
    print "Waiting for connection on RFCOMM"
    client_sock, client_info = server_sock.accept()

    print "Accepted connection from: ", client_info
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11,GPIO.OUT)
    
    data = client_sock.recv(1024)
    if len(data) != 0:
        print "received [%s]" % data
        if data == 'on':
            print "LED on"
            GPIO.output(11,GPIO.HIGH)
            
        elif data == 'off':
            print "LED off"
            GPIO.output(11,GPIO.LOW)
    client_sock.close()

    


   




