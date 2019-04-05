
What test cases would you write based on this screenshot and the information above?
> - Verify that non-alpha numeric characters are not accepted
> - Ensure null values are not accepted
> - Ensure the system does not accept entry of control characters
> - Verify it is not possible to enter the same card number twice
> - Ensure money cannot be added before the card number is entered
> - Ensure negative values are not accepted

What types of testing would you think about conducting against this screen?
> - UI testing - ensure the form continues to look and behave correctly and is responsive across different browsers 
and mobile devices, if these are supported. It may make sense to add a Selenium test to run as coverage for regression.
> - If the app uses an API to pass information to the domain, it may be appropriate to ensure a degree of API 
test coverage, since these tests would provide faster feedback than a UI test, while being cheaper to maintain.
> - Security testing - assuming the BE is running SQL, attempting to SQL inject the fields could mitigate risk of an
attacker trying to retrieve any sensitive information. The page could also be vulnerable to cross site scripting

Is there anything in the screen that you think could be improved?
> - Lookup a card number based on the users credentials. This would avoid human error associated with manual entry
> - Validate number against the name, and do not allow inva lid combinations to make it past the UI/API.
> - By the design there seems to be a risk of a user accidentally activating credit on someone else's card
> - Ideally the process in general would be more automated to remove the need for manual intervention. If balance
is available to spend, the process of activating this against a users card should happen on the back end, and perhaps 
just require the user to acknowledge it by clicking a button in an email.

What else would you be interested to test?
> - Performance of the system when put under load of many users activating credit simultaneously. How is transactional
consistency affected if some of the calls to the db fail or timeout? Are error cases handled correctly at the API 
and UI layers? In the worst case scenario it could result in data loss or corruption.