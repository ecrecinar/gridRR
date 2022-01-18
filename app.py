from matplotlib.style import available
import grid_rr as grr
from datetime import datetime
import data_processing as dp


def ask_dataset():
    datasets = dp.get_datasets()
    str = "Available datasets: "
    for i in range(len(datasets)):
        if i == len(datasets) - 1:
            str += datasets[i]
        else:
            str += datasets[i] + ","
    print(str)
    dataset = input("Choose a dataset: ")
    while dataset not in datasets:
        dataset = input("Dataset not recognized.\nChoose a dataset: ")
    return dataset


def ask_step_size():
    try:
        step_size = float(input("Enter step size (1-1000): "))
    except:
        print("Please enter a number.")
        step_size = -1
    while step_size < 1 or step_size > 1000:
        print("\nStep size must be between 1 and 1000.")
        try:
            step_size = float(input("Enter step size (1-1000): "))
        except:
            print("Please enter a number.")
    return step_size


def ask_rr_prob():
    try:
        rr_prob = float(input("Enter RR probability (0.0-1.0): "))
    except:
        print("Please enter a number.")
        rr_prob = -1
    while rr_prob < 0 or rr_prob > 1:
        print("\nRR probability must be between 0.0 and 1.0.")
        try:
            rr_prob = float(input("Enter RR probability (0.0-1.0): "))
        except:
            print("Please enter a number.")
    return rr_prob


def ask_start_end_times():
    while True:
        try:
            start = input(
                "Enter start date and time in GMT (ex. \"Jan 17 2022 10:00AM\", leave empty for all data.): ") + " -0000"
            if start == " -0000":
                return 0, 9999999999
            start_timestamp = datetime.strptime(
                start, '%b %d %Y %I:%M%p %z').timestamp()
            break
        except:
            print("Format error. Please try again.")

    try:
        end = input(
            "Enter end date and time in GMT (ex. \"Jan 17 2022 10:15AM\"): ") + " -0000"
        end_timestamp = datetime.strptime(
            end, '%b %d %Y %I:%M%p %z').timestamp()
    except:
        print("Format error. Please try again.")
        end_timestamp = -1

    while end_timestamp < start_timestamp:
        try:
            end = input(
                "Enter end date and time in GMT (ex. \"Jan 17 2022 10:15AM\"): ") + " -0000"
            end_timestamp = datetime.strptime(
                end, '%b %d %Y %I:%M%p %z').timestamp()
        except:
            print("Format error. Please try again.")
            end_timestamp = -1

    return start_timestamp, end_timestamp


def ask_show_result():
    show_result = input("Show results? (y/n): ")
    while show_result != "y" and show_result != "n":
        print("\nPlease enter y or n.")
        show_result = input("Show results? (y/n): ")
    if show_result == "y":
        return True
    else:
        return False


while True:
    user_input = input("Enter command. Type \"help\" for a list of commands.\n> ")
    if user_input == "help":
        print("\nCommands:")
        print("run: Run an experiment.")
        print("help: Show this list.")
        print("about: Show about info.")
        print("exit: Exit out of the program.\n")
    elif user_input == "run":
        print("")
        dataset = ask_dataset()
        step_size = ask_step_size()
        rr_prob = ask_rr_prob()
        start_time, end_time = ask_start_end_times()
        show_result = ask_show_result()
        print("Running the experiment with step_size = " +
              str(step_size) + ", rr_prob = " + str(rr_prob))
        print("...")
        grr.run(dataset, step_size, rr_prob, show_result, start_time, end_time)
        print("Finished.")
    elif user_input == "about":
        print("\nGridRR was developed by Ecre Çınar and Michael Bora Sanuk as the final")
        print("project for the COMP430: Data Privacy and Security course, Fall 2021.\n")
    elif user_input == "exit":
        print("Bye!")
        break
    else:
        print("Unkown command.")
