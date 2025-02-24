#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import undetected_chromedriver as uc
# # Setup Selenium WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
# driver2 = webdriver.Chrome(options=options)
# Create a Chrome driver with uc


# In[328]:


p_name = []
p_price = []
p_code = []
p_rating = []
p_reviews = []
p_desc = []
star_5 = []
star_4 = []
star_3 = []
star_2 = []
star_1 = []
######################################################
colour_list = []
fit_type_list = []
size_list = []
availability_list = []
low_stock_count_list = []


# In[354]:


# Prompt the user for URL choice
user_choice = input("Do you want to use the sample product URL or enter a new one? (Type 'sample' or 'new'): ").strip().lower()

# Check the choice and set the URL accordingly
if user_choice == 'new':
    url = input("Enter the new product URL: ").strip()
else:
    url = "https://www.next.co.uk/style/st443901/c15109"
    print("Using the sample product URL.")

# Reminder to keep the browser in the foreground
print("Keep the browser in the foreground at all times to allow interactions.")
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
# Open the product page
driver.get(url)


# In[337]:


try:
    # Wait and click the "Accept All Cookies" button by visible text
    wait = WebDriverWait(driver, 60)
    accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept All Cookies']")))
    accept_button.click()
except:
    pass


# In[340]:


time.sleep(3)
for k in range(7):
    # Scroll down by a chunk
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1.2)
wait = WebDriverWait(driver, 1)


# In[1]:


def Scraping_Data_List_Function(fit_value, color_now, product_size, stock_availability, quantity):
    wait = WebDriverWait(driver, 1)
    try:
        product_desc = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='item-description']"))).get_attribute("innerText")
    except:
        product_desc = ""
    
    try:
        product_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-title']"))).text
    except:
        product_title = ""
    
    try:
        now_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-now-price']"))).text
    except:
        now_price = ""
    
    try:
        reviews = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='rating-style-badge']"))).text
        reviews = reviews.replace("(", "").replace(")", "")
    except:
        reviews = ""
    
    try:
        Rating = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label*='Stars']"))).get_attribute("aria-label")
        Rating = Rating.replace("Stars", "")
    except:
        Rating = ""
    
    try:
        pr_code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-code']"))).text
    except:
        pr_code
    
    stars5 = ""
    stars4 = ""
    stars3 = ""
    stars2 = ""
    stars1 = ""
    try:
        stars = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Stars')]")
        for star in stars:
            rating = star.get_attribute("aria-label")
            count = star.find_element(By.TAG_NAME, "p").text
            if count.find("Star") != -1:
                count = '(0)'
            if rating == "5 Stars":
                stars5 = count.replace("(", "").replace(")", "")
            elif rating == "4 Stars":
                stars4 = count.replace("(", "").replace(")", "")
            elif rating == "3 Stars":
                stars3 = count.replace("(", "").replace(")", "")
            elif rating == "2 Stars":
                stars2 = count.replace("(", "").replace(")", "")
            elif rating == "1 Stars":
                stars1 = count.replace("(", "").replace(")", "")
    except:
        pass
    p_name.append(product_title)
    p_price.append(now_price)
    p_code.append(pr_code)
    p_rating.append(Rating)
    p_reviews.append(reviews)
    p_desc.append(product_desc)

    star_5.append(stars5)
    star_4.append(stars4)
    star_3.append(stars3)
    star_2.append(stars2)
    star_1.append(stars1)

    colour_list.append(color_now)
    fit_type_list.append(fit_value)
    size_list.append(product_size)
    availability_list.append(stock_availability)
    low_stock_count_list.append(quantity)


# In[2]:


