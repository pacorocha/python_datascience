def NULL_not_found(object: any) -> int:
    match object:
        case None:
            print("Nothing: ", object, type(object))
        case float():
            print("Cheese: ", object, type(object))
            return 0
        case int():
            if isinstance(object, bool):
                print("Fake: ", object, type(object))
                return 0
            else:
                print("Zero: ", object, type(object))
                return 0
        case str():
            if object == '':
                print("Empty: ", object, type(object))
                return 0
            else:
                print("Type not Found")
                return 1


