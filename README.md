# PlatinumRx Assignment

* This repository contains complete solutions for the PlatinumRx Data Analyst assignment.  
* It covers SQL, Spreadsheet, and Python tasks with clearly documented approaches and clean, production-ready code.

---

## 📁 Project Structure

---

## 1. SQL Solutions 🛢️

### **Hotel Management System – SQL A**
Includes:
- Full schema creation
- Sample data insertion
- 5 analytical queries

**Tasks & Steps Followed**

> **Task 1: Last booked room for every user**
- Created `users` and `bookings` tables per provided schema  
- Used a subquery to fetch the latest booking date per user  
- Joined subquery with `bookings` to retrieve room numbers  
- Joined final result with `users` for user-level reporting  

> **Tasks 2–5: Billing & Ordering Analytics**
- Used date-range filters on `bookings` and `billing`  
- Aggregated totals using `SUM`, grouped by booking or bill ID  
- Applied window functions (`RANK`, `DENSE_RANK`) for:
  - monthly rankings  
  - customer-level spend analysis  
- Ensured queries return empty sets gracefully when no data exists  

---

### **Clinic Management System – SQL B**
Includes:
- Tables for `clinics`, `customer`, `clinic_sales`, `expenses`
- Exact sample data insertion
- 5 analytical queries around revenue, customer value, and profitability

**Steps Followed**

- Computed revenue grouped by sales channel and year  
- Aggregated customer spending to determine top 10 customers  
- Calculated month-wise revenue, expenses, and profit  
- Assigned profitability status using conditional logic (`CASE WHEN`)  
- Used `WITH` clauses + window functions for:
  - ranking clinics by profitability at city/state levels  
- Filtered final results to identify:
  - most profitable clinic  
  - second least profitable clinic  

---

## 2. Spreadsheet Solutions 𝄜

### **Ticket Analysis Workbook**
Includes:
- **Ticket** and **Feedbacks** data sheets  
- `VLOOKUP` implemented for cross-sheet matching  
- Helper columns for time-based calculations  
- Outlet-wise performance summary  

---

## 3. Python Solutions 🐍

### **Scripts Included**
1. **Time Converter**
   - Converts minutes into formatted `X hr Y min`
   - Includes:
     - integer division for hours  
     - remainder logic for minutes  
     - pluralization handling  
     - error handling for invalid inputs  

2. **Duplicate Remover**
   - Removes repeated characters while preserving original order  
   - Steps:
     - initialize empty result string  
     - loop through characters  
     - append only unseen characters  
   - Includes sample test cases  

---

## 🚀 How to Use

### SQL
1. Run `01_*.sql` and `03_*.sql` to create schemas  
2. Run `02_*.sql` and `04_*.sql` for analytical queries  
3. All queries tested on MySQL 

---

### Spreadsheet
```
cd Spreadsheets
```
- Open `Ticket_Analysis.xlsx`  
- Review formulas in **Feedbacks** sheet  
- View compiled analysis in the analysis sheet  

---

### Python
```
cd Python
python 01_Time_Converter.py
python 02_Remove_Duplicates.py
```

Both include:
- Interactive mode  
- Predefined test cases  

---

## 📊 Key Features
- ✅ Detailed comments throughout the code  
- ✅ Error-handled Python scripts  
- ✅ SQL written for performance & clarity  
- ✅ All Excel formulas validated  
- ✅ Covers edge-case handling across all tasks  

---

## ✔️ Tech Stack
- **SQL**: MySQL 
- **Spreadsheet**: Excel / Google Sheets  
- **Python**: 3.6+ compatible  

---

## 📝 Notes
> All solutions are production-ready, optimized, and thoroughly documented.


