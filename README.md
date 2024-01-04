# FilesOrganizer

Welcome to FilesOrganizer, an automation tool designed to streamline the organization of your files and maintain an orderly workspace on your computer. This readme will guide you through the setup and usage of FilesOrganizer.

## Overview

FilesOrganizer is a Python-based automation tool that helps you sort and manage your files effectively. Upon execution, it interacts with you by asking a series of questions to understand your organizational preferences and then carries out the task accordingly. This ensures that your computer remains a well-organized and efficient working environment.

## Features

- Interactive: Asks questions to tailor the organization process to your needs.
- Customizable paths: Set up specific paths for different file types or purposes.
- Python 3.19.3 based: Utilizes the latest features of Python for efficient performance.

## Requirements

FilesOrganizer is built using Python 3.19.3 and the following libraries:

- DateTime==5.1
- python-dotenv==1.0.0
- pytz==2023.3
- zope.interface==6.0

You can easily install these dependencies using the provided `requirements.txt` file.

## Installation

1. **Python Installation**: Ensure you have Python 3.19.3 installed on your system. If not, download and install it from the official [Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone this repository to your local machine or download the source code.

3. **Install Dependencies**: Navigate to the project directory and run the following command to install the necessary libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**: Create a `.env` file in the root directory of the project and add the following environment variables:

   ```
   FINAL_DESTINY=
   SOURCE_DESTINY=
   BASE_TAXES_PATH=
   BASE_DOING_PATH=
   BASE_DONE_PATH=
   ```

   Fill in the values according to your specific paths and preferences.

## Usage

To run FilesOrganizer, navigate to the project directory in your terminal and execute the following command:

```bash
python main.py
```

The automation will initiate and ask you a series of questions to understand how you wish to organize your files. Answer these questions, and FilesOrganizer will start organizing your files according to your specifications.

## Best Practices

- **Backup Data**: Always ensure you have backups of your important files before running any automation tool.
- **Test on a Small Scale**: Initially, run the tool on a small set of files to ensure it works as expected before scaling up.
- **Keep Your Python Updated**: Regularly update your Python installation to the latest version to ensure compatibility and security.
- **Regularly Update Environment Variables**: Keep the paths in your `.env` file updated according to your current directory structure and needs.
