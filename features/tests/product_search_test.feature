# Created by cabram54 at 9/9/2024

Feature: Test for Target Search Functionality

#Target product search
Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results show coffee
    Then Verify product coffee in URL


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

#Target product in the cart test case
Scenario: User can add a product to cart
    Given Open target main page
    When Search for product
    And Click on cart icon
    And Add item to cart
    Then Verify search results show {item}

#Target Circle Test case
  Scenario: User can search for Target benefits
    Given Open Target Benefits page
    When Click on Target Benefits Tab
    Then Verify 10 benefit links

  #Product names and images present
  Scenario: Verify user can see product names and images
    Given Open Target main page
    When Search for AirPods (3rd Generation)
    Then Verify product has name and image


    Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown

  #Product colors present
  Scenario: User can see product colors
    Given Open Target product A-54551690 page
    Then Verify user can click through colors
