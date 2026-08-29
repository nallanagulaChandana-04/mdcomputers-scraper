from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote_plus
import time


def build_search_url(search_term):
    encoded_term = quote_plus(search_term)

    return (
        "https://mdcomputers.in/"
        f"?route=product/search&search={encoded_term}"
    )


def main():

    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    url = build_search_url(search_term)

    print("\nSearch URL:")
    print(url)

    options = Options()

    # IMPORTANT:
    # Do NOT use headless mode.
    # We want to see what the website actually displays.
    options.add_argument("--window-size=1400,1000")

    driver = webdriver.Chrome(options=options)

    try:

        print("\nOpening website...")

        driver.get(url)

        # Give the website time to load
        time.sleep(8)

        print("\nPage loaded.")

        print("\nCurrent URL:")
        print(driver.current_url)

        print("\nPage title:")
        print(driver.title)

        # --------------------------------------------------
        # Check product-related elements
        # --------------------------------------------------

        product_layouts = driver.find_elements(
            By.CSS_SELECTOR,
            ".product-layout"
        )

        product_thumbs = driver.find_elements(
            By.CSS_SELECTOR,
            ".product-thumb"
        )

        h4_links = driver.find_elements(
            By.CSS_SELECTOR,
            "h4 a"
        )

        product_links = driver.find_elements(
            By.XPATH,
            "//a[contains(@href, 'product')]"
        )

        print("\n----------------------------------------")
        print("DEBUG INFORMATION")
        print("----------------------------------------")

        print(
            "Product layouts:",
            len(product_layouts)
        )

        print(
            "Product thumbs:",
            len(product_thumbs)
        )

        print(
            "H4 links:",
            len(h4_links)
        )

        print(
            "Product-related links:",
            len(product_links)
        )

        # --------------------------------------------------
        # Print visible page text
        # --------------------------------------------------

        body_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        print("\n----------------------------------------")
        print("PAGE TEXT")
        print("----------------------------------------")

        print(body_text[:3000])

        # --------------------------------------------------
        # Save page source for inspection
        # --------------------------------------------------

        with open(
            "debug_page.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                driver.page_source
            )

        print("\n----------------------------------------")
        print("Saved page source as:")
        print("debug_page.html")
        print("----------------------------------------")

        print("\nBrowser will remain open.")
        print("Check what is displayed in Chrome.")

        input(
            "\nPress ENTER here after checking the browser..."
        )

    finally:

        driver.quit()


if __name__ == "__main__":
    main()