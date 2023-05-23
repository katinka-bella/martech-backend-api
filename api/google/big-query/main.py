class big_query_operator:

    def create_query(
        key_path: str,
        sql: str,
    ):
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
        

        query = sql
        query_job = client.query(query)  # Make an API request.

        print("The query data:")
        for row in query_job:
            print(row.c)

    def create_empty_table(
        key_path: str,
        table_id: str,
        schema: list
    ):
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
            
        table = bigquery.Table(table_id, schema=schema)
        table = client.create_table(table)  # Make an API request.
        print(
            "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
            )
    
    def create_table_from_query(
        key_path: str,
        table_id: str,
        sql: str
    ):
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
        
        job_config = bigquery.QueryJobConfig(destination=table_id)

        # Start the query, passing in the extra configuration.
        query_job = client.query(sql, job_config=job_config)  # Make an API request.
        query_job.result()  # Wait for the job to complete.

        print("Query results loaded to the table {}".format(table_id))    