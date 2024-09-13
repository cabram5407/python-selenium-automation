# Created by cabram54 at 9/7/2024
Feature:  Cart functionality

  Scenario: User can see Cart Empty message
     Given Click on cart icon
     When Click on cart icon
     Then Verify Cart Empty message shown

  Scenario: Click sign-in button
     Given Click on sign-in button
     When From side navigation, click sign-in
     Then Verify sign-in button shown

  Scenario: Cart item present
      Given Search for {item}
      When Add item to cart
      When Click on cart icon
      Then Verify search results shown {item}