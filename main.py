from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://learn.senecapolytechnic.ca/ultra/courses/_740746_1/grades")  # Blackboard URL
print("Please log in manually within 30 seconds.")
time.sleep(100) 


grade_rows = driver.find_elements(By.CSS_SELECTOR, "div.student-list-table.is-student-view")

assessment_data = {}

for row in grade_rows:
    try:
        name = row.find_element(By.CSS_SELECTOR, ".element-details .name a").text.strip()
        marks_text = row.find_element(By.CSS_SELECTOR, ".grade-value bdi").text.strip()  # Format: "8 / 10"
        obtained, total = map(float, marks_text.split("/"))
        assessment_data[name] = [obtained, total]
    except:
        continue  # Skip if any part is missing

driver.quit()

# Display extracted data
print("\nExtracted Assessments:")
for name, marks in assessment_data.items():
    print(f"{name}: {marks[0]} / {marks[1]}")

# Step 2: Ask user for weightages
print("\nEnter the weightage (%) for each assessment:")

for name in assessment_data:
    while True:
        try:
            weight = float(input(f"Weightage for '{name}': "))
            assessment_data[name].insert(0, weight)  # Now value = [weightage, obtained, total]
            break
        except ValueError:
            print("Please enter a valid number.")

# Step 3: Calculate course percentage
total_weighted = 0
achieved = 0
deducted = 0
for name, (weight, obtained, maximum) in assessment_data.items():
        if obtained is not None and maximum is not None:
            percent = (obtained / maximum)
            achieved += weight * percent
            deducted += weight * (1 - percent)

# Output
print("\n--- Final Breakdown ---")
print(f"\n--- Final Grade Summary ---")
print(f"✅ Percentage Achieved: {achieved:.2f}%")
print(f"❌ Percentage Deducted: {deducted:.2f}%")
print(f"📊 Yet to be Scored: {100 - (achieved + deducted):.2f}%")
