student_scores = {
    "Barry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for name in student_scores:
    if student_scores[name] > 90:
        student_scores[name] = "Outstanding"
    elif student_scores[name] > 80 and student_scores[name] <= 90:
        student_scores[name] = "Exceeds Expectations"
    elif student_scores[name] > 70 and student_scores[name] <= 80:
        student_scores[name] = "Acceptable"
    else:
        student_scores[name] = "Fail"


print(student_scores)





order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])