from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
 
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('createproduct')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})