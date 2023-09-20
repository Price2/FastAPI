# Simple SQL Database API

A simple API project that manages products and categories in a SQL database.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
- [API Response Structure](#api-response-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This project provides a RESTful API to manage products and categories in a SQL database. It allows you to perform various operations such as adding, retrieving, and updating products and categories.

## Features

- Retrieve a list of categories.
- Retrieve a list of products.
- Retrieve a product by its ID.
- Retrieve products by category ID.
- Add a new product.
- Update an existing product.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

```bash
# Clone the repository and change into the project directory
git clone https://github.com/yourusername/simple-sql-database-api.git
cd simple-sql-database-api

# Create and activate a virtual environment (optional but recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Unix/Linux:
source venv/bin/activate

# Install the required dependencies from the requirements.txt file
pip install -r requirements.txt

# Configure your database connection in the config.py file

# Initialize the database schema
python init_db.py

# Start the FastAPI application
uvicorn main:app --reload
