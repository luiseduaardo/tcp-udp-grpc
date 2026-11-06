import grpc
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from stub.calculator_pb2 import CalcRequest, CalcResponse
from stub.calculator_pb2_grpc import AdderServicer, add_AdderServicer_to_server


class AdderService(AdderServicer):
    def add(self, req: CalcRequest, ctx):
        a, b = req.a, req.b

        print(f'SOMANDO {a} + {b}...')
        sleep(2)
        print(f'RESPOSTA: {a+b}')
        
        return CalcResponse(ans=a+b)

    def sub(self, req: CalcRequest, ctx):
        a, b = req.a, req.b

        print(f'SUBTRAINDO {a} - {b}...')
        sleep(2)
        print(f'RESPOSTA: {a-b}')
        
        return CalcResponse(ans=a-b)

PORT = 3270

if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor(max_workers=5))
    add_AdderServicer_to_server(AdderService(), server)
    server.add_insecure_port(f'[::]:{PORT}')

    server.start()
    print(f'Servidor de soma escutando na porta {PORT}...')
    server.wait_for_termination()