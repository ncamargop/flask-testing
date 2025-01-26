from sqlalchemy import Enum, Boolean, Numeric, DateTime, func
from app import db



## DB MODEL FOR POSGRES
class OfferModel(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.String(80), primary_key =True)
    postId = db.Column(db.String(80), nullable =False)
    userId = db.Column(db.String(80), nullable =False)
    description = db.Column(db.String(140)) 
    size = db.Column(db.Enum('LARGE', 'MEDIUM', 'SMALL', name='size_enum')) #check if this is ok
    fragile = db.Column(Boolean, nullable=False, default=False)
    offer = db.Column(Numeric(10,2), nullable=False)
    createdAt = db.Column(DateTime, nullable=False, default=func.now())