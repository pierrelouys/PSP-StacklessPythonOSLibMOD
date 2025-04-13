import sys
import os
import pydoc

# Create a folder to store documentation
if not os.path.exists('docs'):
    os.mkdir('docs')

# Import the modules list from the file generated in Step 2
from modules_list import modules

# Function to generate and save documentation for a module
def save_module_doc(module_name):
    try:
        # Try importing the module first
        __import__(module_name)
        
        # Generate the HTML documentation
        html_doc = pydoc.HTMLDoc().docmodule(sys.modules[module_name])
        
        # Prepare the filename to save the doc
        filename = os.path.join('docs', module_name + '_doc.html')
        
        # Open the file and write the HTML content
        f = open(filename, 'w')
        f.write(html_doc)
        f.close()
        print "Documentation for %s saved to %s" % (module_name, filename)
    except ImportError:
        print "Module %s not found!" % module_name
    except Exception, e:
        print "An error occurred with module %s: %s" % (module_name, str(e))

# Loop through all modules in the list and generate documentation for each
for module in modules:
    save_module_doc(module)
