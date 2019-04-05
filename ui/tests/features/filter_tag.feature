Feature: New Entity

  Scenario: Add an entity to the database
    Given I visit the new entity page
    When I add details for "John Becrow"
    Then "John Becrow" should be added to the list
