import subprocess
import os
import re
from pathlib import Path
from fastapi import FastAPI
import datetime

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
    seconds_phase_total = 40.000
    return {
        "id_light": 1,
        "is_green": True,
        "is_red": False,
        "seconds_phase_left": seconds_phase_total - (datetime.datetime.now().timestamp() % 40),
        "seconds_phase_total": seconds_phase_total,
    }