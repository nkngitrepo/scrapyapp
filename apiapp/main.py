from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from databases import Database
import sys

database = Database("postgresql://admin:admin@db/admin")

class CBOL(BaseModel):
    name: str
    description: Optional[str] = None

app = FastAPI()

@app.on_event("startup")
async def database_connect():
    import time
    time.sleep(30)
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

@app.post("/CBOL/")
async def insert_item(cbol: CBOL):
    d = cbol.dict()
    if not cbol.name:
        return {"Error":"Mandatory fields are missing"}
    query = "insert into container_bol_requests(cid) values (:cid)"
    await database.execute_many(query=query,values=[{"cid":cbol.name.strip()}])
    return d

@app.get("/")
async def read_root():
    query = "select * from container_bol_requests"
    results = await database.fetch_all(query=query)
    #return {"Hello": "World"}
    return results


@app.get("/request/{container_id}")
async def read_item(container_id: str):
    res = {}
    try:
        query = "select type from req_type where id='"+container_id+"';"
        results = await database.fetch_all(query=query)
        if not results:
            return {'ERROR':container_id+" seems invalid"}
        
        res =results
        if res[0]['type'].strip() == 'CONT':
            query = "select * from container where cid='"+container_id+"';"
            results = await database.fetch_all(query=query)
            res =results
        else:
            query = "select * from bol where bid='"+container_id+"';"
            results = await database.fetch_all(query=query)
            res = results
    except Exception as e:
        print (str(e),file=sys.stderr)
    
    return res
