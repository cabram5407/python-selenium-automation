# Created by cabram54 at 9/8/2024
Feature: Tests for main page user interface (UI)
  #Verify header is shown
  #Given Open Target main page
  #Then verify header is shown

 Scenario: Verify Target header shown
  #not common better to count links
    Given Open Target main page
    Then Verify header is shown
    And Verify header has links


  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 6 links
