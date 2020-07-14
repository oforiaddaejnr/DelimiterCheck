import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
    stack = Stack()
    text = open(filename, "r")
    open_delimeter = "([{"
    close_delimeter = ")]}"
    match = {")":"(","]":"[","}":"{"} #dictionary to help match popped opening delimiters and closing delimeters
    for line in text:
        string = line
        for char in string:
            if char in open_delimeter:
                stack.push(char)
            elif char in close_delimeter:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() != match[char]:
                        return False
    if len(stack)!= 0:
        return False
    return True
    text.close()

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')
