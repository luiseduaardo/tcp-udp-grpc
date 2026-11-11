import grpc
from stub.calculator_pb2 import CalcRequest
from stub.calculator_pb2_grpc import AdderStub, MultiplierStub

ADDER_PORT = 3270
MULTIPLIER_PORT = 3271

def calc(op: str, a: float, b: float) -> float:
    if op in ('add', 'sub'):
        Stub = AdderStub
        port = ADDER_PORT
    else:
        Stub = MultiplierStub
        port = MULTIPLIER_PORT

    with grpc.insecure_channel(f'localhost:{port}') as channel:
        stub_instance = Stub(channel)
        request = CalcRequest(a=a, b=b)

        match op:
            case 'add':
                response = stub_instance.add(request)
            case 'sub':
                response = stub_instance.sub(request)
            case 'mul':
                response = stub_instance.mul(request)
            case 'div':
                response = stub_instance.div(request)

    return response.ans

if __name__ == '__main__':
    print("======== CALCULADORA DISTRIBUÍDA ========")

    i = 1
    while (1):
        print(f"\n\t\tOPERAÇÃO {i}")
        print("OPERAÇÕES SUPORTADAS:")
        print("[ 1 ] SOMA\t\t[ 2 ] SUBTRAÇÃO")
        print("[ 3 ] MULTIPLICAÇÃO\t[ 4 ] DIVISÃO")
        print("[ 5 ] ENCERRAR")

        operacao = int(input("Operação desejada: "))

        if operacao not in range(1,6):
            continue
        if (operacao == 5):
            break

        a = float(input("Primeiro valor : "))
        b = float(input("Segundo valor  : "))

        ans = 'UNDEFINED'
        if (operacao == 1):
            ans = calc('add', a, b)
        elif (operacao == 2):
            ans = calc('sub', a, b)
        elif (operacao == 3):
            ans = calc('mul', a, b)
        elif (operacao == 4):
            ans = calc('div', a, b)

        print(f"RESULTADO: {ans}\n")
        i+=1