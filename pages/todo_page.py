from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TodoPage:
    URL = "https://demo.playwright.dev/todomvc/"

    # Locators
    NEW_TODO_INPUT = (By.CLASS_NAME, "new-todo")
    TODO_ITEMS = (By.CSS_SELECTOR, "ul.todo-list li")
    ERROR_MESSAGE = None  # Bu demo app'te klasik error text yok, istersen sonra ekleriz

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def add_todo(self, text: str):
        """
        Yeni bir todo ekler.
        """
        input_box = self.wait.until(
            EC.visibility_of_element_located(self.NEW_TODO_INPUT)
        )
        input_box.clear()
        input_box.send_keys(text + "\n")  # Enter ile ekleme

    def get_todos(self):
        """
        Listedeki tüm todo item'larını döner.
        """
        return self.driver.find_elements(*self.TODO_ITEMS)

    def get_todo_texts(self):
        """
        Sadece todo yazılarını list olarak döner.
        """
        items = self.get_todos()
        return [item.text for item in items]
    
    def get_todo_count(self) -> int:
        return len(self.driver.find_elements(*self.TODO_ITEMS))

