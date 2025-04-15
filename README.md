# 📊 Blackboard Grade Calculator (Seneca Edition)

Tired of professors disabling the **"View Current Grade"** feature on Blackboard?  
Manually calculating your grades every time is frustrating — so here’s a simple Selenium script to make it easier!

This script helps you quickly extract and calculate your **current grade** from any course's Gradebook on Seneca’s Blackboard.

---

## ⚙️ How It Works

Once the script is launched:

1. A browser window will open automatically.
2. **Manually log in** to [Blackboard](https://learn.senecacollege.ca/) with your Seneca credentials.
3. Navigate to the **Gradebook** of the course you want to check. Your screen should like like this. You have 100 seconds to log in and open grades webpage. Feel free to increase/decrease it as needed.
   
  ![image](https://github.com/user-attachments/assets/e5cb1de1-fab5-41d9-97e9-7f3cf4e39e98)

5. The script will fetch and calculate your current grade based on the visible entries.

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://https://github.com/gurmehakkaur/SenecaGradeCalc
```
### 2. Download dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the script
```bash
python main.py
```
