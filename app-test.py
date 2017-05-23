from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Welcome to Suade Reporting API!')

    def test_reports(self):
        tester = app.test_client(self)
        response = tester.get('/api/reports/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, b'Welcome to Suade Reporting API!')

    def test_xml_report(self):
        tester = app.test_client(self)
        response = tester.get('/api/report/1.xml/', content_type='html/text')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        
    def test_pdf_report(self):
        tester = app.test_client(self)
        response = tester.get('/api/report/1.pdf/', content_type='html/text')
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_dummy_url(self):
        tester = app.test_client(self)
        response = tester.get('/api/report/xyz', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        

if __name__ == '__main__':
    unittest.main()