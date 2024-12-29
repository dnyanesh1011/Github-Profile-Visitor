import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def visit_github_profile(chrome_driver_path, profile_url, visits, delay=1):
    """
    Automates visiting a GitHub profile multiple times using Selenium.
    
    Args:
        chrome_driver_path (str): Path to the ChromeDriver executable.
        profile_url (str): URL of the GitHub profile to visit.
        visits (int): Number of times to visit the profile.
        delay (int): Delay between visits in seconds. Default is 1 second.
    """
    # Set up the WebDriver
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    print("Starting profile visits...")

    try:
        for i in range(visits):
            print(f"Visit {i + 1}/{visits}: Opening {profile_url}")
            driver.get(profile_url)  # Visit the profile
            time.sleep(delay)  # Wait to mimic real browsing behavior
            driver.delete_all_cookies()  # Clear cookies for anonymity
            print(f"Visit {i + 1}/{visits}: Completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()  # Close the browser
        print(f"Completed {visits} visits to {profile_url}.")


if __name__ == "__main__":
    # Configuration
    CHROME_DRIVER_PATH = r"chromedriver.exe"  # Adjust the path as needed
    PROFILE_URL = "https://github.com/your-profile"  # Replace with your GitHub profile URL
    VISITS = 684  # Number of visits to perform
    DELAY_BETWEEN_VISITS = 1  # Delay in seconds

    # Start the visiting process
    visit_github_profile(CHROME_DRIVER_PATH, PROFILE_URL, VISITS, DELAY_BETWEEN_VISITS)
