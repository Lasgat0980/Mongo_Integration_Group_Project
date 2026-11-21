# GitHub Archive Hub - MongoDB Integration

## Application Description

GitHub Archive Hub is a Python application developed as a group project to store, manage, and analyze data from the GitHub Archive dataset using MongoDB. The application includes an interactive menu that allows users to import JSON data and perform Create, Read, Update, and Delete (CRUD) operations.

The application also includes three analysis features that examine commit messages, identify top contributors, and display the most active repositories based on commit activity.

## Group Members

- Lastazia Dickens
- Jonathan Haynes

## Technologies Used

- Python 3
- MongoDB Community Server
- MongoDB Compass
- PyMongo
- JSON
- Python IDLE
- GitHub and GitHub Desktop

## Installation and Setup

1. Install Python 3 and MongoDB Community Server.
2. Make sure the MongoDB server is running on your computer.
3. Install the PyMongo library using the following command:

   `pip install pymongo`

4. Download or clone the GitHub repository.
5. Download and extract the provided GitHub Archive dataset.
6. Open `mongo_app.py` in Python IDLE.
7. Press F5 to run the application.

The application connects to MongoDB using:

`mongodb://localhost:27017/`

It uses the `GitHubArchiveHub` database and the `Commits` collection.

## Application Menu

1. Import JSON Data
2. Create a Record
3. Read a Record
4. Update a Record
5. Delete a Record
6. Commit Message Analysis
7. Top Contributors
8. Most Active Repositories
9. Exit

## Current Features

**JSON Import:** Reads newline-delimited JSON records and imports them into MongoDB in batches of 1,000.

**Create Record:** Allows users to add a new record to MongoDB.

**Read Record:** Retrieves an existing record using its unique ID.

**Update Record:** Modifies information in an existing record.

**Delete Record:** Removes a record from MongoDB.

**Interactive Menu:** Allows users to select application functions without modifying the Python code.

## Analysis Features

The application includes three additional features that analyze commit activity using records stored in the MongoDB `Commits` collection.

**Commit Message Analysis:** Examines commit messages and counts how many contain the terms "fix," "add," and "update." It also displays the total number of commits containing messages.

**Top Contributors:** Uses the author information in the dataset to identify the ten contributors with the highest number of commits. Results are displayed in descending order.

**Most Active Repositories:** Uses the repository names in the dataset to identify the ten repositories with the highest number of commits. Results are displayed in descending order.

All three analysis features have been implemented and successfully tested using the imported `Commits.json` dataset.

## Dataset

The application uses the GitHub Archive dataset provided for the course project.

The `Commits.json` file was successfully imported into the MongoDB `Commits` collection, containing 25,000 records.

When importing data, users can enter `Commits.json` if the file is saved in the same folder as `mongo_app.py`. Alternatively, they can enter the full file path if the dataset is stored elsewhere on their computer. Users should avoid importing the same dataset multiple times because duplicate records may affect the analysis results.

## Testing

The following features have been successfully tested:

- MongoDB database connection
- JSON import of 25,000 records
- Create, Read, Update, and Delete (CRUD) operations
- Interactive menu navigation
- Commit Message Analysis
- Top Contributors
- Most Active Repositories
- Invalid menu selection handling
- Application exit

The imported records were verified using MongoDB Compass. All three analysis features executed successfully and displayed results using the MongoDB `Commits` collection.


The group plans to complete the three analysis features, test the full application, and continue improving its functionality and documentation.

The README will be updated as additional features are implemented and tested.
