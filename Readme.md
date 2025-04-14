# 🧾 Python Programming Assignment: Payslip Generator

---

## 📌 **Project Overview**
This project is a **Python-based Payslip Generator** designed to automate the creation of employee payslips in PDF format. It reads employee data from an Excel file, calculates net salaries, and generates professional payslips for each employee.

---

## ✨ **Features**
- **Automated Payslip Generation**  
  Generates PDF payslips with employee details: name, email, basic salary, allowances, deductions, and net salary.

- **Customizable Design**  
  Includes company logo, header, and footer for a professional appearance.

- **Error Handling**  
  Gracefully manages missing files, invalid formats, and other common issues.

- **Selective Printing**  
  Filter and print specific employee payslips based on criteria.

- **Environment Variables**  
  Uses `.env` files to securely store email credentials.

---

## 🧰 **Requirements**
### **Software**
- **Python 3.7 or higher**

### **Python Libraries**
- `pandas`
- `reportlab`
- `python-dotenv`

### **Input File**
- **Excel File**: `employees.xlsx` with the following columns:
  - `name`
  - `email`
  - `basic_salary`
  - `allowance`
  - `deduction`

---

## ⚙️ **Setup Instructions**
### **1. Clone the Repository**
```bash
git clone https://github.com/Ocean-67/payslip-generator.git
cd payslip-generator
```

### **2. Install Required Libraries**
```bash
pip install -r requirements.txt
```

### **3. Configure the `.env` File**
Create a `.env` file in the project root and add your email credentials:
```plaintext
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password
```

### **4. Prepare the Excel File**
Ensure `employees.xlsx` is in the project root and has the required columns.

### **5. Run the Script**
```bash
python payslips_generator.py
```

---

## 🔍 **How It Works**
1. **Reads Employee Data**  
   The script reads employee information from `employees.xlsx`.

2. **Calculates Net Salary**  
   Formula:  
   ```plaintext
   net_salary = basic_salary + allowance - deduction
   ```

3. **Generates Payslips**  
   Produces a PDF file for each employee with their personal and salary details.

4. **Filters Desired Payslips**  
   Prints only the payslips listed in the `desired_payslips` list.

---

## 📁 **File Structure**
```plaintext
📂 Python Programming Assignment - Payslip Generator
├── payslips_generator.py    # Main script
├── employees.xlsx           # Employee data file
├── bfxcc_logo.png           # Company logo
├── .env                     # Email credentials
├── payslips/                # Generated PDF payslips
└── README.md                # Project documentation
```

---

## 🧾 **Sample Output**
A generated payslip includes:
- Employee Name
- Email Address
- Basic Salary
- Allowances
- Deductions
- Net Salary
- Company Logo, Header, and Footer

---

## ⚠️ **Error Handling**
- **Missing Files**  
  Shows an error if `employees.xlsx` or `bfxcc_logo.png` is not found.

- **Invalid Data**  
  Checks for missing or incorrect columns in the Excel file.

- **Email Configuration**  
  Validates that email credentials are set correctly in the `.env` file.

---

## 🤝 **Contributing**
Contributions are welcome!  
Feel free to fork the repository and submit a pull request.

---

## 📜 **License**
This project is licensed under the MIT License.  
See the LICENSE file for more information.

---

## 📬 **Contact**
- **Name**: BFXCC  
- **Email**: a-z@gmail.com