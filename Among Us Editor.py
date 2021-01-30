import tkinter
from tkinter import ttk, END, BOTTOM, TOP, IntVar

root = tkinter.Tk()
root.title("Hawky's AU Editor")
root.geometry("500x390")
root.resizable(0, 0)
root.iconbitmap("au.ico")

# Please add the location to the among us playerprefs file into the string below.
# The typical windows path will be C:\Users\your_username\AppData\LocalLow\Innersloth\Among Us\playerprefs
among_us_playerprefs_location = ""

# Define fonts and colours
yellow = "#ffe74c"
red = "#F24C00"
orange = "#fc7a1e"
white = "#ffffff"
green = "#6bf178"
blue = "#35a7ff"
grey = "#999478"
main_font = ("Terminal", 15)
modern_font = ("Arial Black", 13)
modern_font_1 = ("Arial", 13)

root.config(bg=red)

# Define hat values in a dict and list
hat_values = {"None": "0",
              "Astronaut Helmet": "1",
              "Backwards Cap": "2",
              "Brain Slug": "3",
              "Bush Hat": "4",
              "Captain Hat": "5",
              "Double Top Hat": "6",
              "Flowerpot Hat": "7",
              "Goggles": "8",
              "Hard Hat": "9",
              "Military Hat": "10",
              "Paper Hat": "11",
              "Party Hat": "12",
              "Police Hat": "13",
              "Stethescope": "14",
              "Top Hat": "15",
              "Towel": "16",
              "Ushanka": "17",
              "Viking": "18",
              "Black Guard Hat": "19",
              "Snowman": "20",
              "Antlers": "21",
              "Christmas Lights": "22",
              "Santa Hat": "23",
              "Christmas Tree Hat": "24",
              "Present Hat": "25",
              "Candy Canes Hat": "26",
              "Elf Hat": "27",
              "Yellow Party Hat": "28",
              "White Hat": "29",
              "Crown": "30",
              "Eyebrows": "31",
              "Angel Halo": "32",
              "Elf Cap": "33",
              "Flat Cap": "34",
              "Plunger": "35",
              "Snorkel": "36",
              "Stickmin Figure": "37",
              "Straw Hat": "38",
              "Sheriff Hat": "39",
              "Eyeball Lamp": "40",
              "Toilet Paper Hat": "41",
              "Toppat Clan Leader Hat": "42",
              "Black Fedora": "43",
              "Ski Goggles": "44",
              "Headphones": "45",
              "Hazmat Mask": "46",
              "Medical Mask": "47",
              "Hat and Glasses": "48",
              "Safari Hat": "49",
              "Banana Hat": "50",
              "Beanie": "51",
              "Bear Ears": "52",
              "Cheese Hat": "53",
              "Cherry Hat": "54",
              "Egg Hat": "55",
              "Green Fedora": "56",
              "Flamingo Hat": "57",
              "Flower Hat": "58",
              "Knight Helmet": "59",
              "Plant Hat": "60",
              "Cat Head Hat": "61",
              "Bat Wings": "62",
              "Devil Horns": "63",
              "Mohawk": "64",
              "Pumpkin Hat": "65",
              "Paper Bag": "66",
              "Witch Hat": "67",
              "Wolf Ears": "68",
              "Pirate Hat": "69",
              "Plague Doctor Mask": "70",
              "Knife Hat": "71",
              "Jason Mask": "72",
              "Mining Hat": "73",
              "Blue Winter Hat": "74",
              "Archaeologist Hat": "75",
              "Antenna": "76",
              "Balloon": "77",
              "Bird Nest": "78",
              "Black Bandanna": "79",
              "Caution Sign Hat": "80",
              "Chef Hat": "81",
              "Blue Guard Hat": "82",
              "Bandanna": "83",
              "Sticky Note": "84",
              "Fez": "85",
              "General Hat": "86",
              "Pompadour": "87",
              "Hunter Hat": "88",
              "Military Helmet": "89",
              "Mini Crewmate": "90",
              "Ninja Mask": "91",
              "Ram Horns": "92",
              "Snow Crewmate": "93",
              "Geoff Kayleigh Hat": "94"}
