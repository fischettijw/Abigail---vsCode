# https://parade.com/944584/parade/trivia-questions-for-kids/

import os
os.system('cls')


def read_questions_from_file(file_path):
    # n: ['',('', '', '', ''),a]
    global questions
    next_line = '\n     '
    questions = {0: [f'How many legs does a spider have?', (6, 8, 10, 12), 1],
                 1: [f'What is the name of the toy cowboy{next_line}in Toy Story?', ('Jesse', 'Peter', 'Woody', 'Alan'), 2],
                 2: [f'What is the color of an emerald?', ('red', 'yellow', 'blue', 'green'), 3],
                 3: [f'What is something you hit with a{next_line}hammer?', ('nail', 'wood', 'plastic', 'glass'), 0],
                 4: [f'What’s the name of a place you go to{next_line}see lots of animals?', ('park', 'school', 'zoo', 'forest'), 2],
                 5: [f'Whose nose grew longer every time he{next_line}lied?', ('Frosty', 'Pinocchio', 'Wicked Witch', 'Cinderella'), 1],
                 6: [f'What is the name of the fairy in{next_line}Peter Pan?', ('Tinkerbell', 'Tiny', 'Fairy', 'Little One'), 0],
                 7: [f'If you freeze water, what do you get?', ('Play-Doh', 'Jelly', 'Peanut Butter', 'Ice'), 3]
                 }


def displayQuestion(num):
    global questions
    dash_line = "\n" + "-" * 50
    if num in questions:
        print(f'# {num} ', questions[num][0],
              f'({questions[num][2]}){dash_line}')
        ans_num = 0
        for options in questions[num][1]:
            print(str(ans_num), '- ', options)
            ans_num += 1
    else:
        print(f'# {num} - ', 'Requested question is not in file')
    print()
    ans_num = 0


questions = []
read_questions_from_file('file')

os.system('cls')
print("\nAbigail's Trivia Program\n")
for k in range(0, len(questions)):  # range(0,4)    range(0,len(questions) + 1)
    displayQuestion(k)
