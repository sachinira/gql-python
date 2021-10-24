import asyncio

from gql import Client
from gql.dsl import DSLQuery, DSLSchema, dsl_gql
from gql.transport.aiohttp import AIOHTTPTransport

async def main():

    transport = AIOHTTPTransport(url="https://countries.trevorblades.com/graphql")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)


    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection.
    # Because we requested to fetch the schema from the transport,
    # GQL will fetch the schema just after the establishment of the first session
    async with client as session:

        # Instantiate the root of the DSL Schema as ds
        ds = DSLSchema(client.schema)

        # Create the query using dynamically generated attributes from ds
        query1 = dsl_gql(
            DSLQuery(
                ds.Query.continents(filter={"code": {"eq": "EU"}}).select(
                    ds.Continent.code, ds.Continent.name
                )
            )
        )

        result1 = await session.execute(query1)
        print(result1)
        print("==========================")

        query2 = dsl_gql(
            DSLQuery(
                ds.Query.continents(filter={"code": {"eq": "EU"}}).alias("EuropeAlias").select(
                    ds.Continent.code, ds.Continent.name
                ),
                ds.Query.continents(filter={"code": {"eq": "AS"}}).alias("AsiaAlias").select(
                    ds.Continent.code, ds.Continent.name
                )
            )
        )

        result2 = await session.execute(query2)
        print(result2)
        print("==========================")

        # query3 = dsl_gql(
        #     DSLQuery(
        #         ds.Query.continents(filter={"code": {"eq": "EU"}}).select(
        #             ds.Continent.code, ds.Continent.name
        #         )
        #     )
        # )

        # result3 = await session.execute(query3)
        # print(result3)
        # print("==========================")

        # Mutations

        # Subsciptions
        
        # Variables

        # Fragments

        # Inline fragments

asyncio.run(main())