import grpc
from stub.calculator_pb2 import CalcRequest, CalcResponse
from stub.calculator_pb2_grpc import AdderStub, MultiplierStub

ADDER_PORT = 3270
MULTIPLIER_PORT = 3271

def calc(port: int, stub_fn_getter, **kwargs) -> float:
    Stub = AdderStub if port == ADDER_PORT else MultiplierStub

    with grpc.insecure_channel(f'localhost:{port}') as channel:
        stub = Stub(channel)
        stub_fn = stub_fn_getter(stub)
        response: CalcResponse = stub_fn(CalcRequest(**kwargs))

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
        param = { 'a': a, 'b': b }
        if (operacao == 1):
            ans = calc(ADDER_PORT, lambda stub: stub.add, **param)
        elif (operacao == 2):
            ans = calc(ADDER_PORT, lambda stub: stub.sub, **param)
        elif (operacao == 3):
            ans = calc(MULTIPLIER_PORT, lambda stub: stub.mul, **param)
        elif (operacao == 4):
            ans = calc(MULTIPLIER_PORT, lambda stub: stub.div, **param)

        print(f"RESULTADO: {ans}\n")
        i+=1
        