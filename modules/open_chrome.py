'''
Author:     Bhanudeep Simhadri
LinkedIn:   https://www.linkedin.com/in/bhanudeepsimhadri/

Copyright (C) 2024 Bhanudeep Simhadri

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/Bhanudeep/Auto-LinkedIn-job-applier

'''
import os
cwd=os.getcwd()
from setup.config import run_in_background, undetected_mode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from modules.helpers import find_default_profile_directory, critical_error_log, print_lg

try:
    ch_options = webdriver.ChromeOptions()
    ch_options.binary_location=cwd+"\\chrome-win64\\chrome.exe"
    driver_path=cwd+"\\chromedriver-win64\\chromedriver.exe"
    service_option = webdriver.ChromeService(executable_path=driver_path) #, service=Service(executable_path="C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"))
    driver= webdriver.Chrome(options=ch_options, service=service_option)
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
except Exception as e:
    msg = "Seems like Google Chrome browser is already running or Chrome-driver is out dated. Close Chrome and run windows-setup.bat for windows or try your luck with setup.sh or update the Chrome-driver and then run this program! If error occurred when using undetected_mode uninstall and install undetected-chromedriver. (Open  terminal and use commands 'pip uninstall undetected-chromedriver' and 'pip install undetected-chromedriver' respectively.)"
    if isinstance(e,TimeoutError): msg = "Couldn't download Chrome-driver. Set undetected_mode = False in config!"
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    from pyautogui import alert
    alert(msg, "Error in opening chrome")
    try: driver.quit()
    except NameError: exit()
    
