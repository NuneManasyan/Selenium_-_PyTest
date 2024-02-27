from Pages.search_page import Search
import logging
from Test_data.data import non_existing_course



def test_search_a_non_existing_course(driver):    
    logging.info("'Test_2' was initiated.")
   
    search_obj = Search(driver)    
    search_result = search_obj.search_a_non_existing_course()
    
    assert search_result == "No results were found"
    logging.info(f"No courses were found with '{non_existing_course}' key.")

    logging.info("Test_2 was finished.")