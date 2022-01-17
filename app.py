import grid_rr as grr


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
    user_input = input("Enter command. Type \"help\" for help.\n> ")
    if user_input == "help":
        print("Commands:")
        print("run: Run the experiment.")
        print("exit: Exit out of the program.\n")
    elif user_input == "run":
        step_size = ask_step_size()
        rr_prob = ask_rr_prob()
        show_result = ask_show_result()
        print("Running the experiment with step_size = " +
              str(step_size) + ", rr_prob = " + str(rr_prob))
        print("...")
        grr.run(step_size, rr_prob, show_result)
        print("Finished.")
    elif user_input == "exit":
        print("Bye!")
        break
