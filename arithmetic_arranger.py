def arithmetic_arranger(problem_list, calculate=False):
    # Splits problems string into problems list
    problems = [problem.split() for problem in problem_list]
    for problem in problems:
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            len_error = 'Error: Numbers cannot be more than four digits.'
            return len_error
    try:
        [(int(problem[0]), int(problem[2])) for problem in problems]
    except:
        digits_error = 'Error: Numbers must only contain digits.'
        return digits_error
    else:
        if len(problems) > 5:
            problems_error = 'Error: Too many problems.'
            return problems_error
        elif '/' in str(problem_list) or '*' in str(problem_list):
            operator_error ='''Error: Operator must be '+' or '-'.'''
            return(operator_error)
        else:
            # Creates empty lists for each different element that needs to be called
            first_num = []
            second_num = []
            operators = []
            answers = []
            long_num = []
            short_num = []
            # Determines which operand is longer for each problem and appends to the appropriate list
            for problem in problems:
                if len(problem[0]) >= len(problem[2]):
                    long_num.append(problem[0])
                    short_num.append(problem[2])
                else:
                    long_num.append(problem[2])
                    short_num.append(problem[0])
            # Populates lists above and creates lists of formatting elements from the problem string
            first_num = [problem[0] for problem in problems]
            second_num = [problem[2] for problem in problems]
            operators = [problem[1] for problem in problems]
            num_dashes = [len(num) + 2 for num in long_num]
            num_spaces1 = [a - len(b) for a, b in zip(num_dashes, first_num)]
            num_spaces2 = [a - 1 - len(b) for a, b in zip(num_dashes, second_num)]
            # Populates the answers list form the problem string
            
            
            for problem in problems:
                if '+' in problem:
                    answers.append(int(problem[0]) + int(problem[2]))
                elif '-' in problem:
                    answers.append(int(problem[0]) - int(problem[2]))
            num_spaces_answers = [a - len(str(b)) for a, b in zip(num_dashes, answers)]

            # Defines empty lists for each line of the formatter
            conversion_False1 = ''
            conversion_False2 = ''
            conversion_False3 = ''
            conversion_True = ''
                    
            for i in range(len(problems)):
                conversion_False1 += (num_spaces1[i]*' ') + first_num[i] + '    '
                conversion_False2 += operators[i] + (num_spaces2[i]*' ') + second_num[i] + '    '
                conversion_False3 += (num_dashes[i] * '-') + '    '
                conversion_True += (num_spaces_answers[i] * ' ') + str(answers[i]) + '    '
            

            conversion_complete = conversion_False1.rstrip() + '\n' + conversion_False2.rstrip() + '\n' + conversion_False3.rstrip() + '\n' + conversion_True.rstrip()

            conversion_sums = conversion_False1.rstrip() + '\n' + conversion_False2.rstrip() + '\n' + conversion_False3.rstrip()

            if calculate == True:
                return conversion_complete
            else:
                return conversion_sums
        
    
    #print(first_num)
    #print(second_num)
    #print(num_dashes)
    #print(problems)
    #print(answers)
    #print(long_num)
    #print(short_num)
    #print(num_spaces1)
    #print(num_spaces2)
    #print(conversion_False1)
    #print(conversion_False2)
    #print(conversion_False3)
    



print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))

