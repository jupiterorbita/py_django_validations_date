from django.db import models
from django.db.models.fields import DateField
from datetime import date, datetime

# Create a function that takes a dictionary with these keys:
# title, description, due-date

# Validate:
# check to make sure that title, description and due-date
# values are not empty strings.
# Check to make sure title is at least 3 characters,
# description is at least 10 characters

# Return Error info:
# Return a dictionary with the only the keys
# that have any errors, and the value as a message 
# describing the error.

# No methods in our new manager should ever receive the whole request object as an argument! 
class TaskManager(models.Manager): # change to MANAGER
  def basic_validator(self, postData):
    
    today = date.today()
    print('\n* * * * * DATETIME.NOW() * * * * \n')
    print(today)
    
    errors = {}
    
    if len(postData['title']) < 3:
      errors['title'] = 'Title must have at least 3 characters'

    if len(postData['descriptions']) < 10:
      errors['descriptions'] = 'description must have at least 10 characters'
      
    if len(postData['due_date']) is not 10:
      print(f'\n\n =======\n date came as {postData["due_date"]}')
      errors['due_date'] = "please enter a date"
      return errors

    # date check in future:
    if postData['due_date'] < str(today):
      errors['due_date'] = "date is in the past"

    return errors
    
class Task(models.Model):
  title = models.CharField(max_length=80)
  descriptions = models.TextField()
  due_date = DateField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = TaskManager() # <-- ADD THIS




# models come with a hidden property:
#       objects = models.Manager()
# we are going to override this!
