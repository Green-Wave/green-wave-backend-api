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

@app.get("/seconds_phase_left")
def get_seconds_phase_left():
    # mockup
    return {
        "id_light": 1,
        "is_green": True,
        "is_red": False,
        "seconds_phase_left": 35.123,
        "seconds_phase_total": 40.000,
    }