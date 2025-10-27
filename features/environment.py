"""
Environment file for Behave tests
This file sets up the WebDriver before each scenario
"""

from utilities.driver_setup import DriverSetup


def before_scenario(context, scenario):
    """
    Behave hook that runs before each scenario
    Sets up the WebDriver and navigates to homepage
    """
    print(f"\n🚀 Starting scenario: {scenario.name}")
    context.driver_setup = DriverSetup()
    context.driver = context.driver_setup.setup_driver()
    context.wait = context.driver_setup.get_wait()
    
    # Navigate to homepage
    success = context.driver_setup.navigate_to_homepage()
    if not success:
        raise Exception("Failed to navigate to homepage")


def after_scenario(context, scenario):
    """
    Behave hook that runs after each scenario
    Cleans up WebDriver resources
    """
    print(f"🏁 Completed scenario: {scenario.name}")
    if hasattr(context, 'driver_setup'):
        context.driver_setup.cleanup()
    print("-" * 50)

