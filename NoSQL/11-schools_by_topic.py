#!/usr/bin/env python3
"""Where can I learn Python?"""

def schools_by_topic(mongo_collection, topic):
    """return specific from a MongoDB collection"""
    result = list(mongo_collection.find({"topics": topic}))
    return result
