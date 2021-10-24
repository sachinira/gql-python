from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://countries.trevorblades.com/")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

queryWithVariales = gql(
    """
    query getContinentName ($code: ID!) {
      continent (code: $code) {
        name
      }
    }
"""
)

params = {"code": "EU"}

# Get name of continent with code "EU"
resultWithVariableQueryEU = client.execute(queryWithVariales, variable_values=params)
print(resultWithVariableQueryEU)

params = {"code": "AF"}

# Get name of continent with code "AF"
resultWithVariableQueryAF = client.execute(queryWithVariales, variable_values=params)
print(resultWithVariableQueryAF)