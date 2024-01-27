# Flashy - Language Learning Flashcard App

## Overview

Flashy is a simple language learning flashcard application built using Python's Tkinter library. It allows users to practice and learn new words in a foreign language by presenting flashcards with the translation on the back. Users can indicate whether they know the word or not, and the app keeps track of known and unknown words.

## Features

- Flashcards with German words on the front and English translations on the back.
- Right and Wrong buttons to indicate whether the user knows the word or not.
- Word counts for known and unknown words displayed at the bottom.
- Timer to automatically flip the card after 3 seconds.

## Prerequisites

Make sure you have the necessary dependencies installed before running the application:

- Python (>=3.6)
- pandas
- tkinter (usually included with Python installations)

Install the required packages using the following command:

```bash
pip install pandas
```

## Usage

1. Clone the repository:

```bash
git clone git@github.com:Sakib-Dalal/Flash_Card_Game.git
cd Flash_Card_Game
```

2. Run the application:

```bash
python main.py
```

3. The Flashy app window will appear, and you can start learning and practicing with the flashcards.

## Data Setup

Flashy uses a CSV file (`Language_data.csv`) to store language data. Make sure the file is present in the `data` directory. The CSV file should have columns for German and English words.

## File Structure

- `main.py`: Main script containing the application code.
- `data/Language_data.csv`: CSV file containing language data.
- `images/`: Directory containing card images and button icons.

## Acknowledgments

Flashy was created by Sakib Dalal as a simple language learning tool. Feel free to customize and extend it according to your needs.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README file based on your project structure and additional features. Include any relevant information about the project's purpose, usage, and customization options.
