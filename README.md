# Next-Scraper
**Scrapes Next (Fashion Based Website) Product data**


![Next_Scraper_Running_Demo-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/71a8af07-5b70-4990-a3f6-cd49e22c104b)

## **How to Run the Script**  

1. **Download the Files**  
    - Download the `.py` script into a local folder.  
    - Download the `requirements.txt` file into the **same folder** as the `.py` script.  

2. **Ensure Python is Installed**  
    - Make sure you have Python installed on your system.  
    - Verify that the Python executable path is added to your system's **Environment Variables**.  

3. **Install Required Dependencies**  
    - Open your terminal or command prompt in the directory containing the `.py` and `requirements.txt` files.  
    - Run the following command to install the required dependencies:  
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Script**  
    - In the same terminal, run the script using:  
    ```bash
    python <name_of_file>.py
    ```

5. **Important Notes**  
    - The terminal will prompt you to either choose a new URL or use the sample URL provided.  
    - Keep the browser **in the foreground at all times** from the start of the script. This is necessary for Selenium to perform clicks without issues.  
    - The script will take some time to scrape all variations.  
    - Once completed, the data will be saved in an Excel file in the same folder.  
    - **If the Selenium-based browser fails to load:**  
      - Download the latest chromedriver that matches your Google Chrome version from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).  
      - Place the downloaded `chromedriver.exe` in the **same folder** as the `.py` file.   

---

## **Next Steps and Improvements**  

### 1. **Optimization and Performance Enhancements**  
- **Multithreading:** In Future, Introduce multithreading to concurrently scrape multiple product variations, reducing overall execution time.  
- **Headless Browser or Alternative Libraries:**  
  - In Future, Run the browser in headless mode for faster execution and reduced resource usage.  
  - In Future, Explore other libraries like Playwright for more efficient rendering and interaction with JavaScript-heavy content.     

### 2. **Scalability and Maintainability**  
- In Future, Implement logging for better monitoring and debugging.  

---

## **Challenges**  
### 1. **Quantity Limit After 9**  
- **Challenge:** The website does not allow adding more than 9 units directly through the UI, limiting the ability to determine accurate stock levels for high-quantity items. Currently, the scraper effectively handles low stock scenarios but is limited by the UI constraint of not displaying quantities above 9 so stock quantity is undetermined except for the Low Stock Products.  

### 2. **Foreground Requirement for Selenium**  
- **Challenge:** Selenium requires the browser to be in the foreground for interactions, especially with JavaScript-rendered content. When minimized, clicks may fail or data may be empty.  

### 3. **No Blockers Encountered (Anti-Detection Measures)**  
- Leveraged **undetected chromedriver** to bypass bot detection without issues.  
- If detection issues arise in the future, rotating residential proxies will be integrated to change the IP address with each request.  

---

## **Criteria Fulfillment**  
- The solution is robust as long as the website's structure remains consistent. If changes occur, minor adjustments or additions to element locators may be needed.  

---

## **Tools and Technologies Used**  
- **Python**  
- **Selenium**  
- **Undetected Chromedriver** (for bypassing bot detection)  

---

## **Usage Notes**  
- Keep the browser window in the foreground during execution to avoid interaction issues.  
---

**Need Help?**  
    If you have any questions or face issues while running the script, feel free to reach out to:  
    - **Muhammad Qasim Khan**  
    - Email: kmqasim055@gmail.com
