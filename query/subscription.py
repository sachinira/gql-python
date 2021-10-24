from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport

transport = WebsocketsTransport(url='wss://your_server/graphql')

client = Client(
    transport=transport,
    fetch_schema_from_transport=True,
)

query = gql('''
    subscription yourSubscription {
        ...
    }
''')

for result in client.subscribe(query):
    print (result)


# The websockets transport can also execute queries or mutations, it is not restricted to subscriptions
