# Created by cabram54 at 9/7/2024
Feature:Test Target Cart is Empty

  Scenario: User can confirm that cart is empty
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty