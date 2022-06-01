from django.shortcuts import render
from .filters import *
from django.contrib import messages
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .models import *
import requests


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Нэр эсвэл нууц үг буруу байна.')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homepage(request):
    username = request.user
    context = {'username': username}
    return render(request, 'home.html', context)


def FbCreate(request):
    context = {}

    if request.method == 'POST':
        form = FacebookForm(request.POST, None)
        if form.is_valid():
            form.save()
            print("---form valid-----")
        else:
            print("---error-----", form.errors)
    else:
        form = FacebookForm(None)

    context['form'] = form

    return render(request, 'fb.html', context)


def PageCreate(request):
    context = {}

    if request.method == 'POST':
        form = PageForm(request.POST, None)
        if form.is_valid():
            form.save()
            print("---form valid-----")
        else:
            print("---error-----", form.errors)
    else:
        form = PageForm(None)

    context['form'] = form

    return render(request, 'page.html', context)


def GroupCreate(request):
    context = {}

    if request.method == 'POST':
        form = GroupForm(request.POST, None)
        if form.is_valid():
            form.save()
            print("---form valid-----")
        else:
            print("---error-----", form.errors)
    else:
        form = GroupForm(None)

    context['form'] = form

    return render(request, 'group.html', context)


def PostCreate(request):
    context = {}

    if request.method == 'POST':
        form = PostForm(request.POST, None)
        if form.is_valid():
            form.save()
            print("---form valid-----")
        else:
            print("---error-----", form.errors)
    else:
        form = PostForm(None)

    context['form'] = form

    return render(request, 'post.html', context)


def Fb_list(request):
    fb_list = Facebook.objects.all()
    if request.method in 'POST':
        if 'delete' in request.POST:
            if request.POST['delete'] != "":
                fb = Facebook.objects.get(id=int(request.POST['delete']))
                fb.delete()
                fb_list = Facebook.objects.all()
        if 'search' in request.POST:
            filter_name = request.POST.get("name")
            if filter_name:
                fb_list = fb_list.filter(user_name=filter_name)
    return render(request, 'fb_list.html', {'fb_list': fb_list})


def Page_list(request):
    page_list = Page.objects.all()
    if request.method in 'POST':
        if 'delete' in request.POST:
            if request.POST['delete'] != "":
                page = Page.objects.get(id=int(request.POST['delete']))
                page.delete()
                page_list = Page.objects.all()
        if 'search' in request.POST:
            filter_name = request.POST.get("name")
            if filter_name:
                page_list = page_list.filter(user_name=filter_name)
    return render(request, 'page_list.html', {'page_list': page_list})


def Post_list(request):
    post_list = Post.objects.all()
    if request.method in 'POST':
        if 'delete' in request.POST:
            if request.POST['delete'] != "":
                post = Post.objects.get(id=int(request.POST['delete']))
                post.delete()
                post_list = Post.objects.all()
        if 'search' in request.POST:
            filter_name = request.POST.get("name")
            if filter_name:
                post_list = post_list.filter(user_name=filter_name)
    return render(request, 'post_list.html', {'post_list': post_list})


def Group_list(request):
    group_list = Group.objects.all()
    if request.method in 'POST':
        if 'delete' in request.POST:
            if request.POST['delete'] != "":
                group = Group.objects.get(id=int(request.POST['delete']))
                group.delete()
                group_list = Group.objects.all()
        if 'search' in request.POST:
            filter_name = request.POST.get("admin")
            if filter_name:
                group_list = group_list.filter(admin=filter_name)
    return render(request, 'group_list.html', {'group_list': group_list})


def editFacebook(request, pk):
    context = {}
    prod = Facebook.objects.get(id=pk)
    if request.method == "POST":
        form = FacebookForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save()
            return redirect('/fb_list')
    else:
        form = FacebookForm(instance=prod)
    context['prod'] = prod
    context['form'] = form
    return render(request, 'fb_edit.html', context)


def editGroup(request, pk):
    context = {}
    prod = Group.objects.get(id=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save()
            return redirect('/group_list')
    else:
        form = GroupForm(instance=prod)
    context['prod'] = prod
    context['form'] = form
    return render(request, 'group_edit.html', context)


def editPage(request, pk):
    context = {}
    prod = Page.objects.get(id=pk)
    if request.method == "POST":
        form = PageForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save()
            return redirect('/page_list')
    else:
        form = PageForm(instance=prod)
    context['prod'] = prod
    context['form'] = form
    return render(request, 'page_edit.html', context)


def editPost(request, pk):
    context = {}
    prod = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save()
            return redirect('/post_list')
    else:
        form = PostForm(instance=prod)
    context['prod'] = prod
    context['form'] = form
    return render(request, 'post_edit.html', context)


def search(request):
    user_list = Facebook.objects.all()
    user_filter = FacebookFilter(request.GET, queryset=user_list)
    return render(request, 'fb_list.html', {'filter': user_filter})


def search(request):
    user_list = Group.objects.all()
    user_filter = GroupFilter(request.GET, queryset=user_list)
    return render(request, 'group_list.html', {'filter': user_filter})


def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})


def busmodels(request):
    context = {}
    url = 'https://api.u-money.mn/travel/bus_line_detail/11400020/start'
    response = requests.post(url, data={})
    if response.status_code == 200:
        data = response.json()
        for x in data['station_list']:
            print(x)
            st_save = station_list(station_name=x['station_name'], station_id=x['station_id'], longitude=x['longitude'],
                                   station_seq=x['station_seq'], exist_bus=x['exist_bus'], latitude=x['latitude'],)
            st_save.save()
        context['bus'] = data['station_list']
    return render(request, 'bus.html', context)
    
