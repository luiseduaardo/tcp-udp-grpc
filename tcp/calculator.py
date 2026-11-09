from protocol import call, ADDER_PORT, MULTIPLIER_PORT

if __name__ == '__main__':
    print("======== CALCULADORA DISTRIBUÍDA (TCP) ========")

    i = 1
    while True:
        print(f"\n\t\tOPERAÇÃO {i}")
        print("OPERAÇÕES SUPORTADAS:")
        print("[ 1 ] SOMA\t\t[ 2 ] SUBTRAÇÃO")
        print("[ 3 ] MULTIPLICAÇÃO\t[ 4 ] DIVISÃO")
        print("[ 5 ] ENCERRAR")

        operacao = int(input("Operação desejada: "))

        if operacao not in range(1, 6):
            continue
        if operacao == 5:
            break

        a = float(input("Primeiro valor : "))
        b = float(input("Segundo valor  : "))

        port, op = {
            1: (ADDER_PORT, 'add'),
            2: (ADDER_PORT, 'sub'),
            3: (MULTIPLIER_PORT, 'mul'),
            4: (MULTIPLIER_PORT, 'div'),
        }[operacao]

        try:
            print(f"RESULTADO: {call(port, op, a, b)}\n")
        except (RuntimeError, OSError) as e:
            print(f"ERRO: {e}\n")
        i += 1