reverse_hat_values = {"0": "None",
                      "1": "Astronaut Helmet",
                      "2": "Backwards Cap",
                      "3": "Brain Slug",
                      "4": "Bush Hat",
                      "5": "Captain Hat",
                      "6": "Double Top Hat",
                      "7": "Flowerpot Hat",
                      "8": "Goggles",
                      "9": "Hard Hat",
                      "10": "Military Hat",
                      "11": "Paper Hat",
                      "12": "Party Hat",
                      "13": "Police Hat",
                      "14": "Stethescope",
                      "15": "Top Hat",
                      "16": "Towel",
                      "17": "Ushanka",
                      "18": "Viking",
                      "19": "Black Guard Hat",
                      "20": "Snowman",
                      "21": "Antlers",
                      "22": "Christmas Lights",
                      "23": "Santa Hat",
                      "24": "Christmas Tree Hat",
                      "25": "Present Hat",
                      "26": "Candy Canes Hat",
                      "27": "Elf Hat",
                      "28": "Yellow Party Hat",
                      "29": "White Hat",
                      "30": "Crown",
                      "31": "Eyebrows",
                      "32": "Angel Halo",
                      "33": "Elf Cap",
                      "34": "Flat Cap",
                      "35": "Plunger",
                      "36": "Snorkel",
                      "37": "Stickmin Figure",
                      "38": "Straw Hat",
                      "39": "Sheriff Hat",
                      "40": "Eyeball Lamp",
                      "41": "Toilet Paper Hat",
                      "42": "Toppat Clan Leader Hat",
                      "43": "Black Fedora",
                      "44": "Ski Goggles",
                      "45": "Headphones",
                      "46": "Hazmat Mask",
                      "47": "Medical Mask",
                      "48": "Hat and Glasses",
                      "49": "Safari Hat",
                      "50": "Banana Hat",
                      "51": "Beanie",
                      "52": "Bear Ears",
                      "53": "Cheese Hat",
                      "54": "Cherry Hat",
                      "55": "Egg Hat",
                      "56": "Green Fedora",
                      "57": "Flamingo Hat",
                      "58": "Flower Hat",
                      "59": "Knight Helmet",
                      "60": "Plant Hat",
                      "61": "Cat Head Hat",
                      "62": "Bat Wings",
                      "63": "Devil Horns",
                      "64": "Mohawk",
                      "65": "Pumpkin Hat",
                      "66": "Paper Bag",
                      "67": "Witch Hat",
                      "68": "Wolf Ears",
                      "69": "Pirate Hat",
                      "70": "Plague Doctor Mask",
                      "71": "Knife Hat",
                      "72": "Jason Mask",
                      "73": "Mining Hat",
                      "74": "Blue Winter Hat",
                      "75": "Archaeologist Hat",
                      "76": "Antenna",
                      "77": "Balloon",
                      "78": "Bird Nest",
                      "79": "Black Bandanna",
                      "80": "Caution Sign Hat",
                      "81": "Chef Hat",
                      "82": "Blue Guard Hat",
                      "83": "Bandanna",
                      "84": "Sticky Note",
                      "85": "Fez",
                      "86": "General Hat",
                      "87": "Pompadour",
                      "88": "Hunter Hat",
                      "89": "Military Helmet",
                      "90": "Mini Crewmate",
                      "91": "Ninja Mask",
                      "92": "Ram Horns",
                      "93": "Snow Crewmate",
                      "94": "Geoff Kayleigh Hat"}
hat_list = ["None", "Astronaut Helmet", "Backwards Cap", "Brain Slug", "Bush Hat", "Captain Hat",
            "Double Top Hat", "Flowerpot Hat", "Goggles", "Hard Hat", "Military Hat", "Paper Hat",
            "Party Hat", "Police Hat", "Stethoscope", "Top Hat", "Towel", "Ushanka", "Viking", "Black Guard Hat",
            "Snowman", "Antlers", "Christmas Lights", "Santa Hat", "Christmas Tree Hat", "Present Hat",
            "Candy Canes Hat", "Elf Hat", "Yellow Party Hat", "White Hat", "Crown", "Eyebrows", "Angel Halo",
            "Elf Cap", "Flat Cap", "Plunger", "Snorkel", "Stickmin Figure", "Straw Hat", "Sheriff Hat", "Eyeball Lamp",
            "Toilet Paper Hat", "Black Fedora", "Ski Goggles", "Headphones", "Hazmat Mask", "Medical Mask", "Hat and Glasses",
            "Safari Hat", "Banana Hat", "Beanie", "Bear Ears", "Cheese Hat", "Cherry Hat", "Egg Hat", "Green Fedora", "Flamingo Hat",
            "Flower Hat", "Knight Helmet", "Plant Hat", "Cat Head Hat", "Bat Wings", "Devil Horns", "Mohawk",
            "Pumpkin Hat", "Paper Bag", "Witch Hat", "Wolf Ears", "Pirate Hat", "Plague Doctor Mask", "Knife Hat",
            "Jason Mask", "Mining Hat", "Blue Winter Hat", "Archaeologist Hat", "Antenna", "Balloon", "Bird Nest",
            "Black Bandanna", "Caution Sign Hat", "Chef Hat", "Blue Guard Hat", "Bandanna", "Sticky Note", "Fez",
            "General Hat", "Pompadour", "Hunter Hat", "Military Helmet", "Mini Crewmate", "Ninja Mask", "Ram Horns",
            "Snow Crewmate", "Geoff Kayleigh Hat"]

