# Import the necessary Selenium webdriver module
from selenium import webdriver
import time

def run_financial_automation():
    print("Initializing browser automation...")
    
    # Step 1: Initialize the Chrome WebDriver
    # Note: Modern Selenium (v4+) handles driver installation automatically in most cases.
    driver = webdriver.Chrome()
    
    try:
        # Step 2: Navigate to a financial data source
        target_url = "https://finance.yahoo.com/markets/world-indices/"
        print(f"Navigating to: {target_url}")
        driver.get(target_url)
        
        # Step 3: Automate browser behavior (Maximize window for better data loading)
        driver.maximize_window()
        
        # Pause to allow the page's JavaScript to render dynamic financial data
        time.sleep(3) 
        
        # Step 4: Extract basic page data to confirm successful navigation
        page_title = driver.title
        print("\n--- Automation Success ---")
        print(f"Active Page Title: {page_title}")
        print(f"Current URL: {driver.current_url}")
        print("--------------------------\n")
        
        # Hold the browser open briefly so you can visually verify the result
        time.sleep(2)
        
    except Exception as e:
        print(f"An error occurred during automation: {e}")
        
    finally:
        # Step 5: Gracefully close the browser and end the WebDriver session
        print("Closing the browser session...")
        driver.quit()

if __name__ == "__main__":
    run_financial_automation()