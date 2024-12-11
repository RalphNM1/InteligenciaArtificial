import argparse

def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def inicio():
    
    parser = argparse.ArgumentParser(description="Genera los primeros números de Fibonacci del número introducido")

    parser.add_argument("--num", "-n", type=int, help="Número", required=True)
        
    args = parser.parse_args()

    print(f"{args.num} primeros números de Fibonacci:")
    fib = fibonacci()
    for _ in range(args.num+1):
        print(next(fib),end=" ")

def inicio2():
    
    numero = int(input("Introduzca un número"))

    print(f"{numero} primeros números de Fibonacci: ")
    fib = fibonacci()
    for _ in range(numero+1):
        print(next(fib),end=" ")


