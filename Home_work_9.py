phone_list = dict()

def input_error(func):
    def inner(text):
        try:
            func(text)
        except IndexError: 
            result = "Give me name and phone please"
            return result
        except KeyError:
            result = "Such a name does not exist"
            return result
        except:
            result = "Something went wrong. Try again"
            return result
        else:
            result = func(text)
            return result     
    return inner

@input_error
def add_phone(text):
    text_list = text.strip().split()
    phone_list[text_list[1]] = text_list[2]
    return "Done!"

@input_error
def change_phone(text):
    text_list = text.strip().split()
    phone_list[text_list[1]] = text_list[2]
    return "Phone number has been changed!"

@input_error
def phone_number(text):
    text_list = text.strip().split()
    return "Phone number is " + phone_list[text_list[1]]

def main():
    while True:
        text_new = input()
        text = text_new.lower()
        if "good bye" in text or "close"in text or "exit" in text:
            print("Good bye!")
            break
        elif "hello" in text:
            print("How can I help you?")
        elif "add" in text:
            print(add_phone(text_new))
        elif "change" in text:
            print(change_phone(text_new))
        elif "phone" in text:
            print(phone_number(text_new))
        elif "show all" in text:
            for name, phone in phone_list.items():
                print(name, phone)
        else:
            print("I don't understand. Please, say again")
        

if __name__ == '__main__':
    main()
