# Comprehensive Python Learning Platform - Sample Data
# Complete roadmap from beginner to advanced Python concepts

PYTHON_ROADMAP = {
    "title": "Python Learning Roadmap",
    "content": """
# 🐍 Complete Python Learning Roadmap

## 🚀 Beginner Level (Weeks 1-4)
1. **Python Basics** - Syntax, variables, data types
2. **Control Flow** - If statements, loops
3. **Data Structures** - Lists, tuples, sets, dictionaries
4. **Functions** - Definition, parameters, return values

## 🔧 Intermediate Level (Weeks 5-8)
5. **Advanced Functions** - *args, **kwargs, lambda, recursion
6. **Object-Oriented Programming** - Classes, inheritance
7. **File I/O & Exceptions** - Reading/writing files, error handling
8. **Modules & Packages** - Import system, pip, virtual environments

## 🎯 Advanced Level (Weeks 9-12)
9. **Advanced OOP** - Magic methods, properties, abstract classes
10. **Functional Programming** - Decorators, generators, context managers
11. **Testing & Debugging** - Unit tests, debugging techniques
12. **Real-World Applications** - Web development, data science, automation

## 🎓 Specializations
- **Web Development** - Flask/Django, APIs
- **Data Science** - Pandas, NumPy, Matplotlib
- **Automation** - Scripts, web scraping, automation
- **Machine Learning** - Scikit-learn, TensorFlow
""",
    "image_prompt": "Python learning roadmap infographic showing progression from beginner to advanced with colorful milestones and checkpoints"
}

