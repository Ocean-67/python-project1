import os
import smtplib
import pandas as pd
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import glob
from reportlab.lib.utils import ImageReader

# List all files in the current directory
print("All files in current directory:")
for file in os.listdir():
    print(file)

# Load environment variables
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER", "sibandaaartii@gmail.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "kaxi gjct ulic ogaw")

# Verify email credentials
print("Loaded email:", EMAIL_USER)
if not EMAIL_USER or not EMAIL_PASS:
    print("❌ ERROR: Please set the EMAIL_USER and EMAIL_PASS environment variables.")
    exit(1)

# Read employee data
try:
    df = pd.read_excel("employees.xlsx")
except FileNotFoundError:
    print("❌ ERROR: The file 'employees.xlsx' was not found.")
    exit()

# Print actual column names for debugging
print("\nOriginal columns from Excel:")
print(df.columns.tolist())

# Clean column names: lowercase, replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df.rename(columns={'emails': 'email', 'alowance': 'allowance'}, inplace=True)

print("\nSanitized column names:")
print(df.columns.tolist())

# Filter only the required columns
required_columns = ['email', 'basic_salary', 'allowance', 'deduction']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(f"❌ ERROR: Missing required columns in the Excel file: {missing_columns}")
    exit()

df = df[required_columns]

# Calculate net salary
try:
    df["net_salary"] = df["basic_salary"] + df["allowance"] - df["deduction"]
except KeyError as e:
    print(f"❌ ERROR: Missing column in the Excel file: {e}")
    exit()

print("\nEmployee Data with Net Salary:")
print(df)

# Function to generate PDF payslip
def generate_payslip(employee):
    email_str = str(employee.email)
    filename = f"payslips/{email_str.replace(' ', '_')}_payslip.pdf"

    os.makedirs("payslips", exist_ok=True)
    c = canvas.Canvas(filename, pagesize=letter)

    # Logo path
    logo_path = "bfxcc_logo.png"
    try:
        logo = ImageReader(logo_path)
        c.drawImage(logo, 50, 700, width=60, height=60, mask='auto')
    except Exception as e:
        print(f"⚠️ WARNING: Could not load logo from {logo_path}. Skipping logo.")

    # Company Header
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.darkblue)
    c.drawString(120, 740, "BFXCC")
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.gray)
    c.drawString(120, 725, "Background Foundation of Creation Century")

    # Horizontal Line
    c.setStrokeColor(colors.grey)
    c.setLineWidth(0.5)
    c.line(50, 710, 550, 710)

    # Address & Date
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.black)
    c.drawString(50, 695, "52, Jalan Awan Hijau, 58200 Harare, Zimbabwe")
    c.drawRightString(550, 695, f"Date: {pd.Timestamp.now().strftime('%d-%m-%Y')}")

    # Payslip Content Box
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(45, 450, 510, 220, stroke=1, fill=0)

    # Employee Details
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(50, 660, "Employee Payslip")

    c.setFont("Helvetica", 11)
    c.drawString(60, 615, f"Email:")
    c.drawString(200, 615, f"{email_str}")

    c.drawString(60, 590, "Basic Salary:")
    c.drawString(200, 590, f"${employee.basic_salary:,.2f}")

    c.drawString(60, 565, "Allowances:")
    c.drawString(200, 565, f"${employee.allowance:,.2f}")

    c.drawString(60, 540, "Deductions:")
    c.drawString(200, 540, f"${employee.deduction:,.2f}")

    c.setFont("Helvetica-Bold", 11)
    c.drawString(60, 510, "Net Salary:")
    c.drawString(200, 510, f"${employee.net_salary:,.2f}")

    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(colors.gray)
    c.drawString(50, 100, "Payslip generated automatically. Contact HR for queries.")
    c.line(50, 120, 550, 120)

    c.save()
    return filename

# Generate and send payslips
for _, employee in df.iterrows():
    pdf_file = generate_payslip(employee)
    print(f"✅ Payslip generated: {pdf_file}")

# List all generated PDF files
payslip_files = glob.glob("payslips/*.pdf")

# Specify the exact payslips to print
desired_payslips = [
    "payslips/kupakwashekondo96@gmail.com_payslip.pdf",
    "payslips/kurangwareece@gmail.com_payslip.pdf",
    "payslips/Reecekhalid96@gmail.com_payslip.pdf",
    "payslips/Reecekondo96@gmail.com_payslip.pdf"
]

# Filter and print only the desired payslips
print("\nGenerated Payslip Files:")
for file in payslip_files:
    if file in desired_payslips:
        print(f"📄 {file}")

print("✅ Payslips have been generated.")