# Define skin values in a dict and list
skin_values = {"No Skin": "0",
               "Astronaut": "1",
               "Captain": "2",
               "Mechanic": "3",
               "Military": "4",
               "Police": "5",
               "Doctor": "6",
               "Black Suit": "7",
               "White Suit": "8",
               "Guard Suit": "9",
               "Hazmat Suit": "10",
               "Security Suit": "11",
               "High Vis  Jacket": "12",
               "Miner Gear": "13",
               "Winter Suit": "14",
               "Archaeologist": "15"}
reverse_skin_values = {"0": "No Skin",
                       "1": "Astronaut",
                       "2": "Captain",
                       "3": "Mechanic",
                       "4": "Military",
                       "5": "Police",
                       "6": "Doctor",
                       "7": "Black Suit",
                       "8": "White Suit",
                       "9": "Guard Suit",
                       "10": "Hazmat Suit",
                       "11": "Security Suit",
                       "12": "High Vis  Jacket",
                       "13": "Miner Gear",
                       "14": "Winter Suit",
                       "15": "Archaeologist"}
skin_list = ["No Skin", "Astronaut", "Captain", "Mechanic", "Military", "Police", "Doctor", "Black Suit", "White Suit",
             "Guard Suit", "Hazmat Suit", "Security Suit", "High Vis Jacket", "Miner Gear",
             "Winter Suit", "Archaeologist"]

# Define pet values in a dict and list
pet_values = {"None": "0",
              "Brain Slug": "1",
              "Mini Crewmate": "2",
              "Dog": "3",
              "Henry Stickman": "4",
              "Hamster": "5",
              "Robot": "6",
              "UFO": "7",
              "Ellie Stickwoman": "8",
              "Squig": "9",
              "Bedcrab": "10",
              "Twitch Follower": "11"}
reverse_pet_values = {"0": "None",
                      "1": "Brain Slug",
                      "2": "Mini Crewmate",
                      "3": "Dog",
                      "4": "Henry Stickman",
                      "5": "Hamster",
                      "6": "Robot",
                      "7": "UFO",
                      "8": "Ellie Stickwoman",
                      "9": "Squig",
                      "10": "Bedcrab",
                      "11": "Twitch Follower"}
pet_list = ["None", "Brain Slug", "Mini Crewmate", "Dog", "Henry Stickman", "Hamster", "Robot", "UFO", "Ellie Stickwoman",
            "Squig", "Bedcrab", "Twitch Follower"]

# Define colour values in a dict and list
colour_values = {"Red": "0",
                 "Blue": "1",
                 "Dark Green": "2",
                 "Pink": "3",
                 "Orange": "4",
                 "Yellow": "5",
                 "Black": "6",
                 "White": "7",
                 "Purple": "8",
                 "Brown": "9",
                 "Teal": "10",
                 "Lime": "11"
                 }
reverse_colour_values = {"0": "Red",
                         "1": "Blue",
                         "2": "Dark Green",
                         "3": "Pink",
                         "4": "Orange",
                         "5": "Yellow",
                         "6": "Black",
                         "7": "White",
                         "8": "Purple",
                         "9": "Brown",
                         "10": "Teal",
                         "11": "Lime"}
colour_list = ["Red", "Blue", "Dark Green", "Pink", "Orange", "Yellow", "Black",
               "White", "Purple", "Brown", "Teal", "Lime"]

darkmode = IntVar()
modern = IntVar()


