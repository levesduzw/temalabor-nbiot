## NB-IoT és okostelefonok: közös felhasználási lehetőségek
#### BME Témalabor projekt

Kommunikáció megvalósítása az Ericsson Narrowband IoT teszthálózatán.

![Setup](https://i.imgur.com/hBA9YFY.jpg)

## Cél

A feladat elsődleges célja az volt, hogy megvizsgáljam a piacon levő Arduino NB-IoT Shield-ek okostelefonról való vezérelhetőségét.

## Részletek

Az okostelefon szenzorainak adatait elküldi egy UDP Socket szerverre. Az okostelefon az Internetre közvetlenül nem csatlakozik, az NB-IoT hálózatot használja adatok küldésére.

#### A telefon felülete:

![A telefon felülete](https://i.imgur.com/lYcJTJW.jpg)

#### A szerver által megjelenített weboldal:

![A szerver által megjelenített weboldal](https://i.imgur.com/wFQGvNu.jpg)

#### Példakód (az elforgatás szenzor adatainak kiolvasása):
```python
import androidhelper
droid = androidhelper.Android()
droid.startSensingTimed(1, 250) # 1: all sensors, 250: minimum time between readings
orientation = droid.sensorsReadOrientation().result
```

[Szenzoradatok - ural2 weboldal](http://users.hszk.bme.hu/~sl1308/) 152.66.130.2

[Szóbeli beszámoló slideshow](https://goo.gl/Q8ppgK)

## Egyéb

#### Fontosabb forrásfájlok:
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


#### AT parancsok Termux-ból:
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


#### Parancsok teszteléshez:
```
AT+CGATT?
AT+CGPADDR
AT+NCONFIG?
AT+NUESTATS
AT+NPING=8.8.8.8
```


#### Üzenetküldés:
```
AT+NSOCR=DGRAM,17,42000,1
AT+NSOST=0,152.66.130.2,5005,4,deadbeef
```
