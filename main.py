import os

import pandas as pd


def save_as_csv(to_save: list[list[str]], columns: list[str], relpath: str) -> None:
    df = pd.DataFrame(to_save, columns=columns)
    df.to_csv(relpath, sep=";")
    print(f'Successfully saved in {relpath}')


def scan_dataset(folder_paths: list[str]) -> list[list[str]]:
    result = []
    for folder in folder_paths:
        item_class = folder.split('\\')[-1]
        for name in os.listdir(folder):
            result.append([os.path.abspath(folder + '\\' + name), f'{folder}\\{name}', item_class])
    return result


if __name__ == "__main__":
    rel_path1 = r'dataset\bay horse'
    rel_path2 = r'dataset\zebra'

    columns = ["Absolute path", "Relative path", "Class"]
    data = scan_dataset([rel_path1, rel_path2])
    save_as_csv(data, columns, 'annotation.csv')


    