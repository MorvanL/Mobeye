
def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams.
    :param s1: string
    :param s2: string
    :return: True or False
    """

    # Easiest solution
    """
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)
    """

    # Most efficient solution
    if len(s1) != len(s2) :
        return False

    counter1 = count_letter_in_dict(s1)
    counter2 = count_letter_in_dict(s2)

    return contain_same_values_and_keys(counter1, counter2)



def contain_same_values_and_keys(dict1, dict2):
    # Don't forget to compare lenght if it's not already done
    for key in dict1:
        if not key in dict2 :
            return False
        if dict1[key] != dict2[key] :
            return False

    return True



def count_letter_in_dict(s):
    counter = {}

    for l in s :
        if l in counter:
            counter[l] += 1
        else:
            counter[l] = 1

    return counter





def check_parenthesis_consistency_only(string):
    """
    Write an algorithm that determines if the parentheses (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """
    stack = [];

    for l in string :

        if l == '(' :
            stack.append(l)

        elif l == ')' :
            if not stack :
                return False
            stack.pop();

    if len(stack) == 0: 
        return True
    else : 
        return False


def check_any_bracket_consistency(string):
    """
    Write an algorithm that determines if the round brackets "()", square brackets "[]" and curly braces "{}" in a
    string are properly balanced.
    E.g.: "(){}" is OK, "({)}" is not.
    :param string: the string to analyse.
    :return: True if the brackets are balanced, False if not.
    """
    # Write your code here
    stack = [];

    for l in string :

        if( l == '('  or  l == '['  or  l == '{' ):
            stack.append(l)

        elif l == ')' :
            if not stack :
                return False
            e = stack.pop();
            if e != '(':
                return False

        elif l == ']' :
            if not stack :
                return False
            e = stack.pop();
            if e != '[':
                return False

        elif l == '}' :
            if not stack :
                return False
            e = stack.pop();
            if e != '{':
                return False

    if len(stack) == 0: 
        return True
    else : 
        return False
