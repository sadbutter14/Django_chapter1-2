from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm


def post_share():
    ...


class PostListView(ListView):  # аналог post_list()
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 1)  # По 1 статье на каждой странице.
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # Если страница не является целым числом, возвращаем первую страницу.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    return render(request, 'blog/post/post.html', {'post': post})
