import re

# Read raw text
with open("../output/raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Remove multiple spaces
text = re.sub(r'\s+', ' ', text)

# Remove unwanted special characters
text = re.sub(r'[^\w\s.,:%()-]', '', text)

# Save cleaned text
with open("../output/clean.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaning Completed Successfully!")
