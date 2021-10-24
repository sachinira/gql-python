from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


# The RequestsHTTPTransport is a sync transport using the requests library and allows you to send GraphQL queries using the HTTP protocol.
transport = RequestsHTTPTransport(
    url="https://countries.trevorblades.com/", verify=True, retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
    query getContinents {
      continents {
        code
        name
      }
    }
"""
)

result = client.execute(query)
print(result)