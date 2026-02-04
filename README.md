# FastBox-Delivery-System
Python delivery simulation project

##  Project Overview

The **FastBox Mystery Delivery System** is a Python-based simulation project that models a real-world delivery operation.
The system manages **warehouses**, **delivery agents**, and **packages**, and simulates how packages are delivered efficiently.

The project focuses on:

* Assigning each package to the **nearest delivery agent**
* Calculating the **total distance traveled** by each agent
* Measuring **agent efficiency**
* Identifying the **best (most efficient) delivery agent**

---

##  Problem Statement

FastBox is a delivery company with:

* Multiple warehouses
* Multiple delivery agents
* Packages that must be delivered from warehouses to destinations

### Objective:

* Assign packages to the closest available agent
* Simulate the delivery journey
* Calculate efficiency for each agent
* Select the **Best Agent** based on minimum average distance traveled per package

---

## 🗂️ Project Structure

```
FastBox-Delivery-System
│
├── Delivery.py
├── README.md
├── FastBox_Delivery_System_Assignment.pdf
└── test_cases
    ├── test_case_1.json
    ├── test_case_1_report.json
    ├── test_case_2.json
    ├── test_case_2_report.json
    └── ...
```

---

## Input Format (JSON)

Each test case is provided as a JSON file containing:

* **warehouses** → warehouse IDs and coordinates
* **agents** → agent IDs and coordinates
* **packages** → warehouse reference and destination coordinates

### Sample Input:

```json
{
  "warehouses": {
    "W1": [0, 0]
  },
  "agents": {
    "A1": [5, 5]
  },
  "packages": [
    {
      "id": "P1",
      "warehouse": "W1",
      "destination": [10, 10]
    }
  ]
}
```

---

## Distance Calculation

The project uses the **Euclidean distance formula**:

```
distance = √((x2 - x1)² + (y2 - y1)²)
```

---

## How to Run the Project

### Step 1: Navigate to the project directory

```powershell
cd "C:\Users\pushpa\Downloads\Python Assignment -2026"
```

### Step 2: Run the script with a test case

```powershell
python Delivery.py test_cases/test_case_1.json
```

### Successful Execution Output:

```
test_cases/test_case_1.json processed → test_cases/test_case_1_report.json
```

---

##Output Format (Report JSON)

For each delivery agent, the output report includes:

* Number of packages delivered
* Total distance traveled
* Efficiency score

Additionally, the report specifies:
best_agent

### Sample Output:

```json
{
  "A1": {
    "packages_delivered": 2,
    "total_distance": 85.4,
    "efficiency": 42.7
  },
  "best_agent": "A1"
}
```

=>Best Agent Selection Logic

Efficiency = Total Distance / Packages Delivered
The agent with the 'lowest efficiency value' is considered the 'Best Agent'.


=>Technologies Used

* Python 3.11
* JSON
* Command-line arguments (`sys.argv`)
* File handling


Author

Pushpalatha Menda
Python | SQL | AWS | Aspiring Data Engineer




