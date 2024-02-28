# Selenium_-_PyTest
# Main test scenario:

1. Open the Chrome browser, navigate to "https://courses.ultimateqa.com/collections", click "SIGN IN", go to the 
   "Create a new account" page.
2. Create fake credentials and register.
3. Enter an existing course name ("selenium") in the "Search box" and validate that there are any results. 
4. Enter a non-existing course name ("millenium") in the "Search box"  and validate that "No results were found" message was displayed. 


## Pages
### home_page.py              
                              - go_to_create_a_new_account: Clicks on the "Sign In" button and navigates the user to 
                                'Create a new account'page for registration.         
### register_page.py          
                              - save_fake_credentials_in_json: Saves fake credentials in "cred.json" file, which were originated in 
                                "data.py" file .
                              - registration: Registers the user with credentials taken from "data.py" file.
                              - find_user_credentials_in_homepage: Ensures that user credentials are displayed on the homepage after
                                successful register.
### search_page.py            
                              - search_an_existing_course: Navigates to the search box and enters the "existing course" query.
                              - search_a_non_existing_course: Navigates to the search box and enters the "non_existing course" query.

## Helper_functions
### helpers.py                
                              - open_url: Opens the browser, having the URL.
                              - wait_for_element_in_dom: Waits for an element until it is located using the provided value.
                              - wait_until_element_visible: Waits until the given element is visible.
                              - find_element_and_click: Finds an element and clicks on it.
                              - find_element_by_id: Finds an element by ID.
                              - move_to_element: Scrolls to the provided element on the page.
                              - find_and_send_keys: Finds an element and enters a query.
                              - make_screenshot: Takes screenshots.
                              - write_to_json: Writes given data to the provided JSON file.
                              - read_from_json: Reads data from the given JSON file.

## Test_data
### data.py
                              - Creates fake credentials for register, keeps necessary queries.

## my_config.py               
                              - Keeps the URL, JSON file name and JSON file path.   

## conftest.py               
                              - driver: Opens the "Chrome" browser, maximizes the window and closes it after
                                the session.
                              - pytest_configure: Configures logging.          
                              
## Test Cases:
### test_1_search_an_existing_course.py
                             - The script is designed to perform a search for an existing course on a web application. 
                               The test involves the following steps:

                              1. Navigate to the Home Page:
                                 Opens the specified URL.
                                 Clicks on the link to create a new account on the home page.

                              2. Register a New Account:
                                 Fills in registration details with fake credentials.
                                 Saves the fake credentials in a JSON file.
                                 Completes the registration process.

                              3. Search for an Existing Course:
                                 Performs a search for an existing course using the search functionality.
                                 Captures the search results.

                              4. Assertion:
                                 Asserts that there is at least one existing course in the search results.

### test_2_search_a_non_existing_course.py
                              - The script is designed to perform a search for a non-existing course on a web application. 
                                The test involves the following steps:

                              1. Search for an Non-existing Course:
                                 Performs a search for a non-existing course using the search functionality.
                                 Captures the search results.

                              2. Assertion:
                                 Asserts that the search result is "No results were found."


## requirements.txt           
                              - includes required libraries for running the project
                                                                                                               
