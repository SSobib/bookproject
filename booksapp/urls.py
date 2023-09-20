from django.urls import path
from .import views

app_name = 'booksapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),  # Home View
    path('country_list', views.CountryCreateView.as_view(), name='country_create'),  # Country View
    path('country_create', views.CountryListView.as_view(), name='country_list'),  # Country View
    path('country_update/<int:pk>', views.CountryUpdateView.as_view(), name='country_update'),  # Country View

    path('language_list', views.LanguageListView.as_view(), name='language_list'),  # Country View
    path('language_create', views.LanguageCreateView.as_view(), name='language_create'),  # Country View
    path('language_update/<int:pk>', views.LanguageUpdateView.as_view(), name='language_update'),  # Country View

    path('author_list', views.AuthorListView.as_view(), name='author_list'),  # Country View
    path('author_create', views.AuthorCreateView.as_view(), name='author_create'),  # Country View
    path('author_update/<int:pk>', views.AuthorUpdateView.as_view(), name='author_update'),  # Country View

    path('book_list', views.BookListView.as_view(), name='book_list'),  # Country View
    path('book_create', views.BookCreateView.as_view(), name='book_create'),  # Country View
    path('book_update/<int:pk>', views.BookUpdateView.as_view(), name='book_update'),  # Country View
]