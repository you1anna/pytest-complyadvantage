# Requirements:
1) Windows OS
2) Python 3.6.5+
3) Chrome version 72.0.3683.86

# UI Tests
1) Dependencies: PyTest-BDD, Selenium
2) The .feature file contains the scenario steps
3) The test is created using the Page Object Model pattern

# Steps
1) Run <go.bat> in \ui\ which will setup a virtualenv and run the test

# Expected results

\ui\tests\test_add_politician_form.py [FAIL]

Bugs:
- Able to submit same entry twice
- Full name is always set to John Doe
- John Doe is persisted to the db
- Fullname field is reset on saving
- UI is not responsive

# API Tests

1) Dependencies: PyTest, Requests
2) Tests use an API client class to manage http and json files for post requests

# Steps
1) Run <go.bat> in \api\ which will setup a virtualenv and run the test

# Expected results

\api\tests\test_peps_create_endpoint.py [PASS, FAIL, FAIL]

\api\tests\test_peps_read_by_id_endpoint.py [PASS]

\api\tests\test_peps_read_endpoint.py [FAIL]   

# Bugs
- 10 entries are returned instead of 5 on the GET
- Possible to submit invalid characters
- 201 returned when required params are missing

# Approach

I chose Python because of its versatility as a scripting language, with the benefits that debugging in Pycharm brings.
It also has good library support for testing. The fact that compilation is not necessary also enables easier 
integration into CI.

For the UI tests I chose a new plugin for Pytest called Pytest-BDD, because tests at the UI
layer reflect business logic, it can be useful to describe their behaviour at a high level, via
the .feature files. This proved extra work to manage, and frustratingly it was not possible to debug
these without the professional version of Pycharm, so I was forced to test them via the console. In terms of 
the framework, using Page Object Model enables cleaner code and tests to be decoupled from the object locators.
This also aids maintainability when scaling out to larger suites.

Given more time I would likely split out the driver fixture into a common module to allow other scenario to 
reuse it, and parametrise the browser fixture to enable testing across different browsers.

I chose not to use BDD on the API tests to speed debugging. While the tests are harder to read, there is
less business logic at stake and fewer code files are needed. 

Given more time I would utilise JsonPath to be able to manipulate json data per request, instead of relying
on a separate file per test case.

