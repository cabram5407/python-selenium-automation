# Created by cabram54 at 9/9/2024
Scenario Outline: User can search for a product
    Given Open target main page
    When Search for {item}
    Then Verify header is shown

Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results shown for <search_result>
    Examples:
    |search_word  |search_result |
    |coffee       |coffee        |
    |tea          |tea           |
    |mug          |mug           |
    |sugar        |sugar         |


