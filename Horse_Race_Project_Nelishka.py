import random
import time

# codes for bold and cyan text.
bold_cyan_text = "\033[1;36m"
reset_format = "\033[0m"

# Title of the program.
print()
print("-" * 149)
print(" " * 65, bold_cyan_text + "~~~~ Rapid Race ~~~~" + reset_format)
print("-" * 149)


# Initializing empty lists to store horse details.
horse_ids = []
horse_names = []
jockey_names = []
horse_ages = []
horse_breeds = []
race_records = []
horse_groups = []


# Create a dictionary to keep track of horse counts for each group. (A, B, C, D)
horse_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

#Create a dictionary to insert horses selected for finals.
horses_for_final = {}



def add_horse_details():
    # Prompt for horse details.
    while True:
        # Validate horse ID in correct data type.
        try:
            while True:
                horse_id = int(input("Enter Horse ID: "))
                # Changing the data type of horse_id to string.
                horse_id = str(horse_id)
                # Checking whether horse ID is taken before.
                if horse_id in horse_ids:
                    print("Horse ID is taken. Try another one")
                else:
                    break
            break
        except:
            print("Invalid input")

    # Input horse name.
    horse_name = input("Enter Horse Name: ")

    # Input jockey name.
    jockey_name = input("Enter Jockey Name: ")

    # Validate age in correct data type.
    while True:
        try:
            horse_age = int(input("Enter horse age: "))
            break
        except:
            print("Invalid input")

    # Input horse breed.
    horse_breed = input("Enter Horse Breed: ")

    # Validate wins and races compete in correct data type.
    while True:
        while True:
            try:
                # Input number of wins.
                win = int(input("Number of Wins: "))
                break
            except:
                print("Invalid input")
        while True:
            try:
                # Input number of races compete.
                races = int(input("Number of races compete: "))
                break
            except:
                print("Invalid input")
        # Checking whether win count greater than compete races count.
        if win <= races:
            # Assign variable called race record.
            race_record = f"{win} wins in {races} races"
            break
        else:
            print("Number of races compete is wrong")
    while True:
        horse_group = input("Enter Horse Group (A, B, C, or D): ").upper()
        # Validate horse group.
        while horse_group not in ["A", "B", "C", "D"]:
            horse_group = input("Invalid group. Enter Horse Group (A, B, C, or D): ").upper()
        # checking whether one group have only 5 horses.
        if horse_counts[horse_group] < 5:
            print("Horse added to group", horse_group)
            # Add horse details to relevant lists.
            horse_ids.append(horse_id)
            horse_names.append(horse_name)
            jockey_names.append(jockey_name)
            horse_ages.append(horse_age)
            horse_breeds.append(horse_breed)
            race_records.append(race_record)
            horse_groups.append(horse_group)

            # Update horse counts for the respective group.
            horse_counts[horse_group] += 1

            print("\nHorse details added successfully!")
            break
        # Checking whether other groups have enough space to insert horse details.
        elif horse_counts['A'] < 5 or horse_counts['B'] < 5 or horse_counts['C'] < 5 or horse_counts['D'] < 5:
            print(f"Cannot add horse to Group {horse_group}. Group is full.")
            print(horse_counts.items())
            print("Try another group")
        else:
            # When all groups are filled display this message.
            print("\nSorry All slots are filled")
            break




def selection_sort(horse_ids, horse_names, jockey_names, horse_ages, horse_breeds, race_records, horse_groups):
    # Sorting algorithm according to ascending order of horse ids.
    n = len(horse_ids)
    for i in range(n - 1):
        # Assign minimum index to i.
        min_index = i
        for j in range(i + 1, n):
            # Convert horse IDs to integers for numerical comparison.
            if int(horse_ids[j]) < int(horse_ids[min_index]):
                # if horse_ids[j]<horse_ids[i] then assign minimum index to j.
                min_index = j

        # Swap the found minimum element with the first element.
        horse_ids[i], horse_ids[min_index] = horse_ids[min_index], horse_ids[i]
        horse_names[i], horse_names[min_index] = horse_names[min_index], horse_names[i]
        jockey_names[i], jockey_names[min_index] = jockey_names[min_index], jockey_names[i]
        horse_ages[i], horse_ages[min_index] = horse_ages[min_index], horse_ages[i]
        horse_breeds[i], horse_breeds[min_index] = horse_breeds[min_index], horse_breeds[i]
        race_records[i], race_records[min_index] = race_records[min_index], race_records[i]
        horse_groups[i], horse_groups[min_index] = horse_groups[min_index], horse_groups[i]


