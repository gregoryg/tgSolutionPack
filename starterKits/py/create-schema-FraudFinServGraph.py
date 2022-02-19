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
DROP GRAPH FraudFinServGraph

CREATE GRAPH FraudFinServGraph()
USE GRAPH FraudFinServGraph

CREATE SCHEMA_CHANGE JOB FraudFinServGraph_change_job FOR GRAPH FraudFinServGraph {

ADD VERTEX Transaction(PRIMARY_ID id STRING, ts UINT, amount FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX User(PRIMARY_ID id STRING, signupEpoch UINT, mobile STRING, trust_score FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Device_Token(PRIMARY_ID id STRING, is_banned BOOL, os_name STRING, os_version STRING, model STRING, carrier STRING, is_rooted BOOL, is_emulator BOOL, device_name STRING, trust_score FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX Payment_Instrument(PRIMARY_ID id STRING, token_handle STRING, token_type STRING, card_issuing_country_iso2 STRING, card_issuing_bank STRING, card_bin STRING, trust_score FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD DIRECTED EDGE User_Transfer_Transaction(FROM User, TO Transaction) WITH REVERSE_EDGE="User_Transfer_Transaction_Rev";
ADD DIRECTED EDGE User_Recieve_Transaction(FROM User, TO Transaction) WITH REVERSE_EDGE="User_Recieve_Transaction_Rev";
ADD UNDIRECTED EDGE User_to_Device(FROM User, TO Device_Token);
ADD UNDIRECTED EDGE User_to_Payment(FROM User, TO Payment_Instrument);
ADD DIRECTED EDGE User_Refer_User(FROM User, TO User) WITH REVERSE_EDGE="User_Referred_By_User";
}

RUN SCHEMA_CHANGE JOB FraudFinServGraph_change_job
DROP JOB FraudFinServGraph_change_job
''', options=[])
