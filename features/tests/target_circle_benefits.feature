Feature: Target Benefits

  Scenario: User can search for Target benefits
    Given Open Target Benefits page
    When Input {search_word} into search field
    When Click on search icon
    Then Verify 10 benefit links