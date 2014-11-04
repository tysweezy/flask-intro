from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
	
	# test if login response is ok.
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

    # test to see if login page loads
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Login' in response.data)

    # test if login is working correctly with correct creds
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
		)
		self.assertIn(b'You are now logged in', response.data)

    # test if login is working correctly with incorrect creds
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="wrong", password="pass"),
			follow_redirects=True
		)
		self.assertIn(b'Invalid creds. try again.', response.data)

	# ensure that logout behaves correctly
	def test_logout(self):
		tester = app.test_client(self)
		tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
		)
		response = tester.get('/logout', follow_redirects=True)
		self.assertIn(b'You are now logged out.', response.data)

    # test if main page/route requires login
	def test_main_route_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects=True)
		self.assertTrue(b'You need to be logged in first.' in response.data)

	# test that posts show up on main page
 	def test_post_show_up(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
		)
		self.assertIn(b'hey from the shell', response.data)


if __name__ == '__main__':
	unittest.main()	