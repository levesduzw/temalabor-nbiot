import os, time, subprocess, androidhelper

NUMBER_OF_UPDATES = 12    # sec
TIME_BETWEEN_UPDATES = 10    # sec

path = '/storage/emulated/0/qpython/test/'
data_path = os.path.join(path, 'data.txt')
os.chdir(path)

# start monitoring 
droid = androidhelper.Android()
droid.batteryStartMonitoring()
droid.startSensingTimed(1, 250)    # 1: all senrors, 250: minimum time between readings
droid.wakeLockAcquirePartial()     # run even when screen is off

for i in range(NUMBER_OF_UPDATES):
    time.sleep(TIME_BETWEEN_UPDATES)
    
    # get sensor data
    battery = droid.batteryGetLevel().result
    orient = droid.sensorsReadOrientation().result
    accel = droid.sensorsReadAccelerometer().result
    magneto = droid.sensorsReadMagnetometer().result 
    light = droid.sensorsGetLight().result

    print('Saving data...')
    with open(data_path, 'a') as f:
        f.write('{} # {} # {} # {} # {}\n'.format(str(battery), str(orient), str(accel), str(magneto), str(light)))

#subprocess.Popen('cd {}; pwd; ls'.format(path), shell=True)

# stop monitoring 
droid.batteryStopMonitoring()
droid.stopSensing()
droid.wakeLockRelease()
