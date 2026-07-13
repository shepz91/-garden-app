"""User input field for selected which season and plant type"""
season = input("What season is it?")  # TODO: Replace with input() to allow user interaction.
plant_type = input("What type of plant?")  # TODO: Replace with input() to allow user interaction.

"""variable for storing selected advice"""
advice = ""

"""if/else statment for selecting advice based on user season input"""
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

"""if/else statment for selecting advice based on user plant type input"""
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

"""Prints the combined seasonal advise and plant type advise for user to see"""
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
