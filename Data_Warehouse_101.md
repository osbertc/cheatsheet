# DB warehouse

- Most business use cases just need a daily refresh of analytics data.
- A pipeline that runs after midnight and finishes before people get to work.

For instance, if you're a restaurant and want to analyze orders/waitress ratio efficiency (which hour of the week the staff is most busy vs most free), you need to combine your sales data (from POS system) with your staff duty data (from HR system).

# Four Reasons TO Get A Data Warehouse
1. You need to analyse data from different sources
2. You need to separate analytical from transactional data
3. Your original data source isnt suitable for querying (No SQL, for instance!)
4. To improve the performance of your most-used queries (think: transformed summary tables!) 

# Transactional vs Analytics DBs

Transactional databases  
optimized for fast, short queries with high concurrent volume  

Analytics database  
optimized for long-running, resource-intensive queries  

|        | Transactional DBs           | Analytics DBs               |  
| -      | -                           | -                           |  
| -      | many simple queries         | few heavy queries           |  
|Data    | Manay single-row writes     | Few large batch imports     |   
|        | Current, single data        | Years of data, many sources |
|Queries | Generated by user activites | Generated by large reports  |  
|        | <1s response time           | Queries run for hours       |
|        | short queries               | Long, complex queries       |   
| -      | -                           | -                           |  
|workload| SELECT * FROM products<br>WHERE id = 123 | SELECT category_name, count(*)<br>as num_products<br>FROM products GROUP BY 1 |  




--- I dont understand this ---  
Quick note:  

Columnar storage engine: Instead of storing data row by row on disk, analytical databases group columns of data together and store them.

Compression of columnar data: Data within each column is compressed for smaller storage and faster retrieval.

Parallelization of query executions: Modern analytical databases are typically run on top of thousands of machines. Each analytical query can thus be split into multiple smaller queries to be executed in parallel amongst those machines (divide and conquer strategy).

https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e