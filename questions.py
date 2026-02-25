
# This file questions.py is the module
# It creates classes to store data and generate README content 
# It DOSEN'T create questions, handle InquirePy or decide if the readme should be written, these stay in main.py
# the class holds the answers and knows how to turn the answers into a markdown 
# the class has 2 behaviour METHODS, 1 a CONSTRUCTOR, 2 a METHOD THAT RETURNS A MARKDOWN
  
    
    # NB it returns a string it DOES NOT write the file (which means the class is REUSEABLE and TESTABLE)

# 1 a CONSTRUCTOR (__init__) - when I create a readme give it all the answers (defines the ATTRIBUTES of the OBJECT)
# the following are the variables to define the answers that are used below to be put into the markdown

class Readme:
    def __init__(
        self,
        title,
        description,
        installation,
        usage,
        licence,
        author,
        contact
    ):
        self.title = title
        self.description = description
        self.installation = installation
        self.usage = usage
        self.licence = licence
        self.author = author
        self.contact = contact

# 2 a METHOD THAT RETURNS A MARKDOWN 
# generate_markdown() - takes the stored answers (the data stored in the OBJECT, ie 'readme' on main.py)
# forms them into a markdown and returns a single string

# return f"""# {self.title}  builds and returns one large block of text, from the answers for the readme
# then below that eg ## Description {self.description}, is the way the answers appear in the README, 
# the answers are put in the {}, the {}'s are placeholders, anything between the
# """ are treated as part of the string. 


    def generate_markdown(self):
        return f"""# {self.title} 


## Description
{self.description}

## Installation
{self.installation}

## Usage
{self.usage}

## Licence
{self.licence}

## Author
{self.author}

## Contact
{self.contact}
"""
# """ allows text to exist as one multiline string

    
    
    def write_to_file(self, filename="README.md"):
# declares the method and will write to a file called README.md
        content = self.generate_markdown()
# calls the above method generate_markdown (the string) and stroes it in a variable called content
        with open(filename, "w") as file:
# opens the file for writing "w", creating it if it doesnt exist or overwriting it if it does
# 'with' means the file is properly closed when the block ends
            file.write(content)
# writes the Markdown content into the file


# more clarity The __init__ method defines the attributes of the object — the pieces of data the class will hold (title, description, installation, usage, licence, author, contact).
# generate_markdown() is a method that takes those stored attributes and builds one large multi-line Markdown string using f-strings, with the placeholders {self.title}, {self.description}, etc., filled in with the actual user input.
# write_to_file() is another method that calls generate_markdown(), opens a file called README.md (or another filename you specify), and writes the Markdown string into it, safely closing the file afterward.