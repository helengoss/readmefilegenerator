# In this whole CLI (Command Line Interface - runningnsoley in the terminal) tool/utility has
# Python as the core language, the foundation that handles variables, data structures, 
# classes, file I/O, logic, and flow control, creating the Readme class, storing the user input, 
# generating the Markdown string, writing to a file.
# InquirerPy is a library (which uses its own functions, classes, and methods) built on top of Python. Its job is very specific: it makes it easy 
# to create interactive command-line prompts like text input, yes/no confirms, or drop-down selections.
# when you see inquirer.text or inquirer.select/test/confirm thats inquirerpy

from InquirerPy import inquirer
from questions import Readme #tells this page to read the MODULE questions.py file


# this code asks the user questions using InquirerPy and calls the CLASS (defined in the MODULE questions.py) to write the file
def main():
    # Project title
    title = inquirer.text("What's your project title?").execute()
    confirm = inquirer.confirm("Confirm project title?").execute()
    if not confirm:
        print("README generation cancelled.")
        return

    # Description
    description = inquirer.text("Enter project description:").execute()
    if not inquirer.confirm("Confirm description?").execute():
        print("README generation cancelled.")
        return

    # Installation instructions
    installation = inquirer.text("Enter installation instructions:").execute()
    if not inquirer.confirm("Confirm installation instructions?").execute():
        print("README generation cancelled.")
        return

    # Usage information
    usage = inquirer.text("Enter usage information:").execute()
    if not inquirer.confirm("Confirm usage information?").execute():
        print("README generation cancelled.")
        return

    # Licence selection
    licence = inquirer.select(
        message="Select a licence:",
        choices=[
            "MIT Licence",
            "GNU General Public Licence (GPL v3)",
            "GNU Lesser General Public Licence (LGPL v3)",
            "Mozilla Public Licence 2.0",
            "Creative Commons (CC0 / CC BY)",
            "Unlicensed"
        ]
    ).execute()

    # Author name
    author = inquirer.text("Enter author's name:").execute()
    if not inquirer.confirm("Confirm author name?").execute():
        print("README generation cancelled.")
        return

    # Contact information
    contact = inquirer.text("Enter contact information:").execute()
    if not inquirer.confirm("Confirm contact information?").execute():
        print("README generation cancelled.")
        return

    # Create Readme object
    readme = Readme(
        title=title,
        description=description,
        installation=installation,
        usage=usage,
        licence=licence,
        author=author,
        contact=contact
    )

    # Write README.md
    readme.write_to_file()
    print("README.md has been generated successfully.")

# this next line this line ensures that the program starts running your main function 
# only when you run main.py directly, keeping the file safe to import elsewhere without 
# immediately executing the code. Python uses this convention for clean, modular scripts.
if __name__ == "__main__":
    main()

    # InquirerPy Library (https://inquirerpy.readthedocs.io/)
    # InquirerPy has it own “library reference” for the module. 
    # This is where you can see all the prompt types 
    # (text(), confirm(), select() 
    # what arguments they take, 
    # and how to call methods like .execute()

# The wholelibrary also will show you;
# How to import the module (from InquirerPy import inquirer)
# Examples of asking questions, confirming input, and selecting from choices
# All the prompt types you can use
# Tips for advanced features like key bindings, default values, and stylingips 
# for advanced features like key bindings, default values, and styling