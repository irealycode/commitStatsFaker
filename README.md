# Git Commit Faker

This repository contains a Python script that generates random Git commits throughout the year to populate your GitHub contribution graph. The script is useful for showcasing activity or testing commit statistics visualization.

## Features

- Creates **random commits** throughout the year.
- Allows customization of the number of commits.
- Automatically updates a specified file to simulate meaningful changes.
- Supports random dates and times for commit logs.
- Commits are pushed directly to the `main` branch.

## Prerequisites

- Python 3.6 or later
- Git installed on your system
- A configured Git repository with remote access

## How It Works

The script:
1. Modifies a specified file (`your_file.txt`) by appending unique lines.
2. Stages changes using `git add`.
3. Generates random dates and times within the year.
4. Commits changes with the specified random date using `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`.
5. Pushes the commits to the remote `main` branch.

## Usage

1. Clone or initialize a Git repository:
   ```bash
   git init
   git remote add origin <your-repository-url>
