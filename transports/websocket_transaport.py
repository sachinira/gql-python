import asyncio
import logging

from gql import Client, gql
from gql.transport.websockets import WebsocketsTransport

logging.basicConfig(level=logging.INFO)


async def main():

    transport = WebsocketsTransport(url="wss://countries.trevorblades.com/graphql")
    # Websockets SSL
    # use _wss_ instead of _ws_ in the url of the transport

    # sample_transport = WebsocketsTransport(
    # url='wss://SERVER_URL:SERVER_PORT/graphql',
    # headers={'Authorization': 'token'})

    # self-signed ssl certificate
    # 
    # import pathlib
    # import ssl

    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    # localhost_pem = pathlib.Path(__file__).with_name("YOUR_SERVER_PUBLIC_CERTIFICATE.pem")
    # ssl_context.load_verify_locations(localhost_pem)

    # sample_transport = WebsocketsTransport(
    #     url='wss://SERVER_URL:SERVER_PORT/graphql',
    #     ssl=ssl_context
    # )

    # client ssl certificate
    # ssl_context.load_cert_chain(certfile='YOUR_CLIENT_CERTIFICATE.pem', keyfile='YOUR_CLIENT_CERTIFICATE_KEY.key')

    # Authentication

    # HTTP Headers
    # sample_transport = WebsocketsTransport(
    #     url='wss://SERVER_URL:SERVER_PORT/graphql',
    #     headers={'Authorization': 'token'}
    # )

    # Payload in the connection_init websocket message
    # sample_transport = WebsocketsTransport(
    #     url='wss://SERVER_URL:SERVER_PORT/graphql',
    #     init_payload={'Authorization': 'token'}
    # )


    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
        transport=transport, fetch_schema_from_transport=True,
    ) as session:

        # Execute single query
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
        result = await session.execute(query)
        print(result)

        # Request subscription
        subscription = gql(
            """
            subscription {
                somethingChanged {
                    id
                }
            }
        """
        )
        async for result in session.subscribe(subscription):
            print(result)


asyncio.run(main())