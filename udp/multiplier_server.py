from time import sleep
from protocol import serve, MULTIPLIER_PORT


def mul(a: float, b: float) -> float:
    print(f'MULTIPLICANDO {a} * {b}...')
    sleep(2)
    print(f'RESPOSTA: {a*b}')
    return a * b


def div(a: float, b: float) -> float:
    print(f'DIVIDINDO {a} / {b}...')
    sleep(2)
    print(f'RESPOSTA: {a/b}')
    return a / b


if __name__ == '__main__':
    serve(MULTIPLIER_PORT, {'mul': mul, 'div': div}, 'multiplicação')
