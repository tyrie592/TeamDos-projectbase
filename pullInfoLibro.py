import gspread as gs

# import pandas as pd

gc = gs.service_account(filename='/Users/jose.pacheco/Downloads/service_account.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1pnRSgaBcBgoFdBhrqd8OSZPONth1_oC37hCftr3aFPg/edit?usp'
                    '=sharing')


# Previous version, 0.1
# sh = gc.open("LIBROS")
# ws = sh.worksheet('ZAPAS')
# df = pd.DataFrame(ws.get_all_records())
# df.head()

# Previous version, 0.2
# wks = sh.worksheet("ZAPAS")
# print(wks.get_all_records())

class pull_info_action2:
    id = 2
    wks = sh.worksheet("LIBROS")
    print(wks.get_all_records())
