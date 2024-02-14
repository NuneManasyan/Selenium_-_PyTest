from Helper_functions.helpers import Helper
from Pages.home_page import HomePage
from Pages.register_page import Register
from Pages.search_page import Search
import my_config
import logging
from Test_data.data import non_existing_course



def test_search_a_non_existing_course(driver):    
    logging.info("'Test_2' was initiated.")

    # helper_obj = Helper(driver)
    # helper_obj.open_url(my_config.url) 

    # home_page_obj = HomePage(driver)
    # home_page_obj.go_to_create_a_new_account()

    # register_obj = Register(driver)   
    # register_obj.save_fake_credentials_in_json()
    # register_obj.registration()
    # register_obj.find_user_credentials_in_homepage()

    
    search_obj = Search(driver)    
    search_result = search_obj.search_a_non_existing_course()
    
    assert search_result == "No results were found"
    logging.info(f"No courses were found with '{non_existing_course}' key.")

    logging.info("Test_2 was finished.")