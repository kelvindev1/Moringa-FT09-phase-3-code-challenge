import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_author_instance(self):
        author = Author(1, 'Jane Doe')
        assert author.id == 1
        assert author.name == 'Jane Doe'

    def test_author_save(self):
        author = Author(name='John Doe')
        author.save()
        assert author.id is not None

    def test_article_instance(self):
        article = Article(id=1, title='New Article', content='Article Content', author_id=1, magazine_id=1)
        assert article.id == 1
        assert article.title == 'New Article'
        assert article.content == 'Article Content'
        assert article.author_id == 1
        assert article.magazine_id == 1


    def test_create_magazine(self):
        magazine = Magazine(name='Test Mag', category='Test Category')
        assert magazine.name == 'Test Mag'
        assert magazine.category == 'Test Category'
        assert magazine.id is None

    def test_set_id(self):
        magazine = Magazine(name='Test Mag', category='Test Category')
        magazine.id = 1
        assert magazine.id == 1

    def test_save_new_magazine(self):
        magazine = Magazine(name='New Mag', category='New Category')
        magazine.save()
        assert isinstance(magazine.id, int)

    def test_create_author(self):
        author = Author(name='John Doe')
        assert author.name == 'John Doe'
        assert author.id is None



if __name__ == "__main__":
    unittest.main()
