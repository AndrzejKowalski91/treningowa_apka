import sqlite3


def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('exercise_database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a table to store exercises
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            description TEXT,
            equipment_needed TEXT,
            weightlifting BOOLEAN,
            score INTEGER
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def add_exercise():
    # Prompt the user for exercise details
    name = input("Enter the exercise name: ")
    category = input("Enter the exercise category (Metabolic, Weightlifting, Gymnastic): ")

    # Check if the exercise is Weightlifting
    weightlifting = category.lower() == 'weightlifting'

    # Prompt for equipment only if it's a weightlifting exercise
    if weightlifting:
        equipment_options = ["kettlebells", "dumbbells", "barbell", "all"]

        print("Equipment options:", ', '.join(equipment_options))
        equipment_needed = input("Enter the equipment needed (separate multiple options with commas): ")

        # Handle the case where "all" is selected
        if "all" in equipment_needed.lower():
            equipment_needed = ', '.join(equipment_options[:-1])  # Exclude "all"
        else:
            equipment_needed = ', '.join(option.strip() for option in equipment_needed.split(','))

        while not all(option.strip() in equipment_options for option in equipment_needed.split(',')):
            print("Invalid equipment. Choose from:", ', '.join(equipment_options))
            equipment_needed = input("Enter the equipment needed (separate multiple options with commas): ")

    else:
        equipment_needed = None

    description = input("Enter the exercise description: ")
    score = int(input("Enter the exercise score: "))

    # Connect to SQLite database
    conn = sqlite3.connect('exercise_database.db')
    cursor = conn.cursor()

    # Insert the exercise data into the table
    cursor.execute('''
        INSERT INTO exercises (name, category, description, equipment_needed, weightlifting, score)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, category, description, equipment_needed, weightlifting, score))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()

    # Allow the user to add exercises
    while True:
        add_exercise()
        more_exercises = input("Do you want to add another exercise? (yes/no): ")
        if more_exercises.lower() != 'yes':
            break