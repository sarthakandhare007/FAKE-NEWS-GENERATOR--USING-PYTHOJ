import tkinter as tk
import random

# Data sources
subjects = [ 
    "The Prime Minister visits",
    "Virat Kohli, the cricketer",
    "India, the land of spirituality",
    "An aunty eats an apple",
    "Sumit rides a bicycle",
    "Neesha travels to Jaipur"
]

actions = [
    "launches a surprise event",
    "laughs uncontrollably",
    "starts crying",
    "cooks something mysterious",
    "fries snacks for everyone",
    "declares an unexpected war"
]

places_or_things = [
    "at the Red Fort",
    "on a Mumbai local train",
    "near the Ganga Ghat",
    "during an IPL match",
    "in a monkey temple"
]

# Generate headline
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    location = random.choice(places_or_things)
    headline = f"BREAKING NEWS: {subject} {action} {location}!"
    headline_label.config(text=headline)

# Setup the GUI window
root = tk.Tk()
root.title("Fake Headline Generator")
root.geometry("500x250")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="📰 Fake Headline Generator 📰", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Headline display
headline_label = tk.Label(root, text="", wraplength=450, justify="center", font=("Arial", 12), fg="darkred")
headline_label.pack(pady=20)

# Generate Button
generate_button = tk.Button(root, text="Generate Headline", command=generate_headline, font=("Arial", 12))
generate_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 10))
exit_button.pack(pady=5)

# Run the app
root.mainloop()
import tkinter as tk
import random

# Data sources
subjects = [ 
    "The Prime Minister visits",
    "Virat Kohli, the cricketer",
    "India, the land of spirituality",
    "An aunty eats an apple",
    "Sumit rides a bicycle",
    "Neesha travels to Jaipur"
]

actions = [
    "launches a surprise event",
    "laughs uncontrollably",
    "starts crying",
    "cooks something mysterious",
    "fries snacks for everyone",
    "declares an unexpected war"
]

places_or_things = [
    "at the Red Fort",
    "on a Mumbai local train",
    "near the Ganga Ghat",
    "during an IPL match",
    "in a monkey temple"
]

# Generate headline
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    location = random.choice(places_or_things)
    headline = f"BREAKING NEWS: {subject} {action} {location}!"
    headline_label.config(text=headline)

# Setup the GUI window
root = tk.Tk()
root.title("Fake Headline Generator")
root.geometry("500x250")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="📰 Fake Headline Generator 📰", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Headline display
headline_label = tk.Label(root, text="", wraplength=450, justify="center", font=("Arial", 12), fg="darkred")
headline_label.pack(pady=20)

# Generate Button
generate_button = tk.Button(root, text="Generate Headline", command=generate_headline, font=("Arial", 12))
generate_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 10))
exit_button.pack(pady=5)

# Run the app
root.mainloop()
