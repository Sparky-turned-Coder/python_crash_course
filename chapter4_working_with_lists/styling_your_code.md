# Styling Your Code

> <i>"A Foolish Consistency is the Hobgoblin of Little Minds"</i> <br>

One of Guido's key insights is that code is read much more often than it is written.

Now that we're writing longer programs, it's a good idea to learn how to style your code consistently.
Take the time to make your code as easy as possible to read. Writing easy-to-read code helps you keep
track of what programs are doing and heklps others understand your code as well.

Python programmers have agreed on a number of styling conventions to ensure that everyone's code is
structured in roughly the same way. Once you've learned to write clean Python code, you should be able
to understand the overall structure of anyone else's Python code, as long as they follow the same guidelines.
Develop good habits if you ever hope to be a professional programmer.

## The Style Guide

When someone wants to make a change to the Python language, they write a <i>Python Enhancement Proposal(PEP)</i>.
One of the oldest PEPs is <i>PEP 8</i>, which instructs Python programmers on how to style their code. PEP 8 is
fairly lengthy, but much of it relates to more complex coding structures than what you've seen so far.

Given the choice between writing code that's easier to write or code that's easier to read, Python programmers
will almost always encourage you to write code that's easier to read.

### Indentation

PEP 8 recommends that you use four spaces per indentation level. Using four spaces improves readability while leaving
room for multiple levels of indentation on each line.

In neovim, I can set tab to be however many spaces I want it to be. Currently, it is already set to four spaces.

Don't mix tabs and spaces in your code. It can cause problems that are difficult to diagnose, as Python specifically
utilizes whitespace in its syntax.

### Line Length

Many Python programmers recommend that each line should be less than 80 characters. Historically, this guideline developed
because most computers could fit only 79 characters on a single line in a terminal window. Currently, people can fit much
longer lines on their screens, but other reasons exist to adhere to the 79-character standard line length.

Professional programmers often have several files open on the same screen, and using the standard line length allows them to
see entire lines in two or three files that are open side by side onscreen. PEP 8 also recommends that you limit all of your
comments to 72 characters per line, because some of the tools that generate automatic documentation for larger projects add
formatting characters at the beginning of each commented line.

The PEP 8 guidelines for line length are not set in stone, and some teams prefer a 99-character limit. Don't worry too much
about line length in your code as you're learning, but be aware that people who are working collaboratively almost always
follow PEP 8 guidelines.

### Blank Lines

To group parts of your program visually, use blank lines. You should use blank lines to organize your files, but don't do so
excessively. By following the examples provided in this book, you should strike the right balance. <b>For example, if you have
five lines of code that build a list and then another three lines that do something with that list, its appropriate to place
a blank line between the two sections. However, you should not place three or four blank lines between the two sections.</b>

### Other Style Guidelines

PEP 8 has many additional styling recommendations, but most of the guidelines refer to more complex programs than what you're
writing at this point. As you learn more complex Python structures, I'll share the relevant parts of the PEP 8 guidelines.
