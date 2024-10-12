# from tokenize import Comment
from decimal import Decimal
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cart.cart import Cart
from contact.models import Company, Contactus
from single.models import Description, Manufacturer, Review, Single
from store.models import Category, Product
from .forms import CheckoutForm, ContactusForm, LoginForm, UserRegistrationForm
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from about.models import About, Liquid
from account.models import User
from blog.models import Blog
from info.models import Info
from offering.models import Offering
from supports.models import Support
from testimonial.models import Comment, Experiense
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib import messages

User = get_user_model()


def accountView(request):
    user = User.objects.all()
    support = Support.objects.all()
    about = About.objects.all()
    liquid = Liquid.objects.all()
    offering = Offering.objects.all()
    comment = Comment.objects.all()
    experiense = Experiense.objects.all()
    blog = Blog.objects.all().order_by('-date')
    info = Info.objects.all()
    cart = Cart(request)

    return render(request, 'landing/index.html', context={
        'user': user,
        'support': support,
        'about': about,
        'liquid': liquid,
        'offering': offering,
        'comment': comment,
        'experiense': experiense,
        'blog': blog,
        'info': info,
        'cart': cart,

    })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')  # Redirect to the index view
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()  # Initialize the form for a GET request

    return render(request, 'account/login.html', {'form': form})


def register(request):
    user = User.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Save the new user
            new_user = user_form.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', context={
        'user_form': user_form,
        'user': user,
    })


def aboutView(request):
    support = Support.objects.all()
    about = About.objects.all()
    comment = Comment.objects.all()
    experiense = Experiense.objects.all()
    info = Info.objects.all()
    cart = Cart(request)

    return render(request, 'landing/about.html', context={
        'support': support,
        'about': about,
        'experiense': experiense,
        'comment': comment,
        'info': info,
        'cart': cart,

    })


def blogView(request):
    info = Info.objects.all()
    cart = Cart(request)
    blog = Blog.objects.all()  # Assuming Blog is your model
    paginator = Paginator(blog, 4)  # Show 4 blogs per page

    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)

    context = {
        'info': info,
        'cart': cart,
        'blog_list': blog_list,
        'blog_has_previous': blog_list.has_previous(),
        'blog_previous_page': blog_list.previous_page_number() if blog_list.has_previous() else None,
        'blog_has_next': blog_list.has_next(),
        'blog_next_page': blog_list.next_page_number() if blog_list.has_next() else None,
        'blog_number': blog_list.number,
        'blog_page_range': paginator.page_range,
    }

    return render(request, 'landing/blog.html', context)


def contactView(request):
    contactus = Contactus.objects.all()
    company = Company.objects.all()
    info = Info.objects.all()
    cart = Cart(request)

    if request.method == "POST":
        form = ContactusForm(request.POST)
        if form.is_valid():

            form.save(commit=False)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            recipients = ["backender.py@gmail.com"]

            form.save()
            messages.success(
                request, "Your message has been sent successfully!")
            return HttpResponseRedirect("#")

    else:
        form = ContactusForm()

    return render(request, 'landing/contact.html', context={
        'company': company,
        'contactus': contactus,
        'info': info,
        'form': form,
        'cart': cart,

    })


def productView(request):
    products = Product.objects.all()
    blog = Blog.objects.all().order_by('-date')
    info = Info.objects.all()
    cart = Cart(request)
    # Get the selected category from the URL
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    paginator = Paginator(products, 9)  # Show 9 products per page
    page_number = request.GET.get('page')
    products_list = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'info': info,
        'cart': cart,
        'products': products_list,
        'categories': categories,
        'blog': blog,
        'products_list': products_list,
        'products_has_previous': products_list.has_previous(),
        'products_previous_page': products_list.previous_page_number() if products_list.has_previous() else None,
        'products_has_next': products_list.has_next(),
        'products_next_page': products_list.next_page_number() if products_list.has_next() else None,
        'products_number': products_list.number,
        'products_page_range': paginator.page_range,
    }

    return render(request, 'landing/product.html', context)


def productsingleView(request):
    single = Single.objects.all()
    print(single,1111111111111111111111111111111111111111111)
    description = Description.objects.all()
    manufacturer = Manufacturer.objects.all()
    review = Review.objects.all()
    info = Info.objects.all()
    cart = Cart(request)
    # item.singnal.name

    return render(request, 'landing/product-single.html', context={
        'single': single,
        'description': description,
        'manufacturer': manufacturer,
        'review': review,
        'info': info,
        'cart': cart,

    })


def checkoutView(request):
    info = Info.objects.all()
    cart = Cart(request)
    count = Decimal('0.02')  # Convert the float to Decimal
    discount = Decimal(cart.get_total_price()) * count
    delivery = Decimal('0.05') * Decimal(cart.get_total_price())
    subtotal = cart.get_total_price()
    total_price = subtotal - discount + delivery

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.instance.total_price = cart.get_total_price() + delivery  - count

            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect("/checkout")
    else:
        form = CheckoutForm(initial={'total_price': cart.get_total_price() + delivery - count})

    return render(request, 'landing/checkout.html', context={
        'info': info,
        'cart': cart,
        'form': form,
        'discount': discount,
        'delivery': delivery,
        'total_price': total_price,
        

    })


