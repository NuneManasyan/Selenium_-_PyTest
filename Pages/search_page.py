from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Helper_functions.helpers import Helper
import logging
from Test_data.data import existing_course, non_existing_course


class Search(Helper):
    search_box_loc = (By.XPATH, '//input[@name="q"]')
    course_search_result_loc = (By.XPATH, '//h3[@class="card__name"]')
    no_results_found_loc = (By.XPATH, '//p[@class="products__list-no-results"]')
    
    def search_an_existing_course(self):
        try:
            self.move_to_element(self.search_box_loc)
            query = self.find_and_send_keys(self.search_box_loc, existing_course, timeout=30)            
            query.send_keys(Keys.ENTER)            
            self.wait_for_element_in_dom(self.course_search_result_loc, timeout=100)
        except Exception as e:             
            logging.error(f"An error occurred while searching an existing course: {e}")
            self.make_screenshot("failed_search_existing_course_screen.png")

    def search_a_non_existing_course(self):
        try:
            clear_element = self.wait_for_element_in_dom(self.search_box_loc)
            clear_element.clear()
            logging.info("Search box was cleared.")
          
            query = self.find_and_send_keys(self.search_box_loc, non_existing_course, timeout=30)            
            query.send_keys(Keys.ENTER) 
            
            no_result = self.wait_until_element_visible(self.no_results_found_loc) 
            return no_result.text.strip()   

        except Exception as e:             
            logging.error(f"An error occurred while searching a non-existing course: {e}")
            self.make_screenshot("failed_search_a_non_existing_course_screen.png")

  