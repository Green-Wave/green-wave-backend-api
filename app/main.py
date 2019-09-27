from typing import List

import os
import json
import time

from fastapi import FastAPI
import datetime

app = FastAPI()

times_list = []


@app.get("/")
def read_root():
    return {
        "message": "Congratulations, you have reached the green wave backend API, Muenster's awesome new quality of life enhancement for the cities bikers. You can find this API's documentation at http://<server address>/docs"
    }


@app.get("/update_phase")
def update_phase(is_green: bool, phase_length: float):
    data = {
        "is_green": is_green,
        "phase_length": phase_length,
        "commit_time": time.time()
    }
    with open("data.json", "w") as data_file:
        json.dump(data, data_file)


@app.get("/seconds_phase_left")
def get_seconds_phase_left():
    if os.path.isfile("data.json"):
        with open("data.json", "r") as data_file:
            data_dict = json.load(data_file)
            return {
                "status": "OK",
                "message": "",
                "id_light": 1,
                "is_green": bool(data_dict["is_green"]),
                "is_red": not bool(data_dict["is_green"]),
                "seconds_phase_left": data_dict["commit_time"] - time.time(),
                "seconds_phase_total": data_dict["phase_length"],
            }

    else:
        # no data has been written yet
        return {
            "status": "ERROR",
            "message": "No data history",
            "id_light": 1,
            "is_green": False,
            "is_red": False,
            "seconds_phase_left": 40.000,
            "seconds_phase_total": 40.000,
        }

@app.get("/seconds_phase_left_mockup_dynamic")
def seconds_phase_left_mockup_dynamic():
    # mockup
    seconds_phase_total = 40.000
    return {
        "status": "OK",
        "message": "",
        "id_light": 1,
        "is_green": True,
        "is_red": False,
        "seconds_phase_left": seconds_phase_total - (datetime.datetime.now().timestamp() % 40),
        "seconds_phase_total": seconds_phase_total,
    }

@app.get("/seconds_phase_left_mockup_static")
def seconds_phase_left_mockup_static():
    # mockup
    seconds_phase_total = 40.000
    return {
        "status": "OK",
        "message": "",
        "id_light": 1,
        "is_green": True,
        "is_red": False,
        "seconds_phase_left": 35.123,
        "seconds_phase_total": 40.000,
    }
