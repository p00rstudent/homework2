from pathlib import Path
from csv import DictReader
import json


def main():
    root = Path(__file__).parent
    books = get_csv_dict(root.joinpath('books.csv'))
    users = load_json(root.joinpath('users.json'))
    users = [modify_user(user) for user in users]
    split_books(users, books)
    dump_users_to_json(root.joinpath('result.json'), users)


def get_csv_dict(path: Path) -> []:
    assert path.is_file() and path.suffix == '.csv', 'Wrong file path'
    with path.open(mode='r') as csv_f:
        return list(DictReader(csv_f))


def load_json(path: Path) -> []:
    assert path.is_file() and path.suffix == '.json', 'Wrong file path'
    with path.open(mode='r') as json_f:
        return json.load(json_f)


def modify_user(user: dict) -> {}:
    return {
        "name": user.get('name', None),
        "gender": user.get('gender', None),
        "address": user.get('address', None),
        "age": user.get('age', None),
        "books": []
    }


def split_books(users: [], books: []) -> []:
    books_count = len(books) // len(users)
    addition_book_counter = len(books) % len(users)
    for user in users:
        for i in range(books_count):
            user['books'].append(books.pop())
        if addition_book_counter > 0:
            user['books'].append(books.pop())
            addition_book_counter -= 1


def dump_users_to_json(path: Path, users: []) -> None:
    with path.open(mode='w') as json_f:
        json.dump(users, json_f, indent=4)


main()
