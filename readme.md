## BME Témalabor projekt

[Google Slides prezentáció](https://goo.gl/Q8ppgK)


[Szenzoradatok - ural2 weboldal](http://users.hszk.bme.hu/~sl1308/) 152.66.130.2


Fontosabb forrásfájlok:
* csak Interneten történő adatküldés (tesztelés)
  * client_main_UDP.py - adatok küldése
  * socket/server_sunos_UDP.py - adatok fogadása
* NB-IoT hálózaton történő adatküldés 
  * client_main_NB.py - adatok küldése
  * socket/server_sunos_NB.py - adatok fogadása
* adatok megjelenítése
  * public_html/index.html
* Arduino Passthrough Script
  * Arduino/at_sketch.c


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
