import gspread

gc = gspread.service_account(filename="E:\Programming\credentials.json")

sh = gc.open("Project CMS Main Server")


second_sheet =sh.worksheet("test")
print(second_sheet.get("A1"))
# print(sh.sheet1.get('G4'))