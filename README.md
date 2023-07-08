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
</details>

<details>
<summary><h2>Syntax</h2></summary>

```ruby
_printf("%[format indicator]", input);
```

| Format indicator | Description |
| --- | --- |
| %c | Prints a single character |
| %s | Prints a string of characters |
| %i | Prints an integer in base 10 |
| %d | Prints a decimal number in base 10 |
| %% | Prints a percent sign |

#### Example:

Input

```ruby
int main()
{
	_printf("Character:[%c]\n", 'H');
	return(0);
}
```

Output

```ruby
Character:[H]
```

</details>

<details>
<summary><h2>Files</h2></summary>
  
### [_printf.c](/_printf.c/)
<p align= "justify">This file contains the main code of the printf function. This function is in charge of checking for possible error cases such as the format given being null, or there being no format specifier given after the '%'. It also is in charge of calling the get_functions function when the conditions are met, as well as sending the format to the print function that will be used. Finally, it is also in charge of returning the the number of characters printed (excluding the null byte used to end output to strings).</p>
<p>Prototype:</p> 
  
 ```ruby
 int _printf(const char *format, ...);
 ```
 <details>
   <summary><h3>Flowchart</h3></summary>
   
   ![Diagrama sin título](https://user-images.githubusercontent.com/124692695/229196886-cd213d01-1be9-4e5f-b66c-db10ef842a81.jpg)
   
  </details>
  
### [get_functions.c](/get_functions.c/)
<p align= "justify">This file contains the function that will return the print function associated with the format specifier given. It will do so by comparing the items enlisted in a structure.</p>
<p>Prototype:</p>

```ruby
int (*get_functions(char format))(va_list)  
```

### [functions.c](/functions.c/)
This file contains the different print functions pertainting to each printing format:
<ul>
  <li><b>print_string</b> - Writes the characters of the string specified by an argument of type char * up to (but not including) the NULL character ('\0'). If the string is null, it simply writes (null). When it is finished printing, it returns the amount of characters printed.</li>
  <p>Prototype:</p>
  
  ```ruby
  int print_string(va_list args); 
  ```
  
  <li><b>print_char</b> -  Converts an argument of type int to a value of type unsigned char and writes the resulting character. When finished, it returns 1 (beacuse one character is printed).</li>
  <p>Prototype:</p>
  
  ```ruby
  int print_char(va_list args); 
  ```
  
  <li><b>print_percentage</b> - A '%' is written, and a 1 is returned (beacuse one character is printed).</li>
  <p>Prototype:</p>
  
  ```ruby
  int print_percentage(va_list args); 
  ```
  
  <li><b>print_int</b> - Converts an int argument to signed decimal notation and writes the resulting integers. When finished, it returns a counter that held the amount of characters printed.</li>
  <p>Prototype:</p>
  
  ```ruby
  int print_int(va_list args); 
  ```
</ul>

### [aux_functions.c](/aux_functions.c/)
This file contains the auxiliary functions used by other functions, such as _strlen and _putchar.
  
### [main.h](/main.h/)
This file contains all the libraries used, as well as the definition of the structure and the prototypes of each function.
</details>

<p align="center">Authors:</p>
<p align="center"><a href= "https://github.com/solp22">Sol Puente</a></p>
<p align="center"><a href= "https://github.com/JoaquinGarcia2408">Joaquin Garcia</a></p>
  