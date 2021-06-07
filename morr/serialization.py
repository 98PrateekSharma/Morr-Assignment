from morr import db
from morr.models import Contact
from morr import ma


class Contact_Book_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact
        include_fk = True
