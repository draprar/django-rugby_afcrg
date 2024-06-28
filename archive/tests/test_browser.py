import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(url='http://127.0.0.1:8000/admin/')


class ClickAllButtonsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_click_all_buttons(self):
        self.driver.get("http://127.0.0.1:8000/")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.is_displayed() and button.is_enabled():
                button.click()

    def tearDown(self):
        self.driver.quit()


class PageResponseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_page_response(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn("TongueTwister", self.driver.title)

    def tearDown(self):
        self.driver.quit()


class ElementClickabilityTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_element_clickable(self):
        self.driver.get("http://127.0.0.1:8000/")
        button = self.driver.find_element(By.ID, "nav-logo")
        self.assertTrue(button.is_enabled())
        button.click()

    def tearDown(self):
        self.driver.quit()


class ScrollAndNavbar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_scroll_page(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "footer"))
        )
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "footer").is_displayed())

        self.driver.execute_script("window.scrollTo(0, 0);")
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "header").is_displayed())

    def test_navbar_links(self):
        self.driver.get("http://127.0.0.1:8000/")

        navbar_links = self.driver.find_elements(By.CSS_SELECTOR, "nav a")
        for link in navbar_links:
            link.click()
            WebDriverWait(self.driver, 5).until(EC.url_contains(link.get_attribute("href")))
            self.driver.back()
            WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a")))

            self.driver.get(self.driver.get("http://127.0.0.1:8000/"))

    def test_accordion(self):
        self.driver.get("http://127.0.0.1:8000/archive/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "accordion"))
        )

        accordion_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".accordion-button")

        for button in accordion_buttons:
            button.click()
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".accordion-body"))
            )

            accordion_body = button.find_element(By.XPATH, "../..").find_element(By.CSS_SELECTOR, ".accordion-body")
            self.assertTrue(accordion_body.is_displayed())

            button.click()
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".accordion-body"))
            )

            self.assertFalse(accordion_body.is_displayed())

    def test_add_record(self):
        self.driver.get(self.driver.get("http://127.0.0.1:8000/admin/"))

        self.driver.find_element(By.NAME, "username").send_keys("*")
        self.driver.find_element(By.NAME, "password").send_keys("*")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Navigate to the model add page
        self.driver.find_element(By.LINK_TEXT, "Archive").click()
        self.driver.find_element(By.LINK_TEXT, "Posts").click()
        self.driver.find_element(By.LINK_TEXT, "Dodaj").click()

        # Fill in the form
        self.driver.find_element(By.NAME, "author").send_keys("testauthor")
        self.driver.find_element(By.NAME, "title").send_keys("testtitle")
        self.driver.find_element(By.NAME, "title").send_keys("testext")

        # Save the form
        self.driver.find_element(By.NAME, "_save").click()

        # Check if the record is added
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "success").is_displayed())

    def tearDown(self):
        self.driver.quit()

