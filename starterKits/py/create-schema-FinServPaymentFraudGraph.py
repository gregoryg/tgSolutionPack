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
DROP GRAPH FinServPaymentFraudGraph

CREATE GRAPH FinServPaymentFraudGraph()
USE GRAPH FinServPaymentFraudGraph

CREATE SCHEMA_CHANGE JOB FinServPaymentFraudGraph_change_job FOR GRAPH FinServPaymentFraudGraph {

ADD VERTEX email(PRIMARY_ID id STRING, address STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX bank(PRIMARY_ID id STRING, name STRING, ABA_routing_number UINT, swift_code UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX device(PRIMARY_ID id STRING, manufacturer STRING, model STRING, IMEI STRING, trust_score FLOAT DEFAULT "0.5") WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX payment(PRIMARY_ID id STRING, amount FLOAT, transaction_date STRING, transactionEpoch UINT, trust_score FLOAT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX phone_number(PRIMARY_ID id STRING, number STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX merchant_account(PRIMARY_ID id STRING, create_date STRING, createEpoch UINT, phone_number STRING, email STRING) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX user_account(PRIMARY_ID id STRING, created_date STRING, createEpoch UINT, trust_score FLOAT DEFAULT "0.5") WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD VERTEX user(PRIMARY_ID id STRING, id STRING, created_date STRING, mobile STRING, trust_score FLOAT DEFAULT "0.5", createEpoch UINT) WITH STATS="OUTDEGREE_BY_EDGETYPE", PRIMARY_ID_AS_ATTRIBUTE="false";
ADD DIRECTED EDGE used_with(FROM device, TO phone_number) WITH REVERSE_EDGE="reverse_used_with";
ADD DIRECTED EDGE used_for(FROM device, TO payment) WITH REVERSE_EDGE="reverse_used_for";
ADD DIRECTED EDGE receives_pmnt(FROM payment, TO merchant_account) WITH REVERSE_EDGE="reverse_receives_pmnt";
ADD DIRECTED EDGE has_num(FROM user_account, TO phone_number) WITH REVERSE_EDGE="reverse_has_num";
ADD DIRECTED EDGE has_email(FROM user_account, TO email) WITH REVERSE_EDGE="reverse_has_email";
ADD DIRECTED EDGE sends(FROM user_account, TO payment) WITH REVERSE_EDGE="reverse_sends";
ADD DIRECTED EDGE receives(FROM payment, TO user_account) WITH REVERSE_EDGE="reverse_receives";
ADD DIRECTED EDGE user_account_bank(FROM user_account, TO bank) WITH REVERSE_EDGE="reverse_user_account_bank";
ADD DIRECTED EDGE associated_with(FROM device, TO user_account) WITH REVERSE_EDGE="reverse_associated_with";
ADD DIRECTED EDGE sends_pmnt(FROM merchant_account, TO payment) WITH REVERSE_EDGE="reverse_sends_pmnt";
ADD DIRECTED EDGE merchant_account_device(FROM merchant_account, TO device) WITH REVERSE_EDGE="reverse_merchant_account_device";
ADD DIRECTED EDGE merchant_account_bank(FROM merchant_account, TO bank) WITH REVERSE_EDGE="reverse_merchant_account_bank";
ADD DIRECTED EDGE authenticated_by_num(FROM user, TO phone_number) WITH REVERSE_EDGE="reverse_authenticated_by_num";
ADD DIRECTED EDGE authenticated_by_email(FROM user, TO email) WITH REVERSE_EDGE="reverse_authenticated_by_email";
ADD DIRECTED EDGE sets_up(FROM user, TO user_account) WITH REVERSE_EDGE="reverse_sets_up";
}

RUN SCHEMA_CHANGE JOB FinServPaymentFraudGraph_change_job
DROP JOB FinServPaymentFraudGraph_change_job
''', options=[])
