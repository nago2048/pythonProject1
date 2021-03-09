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
    Then Verify that "Watchlist" link is visible in header
    Then Verify that " Brand Outlet" link is visible in header
    Then Change width to "1008"
    Then Verify that "Watchlist" link is not visible in header
    Then Verify that " Brand Outlet" link is not visible in header

  Scenario: Verify all navigation links
    Given Navigate to eBay
    Then Click on "Daily Deals" link in header
    Then Go back
    Then Click on "Sell" link in header
    Then Go back
    Then Click on "My eBay" link in header
    Then Go back
    Then Click on "Help & Contact" link in header
    Then Go back


  #--------------Item sorting-------------
  Scenario: Just sort shoes
    Given Navigate to eBay
    Then Type "Shoes" in search input
    Then Search by enter
    Then Filter results by "25% off $30+" and "Free shipping" and "Free returns" and print results
