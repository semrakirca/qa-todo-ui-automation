import pytest
from pages.todo_page import TodoPage


def test_add_single_todo(driver):
    page = TodoPage(driver)

    # 1) Sayfayı aç
    page.open()

    # 2) Yeni bir todo ekle
    page.add_todo("Kitap oku")

    # 3) Listede var mı kontrol et
    todos = page.get_todo_texts()

    assert "Kitap oku" in todos


@pytest.mark.parametrize("task_text", ["Spor yap", "Alışveriş yap", "Mail kontrol et"])
def test_add_multiple_todos(driver, task_text):
    page = TodoPage(driver)

    page.open()
    page.add_todo(task_text)

    todos = page.get_todo_texts()

    assert task_text in todos
import pytest
from pages.todo_page import TodoPage


def test_add_single_todo(driver):
    page = TodoPage(driver)

    # 1) Sayfayı aç
    page.open()

    # 2) Yeni bir todo ekle
    page.add_todo("Kitap oku")

    # 3) Listede var mı kontrol et
    todos = page.get_todo_texts()

    assert "Kitap oku" in todos


@pytest.mark.parametrize("task_text", ["Spor yap", "Alışveriş yap", "Mail kontrol et"])
def test_add_multiple_todos(driver, task_text):
    page = TodoPage(driver)

    page.open()
    page.add_todo(task_text)

    todos = page.get_todo_texts()

    assert task_text in todos

def test_empty_todo_is_not_added(driver):
    page = TodoPage(driver)
    page.open()

    page.add_todo("")  # boş

    todos = page.get_todo_texts()
    assert len(todos) == 0

def test_whitespace_todo_is_not_added(driver):
    page = TodoPage(driver)
    page.open()

    page.add_todo("   ")

    todos = page.get_todo_texts()
    assert len(todos) == 0

def test_add_todo_with_valid_text_tc_add_001(driver):
    """
    TC_ADD_001 - Add todo with valid text

    Preconditions:
    - Application is open
    - Add Todo page is displayed

    Steps:
    1. Click todo input
    2. Enter "Kitap oku"
    3. Press Enter

    Expected Result:
    - "Kitap oku" appears in the todo list
    """

    # Preconditions
    page = TodoPage(driver)
    page.open()

    # Steps
    page.add_todo("Kitap oku")

    # Expected Result (ASSERTION)
    todos = page.get_todo_texts()
    assert "Kitap oku" in todos


def test_empty_input_should_not_create_todo_tc_add_003(driver):
    """
    TC_ADD_003 - Empty input should not create a todo

    Preconditions:
    - Application is open
    - Add Todo page is displayed
    - Todo list is initially empty
    """

    page = TodoPage(driver)
    page.open()

    # (İstersen buraya başlangıçta todo olmadığını da assert edebilirsin)
    initial_count = page.get_todo_count()

    # Steps:
    # 1. Leave input empty
    # 2. Press Enter
    page.add_todo("")  # boş string

    # Expected Result:
    # - No new todo is added
    final_count = page.get_todo_count()
    assert final_count == initial_count

def test_whitespace_input_should_not_create_todo_tc_add_004(driver):
    """
    TC_ADD_004 - Whitespace-only input should not create a todo

    Preconditions:
    - Application is open
    - Add Todo page is displayed
    - Todo list is initially empty
    """

    page = TodoPage(driver)
    page.open()

    initial_count = page.get_todo_count()

    # Steps:
    # 1. Enter "   " (spaces)
    # 2. Press Enter
    page.add_todo("   ")

    # Expected Result:
    # - No new todo is added
    final_count = page.get_todo_count()
    assert final_count == initial_count

def test_todos_persist_after_refresh_tc_add_009(driver):
    """
    TC_ADD_009 - Todos should remain after page refresh

    Preconditions:
    - Application is open
    - At least one todo exists in the list

    Steps:
    1. Add a todo
    2. Refresh the page

    Expected Result:
    - The previously added todo is still visible in the list
    """

    page = TodoPage(driver)
    page.open()

    # En az bir todo ekle (Precondition'ı kodla sağlıyoruz)
    page.add_todo("Kitap oku")
    todos_before = page.get_todo_texts()
    assert "Kitap oku" in todos_before

    # Sayfayı yenile
    driver.refresh()

    # Beklenen sonuç: todo hâlâ listede
    todos_after = page.get_todo_texts()
    assert "Kitap oku" in todos_after
def test_add_todo_with_turkish_characters_tc_add_005(driver):
    page = TodoPage(driver)
    page.open()

    page.add_todo("Çalışma planı hazırlayacağım.")
    todos = page.get_todo_texts()
    assert "Çalışma planı hazırlayacağım." in todos

    driver.refresh()