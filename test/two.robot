*** Settings ***
Documentation    Test for Calculator Application
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:8501
${BROWSER}    Chrome
${INPUT_FIELD}    xpath=//input

*** Test Cases ***
Open Calculator
    [Documentation]    otwiera strone aplikacji i sprawdza dzialanie
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Page Contains    Calculator by Tomasz Burnejko    timeout=10s
    Wait Until Page Contains    Wprowadź równanie:    timeout=10s
    Close Browser

Use Calculator One
    [Documentation]    dodawanie
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    ${INPUT_FIELD}    timeout=10s
    Input Text    ${INPUT_FIELD}    2+2
    Press Keys    ${INPUT_FIELD}    ENTER
    Wait Until Page Contains    4    timeout=10s
    Close Browser

Use Calculator Two
    [Documentation]    mnozenie
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    ${INPUT_FIELD}    timeout=10s
    Input Text    ${INPUT_FIELD}    3*3
    Press Keys    ${INPUT_FIELD}    ENTER
    Wait Until Page Contains    9    timeout=10s
    Close Browser

Use Calculator Three
    [Documentation]    odejmowanie
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    ${INPUT_FIELD}    timeout=10s
    Input Text    ${INPUT_FIELD}    5-3
    Press Keys    ${INPUT_FIELD}    ENTER
    Wait Until Page Contains    2    timeout=10s
    Close Browser

Use Calculator Four
    [Documentation]    dzielenie
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    ${INPUT_FIELD}    timeout=10s
    Input Text    ${INPUT_FIELD}    10/2
    Press Keys    ${INPUT_FIELD}    ENTER
    Wait Until Page Contains    5    timeout=10s
    Close Browser

Use Calculator Five
    [Documentation]    zlozone obliczenia
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    ${INPUT_FIELD}    timeout=10s
    Input Text   ${INPUT_FIELD}    (2+3)*4-5/5
    Press Keys   ${INPUT_FIELD}    ENTER
    Wait Until Page Contains    19    timeout=10s
    Close Browser

*** Keywords ***
Close Browser
    [Documentation]    zamyka przegladarke po zakonczeniu testow
    Close All Browsers
