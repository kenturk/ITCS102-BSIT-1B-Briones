import openpyxl
from datetime import datetime

def favperson():
    year = datetime.now().year
    
    records = []
    
    print("--- Favorite People Recorder ---")
    print("Please enter information for 3 favorite person.\n")

    for i in range(1, 4):
        print(f"Person {i}:")
        f_name = input("First Name: ").strip()
        l_name = input("Last Name: ").strip()
        
        while True:
            try:
                b_year_str = input("Birth Year: ").strip()
                b_year = int(birth_year_str)
                if b_year < 1900 or b_year > year:
                    print(f"Please enter a valid birth year between 1900 and {year}.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric year.")

        age = year - b_year

        person_id = i
        
        record = {
            "ID": person_id,
            "First Name": f_name,
            "Last Name": l_name,
            "Birth Year": b_year,
            "Age": age
        }
        records.append(record)
        print() 

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Favorite People"

    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    ws.append(headers)

    for record in records:
        ws.append([
            record["ID"],
            record["First Name"],
            record["Last Name"],
            record["Birth Year"],
            record["Age"]
        ])

    excel_filename = "favorite_people.xlsx"
    wb.save(excel_filename)
    print(f"Data successfully saved to '{excel_filename}'.\n")

    print("=== 𝑺𝒂𝒗𝒆𝒅 𝑹𝒆𝒄𝒐𝒓𝒅𝒔 ===")
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Birth Year':<12} {'Age':<5}")
    print("-" * 55)
    
    for record in records:
        print(f"{record['ID']:<5} {record['First Name']:<15} {record['Last Name']:<15} {record['Birth Year']:<12} {record['Age']:<5}")

favperson()