# Define functions
def get_values():
    """Open the Among Us playerprefs file and get the values, setting the default values of the dropdowns/
    entries to the correct values."""
    with open(among_us_playerprefs_location, "r") as def_file:
        # Get the contents of the file
        contents = def_file.read()
        # Split the contents into a string
        new_contents = contents.split(",")

        name = new_contents[0]

        # Get the names of the values from their respective reverse dictionaries
        hat = reverse_hat_values.get(new_contents[10])
        skin = reverse_skin_values.get(new_contents[15])
        pet = reverse_pet_values.get(new_contents[16])
        colour = reverse_colour_values.get(new_contents[2])

        # Set the entries and dropdowns to the correct values
        dropdown_hat.set(hat)
        dropdown_pet.set(pet)
        dropdown_skin.set(skin)
        dropdown_colour.set(colour)
        name_entry.insert(END, name)


def apply_changes():
    """Open the Among us playerprefs file and apply specified changes."""

    with open(among_us_playerprefs_location, "r") as file:
        # Get the contents of the file
        contents = file.read()
        # Split the contents into a string

        new_contents = contents.split(",")
        # Get the user's input from the comboboxes, and change the indexes to the new values
        user_hat_choice = str(dropdown_hat.get())
        user_skin_choice = str(dropdown_skin.get())
        user_pet_choice = str(dropdown_pet.get())
        user_name_choice = str(name_entry.get())
        user_colour_choice = str(dropdown_colour.get())

        new_contents[0] = user_name_choice
        new_contents[2] = colour_values[user_colour_choice]
        new_contents[10] = hat_values[user_hat_choice]
        new_contents[15] = skin_values[user_skin_choice]
        new_contents[16] = pet_values[user_pet_choice]

    with open(among_us_playerprefs_location, "w") as write_file:
        # Run a loop that rewrites the text file in the correct format with the specified changes.
        for i in range(len(new_contents)):
            write_file.writelines(new_contents[i])
            write_file.writelines(",")


