import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65435  # The port used by the server

def send_http_request() -> bytes:
    """
    GET / HTTP/1.1
Host: localhost:65435
Sec-Fetch-Dest: document
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Accept-Language: en-GB,en;q=0.9
Priority: u=0, i
Accept-Encoding: gzip, deflate
Connection: keep-alive
    """
    request = """
GET / HTTP/1.1
Host: localhost:65435
Sec-Fetch-Dest: document
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Accept-Language: en-GB,en;q=0.9
Priority: u=0, i
Accept-Encoding: gzip, deflate
Connection: keep-alive
"""
    return request.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(send_http_request())
    data = s.recv(1024)

print(f"Received {data!r}")

