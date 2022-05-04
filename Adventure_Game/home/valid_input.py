def valid_input(prompt, option1, option2):
    repeater_input = []
    index = 0
    while index <= len(repeater_input):
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif response in repeater_input:
            print("You already enter this input, please try to concentrate.\n")
        else:
            repeater_input.append(str(response))
            index += 1
            print("Sorry, wrong input. Please answer:")
    return response
