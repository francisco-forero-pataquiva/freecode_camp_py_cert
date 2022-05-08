def arithmetic_arranger(operations,display_answers=False):
    first_lines=""
    second_lines=""
    separators=""
    results=""
    spacing="    "
    counter = 0
    if len(operations) > 5:
        return("Error: Too many problems.")
    else:
        for operation in operations:
            if "/" in operation or "*" in operation:
                return("Error: Operator must be '+' or '-'.")   
            else:
                divided_operation= operation.split()
                x = [s.strip("divided_operation[1]") for s in operation]
                if divided_operation[0].isdigit() is False or divided_operation[2].isdigit() is False:
                    return('Error: Numbers must only contain digits.')
                else:           
                    if len(divided_operation[0]) > 4 or len(divided_operation[2]) > 4:
                        return("Error: Numbers cannot be more than four digits.")
                    else:
                        if len(divided_operation[0]) > len(divided_operation[2]): 
                            longer_operand = divided_operation[0] 
                        else:
                            longer_operand = divided_operation[2]
                        
                        first_line = str(divided_operation[0])
                        separator = str('-'*(len(longer_operand)+2))
                        x=len(separator)-len(divided_operation[2])-1 
                        y=len(separator)-len(divided_operation[0])
                        first_line = str((' '*y)+divided_operation[0])
                        second_line = str(divided_operation[1]+(' '*x)+divided_operation[2])
                        result = str(eval(operation))
                        z = len(separator)-len(result)
                        result = str((' '*z)+result)
                        separator = str('-'*(len(longer_operand)+2))
                        if counter < len(operations)-1:
                                first_lines +=f'{first_line+spacing}'
                                second_lines +=f'{second_line+spacing}'
                                separators +=f'{separator+spacing}'
                                results +=f'{result+spacing}'
                                counter += 1
                        else:
                            first_lines +=first_line+'\n'
                            second_lines +=second_line+'\n'
                            separators +=separator
                            results +=result
    if display_answers is False:
       return (first_lines+second_lines+separators) 
    else:                
        separators+= "\n"
        return (first_lines+second_lines+separators+results)
