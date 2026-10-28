"""
    group_project2.py.


    "Adventurer's Quest Back Home"
    Elena, Simplicio,


"""

# Global inventory list to track player items across different story paths
inventory: list[str] = []

def get_choice(prompt: str, valid_options: list[str]) -> str:
    """
    If the user puts in an invalid answer, this function tells them and helps them fix it.

    Parameters
    ----------
    prompt : str
        
    valid_options : list[str]
        This is a list that will show what options the user has after putting in the wrong input.

    Returns
    -------
    str
        

    Raises
    ------
    ValueError
        Tells the user that the input cannot be empty if they do not put anything in the terminal.
    """
    while True:
            user_input: str = input(prompt).strip()
            
            # Raising an error to communicate bad state between logic blocks
            if not user_input:
                raise ValueError("Input cannot be empty.")
                
            if user_input in valid_options:
                return user_input
                
            print(f"Invalid choice. Please select from your options: {', '.join(valid_options)}")
            

# ----- Ending Functions -----

def game_over() -> bool:
    """
    Prompts the player to restart or exit the game loop.


    Returns:
        bool: True if the user wants to replay, False otherwise.
    """
    print("\nWould you like to play again?")
    choice: str = get_choice("Enter 1 for Yes or 2 for No: ", ["1", "2"])

    if choice == "1":
        return True
    return False
# ----- Story Functions -----

def examine_keys() -> None:
    """
    Simulates a multi-attempt lock-picking puzzle using a while loop.


    Requires the user to select the correct key out of 4 options.
    """
    print("\nYou find that 4 of the keys have the same patterns on the door.")

    attempts: int = 0
    max_attempts: int = 3
    door_locked: bool = True

   # Added a while loop to allow multiple attempts before failing
    while door_locked and attempts < max_attempts:
        print(f"\nWhich key will you try? (Remaining attempts: {max_attempts - attempts})")
        key_num: str = get_choice("Choose a key (1-4): ", ["1", "2", "3", "4"])

        if key_num == "2":
            print("\nKey number 2 works!")
            print("You have unlocked the door but the walls start shaking and you see a clock on the wall.")
            print("You look at the clock and see words carved into the wall right next to it.")
            print("The words have the same style as the symbols so you go over and read them.")
            text: str = "You have 1 minute to get across without the  "
            symbols: str = "\x1B[3m" + text + "\x1B[0m"
            print(symbols)
            door_locked = False
        else:
            print(f"Key number {key_num} did not work.")
            attempts += 1

    if door_locked:
        print("\nYour time ran out! The lock jams completely.")
        print("THE END")

def leave_shack() -> None:
   """
   Triggers an unavoidable combat failure state when leaving the safe area.
   """
   print("\nYou turn around to go back but find that a flying")
   print("Sand Scorpion had followed you in and was blocking the path.")
   print("You have no choice but to try and fight it,")
   print("but its reflexes are too fast and the venomous stinger")
   print("impales your neck.")
   print("With no one around to save you, your journey has come to an end.")
   print("THE END")




def break_door() -> None:
   """
   Triggers a physical failure state if the user brute-forces the door.
   """
   print("\nAfter cracking the door a little bit while kicking it,")
   print("you try to run and bust through it.")
   print("The attempt fails and you end up busting your head open")
   print("and become unconscious.")
   print("THE END")




def check_it_out() -> None:
    """
    Handles the basement discovery event.
    Populates the player's inventory list with items needed for subsequent scenes.
    """
    print("\nYou look around among the rabble of the shack")
    print("and find an old door and a box of keys.")
    print("Buried under some wood, you pick up the keys")


    # Added dynamic state tracking to conditionally modify gameplay options later
    if "Mysterious Keys" not in inventory:
        inventory.append("Mysterious Keys")
        print("[System: 'Mysterious Keys' added to your inventory!]")


    print("You try to open the door, only to find that it is locked.")
    print("You spot symbols on the door that you missed before.")
    print("They remind you of the magical symbols that appeared")
    print("beneath you in the abandoned cave.")
    print("You're not an expert at magic but you know your way")
    print("around casting visual runes.")


    print("\nWhat will you do next?")
    print("1. Examine keys closer")
    print("2. Leave the shack and try to get home")
    print("3. Try and break down the door")


    choice: str = get_choice("\nChoose 1, 2, or 3: ", ["1", "2", "3"])


    if choice == "1":
        if "Mysterious Keys" in inventory:
           examine_keys()
        else:
            print("You don't have the keys to examine!")
    elif choice == "2":
        leave_shack()
    elif choice == "3":
        break_door()




