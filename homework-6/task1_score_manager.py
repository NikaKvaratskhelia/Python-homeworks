scores = []

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

print(f"Initial scores: {scores}")

scores.remove(45)
print(f"Scores after removing 45: {scores}")

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print(f"Average score: {average_score}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")

scores.sort()
print(f"Sorted scores: {scores}")

passed_scores = [score for score in scores if score >= 60]
print(f"Passed scores: {passed_scores}")
