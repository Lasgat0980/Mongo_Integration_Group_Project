
# Group Members: Lastazia Dickens and Jonathan Haynes
# Date: November 19, 2026
# Project: GitHub Archive Hub - MongoDB Integration
# Objective: Create a Python application that uses MongoDB to
# import, manage, and analyze GitHub Archive data.

from pymongo import MongoClient
import json
import os

# Connect to the MongoDB database
dbLink = "mongodb://localhost:27017/"
client = MongoClient(dbLink)

# Select the database and collection
db = client["GitHubArchiveHub"]
commitsCollection = db["Commits"]

# Check the MongoDB connection
try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB!")
except Exception as error:
    print("Could not connect to MongoDB.")
    print(error)


# Import JSON data into MongoDB
def import_json(filename):
    try:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            count = 0
            records = []

            for line in file:
                data = json.loads(line)
                records.append(data)
                count += 1

                if len(records) == 1000:
                    commitsCollection.insert_many(records)
                    records = []

            if records:
                commitsCollection.insert_many(records)

        print(f"Successfully imported {count} records from {filename}.")

    except FileNotFoundError:
        print(f"File not found: {filename}")

    except json.JSONDecodeError:
        print(f"Invalid JSON data in {filename}")


# CREATE - Add a new record to MongoDB
def create_record(key, value):
    # Use the key as the record's unique ID
    value["_id"] = key

    commitsCollection.insert_one(value)
    print(f"Record '{key}' created successfully.")


# READ - Retrieve a record from MongoDB
def read_record(key):
    query = {"_id": key}
    record = commitsCollection.find_one(query)

    if record:
        print(record)
    else:
        print(f"Record '{key}' not found.")


# UPDATE - Modify an existing record in MongoDB
def update_record(key, value):
    query = {"_id": key}
    new_values = {"$set": value}

    result = commitsCollection.update_one(query, new_values)

    if result.matched_count > 0:
        print(f"Record '{key}' updated successfully.")
    else:
        print(f"Record '{key}' not found.")

# DELETE - Remove a record from MongoDB
def delete_record(key):
    query = {"_id": key}

    result = commitsCollection.delete_one(query)

    if result.deleted_count > 0:
        print(f"Record '{key}' deleted successfully.")
    else:
        print(f"Record '{key}' not found.")


# Display the main menu
def display_menu():
    print("\nGitHub Archive Hub - MongoDB")
    print("1. Import JSON Data")
    print("2. Create a Record")
    print("3. Read a Record")
    print("4. Update a Record")
    print("5. Delete a Record")
    print("6. Commit Message Analysis")
    print("7. Top Contributors")
    print("8. Most Active Repositories")
    print("9. Exit")


# Allow users to select an option
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            filename = input("Enter JSON filename: ")
            import_json(filename)

        elif choice == "2":
            key = input("Enter record key: ")

            try:
                value = json.loads(input("Enter record value as JSON: "))
                create_record(key, value)

            except json.JSONDecodeError:
                print("Invalid JSON format. Please try again.")

        elif choice == "3":
            key = input("Enter record key: ")
            read_record(key)

        elif choice == "4":
            key = input("Enter record key: ")

            try:
                value = json.loads(input("Enter new record value as JSON: "))
                value.pop("_id", None)
                update_record(key, value)

            except json.JSONDecodeError:
                print("Invalid JSON format. Please try again.")

        elif choice == "5":
            key = input("Enter record key: ")
            delete_record(key)

        elif choice == "6":
            print("Commit Message Analysis will be added next.")

        elif choice == "7":
            print("Top Contributors will be added by the group.")

        elif choice == "8":
            print("Most Active Repositories will be added by the group.")

        elif choice == "9":
            print("Exiting application.")
            client.close()
            break

        else:
            print("Invalid choice. Please try again.")


# Start the application
if __name__ == "__main__":
    main()




