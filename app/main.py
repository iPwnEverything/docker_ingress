from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": F"From: {os.environ.get('HOSTNAME', 'HOSTNAME_DEV')}"}