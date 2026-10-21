# Socket Programming

An HTTP server and client on raw sockets, with no web framework.

- `server.py` listens on `127.0.0.1:65435`, parses each request and answers it with the `HttpResponse` class from `modules.py`.
- `clent.py` sends a GET request to that server and prints the reply.
- `remove_binding.py` frees a port on macOS when a previous run left it bound.

```bash
python server.py
python clent.py              # in a second terminal
python remove_binding.py 65435
```
