'''
Vaastu
------------

  Total Site Area  : SA
Construction Area  : CA

    01.Dhana Varga     : (CA x 8) % 12
    02.Runa Varha      : (CA x 3) % 8 
    03.Vaara Varga     : (CA x 9) % 7
    04.Thidhi Varga    : (CA x 6) % 30
    05.Tatva Varga     : (CA x 3) % 5
    06.Lagna Varga     : (CA x 9) % 12
    07.Yoga Varga      : (CA x 4) % 27
    08.Graha Varga     : (CA x 5) % 9
    09.Kula Varga      : (CA x 9) % 4
    10.Kalaa Varga     : (CA x 12) % 16
    11.Nakshatra Varga : (CA x 8) % 27
    12.Aaya Varga      : (CA x 9) % 8
    13.Aayu Varga      : (CA x 9) % 120
    14.Amsha Varga     : (CA x 6) % 9
    15.Dikhpathi Varga : (CA x 9) % 8
    16.Karana Varga    : (CA x 5) % 11


Aayu Varga : if the value is < 60, then Alert (danger).
Aaya Varga : if the value is == 
                1 : then Dwajaya.
                2 : then Dhoomraya.
                3 : then Simhaya.
                4 : then Shunakaya.
                5 : then Vrushabaya.
                6 : then Kharaya.
                7 : then Gajaya.
                0 : then Kakaya.

  Total Site Area (SA) : 30x40
Construction Area (CA) : 21x29

                   (CA x 8) % 12  = Dhana Varga
                   (CA x 3) % 8   = Runa Varga
                   (CA x 9) % 7   = Vara Varga
                   (CA x 6) % 30  = Thithi Varga
                   
'''

import sys

if(len(sys.argv) < 3):
    print("Usage :\n\tvaastu.py <width> <depth>")
    exit(0)

ca_width = int(sys.argv[1])
ca_depth = int(sys.argv[2])

ca = ca_width * ca_depth

print("Total CA : {0}".format(ca))

#01.Dhana Varga     : (CA x 8) % 12
dhana_varga = (ca * 8) % 12
print("Dhana Varga : {0}".format(dhana_varga))

#02.Runa Varha      : (CA x 3) % 8 
runa_varga = (ca * 3) % 8
print("Runa Varga : {0}".format(runa_varga))

#03.Vaara Varga     : (CA x 9) % 7
#04.Thidhi Varga    : (CA x 6) % 30
#05.Tatva Varga     : (CA x 3) % 5
#06.Lagna Varga     : (CA x 9) % 12
#07.Yoga Varga      : (CA x 4) % 27
#08.Graha Varga     : (CA x 5) % 9
#09.Kula Varga      : (CA x 9) % 4
#10.Kalaa Varga     : (CA x 12) % 16
#11.Nakshatra Varga : (CA x 8) % 27
#12.Aaya Varga      : (CA x 9) % 8
#13.Aayu Varga      : (CA x 9) % 120
#14.Amsha Varga     : (CA x 6) % 9
#15.Dikhpathi Varga : (CA x 9) % 8
#16.Karana Varga    : (CA x 5) % 11





'''
# Aayu Varga : (CA x 9) % 120    
aayu_varga = (ca*9) % 120
print("Aayu Varga : {0}".format(aayu_varga))

#Aaya Varga : (CA x 9) % 8  
aaya_varga = (ca*9) % 8
aaya_varga_ip = [
        "Kakaya",
        "Dwajaya",
        "Dhoomraya",
        "Simhaya",
        "Shunakaya",
        "Vrushabaya",
        "Kharaya",
        "Gajaya" ]
print("Aaya Varga : {0} - {1}".format(aaya_varga, 
                                aaya_varga_ip[aaya_varga]))
'''


