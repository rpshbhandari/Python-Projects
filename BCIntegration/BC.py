import logging
import re
import socket
import json
from base64 import b64encode
import config

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])

class BusinessCentral:
    def __init__(self, base_url: str, path: str, auth: tuple[str, str], param: dict[str, str]) -> None:
        """
        Initialize the BusinessCentral instance.

        :param base_url: The base URL of the Business Central instance.
        :param path: The API path to access.
        :param auth: A tuple containing the username and password.
        :param param: A dictionary of query parameters.
        """
        self.base_url: str = base_url
        self.path: str = path
        self.auth: tuple[str, str] = auth
        self.param: dict[str, str] = param
        self.host_port: str = base_url.split("//")[1]
        self.host: str = self.host_port.split(":")[0]
        self.port: int = int(self.host_port.split(":")[1])

    def get_auth(self, auth: tuple[str, str]) -> str:
        """
        Generate the base64 encoded authentication string.

        :param auth: A tuple containing the username and password.
        :return: The base64 encoded authentication string.
        """
        auth_str: str = f"{auth[0]}:{auth[1]}"
        return b64encode(auth_str.encode()).decode()

    def get_data(self) -> str:
        """
        Retrieve data from the Business Central instance.

        :return: The cleaned JSON string.
        """
        try:
            # Prepare the path with parameters
            # path_with_params: str = self.path
            # if self.param:
            #     path_with_params += "?" + "&".join(
            #         [f"{k}={v}" for k, v in self.param.items()]
            #     )

            # Create a socket and connect to the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                ip: str = socket.gethostbyname(self.host)
                s.connect((ip, self.port))

                # Prepare the HTTP GET request
                request: str = (
                    f"GET {self.path} HTTP/1.1\r\n"
                    f"Authorization: Basic {self.get_auth(self.auth)}\r\n"
                    f"Host: {self.host_port}\r\n"
                    f"User-Agent: Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 "
                    f"(KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 "
                    f"CrKey/1.54.248666 Edg/132.0.0.0\r\n"
                    f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,"
                    f"image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;"
                    f"v=b3;q=0.7\r\n"
                    f"Accept-Encoding: gzip, deflate\r\n"
                    f"Accept-Language: en-US,en;q=0.9\r\n"
                    f"Cache-Control: max-age=0\r\n"
                    f"Connection: close\r\n"
                    f"DNT: 1\r\n"
                    f"Upgrade-Insecure-Requests: 1\r\n\r\n"
                )
                
                logging.info(request)

                # Send the HTTP request
                s.sendall(request.encode())

                # Receive the response
                response: bytes = b""
                while True:
                    data: bytes = s.recv(4096)
                    if not data:
                        break
                    response += data

            # Extract the body from the HTTP response
            response_str: str = response.decode()
            logging.info(f"Response: {response_str}")
            return self.clean_data(response_str)
        
        except Exception as e:
            logging.error(f"Error retrieving data: {e}")
            raise RuntimeError(f"Error retrieving data: {e}")

    @staticmethod
    def clean_data(response_str: str) -> str:
        """
        Clean the response data by extracting the first JSON object.

        :param response_str: The response string to clean.
        :return: The cleaned JSON string.
        """
        json_match = re.search(r'\{.*\}', response_str, re.DOTALL)
        
        if json_match:
            return json_match.group(0)  # Return the matched JSON string
        else:
            logging.error("No JSON object found in the response")
            raise ValueError("No JSON object found in the response")

if __name__ == "__main__":
    
    # Load the environment variables

    BASE_URL = config.BASE_URL
    PATH = config.PATH
    USER = config.USER
    PASSWORD = config.PASSWORD
    PARAMS = config.PARAM


    BC = BusinessCentral(base_url=BASE_URL, path=PATH, auth=(USER, PASSWORD), param=PARAMS)
    try:
        data: str = BC.get_data()
        logging.info(f"Retrieved data: {data}")
        parsed_data = json.loads(data)

        # Pretty print the parsed JSON data
        logging.info(json.dumps(parsed_data, indent=4))
    except RuntimeError as e:
        logging.error(f"Failed to retrieve data: {e}")