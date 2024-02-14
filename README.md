# Selenium_-_Pytest
# Main test scenario:

1. Open Chrome browser, navigate to "https://courses.ultimateqa.com/collections", click "SIGN IN", go to the "Create a new account" page.
2. Create fake credentials and register.
3. Enter an existing course name ("selenium") in the "Search box" and validate that there are any results. 
4. Enter a non-existing course name ("millenium") in the "Search box"  and validate that "No results were found" message was displayed. 



# Test Cases:

## Pages
### home_page.py              - go_to_create_a_new_account -           


                              - alert_popup - clicks on the "Alert" button, switches to the popped up dialog box,
                                 writes pop-up text to the provided file
                              - hide_element - clicks on the "Hide" button, gets the value of the given attribute 
                                 and writes it to the provided file
                              - mouse_hover - moves to the "Mouse Hover" button, clicks on the "Top" option,
                                 which automatically scrolls up to the top of the page
                              - get_footer_text - navigates to the provided footer element and writes its text to the provided file
### login.py                  - sign_in - scrolls up to the top of the page, clicks on the "SIGN IN" button, enters provided invalid credentials,
                                 writes validation message text to the provided file                               
### google_search.py          - search_text - opens the provided URL, enters given query in the "Search box", gets text from results, 
                                 parses count of results and writes it to the provided file 

## Tests  
### test_runner.py            - includes necessary function calls, durations time of the project run

## common_functions.py        - set_up_logging: Configures the logging settings for the test framework.
                              - browser: Initializes the Chrome browser.
                              - navigate_to_url: Navigates to the given URL, maximizes the window, and handles page load timeouts.
                              - wait_for_element: Waits for an element until it is located using the provided value.
                              - wait_until_element_visible: Waits until the given element is visible.
                              - wait_until_element_clickable: Waits until the given element is clickable.
                              - move_to_element: Scrolls to the provided element on the page.
                              - write_to_file: Writes data to the "live_coding_text.txt" file.
                              - make_screenshot: Takes screenshots.
                              - close_browser: Quits the browser instance.
                              - delete_files: Deletes specified files after confirmation. 
## data.py                    - keeps data for the test
## my_config.py               - keeps url, quiry data                                                                                                                 
