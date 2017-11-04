import os, time, subprocess, androidhelper

time.sleep(1)

path = '/storage/emulated/0/qpython/test/'
data_path = os.path.join(path, 'data.txt')
cmd = ['cd', '..']
os.chdir(path)
print(os.getcwd())

# start monitoring 
droid = androidhelper.Android()
droid.startSensingTimed(1, 250)
droid.batteryStartMonitoring()

for i in range(10):
    time.sleep(10)
    
    # get sensor data
    battery = droid.batteryGetLevel().result
    magneto = droid.sensorsReadMagnetometer().result 
    print(battery) 
    print(magneto) 

    print('Saving data...')
    with open(data_path, 'a') as f:
        f.write(str(magneto))

#subprocess.Popen('cd {}; pwd; ls'.format(path), shell=True)

# stop monitoring 
droid.stopSensing()
droid.batteryStopMonitoring()
