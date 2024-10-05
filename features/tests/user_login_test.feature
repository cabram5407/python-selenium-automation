# Created by cabram54 at 10/4/2024
 Feature: User Signin Page Functions

  Scenario: User can open signin page
    Given User opens signin page
    When User enters incorrect email and password
    When Clicks login button
    Then Verify Cannot find account message shows