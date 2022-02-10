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
host = "https://tg-se-demo-hub.i.tgcloud.io"
username = "tigergraph"
password = "TigerG123"  

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema
# Let's define the verticies and edges we would like to use for this lab. Below you will see a series of `CREATE` statements. These statements describe our graph solution. When you look at the `CREATE` statements of `EDGES` you will notice `To` and `From`. This is descibing the connections between verticies. Also note at this step we are populating the attributes along with the types. 

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH SupplyChainGraph

CREATE GRAPH SupplyChainGraph()
USE GRAPH SupplyChainGraph

CREATE SCHEMA_CHANGE JOB SupplyChainGraph_change_job FOR GRAPH SupplyChainGraph {

ADD VERTEX product(PRIMARY_ID pid STRING, name STRING, price FLOAT, formula STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX site(PRIMARY_ID sid STRING, name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX p_order(PRIMARY_ID orderId STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX stocking(PRIMARY_ID stockingId STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD DIRECTED EDGE usedBy(FROM product, TO product, formula_order STRING, useAmount FLOAT) WITH REVERSE_EDGE="reverseUsedBy";
ADD DIRECTED EDGE deliver(FROM site, TO site, itemId STRING) WITH REVERSE_EDGE="reverseDeliver";
ADD DIRECTED EDGE produce(FROM site, TO product) WITH REVERSE_EDGE="reverseProduce";
ADD UNDIRECTED EDGE prodOrder(FROM p_order, TO product, amount INT);
ADD UNDIRECTED EDGE prodStocking(FROM stocking, TO product, amount INT);
}

RUN SCHEMA_CHANGE JOB SupplyChainGraph_change_job
DROP JOB SupplyChainGraph_change_job
''', options=[])
