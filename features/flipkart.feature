Feature: Flipkart Product Search

  Scenario: Extract and create product from search result
    Given the user opens the Flipkart homepage
    When the user searches for a product "apple 16 pro max"
    And the user clicks on the 3rd product in the search results
    Then the product name, price, and description should be displayed
    And the product should be created via API
    And the created product should be deleted
