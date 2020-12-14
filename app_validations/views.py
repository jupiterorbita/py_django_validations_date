from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from django.contrib import messages
from datetime import date


def index(request):
  print('\n------ index -------')
  
  context = {
    'all_tasks': Task.objects.all(),
    'today' : str(date.today())
  }
  
  
  return render(request, 'index.html', context)

def create_task(request):
  print('\n------ create_task -------')
  print(request.POST)
  print(len(request.POST))
  print('what get? request.POST.get("title")')
  
  #pass the request.POST to the method we wrote and save the response in a a var called errors
  errors = Task.objects.basic_validator(request.POST)
  
  # check if errors dict came back with anything in
  if len(errors) > 0:
    
    # if errors dict contains anything, loop thru each key-val pair and make a flash message 
    for key, value in errors.items():
      messages.error(request, value)
      
      print('\n errors ====>', errors)
     
      # redirect the user back to the form to fix the errors
    return redirect('/')
  else:
    # if the errors obj is empty, no errors!
    # ok to do changes in DB
    Task.objects.create(
      title=request.POST['title'],
      descriptions=request.POST['descriptions'],
      due_date = request.POST['due_date'])
    print('created -> ', Task.objects.all())
    
  return redirect('/')

# def validate(form_data):
#   print('\n= = = = VALIDATE = = = =')
#   # return a dictionary with errors
#   print(form_data)

#   title=form_data['title']
#   descriptions=form_data['descriptions']
#   due_date = form_data['due_date']
  
#   print(title)
#   print(descriptions)
  
#   errors = {}
  
#   if len(form_data['title']) < 2 :
#     errors['title'] = "Title cannot be less than 2 letters"
#   if len(form_data['descriptions']) < 2:
#     errors['descriptions'] = "Description cannot be less than 2 letters"
  
#   return errors

# {"title": "title cannot be blank",
# "descriptions": "please write ", 
# "date": "date must be in the future"}
  