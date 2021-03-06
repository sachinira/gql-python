from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://countries.trevorblades.com/")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

queryWithAlias = gql(
    """
    query Query {
    europe: continents(filter: {code: {eq : "EU"} })  {
        code
        name
    },

    asia: continents(filter: {code: {eq : "AS"} })  {
        code
        name
    }
    }
    """
)

# Get name of continent with code "EU"
resultWithAlias = client.execute(queryWithAlias)
print(resultWithAlias)
