from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
usernameStr = ''
passwordStr = ''
searchStr = 'app'
smcLink = 'https://my301056.s4hana.ondemand.com/ui?saml2=enabled&sap-language=EN#Shell-home'
templateStr = 'interactions: create interactions with google big'
exactActions = 'BigQuery-AddToCart-Massive\nBigQuery-ProductViewed-Massive\nBigQuery-RemoveFromCart-Massive'

f = open("inputDates.txt", "r")
for i ,tempdate in enumerate(f):
    while True:
        try:
            print(i)
            date = tempdate.replace('\n','')
            print(date)
            browser = webdriver.Chrome()
            browser.get(smcLink)
            browser.maximize_window()
            time.sleep(5)
            print(i, 'Abrió la sesión')
            username = browser.find_element_by_id('j_username')
            username.send_keys(usernameStr)
            time.sleep(5)
            password = browser.find_element_by_id('j_password')
            password.send_keys(passwordStr)
            logOnButton = browser.find_element_by_id('logOnFormSubmit')
            logOnButton.click()
            time.sleep(20)
            print(i, 'Login succesfull')
            searchButton = browser.find_element_by_id('sf')
            searchButton.click()
            print(i, 'Presióno busqueda')
            time.sleep(5)
            searchBar = browser.find_element_by_id('searchFieldInShell-input-inner')
            searchBar.send_keys(searchStr)
            time.sleep(5)
            appBar = browser.find_element_by_class_name('sapMLIBContent')
            appBar.click()
            time.sleep(5)
            print(i, 'Entró a app job')
            plusButton = browser.find_element_by_id(
                'application-ApplicationJob-show-component---JobRunList--appJobsOverviewAddJobButton-inner')
            plusButton.click()
            time.sleep(5)
            print(i, 'Presiono nuevo job')
            dropDown = browser.find_element_by_id(
                'application-ApplicationJob-show-component---JobRunCreate--jobTemplateSelection-vhi')
            dropDown.click()
            time.sleep(5)
            print(i, 'Presióno template')
            templateSelectionTextBox = browser.find_element_by_id('idTemplateValueHelpDialog-searchField-I')
            templateSelectionTextBox.clear()
            templateSelectionTextBox.send_keys(templateStr)
            time.sleep(5)
            correctTemplate = browser.find_element_by_class_name('sapMLIB')
            correctTemplate.click()
            time.sleep(5)
            print(i, 'Selecciono el template')
            recurrencePatternLink = browser.find_element_by_id(
                'application-ApplicationJob-show-component---JobRunCreate--linkAddEditSchedulingOptions')
            recurrencePatternLink.click()
            time.sleep(5)
            print(i, 'Selecciono Temporalidad')
            recurrencePattern = browser.find_element_by_class_name('sapMSltArrow')
            recurrencePattern.click()
            time.sleep(5)
            action = webdriver.common.action_chains.ActionChains(browser)
            action.move_to_element_with_offset(recurrencePattern, -100, 40)
            action.click()
            action.perform()
            time.sleep(5)
            print(i, 'Presiono Single run')
            okButton = browser.find_element_by_id('recurrenceFragment--btnRecurrenceOK-inner')
            okButton.click()
            time.sleep(5)
            print(i, 'Presiono OK')
            queryConfiguration = browser.find_element_by_id('__input5-inner')
            queryConfiguration.send_keys(exactActions)
            print(i, 'Ingresar jobs names')
            time.sleep(5)
            startDate = browser.find_element_by_id('__input6-inner')
            startDate.clear()
            startDate.send_keys(date)
            endDate = browser.find_element_by_id('__input7-inner')
            endDate.clear()
            endDate.send_keys(date)
            time.sleep(5)
            buttons = browser.find_elements_by_class_name('sapMRbBInn')
            buttons[1].click()
            time.sleep(5)
            print(i, 'Presiono productive mode')
            scheduleButton = browser.find_element_by_id(
                'application-ApplicationJob-show-component---JobRunCreate--scheduleButton-inner')
            scheduleButton.click()
            time.sleep(10)
            print(i, 'Presiono schedule')
            browser.quit()
            break
        except Exception:  # Replace Exception with something more specific.
            browser.quit()
            print('Error: ', date)
            continue

print('Termino')