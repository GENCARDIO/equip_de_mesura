import pandas as pd


def llegir_excel(path_excel):
    path_excel = "/home/gencardio/Baixades/LDG_REG_202_INVENTARI APARELLS_V6.xlsx"
    data = pd.read_excel(path_excel, skiprows=4)
    filas = data.to_numpy().tolist()
    return filas
