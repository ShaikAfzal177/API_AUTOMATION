Feature: Happy test flow of saucedemo

  Scenario: User Login
    Given the user is on the saucedemo login page
    When the user logs in with "standard_user" and "secret_sauce"
    Then the user land on the products page

  Scenario: Select one product from multiple products
    Given the user land on the products page
    When Add to cart "Sauce Labs Bolt T-Shirt" from  all product list
    Then validate cart item "Sauce Labs Bolt T-Shirt"

  Scenario:Order the product from cart
    Given click check out button
    When fill the userdetails "afzal" "shaik" "516156" and click continue and finish button
    Then show the order placed message