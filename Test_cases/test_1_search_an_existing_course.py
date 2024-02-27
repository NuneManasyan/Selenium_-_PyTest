from Helper_functions.helpers import Helper
from Pages.home_page import HomePage
from Pages.register_page import Register
from Pages.search_page import Search
import my_config
import logging




def test_search_an_existing_course(driver):
    
    logging.info("'Test_1' was initiated.")
    helper_obj = Helper(driver)
    helper_obj.open_url(my_config.url) 

    home_page_obj = HomePage(driver)
    home_page_obj.go_to_create_a_new_account()

    register_obj = Register(driver)   
    register_obj.save_fake_credentials_in_json()
    register_obj.registration()
    register_obj.find_user_credentials_in_homepage()
      
    search_obj = Search(driver)
    existing_course_search_result = search_obj.search_an_existing_course()

    assert len(existing_course_search_result) > 0 , "No existing courses were found in the search results."
    if existing_course_search_result:
        logging.info("Existing courses were displayed.")
    else:
        logging.error("No existing courses were found in the search results.")

    logging.info("Test_1 was finished.")

    
   

