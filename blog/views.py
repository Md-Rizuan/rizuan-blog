from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.contrib import messages

from user_profile.models import User

from .models import (
    Blog,
    Tag,
    Category,
    Comment,
    Reply,
    District,
    Thana,
    
)
from .forms import TextForm, AddBlogForm

def home(request):
    blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    context = {
        "blogs":blogs,
        "tags": tags,
    }
    return render(request, 'home.html', context)

def blogs(request):
     queryset = Blog.objects.order_by('-created_date')
     tags = Tag.objects.order_by('-created_date')
     page = request.GET.get('page', 1)
     paginator = Paginator(queryset, 2)
     all_blogs = Blog.objects.order_by('-created_date')[:5]
     try:
          blogs = paginator.page(page)
     except EmptyPage:
          blogs = paginator.page(1)
     except PageNotAnInteger:
          blogs = paginator.page(1)

     context = {
        "blogs":blogs,
        "tags": tags,
        "all_blogs" : all_blogs
    }
     return render(request, 'blogs.html', context)

def category_blogs(request, slug):
     category = get_object_or_404(Category, slug=slug)
     queryset = category.category_blogs.all()
     tags = Tag.objects.order_by('-created_date')[:5]
     page = request.GET.get('page', 1)
     paginator = Paginator(queryset, 2)
     all_blogs = Blog.objects.order_by('-created_date')[:5]
     try:
          blogs = paginator.page(page)
     except EmptyPage:
          blogs = paginator.page(1)
     except PageNotAnInteger:
          blogs = paginator.page(1)
     context = {
          "blogs": blogs,
          "tags":tags,
          "all_blogs": all_blogs
     }
     return render(request, 'category_blogs.html', context)

def tag_blogs(request, slug):
     tag = get_object_or_404(Tag, slug=slug)
     queryset = tag.tag_blogs.all()
     tags = Tag.objects.order_by('-created_date')[:5]
     page = request.GET.get('page', 1)
     paginator = Paginator(queryset, 2)
     all_blogs = Blog.objects.order_by('-created_date')[:5]
     try:
          blogs = paginator.page(page)
     except EmptyPage:
          blogs = paginator.page(1)
     except PageNotAnInteger:
          blogs = paginator.page(1)
     context = {
          "blogs": blogs,
          "tags":tags,
          "all_blogs": all_blogs
     }
     return render(request, 'category_blogs.html', context)


def blog_details(request, slug):
     form = TextForm()
     blog = get_object_or_404(Blog, slug=slug)
     category = Category.objects.get(id=blog.category.id)
     related_blogs = category.category_blogs.all()
     tags = Tag.objects.order_by('-created_date')[:5]

     if request.method ==  "POST" and request.user.is_authenticated:
          form = TextForm(request.POST)
          if form.is_valid():
               Comment.objects.create(
                    user = request.user,
                    blog=blog,
                    text =form.cleaned_data.get('text')
                    )
               return redirect('blog_details', slug=slug)
     


     context = {
          "blog": blog,
          "related_blogs": related_blogs,
          "tags": tags,
          "form": form
     }
     return render(request, 'blog_details.html', context)
@login_required(login_url='login')
def add_reply(request, blog_id, comment_id):
     blog = get_object_or_404(Blog, id=blog_id)
     if request.method == "POST":
          form = TextForm(request.POST)
          if form.is_valid():

               
               comment = get_object_or_404(Comment, id=comment_id)
               Reply.objects.create(
                    user=request.user,
                    comment=comment,
                    text=form.cleaned_data.get('text')
               )

     return redirect('blog_details', slug=blog.slug)

@login_required(login_url='login')

def like_blog(request,pk):
     context = {}
     blog = get_object_or_404(Blog, pk=pk)

     if request.user in blog.likes.all():
          blog.likes.remove(request.user)
          context['liked']=False
          context['like_count']=blog.likes.count
     else:
          blog.likes.add(request.user)
          context['liked']=True
          context['like_count']=blog.likes.count

     return JsonResponse(context, safe=False)

def search_blogs(request):
     search_key = request.GET.get('search', None)
     recent_blogs = Blog.objects.order_by('-created_date')
     tags = Tag.objects.order_by('-created_date')

     if search_key:
          blogs =Blog.objects.filter(
               Q(title__icontains=search_key) |
               Q(category__title__icontains=search_key) |
               Q(user__username__icontains=search_key)|
               Q(tags__title__icontains=search_key)
          ).distinct()

          context = {
               "blogs": blogs,
               "recent_blogs":recent_blogs,
               "tags":tags,
               "search_key":search_key
          }

          return render(request, 'search.html', context)
     else:
          return redirect("home")
     


def my_blogs(request):
    
     queryset = request.user.user_blogs.all()
     page = request.GET.get('page', 1)
     paginator = Paginator(queryset, 3)
    
     try:
          blogs = paginator.page(page)
     except EmptyPage:
          blogs = paginator.page(1)
     except PageNotAnInteger:
          blogs = paginator.page(1)
     context = {
          "blogs": blogs,
          "paginator":paginator
     }
     return render(request, 'my_blogs.html', context)


@login_required(login_url='login')
def add_blog(request):
     form = AddBlogForm()
     if request.method =="POST":
          form =AddBlogForm(request.POST, request.FILES)
          if form.is_valid():
               user = get_object_or_404(User, pk=request.user.pk)
               category = get_object_or_404(Category, pk=request.POST['category'])
               #district = District.objects.all(District, pk=request.POST['district'])
               #print(district)
               #thana = Thana(Thana, pk=request.POST['thana'])
               #print(thana)
               blog = form.save(commit=False)
               blog.user = user
               blog.category = category
               #blog.district = district  # Save the district
              # blog.thana = thana 
               blog.save()

               messages.success(request, "Blog added successfully")
               return redirect('blog_details', slug=blog.slug)
          else:
               print(form.errors)
 
     context ={
          "form":form,
          "districts": District.objects.all()
     }
     return render(request, 'add_blog.html', context)
        

def get_thanas(request):
    district_id = request.GET.get('district_id')
    if district_id:
        thanas = Thana.objects.filter(district_id=district_id).values('id', 'name')
        return JsonResponse({'thanas': list(thanas)})
    else:
        return JsonResponse({'thanas': []})

          


