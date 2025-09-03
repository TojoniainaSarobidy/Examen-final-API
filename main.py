from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

phones_db: List[Phone] = []

@app.get("/health")
def health():
    return "OK"

@app.post("/phones",status_code=201)
def create_phones(phones: List[Phone]):
    phones_db.extend(phones)
    return {"message": "added successfully."}

@app.get("/phones/{id}")
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(status_code=404, detail="Phone with id '{id}' not found.")