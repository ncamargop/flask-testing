from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, Boolean, Numeric, DateTime, func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


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


    

@app.route('/', methods=['GET']) # Also can use .get()
def home():
    return 'hola mundo'

if __name__ == '__main__':
    app.run(debug=True)