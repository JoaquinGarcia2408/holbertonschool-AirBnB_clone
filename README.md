<h1 align="center">AirBnB clone - The console</h1>
<p align= "justify">This is the first project in a series of projects aimed at recreating the AirBnb website. The goal of this project is to create a command interpreter to manage our AirBnB objects.</p>


<details>
<summary><h2>Project requirements</h2></summary>
  <h3>Python Scripts</h3>
  <ul>
    <li>Allowed editors: vi, vim, emacs</li>
    <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
    <li>All your files should end with a new line</li>
    <li>The first line of all your files should be exactly #!/usr/bin/python3</li>
    <li>A README.md file, at the root of the folder of the project, is mandatory</li>
    <li>Your code should use the pycodestyle (version 2.7.*)</li>
    <li>All your files must be executable</li>
    <li>The length of your files will be tested using wc</li>
    <li>All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')</li>
    <li>All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')</li>
    <li>All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')</li>
    <li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
  </ul>
  <h3>Python Unit Tests</h3>
  <ul>
    <li>Allowed editors: vi, vim, emacs</li>
    <li>All your files should end with a new line</li>
    <li>All your test files should be inside a folder tests</li>
    <li>You have to use the unittest module</li>
    <li>All your test files should be python files (extension: .py)</li>
    <li>All your test files and folders should start by test_</li>
    <li>Your file organization in the tests folder should be the same as your project</li>
    <li>e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py</li>
    <li>e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py</li>
    <li>All your tests should be executed by using this command: python3 -m unittest discover tests</li>
    <li>You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py</li>
    <li>All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')</li>
    <li>All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')</li>
    <li>All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')</li>
    <li>We strongly encourage you to work together on test cases, so that you don’t miss any edge case</li>
  </ul>
 </details>
 
<details>
<summary><h2>List of Commands</h2></summary>
<h3>Console commands</h3>
<ul>
    <li>create: Creates a new instance of BaseModel and prints the id.</li>
    <li>show: Prints the string representation of an instance based on the class name and id</li>
    <li>destroy: Deletes an instance based on the class name and id</li>
    <li>all: Prints all string representation of all instances based or not on the class name</li>
    <li>update: Updates an instance based on the class name id by adding or updating attribute</li>
    <li>quit and EOF: Exit to the program</li>
  </ul>
  <h3>Usage/Examples</h3>
  <p align= "justify">That is how the console works in interactive mode:


```ruby
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
<p align= "justify">And in non-interactive mode:


```ruby
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
</details>

<p align="center">Authors:</p>
<p align="center"><a href= "https://github.com/EliasMartincorre">Martin Correa Poggio</a></p>
<p align="center"><a href= "https://github.com/JoaquinGarcia2408">Joaquin Garcia</a></p>
  