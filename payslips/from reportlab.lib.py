from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import inch
from reportlab.platypus import Image
import os

def generate_payslip(employee):
    # Ensure that 'name' is a string, even if it's not
    name_str = str(employee.name)
    filename = f"payslips/{name_str.replace(' ', '_')}_payslip.pdf"
    
    # Create directory for saving payslips if it doesn't exist
    os.makedirs("payslips", exist_ok=True)

    # Create a PDF canvas
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Add the company logo
    logo_path = "logo.png"  # Replace with the actual path to your logo file
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 50, 730, width=50, height=50)  # Adjust size and position as needed
    else:
        print("❌ Logo file not found. Skipping logo.")

    # Set up the title (Company name, payslip title)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(120, 750, "Background Foundation Of Creation Century")
    c.setFont("Helvetica", 10)
    c.drawString(50, 730, "52, Jalan Awan Hijau, 58200 Kuala Lumpur, Malaysia")
    c.drawString(450, 730, "Date: 03-03-2025")
    
    # Employee details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 700, f"Name: {name_str}")
    c.drawString(50, 685, f"Employee ID: {employee.employees_id}")
    c.drawString(50, 670, f"Email: {employee.emails}")
    c.drawString(450, 700, "Payslip for: February, 2025")
    c.drawString(450, 685, "Staff No: 058")
    
    # Draw a line to separate the header
    c.line(50, 660, 550, 660)
    
    # Salary breakdown table
    data = [
        ["EARNINGS", "CURRENT (RM)", "DEDUCTIONS", "CURRENT (RM)"],
        ["Basic Pay", f"{employee.basic_salary:,.2f}", "Employee EPF", "275.00"],
        ["Gross Total", f"{employee.basic_salary:,.2f}", "Employee SOCSO", "12.25"],
        ["", "", "Total Deductions", "287.25"],
        ["", "", "", ""],
        ["NETT PAY", f"{employee.net_salary:,.2f}", "", ""]
    ]
    
    table = Table(data, colWidths=[150, 100, 150, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('SPAN', (0, 5), (2, 5)),  # Merge cells for "NETT PAY"
        ('ALIGN', (1, 5), (1, 5), 'RIGHT'),
        ('FONTNAME', (0, 5), (0, 5), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 5), (0, 5), 12),
    ]))
    
    # Draw the table
    table.wrapOn(c, 50, 400)
    table.drawOn(c, 50, 400)
    
    # Footer
    c.setFont("Helvetica", 8)
    c.drawString(50, 100, "Medical Leave = 1, Balance = 9")
    c.drawString(50, 85, "Annual Leave = 3, Balance = 17")
    
    # Save the PDF
    c.save()
    
    return filename