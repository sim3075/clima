import json
import sys

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=4.6473&longitude=-74.0962&hourly=temperature_2m,relativehumidity_2m,precipitation&start_date=2022-10-25&end_date=2022-10-30"
response = requests.get(url)
data = json.loads(response.text)

class Consola:

    def __init__(self):
        self.opciones = {
            "1":  24,
            "2":  48,
            "3":  72,
            "4":  96,
            "5":  120,
            "6": self.salir
        }
    def mostar_menu(self):
        print("""
        \n
        ¿QUIERES SABER EL CLIMA DE LOS PROXIMOS DIAS?
        \u2601\uFE0F \u2601\uFE0F \u2601\uFE0F \u2601\uFE0F
        Menú de opciones:\n
        1. 25 de octubre
        2. 26 de octubre
        3. 27 de octubre
        4. 28 de octubrte
        5. 29 de octubre
        6. salir
        \u2601\uFE0F \u2601\uFE0F \u2601\uFE0F \u2601\uFE0F
        """)

    def ejecutar(self):
        while True:
            self.mostar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"ERROR: {opcion} no es una opción válida")

    def salir(self):
        print("\n \u2601\uFE0F TENGA BUEN DIA \U0001F600")
        sys.exit(0)


fecha = data["hourly"]["time"][:24]
# temp = data["hourly"]["temperature_2m"][1]
# humedad  = data["hourly"]["relativehumidity_2m"][1]
# prec = data["hourly"]["precipitation"][1]

print(f"{fecha}, la temperatura es °C, la humedad %, y la precipitacion ")
