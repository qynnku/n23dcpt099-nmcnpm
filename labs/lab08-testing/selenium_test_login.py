import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

class TestLoginForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Đường dẫn tới chromedriver nếu cần: executable_path='...'
        cls.driver = webdriver.Chrome()
        cls.driver.get('file:///Users/jun/Downloads/MON_NHAP_MON_CNPM/LAB1/labs/lab08-testing/index.html')
        cls.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.refresh()
        time.sleep(0.5)

    def test_login_success(self):
        self.driver.find_element(By.ID, 'username').send_keys('user')
        self.driver.find_element(By.ID, 'password').send_keys('pass')
        self.driver.find_element(By.ID, 'loginForm').submit()
        alert = Alert(self.driver)
        self.assertEqual(alert.text, 'Đăng nhập thành công!')
        alert.accept()

    def test_login_empty_username(self):
        self.driver.find_element(By.ID, 'password').send_keys('pass')
        self.driver.find_element(By.ID, 'loginForm').submit()
        alert = Alert(self.driver)
        self.assertEqual(alert.text, 'Vui lòng nhập đầy đủ thông tin!')
        alert.accept()

    def test_login_empty_password(self):
        self.driver.find_element(By.ID, 'username').send_keys('user')
        self.driver.find_element(By.ID, 'loginForm').submit()
        alert = Alert(self.driver)
        self.assertEqual(alert.text, 'Vui lòng nhập đầy đủ thông tin!')
        alert.accept()

    def test_login_empty_both(self):
        self.driver.find_element(By.ID, 'loginForm').submit()
        alert = Alert(self.driver)
        self.assertEqual(alert.text, 'Vui lòng nhập đầy đủ thông tin!')
        alert.accept()

    def test_login_remember_me(self):
        self.driver.find_element(By.ID, 'username').send_keys('user')
        self.driver.find_element(By.ID, 'password').send_keys('pass')
        self.driver.find_element(By.ID, 'rememberMe').click()
        self.driver.find_element(By.ID, 'loginForm').submit()
        alert = Alert(self.driver)
        self.assertEqual(alert.text, 'Đăng nhập thành công! (Đã ghi nhớ đăng nhập)')
        alert.accept()

if __name__ == '__main__':
    unittest.main()
