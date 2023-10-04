import unittest
from models import db, User

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_new_user(self):
        user = User(first_name='John', last_name='Doe')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_full_name_property(self):
        user = User(first_name='John', last_name='Doe')
        self.assertEqual(user.full_name, 'John Doe')

if __name__ == '__main__':
    unittest.main()
