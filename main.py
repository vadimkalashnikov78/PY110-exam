import json
import random

from conf import MODEL
from faker import Faker
fake = Faker()


def get_model() -> str:  # Задание имени модели из файла conf.py
    """

    :return: Model name from conf.py
    """
    return MODEL


def get_title() -> str:
    """

    :return: Title from books.txt
    """
    with open("books.txt", encoding="UTF-8") as f:
        return random.choice([index_.strip() for index_ in f.readlines()])


def get_year() -> int:
    """

    :return:Year of Publishing
    """
    years = int(fake.unique.random_int(min=1900, max=2023))
    return years


def get_pages() -> int:
    """

    :return:Number of pages
    """
    pages = int(fake.unique.random_int(min=1, max=1000))
    return pages


def get_rating() -> float:
    """

    :return: Rating of the book
    """
    rating = round(random.uniform(0.0, 5.0), 1)
    return rating


def get_isbn(book_number: int = 1000) -> str:
    """

    :return: ISBN
    """
    Faker.seed(book_number)
    return fake.isbn13()


def get_price() -> str:
    """


    :return: Price of the book in rubles
    """
    price = str(round(random.uniform(100.0, 5000.00), 2)) + " р."
    return price


"""
def get_authors():
    

  #  :return: Authors of the book
   
    number_of_authors = fake.unique.random_int(min=1, max=3)
    print(number_of_authors)
    authors = []
    for index_ in range(number_of_authors):
        authors.append([str(fake.name())])
    return authors
"""


def book_generator(start_pk: int = 1, book_count: int = 5) -> dict:
    """

    :param start_pk:
    :param book_count:
    :return: Dictionary with books
    """

    pk = start_pk
    for index_ in range(1, book_count + 1):
        book_dict = {
            "model": get_model(),
            "pk": pk,
            "fields": {
                "title": get_title(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn(),
                "rating": get_rating(),
                "price": get_price(),
   #             "authors": get_authors()
            }
        }
        yield book_dict
        pk += 1


# Запуск основного тела программы
if __name__ == '__main__':
  #  print(get_authors())
    books = book_generator(start_pk=1, book_count=100)
    with open("books.json", "w", encoding="UTF-8") as books_write_file:
        json.dump([book for book in books],
                  books_write_file,
                  ensure_ascii=False,
                  indent=4)
