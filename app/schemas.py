from pydantic import BaseModel

class TrafficlightPhase(BaseModel):
    is_green: bool
    phase_length: float
    commit_time: float

    class Config:
        orm_mode = True
