from django.urls import path
# from watchlist_app.api import views
from watchlist_app.api.views import MovieListAV, MovieDetailAV


urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
    # path('list/', views.movie_list, name='movie-list'),
    # path('<int:pk>', views.movie_details, name='movie-detail'),

]
