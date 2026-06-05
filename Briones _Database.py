import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

# Changing the headers to match the Sports Facility Reservation System
sheet['A1'] = "Reservation ID"
sheet['B1'] = "Customer Name"
sheet['C1'] = "Facility Name"
sheet['D1'] = "Phone"
sheet['E1'] = "Email"
sheet['F1'] = "Membership Type"
sheet['G1'] = "Duration (Hours)"
sheet['H1'] = "Hourly Rate"
sheet['I1'] = "Total Amount"
sheet['J1'] = "Status"
sheet['K1'] = "Reservation Date"

# Make the header text bold
for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
    from openpyxl.styles import Font

sheet[f'{col}1'].font = Font(bold=True)

# Saving it under your database filename
workbook.save("briones_Database.xlsx")