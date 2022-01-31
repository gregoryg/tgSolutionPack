#!/usr/bin/env python

# # 1 - TigerGraph Schema Refresh Job
# 
# These scripts are used to automatically refresh the a TigerGraph instance on TGCloud (or EC2)
# The steps included are:
#     
#     1. Create empty graph - drop if exists
#     2. Create schema change job
#     3. Run schema change job
#     3. Create load jobs
#     4. Run load jobs
# 

# FETCH PACKAGES
import sys
import pyTigerGraph as tg

# ### 1.3.2 - Setup Connection to TGCloud
# Access to TGCloud is thru REST API, and a combo of token & username/pw authentication

#User definied parameters
host = "https://mov-rec-tgws.i.tgcloud.io"
username = "tigergraph"
password = "TigerG123"  

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema
# Let's define the verticies and edges we would like to use for this lab. Below you will see a series of `CREATE` statements. These statements describe our graph solution. When you look at the `CREATE` statements of `EDGES` you will notice `To` and `From`. This is descibing the connections between verticies. Also note at this step we are populating the attributes along with the types. 

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH Rec2HyperMarketingGraph

CREATE GRAPH Rec2HyperMarketingGraph()
USE GRAPH Rec2HyperMarketingGraph

CREATE SCHEMA_CHANGE JOB Rec2HyperMarketingGraph_change_job FOR GRAPH Rec2HyperMarketingGraph {

ADD VERTEX product(PRIMARY_ID id STRING, name STRING, latitude FLOAT, longitude FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX feature(PRIMARY_ID id STRING, name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX customer(PRIMARY_ID id STRING, name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX history(PRIMARY_ID id STRING, name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX demographic(PRIMARY_ID id STRING, name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD VERTEX context(PRIMARY_ID id STRING, ctxValue STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="true";
ADD UNDIRECTED EDGE demo_customer(FROM demographic, TO customer);
ADD UNDIRECTED EDGE customer_history(FROM customer, TO history);
ADD UNDIRECTED EDGE history_product(FROM history, TO product);
ADD UNDIRECTED EDGE demo_feature(FROM demographic, TO feature, affinity DOUBLE);
ADD UNDIRECTED EDGE customer_feature(FROM customer, TO feature, affinity DOUBLE);
ADD UNDIRECTED EDGE product_feature(FROM product, TO feature, weight DOUBLE);
ADD UNDIRECTED EDGE product_context(FROM product, TO context);
}

RUN SCHEMA_CHANGE JOB Rec2HyperMarketingGraph_change_job
DROP JOB Rec2HyperMarketingGraph_change_job
''', options=[])
