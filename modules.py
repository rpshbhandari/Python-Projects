
PROTOCOL = "HTTP/1.1"
STATUS_CODES = {
    200: "OK",
    400: "Bad Request",
    404: "Not Found",
    500: "Internal Server Error"
}

MANDATORY_HEADERS = [
    "Content-Type",
    "Content-Length",
    "Connection",
    "Accept",
    "Host",
    "User-Agent",
    "Accept-Encoding"
]

DEFAULT_HEADERS = {
    "Content-Type": "text/html; charset=utf-8",
    "Content-Length": "0",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Host": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Encoding": "gzip, deflate, br"
}


class HttpResponse:
    # Accept many headers dynamically
    def __init__(self, status,**kwargs) -> None:
        """
        Initializes an HttpResponse object.

        Args:
            args: Positional arguments.
            kwargs: Keyword arguments.
        """
        self.status_line = f"{PROTOCOL} {status} {STATUS_CODES.get(status, 'Unknown')}\r\n"
        self.headers = DEFAULT_HEADERS.copy()
        self.body = ""
        for key, value in kwargs.items():
            self.headers[key] = value
        

    def add_header(self, key: str, value: str) -> None:
        """
        Adds a header to the HttpResponse object.

        Args:
            key (str): The header key.
            value (str): The header value.
        """
        self.headers[key] = value
    
    def get_header(self, key: str) -> str:
        """
        Retrieves a header value from the HttpResponse object.

        Args:
            key (str): The header key.

        Returns:
            str: The header value.
        """
        return self.headers.get(key, "")
    
    def add_body(self, body: str, is_binary=False) -> None:
        """
        Adds a body to the HttpResponse object.

        Args:
            body (str): The body content.
            is_binary (bool): Set to True if the body is binary (e.g., images, files).
        """
        self.body = body
        # If binary content, ensure we handle it properly for content length and encoding
        if not is_binary:
            self.headers['Content-Length'] = str(self._get_content_length(body))
            if 'Content-Type' not in self.headers:
                self.headers['Content-Type'] = self._get_content_type(body)
        else:
            # For binary data, we avoid Content-Type auto-detection and let the user define it
            if 'Content-Type' not in self.headers:
                self.headers['Content-Type'] = 'application/octet-stream'
    
    def encode(self) -> bytes:
        """
        Encodes the HttpResponse object into bytes.

        Returns:
            bytes: The encoded response.
        """
        response = str(self).encode('utf-8')
        return response
    
    def _get_content_type(self, str) -> str:
        """
        Calculates the content type of the response.

        Returns:
            str: The content type.
        """
        if str.endswith(".html"):
            return "text/html; charset=utf-8"
        elif str.endswith(".css"):
            return "text/css; charset=utf-8"
        elif str.endswith(".js"):
            return "application/javascript; charset=utf-8"
        elif str.endswith(".json"):
            return "application/json; charset=utf-8"
        elif str.endswith(".png"):
            return "image/png"
        elif str.endswith(".jpg") or str.endswith(".jpeg"):
            return "image/jpeg"
        elif str.endswith(".gif"):
            return "image/gif"
        elif str.endswith(".svg"):
            return "image/svg+xml"
        elif str.endswith(".ico"):
            return "image/x-icon"
        elif str.endswith(".txt"):
            return "text/plain; charset=utf-8"
        elif str.endswith(".xml"):
            return "application/xml; charset=utf-8"
        elif str.endswith(".pdf"):
            return "application/pdf"

    def _get_content_length(self, str) -> int:
        """
        Calculates the content length of the response.

        Returns:
            int: The content length.
        """
        return len(str.encode('utf-8'))
    
    def __str__(self) -> str:
        """Returns a string representation of the HttpResponse object."""
        response = self.status_line
        for key, value in self.headers.items():
            response += f"{key}: {value}\r\n"
        response += "\r\n"  # End of headers

        if self.body:
            response += self.body  # Add the body content

        return response

if __name__ == "__main__":
    response = HttpResponse(status= 200, ContentType="text/html", Server="MyServer")
    response.add_body("<html><body>Hello, World asdasd!</body></html>")
    print(response)