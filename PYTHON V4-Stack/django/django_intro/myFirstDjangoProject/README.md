### First Django Project
<br/>

**Objectives:**

- Practice setting up a new Django project
- Practice setting up a new Django app
- Practice routing in Django
- Familiarity with views and how to return a response
<hr>
It's time to practice routing! Use the checklist below to add routes to your project. 

***Note*** for the assignment, the show, edit, and delete methods will require the use of Route Parameters.  

***Bonus*** result:

![](img.png)

- [x] Create a new project with a single app

- [x] / - redirects to the "/blogs" route with a method called "root"

- [x] /blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"

- [x] /blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"

- [x] /blogs/create - redirect to the "/" route with a method called "create"

- [x] /blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15')

- [x] /blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"

- [x] /blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"