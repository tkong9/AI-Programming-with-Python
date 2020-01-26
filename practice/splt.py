participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

# for i in range(len(completion)):
#     if completion[i] in participant:
#         participant.remove(completion[i])

answer = ''
participant_dict = dict()
completion_dict = dict()

for element in participant:
    participant_dict[element] = 1

for element in completion:
    completion_dict[element] = 1

for key in completion_dict.keys():
    if key in participant_dict:
        participant_dict.pop(key)
for key in participant_dict.keys():
    answer += key

print(answer)
