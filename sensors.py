import binascii, os, time, subprocess, androidhelper

def hex_encode(_input):
    return str(binascii.hexlify(str.encode(str(_input)))) 

subprocess.Popen('su', shell=True) # root shell
subprocess.Popen('ls /', shell=True)
#subprocess.Popen('echo $(tty); cat /dev/ttyACM0 > $(tty) &', shell=True) # 
#subprocess.Popen('echo -e "AT\r" > /dev/ttyACM0 ', shell=True) 

NUMBER_OF_UPDATES = 4
TIME_BETWEEN_UPDATES = 2    # sec
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
        for sensor_data in sensor_data_list:
            for result_value in sensor_data:
                truncated = '{0:.{1}f}'.format(result_value, PRECISION)
                #floor, fraction = int(truncated.split(.)[0]), int(truncated.split(.)[1])   # int method
                bytes = truncated.encode('ascii')
                
                

subprocess.Popen('cd {}; pwd; ls -l; wc -l data.txt'.format(path), shell=True)

# stop monitoring 
droid.batteryStopMonitoring()
droid.stopSensing()
droid.wakeLockRelease()

time.sleep(1)