def dont_go() -> None:
   """
   Triggers an ambush failure state if the player rests in an unsafe zone.
   """
   print("\nIt is late, and rather than check out the creepy noise,")
   print("you decide to find a place in the shack to rest.")
   print("You find an old cot laying in the corner and decide to sleep on it.")
   print("What you didn't know was that cot belonged to a dangerous spectre!")
   print("The spectre puts its hands around your neck and chokes you to death.")
   print("OOPS THE END")




def light_fire() -> None:
   """
   Triggers a timed environmental monster event inside the shack.
   """
   print("\nYou use your sword and a rock to spark a fire on some wood.")
   print("As the room begins to light you see scrolls scattered on the floor.")
   print("You see that some of them are maps!")
   print("In hopes that you can find a map to get back home,")
   print("you spend hours searching the shack, inevitably until it gets dark outside.")
   print("You hear a roaring sound far away.")
   print("Then the ground begins to tremble beneath your bare feet.")
   print("While walking you find a house.")
   print("As you're close to the house, the deep rumble grows louder,")
   print("shaking the dust off the window glass.")
   print("Then when you turn around, a creature is standing there")
   print("and bites your head off...")
   print("THE END")




def call_out() -> None:
   """
   Branches the narrative into the exploration or avoidance paths of the house.
   """
   print("\nYou call out 'Hello? Is anyone there?'")
   print("You hear a draft coming from under the floor.")
   print("There is probably a basement.")


   print("\nWhat will you do now?")
   print("1. Find the basement and check it out")
   print("2. Definitely don't go down there")


   choice: str = get_choice("\nChoose 1 or 2: ", ["1", "2"])


   if choice == "1":
       check_it_out()
   elif choice == "2":
       dont_go()




def fight_scorpions() -> None:
   """
   Triggers a premature combat failure state if battling early enemies.
   """
   print("\nYou pull your sword out and begin swinging at them!")
   print("You quickly find out you're not built for this...")
   print("They grab you by your harness and fly you high above clouds,")
   print("and one of them stabs you in the back with poison.")
   print("You begin hallucinating and losing consciousness")
   print("until you inevitably drop to your gruesome death.")
   print("THE END")




def abandoned_shack() -> None:
   """
   Branches the initial safe house narrative between vision and communication options.
   """
   print("\nYou just barely make it to the shack.")
   print("It's dark and eerily quiet.")
   print("You grow wary and need to make a decision.")


   print("\nWhat do you do next?")
   print("1. Light a fire to see")
   print("2. Call out to see if anyone is there")


   choice: str = get_choice("\nChoose 1 or 2: ", ["1", "2"])


   if choice == "1":
       light_fire()
   elif choice == "2":
       call_out()




# ----- Main Game Loop -----




def play_game() -> None:
   """
   Executes the core intro narrative structure and branches the starting choices.
   """
   print("\n===================================")
   print("Adventurer's Quest Back Home")
   print("===================================")


   print("\nYou are a young adventurer trying to make a living.")
   print("While on a simple quest to hunt goblins in an abandoned cave,")
   print("magical circles suddenly appear from under you!")
   print("You are abruptly teleported to an unknown desert in the Demon Realm!")


   print("\nFlying Sand Scorpions see you and start flying towards you.")
   print("You look around and see an abandoned shack in the distance.")


   print("\nWhat do you choose to do?")
   print("1. Run towards the abandoned shack")
   print("2. Pull your sword to fight the Sand Scorpions!")


   choice: str = get_choice("\nChoose 1 or 2: ", ["1", "2"])


   if choice == "1":
       abandoned_shack()
   elif choice == "2":
       fight_scorpions()




# Execution loop controlling application restart logic
while True:
   # Clear out items from the last run so a restarted game has a fresh state
   inventory.clear()
  
   play_game()


   print("\n===================================")
   print("Your adventure has ended.")
   print("===================================")


   if not game_over():
       print("\n===================================")