def color_selection(fit_value):
    # Locate color buttons and click each one
    wait = WebDriverWait(driver, 3)
    try:
        color_buttons = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-testid='colour-chips-button-group']//button")
        ))
        wait = WebDriverWait(driver, 10)
        sizes_colours = len(color_buttons)
        for button in range(sizes_colours):
            while True:
                try:
                    color_buttons = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@data-testid='colour-chips-button-group']//button")
                    ))
                    color_buttons[button].click()
                    break
                except:
                    time.sleep(0.3)
            time.sleep(2)  # Adjust sleep time if necessary
            color_now = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='selected-colour-label']"))).text
    
            # print("Selected Color Label:", color_now)
            Size_Stock_Selection(fit_value, color_now)
    except:
        try:
            fit_select = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-testid='colour-select']//div[@role='combobox']")
            ))
            fit_select.click()
            wait = WebDriverWait(driver, 10)
            # Wait for the dropdown to expand and the list to be visible
            fit_options = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@aria-labelledby='colour-input-label']//li")
            ))
            sizes_length = len(fit_options)
            # Loop through each option, click it, and extract the text
            for option in range(sizes_length):
                if option != 0:
                    fit_select = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[@data-testid='colour-select']//div[@role='combobox']")
                    ))
                    fit_select.click()
                # Wait for the dropdown to expand and the list to be visible
                fit_options = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//ul[@aria-labelledby='colour-input-label']//li")
                ))
                color_now = fit_options[option].get_attribute("innerText")  # Extract inner text
                # print(color_now)
                fit_options[option].click()
                time.sleep(2)  # Optional: Add a small delay between clicks
                Size_Stock_Selection(fit_value, color_now)
        except:
            # print("Color expection!!!!")
            Size_Stock_Selection(fit_value, "")


# In[3]:


def Fit_selection():
    try:
        # Locate fit buttons and click each one
        wait = WebDriverWait(driver, 1)
        fit_buttons = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-testid='fit-chips-button-group']//button")
        ))
        wait = WebDriverWait(driver, 10)
        sizes_fits = len(fit_buttons)
        for buttonf in range(sizes_fits):
            while True:
                try:
                    fit_buttons = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, "//div[@data-testid='fit-chips-button-group']//button")
                    ))
                    fit_buttons[buttonf].click()
                    break
                except:
                    time.sleep(0.3)
            time.sleep(2)  # Adjust sleep time if necessary
            fit_option_text = fit_buttons[buttonf].text
            # print("Selected option:", fit_option_text)
            color_selection(fit_option_text)
    except:
        try:
            # Locate the size select element by data-testid and click it
            fit_select = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-testid='fit-select']//div[@role='combobox']")
            ))
            fit_select.click()
            wait = WebDriverWait(driver, 10)
            # Wait for the dropdown to expand and the list to be visible
            fit_options = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@aria-labelledby='fit-input-label']//li")
            ))
            sizes_length = len(fit_options)
            # Loop through each option, click it, and extract the text
            for option in range(sizes_length):
                if option != 0:
                    # Locate the size select element by data-testid and click it
                    fit_select = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//div[@data-testid='fit-select']//div[@role='combobox']")
                    ))
                    fit_select.click()
                # Wait for the dropdown to expand and the list to be visible
                fit_options = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, "//ul[@aria-labelledby='fit-input-label']//li")
                ))
                fit_text = fit_options[option].get_attribute("innerText")  # Extract inner text
                # print(fit_text)
                fit_options[option].click()
                time.sleep(2)  # Optional: Add a small delay between clicks
                color_selection(fit_text)
        except:
            color_selection("")


# In[4]:


