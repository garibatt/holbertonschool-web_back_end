#!/usr/bin/env python3
"""this is docstring"""


def insert_school(mongo_collection, **kwargs):
        """this is docstring"""
        res = mongo_collection.insert_one(kwargs)
        return res.inserted_id
