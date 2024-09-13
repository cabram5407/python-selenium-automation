Feature: Test Scenarios for Search functionality

  Scenario: User can search for Target benefits
    Given Open Target Benefits page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown