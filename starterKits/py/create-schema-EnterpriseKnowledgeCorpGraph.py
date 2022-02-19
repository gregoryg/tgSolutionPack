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
host = "http://localhost"
username = "tigergraph"
password = "tigergraph"  

conn = tg.TigerGraphConnection(host=host, username=username, password=password)

# ### 1.4.1 - Create Schema
# Let's define the verticies and edges we would like to use for this lab. Below you will see a series of `CREATE` statements. These statements describe our graph solution. When you look at the `CREATE` statements of `EDGES` you will notice `To` and `From`. This is descibing the connections between verticies. Also note at this step we are populating the attributes along with the types. 

# DEFINE / CREATE ALL EDGES AND VERTICES 
conn.gsql(''' 
USE GLOBAL
DROP GRAPH EnterpriseKnowledgeCorpGraph

CREATE GRAPH EnterpriseKnowledgeCorpGraph()
USE GRAPH EnterpriseKnowledgeCorpGraph

CREATE SCHEMA_CHANGE JOB EnterpriseKnowledgeCorpGraph_change_job FOR GRAPH EnterpriseKnowledgeCorpGraph {

ADD VERTEX Person(PRIMARY_ID name STRING, gender STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Company(PRIMARY_ID name STRING, registered_capital UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Project(PRIMARY_ID name STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD UNDIRECTED EDGE WorkFor(FROM Person, TO Company, title STRING);
ADD UNDIRECTED EDGE PersonInvestCompany(FROM Person, TO Company, invest_year UINT, amount DOUBLE, control_type STRING);
ADD DIRECTED EDGE CompanyInvestCompany(FROM Company, TO Company, invest_year UINT, amount DOUBLE, control_type STRING) WITH REVERSE_EDGE="reverse_CompanyInvestCompany";
ADD UNDIRECTED EDGE BidFor(FROM Company, TO Project, price DOUBLE, solution STRING);
}

RUN SCHEMA_CHANGE JOB EnterpriseKnowledgeCorpGraph_change_job
DROP JOB EnterpriseKnowledgeCorpGraph_change_job
''', options=[])
