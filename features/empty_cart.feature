Feature: Empty Cart Display
  As a customer
  I want to see appropriate messages when my cart is empty
  So that I understand the current state of my cart

  Background:
    Given the user is on the e-kart homepage

  Scenario: Display empty cart message initially
    Given the cart is empty
    Then the cart should show "Your cart is empty"
    And the cart should be empty
    And the total price should be $0.00

  Scenario: Show empty message after removing all items
    Given the cart contains 1 product
    When the user clicks "Remove" for one product
    Then the cart should show "Your cart is empty"
    And the cart should be empty

  Scenario: Hide empty message when adding product
    Given the cart is empty
    When the user clicks "Add to Cart" for one product
    Then the cart should not show "Your cart is empty"
    And the cart should contain 1 product

  Scenario: Show empty message after clearing cart
    Given the cart contains 3 products
    When the user removes all products
    Then the cart should show "Your cart is empty"
    And the cart should be empty
    And the total price should be $0.00

  Scenario: Verify empty cart state persistence
    Given the cart is empty
    When the user navigates to homepage
    Then the cart should remain empty
    And the cart should show "Your cart is empty"

  Scenario: Empty cart after removing specific product
    Given the cart contains a "Smartphone"
    When the user clicks "Remove" for "Smartphone"
    Then the cart should show "Your cart is empty"
    And the cart should be empty

  Scenario: Empty cart message visibility
    Given the cart is empty
    Then the empty message should be visible
    And no cart items should be displayed
    And the total price should be $0.00

  Scenario: Empty cart after multiple operations
    Given the cart contains 2 products
    When the user clicks "Remove" for one product
    And the user clicks "Remove" for one product
    Then the cart should show "Your cart is empty"
    And the cart should be empty

  Scenario: Empty cart state verification
    Given the cart is empty
    Then the cart should contain 0 products
    And the cart should show "Your cart is empty"
    And the total price should be $0.00
    And no remove buttons should be visible

