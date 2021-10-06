from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# registeration form for new users
def register(request):
    # POST: called when new user submits registration form
    if request.method == 'POST':
        print('post ---')
        # create a new form object using new user's POST request
        form = UserRegisterForm(request.POST)
        
        # validate form data submitted
        if form.is_valid():
            print('form is valid ---')

            # save the form 
            form.save()

            # clean the POST data
            username = form.cleaned_data.get('username')

            # flash method, successful submission
            messages.success(request, f'Account created for {username}!')

            # redirect to new user's note_index
            #return redirect('note_index')
            return redirect('login')

    # GET: return a form 
    else:
        print('get ---')
        # instance of an empty form
        form = UserRegisterForm()
    
    # create form using template 
    print('render ---')
    #return render(request, 'register.html', {'form': form})
    return render(request, 'users/register.html', {'form': form})

# stops user from accessing user pages unless they are logged in
@login_required
def profile(request):
    return render(request, 'users/profile.html')