# GitHub Archive Hub - MongoDB Integration

## Application Description

GitHub Archive Hub is a Python application developed as a group project to store, manage, and analyze data from the GitHub Archive dataset using MongoDB. The application includes an interactive menu that allows users to import JSON data and perform Create, Read, Update, and Delete (CRUD) operations.

The project also includes plans for three analysis features that will help users explore commit messages, contributor activity, and repository activity.

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

## Analysis Features in Development

The following features are included in the menu but are not yet fully implemented:

- **Commit Message Analysis:** Analyze commit messages for common terms such as fixes, additions, and updates.
- **Top Contributors:** Identify contributors with the highest number of commits.
- **Most Active Repositories:** Identify repositories with the most commit activity.

## Dataset

The application uses the GitHub Archive dataset provided for the course project.

The `Commits.json` file was successfully imported into the MongoDB `Commits` collection, containing 25,000 records.

Users must provide the location of the JSON file on their own computer when selecting the import option.

## Testing

The following features have been successfully tested:

- MongoDB database connection
- JSON data import
- Create operation
- Read operation
- Update operation
- Delete operation
- Interactive menu

The imported records were also verified using MongoDB Compass.

## Future Development

The group plans to complete the three analysis features, test the full application, and continue improving its functionality and documentation.

The README will be updated as additional features are implemented and tested.
