def get_dict_value(dct, path):
    keys = path.split(".")

    current = dct

    for key in keys:
        if key in current:
            current = current[key]
        else:
            return None

    return current

dct = {
    "student": {
        "roll_number": "10",
        "class": "1st"
    },
    "teacher": {
        "school": "LPU"
    }
}

m = int(input("Enter number of paths: "))

for i in range(m):
    path = input("Enter path: ")
    print(get_dict_value(dct, path))