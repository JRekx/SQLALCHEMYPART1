import unittest
from app import app, db, User

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_root_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for redirection

    def test_users_index_route(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for OK

    # Add more test cases for other routes as needed

if __name__ == '__main__':
    unittest.main()
