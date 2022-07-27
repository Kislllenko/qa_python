from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Нельзя добавить одну и ту же книгу дважды.
    def test_add_new_book_adding_existed_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

    # Нельзя выставить рейтинг книге, которой нет в списке.
    def test_set_book_rating_for_not_exist_book(self):
        collector = BooksCollector()

        collector.set_book_rating('Гордость и предубеждение', 6)

        assert collector.get_books_rating() == {}

    # Нельзя выставить рейтинг меньше 1.
    def test_set_book_rating_less_then_one(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', 0)

        assert collector.get_books_with_specific_rating(0) == []

    # Нельзя выставить рейтинг больше 10.
    def test_set_book_rating_more_then_ten(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', 11)

        assert collector.get_books_with_specific_rating(11) == []

    # У не добавленной книги нет рейтинга.
    def test_get_book_rating_for_not_exist_book(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Гордость и предубеждение') is None

    # Добавление книги в избранное.
    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение'] \
               and collector.get_list_of_favorites_books() != ['Что делать, если ваш кот хочет вас убить']

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
    def test_add_book_in_favorites_not_permited_if_book_not_in_books_rating(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Гордость и предубеждение')

        assert collector.get_list_of_favorites_books() == []

    # Проверка удаления книги из избранного.
    def test_delete_book_from_favorites_book_not_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение']
