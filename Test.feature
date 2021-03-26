Feature: eBay Regression

  Background: Open eBay
    Given Navigate to eBay

  @search
  Scenario: Testing Search functionality (click)
    And Type "Dress" in search input
    And Search by click
    Then Verify that "Dress" in results

  @search
  Scenario: Testing Search functionality multiple pages
    And Type "Shoes" in search input
    And Search by click
    Then Verify that "Shoes" in results in 2 pages

  @search
  Scenario:  Testing Search functionality (enter)
    And Type "Dress" in search input
    And Search by enter
    Then Verify that "Dress" in results

  @search
  Scenario:  Testing Search functionality negative
    And Type "Dress" in search input
    And Search by enter
    Then Verify that "Fishing rod" not in results


  @navigation
  Scenario: Verify if all navigation elements present
    And Maximize window
    Then Hover all navigation elements

  @navigation
  Scenario: Verify that Watchlist link is not visible if window width less then 1009 px
    Then Change window size to "1009" x "800"
    Then Verify that "Watchlist" link is visible in header
    Then Verify that " Brand Outlet" link is visible in header
    Then Change window size to "1008" x "800"
    Then Verify that "Watchlist" link is not visible in header
    Then Verify that " Brand Outlet" link is not visible in header

  @navigation
  Scenario: Verify all navigation links
    Then Click on "Daily Deals" link in header
    Then Go back
    Then Click on "Sell" link in header
    Then Go back
    Then Click on "My eBay" link in header
    Then Go back
    Then Click on "Help & Contact" link in header
    Then Go back


  @filter
  Scenario: Just sort shoes
    Then Type "Shoes" in search input
    Then Search by enter
    Then Filter results by "25% off $30+" and "Free shipping" and "Free returns" and print results

  @filter
  Scenario: Verify that filter works
    And Type "Shoes" in search input
    And Search by click
    And filter by "New with tags" in "Condition" category

  @filter
  Scenario: Verify that filter works with multiple parameters
    And Type "Shoes" in search input
    And Search by click
    And filter by "adidas" in "Brand" category
    And filter by "New with tags" in "Condition" category
    And filter by "Comfort" in "Features" category

  @filter
  Scenario: Verify that filter works from table
    And Type "Shoes" in search input
    And Search by click
    And Apply following filters
    | Filter :  | value :       |
    | Brand     | adidas        |
    | Features  | Comfort       |
    | Condition | New with tags |

  @filter
  Scenario Outline: Verify that filter works with table outline
    And Type "<search_item>" in search input
    And Search by click
    And Apply following filters
    | Filter :       | value :             |
    | <filter_name1>  | <filter_value1>    |
    | <filter_name2>  | <filter_value2>    |
    | <filter_name3>  | <filter_value3>    |


    Examples:
    | search_item | filter_name1 | filter_value1 | filter_name2 | filter_value2 | filter_name3  | filter_value3  |
    |   shoes     |  Brand       | adidas        |   Features   |    Comfort    |  Condition    |  New with tags |
    |   dress     |  Brand       | Calvin Klein  | Dress Length |     Long      | Item Location |  US Only       |

  @other
    Scenario: Underline testing
      And I hover on element and check if it has css property underline
