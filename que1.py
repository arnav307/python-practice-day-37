def strings(name,surname):
    try:
        concatinate= name+surname
        print(concatinate)
    except TypeError:
        print("you cannot concatenate int or any other datatype except string")
strings("arnav","ghimire")
