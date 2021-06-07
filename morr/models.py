from morr import db

class Contact(db.Model):

    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=True, unique=False)

    def __repr__(self):
        return f"Contact('{self.name},{self.email},{self.phone_number}')"
