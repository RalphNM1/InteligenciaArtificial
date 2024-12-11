import argparse
def inicio():
    parser = argparse.ArgumentParser(description="Convierte temperaturas entre Celsius y Fahrenheit")

    parser.add_argument("--temp", "-t", type=float, help="Temperatura", required=True)
    parser.add_argument("--scale", "-s",help ="Escala", required=False,
                        type=str,
                        choices=["C", "F"],
                        default="C",
    )

    args = parser.parse_args()

    if args.scale == 'C': # Pasar de Celsius a Fahrenheit (0 °C × 9 / 5) + 32 = 32 °F
        celsius_fahrenheit =  args.temp * 9 / 5 + 32
        print(f"{args.temp} ºC son {celsius_fahrenheit} ºF")
    elif args.scale == 'F': # Pasar de Fahrenheit a Celsiues (32 °F − 32) × 5 / 9 = 0 °C
        fahrenheit_celsius =  (args.temp  - 32) * 5 / 9
        print(f"{args.temp} ºF son {fahrenheit_celsius} ºC")
    else:
        print("Error,Introduzca una escala válida (C - F)")

def inicio2():
    temperatura = float(input("Introduzca la temperatura: "))
    
    escala = str(input("Introduzca la escala (C - F): "))

    while(escala != "C" and escala != "F"):
        print("Error, la escala tiene que ser (C - F)")
        escala = input("Introduzca la escala (C- F): ")


    if escala == 'C': # Pasar de Celsius a Fahrenheit (0 °C × 9 / 5) + 32 = 32 °F
        celsius_fahrenheit =  temperatura * 9 / 5 + 32
        print(f"{temperatura} ºC son {celsius_fahrenheit} ºF")
    elif escala == 'F': # Pasar de Fahrenheit a Celsiues (32 °F − 32) × 5 / 9 = 0 °C
        fahrenheit_celsius =  (temperatura  - 32) * 5 / 9
        print(f"{temperatura} ºF son {fahrenheit_celsius} ºC")
   
