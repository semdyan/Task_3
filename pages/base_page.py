from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def wait_and_get_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_and_click_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_field(self, locator, text):
        self.wait_and_get_element(locator).send_keys(text)

    def wait_and_get_text_from_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.wait_and_get_element(locator).text

    def go_to_next_tab(self):
        next_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(next_tab)

    def scroll_to_element(self, locator):
        element = self.wait_and_get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def drag_and_drop_chrome(self, locator1, locator2):
        element1 = self.wait_and_get_element(locator1)
        element2 = self.wait_and_get_element(locator2)
        self.driver.drag_and_drop(element1, element2).perform()

    def drag_and_drop_firefox_1(self, source_element, target_element):
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
        self.driver.execute_script(script, source_element, target_element)

    def drag_and_drop_firefox_2(self, locator_element, locator_target):
        element = self.get_element(locator_element)
        target = self.get_element(locator_target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()