class big_query_operator:


    def create_client(
        key_path: str
    ):
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

        return client


    def create_query(
        client, query: str,
    ):

        query_job = client.query(query)  # Make an API request.

        print("The query data:")
        for row in query_job:
            print(row)


    def create_table(
        client, table_id: str, schema: list
    ):
            
        table = bigquery.Table(table_id, schema=schema)
        table = client.create_table(table)  # Make an API request.
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
            )
    