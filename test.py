try:
    from run import app
    import unittest
    import requests
    import os

except Exception as e:
    print("Some modules are missing: {} ".format(e))


class FlaskAPI_Testing(unittest.TestCase):
    PATH = 'http://127.0.0.1:5000'

    # Ensure flask api is Listening
    def test_1_get_all_index(self):
        tester = app.test_client(self)
        response = tester.get(FlaskAPI_Testing.PATH, content_type='html/text')
        self.assertEqual(response.status_code, 308)

    # Ensure Api is listenig at allContacts
    def test_2_get_all_contacts(self):
        tester = app.test_client(self)
        response = tester.get(f"{FlaskAPI_Testing.PATH}/contacts", content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure Api is listenig at search
    def test_3_get_contact_from_search(self):
        tester = app.test_client(self)
        response = tester.post(f"{FlaskAPI_Testing.PATH}/search", data={'search': 'Rem'})
        self.assertEqual(response.status_code, 405)

    # Ensure Api is listenig at contact/delete and delete contact
    def test_4_delete_contact(self):
        tester = app.test_client(self)
        response = tester.post(f"{FlaskAPI_Testing.PATH}/contacts/delete", data={'id': '1'})
        self.assertEqual(response.status_code, 302)

    # Ensure Api is listenig at edit_contact
    def test_5_edit_contact(self):
        tester = app.test_client(self)
        response = tester.post(f"{FlaskAPI_Testing.PATH}/edit_contact/1", data={})
        self.assertEqual(response.status_code, 200)

    # Ensure Api is listenig at allContacts
    def test_2_get_all_contacts(self):
        tester = app.test_client(self)
        response = tester.get(f"{FlaskAPI_Testing.PATH}/contacts", content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure Api is listenig at allContacts
    def test_2_get_create_contacts(self):
        tester = app.test_client(self)
        response = tester.get(f"{FlaskAPI_Testing.PATH}/contacts", data={'name': "Prateek", 'email': 'Prateek@gmail.com', 'phone_number': "9452739871"}, content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main(exit=False)     