def view_horse_details():
    # Check if any horses are registered.
    if not horse_ids:
        print("\nNo Horses registered yet.")
        return

    # Call sorting algorithm.
    selection_sort(horse_ids, horse_names, jockey_names, horse_ages, horse_breeds, race_records, horse_groups)

    # Display horse details table.
    print("\nHorse Details Table:")
    print("-" * 126)
    # Display column titles.
    print("| {:<9} | {:<20} | {:<20} | {:<9} | {:<15} | {:<20} | {:<11} |".format("Horse ID", "Horse Name", "Jockey Name", "Horse Age", "Horse Breed", "Race Record", "Horse Group"))
    print("-" * 126)

    for i in range(len(horse_ids)):
        # Display horse records according to the given format.
        print("| {:<9} | {:<20} | {:<20} | {:<9} | {:<15} | {:<20} | {:<11} |".format(horse_ids[i], horse_names[i], jockey_names[i], horse_ages[i], horse_breeds[i], race_records[i], horse_groups[i]))

    print("-" * 126)


def update_horse_details():
    # Check if any horses are registered yet.
    if not horse_ids:
        print("\nNo Horses registered yet.")
        return
    # Get update horse ID as user input.
    up_horse_id = input("\nEnter the Horse ID you want to update: ")

    # Check if the entered Horse ID exists in the list.
    if up_horse_id in horse_ids:
        # Find the respective index for the given horse ID.
        up_index = horse_ids.index(up_horse_id)
        # Display a command line menu for user to choose an option.
        while True:
            print("\nChoose relevant number")
            print("Horse Name --> 1")
            print("Jockey Names --> 2")
            print("Horse age --> 3")
            print("Horse Breed --> 4")
            print("Race Records --> 5")
            print("Horse groups --> 6")
            print("Exit --> 7")

            while True:
                try:
                    # Get user input according to the menu.
                    update_option = int(input("\nSelect the option you want: "))
                    break
                except:
                    print("Invalid Input. Try again")
            # Check if is the user input equals to 1.
            if update_option == 1:
                # Get user input and assign new horse name to a variable.
                new_horse_name = input("Enter Horse name: ")
                # Update the new horse name with the respective index.
                horse_names[up_index] = new_horse_name
                print("\nHorse name changed successfully")
            # Check if is the user input equals to 2.
            elif update_option == 2:
                # Get user input and assign new jockey name to a variable.
                new_jockey_name = input("Enter Jockey name: ")
                # Update the new jockey name with the respective index.
                jockey_names[up_index] = new_jockey_name
                print("\nJockey name changed successfully")
            # Check if is the user input equals to 3.
            elif update_option == 3:
                while True:
                    # Validate new horse age in correct data type.
                    try:
                        # Get user input and assign new horse age to a variable.
                        new_horse_age = int(input("Enter Horse age: "))
                        # Update the new horse age with the respective index.
                        horse_ages[up_index] = new_horse_age
                        print("\nHorse age changed successfully")
                        break
                    except:
                        print("\nInvalid Input. Try again")
            # Check if is the user input equals to 4.
            elif update_option == 4:
                # Get user input and assign new horse breed to a variable.
                new_horse_breed = input("Enter Horse breed: ")
                # Update the new horse breed with the respective index.
                horse_breeds[up_index] = new_horse_breed
                print("\nHorse breed changed successfully")
            # Check if is the user input equals to 5.
            elif update_option == 5:
                # Validate wins and races compete in correct data type.
                while True:
                    try:
                        # Get user input and assign new wins count to a variable.
                        new_win = int(input("Number of Wins: "))
                        break
                    except:
                        print("Invalid input")
                while True:
                    try:
                        # Get user input and assign new races compete count to a variable.
                        new_races = int(input("Number of races compete: "))
                        break
                    except:
                        print("Invalid input")
                # Assign new race records to a variable.
                new_race_record = f"{new_win} wins in {new_races} races"
                # Update the new race records with the respective index.
                race_records[up_index] = new_race_record
                print("\nRace record changed successfully")
            # Check if is the user input equals to 6.
            elif update_option == 6:
                # Get user input and assign new horse group to a variable.
                new_horse_group = input("Enter Horse Group (A, B, C, or D): ").upper()
                # Validate horse group.
                while new_horse_group not in ["A", "B", "C", "D"]:
                    new_horse_group = input("Invalid group. Enter Horse Group (A, B, C, or D): ").upper()
                # checking whether one group have only 5 horses.
                if horse_counts[new_horse_group] < 5:
                    # Update horse counts for the old group.
                    horse_counts[horse_groups[up_index]] -= 1
                    print("Horse added to group", new_horse_group)
                    # Add horse to the relevant group.
                    horse_groups[up_index] = new_horse_group
                    print("\nHorse group changed successfully")
                    # Update horse counts for the respective group.
                    horse_counts[new_horse_group] += 1
                # Checking whether other groups have enough space to insert horse details.
                elif horse_counts['A'] < 5 or horse_counts['B'] < 5 or horse_counts['C'] < 5 or horse_counts['D'] < 5:
                    print(f"Cannot add horse to Group {new_horse_group}. Group is full.")
                    # Show user which group have enough space to add horse
                    print(horse_counts.items())
                    print("Try another group")
                else:
                    # When all slots are filled display this message.
                    print("You can't change the group. All slots are filled.")
            # Check if is the user input equals to 7.
            elif update_option == 7:
                break
            else:
                print("Invalid Input. Try again")
    else:
        print("Invalid Horse ID. Please enter valid Horse ID.")



