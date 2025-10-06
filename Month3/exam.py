answe = 'Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.'
answer = answe.split(" ")
# print(answer)

keywords = ['Photosynthesis', 'light energy', 'chemical energy', 'chloroplasts', 'chlorophyll', 'carbon dioxide', 'water', 'glucose', 'oxygen', 'ATP']

student_answer = input("Answer here: ")
score = 0
for word in keywords:
    if word in student_answer:
        for photo in keywords:
            if photo in student_answer == 'Photosynthesis':
                score += 2
        score += 1

print(f'Your score is {score}')