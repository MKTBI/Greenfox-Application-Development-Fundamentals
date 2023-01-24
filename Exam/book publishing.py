'''Book publishing

Your task is to create a program to model some processes of a book publisher company.


BookPublisher
has a name

can publish given books

can show the published books (products): print all the published books after each other


A publisher can publish different types of books:


Fiction
can be created by its title, description and price

is represented in the following format:
«title» - «price»
«description»


Dictionary
can be created by the source language, the target language and the price

translations can be added later to it

a translation is a tuple with values: («word in source language», «word in target language»)

new dictionaries can be automatically generated from existing ones. For example if we have an English-Hungarian and an English-Russian dictionary, we should be able to generate a Hungarian-Russian dictionary by merging the common elements from the existing dictionaries. The price of the generated dictionary should be the price of the cheaper dictionary we use for generation.

is represented in the following format (after the first line, all the translations should appear in new lines):
«source» - «target» dictionary - «price»$
«word in source language» - «word in target language»


Tests
Write at least 2 unit tests to your dictionary merger function.


Sample code to run
Using your solution, the following code should run without errors and print the expected results.


english_hungarian = Dictionary('English', 'Hungarian', 5)
english_hungarian.add_translation(('apple', 'alma'), ('table', 'asztal'), ('dog', 'kutya'))
english_russian = Dictionary('English', 'Russian', 8)
english_russian.add_translation(('apple', 'яблоко'), ('table', 'стол'), ('cat', 'кошка'))
hungarian_russian = Dictionary.merge(english_hungarian, english_russian)
fiction = Fiction('Nineteen Eighty-Four', 'A science fiction novel by English novelist George Orwell', 10)
golden_books = BookPublisher('Golden Books')
golden_books.publish(english_hungarian, english_russian, hungarian_russian, fiction)
golden_books.show_products() # should print:
# English - Hungarian dictionary - 5$
# apple - alma
# table - asztal
# dog - kutya
#
# English - Russian dictionary - 8$
# apple - яблоко
# table - стол
# cat - кошка
#
# Hungarian - Russian dictionary - 5$
# alma - яблоко
# asztal - стол
#
# Nineteen Eighty-Four - 10$
# A science fiction novel by English novelist George Orwell'''

class BookPublisher:
    def __init__(self, name):
        self.name = name
        self.products = []

    def publish(self, *books):
        self.products.extend(books)

    def show_products(self):
        for product in self.products:
            print(product)

class Fiction:
    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price

    def __str__(self):
        return '{} - {}$\n{}'.format(self.title, self.price, self.description)

class Dictionary:
    def __init__(self, source, target, price):
        self.source = source
        self.target = target
        self.price = price
        self.translations = {}

    def add_translation(self, *translations):
        for translation in translations:
            self.translations[translation[0]] = translation[1]

    def __str__(self):
        translations = '\n'.join('{} - {}'.format(k, v) for k, v in self.translations.items())
        return '{} - {} dictionary - {}$\n{}'.format(self.source, self.target, self.price, translations)

    @classmethod
    def merge(cls, dict1, dict2):
        if dict1.source == dict2.target:
            source, target = dict1.source, dict2.target
            price = min(dict1.price, dict2.price)
        elif dict1.target == dict2.source:
            source, target = dict2.source, dict1.target
            price = min(dict1.price, dict2.price)
        else:
            raise ValueError('Cannot merge dictionaries')

        merged_dict = cls(source, target, price)
        for word, translation in dict1.translations.items():
            if word in dict2.translations:
                merged_dict.add_translation((word, dict2.translations[word]))
        return merged_dict

# Unit tests for the merge() method
def test_dictionary_merge():
    eng_hun = Dictionary('English', 'Hungarian', 5)
    eng_hun.add_translation(('apple', 'alma'))
    eng_rus = Dictionary('English', 'Russian', 8)
    eng_rus.add_translation(('apple', 'яблоко'))
    hun_rus = Dictionary.merge(eng_hun, eng_rus)
    assert hun_rus.translations == {'apple': 'яблоко'}
    assert hun_rus.price == 5
    assert hun_rus.source == 'Hungarian'
    assert hun_rus.target == 'Russian'

    eng_hun = Dictionary('English', 'Hungarian', 5)
    eng_hun.add_translation(('apple', 'alma'))
    eng_rus = Dictionary('English', 'Russian', 8)
    eng_rus.add_translation(('table', 'стол'))
    hun_rus = Dictionary.mer
