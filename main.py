import pandas as pd


def read_excel(file_name):
    df = pd.read_excel(f"{file_name}.xlsx")
    return df


def change_column(column):
    half_side = lambda x: f"{x[:min(len(x), 12)]}{'0' * (12 - min(len(x), 12))}"
    for i in range(len(column)):
        items = column.iloc[i].split(", ")
        if len(items) != 2:
            raise ZeroDivisionError
        column.iloc[i] = f"{half_side(items[0])}, {half_side(items[1])}"
    return column

def main():
    file_name="Dzerzhinskogo_Lobachevskogo_Karla_Marxa_Lobachevskogo_1"
    df = pd.read_excel(f"{file_name}.xlsx")
    print(change_column(df["Местоположение"]))

if __name__ == '__main__':
    main()


# See PyCharm help at
