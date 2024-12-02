import time

# username and password
USER_CREDENTIALS = {"username": "gymrats", "password": "123456"}

def login():
    print("Welcome to the Real World Guys!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
        print("Login successful, start grinding!\n")
        return True
    else:
        print("Invalid username or password. Please try again.\n")
        return False

# Function to display a list of exercises
def display_exercises():
    print("\n--- Available Gym Exercises ---")
    print("1. Chest Day")
    print("2. Legs Day")
    print("3. Back Day")
    print("4. Biceps Day")
    print("5. Triceps Day")
    print("6. Shoulders Day")
    print("7. Cardio")
    print("8. Exit")

# Function to track an individual exercise
def track_exercise(exercise_name):
    sets = int(input(f"\nHow many sets of {exercise_name} would you like to do? "))
    reps = int(input(f"How many reps per set of {exercise_name}? "))
    
    print(f"\nStarting {exercise_name} workout...\n")
    
    total_reps = sets * reps
    
    for set_number in range(1, sets + 1):
        print(f"\nSet {set_number} of {sets}")
        input(f"Press Enter to start set {set_number} of {exercise_name}...")
        
        print(f"\nSet {set_number} of {exercise_name} complete!")
        
        if set_number < sets:
            rest_time = int(input("How long would you like to rest between sets (in seconds)? "))
            print(f"Resting for {rest_time} seconds...")
            time.sleep(rest_time)  # Rest period between sets
            print(f"Rest time is over. Let's go to set {set_number + 1}!\n")
    
    print(f"\nWorkout complete! You did {total_reps} reps of {exercise_name}.\n")

# Function to display and track Chest Day exercises
def chest_day():
    print("\n--- Chest Day Exercises ---")
    print("1. Bench Press")
    print("2. Incline Dumbbell Press")
    print("3. Dumbbell Flyes")
    print("4. Cable Chest Fly")

    choice = input("\nSelect an exercise for Chest Day (1-4): ")
    if choice == "1":
        track_exercise("Bench Press")
    elif choice == "2":
        track_exercise("Incline Dumbbell Press")
    elif choice == "3":
        track_exercise("Dumbbell Flyes")
    elif choice == "4":
        track_exercise("Cable Chest Fly")
    else:
        print("Invalid choice, please try again.")

# Function to display and track Legs Day exercises
def legs_day():
    print("\n--- Legs Day Exercises ---")
    print("1. Squats")
    print("2. Romanian Deadlifts")
    print("3. Leg Press")
    print("4. Leg Extension")

    choice = input("\nSelect an exercise for Legs Day (1-4): ")
    if choice == "1":
        track_exercise("Squats")
    elif choice == "2":
        track_exercise("Romanian Deadlifts")
    elif choice == "3":
        track_exercise("Leg Press")
    elif choice == "4":
        track_exercise("Leg Extension")
    else:
        print("Invalid choice, please try again.")

# Function to display and track Back Day exercises
def back_day():
    print("\n--- Back Day Exercises ---")
    print("1. Seated Cable Row")
    print("2. Lat Pulldown")
    print("3. Deadlift")
    print("4. Pull-ups")

    choice = input("\nSelect an exercise for Back Day (1-4): ")
    if choice == "1":
        track_exercise("Seated Cable Row")
    elif choice == "2":
        track_exercise("Lat Pulldown")
    elif choice == "3":
        track_exercise("Deadlift")
    elif choice == "4":
        track_exercise("Pull-ups")
    else:
        print("Invalid choice, please try again.")

# Function to display and track Biceps exercises
def biceps_day():
    print("\n--- Biceps Day Exercises ---")
    print("1. Cable Curl")
    print("2. Hammer Curl")
    print("3. Preacher Curl")
    print("4. Dumbbell Curl")

    choice = input("\nSelect an exercise for Biceps Day (1-4): ")
    if choice == "1":
        track_exercise("Cable Curl")
    elif choice == "2":
        track_exercise("Hammer Curl")
    elif choice == "3":
        track_exercise("Preacher Curl")
    elif choice == "4":
        track_exercise("Dumbbell Curl")
    else:
        print("Invalid choice, please try again.")

# Function to display and track Triceps exercises
def triceps_day():
    print("\n--- Triceps Day Exercises ---")
    print("1. Tricep Pushdown")
    print("2. Tricep Extension")
    print("3. Diamond Pushups")
    print("4. Dips")

    choice = input("\nSelect an exercise for Triceps Day (1-4): ")
    if choice == "1":
        track_exercise("Tricep Pushdown")
    elif choice == "2":
        track_exercise("Tricep Extension")
    elif choice == "3":
        track_exercise("Diamond Pushups")
    elif choice == "4":
        track_exercise("Dips")
    else:
        print("Invalid choice, please try again.")

# Function to display and track Shoulders exercises
def shoulders_day():
    print("\n--- Shoulders Day Exercises ---")
    print("1. Lateral Raise")
    print("2. Dumbbell Front Raise")
    print("3. Dumbbell Shoulder Press")
    print("4. Shrugs")

    choice = input("\nSelect an exercise for Shoulders Day (1-4): ")
    if choice == "1":
        track_exercise("Lateral Raise")
    elif choice == "2":
        track_exercise("Dumbbell Front Raise")
    elif choice == "3":
        track_exercise("Dumbbell Shoulder Press")
    elif choice == "4":
        track_exercise("Shrugs")
    else:
        print("Invalid choice, please try again.")

# Main function to start the fitness tracker
def fitness_tracker():
    # Ask the user to log in first
    if not login():
        return  # Exit if login fails
    
    while True:
        display_exercises()
        
        # Get user input to select an exercise or exit
        choice = input("\nSelect an exercise (1-8): ")

        if choice == "1":
            chest_day()
        elif choice == "2":
            legs_day()
        elif choice == "3":
            back_day()
        elif choice == "4":
            biceps_day()
        elif choice == "5":
            triceps_day()
        elif choice == "6":
            shoulders_day()
        elif choice == "7":
            print("\nCardio exercises can be tracked manually.")
            # You can implement Cardio tracking logic here
        elif choice == "8":
            print("\nWhat seems impossible today will one day become your warm-up. Well Done Champ!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the fitness tracker program
if __name__ == "__main__":
    fitness_tracker()

