import json
import socket
from socketserver import StreamRequestHandler, ThreadingTCPServer

ADDER_PORT = 3270
MULTIPLIER_PORT = 3271


# ============= SERVIDOR =============

def make_handler(operations: dict):
    class Handler(StreamRequestHandler):
        def handle(self):
            # uma requisição por linha; a conexão pode ser reutilizada
            for line in self.rfile:
                try:
                    req = json.loads(line)
                    fn = operations[req['op']]
                    resp = {'ans': fn(float(req['a']), float(req['b']))}
                except KeyError as e:
                    resp = {'error': f'campo/operação inválida: {e}'}
                except (ValueError) as e:
                    resp = {'error': str(e)}
                self.wfile.write((json.dumps(resp) + '\n').encode())

    return Handler


def serve(port: int, operations: dict, name: str):
    ThreadingTCPServer.allow_reuse_address = True
    ThreadingTCPServer.daemon_threads = True        # Thread morrem junto com fim do programa

    # Cria um socket de escuta 
    with ThreadingTCPServer(('', port), make_handler(operations)) as server:
        print(f'Servidor de {name} escutando na porta {port}...')
        server.serve_forever()

# ============= CLIENTE =============

def call(port: int, op: str, a: float, b: float, host: str = 'localhost') -> float:
    with socket.create_connection((host, port)) as sock:
        with sock.makefile('rwb') as f:
            f.write((json.dumps({'op': op, 'a': a, 'b': b}) + '\n').encode())
            f.flush()
            resp = json.loads(f.readline())

    if 'error' in resp:
        raise RuntimeError(resp['error'])
    return resp['ans']
