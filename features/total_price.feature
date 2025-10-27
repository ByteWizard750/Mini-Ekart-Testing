Feature: Total Price Calculation
  As a customer
  I want to see the correct total price for my cart
  So that I know how much I will pay

  Background:
    Given the user is on the e-kart homepage
    And the cart is empty

  Scenario: Calculate total for single product
    When the user clicks "Add to Cart" for "Smartphone"
    Then the total price should be $699.99

  Scenario: Calculate total for multiple different products
    When the user clicks "Add to Cart" for "Smartphone"
    And the user clicks "Add to Cart" for "Laptop"
    Then the total price should be $1999.98

  Scenario: Calculate total for three products
    When the user clicks "Add to Cart" for "Headphones"
    And the user clicks "Add to Cart" for "Tablet"
    And the user clicks "Add to Cart" for "Smart Watch"
    Then the total price should be $999.97

  Scenario: Calculate total after removing product
    Given the cart contains 2 products
    When the user clicks "Remove" for one product
    Then the total price should be correctly updated

  Scenario: Calculate total for expensive products
    When the user clicks "Add to Cart" for "Laptop"
    And the user clicks "Add to Cart" for "Camera"
    Then the total price should be $2199.98

  Scenario: Calculate total for affordable products
    When the user clicks "Add to Cart" for "Headphones"
    And the user clicks "Add to Cart" for "Smart Watch"
    Then the total price should be $499.98

  Scenario: Calculate total for mixed price range
    When the user clicks "Add to Cart" for "Smartphone"
    And the user clicks "Add to Cart" for "Headphones"
    And the user clicks "Add to Cart" for "Tablet"
    Then the total price should be $1399.97

  Scenario: Calculate total for all products
    When the user adds 6 products
    Then the total price should be correctly updated
    And the total price should be greater than $0

  Scenario: Calculate total after clearing cart
    Given the cart contains 3 products
    When the user removes all products
    Then the total price should be $0.00

  Scenario: Verify total price accuracy
    When the user clicks "Add to Cart" for "Smartphone"
    And the user clicks "Add to Cart" for "Laptop"
    And the user clicks "Add to Cart" for "Headphones"
    Then the total price should be correctly updated
    And the total price should be $2199.97

