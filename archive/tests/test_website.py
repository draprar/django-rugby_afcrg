import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RugbyWebsiteTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://rugby.fly.dev"

    def test_page_response(self):
        self.driver.get(self.base_url)
        self.assertEqual(self.driver.current_url.rstrip('/'), self.base_url.rstrip('/'))
        self.assertEqual(self.driver.title, "AFC Rugby Giżycko")

    def test_mobile_view(self):
        self.driver.set_window_size(375, 667)
        self.driver.get(self.base_url)

        toggle_button = self.driver.find_element(By.CLASS_NAME, "navbar-toggler")
        self.assertTrue(toggle_button.is_displayed())

        toggle_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "navbarCollapse"))
        )

        mobile_menu = self.driver.find_element(By.ID, "navbarCollapse")
        self.assertTrue(mobile_menu.is_displayed())

    def test_navbar_links(self):
        self.driver.get(self.base_url)

        navbar_links = {
            "Strona główna": "a[href='#']",
            "Drużyna": "a[href='#info']",
            "Promocja": "a[href='#media']",
            "Historia": "a[href='#about']",
            "Archiwum": "a[href='#archive']",
            "Kontakt": "a[href='#footer']"
        }

        for link_text, css_selector in navbar_links.items():
            link = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            link.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            target_element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            self.assertTrue(target_element.is_displayed())

    def test_scroll_page(self):
        self.driver.get(self.base_url)
        action = ActionChains(self.driver)

        footer = self.driver.find_element(By.ID, "footer")
        action.move_to_element(footer).perform()
        self.assertTrue(footer.is_displayed())

        self.driver.execute_script("window.scrollTo(0, 0)")
        navbar = self.driver.find_element(By.CLASS_NAME, "navbar")
        self.assertTrue(navbar.is_displayed())

    def test_click_elements(self):
        self.driver.get(self.base_url)

        elements_to_click = [
            (By.LINK_TEXT, "Strona główna"),
            (By.LINK_TEXT, "Drużyna"),
            (By.LINK_TEXT, "Promocja"),
            (By.LINK_TEXT, "Historia"),
            (By.LINK_TEXT, "Archiwum"),
            (By.LINK_TEXT, "Kontakt")
        ]

        for by, value in elements_to_click:
            try:
                element = self.driver.find_element(by, value)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
                self.assertTrue(element.is_displayed())
            except Exception as e:
                print(f"Error with element: {value}")
                print(e)
                raise e

    def test_click_all_links_in_content(self):
        self.driver.get(self.base_url)

        content_section = self.driver.find_element(By.ID, "about")

        links = content_section.find_elements(By.TAG_NAME, "a")

        for link in links:
            href = link.get_attribute("href")
            self.assertIsNotNone(href, f"Link {link.text} does not have an href attribute")

            link.click()

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )

            self.assertIn("rugby.fly.dev", self.driver.current_url)

            self.driver.back()
            self.driver.find_element(By.ID, "about")

    def test_click_all_links_in_footer(self):
        self.driver.get(self.base_url)

        footer = self.driver.find_element(By.ID, "footer")

        links = footer.find_elements(By.TAG_NAME, "a")

        for link in links:
            href = link.get_attribute("href")
            self.assertIsNotNone(href, f"Link {link.text} does not have an href attribute")

            link.click()

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )

            self.assertIn("rugby.fly.dev", self.driver.current_url)

            self.driver.back()
            self.driver.find_element(By.ID, "footer")

    def test_mark_text_hero(self):
        self.driver.get(self.base_url)

        text_section = self.driver.find_element(By.ID, "hero")

        paragraph = text_section.find_element(By.TAG_NAME, "p")

        ActionChains(self.driver).click_and_hold(paragraph).move_by_offset(100, 0).release().perform()

        selected_text = self.driver.execute_script("return window.getSelection().toString();")
        self.assertNotEqual(selected_text.strip(), "", "Text selection failed")

    def test_mark_text_info(self):
        self.driver.get(self.base_url)

        text_section = self.driver.find_element(By.ID, "info")

        paragraph = text_section.find_element(By.TAG_NAME, "p")

        ActionChains(self.driver).click_and_hold(paragraph).move_by_offset(100, 0).release().perform()

        selected_text = self.driver.execute_script("return window.getSelection().toString();")
        self.assertNotEqual(selected_text.strip(), "", "Text selection failed")

    def test_mark_text_media(self):
        self.driver.get(self.base_url)

        text_section = self.driver.find_element(By.ID, "media")

        paragraph = text_section.find_element(By.TAG_NAME, "p")

        ActionChains(self.driver).click_and_hold(paragraph).move_by_offset(100, 0).release().perform()

        selected_text = self.driver.execute_script("return window.getSelection().toString();")
        self.assertNotEqual(selected_text.strip(), "", "Text selection failed")

    def test_mark_text_about(self):
        self.driver.get(self.base_url)

        text_section = self.driver.find_element(By.ID, "about")

        paragraph = text_section.find_element(By.TAG_NAME, "p")

        ActionChains(self.driver).click_and_hold(paragraph).move_by_offset(100, 0).release().perform()

        selected_text = self.driver.execute_script("return window.getSelection().toString();")
        self.assertNotEqual(selected_text.strip(), "", "Text selection failed")

    def test_mark_text_footer(self):
        self.driver.get(self.base_url)

        footer = self.driver.find_element(By.ID, "footer")

        paragraph = footer.find_element(By.TAG_NAME, "p")

        ActionChains(self.driver).click_and_hold(paragraph).move_by_offset(100, 0).release().perform()

        selected_text = self.driver.execute_script("return window.getSelection().toString();")
        self.assertNotEqual(selected_text.strip(), "", "Text selection failed")

    def test_media_content(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.CSS_SELECTOR, "a[href='#media']").click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "media"))
        )

        youtube_iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[src*='youtube']")
        youtube_link = youtube_iframe.get_attribute("src")
        self.driver.execute_script("window.open(arguments[0]);", youtube_link)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ytd-player"))
        )
        self.assertIn("youtube.com", self.driver.current_url)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        images = self.driver.find_elements(By.CSS_SELECTOR, "img.img-fluid")
        for image in images:
            ActionChains(self.driver).context_click(image).perform()
            ActionChains(self.driver).send_keys('w').perform()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "img"))
            )
            self.assertIn("img", self.driver.current_url)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def test_accordion_behavior(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.CSS_SELECTOR, "a[href='#archive']").click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "accordion"))
        )

        accordion_buttons = self.driver.find_elements(By.CLASS_NAME, "accordion-button")
        for button in accordion_buttons:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            button.click()

            content = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, button.get_attribute("aria-controls")))
            )
            self.assertTrue(content.is_displayed(), f"Content for {button.text} should be visible")

            button.click()

            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.ID, button.get_attribute("aria-controls")))
            )
            self.assertFalse(content.is_displayed(), f"Content for {button.text} should be hidden")

    def test_404_page(self):
        non_existent_url = self.base_url + "/nonexistentpage"
        self.driver.get(non_existent_url)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        error_message = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(error_message.text, "404")

        error_description = self.driver.find_element(By.TAG_NAME, "p")
        self.assertIn("Ups! Strona nie istnieje.", error_description.text)

        self.driver.find_element(By.CSS_SELECTOR, "a[type='submit']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd(), 'tests_outcomes')
    os.makedirs(test_dir, exist_ok=True)
    test_outcome_file = os.path.join(test_dir, 'test_website_outcome.txt')

    with open(test_outcome_file, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = unittest.main(testRunner=runner, exit=False)

    print(f"Test results written to {test_outcome_file}")
