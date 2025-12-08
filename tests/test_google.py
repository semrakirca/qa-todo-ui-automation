from selenium.webdriver.common.by import By

def test_google_search_box_visible(driver):
    # 1) Google'a git
    driver.get("https://www.google.com")

    # 2) Arama kutusunu bul
    search_box = driver.find_element(By.NAME, "q")

    # 3) Görünüyor mu kontrol et
    assert search_box.is_displayed()
