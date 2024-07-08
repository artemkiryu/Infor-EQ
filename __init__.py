import pytest
import time
import json

from pytest_html.extras import url
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestLoginpage():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    ##def teardown_method(self, method):
        ##self.driver.quit()

    def test_loginpage(self):
        # Test name: login_page
        # Step # | name | target | value
        # 1 | open | main URL |
        self.driver.get("https://mingle-portal.inforcloudsuite.com/v2/ZMJ82E43PJMRC4QC_TST/8db4db08-025f-46bd-9da0-9f984d8c1aca")
        self.driver.set_window_size(1370, 1012)


        # 3 | click | linkText=Cloud Identities |
        self.driver.find_element(By.LINK_TEXT, "Cloud Identities").click()


        #Login Informatgion
        self.driver.find_element(By.ID, "username").send_keys("*******")
        self.driver.find_element(By.ID, "pass").send_keys("*******")
        # 6 | click | css=.ping-button |
        self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()

        # Timeout 30 seconds
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(.,\'Home\')]")))
        element = self.driver.find_element(By.ID, "osp-tabh-morebutton")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 2 | click | id=osp-tabh-morebutton |
        self.driver.find_element(By.ID, "osp-tabh-morebutton").click()


        # 7 | selectFrame | index=0 |
        self.driver.switch_to.frame(0)
        # 10 | click | xpath=//span[contains(.,'Home')] |
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Home\')]").click()


        # Test name: allButtonAssert
        # Step # | name | target | value
        # 1 | mouseOver | id=osp-tabh-morebutton |
        element = self.driver.find_element(By.ID, "osp-tabh-morebutton")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 2 | click | id=osp-tabh-morebutton |
        self.driver.find_element(By.ID, "osp-tabh-morebutton").click()


        # 3 | mouseOut | id=osp-tabh-morebutton |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()


        # 4 | click | id=osp-tabh-morebutton |
        self.driver.find_element(By.ID, "osp-tabh-morebutton").click()

        # 5 | click | xpath=//a[contains(text(),'Enterprise Quoting')] |
        self.driver.find_element(By.XPATH, "//a[contains(text(),\'Enterprise Quoting\')]").click()

        # 6 | assertTitle | Enterprise Quoting |
        assert self.driver.title == "Enterprise Quoting"

        # 7 | selectFrame | index=1 |
        self.driver.switch_to.frame(1)

        # 8 | assertText | css=.MobileNavigationLink:nth-child(1) .caption | Dealers
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".MobileNavigationLink:nth-child(1) .caption").text == "Dealers"
        # 9 | click | css=.MobileNavigationLink:nth-child(1) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".MobileNavigationLink:nth-child(1) .caption").click()

        # 10 | assertTitle | Infor |
        assert self.driver.title == "Infor"
        # 11 | assertText | css=.container-element:nth-child(1) > .navigation-menu > ul > .navigation-link:nth-child(2) .caption | Quotes
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container-element:nth-child(1) > .navigation-menu > ul > .navigation-link:nth-child(2) .caption").text == "Quotes"
        # 12 | click | linkText=Quotes |
        self.driver.find_element(By.LINK_TEXT, "Quotes").click()

        # 13 | mouseOver | linkText=Quotes |
        element = self.driver.find_element(By.LINK_TEXT, "Quotes")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # 14 | mouseOut | linkText=Quotes |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

        # 15 | assertText | css=.container-element:nth-child(5) > .breadcrumb-container .v-caption | Quotes
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container-element:nth-child(5) > .breadcrumb-container .v-caption").text == "Quotes"
        # 16 | assertText | css=ul:nth-child(1) > .NavigationLink:nth-child(3) .caption | Orders
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "ul:nth-child(1) > .NavigationLink:nth-child(3) .caption").text == "Orders"
        # 17 | click | css=ul:nth-child(1) > .NavigationLink:nth-child(3) .caption |
        self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(1) > .NavigationLink:nth-child(3) .caption").click()

        # 18 | mouseOver | css=ul:nth-child(1) > .NavigationLink:nth-child(3) .caption |
        element = self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(1) > .NavigationLink:nth-child(3) .caption")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # 19 | mouseOut | css=.selected:nth-child(3) .caption |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

        # 20 | assertText | css=.container-element:nth-child(5) > .breadcrumb-container .v-caption | Orders
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container-element:nth-child(5) > .breadcrumb-container .v-caption").text == "Orders"

        # 21 | assertText | css=.MobileNavigationLink:nth-child(4) .caption | Customers
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".MobileNavigationLink:nth-child(4) .caption").text == "Customers"

        # 22 | click | css=.MobileNavigationLink:nth-child(4) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".MobileNavigationLink:nth-child(4) .caption").click()

        # 23 | assertText | css=.breadcrumb .v-caption | Customers
        assert self.driver.find_element(By.CSS_SELECTOR, ".breadcrumb .v-caption").text == "Customers"

        # 24 | assertText | css=.MobileNavigationLink:nth-child(5) .caption | Agreements
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".MobileNavigationLink:nth-child(5) .caption").text == "Agreements"

        # 25 | click | css=.MobileNavigationLink:nth-child(5) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".MobileNavigationLink:nth-child(5) .caption").click()

        # 26 | verifyText | css=.container-element:nth-child(7) > .breadcrumb-container .v-caption | Agreements
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container-element:nth-child(7) > .breadcrumb-container .v-caption").text == "Agreements"

        # 27 | assertText | css=ul:nth-child(1) > .NavigationLink:nth-child(6) .caption | Projects
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "ul:nth-child(1) > .NavigationLink:nth-child(6) .caption").text == "Projects"

        # 28 | click | linkText=Projects |
        self.driver.find_element(By.LINK_TEXT, "Projects").click()

        # 29 | assertText | css=.breadcrumb .v-caption | Projects
        assert self.driver.find_element(By.CSS_SELECTOR, ".breadcrumb .v-caption").text == "Projects"

        # 30 | assertText | css=.container-element:nth-child(1) > .navigation-menu .navigation-item:nth-child(7) > a > .caption | Items
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container-element:nth-child(1) > .navigation-menu .navigation-item:nth-child(7) > a > .caption").text == "Items"

        # 31 | click | css=.container-element:nth-child(1) > .navigation-menu .navigation-item:nth-child(7) > a > .caption |
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".container-element:nth-child(1) > .navigation-menu .navigation-item:nth-child(7) > a > .caption").click()

        # 32 | assertText | css=.selected > .children .caption | Named Configurations
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected > .children .caption").text == "Named Configurations"

        # 33 | click | css=.selected > .children .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".selected > .children .caption").click()

        # 34 | assertText | xpath=//div[@id='navigation-target']/div/div/ul/li/a/span | Named Configurations
        assert self.driver.find_element(By.XPATH,
                                        "//div[@id=\'navigation-target\']/div/div/ul/li/a/span").text == "Named Configurations"

        # 35 | assertText | css=.container-element:nth-child(1) > .navigation-menu .navigation-item:nth-child(8) > a > .caption | Product Maintenance
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container-element:nth-child(1) > .navigation-menu .navigation-item:nth-child(8) > a > .caption").text == "Product Maintenance"

        # 36 | click | linkText=Product Maintenance |
        self.driver.find_element(By.LINK_TEXT, "Product Maintenance").click()

        # 37 | assertText | linkText=Series | Series
        assert self.driver.find_element(By.LINK_TEXT, "Series").text == "Series"

        # 38 | assertText | css=.selected .navigation-link:nth-child(2) .caption | Models
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected .navigation-link:nth-child(2) .caption").text == "Models"

        # 39 | assertText | css=.selected .navigation-link:nth-child(3) .caption | Categories
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected .navigation-link:nth-child(3) .caption").text == "Categories"

        # 40 | assertText | css=.selected .navigation-link:nth-child(4) .caption | Products
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected .navigation-link:nth-child(4) .caption").text == "Products"

        # 41 | assertText | css=.selected .navigation-link:nth-child(5) .caption | Price Lists
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected .navigation-link:nth-child(5) .caption").text == "Price Lists"

        # 42 | assertText | css=.selected .navigation-link:nth-child(6) .caption | Product Filter Attributes
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected .navigation-link:nth-child(6) .caption").text == "Product Filter Attributes"

        # 43 | click | css=.selected .navigation-link:nth-child(1) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".selected .navigation-link:nth-child(1) .caption").click()

        # 44 | mouseOver | xpath=//div[@id='root']/div/div/nav/ul/li[8]/ul/li/a/span |
        element = self.driver.find_element(By.XPATH, "//div[@id=\'root\']/div/div/nav/ul/li[8]/ul/li/a/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # 45 | mouseOut | css=.selected:nth-child(1) .caption |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

        # 46 | assertText | css=.breadcrumb .v-caption | Series
        assert self.driver.find_element(By.CSS_SELECTOR, ".breadcrumb .v-caption").text == "Series"

        # 47 | click | css=.active .navigation-link:nth-child(2) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".active .navigation-link:nth-child(2) .caption").click()

        # 48 | assertText | css=.breadcrumb .v-caption | Models
        assert self.driver.find_element(By.CSS_SELECTOR, ".breadcrumb .v-caption").text == "Models"

        # 49 | click | css=.expanded .navigation-link:nth-child(3) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".expanded .navigation-link:nth-child(3) .caption").click()

        # 50 | assertText | css=.disabled > .v-caption:nth-child(1) | Categories
        assert self.driver.find_element(By.CSS_SELECTOR, ".disabled > .v-caption:nth-child(1)").text == "Categories"

        # 51 | click | css=.expanded .navigation-link:nth-child(4) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".expanded .navigation-link:nth-child(4) .caption").click()
        # 52 | assertText | xpath=//div[@id='navigation-target']/div/div/ul/li/a/span | Products
        assert self.driver.find_element(By.XPATH,
                                        "//div[@id=\'navigation-target\']/div/div/ul/li/a/span").text == "Products"

        # 53 | click | css=.expanded .navigation-link:nth-child(5) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".expanded .navigation-link:nth-child(5) .caption").click()

        # 54 | assertText | xpath=//div[@id='navigation-target']/div/div/ul/li/a/span | Price Lists
        assert self.driver.find_element(By.XPATH,
                                        "//div[@id=\'navigation-target\']/div/div/ul/li/a/span").text == "Price Lists"

        # 55 | click | css=.expanded .navigation-link:nth-child(6) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".expanded .navigation-link:nth-child(6) .caption").click()
        # 56 | assertText | xpath=//div[@id='navigation-target']/div/div/ul/li/a/span | Product Filter Attributes
        assert self.driver.find_element(By.XPATH,
                                        "//div[@id=\'navigation-target\']/div/div/ul/li/a/span").text == "Product Filter Attributes"

        # 57 | assertText | css=.MobileNavigationLink:nth-child(9) .caption | Reports
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".MobileNavigationLink:nth-child(9) .caption").text == "Reports"

        # 58 | click | css=.MobileNavigationLink:nth-child(9) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".MobileNavigationLink:nth-child(9) .caption").click()

        # 59 | assertText | xpath=//div[@id='navigation-target']/div/div/ul/li/a/span | Reports
        assert self.driver.find_element(By.XPATH,
                                        "//div[@id=\'navigation-target\']/div/div/ul/li/a/span").text == "Reports"

        # 60 | assertText | css=.navigation-item:nth-child(12) > a > .caption | System Messages
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".navigation-item:nth-child(12) > a > .caption").text == "System Messages"

        # 61 | click | css=.MobileNavigationLink:nth-child(9) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".MobileNavigationLink:nth-child(9) .caption").click()

        # 62 | assertText | css=.container-element:nth-child(1) > .breadcrumb-container .v-caption | Reports
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container-element:nth-child(1) > .breadcrumb-container .v-caption").text == "Reports"

        # 63 | assertText | css=.navigation-item:nth-child(12) > a > .caption | System Messages
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".navigation-item:nth-child(12) > a > .caption").text == "System Messages"

        # 64 | click | css=.navigation-item:nth-child(12) > a > .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".navigation-item:nth-child(12) > a > .caption").click()

        # 65 | assertText | css=.selected .navigation-link:nth-child(1) .caption | System Messages
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected .navigation-link:nth-child(1) .caption").text == "System Messages"

        # 66 | click | css=.selected .navigation-link:nth-child(1) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".selected .navigation-link:nth-child(1) .caption").click()

        # 67 | assertText | xpath=//div[@id='navigation-target']/div/div/ul/li/a/span | System Messages
        assert self.driver.find_element(By.XPATH,
                                        "//div[@id=\'navigation-target\']/div/div/ul/li/a/span").text == "System Messages"

        # 68 | assertText | css=.navigation-item:nth-child(12) .navigation-link:nth-child(2) .caption | Dealer Groups
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".navigation-item:nth-child(12) .navigation-link:nth-child(2) .caption").text == "Dealer Groups"

        # 69 | click | css=.navigation-item:nth-child(12) .navigation-link:nth-child(2) .caption |
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".navigation-item:nth-child(12) .navigation-link:nth-child(2) .caption").click()

        # 70 | assertText | css=.link > .v-caption | Dealer Groups
        assert self.driver.find_element(By.CSS_SELECTOR, ".link > .v-caption").text == "Dealer Groups"

        # 71 | assertText | css=.navigation-item:nth-child(13) > a > .caption | My Company
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".navigation-item:nth-child(13) > a > .caption").text == "My Company"

        # 72 | click | linkText=Dealer Groups |
        self.driver.find_element(By.LINK_TEXT, "Dealer Groups").click()

        # 73 | mouseOver | linkText=Dealer Groups |
        element = self.driver.find_element(By.LINK_TEXT, "Dealer Groups")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # 74 | mouseOut | linkText=Dealer Groups |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

        # 75 | assertText | css=.link > .v-caption | Dealer Groups
        assert self.driver.find_element(By.CSS_SELECTOR, ".link > .v-caption").text == "Dealer Groups"

        # 76 | assertText | css=.navigation-item:nth-child(13) > a > .caption | My Company
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".navigation-item:nth-child(13) > a > .caption").text == "My Company"
        # 77 | click | linkText=My Company |
        self.driver.find_element(By.LINK_TEXT, "My Company").click()
        # 78 | assertText | css=.selected .navigation-link:nth-child(1) .caption | Profile
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".selected .navigation-link:nth-child(1) .caption").text == "Profile"
        # 79 | click | css=.selected .navigation-link:nth-child(1) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".selected .navigation-link:nth-child(1) .caption").click()

        # 80 | assertText | css=.link > .v-caption | Profile
        assert self.driver.find_element(By.CSS_SELECTOR, ".link > .v-caption").text == "Profile"

        # 81 | assertText | css=.active .navigation-link:nth-child(3) .caption | Territories
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".active .navigation-link:nth-child(3) .caption").text == "Territories"

        # 82 | click | css=.active .navigation-link:nth-child(3) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".active .navigation-link:nth-child(3) .caption").click()

        # 83 | assertText | css=.breadcrumb .v-caption | Territories
        assert self.driver.find_element(By.CSS_SELECTOR, ".breadcrumb .v-caption").text == "Territories"

        # 84 | assertText | css=.expanded .navigation-link:nth-child(4) .caption | Representatives
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".expanded .navigation-link:nth-child(4) .caption").text == "Representatives"

        # 85 | click | css=.expanded .navigation-link:nth-child(4) .caption |
        self.driver.find_element(By.CSS_SELECTOR, ".expanded .navigation-link:nth-child(4) .caption").click()

        # 86 | assertText | css=.breadcrumb .v-caption | Representatives
        assert self.driver.find_element(By.CSS_SELECTOR, ".breadcrumb .v-caption").text == "Representatives"

