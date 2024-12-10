import argparse

parser = argparse.ArgumentParser(description="Convierte temperaturas entre Celsius y Fahrenheit")

parser.add_argument("--temp", "-t", type=float, help="Temperatura")
parser.add_argument("--scale", "-s",help ="temperatura",
                    type=str,
                    choices=["Celcius", "Farenheit"],
                    default="Celcius", required=False,
)

args = parser.parse_args()
print("Hello")


"""
#### Ejemplo de ejecución:
<pre>
$ python3 temperature_converter.py -h
usage: temperature_converter.py [-h] [--temp TEMP] [--scale {C,F}]
Conversor de temperatura options:
-h, --help	show this help message and exit
--temp TEMP	Valor de temperatura a convertir.
--scale {C,F}  Escala de la temperatura de entrada (C or F). Opcional - Valor por defecto: C

"""