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


@app.get("/synchronize")
def synchronize(is_green: bool, phase_length: float = None, infer_phase_length: bool = False):

    if phase_length is not None and infer_phase_length:
        return {
            "status": "ERROR",
            "message": "Phase length cannot be updated at the same time while automatically infering the phase length",
            "id_light": 1,
            "data": ""
        }

    data_dict = None

    if os.path.isfile("data.json"):
        with open("data.json", "r") as data_file:
            data_dict = json.load(data_file)

    if data_dict is None:
        # this should only be executed if the data file is not present yet => first time
        data_dict = {
            "last_synchronization_time": time.time() - 40.0,
            "last_synchronization_is_green": not is_green,
            "phase_durations": {
                "red": 50.0,
                "green": 40.0
	        }
        }
        
    # update phase lengths if needed
    if infer_phase_length:
        time_difference = time.time() - float(data_dict["last_synchronization_time"])
        if bool(data_dict["last_synchronization_is_green"]):
            data_dict["phase_durations"]["green"] = time_difference
        else:
            data_dict["phase_durations"]["red"] = time_difference

    if phase_length is not None:
        if is_green:
            data_dict["phase_durations"]["green"] = phase_length
        else:
            data_dict["phase_durations"]["red"] = phase_length

    data_dict["last_synchronization_time"] = time.time()
    data_dict["last_synchronization_is_green"] = is_green
    
    with open("data.json", "w") as data_file:
        json.dump(data_dict, data_file)

    return {
        "status": "SUCCESS",
        "message": "",
        "id_light": 1,
        "data": data_dict
    }

@app.get("/seconds_phase_left")
def get_seconds_phase_left():
    if os.path.isfile("data.json"):
        with open("data.json", "r") as data_file:
            data_dict = json.load(data_file)

            phase_durations = {
                True: data_dict["phase_durations"]["green"],
                False: data_dict["phase_durations"]["red"]
            }

            time_difference_sync = time.time() - float(data_dict["last_synchronization_time"])
            time_difference = time_difference_sync
            current_phase_green = bool(data_dict["last_synchronization_is_green"])

            while True:
                # TODO: make this more beautiful, e.g. by saving the last toogle time
                if time_difference < phase_durations[current_phase_green]:
                    break
                else:
                    time_difference = time_difference - phase_durations[current_phase_green]
                    current_phase_green = not current_phase_green

            return {
                "status": "OK",
                "message": "",
                "id_light": 1,
                "is_green": current_phase_green,
                "is_red": not current_phase_green,
                "seconds_phase_left": phase_durations[current_phase_green] - time_difference,
                "seconds_phase_total": phase_durations[current_phase_green],
                "time_since_last_toogle": time_difference,
                "time_since_last_sync": time_difference_sync
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
