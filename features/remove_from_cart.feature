Feature: Remove from Cart
  As a customer
  I want to remove products from my shopping cart
  So that I can change my mind about purchases

  Background:
    Given the user is on the e-kart homepage

  Scenario: Remove one product from cart
    Given the cart contains 1 product
    When the user clicks "Remove" for one product
    Then the cart should be empty
    And the cart should show "Your cart is empty"

  Scenario: Remove specific product from cart
    Given the cart contains a "Smartphone"
    When the user clicks "Remove" for "Smartphone"
    Then the "Smartphone" should be removed from the cart
    And the cart should be empty

  Scenario: Remove product from multiple items cart
    Given the cart contains 3 products
    When the user clicks "Remove" for one product
    Then the cart should contain 2 products
    And the total price should be correctly updated

  Scenario: Remove expensive product from cart
    Given the cart contains a "Laptop"
    When the user clicks "Remove" for "Laptop"
    Then the "Laptop" should be removed from the cart
    And the cart should be empty
    And the total price should be $0.00

  Scenario: Remove all products from cart
    Given the cart contains 5 products
    When the user removes all products
    Then the cart should be empty
    And the cart should show "Your cart is empty"
    And the total price should be $0.00

  Scenario: Remove product and verify cart updates
    Given the cart contains a "Headphones"
    When the user clicks "Remove" for "Headphones"
    Then the cart should be empty
    And the cart should not contain any products
    And the total price should be $0.00

  Scenario: Remove from empty cart
    Given the cart is empty
    When the user tries to remove a product
    Then the cart should remain empty
    And the cart should show "Your cart is empty"

  Scenario: Remove multiple products sequentially
    Given the cart contains 4 products
    When the user clicks "Remove" for one product
    And the user clicks "Remove" for one product
    Then the cart should contain 2 products
    And the total price should be correctly updated

