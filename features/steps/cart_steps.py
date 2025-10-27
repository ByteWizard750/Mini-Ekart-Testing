import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def parse_price(price_text):
    match = re.search(r'\$?(\d+\.?\d*)', price_text)
    if match:
        return float(match.group(1))
    else:
        return 0.0

def get_product_price_by_name(driver, product_name):
    try:
        cards = driver.find_elements(By.CLASS_NAME, "product-card")
        for card in cards:
            name = card.find_element(By.CLASS_NAME, "product-name").text.strip()
            if name == product_name:
                price = card.find_element(By.CLASS_NAME, "product-price").text
                return parse_price(price)
        print(f"⚠️ Product {product_name} not found")
        return 0.0
    except Exception as e:
        print(f"❌ Error getting price for {product_name}: {e}")
        return 0.0

def get_cart_item_count(driver):
    try:
        items = driver.find_elements(By.CLASS_NAME, "cart-item")
        return len(items)
    except:
        return 0

def get_cart_total_price(driver):
    try:
        total = driver.find_element(By.ID, "total-price").text
        return parse_price(total)
    except Exception as e:
        print(f"Error reading total: {e}")
        return 0.0

def is_cart_empty(driver):
    try:
        msg = driver.find_element(By.ID, "empty-message")
        return msg.is_displayed()
    except:
        return False

@given('the user is on the e-kart homepage')
def step_user_on_homepage(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "products-grid"))
    )
    assert "Mini E-Kart" in context.driver.title
    print("✅ User is on homepage")

@given('the cart is empty')
def step_cart_is_empty(context):
    msg = context.driver.find_element(By.ID, "empty-message")
    assert msg.is_displayed()
    items = context.driver.find_elements(By.CLASS_NAME, "cart-item")
    assert len(items) == 0
    print("✅ Cart is empty")

@when('the user clicks "Add to Cart" for "{product_name}"')
def step_click_add_for_product(context, product_name):
    cards = context.driver.find_elements(By.CLASS_NAME, "product-card")
    found = False
    for c in cards:
        name = c.find_element(By.CLASS_NAME, "product-name").text.strip()
        if name == product_name:
            c.find_element(By.CLASS_NAME, "add-btn").click()
            print(f"✅ Added {product_name}")
            found = True
            time.sleep(1)
            break
    if not found:
        raise AssertionError(f"{product_name} not found to add")

@when('the user clicks "Remove" for "{product_name}"')
def step_click_remove(context, product_name):
    items = context.driver.find_elements(By.CLASS_NAME, "cart-item")
    ok = False
    for i in items:
        n = i.find_element(By.CLASS_NAME, "cart-item-name").text.strip()
        if n == product_name:
            i.find_element(By.CLASS_NAME, "remove-btn").click()
            print(f"✅ Removed {product_name}")
            time.sleep(1)
            ok = True
            break
    if not ok:
        raise AssertionError(f"{product_name} not found to remove")

@when('the user adds {count:d} products')
def step_add_multiple(context, count):
    btns = context.driver.find_elements(By.CLASS_NAME, "add-btn")
    if len(btns) < count:
        raise AssertionError("Not enough products")
    for i in range(count):
        btns[i].click()
        print(f"Added product {i+1}")
        time.sleep(0.5)

@then('the cart should display that product')
def step_cart_display(context):
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart-item"))
    )
    items = context.driver.find_elements(By.CLASS_NAME, "cart-item")
    assert len(items) > 0
    print("✅ Product shown in cart")

@then('the cart should be empty')
def step_cart_empty(context):
    msg = context.driver.find_element(By.ID, "empty-message")
    assert msg.is_displayed()
    items = context.driver.find_elements(By.CLASS_NAME, "cart-item")
    assert len(items) == 0
    print("✅ Cart empty")

@then('the total price should be correctly updated')
def step_total_correct(context):
    items = context.driver.find_elements(By.CLASS_NAME, "cart-item")
    exp_total = 0.0
    for i in items:
        price = i.find_element(By.CLASS_NAME, "cart-item-price").text
        exp_total += parse_price(price)
    total = context.driver.find_element(By.ID, "total-price").text
    act_total = parse_price(total)
    assert abs(exp_total - act_total) < 0.01, f"Expected {exp_total}, got {act_total}"
    print(f"✅ Total OK: ${act_total:.2f}")