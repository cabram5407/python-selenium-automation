# Created by cabram54 at 9/7/2024
Feature:  Cart empty tests

  Scenario: User can see Cart Empty message
     Given Click on cart icon
     When Click on cart icon
     Then Verify Cart Empty message shown

    Scenario: Click sign-in button
     Given Click on sign-in button
     When From side navigation, click sign-in
     Then Verify sign-in button shown