Feature: Product API Crud

  Scenario: Create new product
    Given I have given payload type "generate-create"
    When  I Send a request to create the product
    Then The product should be created successfully

  Scenario: Get all products
    When I request all products
    Then I Should recieve list of products

  Scenario: Get product by product_id
    Given I have given payload type "generate-create"
    When  I Send a request to create the product
    And I Send a request to get the product
    Then The product should be fetched successfully

  Scenario: Update product
    Given I have given payload type "generate-create"
    When  I Send a request to create the product
    And  Update the product with new details
    Then The product should be updated successfully

  Scenario:Delete the product
    Given I have given payload type "generate-create"
    When  I Send a request to create the product
    And Send a request to Delete the product
    Then The product should be deleted successfully