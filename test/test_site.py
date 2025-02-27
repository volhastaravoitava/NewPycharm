import pytest
import time
from pages.homepage import HomePage
from pages.categorypage import CategoryPage
from pages.productpage import ProductPage



def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open_homepage()
    homepage.click_galaxy_s6()
    productpage = ProductPage(driver)
    productpage.check_title_is('Samsung galaxy s6')

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open_homepage()
    homepage.click_monitor()
    categorypage = CategoryPage(driver)
    time.sleep(3)
    categorypage.check_monitors_count(2)
