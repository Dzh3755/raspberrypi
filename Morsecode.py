import RPi.GPIO as GPIO
import time
from bluetooth import*

def ToMorse(data):
    codes = {'A': '.-', 'B': '-...', 'C': '-.-.',
             'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..',
             'M': '--', 'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',
             'S': '...', 'T': '-', 'U': '..-',
             'V': '...-', 'W': '.--', 'X': '-..-',
             'Y': '-.--', 'Z': '--..', '0': '-----',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             ' ': '='}
             
    print (data)             
    data = data.upper()
    chars = list(data)
    for i in range(len(chars)):
        chars[i] = codes[chars[i]]
    dots=''.join(chars)
    return dots               

def main():
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
        GPIO.setup(13,GPIO.OUT)
        print("1")
        data = client_sock.recv(2048)
        print("2")    
        data = ToMorse(data)
        print("3")
        if len(data) != 0:
            for char in range(len(data)):
                time.sleep(1)
                if data[char] == '.':
                    print "Dot"
                    GPIO.output(11,GPIO.HIGH)
                    time.sleep(.2)
                    GPIO.output(11,GPIO.LOW)
                    
                elif data[char] == '-':
                    print "Dash"
                    GPIO.output(11,GPIO.HIGH)
                    time.sleep(1.5)
                    GPIO.output(11,GPIO.LOW)

                elif data[char] == '=':
                    print "Space"
                    GPIO.output(13,GPIO.HIGH)
                    time.sleep(.5)
                    GPIO.output(13,GPIO.LOW)
                
        client_sock.close()
main()
