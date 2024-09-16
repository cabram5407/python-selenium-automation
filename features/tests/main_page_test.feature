# Created by cabram54 at 9/8/2024
Feature: Tests for main page user interface (UI)
  #Verify header is shown
  #Given Open Target main page
  #Then verify header is shown


  Scenario: Verify user can navigate to sign-in
  #not common better to count links
    Given Open Target main page
    When Click on sign-in button
    When From side navigation, click sign-in
    Then Verify sign-in form shown


 Scenario: Verify Target header shown
  #not common better to count links
    Given Open Target main page
    Then Verify header is shown


  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 6 links


   Scenario: Verify you've captured the correct amount links
    Given Open target benefits page
    Then Verify 10 benefit links
