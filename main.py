# Takeru Shimizu ID:011075878
from track import Track
from packages import Packages

# Main loop to run the delivery simulation.
while True:
    # Input for the end time of delivery in HH:MM format.
    time = input("Please input ending time of the delivery in HH:MM format ")
    hour, minute = time.split(":")  # Splitting the input time into hours and minutes.
    hour = int(hour)
    minute = int(minute)

    # Creating instances of Track for three different tracks.
    track1 = Track()
    track2 = Track()
    track3 = Track()

    # Assigning package IDs to each track.
    track1_package_ids = [1, 4, 7, 13, 14, 15, 16, 20, 21, 29, 30, 34, 37, 39, 40]
    track2_package_ids = [3, 5, 6, 18, 25, 26, 31, 32, 36, 38]
    track3_package_ids = [2, 8, 9, 10, 11, 12, 17, 19, 22, 23, 24, 27, 28, 33, 35]

    # Loading package information.
    packages_info = Packages()

    # Assigning packages to each track.
    track1.assign_package(track1_package_ids, packages_info, "Track 1")
    track2.assign_package(track2_package_ids, packages_info, "Track 2")
    track3.assign_package(track3_package_ids, packages_info, "Track 3")

    # Setting departure times for each track.
    print("Track 1 depart at 08:00")
    print("Track 2 depart at 09:05")
    print("Track 3 depart at 10:20")
    track1.set_time(8, 0)
    track2.set_time(9, 5)
    track3.set_time(10, 20)

    # Starting the delivery process for each track.
    track1.deliver((hour, minute))
    track2.deliver((hour, minute))
    track3.deliver((hour, minute))

    # Each track returns to the hub after delivery.
    track1.back_to_hub()
    track2.back_to_hub()
    track3.back_to_hub()

    # Printing the status of all packages after the delivery process.
    packages_info.print_status_all()

    # Calculating and displaying the total distance traveled by all tracks.
    print(
        f"Total distance traveled: {track1.miles + track2.miles + track3.miles} miles"
    )

    # Prompt for the user to continue or exit the program.
    yes_or_no = input("Please type y or n to continue the program or not ")
    if yes_or_no == "n":
        break  # Exit the loop and end the program if the user inputs 'n'.
