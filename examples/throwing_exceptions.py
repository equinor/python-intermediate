while True:
    user_input = input("Please enter an integer: ")
    if 'q' in user_input:
        print('Thank you, goodbye.')
        break
    try:
        int_user_input = int(user_input)
    except ValueError:
        print("Sorry, I didn't understand that, please enter an integer.")
        continue
    else:
        break