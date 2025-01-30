*** Settings ***
Documentation  Simple Test
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
Open Calculator
    Open Browser  http://localhost:8501  Chrome
    Wait Until Page Contains    Calculator by Tomasz Burnejko
    Page Should Contain         Wprowadź równanie:

Use Calculator One
    Open Browser  http://localhost:8501  Chrome
    Wait Until Page Contains    Calculator by Tomasz Burnejko
    Input Text  id:text_input_1  2+2
    Press Keys  id:text_input_1  ENTER
    Wait Until Page Contains    4

Use Calculator Two
    Open Browser  http://localhost:8501  Chrome
    Wait Until Page Contains    Calculator by Tomasz Burnejko
    Input Text  id:text_input_1  3*3
    Press Keys  id:text_input_1  ENTER
    Wait Until Page Contains    9
