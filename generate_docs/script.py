import __builtin__
import sys
import os

# Output file paths
builtin_file = 'builtin_functions.txt'
modules_file = 'available_modules.txt'

# Get the list of built-in functions and variables
builtin_functions = dir(__builtin__)

# Write the built-in functions to a text file
f = open(builtin_file, 'w')
for item in builtin_functions:
    f.write(item + '\n')
f.close()

# Save available modules to a file by redirecting sys.stdout temporarily
original_stdout = sys.stdout  # Save original stdout
sys.stdout = open(modules_file, 'w')  # Redirect output to a text file
help('modules')  # This lists all the modules in the system
sys.stdout.close()  # Close the file after writing

# Restore original stdout
sys.stdout = original_stdout

# Print messages to the console
print("Built-in functions saved to %s" % builtin_file)
print("Available modules saved to %s" % modules_file)



# Read the available_modules.txt and create a Python list
modules_list = []

# Open the available modules file
f = open('available_modules.txt', 'r')
lines = f.readlines()
f.close()

# Process each line to extract module names
for line in lines:
    # Skip lines containing non-module text
    if ('Please wait a moment while I gather a list of all available modules...' in line or
        'Enter any module name to get more help.  Or, type "modules spam" to search' in line or
        'for modules whose descriptions contain the word "spam".' in line):
        continue
    
    # Split the line into individual module names
    modules = line.split()
    
    # Add each module name to the list
    for module in modules:
        # Add the module to the list if it's not already there
        if module not in modules_list:
            modules_list.append(module)

# Write the cleaned-up Python list to a new file
f = open('modules_list.py', 'w')
f.write('modules = ' + repr(modules_list) + '\n')
f.close()

print "Modules list saved to 'modules_list.py'"

execfile('generate_docs.py')