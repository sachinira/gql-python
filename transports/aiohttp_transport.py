import asyncio

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


async def main():

    # transport = AIOHTTPTransport(url="https://countries.trevorblades.com/graphql")
    transport = AIOHTTPTransport(url="https://swapi-graphql.netlify.app/.netlify/functions/index")

    # Authentications

    # HTTP Headers
    # transport = AIOHTTPTransport(
    # url='https://SERVER_URL:SERVER_PORT/graphql',
    # headers={'Authorization': 'token'})

    # HTTP Cookies
    # transport = AIOHTTPTransport(url=url, cookies={"cookie1": "val1"})

    # Use a cookie jar to save cookies set from the backend and reuse them later.
    # jar = aiohttp.CookieJar()
    # transport = AIOHTTPTransport(url=url, client_session_args={'cookie_jar': jar})

    # Async program to juggle multiple operations without waiting or getting hung up on any one of them. 
    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
        transport=transport, fetch_schema_from_transport=True,
    ) as session:

        # Execute single query
        # query = gql(
        #     """
        #     query getContinents {
        #       continents {
        #         code
        #         name
        #       }
        #     }
        # """
        # )

        query = gql(
            """
            query ErrorQuery {
                film(id: 1) {
                    title
                }
            }
            """
        )

        result = await session.execute(query)
        print(result)

# asyncio.run() is used to launch an async function from the non-asynchronous part of our code, and thus kick off all 
# of the progam’s async activities. (This is how we run main().)
# then run your coroutine in an asyncio event loop by running asyncio.run
asyncio.run(main())
