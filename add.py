intervals = [[80, 81], [1, 2], [1, 2]]
covered_set = set()

for interval in intervals:
    start, end = interval
    for num in range(start, end + 1):
        covered_set.add(num)

result = len(covered_set)
print(result)

#2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeNumbers(n):
    prime_count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count

print(primeNumbers(1))
print(primeNumbers(20))
print(primeNumbers(1000))

#3
import random


with open("Tigrolovi_1370252477.txt", "r", encoding='utf-8') as file:
    text = file.read().lower()


tokens = text.split()


token_dict = {}

for i in range(len(tokens) - 1):
    current_token = tokens[i]
    next_token = tokens[i + 1]
    if current_token not in token_dict:
        token_dict[current_token] = []
    token_dict[current_token].append(next_token)


generated_text = []

current_word = random.choice(list(token_dict.keys()))
generated_text.append(current_word)

for x in range(199):
    if current_word in token_dict:
        next_words = token_dict[current_word]
        current_word = random.choice(next_words)
    else:
        current_word = random.choice(list(token_dict.keys()))
    generated_text.append(current_word)

print(" ".join(generated_text))

#4

students = []
with open("qwer.txt", "r") as file:
    for line in file:
        name, score = line.split()
        students.append((name, int(score)))


total_scores = 0
highest_score = ('', 0)
lowest_score = ('', 100)
score_counts = {}

for name, score in students:
    total_scores += score

    if score > highest_score[1]:
        highest_score = (name, score)

    if score < lowest_score[1]:
        lowest_score = (name, score)

    if score in score_counts:
        score_counts[score] += 1
    else:
        score_counts[score] = 1

average_score = total_scores / len(students)

mode_score = max(score_counts, key=score_counts.get)


with open("results.txt", "w") as file:
    for name, score in students:
        file.write(f"{name} {score}\n")
    file.write("\n")
    file.write(f"Class average score: {average_score:.2f}\n")
    file.write(f"Highest score: {highest_score[0]} {highest_score[1]}\n")
    file.write(f"Lowest score: {lowest_score[0]} {lowest_score[1]}\n")
    file.write(f"Mode score: {mode_score}\n")

