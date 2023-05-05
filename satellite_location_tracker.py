#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymongo


# In[2]:


import pymongo
import time
import json
import pandas as pd
import requests


# In[3]:


# Define the MongoDB connection string
mongo_conn_str = "mongodb://<database_name>:<password_for_database>@ac-yaydskh-shard-00-00.dbdtjgb.mongodb.net:27017,ac-yaydskh-shard-00-01.dbdtjgb.mongodb.net:27017,ac-yaydskh-shard-00-02.dbdtjgb.mongodb.net:27017/?ssl=true&replicaSet=atlas-xjikdp-shard-0&authSource=admin&retryWrites=true&w=majority"

# Define the URL for the API request
url = 'http://api.open-notify.org/iss-now.json'



# In[5]:


# Connect to MongoDB and create a connection object
try:
    conn = pymongo.MongoClient(mongo_conn_str)
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e)
    exit()

# Create a variable to hold the satellite data
sat_Data = []
sat_Conn = conn["satellite"]
db_Var = sat_Conn["location"]

# Define a variable for the number of retries
num_Retries = 3

# Loop through the API request
for i in range(10800):
    # Try to establish a connection to the API
    for j in range(num_Retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            break
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            print("Connection error: %s" % e)
            if j < num_Retries - 1:
                print("Retrying...")
            else:
                print("Max retries exceeded. Exiting...")
                exit()

    # If the response was successful, insert the data into MongoDB
    if response.status_code == 200:
        data = response.json()
        db_Var.insert_one(data)
        time.sleep(1)


# In[ ]:




