// Mini E-Kart Shopping Cart JavaScript
// This file contains all the cart functionality and event handlers

// Global variables to store cart data
let cart = []; // Array to store cart items
let totalPrice = 0; // Total price of all items in cart

// DOM elements
const cartItemsContainer = document.getElementById('cart-items');
const emptyMessage = document.getElementById('empty-message');
const totalPriceElement = document.getElementById('total-price');
const addButtons = document.querySelectorAll('.add-btn');

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Mini E-Kart initialized successfully!');
    
    // Add event listeners to all "Add to Cart" buttons
    addButtons.forEach(button => {
        button.addEventListener('click', addToCart);
    });
    
    // Initialize cart display
    updateCartDisplay();
});

/**
 * Add a product to the shopping cart
 * @param {Event} event - The click event from the add button
 */
function addToCart(event) {
    // Get product information from the button's data attributes
    const productName = event.target.getAttribute('data-name');
    const productPrice = parseFloat(event.target.getAttribute('data-price'));
    
    console.log(`Adding ${productName} ($${productPrice}) to cart`);
    
    // Check if product already exists in cart
    const existingItem = cart.find(item => item.name === productName);
    
    if (existingItem) {
        // If product exists, increase quantity
        existingItem.quantity += 1;
        console.log(`Increased quantity of ${productName} to ${existingItem.quantity}`);
    } else {
        // If product doesn't exist, add new item to cart
        const newItem = {
            name: productName,
            price: productPrice,
            quantity: 1
        };
        cart.push(newItem);
        console.log(`Added new item: ${productName}`);
    }
    
    // Update the cart display and total
    updateCartDisplay();
    
    // Provide visual feedback to user
    showAddToCartFeedback(event.target);
}

/**
 * Remove a product from the shopping cart
 * @param {string} productName - Name of the product to remove
 */
function removeFromCart(productName) {
    console.log(`Removing ${productName} from cart`);
    
    // Find the item in cart
    const itemIndex = cart.findIndex(item => item.name === productName);
    
    if (itemIndex !== -1) {
        // Remove the item from cart array
        cart.splice(itemIndex, 1);
        console.log(`Removed ${productName} from cart`);
        
        // Update the cart display
        updateCartDisplay();
    }
}

/**
 * Update the cart display on the page
 * This function handles showing/hiding empty message and rendering cart items
 */
function updateCartDisplay() {
    // Calculate total price
    calculateTotalPrice();
    
    // Update total price display
    totalPriceElement.textContent = totalPrice.toFixed(2);
    
    // Clear the cart items container
    cartItemsContainer.innerHTML = '';
    
    if (cart.length === 0) {
        // Show empty message if cart is empty
        emptyMessage.style.display = 'block';
        console.log('Cart is empty - showing empty message');
    } else {
        // Hide empty message and show cart items
        emptyMessage.style.display = 'none';
        
        // Render each item in the cart
        cart.forEach(item => {
            const cartItemElement = createCartItemElement(item);
            cartItemsContainer.appendChild(cartItemElement);
        });
        
        console.log(`Displaying ${cart.length} items in cart`);
    }
}

/**
 * Create HTML element for a cart item
 * @param {Object} item - Cart item object with name, price, and quantity
 * @returns {HTMLElement} - The created cart item element
 */
function createCartItemElement(item) {
    // Create the main cart item container
    const cartItemDiv = document.createElement('div');
    cartItemDiv.className = 'cart-item';
    
    // Create item info section
    const itemInfoDiv = document.createElement('div');
    itemInfoDiv.className = 'cart-item-info';
    
    // Create item name element
    const nameElement = document.createElement('div');
    nameElement.className = 'cart-item-name';
    nameElement.textContent = item.name;
    
    // Create item price element
    const priceElement = document.createElement('div');
    priceElement.className = 'cart-item-price';
    priceElement.textContent = `$${item.price.toFixed(2)}`;
    
    // If quantity is more than 1, show quantity
    if (item.quantity > 1) {
        const quantityElement = document.createElement('div');
        quantityElement.className = 'cart-item-quantity';
        quantityElement.textContent = `Qty: ${item.quantity}`;
        quantityElement.style.fontSize = '0.9rem';
        quantityElement.style.color = '#7f8c8d';
        itemInfoDiv.appendChild(quantityElement);
    }
    
    // Create remove button
    const removeButton = document.createElement('button');
    removeButton.className = 'remove-btn';
    removeButton.textContent = 'Remove';
    removeButton.addEventListener('click', () => removeFromCart(item.name));
    
    // Assemble the cart item
    itemInfoDiv.appendChild(nameElement);
    itemInfoDiv.appendChild(priceElement);
    cartItemDiv.appendChild(itemInfoDiv);
    cartItemDiv.appendChild(removeButton);
    
    return cartItemDiv;
}

/**
 * Calculate the total price of all items in the cart
 */
function calculateTotalPrice() {
    totalPrice = 0;
    
    cart.forEach(item => {
        totalPrice += item.price * item.quantity;
    });
    
    console.log(`Total cart price: $${totalPrice.toFixed(2)}`);
}

/**
 * Provide visual feedback when adding item to cart
 * @param {HTMLElement} button - The add button that was clicked
 */
function showAddToCartFeedback(button) {
    // Store original text and style
    const originalText = button.textContent;
    const originalBackground = button.style.background;
    
    // Change button appearance temporarily
    button.textContent = 'Added!';
    button.style.background = '#27ae60';
    
    // Reset after 1 second
    setTimeout(() => {
        button.textContent = originalText;
        button.style.background = originalBackground;
    }, 1000);
}

/**
 * Utility function to get cart summary (for debugging or future features)
 * @returns {Object} - Cart summary with item count and total price
 */
function getCartSummary() {
    const itemCount = cart.reduce((total, item) => total + item.quantity, 0);
    
    return {
        itemCount: itemCount,
        totalPrice: totalPrice,
        items: cart
    };
}

/**
 * Clear the entire cart (utility function for future features)
 */
function clearCart() {
    cart = [];
    totalPrice = 0;
    updateCartDisplay();
    console.log('Cart cleared');
}

// Export functions for potential future use (if using modules)
// This allows the functions to be used in other scripts if needed
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        addToCart,
        removeFromCart,
        getCartSummary,
        clearCart
    };
}

