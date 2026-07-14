# School Vacancy Monitor

A Python automation that monitors available school transfer vacancies on the Rio de Janeiro **Matrícula Fácil** portal and sends Telegram notifications.

I created this project because I needed to transfer from the afternoon shift to the morning shift. Since checking the website manually several times a day is repetitive and time-consuming, I automated the process.

The script can run locally or automatically through **GitHub Actions**, allowing monitoring even when my computer is turned off.

## Features

- Automated form filling with Selenium
- Searches for transfer vacancies
- Telegram notifications
- GitHub Actions support
- Environment variables for sensitive data

## Technologies

- Python
- Selenium
- GitHub Actions
- python-dotenv
- Requests
- Telegram Bot API

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/school-vacancy-monitor.git
cd school-vacancy-monitor
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
MATRICULA=YOUR_ENROLLMENT_NUMBER
DATANASCIMENTO=DDMMYYYY
NOMEALUNO=YOUR_FULL_NAME
NOMEMAE=YOUR_MOTHER_NAME

INDEXANO=6
INDEXMUNICIPIO=50
INDEXBAIRRO=27

TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
```

For GitHub Actions, configure the same values as repository Variables/Secrets.

## Running

```bash
python main.py
```

## Notes

This project was built specifically for the **Matrícula Fácil** portal.

Anyone who wants to test it should use their own credentials and update the selection indexes according to their desired education level, municipality, and neighborhood. The indexes may differ depending on the available options shown by the website.

## Disclaimer

This project is intended for educational purposes and personal automation. It does not modify any information on the website; it only automates vacancy checks and sends notifications.