def del_horse_details():
    # Check if any horses are registered yet
    if not horse_ids:
        print("\nNo Horses registered yet.")
        return

    # Get user input which horse ID need to be deleted.
    del_horse_id = input("Enter the Horse ID you want to delete: ")

    # Check if the entered Horse ID exists
    if del_horse_id in horse_ids:
        # Get user confirm to delete horse details.
        del_confirm = input(f"\nAre you sure to delete all the data of Horse with Horse ID {del_horse_id} (Yes or No) ").lower()
        if del_confirm == "yes":
            # Get respective index according to the given horse ID.
            del_index = horse_ids.index(del_horse_id)

            # Remove horse details from lists
            del horse_ids[del_index]
            del horse_names[del_index]
            del jockey_names[del_index]
            del horse_ages[del_index]
            del horse_breeds[del_index]
            del race_records[del_index]
            # Deleting horse group assign to a variable
            del_horse_group = horse_groups[del_index]
            del horse_groups[del_index]

            # Update horse counts for the respective group
            horse_counts[del_horse_group] -= 1
            print(f"\nHorse with Horse ID {del_horse_id} deleted successfully!")
        elif del_confirm == "no":
            print(f"\nDeleting data of Horse with Horse ID {del_horse_id} is cancelled")
        else:
            # If user enter an ID which not in horse ids display this message.
            print("\nInvalid Input, Try again")
    else:
        print(f"\nHorse with Horse ID {del_horse_id} not found.\nTry again with a valid Horse ID")


# Check if race has started
def race_details():
    while True:
        try:
            # Get user input whether race started.
            race_started = input("\nIs race started? (Yes or No) ").lower()
            # Convert input to lowercase for case sensitivity.
            if race_started not in ["yes", "no"]:
                raise ValueError("Your answer should be Yes or No")
            race_started = race_started == "yes"  # Convert the input to  yes or no
            break
        except:
            print("Invalid input.")

    # Allow horse registration only if race hasn't started
    if not race_started:
        if selected_option == "AHD":
            add_horse_details()
        elif selected_option == "DHD":
            del_horse_details()
        elif selected_option == "UHD":
            update_horse_details()
    else:
        # If race started display this message.
        print("Horse registration is not allowed after the race starts.")


