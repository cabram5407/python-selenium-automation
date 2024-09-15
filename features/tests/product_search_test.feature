# Created by cabram54 at 9/9/2024

Feature: Test for Target Search Functionality

Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results show tea

  Scenario: User can search for a product2
    Given Open target main page
    When Search for coffee
    Then Verify search results show coffee

Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results shown for <search_result>
    Examples:
    |search_word  |search_result |
    |coffee       |coffee        |
    |tea          |tea           |
    |mug          |mug           |
    |sugar        |sugar         |


    Scenario: User can verify sign-in form opened
    Given Open target main page
    When Click on sign-in button
    When From side navigation, click sign-in
    Then Verify sign-in form shown