def open_settings():
    """Create a settings window for the user"""
    if darkmode.get() == 0 and modern.get() == 0:
        settings_window = tkinter.Toplevel()
        settings_window.title("Settings")
        settings_window.iconbitmap("au.ico")
        settings_window.geometry("300x300+" + str(root.winfo_x() + 500) + "+" + str(root.winfo_y()))
        settings_window.resizable(0, 0)
        settings_window.config(bg=red)

        settings_label = tkinter.Label(settings_window, bg=orange, text=("Settings:"), font=("Terminal", 25))
        settings_label.pack(padx=5, pady=5, side=TOP)

        settings_frame = tkinter.Frame(settings_window, bg=red)
        settings_confirm_frame = tkinter.Frame(settings_window, bg=red)
        settings_frame.pack(padx=5, pady=5)
        settings_confirm_frame.pack(padx=5, pady=5)

        darkmode_button = tkinter.Checkbutton(settings_frame, text="Dark Mode", font=main_font, bg=orange, variable=darkmode)
        darkmode_button.grid(row=0, column=0, padx=5, pady=5)

        modern_button = tkinter.Checkbutton(settings_frame, text="Modern Look", font=main_font, bg=orange, variable=modern)
        modern_button.grid(row=0, column=1, padx=5, pady=5)

    elif darkmode.get() == 1 and modern.get() == 0:
        settings_window = tkinter.Toplevel()
        settings_window.title("Settings")
        settings_window.iconbitmap("au.ico")
        settings_window.geometry("300x300+" + str(root.winfo_x() + 500) + "+" + str(root.winfo_y()))
        settings_window.resizable(0, 0)
        settings_window.config(bg="black")

        settings_label = tkinter.Label(settings_window, bg="grey", text=("Settings:"), font=("Terminal", 25))
        settings_label.pack(padx=5, pady=5, side=TOP)

        settings_frame = tkinter.Frame(settings_window, bg="black")
        settings_confirm_frame = tkinter.Frame(settings_window, bg="black")
        settings_frame.pack(padx=5, pady=5)
        settings_confirm_frame.pack(padx=5, pady=5)

        darkmode_button = tkinter.Checkbutton(settings_frame, text="Dark Mode", font=main_font, bg="grey", variable=darkmode)
        darkmode_button.grid(row=0, column=0, padx=5, pady=5)

        modern_button = tkinter.Checkbutton(settings_frame, text="Modern Look", font=main_font, bg="grey", variable=modern)
        modern_button.grid(row=0, column=1, padx=5, pady=5)

    elif darkmode.get() == 1 and modern.get() == 1:
        settings_window = tkinter.Toplevel()
        settings_window.title("Settings")
        settings_window.iconbitmap("au.ico")
        settings_window.geometry("300x300+" + str(root.winfo_x() + 500) + "+" + str(root.winfo_y()))
        settings_window.resizable(0, 0)
        settings_window.config(bg="black")

        settings_label = tkinter.Label(settings_window, bg="grey", text=("Settings:"), font=("Arial Black", 25))
        settings_label.pack(padx=5, pady=5, side=TOP)

        settings_frame = tkinter.Frame(settings_window, bg="black")
        settings_confirm_frame = tkinter.Frame(settings_window, bg="black")
        settings_frame.pack(padx=5, pady=5)
        settings_confirm_frame.pack(padx=5, pady=5)

        darkmode_button = tkinter.Checkbutton(settings_frame, text="Dark Mode", font=modern_font_1, bg="grey", variable=darkmode)
        darkmode_button.grid(row=0, column=0, padx=5, pady=5)

        modern_button = tkinter.Checkbutton(settings_frame, text="Modern Look", font=modern_font_1, bg="grey", variable=modern)
        modern_button.grid(row=0, column=1, padx=5, pady=5)

    elif darkmode.get() == 0 and modern.get() == 1:
        settings_window = tkinter.Toplevel()
        settings_window.title("Settings")
        settings_window.iconbitmap("au.ico")
        settings_window.geometry("300x300+" + str(root.winfo_x() + 500) + "+" + str(root.winfo_y()))
        settings_window.resizable(0, 0)
        settings_window.config(bg=red)

        settings_label = tkinter.Label(settings_window, bg=orange, text=("Settings:"), font=("Arial Black", 25))
        settings_label.pack(padx=5, pady=5, side=TOP)

        settings_frame = tkinter.Frame(settings_window, bg=red)
        settings_confirm_frame = tkinter.Frame(settings_window, bg=red)
        settings_frame.pack(padx=5, pady=5)
        settings_confirm_frame.pack(padx=5, pady=5)

        darkmode_button = tkinter.Checkbutton(settings_frame, text="Dark Mode", font=modern_font_1, bg=orange, variable=darkmode)
        darkmode_button.grid(row=0, column=0, padx=5, pady=5)

        modern_button = tkinter.Checkbutton(settings_frame, text="Modern Look", font=modern_font_1, bg=orange, variable=modern)
        modern_button.grid(row=0, column=1, padx=5, pady=5)

    def apply_settings():
        # Handle settings
        if darkmode.get() == 1:
            """Turn every widget to either black or grey"""
            # Root window widgets
            root.config(bg="black")
            choice_frame.config(bg="black")
            confirm_frame.config(bg="black")
            title.config(bg="grey")
            dropdown_hat_label.config(bg="grey")
            dropdown_skin_label.config(bg="grey")
            dropdown_pet_label.config(bg="grey")
            dropdown_colour_label.config(bg="grey")
            name_entry_label.config(bg="grey")
            credit.config(bg="grey")
            apply_button.config(bg="grey")
            settings_button.config(bg="grey")

            # Settings window widgets
            settings_window.config(bg="black")
            settings_label.config(bg="grey")
            darkmode_button.config(bg="grey")
            settings_frame.config(bg="black")
            settings_confirm_frame.config(bg="black")
            modern_button.config(bg="grey")

        elif darkmode.get() == 0:
            """Turn every widget to either red or orange"""
            # Root window widgets
            root.config(bg=red)
            choice_frame.config(bg=orange)
            confirm_frame.config(bg=red)
            title.config(bg=orange)
            dropdown_hat_label.config(bg=orange)
            dropdown_skin_label.config(bg=orange)
            dropdown_pet_label.config(bg=orange)
            dropdown_colour_label.config(bg=orange)
            name_entry_label.config(bg=orange)
            credit.config(bg=orange)
            apply_button.config(bg=orange)
            settings_button.config(bg=orange)

            # Settings window widgets
            settings_window.config(bg=red)
            settings_label.config(bg=orange)
            darkmode_button.config(bg=orange)
            settings_frame.config(bg=red)
            settings_confirm_frame.config(bg=red)
            modern_button.config(bg=orange)

        if modern.get() == 1:
            """Turn the font style to a more modern look"""
            # Root labels
            credit.config(font=("Arial", 15))
            title.config(font=("Arial Black", 20))
            dropdown_colour_label.config(font=modern_font)
            dropdown_pet_label.config(font=modern_font)
            dropdown_skin_label.config(font=modern_font)
            dropdown_hat_label.config(font=modern_font)
            name_entry_label.config(font=modern_font)
            dropdown_hat.config(font=modern_font_1)
            dropdown_skin.config(font=modern_font_1)
            dropdown_pet.config(font=modern_font_1)
            dropdown_colour.config(font=modern_font_1)
            name_entry.config(font=modern_font_1)
            apply_button.config(font=modern_font_1)
            settings_button.config(font=modern_font_1)

            # Settings labels
            settings_label.config(font=("Arial Black", 25))
            darkmode_button.config(font=modern_font_1)
            modern_button.config(font=modern_font_1)

        elif modern.get() == 0:
            """Turn the font style to a retro look"""
            credit.config(font=main_font)
            title.config(font=("Terminal", 25))
            dropdown_colour_label.config(font=main_font)
            dropdown_pet_label.config(font=main_font)
            dropdown_skin_label.config(font=main_font)
            dropdown_hat_label.config(font=main_font)
            name_entry_label.config(font=main_font)
            dropdown_hat.config(font=main_font)
            dropdown_skin.config(font=main_font)
            dropdown_pet.config(font=main_font)
            dropdown_colour.config(font=main_font)
            name_entry.config(font=main_font)

            # Settings labels
            settings_label.config(font=("Terminal", 25))
            darkmode_button.config(font=main_font)
            modern_button.config(font=main_font)
            apply_button.config(font=main_font)
            settings_button.config(font=main_font)

    confirm_button = tkinter.Button(settings_confirm_frame, text="Confirm", font=main_font, bg=white, command=apply_settings)
    confirm_button.pack(padx=5, pady=5)


