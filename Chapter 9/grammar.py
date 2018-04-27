# Grammar module
# Helps ensure sentences are put together correctly.

def comma_and(list_of_objects):
    """ Take a list of objects with .name attributes and create sentence. """
    sentence = ""
    try:
        for obj in list_of_objects:
            if obj == list_of_objects[(len(list_of_objects)-1)]:
                sentence += obj.name.title()
            elif obj == list_of_objects[(len(list_of_objects)-2)]:
                sentence += obj.name.title() + ' and '
            else:
                sentence += obj.name.title() + ', '
        return sentence
    except:
        for obj in list_of_objects:
            if obj == list_of_objects[(len(list_of_objects)-1)]:
                sentence += obj.title()
            elif obj == list_of_objects[(len(list_of_objects)-2)]:
                sentence += obj.title() + ' and '
            else:
                sentence += obj.title() + ', '
        return sentence

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("Press enter key to exit.")
