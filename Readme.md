Payslip Generator
This Python script generates payslips for employees from an Excel file, calculates their net salary, generates PDF payslips, and sends them via email.

Requirements
Before running the script, ensure you have the following:

Python 3.13+ installed.

Required Python packages installed:

pandas

python-dotenv

reportlab

You can install the required packages using pip:

bash
Copy
Edit
pip install pandas python-dotenv reportlab
Google Account for sending emails (If using Gmail for SMTP).

File and Folder Structure
bash
Copy
Edit
Payslip-Generator/
│
├── payslips_generator.py       # The main script for generating payslips and sending emails
├── employees.xlsx              # Excel file with employee data
├── payslips/                   # Folder where generated PDF payslips will be saved
├── .env                        # Environment variables file (for email configuration)
└── README.md                   # This file
Configuration
Create the .env File: In the project directory, create a .env file that will store sensitive email details like your email address and password.

Example .env file:

env
Copy
Edit
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_password
Replace your_email@example.com with your Gmail address and your_email_password with your password (or an App Password if using 2FA).

Enable "Less Secure Apps" on Gmail (for SMTP): If you are using Gmail, you need to enable access for less secure apps:

Go to: https://myaccount.google.com/lesssecureapps

Turn on "Allow less secure apps" (only if using a non-2FA Google account).

If you have two-factor authentication (2FA) enabled, you will need to use an App Password. To generate an app password:

Visit: https://myaccount.google.com/apppasswords

Create an app password for your script.

Important: If you use a non-Google email service, check your provider's documentation for SMTP settings.

How to Run the Script
Prepare the Employee Data: Ensure the employee data is stored in the employees.xlsx file with the following columns:

Employees ID

Name

Emails

Basic Salary

Allowance

Deduction

Example:

Employees ID	Name	Emails	Basic Salary	Allowance	Deduction
101	Jack Dolson	Reecekhalid96@gmail.com	52500	5800	2100
102	Ceilia Rosean	kurangwareece@gmail.com	61500	7200	2500
103	Unami Wills	kupakwashekondo96@gmail.com	57700	6300	2300
104	Diana Price	Reecekondo96@gmail.com	63500	6800	2450
Run the Script: Open a terminal or command prompt, navigate to the project directory, and execute the following command:

bash
Copy
Edit
python payslips_generator.py
Script Output:

The script will process the employee data from employees.xlsx.

It will calculate the net salary for each employee.

Payslips will be generated as PDF files in the payslips/ directory.

Emails with the corresponding payslips will be sent to each employee.

Example output in the terminal:

pgsql
Copy
Edit
✅ Payslip sent to Reecekhalid96@gmail.com
✅ Payslip sent to kurangwareece@gmail.com
✅ Payslip sent to kupakwashekondo96@gmail.com
✅ Payslip sent to Reecekondo96@gmail.com
✅ Payslips have been generated and emailed to all employees.
Troubleshooting
1. Authentication Errors:
If you encounter an authentication error (e.g., "Username and Password not accepted"), check the following:

Ensure your email and password are correct in the .env file.

If using Gmail, ensure that "Less Secure Apps" is enabled, or use an App Password if you have 2FA enabled.

Check for any account security alerts on your email provider's website.

2. Missing Excel File:
Make sure the employees.xlsx file is in the same directory as the script. The script will look for this file and load the employee data.

License
This project is licensed under the MIT License - see the LICENSE file for details.