def Size_Stock_Selection(fit_value, color_now):
    try:
        wait = WebDriverWait(driver, 1)
        # Locate the size select element by data-testid and click it
        size_select = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@data-testid='size-select']//div[@role='combobox']")
        ))
        size_select.click()
        wait = WebDriverWait(driver, 10)
        # Wait for the dropdown to expand and the list to be visible
        size_options = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//ul[@aria-labelledby='size-input-label']//li")
        ))
        sizes_length = len(size_options)
        # Loop through each option, click it, and extract the text
        for option in range(sizes_length):
            if option != 0:
                # Locate the size select element by data-testid and click it
                size_select = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@data-testid='size-select']//div[@role='combobox']")
                ))
                size_select.click()
            # Wait for the dropdown to expand and the list to be visible
            size_options = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "//ul[@aria-labelledby='size-input-label']//li")
            ))
            size_text = size_options[option].get_attribute("innerText")  # Extract inner text
            parts = size_text.rsplit(" - ", 1)  # Split before the last occurrence of "-"
            product_size = parts[0].strip()  # Product size
            stock_availability = parts[1].strip() if len(parts) > 1 else ""  # Stock availability
            stock_availability = stock_availability.lower()
            if stock_availability.find("unavailable") != -1:
                stock_availability = "Out of Stock"
            elif stock_availability == "":
                stock_availability = "In Stock"
            elif stock_availability == "low stock":
                stock_availability = "Low stock"
            else:
                stock_availability = "In Stock!"
            
            # print("Product Size:", product_size)
            # print("Stock Availability:", stock_availability)
            size_options[option].click()
            time.sleep(1)  # Optional: Add a small delay between clicks
            quantity = ""
            if stock_availability == "Low stock":
                while True:
                    try:
                        # Locate the "Add to Bag" button using its data-testid attribute
                        add_to_bag_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='item-form-addToBag-button']")
                        
                        # Click the button using JavaScript
                        driver.execute_script("arguments[0].click();", add_to_bag_button)
                        time.sleep(2)
                        # Wait for the item status element to be present and extract the text
                        wait = WebDriverWait(driver, 10)
                        item_status = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='header-mini-shopping-bag-item-status']"))).text
                        # print(item_status)
                        item_status = item_status.lower()
                        flag = False
                        if item_status == "currently unavailable" or item_status == "item unavailable":
                            # Locate the quantity element
                            quantity_element = driver.find_elements(By.CSS_SELECTOR, ".MuiTypography-body1.header-19bdvxc")
                            for qt in quantity_element:
                                if qt.text.lower().find("quantity") != -1:
                                    # Extract the text and get the quantity value
                                    quantity_text = qt.text
                                    quantity = quantity_text.split(": ")[1]  # Extracts the number after "Quantity: "
                                    quantity = int(quantity) - 1
                                    # Print the quantity
                                    # print(quantity)
                                    flag = True
                                    break
                        elif item_status == "in stock":
                            pass
                        else:
                            quantity = ""
                            break
                        if flag == True:
                            break
                    except:
                        quantity = ""
                        break
                    time.sleep(1)
            Scraping_Data_List_Function(fit_value, color_now, product_size, stock_availability, quantity)
    except:
        try:
            # Find size selection buttons using data-testid
            size_buttons = driver.find_elements(By.CSS_SELECTOR, "[data-testid='size-chips-button-group'] button")
            if len(size_buttons) != 0:
                sizes_stocks_length = len(size_buttons)
                # Loop through each button, click it, and extract the size
                for button in range(sizes_stocks_length):
                    # Find size selection buttons using data-testid
                    size_buttons = driver.find_elements(By.CSS_SELECTOR, "[data-testid='size-chips-button-group'] button")
                    size = size_buttons[button].text
                    while True:
                        try:
                            size_buttons[button].click()
                            break
                        except:
                            time.sleep(0.3)
                    # print(f"Size selected: {size}")
                    time.sleep(0.5)
                    # Wait until the stock status element is present
                    wait = WebDriverWait(driver, 10)
                    stock_status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='item-form-stock-status']")))
                    
                    # Extract the stock status using JavaScript
                    stock_status = driver.execute_script("return arguments[0].innerText;", stock_status_element)
                    
                    # Print the stock status
                    # print(f"Stock status: {stock_status}")
                    stock_status = stock_status.lower()
        
                    if stock_status.find("unavailable") != -1:
                        stock_status = "Out of Stock"
                    elif stock_status == "low stock":
                        stock_status = "Low stock"
                    else:
                        stock_status = "In Stock"

                    quantity = ""
                    if stock_status == "Low stock":
                        while True:
                            try:
                                # Locate the "Add to Bag" button using its data-testid attribute
                                add_to_bag_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='item-form-addToBag-button']")
                                
                                # Click the button using JavaScript
                                driver.execute_script("arguments[0].click();", add_to_bag_button)
                                time.sleep(2)
                                # Wait for the item status element to be present and extract the text
                                wait = WebDriverWait(driver, 10)
                                item_status = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='header-mini-shopping-bag-item-status']"))).text
                                # print(item_status)
                                item_status = item_status.lower()
                                flag = False
                                if item_status == "currently unavailable" or item_status == "item unavailable":
                                    # Locate the quantity element
                                    quantity_element = driver.find_elements(By.CSS_SELECTOR, ".MuiTypography-body1.header-19bdvxc")
                                    for qt in quantity_element:
                                        if qt.text.lower().find("quantity") != -1:
                                            # Extract the text and get the quantity value
                                            quantity_text = qt.text
                                            quantity = quantity_text.split(": ")[1]  # Extracts the number after "Quantity: "
                                            quantity = int(quantity) - 1
                                            # Print the quantity
                                            # print(quantity)
                                            flag = True
                                            break
                                elif item_status == "in stock":
                                    pass
                                else:
                                    quantity = ""
                                    break
                                if flag == True:
                                    break
                            except:
                                quantity = ""
                                break
                            time.sleep(1)
                    Scraping_Data_List_Function(fit_value, color_now, size, stock_status, quantity)
            else:
                # Wait until the stock status element is present
                wait = WebDriverWait(driver, 10)
                stock_status_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='item-form-stock-status']")))
                
                # Extract the stock status using JavaScript
                stock_status = driver.execute_script("return arguments[0].innerText;", stock_status_element)
                
                # Print the stock status
                # print(f"Stock status: {stock_status}")
                stock_status = stock_status.lower()
        
                if stock_status.find("unavailable") != -1:
                    stock_status = "Out of Stock"
                elif stock_status == "low stock":
                    stock_status = "Low stock"
                else:
                    stock_status = "In Stock"
                quantity = ""
                if stock_status == "Low stock":
                    while True:
                        try:
                            # Locate the "Add to Bag" button using its data-testid attribute
                            add_to_bag_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='item-form-addToBag-button']")
                            
                            # Click the button using JavaScript
                            driver.execute_script("arguments[0].click();", add_to_bag_button)
                            time.sleep(2)
                            # Wait for the item status element to be present and extract the text
                            wait = WebDriverWait(driver, 10)
                            item_status = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='header-mini-shopping-bag-item-status']"))).text
                            # print(item_status)
                            item_status = item_status.lower()
                            flag = False
                            if item_status == "currently unavailable" or item_status == "item unavailable":
                                # Locate the quantity element
                                quantity_element = driver.find_elements(By.CSS_SELECTOR, ".MuiTypography-body1.header-19bdvxc")
                                for qt in quantity_element:
                                    if qt.text.lower().find("quantity") != -1:
                                        # Extract the text and get the quantity value
                                        quantity_text = qt.text
                                        quantity = quantity_text.split(": ")[1]  # Extracts the number after "Quantity: "
                                        quantity = int(quantity) - 1
                                        # Print the quantity
                                        # print(quantity)
                                        flag = True
                                        break
                            elif item_status == "in stock":
                                pass
                            else:
                                quantity = ""
                                break
                            if flag == True:
                                break
                        except:
                            quantity = ""
                            break
                        time.sleep(1)
                Scraping_Data_List_Function(fit_value, color_now, "", stock_status, quantity)
        except:
            Scraping_Data_List_Function(fit_value, color_now, "", "", "")


# In[5]:


def Run_Scrape():
    Fit_selection()


# In[346]:


Run_Scrape()


# In[347]:


# Create a dictionary with the lists as columns
data = {
    'Product Name': p_name,
    'Product Price': p_price,
    'Product Code': p_code,
    'Product Description': p_desc,
    'Product Rating': p_rating,
    'Product Reviews Count': p_reviews,
    '5 Star Count': star_5,
    '4 Star Count': star_4,
    '3 Star Count': star_3,
    '2 Star Count': star_2,
    '1 Star Count': star_1,
    'Colour': colour_list,
    'Fit Type': fit_type_list,
    'Size': size_list,
    'Availability': availability_list,
    'Low Stock Count(If Low Stock Availability)': low_stock_count_list
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('NEXT_Product_Data.xlsx', index=False)

print("Scraping Finished!!!\nExcel File has been created in the same directory.")


# In[ ]:


driver.quit()

