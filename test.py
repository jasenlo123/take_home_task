from dashboard import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        print(response)
        self.assertIn(b'Log In', response.data)

     # Ensure that dashboard requires user login
    def test_main_route_requires_login(self):
        tester = app.test_client()
        response = tester.get('/dashboard', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

        # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        app.config['LOGIN_DISABLED'] = True
        app.login_manager.init_app(app)
        tester = app.test_client()
        response = tester.get('/dashboard', follow_redirects=True)
        self.assertIn(b'member post', response.data)

if __name__ == '__main__':
    unittest.main()