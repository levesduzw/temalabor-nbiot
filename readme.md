## BME Témalabor projekt

[Google Slides](https://goo.gl/Q8ppgK)


[http://users.hszk.bme.hu/~sl1308/](http://users.hszk.bme.hu/~sl1308/) 152.66.130.2


AT parancsok Termux-ból:
```
su
cat /dev/ttyACM0 > $(tty) & 
echo -e "AT\r" > /dev/ttyACM0
```
vagy
```
su
cat /dev/ttyACM0 > $(tty) & 
python AT.py AT
```


Parancsok teszteléshez:
```
AT+CGATT?
AT+CGPADDR
AT+NCONFIG?
AT+NUESTATS
AT+NPING=8.8.8.8
```


Üzenetküldés:
```
AT+NSOCR=DGRAM,17,42000,1
AT+NSOST=0,152.66.130.2,5005,4,deadbeef
```
