# Introduction

Name: Adam Poindexter  
Major: Electrical Engineering (for now)  
Year: Sophomore (Class of 2019)

# Python Language

[Wikipedia:](https://en.wikipedia.org/wiki/Python_(programming_language)
"Python (programming language)")
Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale. Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library.

## Important Points:

* Python is an interpreted language
* Python is dynamically typed
* Python is strongly typed
* Python is a *VERY* high-level language

## Language Comparison
Assembly:
```
.text

.global main
main:
mov $4, %eax /* write system call */
mov $1, %ebx /* stdout */
mov $msg, %ecx
mov $msgend-msg, %edx
int $0x80

mov $1, %eax /* _exit system call */
mov $0, %ebx /* EXIT_SUCCESS */
int $0x80

.data

msg: .ascii "Hello, world\n"
msgend:
```

C++:
``` c++
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, world" << endl;
}
```

Java:
``` java
public class Hello {
    public static void main(String []args) {
        System.out.println("Hello World");
    }
}
```

Python:

``` python
print('Hello, world')
```
