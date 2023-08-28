"""
This is a Fast API to demo CRUD operations on a postgres database
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import datetime
import psycopg2
import json
import os

app = FastAPI()


@app.get("/items")
def read():
    """GET /items endpoints to retrieve all items in the postgres database

    Returns:
        json: returns a json object of items of class Item
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select id, name, created_ts, updated_ts from item;")
    result = json.dumps(cur.fetchall(), default=str)
    return result


@app.get("/items/{id}")
def read_item(id: int):
    """GET /items/{id} endpoint to retrieve a specific item from the postgres database

    Args:
        id (int): unique id of the item

    Returns:
        json: returns a json object of specific item requested
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "select id, name, created_ts, updated_ts from item where id = (%s);", [id]
    )
    result = json.dumps(cur.fetchall(), default=str)
    return result


@app.put("/items/{id}")
def put_item(id: int, name: str):
    """PUT /items/{id} creates a new item in the postgres database

    Args:
        id (int): unique identifier of an item
        name (str): name of the item

    Returns:
        str: returns a string success or failed
    """
    try:
        conn = get_conn()
        cur = conn.cursor()
        created_ts = datetime.datetime.now().isoformat()
        updated_ts = datetime.datetime.now().isoformat()
        cur.execute(
            "insert into item (id, name, created_ts, updated_ts) values (%s, %s, %s, %s);",
            [id, name, created_ts, updated_ts],
        )
        conn.commit()
        return "success"
    except Exception as e:
        print("failed")
        return str(e)


def get_conn():
    """Creates a connection object with the postgres database

    Returns:
        obj: returns a postgres connection object
    """
    conn = psycopg2.connect(
        host="postgres_db", database="postgres", user="postgres", password="XXXXXXX"
    )
    return conn
