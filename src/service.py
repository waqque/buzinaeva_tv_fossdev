import requests
import numpy
import fastapi
import os

def create_service():
    return {"status": "ok"}

if __name__ == "__main__":
    print(create_service())