from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Assignment

# Login View
def user_login(request):
    if request.method == 'POST':
        # Retrieve and validate username and password
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'login.html')

        if not username.isalpha():
            messages.error(request, 'Username must contain only letters.')
            return render(request, 'login.html')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Validate username contains only letters
            username = form.cleaned_data.get('username')
            if not username.isalpha():
                messages.error(request, 'Username must contain only letters.')
                return render(request, 'register.html', {'form': form})

            # Save the user and redirect to login
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
        else:
            # Display form errors as messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# Home/Dashboard View (Protected)
@login_required
def home(request):
    # Fetch up to 5 assignments for the logged-in user
    assignments = Assignment.objects.filter(user=request.user)[:5]
    return render(request, 'home.html', {'assignments': assignments})

# Assignment Tracker View (Protected)
@login_required
def assignments(request):
    if request.method == 'POST':
        # Retrieve and validate form data
        title = request.POST.get('title', '').strip()
        due_date = request.POST.get('due_date', '').strip()
        priority = request.POST.get('priority', '').strip()

        if not title or not due_date or not priority:
            messages.error(request, 'All fields are required.')
        else:
            # Save the assignment and display success message
            Assignment.objects.create(
                user=request.user,
                title=title,
                due_date=due_date,
                priority=priority
            )
            messages.success(request, 'Assignment added successfully.')

    # Fetch all assignments for the logged-in user
    assignments = Assignment.objects.filter(user=request.user)
    return render(request, 'assignments.html', {'assignments': assignments})

# Add Assignment View (Protected)
@login_required
def add_assignment(request):
    if request.method == 'POST':
        # Retrieve and validate form data
        title = request.POST.get('title', '').strip()
        due_date = request.POST.get('due_date', '').strip()
        priority = request.POST.get('priority', '').strip()

        if not title or not due_date or not priority:
            messages.error(request, 'All fields are required.')
        else:
            # Save the assignment and redirect to the Assignment Tracker page
            Assignment.objects.create(
                user=request.user,
                title=title,
                due_date=due_date,
                priority=priority
            )
            messages.success(request, 'Assignment added successfully.')
            return redirect('assignments')

    # Render the add assignment form for GET requests
    return render(request, 'add_assignment.html')