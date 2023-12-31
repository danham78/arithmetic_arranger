# arithmetic_arranger
freeCodeCamp Scientific Computing with Python challenge

This project is a python program I wrote in response to a challenge set as part of the Scientific Computing with Python course certification.
The challenge is described below:


Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

![2023-06-29 (3)](https://github.com/danham78/arithmetic_arranger/assets/131801769/e55d8d79-9652-42e9-8735-b9ea982ba0a3)


Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example

![2023-06-29 (2)](https://github.com/danham78/arithmetic_arranger/assets/131801769/aabb652b-ee09-43ce-b2f1-0af4846eb28f)

Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:

If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.

The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.

Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.

Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

If the user supplied the correct format of problems, the conversion you return will follow these rules:

There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).

Numbers should be right-aligned.

There should be four spaces between each problem.

There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

# Installation
- download the file
- ensure you have python3 installed
- run in the command line with the command python arithmetic_arranger.py

# License 
arithmetic_arranger is available under the MIT, GNU license. 
