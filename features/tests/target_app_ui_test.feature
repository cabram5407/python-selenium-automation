# Created by cabram54 at 9/23/2024
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window

   Scenario: User can open and close Terms and Conditions from Sign-in page
    Given Open Sign-in Page
    And Store original window
    When Click Target Terms and Conditions link
    And Switch to new window
    Then Verify Terms and Conditions page opened
    And Close current page
    And Return to original window