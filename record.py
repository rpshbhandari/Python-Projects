import requests
import logging

class Record:
    def __init__(self, base_url, api_key, entity_name):
        self.base_url = base_url
        self.api_key = api_key
        self.entity_name = entity_name
        self.filters = []
        self.order_by = None
        self.top = None
        self.skip = None

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def setRange(self, field, criteria, operator='eq'):
        """Sets a filter for a field based on given criteria and operator."""
        self.filters.append((field, criteria, operator))

    def setOrderBy(self, field, direction='asc'):
        """Sets the order by field and direction."""
        self.order_by = f"{field} {direction}"

    def setPagination(self, top=None, skip=None):
        """Sets pagination parameters."""
        self.top = top
        self.skip = skip

    def _build_filter_query(self):
        """Builds the OData filter query from the set filters."""
        if not self.filters:
            return ""
        filter_query = "&$filter=" + " and ".join([f"{field} {operator} '{criteria}'" for field, criteria, operator in self.filters])
        return filter_query

    def _build_query_params(self):
        """Builds the query parameters including filters, pagination, and sorting."""
        params = self._build_filter_query()
        if self.order_by:
            params += f"&$orderby={self.order_by}"
        if self.top:
            params += f"&$top={self.top}"
        if self.skip:
            params += f"&$skip={self.skip}"
        return params

    def get_records(self):
        """Retrieves records based on set filters."""
        url = f"{self.base_url}/{self.entity_name}"
        query_params = self._build_query_params()
        response = requests.get(url + query_params, headers=self._headers())

        self.logger.info(f"GET {url + query_params}: {response.status_code}")

        if response.status_code != 200:
            self.logger.error(f"Error fetching records: {response.text}")
            response.raise_for_status()

        return response.json()

    def create_record(self, record_data):
        """Creates a new record."""
        url = f"{self.base_url}/{self.entity_name}"
        response = requests.post(url, json=record_data, headers=self._headers())

        self.logger.info(f"POST {url}: {response.status_code}")

        if response.status_code not in [200, 201]:
            self.logger.error(f"Error creating record: {response.text}")
            response.raise_for_status()

        return response.json()

    def update_record(self, record_id, record_data):
        """Updates an existing record."""
        url = f"{self.base_url}/{self.entity_name}({record_id})"
        response = requests.patch(url, json=record_data, headers=self._headers())

        self.logger.info(f"PATCH {url}: {response.status_code}")

        if response.status_code != 200:
            self.logger.error(f"Error updating record: {response.text}")
            response.raise_for_status()

        return response.json()

    def delete_record(self, record_id):
        """Deletes a record."""
        url = f"{self.base_url}/{self.entity_name}({record_id})"
        response = requests.delete(url, headers=self._headers())

        self.logger.info(f"DELETE {url}: {response.status_code}")

        if response.status_code != 204:
            self.logger.error(f"Error deleting record: {response.text}")
            response.raise_for_status()

        return response.status_code


Rec = Record()
res = requests.get()