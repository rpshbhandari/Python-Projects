import socket
import logging
from modules import HttpResponse

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class HttpRequest:
    """Represents an HTTP request."""

    def __init__(self, method: str, path: str, version: str) -> None:
        """
        Initializes an HttpRequest object.

        Args:
            method (str): The HTTP method (e.g., GET, POST).
            path (str): The requested path.
            version (str): The HTTP version.
        """
        self.method: str = method
        self.path: str = path
        self.version: str = version





def receive_http_request(conn: socket.socket) -> bytes:
    """
    Receives HTTP data from a web browser and extracts the full request.

    Args:
        conn (socket.socket): The socket connection.

    Returns:
        bytes: The received HTTP request data.
    """
    buffer: bytes = b""
    conn.settimeout(2)
    try:
        while True:
            data: bytes = conn.recv(1024)
            if not data:
                break
            buffer += data
            if b"\r\n\r\n" in buffer:
                break
    except socket.timeout as exc:
        logging.warning(f"Socket timeout: {exc}")
    except Exception as exc:
        logging.error(f"An unexpected error occurred: {exc}")
    return buffer


def main() -> None:
    """
    Main function to start the HTTP server.
    """
    HOST: str = "127.0.0.1"
    PORT: int = 65435

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            logging.info(f"listening on {HOST}:{PORT}")

            while True:
                try:
                    conn, addr = s.accept()
                    logging.info(f"Connected by {addr}")
                    with conn:
                        request: bytes = receive_http_request(conn)
                        logging.debug("Received data:\n%s",
                                    request.decode(errors="ignore"))

                        # Sending a proper HTTP response so Safari doesn't hang.
                        response: HttpResponse = HttpResponse(200)
                        response.add_body("Hello, World!asdasds")
                        logging.debug("Encoded response: %s", response.encode())
                        try:
                            conn.sendall(response.encode())
                        except OSError as os_error:
                            logging.error(
                                f"Failed to send data to the client: {os_error}"
                            )
                except Exception as inner_exc:
                    logging.error(f"Error handling connection: {inner_exc}")
    except Exception as outer_exc:
        logging.error(f"Server encountered a fatal error: {outer_exc}")


if __name__ == "__main__":
    main()