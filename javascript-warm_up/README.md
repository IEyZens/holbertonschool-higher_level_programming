# JavaScript - Warm up

**Novice**
**By:** Guillaume
**Weight:** 1

## Description

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

1. **Scripting** (same as we did with Python)
2. **Web front-end**

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

## Resources

**Read or watch:**

- [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)
- [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
- [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)
- [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Module patterns](https://www.patterns.dev/posts/module-pattern/)
- [var, let and const](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/)
- [JavaScript Tutorial](https://javascript.info/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- What are differences between `var`, `const` and `let`
- What are all the data types available in JavaScript
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use `while` and `for` loops
- How to use `break` and `continue` statements
- What is a function and how do you use functions
- What does a function that does not use any return statement return
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

## Requirements

### General
- **Allowed editors:** `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`

## Installation

### Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)

```bash
$ sudo npm install semistandard --global
```

## Tasks

### 0. First constant, first print
**File:** `0-javascript_is_amazing.js`

Write a script that prints "JavaScript is amazing":
- You must create a constant variable called `myVar` with the value "JavaScript is amazing"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```bash
guillaume@ubuntu:~/$ ./0-javascript_is_amazing.js
JavaScript is amazing
```

### 1. 3 languages
**File:** `1-multi_languages.js`

Write a script that prints 3 lines:
- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 2. Arguments
**File:** `2-arguments.js`

Write a script that prints a message depending of the number of arguments passed:
- If no arguments are passed to the script, print "No argument"
- If only one argument is passed to the script, print "Argument found"
- Otherwise, print "Arguments found"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- Reference: `process.argv`

### 3. Value of my argument
**File:** `3-value_argument.js`

Write a script that prints the first argument passed to it:
- If no arguments are passed to the script, print "No argument"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`

### 4. Create a sentence
**File:** `4-concat.js`

Write a script that prints two arguments passed to it, in the following format: " is "
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 5. An Integer
**File:** `5-to_integer.js`

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
- If the argument can't be converted to an integer, print "Not a number"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

### 6. Loop to languages
**File:** `6-multi_languages_loop.js`

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop:
- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop (`while`, `for`, etc.)

### 7. I love C
**File:** `7-multi_c.js`

Write a script that prints x times "C is fun":
- Where x is the first argument of the script
- If the first argument can't be converted to an integer, print "Missing number of occurrences"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (`while`, `for`, etc.)

### 8. Square
**File:** `8-square.js`

Write a script that prints a square:
- The first argument is the size of the square
- If the first argument can't be converted to an integer, print "Missing size"
- You must use the character `X` to print the square
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop (`while`, `for`, etc.)

### 9. Add
**File:** `9-add.js`

Write a script that prints the addition of 2 integers:
- The first argument is the first integer
- The second argument is the second integer
- You have to define a function with this prototype: `function add(a, b)`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 10. Factorial
**File:** `10-factorial.js`

Write a script that computes and prints a factorial:
- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of NaN is 1
- You must do it recursively
- You must use a function
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 11. Second biggest!
**File:** `11-second_biggest.js`

Write a script that searches the second biggest integer in the list of arguments:
- You can assume all arguments can be converted to integer
- If no argument passed, print 0
- If the number of arguments is 1, print 0
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

### 12. Object
**File:** `12-object.js`

Update this script to replace the value 12 with 89:
- You are not allowed to use `var`

### 13. Add file
**File:** `13-add.js`

Write a function that returns the addition of 2 integers:
- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`

## Repository Information

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `javascript-warm_up`

## Author

This project is part of the Holberton School Higher Level Programming curriculum.
