Feature: eBay Regression

  #---------Search-----------
  Scenario: Testing Search functionality (click)
    Given Navigate to eBay
    And Type "Dress" in search input
    And Search by click
    Then Verify that "Dress" in results


  Scenario:  Testing Search functionality (enter)
    Given Navigate to eBay
    And Type "Dress" in search input
    And Search by enter
    Then Verify that "Dress" in results


  Scenario:  Testing Search functionality negative
    Given Navigate to eBay
    And Type "Dress" in search input
    And Search by enter
    Then Verify that "Fishing rod" not in results

  #---------Navigation-----------
  Scenario: Verify if all navigation elements present
    Given Navigate to eBay
    Then Hover all navigation elements

  Scenario: Verify that Watchlist link is not visible if window width less then 1009 px
    Given Navigate to eBay
    Then Change width to "1009"
    Then Verify that Watchlist link is visible
    Then Change width to "1008"
    Then Verify that Watchlist link is not visible