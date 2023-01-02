Stock prices trend for FAANG comapnies

It is a personal project for demonstrating a close to real world data engineering project with
* Data Extraction
* Data storage
* Data visualization


## Data Extraction

I am trying to extract Stock prices for FAANG companies on daily grain using open source api [yfinance](https://pypi.org/project/yfinance/).  Have used [airflow](https://airflow.apache.org/) for job orchestration and managing connections to the database. 

## Data Storage

Have used Postgres for storing data that will be used for visualization. Ideally, this will be replaced by a datawarehouse depending on the size of the project and the complexity of the analysis. For simplicity I have used Postgres.

## Data visualization

I am using [metabase](https://www.metabase.com/) to create visualizations. 

## How to get started
* Clone the repository
* Install docker compose https://docker-docs.netlify.app/compose/install/#install-compose
* execute following command to kick off the services from within the repository
   ```
   docker compose up
  ```
  This should kick off 6 services
  * postgres db
  * airflow metadata postgres db
  * metabase
  * adminer
  * aiflow scheduler
  * airflow webserver
  
  The services are available at following URL
  * metabase: http://localhost:3000/
  * airflow: http://localhost:8081/
  * adminer: http://localhost:8080/

**Note**: 
The project is kept in the state that is meant to be shared and get quick insights so the database state and other 
parameters are kept intact (not ideal for production use case). 
Since we are storing the state of DB, the credentials and other sensitive information is also intact so it is only 
for demoing purposes and is **not** for production use case. 
The serialization of dashboard is available in metabase Enterprice version only.

* If you do not need to view pre-built then that is all what you need.
You can visit http://localhost:3000 and complete the setup.


* Run data dump by
```
     docker exec  <db_cotainer_name> psql my_db user -f data/data_dump.sql
```
Navigate to the url http://localhost:3000/dashboard/2-faang-stock-prices to get the dashboard for the data. 
