import sys

if (sys.argv >= 2):
    ATcmd(argv[1])

def ATcmd(_cmd):
	subprocess.Popen('echo -e "{}\r" > /dev/ttyACM0 '.format(_cmd), shell=True) 