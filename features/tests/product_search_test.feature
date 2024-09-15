# Created by cabram54 at 9/9/2024

Feature: Test for Target Search Functionality

Scenario: User can search for a product
    Given Open target main page
    When Search for {item}
    When Click search button
    Then 'Verify search results show item'

  Scenario: User can search for a product2
    Given Open target main page
    When Search for {item}
    Then 'Verify search results show item'

Scenario Outline: User can search for product
    Given Open target main page
    When Search for <item>
    Then Verify correct search results shown for <search_result>
    Examples:
    |item         |search_result |
    |coffee       |coffee        |
    |tea          |tea           |
    |mug          |mug           |
    |sugar        |sugar         |


Scenario: User can verify sign-in form opened
    Given Open target main page
    When Click on sign-in button
    When From side navigation, click sign-in
    Then Verify sign-in form shown
