available_parts = ['computer',
                   'moniter',
                   'keyboard',
                   'mouse',
                   'hdmi cable',
                   'dvd drive',
                   ]
valid_choices = []
for i in range(1 , len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = '-'
computer_parts = [] #create an empty list

available_parts.sort()

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice)
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
             print("adding {}".format(current_choice))
             computer_parts.append(chosen_part)
        print('your list now contains: {}'.format(computer_parts))
    else:
        print('please add options from the lists below:')
        for number , part in enumerate(available_parts):
            print('{0}:{1}'.format(number + 1 ,part))


    current_choice = input()

print(computer_parts)
