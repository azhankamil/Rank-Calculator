import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium webdriver (make sure you have installed the appropriate browser driver)
driver = webdriver.Chrome()  # Change this line if you're using a different browser driver

i=0

while i<=66:

    # Navigate to the website
    driver.get("https://ctengg.amu.ac.in/web/st_result001.php?prog=btech")  # Replace with the actual URL of the website

    # Read input values from CSV file
    csv_filename = "Electrical.csv"  # Replace with the actual filename of your CSV file
    with open(csv_filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        input_data = list(reader)


    # Find the input fields and the submit button
    input1 = driver.find_element(By.ID, "facno_input")  # Replace "input1_id" with the actual ID of the first input field
    input2 = driver.find_element(By.ID, "eno_input")  # Replace "input2_id" with the actual ID of the second input field
    submit_button = driver.find_element(By.ID, "att_submit")  # Replace "submit_button_id" with the actual ID of the submit button

    input1_value = input_data[i][0]  # Assuming the first column of the first row contains the value for input1
    input2_value = input_data[i][1]  # Assuming the second column of the first row contains the value for input2
    input1.send_keys(input1_value)
    input2.send_keys(input2_value)
    i=i+1

    # # Enter the inputs into the fields
    # input1.send_keys("20cob306")  # Replace "Input 1 value" with the actual value you want to enter in the first field
    # input2.send_keys("gj8915")  # Replace "Input 2 value" with the actual value you want to enter in the second field

    # Click the submit button
    submit_button.click()

    # Wait for the page to load after submitting
    # Replace "10" with the number of seconds you want to wait for the page to load
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.presence_of_element_located((By.ID, "myModal"))) # Replace "Success" with a string that indicates the page has loaded successfully


    table = driver.find_element(By.XPATH, "//table[@style='width:100%;text-align:center;']")

    # Extract the data from the table
    data_rows = table.find_elements(By.TAG_NAME, "tr")  # Find all rows in the table
    data = []  # Store the extracted data
    for row in data_rows:
        cells = row.find_elements(By.TAG_NAME, "td")  # Find all cells in the row
        row_data = [cell.text for cell in cells]  # Extract the text from each cell
        data.append(row_data)

        print(data)
        print(row_data)

    # Write the data to a CSV file
    csv_filename = "result_electrical.csv"  # Replace with the desired filename for the CSV file
    with open(csv_filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row_data in data:
            writer.writerow(row_data)
    data.clear()

# Close the browser
driver.quit()