from flask import jsonify, render_template, redirect, url_for, request, flash
from morr.models import Contact
from morr import app
from morr import db
from morr.serialization import Contact_Book_Schema
from morr.forms import ContactForm


# @app.route("/")
# def documentation():
#     return render_template('index.html')


# @app.route("/contacts", methods=['GET'])
# def get():
#     contact_book = Contact_Book_Schema(many=True)
#     contacts = Contact_Book.query.all()
#     output = contact_book.dump(contacts)
#     return jsonify(output)


# @app.route("/contact/<int:cb_id>", methods=['GET'])
# def get_contact_using_email(cb_id):
#     return jsonify({'Contact': contact_book[cb_id]})

# ######################################################################

@app.route("/")
def index():
    return redirect(url_for('contacts'))


@app.route("/new_contact", methods=('GET', 'POST'))
def new_contact():
    form = ContactForm()
    if form.validate_on_submit():
        my_contact = Contact()
        form.populate_obj(my_contact)
        db.session.add(my_contact)
        try:
            db.session.commit()
            flash('Contact created correctly', 'success')
            return redirect(url_for('contacts'))
        except:
            db.session.rollback()
            flash('Error generating contact.', 'danger')

    return render_template('web/new_contact.html', form=form)


@app.route("/edit_contact/<id>", methods=('GET', 'POST'))
def edit_contact(id):
    my_contact = Contact.query.filter_by(id=id).first()
    form = ContactForm(obj=my_contact)
    if form.validate_on_submit():
        try:
            form.populate_obj(my_contact)
            db.session.add(my_contact)
            db.session.commit()
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update contact.', 'danger')
    return render_template(
        'web/edit_contact.html',
        form=form)


@app.route("/contacts")
def contacts():
    contacts = Contact.query.order_by(Contact.name).all()
    return render_template('web/contacts.html', contacts=contacts)


@app.route("/search")
def search():
    name_search = request.args.get('name')
    all_contacts = Contact.query.filter(
        Contact.name.contains(name_search)
    ).order_by(Contact.name).all()
    return render_template('web/contacts.html', contacts=all_contacts)

@app.route("/searchEmail")
def searchEmail():
    email_search = request.args.get('email')
    all_contacts = Contact.query.filter(
        Contact.email.contains(email_search)
    ).order_by(Contact.name).all()
    return render_template('web/contacts.html', contacts=all_contacts)

@app.route("/contacts/delete", methods=('POST',))
def contacts_delete():
    try:
        mi_contacto = Contact.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_contacto)
        db.session.commit()
        flash('Delete successfully.', 'danger')
        print("delete")
    except:
        db.session.rollback()
        flash('Error delete  contact.', 'danger')

    return redirect(url_for('contacts'))
