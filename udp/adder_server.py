from time import sleep
from protocol import serve, ADDER_PORT


def add(a: float, b: float) -> float:
    print(f'SOMANDO {a} + {b}...')
    sleep(2)
    print(f'RESPOSTA: {a+b}')
    return a + b


def sub(a: float, b: float) -> float:
    print(f'SUBTRAINDO {a} - {b}...')
    sleep(2)
    print(f'RESPOSTA: {a-b}')
    return a - b


if __name__ == '__main__':
    serve(ADDER_PORT, {'add': add, 'sub': sub}, 'soma')
