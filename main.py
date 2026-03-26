import random

quotes = [
    "Discipline beats motivation.",
    "Stay consistent, results will follow.",
    "Winners focus on winning.",
    "Small steps daily = big results.",
    "You either win or you learn.",
    "Focus on progress, not perfection.",
    "Your habits define your future."
]

print("\n🔥 Motivation Generator 🔥")

name = input("\nEnter your name: ")

print(f"\nHey {name}, here's your motivation:\n")
print(random.choice(quotes))
