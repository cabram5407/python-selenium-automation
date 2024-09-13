# Created by cabram54 at 9/7/2024
Feature:Test Target Cart is Empty

  Scenario: User can see Cart empty message
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty


    Scenario: User can verify sign-in form opened
    Given Open target main page
    When Click on sign-in button
    When From side navigation, click sign-in
    Then Verify ign-in form opened