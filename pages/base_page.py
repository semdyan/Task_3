from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_for_element_to_disappear(self, locator):
        self.wait.until_not(expected_conditions.visibility_of_element_located(locator))

    def wait_and_get_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_and_get_elements(self, locator):
        self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def wait_and_click_element(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def wait_until_text_changes(self, locator, text):
        self.wait.until(lambda x: self.wait_and_get_element(locator).text != text)

    def set_field(self, locator, text):
        self.wait_and_get_element(locator).send_keys(text)

    def scroll_to_element_by_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

    def drag_and_drop(self, item_locator, target):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);

                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        target = self.wait_and_get_element(target)
        self.driver.execute_script(script, item_locator, target)
