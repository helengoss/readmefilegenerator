from InquirerPy import inquirer

# Project title
title = inquirer.text("What's your project title?").execute()

# Confirm yes/no
confirm = inquirer.confirm("Confirm?").execute()

# Description
description = inquirer.text("Enter project description:").execute()
description_confirm = inquirer.confirm("Confirm?").execute()

# Installation instructions
installation = inquirer.text("Enter installation instructions:").execute()
installation_confirm = inquirer.confirm("Confirm?").execute()

# Usage information
usage = inquirer.text("Enter usage information:").execute()
usage_confirm = inquirer.confirm("Confirm?").execute()

# Dropdown example
choice = inquirer.select(
    "Select a licence:",
    choices=["MIT Licence", 
             "GNU General Public Licence (GPL v3)", 
             "GNU Lesser General Public Licence (LGPL v3)", 
             "Mozilla Public Licence 2.0", 
             "Creative Common (CC0/CC BY/variants)", 
             "No license"]
).execute()

# Authors Name
author = inquirer.text("Enter author's name:").execute()
author_confirm = inquirer.confirm("Confirm?").execute()

# Contact information
contact = inquirer.text("Enter contact information:").execute()
contact_confirm = inquirer.confirm("Confirm?").execute()

# Print all results
print(f"Project title: {title}")
print(f"Confirmed: {confirm}")
print(f"Description: {description} (Confirmed: {description_confirm})")
print(f"Installation: {installation} (Confirmed: {installation_confirm})")
print(f"Usage: {usage} (Confirmed: {usage_confirm})")
print(f"You selected: {choice}")
print(f"Author: {author} (Confirmed: {author_confirm})")
print(f"Contact: {contact} (Confirmed: {contact_confirm})")


if confirm:
    readme_content = f"""# {title}

## Description
{description}

## Installation
{installation}

## Usage
{usage}

## Licence
{choice}

## Author
{author}

## Contact
{contact}
"""

    with open("README.md", "w") as file:
        file.write(readme_content)

    print("README.md has been generated successfully.")
else:
    print("README generation cancelled by user.")