SAMPLE_LESSONS = [
    # BEGINNER LEVEL
    {
        "title": "Python Basics - Getting Started",
        "content": "Python is a high-level, interpreted programming language known for its simplicity and readability. It's perfect for beginners and widely used in web development, data science, artificial intelligence, and more. Let's start with the fundamentals!",
        "code": "# Your first Python program\nprint('Hello, World!')\n\n# Variables and basic data types\nname = 'Alice'          # String\nage = 25               # Integer\nheight = 5.9           # Float\nis_student = True      # Boolean\n\n# String formatting\nprint(f'My name is {name} and I am {age} years old')\nprint('Height:', height, 'feet')\nprint('Student status:', is_student)\n\n# Basic operations\nx = 10\ny = 3\nprint(f'Addition: {x + y}')\nprint(f'Subtraction: {x - y}')\nprint(f'Multiplication: {x * y}')\nprint(f'Division: {x / y}')\nprint(f'Floor division: {x // y}')\nprint(f'Modulus: {x % y}')\nprint(f'Power: {x ** y}')",
        "notes": "Python uses dynamic typing - you don't need to declare variable types. Indentation is crucial for code blocks. Use meaningful variable names and comments to make your code readable.",
        "video_url": "https://www.youtube.com/embed/rfscVS0vtbw",
        "image_prompt": "Python basics illustration showing variables, data types, and basic operations with code examples"
    },
    {
        "title": "Python Control Flow - Making Decisions",
        "content": "Control flow statements allow your program to make decisions and execute different code based on conditions. Python provides if, elif, and else statements for conditional execution, and various loop structures for repetitive tasks.",
        "code": "# If statements\nage = 18\n\nif age >= 18:\n    print('You are an adult')\nelif age >= 13:\n    print('You are a teenager')\nelse:\n    print('You are a child')\n\n# Comparison operators\nx = 10\ny = 5\n\nprint(f'x > y: {x > y}')\nprint(f'x < y: {x < y}')\nprint(f'x == y: {x == y}')\nprint(f'x != y: {x != y}')\nprint(f'x >= y: {x >= y}')\nprint(f'x <= y: {x <= y}')\n\n# Logical operators\nis_student = True\nhas_id = True\n\nif is_student and has_id:\n    print('Student discount applied!')\n\nif is_student or has_id:\n    print('Some benefits available')\n\nif not is_student:\n    print('Regular pricing')",
        "notes": "Python uses indentation (4 spaces) to define code blocks. The elif keyword is used for additional conditions, and else is used for the default case. Logical operators (and, or, not) help combine conditions.",
        "video_url": "https://www.youtube.com/embed/DZwmZ8Usvnk",
        "image_prompt": "Python control flow diagram showing if statements, loops, and decision making process"
    },
    {
        "title": "Python Loops - Repetition and Iteration",
        "content": "Loops allow you to execute a block of code multiple times. Python has two main types of loops: for loops (for iterating over sequences) and while loops (for repeating while a condition is true). Understanding loops is essential for efficient programming.",
        "code": "# For loop with range\nfor i in range(5):\n    print(f'Count: {i}')\n\n# For loop with list\nfruits = ['apple', 'banana', 'orange']\nfor fruit in fruits:\n    print(f'I like {fruit}')\n\n# For loop with enumerate\nfor index, fruit in enumerate(fruits):\n    print(f'{index + 1}. {fruit}')\n\n# While loop\ncount = 0\nwhile count < 3:\n    print(f'Count is {count}')\n    count += 1\n\n# Loop control statements\nfor i in range(10):\n    if i == 3:\n        continue  # Skip 3\n    if i == 7:\n        break     # Stop at 7\n    print(i)\n\n# Nested loops\nfor i in range(3):\n    for j in range(3):\n        print(f'({i}, {j})', end=' ')\n    print()  # New line after each row",
        "notes": "Use for loops when you know how many times to iterate, and while loops when you want to continue until a condition becomes false. break exits the loop, continue skips to the next iteration.",
        "video_url": "https://www.youtube.com/embed/OnDr4J2UXSA",
        "image_prompt": "Python loops illustration showing for and while loops with flow diagrams and examples"
    },
    {
        "title": "Python Lists - Ordered Collections",
        "content": "Lists are one of Python's most versatile data structures. They are ordered, mutable collections that can store elements of different types. Lists support indexing, slicing, and various methods for manipulation.",
        "code": "# Creating lists\nnumbers = [1, 2, 3, 4, 5]\nfruits = ['apple', 'banana', 'orange']\nmixed = [1, 'hello', 3.14, True]\n\n# Accessing elements\nprint(f'First fruit: {fruits[0]}')\nprint(f'Last fruit: {fruits[-1]}')\nprint(f'First two fruits: {fruits[:2]}')\n\n# Modifying lists\nfruits.append('grape')\nprint(f'After append: {fruits}')\n\nfruits.insert(1, 'mango')\nprint(f'After insert: {fruits}')\n\nfruits.remove('banana')\nprint(f'After remove: {fruits}')\n\npopped = fruits.pop()\nprint(f'Popped: {popped}')\nprint(f'After pop: {fruits}')\n\n# List methods\nnumbers.sort()\nprint(f'Sorted: {numbers}')\n\nnumbers.reverse()\nprint(f'Reversed: {numbers}')\n\n# List comprehension\nsquares = [x**2 for x in range(5)]\nprint(f'Squares: {squares}')\n\n# Filtering with comprehension\neven_squares = [x**2 for x in range(10) if x % 2 == 0]\nprint(f'Even squares: {even_squares}')",
        "notes": "Lists are indexed starting from 0. Negative indices count from the end. Lists are mutable - you can change their contents. List comprehensions provide a concise way to create lists.",
        "video_url": "https://www.youtube.com/embed/daefaLgNkw0",
        "image_prompt": "Python lists illustration showing list operations, indexing, and list comprehensions"
    },
    {
        "title": "Python Dictionaries - Key-Value Pairs",
        "content": "Dictionaries are unordered collections of key-value pairs. They are incredibly useful for storing and retrieving data efficiently. Each key must be unique and immutable (strings, numbers, tuples), while values can be of any type.",
        "code": "# Creating dictionaries\nperson = {\n    'name': 'John Doe',\n    'age': 30,\n    'city': 'New York',\n    'skills': ['Python', 'JavaScript', 'SQL']\n}\n\n# Accessing values\nprint(f'Name: {person[\"name\"]}')\nprint(f'Age: {person.get(\"age\")}')\nprint(f'Skills: {person.get(\"skills\", [])}')\n\n# Adding and updating\nperson['job'] = 'Developer'\nperson['age'] = 31\nprint(f'Updated person: {person}')\n\n# Dictionary methods\nprint(f'Keys: {list(person.keys())}')\nprint(f'Values: {list(person.values())}')\nprint(f'Items: {list(person.items())}')\n\n# Iterating through dictionaries\nfor key in person:\n    print(f'{key}: {person[key]}')\n\nfor key, value in person.items():\n    print(f'{key}: {value}')\n\n# Nested dictionaries\nstudents = {\n    'alice': {'age': 20, 'grade': 'A'},\n    'bob': {'age': 22, 'grade': 'B'},\n    'charlie': {'age': 21, 'grade': 'A-'}\n}\n\nprint(f'Alice\\'s grade: {students[\"alice\"][\"grade\"]}')\n\n# Dictionary comprehension\nsquares = {x: x**2 for x in range(5)}\nprint(f'Number squares: {squares}')",
        "notes": "Dictionaries use keys to access values efficiently. The get() method is safer than direct access as it allows default values. Dictionaries are mutable and support various methods for manipulation.",
        "video_url": "https://www.youtube.com/embed/daefaLgNkw0",
        "image_prompt": "Python dictionaries illustration showing key-value pairs and dictionary operations"
    },
    {
        "title": "Python Functions - Reusable Code Blocks",
        "content": "Functions are reusable blocks of code that perform specific tasks. They help organize code, make it more readable, and avoid repetition. Python functions can take parameters, return values, and have default arguments.",
        "code": "# Basic function definition\ndef greet(name):\n    return f'Hello, {name}!'\n\n# Function call\nmessage = greet('Alice')\nprint(message)\n\n# Function with multiple parameters\ndef add_numbers(a, b):\n    return a + b\n\nresult = add_numbers(5, 3)\nprint(f'5 + 3 = {result}')\n\n# Function with default parameters\ndef greet_with_title(name, title='Mr.'):\n    return f'Hello, {title} {name}!'\n\nprint(greet_with_title('Smith'))\nprint(greet_with_title('Johnson', 'Dr.'))\n\n# Function with *args (variable arguments)\ndef sum_all(*args):\n    return sum(args)\n\nprint(f'Sum of 1,2,3: {sum_all(1, 2, 3)}')\nprint(f'Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}')\n\n# Function with **kwargs (keyword arguments)\ndef print_info(**kwargs):\n    for key, value in kwargs.items():\n        print(f'{key}: {value}')\n\nprint_info(name='John', age=30, city='NYC')\n\n# Lambda functions (anonymous functions)\nsquare = lambda x: x ** 2\nprint(f'Square of 4: {square(4)}')\n\n# Lambda with multiple arguments\nadd = lambda x, y: x + y\nprint(f'Lambda add: {add(3, 5)}')",
        "notes": "Functions should have descriptive names and docstrings. Use default parameters to make functions more flexible. *args collects positional arguments, **kwargs collects keyword arguments. Lambda functions are useful for simple operations.",
        "video_url": "https://www.youtube.com/embed/9Os0o3wzS_I",
        "image_prompt": "Python functions illustration showing function definition, parameters, return values, and lambda functions"
    },
    
    # INTERMEDIATE LEVEL
    {
        "title": "Advanced Functions - *args, **kwargs, and Recursion",
        "content": "Advanced function concepts in Python include variable arguments, keyword arguments, recursion, and function decorators. These features make functions more flexible and powerful for complex programming tasks.",
        "code": "# *args - Variable positional arguments\ndef calculate_average(*args):\n    if not args:\n        return 0\n    return sum(args) / len(args)\n\nprint(f'Average of 1,2,3: {calculate_average(1, 2, 3)}')\nprint(f'Average of 10,20,30,40: {calculate_average(10, 20, 30, 40)}')\n\n# **kwargs - Variable keyword arguments\ndef create_profile(**kwargs):\n    profile = {}\n    for key, value in kwargs.items():\n        profile[key] = value\n    return profile\n\nuser = create_profile(name='Alice', age=25, city='Boston', job='Engineer')\nprint(f'User profile: {user}')\n\n# Combining *args and **kwargs\ndef flexible_function(*args, **kwargs):\n    print(f'Positional arguments: {args}')\n    print(f'Keyword arguments: {kwargs}')\n\nflexible_function(1, 2, 3, name='John', age=30)\n\n# Recursion - Function calling itself\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(f'Factorial of 5: {factorial(5)}')\n\n# Recursive Fibonacci\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\nprint(f'Fibonacci sequence: {[fibonacci(i) for i in range(10)]}')\n\n# Function as first-class objects\ndef apply_operation(func, x, y):\n    return func(x, y)\n\ndef add(x, y):\n    return x + y\n\ndef multiply(x, y):\n    return x * y\n\nprint(f'Apply add: {apply_operation(add, 5, 3)}')\nprint(f'Apply multiply: {apply_operation(multiply, 5, 3)}')",
        "notes": "*args collects all positional arguments into a tuple. **kwargs collects all keyword arguments into a dictionary. Recursion is powerful but can cause stack overflow for deep calls. Functions are first-class objects in Python.",
        "video_url": "https://www.youtube.com/embed/9Os0o3wzS_I",
        "image_prompt": "Advanced Python functions illustration showing *args, **kwargs, recursion, and function objects"
    },
    {
        "title": "Object-Oriented Programming - Classes and Objects",
        "content": "Object-Oriented Programming (OOP) is a programming paradigm that uses objects to design applications. Python supports OOP with classes, objects, inheritance, and polymorphism. Understanding OOP is crucial for building complex applications.",
        "code": "# Basic class definition\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    \n    def greet(self):\n        return f'Hello, my name is {self.name} and I am {self.age} years old.'\n    \n    def have_birthday(self):\n        self.age += 1\n        return f'{self.name} is now {self.age} years old!'\n\n# Creating objects\nperson1 = Person('Alice', 25)\nperson2 = Person('Bob', 30)\n\nprint(person1.greet())\nprint(person2.greet())\nprint(person1.have_birthday())\n\n# Class with class variables\nclass Student:\n    school_name = 'Python Academy'\n    \n    def __init__(self, name, grade):\n        self.name = name\n        self.grade = grade\n    \n    def get_info(self):\n        return f'{self.name} is a {self.grade} student at {self.school_name}'\n\nstudent1 = Student('Charlie', 'A')\nstudent2 = Student('Diana', 'B')\n\nprint(student1.get_info())\nprint(student2.get_info())\n\n# Inheritance\nclass Employee(Person):\n    def __init__(self, name, age, employee_id, salary):\n        super().__init__(name, age)\n        self.employee_id = employee_id\n        self.salary = salary\n    \n    def get_salary_info(self):\n        return f'{self.name} earns ${self.salary:,} per year'\n\nemployee = Employee('Eve', 28, 'EMP001', 75000)\nprint(employee.greet())\nprint(employee.get_salary_info())\n\n# Method overriding\nclass Manager(Employee):\n    def __init__(self, name, age, employee_id, salary, department):\n        super().__init__(name, age, employee_id, salary)\n        self.department = department\n    \n    def get_salary_info(self):\n        return f'{self.name} is a {self.department} manager earning ${self.salary:,} per year'\n\nmanager = Manager('Frank', 35, 'EMP002', 100000, 'Engineering')\nprint(manager.get_salary_info())",
        "notes": "Classes are blueprints for creating objects. The __init__ method is the constructor. self refers to the instance of the class. Inheritance allows classes to inherit attributes and methods from parent classes.",
        "video_url": "https://www.youtube.com/embed/JeznW_7DlB0",
        "image_prompt": "Python OOP illustration showing classes, objects, inheritance, and object relationships"
    },
    {
        "title": "File I/O and Exception Handling",
        "content": "File Input/Output (I/O) operations allow you to read from and write to files. Exception handling helps you manage errors gracefully. These are essential skills for building robust applications that interact with external data.",
        "code": "# Reading files\ntry:\n    with open('sample.txt', 'w') as file:\n        file.write('Hello, World!\\n')\n        file.write('This is a sample file.\\n')\n        file.write('Python is awesome!\\n')\n    print('File created successfully!')\nexcept IOError as e:\n    print(f'Error creating file: {e}')\n\n# Reading files\ntry:\n    with open('sample.txt', 'r') as file:\n        content = file.read()\n        print('File content:')\n        print(content)\nexcept FileNotFoundError:\n    print('File not found!')\nexcept IOError as e:\n    print(f'Error reading file: {e}')\n\n# Reading line by line\ntry:\n    with open('sample.txt', 'r') as file:\n        print('Reading line by line:')\n        for line_num, line in enumerate(file, 1):\n            print(f'Line {line_num}: {line.strip()}')\nexcept FileNotFoundError:\n    print('File not found!')\n\n# Writing to files with different modes\ntry:\n    with open('data.txt', 'w') as file:\n        file.write('Line 1\\n')\n        file.write('Line 2\\n')\n    \n    with open('data.txt', 'a') as file:  # Append mode\n        file.write('Line 3\\n')\n        file.write('Line 4\\n')\n    \n    print('File written successfully!')\nexcept IOError as e:\n    print(f'Error writing file: {e}')\n\n# Exception handling examples\ndef divide_numbers(a, b):\n    try:\n        result = a / b\n        return result\n    except ZeroDivisionError:\n        return 'Error: Division by zero!'\n    except TypeError:\n        return 'Error: Invalid input types!'\n    except Exception as e:\n        return f'Unexpected error: {e}'\n\nprint(f'10 / 2 = {divide_numbers(10, 2)}')\nprint(f'10 / 0 = {divide_numbers(10, 0)}')\nprint(f'10 / \"a\" = {divide_numbers(10, \"a\")}')\n\n# Custom exceptions\nclass AgeError(Exception):\n    pass\n\ndef verify_age(age):\n    if age < 0:\n        raise AgeError('Age cannot be negative!')\n    if age > 150:\n        raise AgeError('Age seems unrealistic!')\n    return f'Age {age} is valid!'\n\ntry:\n    print(verify_age(25))\n    print(verify_age(-5))\nexcept AgeError as e:\n    print(f'Age error: {e}')",
        "notes": "Always use 'with' statements for file operations - they automatically close files. Handle specific exceptions before general ones. Custom exceptions help create meaningful error messages for your application.",
        "video_url": "https://www.youtube.com/embed/Uh2ebFW8OYM",
        "image_prompt": "Python file I/O and exception handling illustration showing file operations and error handling"
    },
    
    # ADVANCED LEVEL
    {
        "title": "Advanced OOP - Magic Methods and Properties",
        "content": "Advanced Object-Oriented Programming in Python includes magic methods (special methods), properties, abstract classes, and design patterns. These concepts help you create more sophisticated and Pythonic classes.",
        "code": "# Magic methods (special methods)\nclass Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    \n    def __str__(self):\n        return f'Vector({self.x}, {self.y})'\n    \n    def __repr__(self):\n        return f'Vector({self.x}, {self.y})'\n    \n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    \n    def __sub__(self, other):\n        return Vector(self.x - other.x, self.y - other.y)\n    \n    def __eq__(self, other):\n        return self.x == other.x and self.y == other.y\n    \n    def __len__(self):\n        return int((self.x**2 + self.y**2)**0.5)\n\nv1 = Vector(3, 4)\nv2 = Vector(1, 2)\n\nprint(f'v1: {v1}')\nprint(f'v2: {v2}')\nprint(f'v1 + v2: {v1 + v2}')\nprint(f'v1 - v2: {v1 - v2}')\nprint(f'v1 == v2: {v1 == v2}')\nprint(f'Length of v1: {len(v1)}')\n\n# Properties\nclass Circle:\n    def __init__(self, radius):\n        self._radius = radius\n    \n    @property\n    def radius(self):\n        return self._radius\n    \n    @radius.setter\n    def radius(self, value):\n        if value < 0:\n            raise ValueError('Radius cannot be negative!')\n        self._radius = value\n    \n    @property\n    def area(self):\n        return 3.14159 * self._radius ** 2\n    \n    @property\n    def circumference(self):\n        return 2 * 3.14159 * self._radius\n\ncircle = Circle(5)\nprint(f'Radius: {circle.radius}')\nprint(f'Area: {circle.area:.2f}')\nprint(f'Circumference: {circle.circumference:.2f}')\n\ncircle.radius = 7\nprint(f'New radius: {circle.radius}')\nprint(f'New area: {circle.area:.2f}')\n\n# Abstract base classes\nfrom abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n    \n    @abstractmethod\n    def perimeter(self):\n        pass\n\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    \n    def area(self):\n        return self.width * self.height\n    \n    def perimeter(self):\n        return 2 * (self.width + self.height)\n\nclass Triangle(Shape):\n    def __init__(self, a, b, c):\n        self.a = a\n        self.b = b\n        self.c = c\n    \n    def area(self):\n        # Heron's formula\n        s = (self.a + self.b + self.c) / 2\n        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5\n    \n    def perimeter(self):\n        return self.a + self.b + self.c\n\nrect = Rectangle(4, 6)\ntri = Triangle(3, 4, 5)\n\nprint(f'Rectangle area: {rect.area()}, perimeter: {rect.perimeter()}')\nprint(f'Triangle area: {tri.area():.2f}, perimeter: {tri.perimeter()}')",
        "notes": "Magic methods allow you to define how objects behave with operators. Properties provide controlled access to attributes. Abstract base classes enforce interface implementation. These concepts make your code more Pythonic and maintainable.",
        "video_url": "https://www.youtube.com/embed/JeznW_7DlB0",
        "image_prompt": "Advanced Python OOP illustration showing magic methods, properties, and abstract classes"
    },
    {
        "title": "Decorators and Generators - Advanced Python Features",
        "content": "Decorators and generators are powerful Python features that enable functional programming patterns and memory-efficient iteration. Decorators modify or enhance functions, while generators create iterators without storing all values in memory.",
        "code": "# Simple decorator\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        import time\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f'{func.__name__} took {end - start:.4f} seconds')\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    import time\n    time.sleep(1)\n    return 'Done!'\n\nresult = slow_function()\nprint(result)\n\n# Decorator with parameters\ndef repeat(times):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for _ in range(times):\n                result = func(*args, **kwargs)\n            return result\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef greet(name):\n    print(f'Hello, {name}!')\n\ngreet('Alice')\n\n# Class decorator\nclass Logger:\n    def __init__(self, func):\n        self.func = func\n        self.calls = 0\n    \n    def __call__(self, *args, **kwargs):\n        self.calls += 1\n        print(f'Calling {self.func.__name__} (call #{self.calls})')\n        return self.func(*args, **kwargs)\n\n@Logger\ndef add(a, b):\n    return a + b\n\nprint(add(3, 5))\nprint(add(10, 20))\n\n# Generators\ndef fibonacci_generator(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\nprint('Fibonacci sequence:')\nfor num in fibonacci_generator(10):\n    print(num, end=' ')\nprint()\n\n# Generator expression\nsquares = (x**2 for x in range(5))\nprint(f'Generator squares: {list(squares)}')\n\n# Context managers with generators\nfrom contextlib import contextmanager\n\n@contextmanager\ndef timer_context():\n    import time\n    start = time.time()\n    yield\n    end = time.time()\n    print(f'Operation took {end - start:.4f} seconds')\n\nwith timer_context():\n    import time\n    time.sleep(0.5)\n    print('Some operation...')\n\n# Practical decorator example\ndef cache(func):\n    memo = {}\n    def wrapper(*args):\n        if args not in memo:\n            memo[args] = func(*args)\n        return memo[args]\n    return wrapper\n\n@cache\ndef fibonacci(n):\n    if n < 2:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\nprint(f'Fibonacci(10): {fibonacci(10)}')\nprint(f'Fibonacci(20): {fibonacci(20)}')",
        "notes": "Decorators modify or enhance functions without changing their source code. Generators create iterators efficiently by yielding values one at a time. Context managers handle setup and cleanup automatically. These features enable elegant and efficient code patterns.",
        "video_url": "https://www.youtube.com/embed/FXUUSfJO_J4",
        "image_prompt": "Python decorators and generators illustration showing function decoration and generator patterns"
    }
]

