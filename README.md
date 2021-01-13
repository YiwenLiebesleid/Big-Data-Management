# Big Data Management Final Project

### Topic
Progressive Approximate Answers for Aggregation Queries

### Description
Aggregation queries can be answered by checking the entire dataset and aggregating all records. This will generate an exact answer. But the problem with this approach is that queries may take long time especially if the data is very large. Another practical approach is to answer the aggregation queries using a sample of the data.

* Build an interface that takes a SQL-like aggregation query.

* Translate the query into a sequence of map-reduce jobs, each time considers 5% of the data (randomly selected), and produces an approximate answer for the query.

* Trigger another 5% of the data only if the results from the latest job differ from the combined results by more that the specified threshold.

* Report the result progressively.

### Setup
We are using Mongodb for database, Python for backend, Flask framework for connecting frontend and backend, and HTML and Javascript for frontend.

### Python Files
generate.py: generate the random data file "Customer.json"

insert.py: insert the records in the "Customer.json" into dataset

progressive-queries.py: basic logic of the project, and connection with frontend.

### Input
The dataset is already linked, the user only need to select which column and what properties are interested.

### Output
If the log is selected to be shown, all of the progressive results (along with difference according to the latest iteration and the time) will be displayed on the new page. While if not, only the final result will be displayed.

### REFERENCES
* *Encyclopedia of GIS, Lazaridis and Mehrotra, 2017.*

* *Online Aggregation, Hellerstein et al., 1997.*

* *Progressive Approximate Aggregate Queries with a Multi-Resolution Tree Structure, Lazaridis and Mehrotra, 2001.*

* *pCube: Update-Efficient Online Aggregation with Progressive Feedback and Error Bounds, Riedewald et al., 2000.*
