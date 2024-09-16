# Created by cabram54 at 9/7/2024
Feature:  Cart functionality

  Scenario: User can see Cart Empty message
     Given Open target main page
     When Click on cart icon
     Then Verify Cart Empty message shown


  Scenario: Cart item present
      Given Search for {item}
      When Add item to cart
      When Click on cart icon
      Then Verify search results show {item}