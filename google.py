from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=900)
    #create a new page/tab
    page = browser.new_page()
    #visit playwright website
    page.goto("https://www.playwright.dev/python")
   
    browser.close()