# sdp-quick-start

Databricks recently open-sourced **Spark Declarative Pipelines (SDP)** and contributed them to Apache Spark. This is game changer and positioned to take Spark from an imperative model to a declarative model. However, getting started with SDP can be quite challenging. If this is your first time encountering SDP, you can get an introduction [here](https://medium.com/@idowuilekura/spark-declarative-pipeline-dbt-replacement-for-spark-8d76f55c213b)


The aim of this repository is to serve as a quick-start guide for Spark Declarative Pipelines.


## What This Repo Contains

The repository includes:

- A **Docker Compose** setup with prepackaged Spark images and Apache Iceberg to provide a ready-to-use environment  
- Sample data containing `users_details` and `transaction_details` (located in the `data` folder)  
- A working SDP Python pipeline example to help you get started (located in the `transformation` folder)  
- A Spark configuration file configured for Apache Iceberg  
- An SDP pipeline configuration file
- A Docker file to build your custom and prepackaged SDP environment 
## How to Run

Follow these steps to get started:

1. Ensure you have Docker installed on your system  
   - If you are on Windows or Mac, make sure Docker Desktop is running  
2. Clone this repository to your local machine  
3. Open a terminal and navigate to the cloned folder.  
4. Run the following command to start the environment:

   ```bash
   docker compose up
   ```
This will start all required containers.

To enter the running Docker container, run: ```docker exec -it sdpcont /bin/bash``` (where sdpcont is the name of the Docker container)

After that, navigate into the `app` folder inside the container with `cd /app/`

Once inside the container, execute the SDP pipeline with:

  ```bash
  spark-pipelines run --spec spark-pipelines.yaml
  ```

## Next Steps

- Continue exploring and experimenting with Spark Declarative Pipelines  
- You can follow this additional guide for deeper learning [here](https://medium.com/@idowuilekura/spark-declarative-pipeline-dbt-replacement-for-spark-part-2-e39c2f0fa836)  

 ### Changing the SDP Database

If you need to change the database used by SDP:

1. Stop the running containers and remove volumes:
    ```bash
    docker compose down -v
    ```

2. Update the database field in the `spark-pipelines.yaml` file. Which is located inside the `app` folder.

3. Also update the corresponding field in the `docker-compose.yaml` file:

      `- ICEBERG_DATABASE_NAME=your_preferred_database_name`

After making these changes, restart the environment using:
  ```bash
       docker compose up
  ```

Happy building with Spark Declarative Pipelines!