def save_horse_details():
    # Open the file in write mode.
    with open('horse_details.txt', 'w') as f:
        # Display horse details table.
        f.write("\nHorse Details Table:")
        f.write(" ")
        f.write("\n| {:<9} | {:<20} | {:<20} | {:<9} | {:<15} | {:<20} | {:<11} |".format("Horse ID", "Horse Name", "Jockey Name", "Horse Age", "Horse Breed", "Race Record", "Horse Group"))
        # Iterate through horse details based on horse IDs and write to the file.
        for i in range(len(horse_ids)):
            f.write("\n| {:<9} | {:<20} | {:<20} | {:<9} | {:<15} | {:<20} | {:<11} |".format(horse_ids[i], horse_names[i], jockey_names[i], horse_ages[i], horse_breeds[i], race_records[i], horse_groups[i]))
    print("Horse details saved to file successfully!")




def read_horse_details_from_file():
    # Read horse details from the text file.
    with open('horse_details.txt', 'r') as f:
        # Reads all lines from the file and stores them in the list variable 'lines'.
        lines = f.readlines()

    # Extract horse details from the lines, skipping the header.
    for line in lines[3:]:  # Skip the header lines
        # Removes whitespaces from the string 'line' and then splits it into fields using the '|'
        fields = line.strip().split('|')
        # Appends data from specific fields of the 'fields' list to their respective lists.
        horse_ids.append(fields[1].strip())
        horse_names.append(fields[2].strip())
        jockey_names.append(fields[3].strip())
        try:
            horse_ages.append(int(fields[4].strip()))
        except ValueError:
            # Handle the case where the age cannot be converted to an integer
            horse_ages.append(0)
        horse_breeds.append(fields[5].strip())
        race_records.append(fields[6].strip())
        horse_groups.append(fields[7].strip())




def select_random_horses(horse_counts, horse_ids, horse_names, jockey_names, horse_ages, horse_breeds, race_records, horse_groups):
    horses_for_final = {}

    # Check if there are enough horses in each group for the final round, at-least one horse in each group.
    if all(count >= 1 for count in horse_counts.values()):
        # Clear existing data otherwise data will duplicate.
        horse_ids.clear()
        horse_names.clear()
        jockey_names.clear()
        horse_ages.clear()
        horse_breeds.clear()
        race_records.clear()
        horse_groups.clear()

        # Read horse details from the text file
        read_horse_details_from_file()

        # Select one random horse from each group
        for group in ["A", "B", "C", "D"]:
            group_horses = []

            # Collect horses in the current group
            for i in range(len(horse_ids)):
                # Checks if the horse group of the horse at index 'i' matches the current group iterated.
                if horse_groups[i] == group:
                    # Appends the index of the horse to the 'group_horses'
                    group_horses.append(i)

            # Ensure that there is at least 1 horse in the group before sampling.
            if len(group_horses) >= 1:
                selected_horse_index = random.choice(group_horses)
                horses_for_final[group] = selected_horse_index

        # Display the details of the randomly selected horses
        print("\nRandomly Selected Horses for the Final Round:")
        print("-" * 126)
        # Display the table column headings.
        print("| {:<9} | {:<20} | {:<20} | {:<9} | {:<15} | {:<20} | {:<11} |".format("Horse ID", "Horse Name", "Jockey Name", "Horse Age", "Horse Breed", "Race Record", "Horse Group"))
        print("-" * 126)

        # Iterates through the items  in the horses_for_final.
        for group, horse_index in horses_for_final.items():
            # Assigns the stored index
            i = horse_index
            # Display horse details at the given index
            print("| {:<9} | {:<20} | {:<20} | {:<9} | {:<15} | {:<20} | {:<11} |".format(horse_ids[i], horse_names[i], jockey_names[i], horse_ages[i], horse_breeds[i], race_records[i], horse_groups[i]))

        print("-" * 126)
    else:
        # Display this message when there are not enough horses in each group.
        print("There are not enough horses in each group for the final round.")

    # Returns the populated 'horses_for_final' dictionary.
    # Ready for further processing.
    return horses_for_final


def selection_sort_race_times(race_times):
    n = len(race_times)
    # Iterate through the list
    for i in range(n - 1):
        min_index = i
        # Find the minimum element in the unsorted part of the list
        for j in range(i + 1, n):
            if race_times[j][1] < race_times[min_index][1]:
                min_index = j

        # Swap the found minimum element with the first element
        race_times[i], race_times[min_index] = race_times[min_index], race_times[i]

    # Return the sorted list
    return race_times


