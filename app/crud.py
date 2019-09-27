from sqlalchemy.orm import Session

from . import models, schemas


def get_trafficlightphase(db: Session, trafficlightphase_id: int):
    return (
        db.query(models.TrafficlightPhase)
        .filter(models.TrafficlightPhase.id == trafficlightphase_id)
        .first()
    )


def create_trafficlightphase(db: Session, trafficlightphase: schemas.TrafficlightPhase):
    db_trafficlightphase = models.TrafficlightPhase(
        is_green=trafficlightphase.is_green, phase_length=trafficlightphase.phase_length, commit_time=trafficlightphase.commit_time
    )
    db.add(db_trafficlightphase)
    db.commit()
    db.refresh(db_trafficlightphase)
    return db_trafficlightphase
