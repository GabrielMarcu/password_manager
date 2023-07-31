import csv


def append(path: str, col1: str, col2: str, col3: str, col4: str) -> None:
    """
    Appends row to database(csv file)
    :param path: Path to csv file
    :param col1: Column 1 in csv file
    :param col2: Column 2 in csv file
    :param col3: Column 3 in csv file
    :param col4: Column 4 in csv file
    :return: None
    """
    with open(path, 'a', newline='') as file_a:
        writer = csv.writer(file_a)
        writer.writerow([col1, col2, col3, col4])


def read(path):
    """
    Creates a list with the elements of the cvs file
    :return: List of rows from cvs file
    """
    with open(path, 'r', newline='') as file_r:
        reader = csv.reader(file_r)
        list_reader = list(reader)
        return list_reader

def create(path: str):
    """
    Creates or overwrites a csv file with hardcoded fieldnames Username, Password, Name, Email
    :return: None
    """
    with open(path, 'w', newline='') as fw:
        writer = csv.writer(fw)
        writer.writerow(['Username', 'Password', 'Name', 'Email'])
