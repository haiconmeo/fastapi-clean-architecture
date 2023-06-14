# autopep8: off

from pybars import Compiler
import os
import sys
import argparse
sys.path.append(".")
from app.helper.string_case import pascalize, singularize


template_files = []
parser = argparse.ArgumentParser(description='Generate file from template.')
parser.add_argument('resource', help='resource name')
args = parser.parse_args()
module = args.resource
# module_path = os.mkdir(f'app/modules/{module}')

template_folder = 'cli/module'
path_folder = 'app/modules'

for root, dirs, files in os.walk(template_folder):
    for file in files:
        # Get the absolute file path

        file_path = os.path.join(root, file)

        # Add the file path to the list of template files
        template_files.append(file_path)

# Compile each template and generate files
compiler = Compiler()
for template_file in template_files:
    with open(template_file, 'r') as f:
        template_source = f.read()
    template = compiler.compile(template_source)

    # Prepare the data for rendering
    model = singularize( pascalize(module))
    data = {
        'name': module,
        'model': model,
    }

    # Render the template with the data
    rendered = template(data)

    # Get the output file path by replacing 'templates' in the template file path
    # with the desired output folder name
    output_folder = f'app/modules/{module}'
    output_file_path = template_file.replace(template_folder, output_folder)
    output_file_path = output_file_path.replace('hbs', 'py')
    if '{{name}}' in output_file_path:
        output_file_path = output_file_path.replace("{{name}}", module)
    # Create the output folder if it doesn't exist
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Write the rendered content to the output file
    with open(output_file_path, 'w') as f:
        f.write(rendered)


    print(f"File '{output_file_path}' created successfully.")

# add model
with open('app/db_model.py', 'a') as file:
    file.write(f'from app.modules.{module}.model import {model}\n')
# add router

with open('app/router.py', 'a') as file:
    file.write(f'from app.modules.{module} import {module}_router\n')
with open('app/router.py', 'a') as file:
    file.write(f'api_router.include_router({module}_transport.get_router(),prefix="/{module}", tags=["{module}"])\n')
