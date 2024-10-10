import random

# Load Turkish words from a text file
with open('turkish_words', 'r', encoding='utf-8') as file:
    turkish_words = file.read().splitlines()

def generate_poem():
    num_lines = random.randint(5, 20)  # Random number of lines between 5 and 20
    poem_lines = []
    for _ in range(num_lines):
        # Randomly choose line length between 5 and 10
        line_length = random.randint(5, 10)
        # Create a line by choosing random words
        line = ' '.join(random.choice(turkish_words) for _ in range(line_length))
        poem_lines.append(line)

    return '\n'.join(poem_lines)

# Generate and print a random poem
poem = generate_poem()

# Print the formatted poem
print("=== Generated Poem ===")
print("\n".join(f"{line:^50}" for line in poem.split('\n')))  # Center each line