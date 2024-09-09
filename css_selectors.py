
# open the url
driver.get('https://www.amazon.com/')

# By CSS, by ID, use #:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# Same as =>
driver.find_element(By.ID, "twotabsearchtextbox")  # Note, By.ID is preferred if you only use ID

# By CSS, by class, use .
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute")
driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
# By CSS, by tag & class(es)
driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")
# By CSS, tag & ID & class
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input.nav-progressive-attribute")

# By CSS, attributes, use []:
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, ".nav-input[tabindex='0'][placeholder='Search Amazon']")

# By CSS, attribute, partial match:
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[class*='search']")
driver.find_element(By.CSS_SELECTOR, "[id*='search']")

#partial search
driver.find_element(By.CSS_SELECTOR, "[class*='search']")

# By CSS, from parent => to child, separate by space:
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")
driver.find_element(By.CSS_SELECTOR, ".a-box-inner #legalTextRow [href*='privacy']")