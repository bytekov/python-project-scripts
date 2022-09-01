PLACEHOLDER_NAME = "Name"

# Open and read receipiant-names file
with open("./Input/Name/invited_names.txt") as file:
    receipiant_names = file.read()
    
    # List [] receipiants names
    receipiants_list = receipiant_names.split()

# Open and read template letter file
with open("./Input/Letter/starting_letter.txt") as file:
    template_letter = file.read()

for item in receipiants_list:
    # Replace placeholder name with receipiant name
    edited_letter = template_letter.replace(PLACEHOLDER_NAME,item)
    
    # Create and save new file with modified letter
    with open(f"Output/{item}.txt", mode="w") as file:
        file.write(edited_letter) 


    


























