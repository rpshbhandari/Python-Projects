# Business Central Integration

Python clients for Microsoft Dynamics 365 Business Central's OData web services.

- `BC.py` fetches data over a raw socket with basic authentication.
- `record.py` wraps an API endpoint with filters, ordering, paging, and create, update and delete.
- `test.py` makes the same request as `BC.py` with `requests`.

## Configure

`config.py` reads the connection from the environment:

| Variable | Example |
| --- | --- |
| `BC_BASE_URL` | `http://localhost:7048` (include the port) |
| `BC_PATH` | `/bc210/ODataV4/Company('CRONUS International Ltd.')/webservices/` |
| `BC_USER`, `BC_PASSWORD` | A Business Central user with web service access |

```bash
pip install requests
python BC.py
```
