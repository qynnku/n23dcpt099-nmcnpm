import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLoginForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///Users/yourname/Downloads/lab04-login.html")

    def test_login_success(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        self.assertIn("Đăng nhập thành công", alert.text)
        alert.accept()

    def test_login_empty(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        self.assertIn("Vui lòng nhập đầy đủ", alert.text)
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
