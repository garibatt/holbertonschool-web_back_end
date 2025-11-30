#!/usr/bin/env python3
"""this is docstring"""
from pymongo import MongoClient

def main():
    """this is docstring"""
    # Connect to MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection =client.logs.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # Number of logs per HTTP method
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print("\t{}: {}".format(method, count))

    # Number of GET requests to /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} GET /status requests".format(status_count))

if __name__ == "__main__":
    """this is docstring"""
    main()
