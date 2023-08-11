from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import datetime
import psycopg2
import json
import os

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    created_ts: str
    update_ts: str

@app.get("/items")
def read():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select id, name, created_ts, updated_ts from item;")
    result = json.dumps(cur.fetchall(), default=str, indent=4)
    return result


@app.get("/items/{id}")
def read_item(id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select id, name, created_ts, updated_ts from item where id = (%s);", [id])
    result = json.dumps(cur.fetchall(), default=str, indent=4)
    return result


@app.put("/items/{id}")
def put_item(id: int, name: str):
    conn = get_conn()
    cur = conn.cursor()
    created_ts = datetime.datetime.now().isoformat()
    updated_ts = datetime.datetime.now().isoformat()
    cur.execute("insert into item (id, name, created_ts, updated_ts) values (%s, %s, %s, %s);", [id, name, created_ts, updated_ts])
    conn.commit()
    return "success"


def get_conn():
    conn = psycopg2.connect(
        host="postgres_db",
        database="postgres",
        user="postgres",
        password="<enter_pwd>"
        )
    return conn