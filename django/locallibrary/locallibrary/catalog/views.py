from django.shortcuts import render
# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
	"""
	Функция отображиения для домашней страницы сайта.
	"""
	# Генерация "количеств" некоторых главных объектов
	num_genre=Genre.objects.all().count()
	num_books=Book.objects.filter(title__icontains='we')
	num_instances=BookInstance.objects.all().count()
	# Доступные книги (статус = 'a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count() # Метод 'all()' применем по умолчанию.

	# Отрисовка HTML-шаблона index.html с данными внутри
	# переменной контекста context
	return render(
		request,
		'index.html',
		context={'num_genre':num_genre,'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
	)

from django.views import generic

class BookListView(generic.ListView):
	model = Book
	contex_object_name = 'my_book_list' # ваше собственное имя переменной контекста в шаблоне
	queryset = Book.objects.filter(title__icontains='war')[:5] # получение 5 книг, содержащих слово 'war' в заголовке
	template_name = 'book/my_arbitrary_template_name_list.html' # определение имени вашего шаблона и его расположения
	