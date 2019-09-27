import subprocess
import os
import re
from pathlib import Path
from fastapi import FastAPI

app = FastAPI()

times_list = []


@app.get("/")
def read_root():
    return {
        "message": "Congratulations, you have reached the green wave backend API, Muenster's awesome new quality of life enhancement for the cities bikers. You can find this API's documentation at http://<server address>/docs"
    }