SAMPLE_QUIZZES = {
    1: [  # Python Basics
        {
            "question": "What is the correct way to print 'Hello, World!' in Python?",
            "options": ["print('Hello, World!')", "echo('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')"],
            "answer": "print('Hello, World!')",
            "explanation": "Python uses the print() function to output text to the console."
        },
        {
            "question": "Which of the following is a valid Python variable name?",
            "options": ["2name", "my-name", "my_name", "class"],
            "answer": "my_name",
            "explanation": "Variable names can contain letters, numbers, and underscores, but cannot start with a number or contain hyphens."
        },
        {
            "question": "What is the result of 5 // 2 in Python?",
            "options": ["2.5", "2", "2.0", "3"],
            "answer": "2",
            "explanation": "The // operator performs floor division, which returns the largest integer less than or equal to the division result."
        }
    ],
    2: [  # Control Flow
        {
            "question": "What is the correct syntax for an if statement in Python?",
            "options": ["if x > y:", "if (x > y)", "if x > y then", "if x > y {"],
            "answer": "if x > y:",
            "explanation": "Python uses colons (:) to indicate the start of a code block, not parentheses or braces."
        },
        {
            "question": "Which keyword is used for additional conditions in an if statement?",
            "options": ["elseif", "elif", "else if", "ifelse"],
            "answer": "elif",
            "explanation": "elif is the Python keyword for 'else if' - it allows you to check multiple conditions."
        },
        {
            "question": "What does the 'break' statement do in a loop?",
            "options": ["Skip to the next iteration", "Exit the loop completely", "Continue the loop", "Pause the loop"],
            "answer": "Exit the loop completely",
            "explanation": "The break statement immediately exits the innermost loop that contains it."
        }
    ],
    3: [  # Loops
        {
            "question": "How do you iterate over a list in Python?",
            "options": ["for i in list:", "for i = 0; i < len(list); i++", "foreach item in list:", "while i < len(list):"],
            "answer": "for i in list:",
            "explanation": "Python's for loop directly iterates over the elements of a sequence like a list."
        },
        {
            "question": "What does the 'continue' statement do in a loop?",
            "options": ["Exit the loop", "Skip to the next iteration", "Pause the loop", "Restart the loop"],
            "answer": "Skip to the next iteration",
            "explanation": "The continue statement skips the rest of the current iteration and moves to the next one."
        }
    ],
    4: [  # Lists
        {
            "question": "How do you add an element to the end of a list?",
            "options": ["list.add(item)", "list.append(item)", "list.insert(item)", "list.push(item)"],
            "answer": "list.append(item)",
            "explanation": "The append() method adds an element to the end of a list."
        },
        {
            "question": "What is list indexing in Python?",
            "options": ["Starts at 1", "Starts at 0", "Starts at -1", "Starts at any number"],
            "answer": "Starts at 0",
            "explanation": "Python uses zero-based indexing, meaning the first element is at index 0."
        }
    ],
    5: [  # Dictionaries
        {
            "question": "How do you access a value in a dictionary?",
            "options": ["dict.get(key)", "dict[key]", "Both A and B", "dict.value(key)"],
            "answer": "Both A and B",
            "explanation": "You can use either dict[key] or dict.get(key) to access dictionary values."
        },
        {
            "question": "What type of object can be used as a dictionary key?",
            "options": ["Any object", "Only strings", "Only immutable objects", "Only numbers"],
            "answer": "Only immutable objects",
            "explanation": "Dictionary keys must be immutable (strings, numbers, tuples), but not lists or dictionaries."
        }
    ],
    6: [  # Functions
        {
            "question": "What is the purpose of the 'return' statement in a function?",
            "options": ["To print a value", "To send a value back to the caller", "To end the function", "To define the function"],
            "answer": "To send a value back to the caller",
            "explanation": "The return statement sends a value back to wherever the function was called from."
        },
        {
            "question": "What does *args do in a function definition?",
            "options": ["Collects keyword arguments", "Collects positional arguments", "Defines required arguments", "Creates a list"],
            "answer": "Collects positional arguments",
            "explanation": "*args collects all positional arguments into a tuple."
        }
    ]
} 