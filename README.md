# Sotto_EventRegistrationFormatter-

# Event Registration Formatter

## Description
A Python console application built for school event registration. It collects messy student inputs—such as names, sections, and numeric dates—and cleans them into a standardized, readable registration summary.

## Features
- **Input Cleaning:** Removes accidental leading and trailing spaces using `.strip()`.
- **Text Standardization:** Formats full names and event titles into Title Case (`.title()`), and converts sections and name codes to uppercase (`.upper()`).
- **Date Formatting:** Converts numeric year, month, and day inputs into a human-readable date format (e.g., `June 3, 2026`) using Python's built-in `datetime` module.

## How to Run
1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:
   ```bash
   python event_registration.py
