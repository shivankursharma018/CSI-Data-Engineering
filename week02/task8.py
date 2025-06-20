# https://www.hackerrank.com/challenges/incorrect-regex/problem
import re
def solve_for_regex():
    num_test_cases = int(raw_input()) 
    for i in range(num_test_cases):
        regex_string = raw_input()
        try:
            re.compile(regex_string)
            print "True" 
        except re.error:
            print "False"
solve_for_regex()