from playwright.sync_api import sync_playwright
import time

# p=sync_playwright().start()
# browser=p.chromium.launch(headless=False)
# page1=browser.new_page()
# page1.goto("https://www.google.com")
# time.sleep(5)
# p.stop()

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    # page.goto("https://www.scrapethissite.com/pages/forms/")

    # # use to select the element and type in this
    # page.get_by_role("textbox",name="Search for Teams: ").type("New York Islanders")
    # page.get_by_role("button",name="Search").click()

    # # Use to Click on Element
    # page.click("input[value='Search']")
    # page.get_by_text("Login").click()

    # # Get Element by the Labels
    # page.get_by_label("Your Password").type("muhammadTaha15")
    # page.get_by_label("Your Email").type("toaha@gmail.com")
    # page.get_by_role("button",name="Login →").click()


    # page.goto("https://practicetestautomation.com/practice-test-login/")

    # #Get the Element by the Alt text
    # page.get_by_alt_text("Practice Test Automation").click()

    # text=page.get_by_text("Username",exact=True).text_content()
    # print(text)

    # # Get all Text in page
    # text_elements=page.get_by_text("Username",exact=True).all()
    # for element in text_elements:
    #     print(element.text_content())

    # user=page.locator("//*[@id='username']")
    # user.type("Toaha15@gmail.com")

    # # Use of Xpath to check the Box
    # page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # page.locator('//*[@id="checkBoxOption1"]').check()
    # page.locator('//*[@id="checkBoxOption1"]').click()

    page.goto("https://www.hyrtutorials.com/p/waits-demo.html")
    page.get_by_text("Add Textbox1").click()
    
    time.sleep(10)
    page.get_by_placeholder("Textbox1").first.type("Taha")
    page.get_by_text("Add Textbox2").click()
    time.sleep(20)
    page.get_by_placeholder("Textbox2").first.type("Hanzala")

    time.sleep(10)
    




