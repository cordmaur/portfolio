"""Docstring"""

import os
from typing import Optional
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC

# add comments to the SeleniumPage class


class SeleniumPage:
    """
    Open a page with selenium and provide the most basic commands to navigate
    the page.
    """

    def __init__(
        self,
        url: Optional[str] = None,
        implicit_wait_seconds: float = 60,
        window_size: str = "1024,768",
        headless: bool = True,
        display: str = "host.docker.internal:0",
    ):
        """
        Initializes a new SeleniumPage instance.

        Args:
            url (str): The URL of the page to open.
            implicit_wait_seconds (float): The implicit wait time in seconds. Defaults to 60.
            window_size (str): The window size in the format "width, height".
            Defaults to "1920, 1080".
            headless (bool): Whether to run the browser in headless mode. Defaults to True.
            display (str): The display to use. Defaults to "host.docker.internal:0".
        """
        # set the DISPLAY variable
        os.environ["DISPLAY"] = display

        # configure the chrome options to run in headless mode if requested
        options = webdriver.ChromeOptions()
        options.add_argument(f"window-size={window_size}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if headless:
            options.add_argument("--headless=new")

        # create the driver
        driver = webdriver.Chrome(options)
        # set the implicit wait time
        driver.implicitly_wait(implicit_wait_seconds)

        # open the page
        if url is not None:
            driver.get(url)

        # store the driver and implicit wait time
        self._driver = driver
        self._implicit_wait_seconds = implicit_wait_seconds

    def get(self, url: str):
        """
        Opens a new page in the browser.

        Args:
            url (str): The URL of the page to open.

        Returns:
            None
        """
        self._driver.get(url)

    def fill_input(self, element: str, value: str, by: str = By.XPATH, wait_time=0):
        """
        Fills an input element on the current page with the specified value.

        Args:
            element (str): The identifier of the input element to fill.
            value (str): The value to fill the input element with.
            by (str, optional): The method to use when finding the input element.
            Defaults to By.XPATH.
            wait_time (int, optional): The time to wait before filling the input element.
            Defaults to 0.

        Returns:
            None
        """
        sleep(wait_time)
        input_el = self._driver.find_element(by=by, value=element)
        input_el.clear()
        input_el.send_keys(value)

    def click(self, element: str, by: str = By.XPATH, wait_time=0):
        """
        Clicks on an element on the current page.

        Args:
            element (str): The identifier of the element to click.
            by (str, optional): The method to use when finding the element. Defaults to By.XPATH.
            wait_time (int, optional): The time to wait before clicking the element. Defaults to 0.

        Returns:
            None
        """

        sleep(wait_time)
        button = self._driver.find_element(by=by, value=element)
        button.click()

    def get_value(
        self, element: str, wait_time: float = 0.0, by=By.XPATH, dont_wait=False
    ) -> str:
        """
        Retrieves the text value of an element on the current page.

        Args:
            element (str): The identifier of the element to retrieve the text value from.
            wait_time (float, optional): The time to wait before retrieving the text value.
            Defaults to 0.0.
            by (By, optional): The method to use when finding the element. Defaults to By.XPATH.
            dont_wait (bool, optional): Whether to return an empty string if the element does not exist.
            Defaults to False.

        Returns:
            str: The text value of the element.
        """
        sleep(wait_time)

        if dont_wait:
            if not self.element_exists(element=element, by=by):
                return ""

        el = self._driver.find_element(by=by, value=element)
        return el.text

    def scroll_down(self, steps: int = 1, height: int = 1000, sleep_time: float = 0.5):
        """
        Scrolls down a webpage by executing a JavaScript script.

        Args:
            steps (int): The number of times to scroll down. Defaults to 1.
            height (int): The height to scroll down by each step. Defaults to 1000.

        Returns:
            None
        """
        for i in range(steps):
            self._driver.execute_script(f"window.scrollTo({i*height}, {(i+1)*height});")
            sleep(sleep_time)

    def element_exists(self, element: str, by: str = By.XPATH):
        """
        Checks if an element exists on the current page.

        Args:
            element (str): The identifier of the element to check.
            by (str, optional): The method to use when finding the element. Defaults to By.XPATH.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        # before checking, lets set wait time to zero
        self._driver.implicitly_wait(0)

        # loook for the element(s)
        els = self._driver.find_elements(by=by, value=element)
        self._driver.implicitly_wait(self._implicit_wait_seconds)

        return len(els) > 0

    def wait_for_element(self, element: str, by: str = By.XPATH, post_wait: float = 0):
        """
        Waits for an element to be present on the current page.

        Args:
            element (str): The identifier of the element to wait for.
            by (str, optional): The method to use when finding the element. Defaults to By.XPATH.
            post_wait (float, optional): The time to wait after the element is found. Defaults to 0.

        Returns:
            None
        """
        WebDriverWait(self._driver, self._implicit_wait_seconds).until(
            EC.presence_of_element_located((By.XPATH, element))
        )

        sleep(post_wait)

    def wait_for_value(
        self, element: str, value: str, by: str = By.XPATH, post_wait: float = 0
    ):
        """
        Waits for the specified element to have a certain value.

        Args:
            element (str): The identifier of the element to wait for.
            value (str): The value to wait for.
            by (str, optional): The method to use when finding the element. Defaults to By.XPATH.
            post_wait (float, optional): The time to wait after the value is found. Defaults to 0.

        Returns:
            None
        """
        WebDriverWait(self._driver, self._implicit_wait_seconds).until(
            EC.text_to_be_present_in_element((by, element), value)
        )
        sleep(post_wait)

    def dismiss_alerts(self, wait_for_alert=False):
        """
        Dismisses alerts on the current page.

        Args:
                wait_for_alert (bool): Whether to wait for the alert to appear before dismissing it.
                Defaults to False.

        Returns:
                None
        """
        #     # if wait_for_alert:
        #     #     print("Esperando dar o alerta antes de fechá-lo")
        #     #     WebDriverWait(self.driver, self.implicit_wait).until(EC.alert_is_present())

        print("Dismissing alerts")

        if wait_for_alert:
            print("Esperando aparecer alerta para fechar")
        else:
            # set  wait time to zero
            self._driver.implicitly_wait(0)

        # get alerts
        els = self._driver.find_elements(
            "xpath", "//button[@data-bs-dismiss='alert'][@aria-labe='Close']"
        )

        if len(els) > 0:
            for el in els:
                el.click()

        self._driver.implicitly_wait(self._implicit_wait_seconds)

    def close(self):
        """
        Closes the driver and quits the browser session.

        This method is used to gracefully close the driver and terminate the browser session.
        It is typically called when you want to safely exit the program and release the resources.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        self._driver.quit()

    def save_snapshot(self, name: str):
        """
        Saves a screenshot of the current page.

        Args:
            name (str): The name of the screenshot file.

        Returns:
            None
        """
        name = Path(name)

        self._driver.save_screenshot(name.with_suffix(".png"))

        # save the page source as name.html
        with open(name.with_suffix(".html"), "w", encoding="utf-8") as f:
            f.write(self._driver.page_source)

    def __del__(self):
        """
        Destructor method to close the driver when the object is about to be destroyed.

        This method is automatically called when the object is no longer needed and is about to be destroyed.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        self.close()
