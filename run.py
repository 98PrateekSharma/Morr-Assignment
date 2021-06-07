from morr import app

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contack_book.db'
# db = SQLAlchemy(app)


# class Contact_Book(db.Model):

#     __tablename__ = 'contact_book'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     phone_number = db.Column(db.String(13), nullable=True, unique=False)

#     def __repr__(self):
#         return f"Contact_Book('{self.name},{self.email},{self.phone_number}')"


# contact_book = [
#     {
#         'id': 1,
#         'name': 'Bhanu Pratap Singh',
#         'email': "a@b.com",
#         'phone': "1234567890",
#         'access_key': "jbjhgjgj"
#     },
#     {
#         'id': 2,
#         'name': 'Ravi Pratap Singh',
#         'email': "r@b.com",
#         'phone': "2234567890"
#     },
#     {
#         'id': 4,
#         'name': 'Sonu Pratap Singh',
#         'email': "s@b.com",
#         'phone': "4234567890"
#     },
#     {
#         'id': 3,
#         'name': 'Hari Pratap Singh',
#         'email': "h@b.com",
#         'phone': "3234567890"
#     },

# ]


# @app.route("/")
# def documentation():
#     return render_template('templates/index.html')


# @app.route("/contacts", methods=['GET'])
# def get():
#     return jsonify({'Contacts': contact_book})


# @app.route("/contact/<int:cb_id>", methods=['GET'])
# def get_contact_using_email(cb_id):
#     return jsonify({'Contact': contact_book[cb_id]})
