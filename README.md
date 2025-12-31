# AutoReg — Automated Web Registration Tool

Small Python utility to automate web registration flows using saved user details.

## Overview

AutoReg reads registration data from `user_details.json` and automates submission to a target web form via `main.py`.

## Files

- `main.py` — entry point for the automation script.
- `user_details.json` — JSON file that contains the user information and any configuration required by the script.

## Requirements

- Python 3.8 or newer
- If the project uses any external libraries, install them via a `requirements.txt` in the same folder. If none exists, the script currently relies only on the standard library.

## Setup

1. Ensure Python is installed and on your PATH.
2. (Optional) Create a virtual environment:

   python -m venv venv
   venv\Scripts\activate

3. If a `requirements.txt` file exists, install dependencies:

   pip install -r requirements.txt

## Configuration (`user_details.json`)

`user_details.json` should contain the registration details the script will use. Example structure (adjust to match `main.py` expectations):

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password": "your-password",
  "target_url": "https://example.com/register"
}

Edit the file with appropriate values before running the script.

## Usage

Run the script from the project folder:

```
python main.py
```

Watch the console for output and any prompts. If `main.py` requires additional arguments, pass them accordingly.

## Notes

- Review `main.py` to confirm what keys the script expects in `user_details.json` and to see any optional flags.
- If the automation uses a browser automation tool (e.g., Selenium), ensure the required driver (e.g., ChromeDriver) is installed and available.

## Next steps

- Add a `requirements.txt` if external packages are required.
- Add example `user_details.example.json` with full key list to make configuration easier.

## License

Add your preferred license or keep for private use.
