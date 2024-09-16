# Created by cabram54 at 9/9/2024

Feature: Test for Target Search Functionality

Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results show coffee


Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search results show tea


Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify search results show <search_word>
    Examples:
    |search_word  |
    |coffee       |
    |tea          |
    |mug          |
    |sugar        |


Scenario: User can verify sign-in form opened
    Given Open target main page
    When Click on sign-in button
    When Confirm Add to Cart - Side Navigation
    Then Verify sign-in form shown


Scenario: User can add a product to cart
    Given Open target main page
    When Search for product
    And Click on cart icon
    And Add item to cart
    And Confirm Add to Cart - Side Navigation
    Then Verify search results show {item}


  Scenario: User can search for Target benefits
    Given Open Target Benefits page
    When Click on Target Benefits Tab
    Then Verify 10 benefit links