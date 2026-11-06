import grpc
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from stub.calculator_pb2 import CalcRequest, CalcResponse
from stub.calculator_pb2_grpc import MultiplierServicer, add_MultiplierServicer_to_server


class MultiplierService(MultiplierServicer):
    def mul(self, req: CalcRequest, ctx):
        a, b = req.a, req.b

        print(f'MULTIPLICANDO {a} * {b}...')
        sleep(2)
        print(f'RESPOSTA: {a*b}')
        
        return CalcResponse(ans=a*b)

    def div(self, req: CalcRequest, ctx):
        a, b = req.a, req.b

        print(f'DIVIDINDO {a} / {b}...')
        sleep(2)
        print(f'RESPOSTA: {a/b}')
        
        return CalcResponse(ans=a/b)

PORT = 3271

if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor(max_workers=5))
    add_MultiplierServicer_to_server(MultiplierService(), server)
    server.add_insecure_port(f'[::]:{PORT}')

    server.start()
    print(f'Servidor de multiplicação escutando na porta {PORT}...')
    server.wait_for_termination()