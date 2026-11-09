import json
import socket
from threading import Thread

ADDER_PORT = 3270
MULTIPLIER_PORT = 3271

# ============= SERVIDOR =============

def handle(sock, data, addr, operations):
    try:
        req = json.loads(data)
        fn = operations[req['op']]
        resp = {'ans': fn(float(req['a']), float(req['b']))}
    except KeyError as e:
        resp = {'error': f'campo/operação inválida: {e}'}
    except (ValueError, ZeroDivisionError) as e:
        resp = {'error': str(e)}

    sock.sendto(json.dumps(resp).encode(), addr)


def serve(port: int, operations: dict, name: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    print(f'Servidor de {name} escutando na porta {port}...')

    while True:
        data, addr = sock.recvfrom(4096)  # espera um datagrama
        Thread(target=handle, args=(sock, data, addr, operations), daemon=True).start()

# ============= CLIENTE =============

def call(port: int, op: str, a: float, b: float, host: str = 'localhost', timeout: float = 5) -> float:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout)
        sock.sendto(json.dumps({'op': op, 'a': a, 'b': b}).encode(), (host, port))
        data, _ = sock.recvfrom(4096)

    resp = json.loads(data)
    if 'error' in resp:
        raise RuntimeError(resp['error'])
    return resp['ans']
