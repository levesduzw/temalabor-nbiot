import socket, binascii, os, time, subprocess, androidhelper
from datetime import datetime

def hex_encode(_input):   # returns string
    _input = str(_input).encode('ascii')
    bytess = binascii.hexlify(_input)        
    return bytess.decode('ascii')
    
def hex_decode(_input):   # returns string
    bytess = binascii.unhexlify(_input)
    return bytess.decode('ascii')
    
def ATcmd(_cmd):
    print('Sending {}'.format(_cmd))
    subprocess.Popen('echo -e "{}\r" > /dev/ttyACM0'.format(_cmd), shell=True) 
    
def udp_send(MESSAGE):
    print("Sent message at " + datetime.now().strftime("%H:%M:%S.%f"))
    print("message: " + MESSAGE)
    MESSAGE = hex_encode(MESSAGE)
    print("encoded: " + MESSAGE)
    MESSAGE = MESSAGE.encode('ascii')   # convert to 'bytes'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))    # takes bytes string
    
def nb_send(_hexstring):    # assumes hexstring is at least 2 bytes long
    print("Sent NB message at " + datetime.now().strftime("%H:%M:%S.%f"))
    _hexstring = hex_encode(_hexstring)
    print('message: {}... length:  {}'.format(_hexstring[:5], int(len(_hexstring) / 2)))
    ATcmd('AT+NSOST=1,152.66.130.2,5005,{},{}'.format(int(len(_hexstring) / 2), _hexstring))
    
def nb_create_socket(): # not called from code yet
    print('Creating socket 1.')
    ATcmd('AT+NSOCR=DGRAM,17,42000,1')
    
def ATresponse():
    ## nb_send()-be time.sleep(2) és call this?
    with open(response.txt, 'r') as f:
        print(f.readline())
    
def main():
    subprocess.Popen('su', shell=True) # root 
    #subprocess.Popen('ls /', shell=True) #root test
    subprocess.Popen('cd ' + path, shell=True)
    #subprocess.Popen('echo $(tty); cat /dev/ttyACM0 > $(tty) &', shell=True)    # show AT responses
    #subprocess.Popen('echo $(tty); cat /dev/ttyACM0 > response.txt &', shell=True)    # show AT responses
    #subprocess.Popen('echo -e "AT\r" > /dev/ttyACM0', shell=True)     # AT cmd test

    # client constants
    #UDP_IP = "178.48.49.12"     # otthoni
    UDP_IP = "152.66.130.2"     # ural2.hszk.bme.hu
    UDP_PORT = 5005
    MESSAGE = ''

    # sensing constants 
    NUMBER_OF_UPDATES = 6
    TIME_BETWEEN_UPDATES = 4    # sec
    PRECISION = 3

    path = '/storage/emulated/0/qpython/test/'
    data_path = os.path.join(path, 'local_data.txt')
    os.chdir(path)
    if os.path.isfile(data_path): os.remove(data_path)

    # start monitoring 
    droid = androidhelper.Android()
    droid.batteryStartMonitoring()
    droid.startSensingTimed(1, 250)    # 1: all sensors, 250: minimum time between readings
    droid.wakeLockAcquirePartial()     # run even when screen is off

    for i in range(NUMBER_OF_UPDATES):
        time.sleep(TIME_BETWEEN_UPDATES)
        
        # get sensor data
        orient = droid.sensorsReadOrientation().result
        accel = droid.sensorsReadAccelerometer().result
        magneto = droid.sensorsReadMagnetometer().result 
        light = droid.sensorsGetLight().result
        battery = droid.batteryGetLevel().result

        sensors_data_list = [orient, accel, magneto, [light], [battery]] 

        print('Saving data...')
        with open(data_path, 'a') as f:
            LIST = []
            for sensor_data in sensors_data_list:
                sensor_data_list = []
                for result_value in sensor_data:
                    truncated = '{0:.{1}f}'.format(result_value, PRECISION)
                    sensor_data_list.append(truncated + ' ')
                LIST.append(''.join(sensor_data_list))	# string
            LIST = ''.join(LIST)

            udp_send(LIST) 
            #nb_send(LIST) # ~150 karakter

            f.write(LIST)
            f.write('\n#\n')
            
            # ATresponse()  # nem tesztelve

    # stop monitoring 
    droid.batteryStopMonitoring()
    droid.stopSensing()
    droid.wakeLockRelease()

    time.sleep(1)

if __name__ == "__main__":
    main()