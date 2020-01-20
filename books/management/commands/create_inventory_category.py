from django.core.management.base import BaseCommand

from books.models import Category


class Command(BaseCommand):
    args = '';
    help = 'For insert data in Category model'

    def insert_category_data(self):
        try:
            if Category.objects.all().count() > 0:
                return "Data has already exists in db"
        except:
            pass
        categories = [Category(name=category) for category in ['Action and adventure',
                                                               'Art',
                                                               'Autobiography',
                                                               'Anthology',
                                                               'Biography',
                                                               'Children',
                                                               'Cookbook',
                                                               'Comic book',
                                                               'Diary',
                                                               'Crime',
                                                               'Encyclopedia',
                                                               'Drama',
                                                               'Guide',
                                                               'Fairytale',
                                                               'Health',
                                                               'Fantasy',
                                                               'History',
                                                               'Graphic novel',
                                                               'Journal',
                                                               'Horror',
                                                               'Memoir',
                                                               'Mystery',
                                                               'Prayer',
                                                               'Paranormal',
                                                               'Religion',
                                                               'Picture book',
                                                               'Textbook',
                                                               'Poetry',
                                                               'Review',
                                                               'Political thriller',
                                                               'Science',
                                                               'Romance',
                                                               'Satire',
                                                               'Travel',
                                                               'Science fiction',
                                                               'True crime',
                                                               'Short story',
                                                               'Suspense',
                                                               'Thriller',
                                                               'Young adult', ]]
        Category.objects.bulk_create(categories)

    def handle(self, *args, **options):
        self.insert_category_data()
        print('data inserted')