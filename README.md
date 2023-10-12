# Get-Email-and-User-Name-from-URL-And-Export-CSV
# Email Extractor

A simple Python script with a GUI built using tkinter to extract unique email addresses from a given website URL.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [License](#license)
- [Author](#author)

## Description

The Email Extractor is a Python script designed to scrape email addresses from a specified webpage and store them in a CSV file. It removes duplicate email addresses and creates a CSV
with two columns: the original email address and a modified version without numbers.

## Features

- Extracts email addresses from a webpage.
- Removes duplicate email addresses.
- Saves data to a CSV file in the user's Downloads folder.
- Provides a simple user interface using tkinter.

## Requirements

- Python 3.x
- The `requests` library

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/email-extractor.git
cd email-extractor
```

2. Install the required Python libraries:

```bash
pip install requests
```

## Usage

1. Run the script:

```bash
python email_extractor.py
```

2. A GUI window will open, prompting you to input the following information:
   - Website URL: Enter the URL from which you want to extract email addresses.
   - Output filename (without extension): Choose a name for the CSV file where the results will be stored.

3. Click the "Extract Emails" button.

4. The script will extract the email addresses, remove duplicates, and save the data to a CSV file in your Downloads folder.

## Important Notes

- The script appends to the CSV file, so if you use the same output filename, the data will be added to the existing file.
- Each time you extract emails, a new CSV file is created with a unique filename.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- Shahbaz Riaz Abasi (https://github.com/shahbazabbasi414)

Feel free to contribute and improve this project by submitting issues and pull requests. Happy email extracting!
```

Remember to replace "your-username" and "email-extractor" with your actual GitHub username and repository name. You can further customize the README by adding images,
 examples, or any other information you think would be helpful to users and contributors.