def display_winning_horses(horses_for_final, horse_ids, horse_names, jockey_names):
    # Simulate the race and assign random times to each horse
    race_times = {horse_id: random.randint(1, 90) for horse_id in horses_for_final.values()}

    # Sort race_times based on race times
    sorted_race_times = selection_sort_race_times(list(race_times.items()))

    # Display the details of the winning horses
    print("\nWinning Horses:")
    print("-" * 126)
    print("| {:<9} | {:<20} | {:<20} | {:<9} | {:<9} |".format("Position", "Horse ID", "Horse Name", "Jockey Name", "Race Time"))
    print("-" * 126)

    for position, (horse_index, race_time) in enumerate(sorted_race_times[:4], start=1):  # Display positions from 1 to 4
        i = horse_index
        print("| {:<9} | {:<20} | {:<20} | {:<9} | {:<9}s |".format(position, horse_ids[i], horse_names[i], jockey_names[i], race_time))

    print("-" * 126)

    return race_times




def visualize_winning_horses():
    global race_times

    # Check if the race has been simulated and winning times are available
    if not race_times:
        print("Race simulation has not been conducted. Please run the 'WHD' command first.")
        return

    # Use selection sort for race_times based on race times
    sorted_race_times = selection_sort_race_times(list(race_times.items()))

    # Display the details of the winning horses with visualization
    print("\nVisualizing Winning Horses:")
    print("-" * 126)

    for position, (horse_index, race_time) in enumerate(sorted_race_times[:3], start=1):  # Display positions from 1 to 3
        # Check if horse_index is within the valid range
        if 0 <= horse_index < len(horse_ids):
            # Calculate the number of '*' based on 10s intervals
            num_stars = race_time // 10
            # Display the details of the winning horses
            print(f"{horse_names[horse_index]}: {'*' * num_stars} {race_time}s ({position}st Place)")
        else:
            print(f"Error: Invalid horse index {horse_index}.")

    print("-" * 126)



data_saved = False
final_selected = False
race_ended = False

while True:
    time.sleep(1)
    print("\nCommand Line Menu")
    print("Type AHD for adding horse details")
    print("Type UHD for Update horse details")
    print("Type DHD for deleting horse details")
    print("Type VHD for view horse details")
    print("Type SHD for Save the horse details to text file")
    print("Type SDD for select four horses randomly for the major round")
    print("Type WHD for Display winning horses")
    print("Type VWH for Visualize Winning horses")
    print("Type ESC to Exit the program")
    print(horse_counts.items())

    # Get user input for selected option.
    selected_option = input("Select the option you want: ").upper()

    # Handle different menu options.
    if selected_option == "AHD" or selected_option == "DHD" or selected_option == "UHD":
        # Call race_details() function for adding, deleting, or updating horse details.
        race_details()
    elif selected_option == "VHD":
        # Call view_horse_details() function for viewing horse details.
        view_horse_details()
    elif selected_option == "SHD":
        # call save_horse_details() funtion for save horse details.
        save_horse_details()
        data_saved = True
    elif selected_option == "SDD":
        # Check if data is saved before selecting horses for the major round.
        if not data_saved:
            print("\nPlease save the data first using SHD")
        else:
            # Call select_random_horses() function to select four horses randomly.
            horses_for_final = select_random_horses(horse_counts, horse_ids, horse_names, jockey_names, horse_ages, horse_breeds, race_records, horse_groups)
            final_selected = True
    elif selected_option == "WHD":
        # Check if data is saved and horses are selected for the major round before displaying winning horses.
        if not data_saved:
            print("\nPlease save the data first using SHD")
        elif not final_selected:
            print("\nPlease select final round horses using SDD")
        else:
            # Call display_winning_horses() function to display winning horses.
            race_times = display_winning_horses(horses_for_final, horse_ids, horse_names, jockey_names)
            race_ended = True
    elif selected_option == "VWH":
        # Check if data is saved and the race has ended before visualizing winning horses.
        if not data_saved:
            print("\nPlease save the data first using SHD")
        elif not race_ended:
            print("\nRace didn't start yet. To start the race use WHD")
        else:
            # Call visualize_winning_horses() function to visualize winning horses.
            visualize_winning_horses()
    elif selected_option == "ESC":
        # Exit the program if the user chooses to exit.
        print("Exiting the program")
        break
    else:
        # Print an error message for invalid input.
        print("Invalid input. Please try again.")

