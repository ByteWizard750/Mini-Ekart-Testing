# Mini E-Kart Testing Framework

A comprehensive automated testing framework for the Mini E-Kart web application using **Selenium WebDriver** and **Cucumber (Behave)** in Python.

## 🎯 Overview

This testing framework provides:
- **25+ test scenarios** across 4 feature files
- **Selenium WebDriver** automation with Chrome browser
- **Cucumber/Behave** BDD scenarios for readable test cases
- **Comprehensive reporting** with statistics and summaries
- **Responsive testing** for cart functionality

## 📁 Project Structure

```
Mini E-Kart/
├── index.html              # Main web application
├── style.css               # Application styles
├── script.js               # Application JavaScript
├── requirements.txt         # Python dependencies
├── run_tests.py            # Main test execution script
├── features/               # Cucumber feature files
│   ├── add_to_cart.feature
│   ├── remove_from_cart.feature
│   ├── total_price.feature
│   ├── empty_cart.feature
│   └── steps/
│       └── cart_steps.py   # Step definitions
├── utilities/              # Test utilities
│   └── driver_setup.py     # WebDriver configuration
└── reports/                # Test reports and results
    └── test_summary.py     # Summary generator
```

## 🚀 Quick Start

### Prerequisites

1. **Python 3.7+** installed
2. **Chrome browser** installed
3. **ChromeDriver** (automatically managed by webdriver-manager)

### Installation & Execution

1. **Clone or download** the project files
2. **Navigate** to the project directory:
   ```bash
   cd "Mini E-Kart"
   ```

3. **Run the complete test suite**:
   ```bash
   python run_tests.py
   ```

   This script will:
   - Install all required dependencies
   - Check Chrome WebDriver compatibility
   - Execute all test scenarios
   - Generate comprehensive reports

### Manual Setup (Alternative)

If you prefer manual setup:

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests with Behave**:
   ```bash
   behave features/ --format=pretty
   ```

3. **Generate summary report**:
   ```bash
   python reports/test_summary.py
   ```

## 🧪 Test Features

### Feature Files Overview

| Feature File | Scenarios | Description |
|-------------|-----------|-------------|
| `add_to_cart.feature` | 8 scenarios | Adding products to cart functionality |
| `remove_from_cart.feature` | 8 scenarios | Removing products from cart |
| `total_price.feature` | 10 scenarios | Price calculation and updates |
| `empty_cart.feature` | 9 scenarios | Empty cart state management |

### Test Scenarios Examples

#### Add to Cart Tests
```gherkin
Scenario: Add specific product to cart
  Given the user is on the e-kart homepage
  And the cart is empty
  When the user clicks "Add to Cart" for "Smartphone"
  Then the cart should display "Smartphone" with price $699.99
  And the cart should contain 1 product
  And the total price should be $699.99
```

#### Remove from Cart Tests
```gherkin
Scenario: Remove specific product from cart
  Given the cart contains a "Smartphone"
  When the user clicks "Remove" for "Smartphone"
  Then the "Smartphone" should be removed from the cart
  And the cart should be empty
```

#### Total Price Tests
```gherkin
Scenario: Calculate total for multiple products
  When the user clicks "Add to Cart" for "Smartphone"
  And the user clicks "Add to Cart" for "Laptop"
  Then the total price should be $1999.98
```

## 🔧 Technical Details

### Selenium WebDriver Configuration

- **Browser**: Chrome (headless mode for CI/CD)
- **Implicit Wait**: 10 seconds
- **Explicit Wait**: 15 seconds
- **Window Size**: 1920x1080
- **Optimizations**: Disabled images, extensions, plugins

### Step Definitions

The `cart_steps.py` file contains all step implementations:

- **Given Steps**: Setup and initial state verification
- **When Steps**: User actions and interactions
- **Then Steps**: Assertions and result verification

### Test Data

Products tested:
- Smartphone ($699.99)
- Laptop ($1299.99)
- Headphones ($199.99)
- Tablet ($499.99)
- Smart Watch ($299.99)
- Camera ($899.99)

## 📊 Test Reports

### Generated Reports

1. **`behave_output.txt`**: Complete test execution log
2. **`test_summary_report.txt`**: Human-readable summary
3. **`test_results.json`**: Machine-readable results for CI/CD
4. **`behave_results.json`**: Detailed Behave output

### Sample Report Output

```
🧪 MINI E-KART TEST EXECUTION SUMMARY
============================================================
📅 Report Generated: 2024-01-15 14:30:25

🔧 Selenium Test Statistics
------------------------------
Total Tests Executed: 28
Passed: 26
Failed: 1
Errors: 1
Skipped: 0
Execution Time: 45.7 seconds
Pass Rate: 92.9%

🥒 Cucumber Test Statistics
------------------------------
Total Scenarios Executed: 25
Passed: 23
Failed: 1
Errors: 1
Skipped: 0
Scenario Pass Rate: 92.0%

📈 Overall Summary
------------------------------
Total Test Executions: 53
Total Passed: 49
Total Failed: 4
Overall Pass Rate: 92.5%

🎯 Test Status
------------------------------
⚠️ MOSTLY PASSING - Minor issues detected
🔧 Consider reviewing failed tests
```

## 🛠️ Customization

### Adding New Test Scenarios

1. **Create new feature file** in `features/` directory
2. **Add step definitions** to `cart_steps.py`
3. **Update test data** if needed
4. **Run tests** to verify

### Modifying Test Configuration

- **WebDriver settings**: Edit `utilities/driver_setup.py`
- **Test data**: Modify product information in step definitions
- **Reporting**: Customize `reports/test_summary.py`

## 🐛 Troubleshooting

### Common Issues

1. **ChromeDriver not found**:
   - Ensure Chrome browser is installed
   - The framework uses webdriver-manager for automatic management

2. **Tests failing**:
   - Check if the web app (`index.html`) is accessible
   - Verify all required elements exist in the HTML

3. **Import errors**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`

### Debug Mode

To run tests in debug mode (non-headless):
1. Edit `utilities/driver_setup.py`
2. Comment out the `--headless` option
3. Run tests to see browser interactions

## 📈 Performance

- **Total Test Execution Time**: ~45-60 seconds
- **Individual Scenario Time**: 2-5 seconds
- **Memory Usage**: ~100-200MB per browser instance
- **Parallel Execution**: Not supported (single browser instance)

## 🤝 Contributing

To add new test scenarios:

1. **Follow BDD format** with Given-When-Then structure
2. **Use descriptive scenario names**
3. **Add appropriate step definitions**
4. **Update this README** with new test counts

## 📝 License

This testing framework is part of the Mini E-Kart project and follows the same licensing terms.

---

**Happy Testing! 🎉**

For questions or issues, check the test output logs in the `reports/` directory.

