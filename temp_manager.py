Hh = 1 # Coeficiente de transmisión de calor entre ambos medios (heating)
Hc = 1 # Coeficiente de transmisión de calor entre ambos medios (cooling)
A = 1  # Superficie total del sensor
C = 1  # Capacidad de calor del sensor
Th = 50 # Temperatura objetivo (heating)
Tc = -50 # Temperatura objetivo (cooling)

class Temp_Manager():
    def __init__(self, data):
        self.Hh = data["Hh"]
        self.Hc = data["Hc"]
        self.Th = data["Th"]
        self.Tc = data["Tc"]
        self.A = data["A"]
        self.C = data["C"]

        def heat(self, temp):
            dT = self.Hh * self.A / self.C * (self.Th - temp)
            return temp + dT

        def cool(self, temp):
            dT = self.Hc * self.A / self.C * (self.Tc - temp)
            return temp + dT