# Define layout
title_frame = tkinter.Frame(root, bg=orange)
choice_frame = tkinter.Frame(root, bg=orange)
confirm_frame = tkinter.Frame(root, bg=red)

title_frame.pack(padx=5, pady=5)
choice_frame.pack(padx=5, pady=5)
confirm_frame.pack(padx=5, pady=10)

credit = tkinter.Label(root, text="Made by AHawky", font=main_font, bg=orange)
credit.pack(side=BOTTOM)

# Title label
title = tkinter.Label(title_frame, text="Hawky's AU Editor", font=("Terminal", 25), bg=orange)
title.grid(row=1, column=1)

# Create dropdowns with labels and grid them
dropdown_hat_label = tkinter.Label(choice_frame, text="Hat:", font=main_font, bg=orange)
dropdown_hat_label.grid(row=0, column=0, pady=5)
dropdown_hat = tkinter.ttk.Combobox(choice_frame, value=hat_list, font=main_font, justify="center", state="readonly")
dropdown_hat.grid(row=1, column=0, padx=10, pady=10)

dropdown_skin_label = tkinter.Label(choice_frame, text="Skin:", font=main_font, bg=orange)
dropdown_skin_label.grid(row=0, column=1, pady=5)
dropdown_skin = tkinter.ttk.Combobox(choice_frame, value=skin_list, font=main_font, justify="center", state="readonly")
dropdown_skin.grid(row=1, column=1, padx=10, pady=10)

dropdown_pet_label = tkinter.Label(choice_frame, text="Pet:", font=main_font, bg=orange)
dropdown_pet_label.grid(row=2, column=1, pady=5)
dropdown_pet = tkinter.ttk.Combobox(choice_frame, value=pet_list, font=main_font, justify="center", state="readonly")
dropdown_pet.grid(row=3, column=1, padx=10, pady=10)

dropdown_colour_label = tkinter.Label(choice_frame, text="Colour:", font=main_font, bg=orange)
dropdown_colour_label.grid(row=4, column=0)
dropdown_colour = tkinter.ttk.Combobox(choice_frame, value=colour_list, font=main_font, justify="center", state="readonly")
dropdown_colour.grid(row=5, column=0, padx=10, pady=10)

# Create a name entry
name_entry = tkinter.Entry(choice_frame, font=main_font)
name_entry.grid(row=3, column=0, ipadx=9)
name_entry_label = tkinter.Label(choice_frame, text="Name:", font=main_font, bg=orange)
name_entry_label.grid(row=2, column=0, ipadx=9)

# Create an apply button
apply_button = tkinter.Button(confirm_frame, text="Apply", font=main_font, bg=orange, command=apply_changes)
apply_button.grid(row=0, column=1, ipadx=60, padx=30)

settings_button = tkinter.Button(confirm_frame, text="Settings", font=main_font, bg=orange, command=open_settings)
settings_button.grid(row=0, column=2, ipadx=50, padx=30)

get_values()

root.mainloop()
