from selenium import webdriver
import pytest
import logging
import os


@pytest.fixture(scope="session")
def driver():
    try:   # TODO, add logging
        driver = webdriver.Chrome()
        logging.info("'Chrome' browser was opened.")
        driver.maximize_window()      
        logging.info("Browser window was maximized.")  
        yield driver
        driver.quit()
        logging.info("'Chrome' browser was closed.")
        
    except Exception as error:
        logging.error(f"An error occurred: {str(error)}")
        raise Exception(error)

def pytest_configure():
    logging.basicConfig (
                        level=logging.INFO,
                        filename = os.path.join(os.path.dirname(__file__), "logs.log"),
                        format="%(asctime)s [%(levelname)s] %(message)s ",
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filemode='a',    
                        encoding='utf-8'                   
                        )  


