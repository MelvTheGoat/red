
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

siblings = ["Ken", "Jack", "Ivy"]
waitlist.extend(siblings)
print("\n\nStage 2")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

groom_ex_classmate = ["Noah", "Oliver"]
waitlist.extend(groom_ex_classmate)
print("\n\nStage 3")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

confirmed_guests.pop(0)
confirmed_guests.append(waitlist[0])
print("\n\nStage 4")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

print("\n\nStage 5")
charlie = confirmed_guests.index("Charlie")
print("Charlie is at number:", charlie)
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

confirmed_guests.pop(1)
confirmed_guests.pop(4)
print("\n\nStage 6")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

waitlist.pop(0)
waitlist.pop(0)
confirmed_guests.append(waitlist[0][1])
print("\n\nStage 7")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

confirmed_guests.pop(-1)
waitlist.pop(2)
print("\n\nStage 8")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)


print("\n\nStage 9")
last_3 = confirmed_guests[5:]
print("Last 3:", last_3)
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

confirmed_guests.append(waitlist[1])
waitlist.pop(1)
print("\n\nStage 10")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

number_of_people = len(confirmed_guests)
print("\n\nStage 11")
print("Number Of People:", number_of_people)
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

print("\n\nStage 12")
confirmed_guests.sort()
print(", ".join(confirmed_guests))
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

del confirmed_guests[8]
del confirmed_guests[3]
confirmed_guests.insert(3, "Collins")
print("\n\nStage 13")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

guests_list_for_caterer = confirmed_guests.copy()
print("\n\nStage 14")
print("Guests List For Caterer:", guests_list_for_caterer)
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)

waitlist.clear()
print("\n\nStage 15")
print("Confirmed guests:", confirmed_guests)
print("Waitlist:", waitlist)