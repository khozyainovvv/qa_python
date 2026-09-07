import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    #def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
       # collector = BooksCollector()

        # добавляем две книги
      #  collector.add_new_book('Гордость и предубеждение и зомби')
      #  collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
       # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('invalid_name', [''])
    def test_add_new_book_invalid_names(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_books_for_children_excludes_age_rating(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', genre)
        children_books = collector.get_books_for_children()
        assert 'Страшная книга' not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert 'Шерлок Холмс' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        collector.add_book_in_favorites('Анна Каренина')
        collector.delete_book_from_favorites('Анна Каренина')
        assert 'Анна Каренина' not in collector.get_list_of_favorites_books()

    def test_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == ''

    @pytest.mark.parametrize('book_name', ['Гарри Поттер', 'A', 'A' * 40])
    def test_add_new_book_valid_names(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('invalid_name', ['', 'A' * 41])
    def test_add_new_book_invalid_names_too_long(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert collector.get_book_genre(invalid_name) is None

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин Колец')
        collector.set_book_genre('Властелин Колец', 'Фантастика')
        assert collector.get_book_genre('Властелин Колец') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Хоббит' in books
