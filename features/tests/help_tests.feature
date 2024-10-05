# Created by cabram54 at 10/4/2024
Feature: Tests for HelpPages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened


  Scenario: User can select Help topic About Target Circle
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened


  Scenario: User can select Help topic Technical Support
    Given Open Help topic for Technical Support
    Then Verify help Technical Support page opened



