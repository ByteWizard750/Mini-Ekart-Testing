Feature: Add to Cart
  As a customer
  I want to add products to my shopping cart
  So that I can purchase multiple items

  Background:
    Given the user is on the e-kart homepage
    And the cart is empty

  Scenario: Add one product to cart
    When the user clicks "Add to Cart" for one product
    Then the cart should display that product
    And the cart should contain 1 product
    And the total price should be correctly updated

  Scenario: Add specific product to cart
    When the user clicks "Add to Cart" for "Smartphone"
    Then the cart should display "Smartphone" with price $699.99
    And the cart should contain 1 product
    And the total price should be $699.99

  Scenario: Add multiple different products to cart
    When the user adds 3 products
    Then the cart should contain 3 products
    And the total price should be correctly updated

  Scenario: Add expensive product to cart
    When the user clicks "Add to Cart" for "Laptop"
    Then the cart should display "Laptop" with price $1299.99
    And the cart should contain 1 product
    And the total price should be $1299.99

  Scenario: Add affordable product to cart
    When the user clicks "Add to Cart" for "Headphones"
    Then the cart should display "Headphones" with price $199.99
    And the cart should contain 1 product
    And the total price should be $199.99

  Scenario: Add multiple same products to cart
    Given the cart contains 1 product
    When the user clicks "Add to Cart" for "Smartphone"
    Then the cart should contain 2 products
    And the total price should be correctly updated

  Scenario: Add all available products to cart
    When the user adds 6 products
    Then the cart should contain 6 products
    And the total price should be correctly updated

  Scenario: Add product and verify cart updates
    When the user clicks "Add to Cart" for "Tablet"
    Then the cart should display "Tablet" with price $499.99
    And the cart should not show "Your cart is empty"
    And the total price should be $499.99

