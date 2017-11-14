import socket, binascii, os, time, subprocess, androidhelper

def hex_encode(_input):   # float -> string
    _input = str(_input).encode('ascii')
    bytess = binascii.hexlify(_input)        
    return bytess.decode('ascii')
    
def hex_decode(_input):   # float -> string
    bytess = binascii.unhexlify(_input)
    return bytess.decode('ascii')
    
def ATcmd(_cmd):
    subprocess.Popen('echo -e "{}\r" > /dev/ttyACM0 '.format(_cmd), shell=True) 
    
def udp_send(_bytes):
    print("UDP target IP:" + UDP_IP)
    print("UDP target port:" + str(UDP_PORT))
    print("message:" + MESSAGE.decode('ascii'))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))    # takes bytes string
    
def nb_send(_hexstring):
    ATcmd('AT+NSOST=0,178.97.147.105,5005,{},{}'.format(int(len(_hexstring) / 2), _hexstring))

subprocess.Popen('su', shell=True) # root shell
#subprocess.Popen('ls /', shell=True) #root test
#subprocess.Popen('echo $(tty); cat /dev/ttyACM0 > $(tty) &', shell=True)    # show AT responses
#subprocess.Popen('echo -e "AT\r" > /dev/ttyACM0 ', shell=True)     # AT cmd test

# client constants
UDP_IP = "178.48.49.12"
UDP_PORT = 5005
MESSAGE = ''

# sensing constants 
NUMBER_OF_UPDATES = 4
TIME_BETWEEN_UPDATES = 8    # sec
PRECISION = 3

path = '/storage/emulated/0/qpython/test/'
data_path = os.path.join(path, 'data.txt')
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

    sensor_data_list = [orient, accel, magneto, [light], [battery]] 

    print('Saving data...')
    with open(data_path, 'a') as f:
    	sensors_data_string = ''
        for sensor_data in sensor_data_list:
        	sensor_data_string = ''
            for result_value in sensor_data:
                truncated = '{0:.{1}f}'.format(result_value, PRECISION)
                #floor, fraction = int(truncated.split(.)[0]), int(truncated.split(.)[1])   # int method
                hexstring = hex_encode(truncated)   # hexstring method
                sensor_data_string.append(hexstring + ' ')
            sensors_data_string.append(sensor_data_string)
        nb_send(sensors_data_string)
        f.write(sensors_data_string)
        f.write('\n#\n')

#subprocess.Popen('cd {}; pwd; ls -l; wc -l data.txt'.format(path), shell=True)

# stop monitoring 
droid.batteryStopMonitoring()
droid.stopSensing()
droid.wakeLockRelease()

time.sleep(1)