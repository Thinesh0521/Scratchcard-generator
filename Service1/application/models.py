from application import db

# Database Model
class prizedb(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    code= db.Column(db.String(50), nullable=False)
    reward= db.Column(db.String(100), nullable= False)

