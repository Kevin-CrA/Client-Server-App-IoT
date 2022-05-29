from random import randint
import wmi
#import psutil
#psutil= wmi en windows



#POO en Python
#Definicion de la clase
class Sensor:

    #Constructor de la clase
    def __init__(self):
        
        #Funciona pa linux
        #self._sensor= psutil.sensors_temperatures()

        #Funciona pa wind
        #self._wmi=wmi.WMI(namespace='root\OpenHardwareMonitor')
        pass

    def get_temp(self):
            return self._sensor['coretemp']

      #Simular 'la toma de algun valor de otro sensor'
    def get_random_number(self):
            return randint(0,90)

    def get_temp_for_windows(self):
            return self._wmi.SensorType['Temperature']
