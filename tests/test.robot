*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:5000/

*** Test Cases ***
Test Addition
	Open Browser    ${URL}    Chrome
	Wait Until Element Is Visible    name=expression    timeout=10
	Input Text    name=expression    2+3
	Click Button    //button[@type='submit']
	Element Text Should Be    //h2    Wynik: 5
	Close Browser
Test Subtraction
	Open Browser    ${URL}    Chrome
	Wait Until Element Is Visible    name=expression    timeout=10
	Input Text    name=expression    5-2
	Click Button    //button[@type='submit']
	Element Text Should Be    //h2    Wynik: 3
	Close Browser
Test Multiplication
	[Documentation]
	Open Browser    ${URL}    Chrome
	Wait Until Element Is Visible    name=expression    timeout=10
	Input Text    name=expression    3*4
	Click Button    //button[@type='submit']
	Element Text Should Be   //h2   Wynik: 12
	[Teardown]     Close Browser
Test Division
	[Documentation]
	Open Browser   ${URL}   Chrome
	Wait Until Element Is Visible   name=expression   timeout=10
	Input Text   name=expression   10/2
	Click Button   //button[@type='submit']
	Element Text Should Be   //h2   Wynik: 5
	[Teardown]   Close Browser
Test Invalid Expression
	[Documentation]
	Open Browser   ${URL}   Chrome
	Wait Until Element Is Visible   name=expression   timeout=10
	Input Text   name=expression   2/
	Click Button   //button[@type='submit']
	Element Text Should Be   //h2   Błąd: Invalid expression.
	[Teardown]   Close Browser
