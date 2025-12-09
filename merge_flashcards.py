#!/usr/bin/env python3
"""
Merge pharmacy flashcards into the main exams.json file
"""

import json

# Load existing medical exams
with open('app/src/data/exams.json', 'r') as f:
    medical_exams = json.load(f)

# Load pharmacy exams
with open('app/src/data/pharmacy-exams.json', 'r') as f:
    pharmacy_exams = json.load(f)

# Combine both sets of exams
combined_exams = {
    "exams": medical_exams["exams"] + pharmacy_exams["exams"]
}

# Write to exams.json
with open('app/src/data/exams.json', 'w') as f:
    json.dump(combined_exams, f, indent=2)

print(f"✓ Successfully merged flashcards!")
print(f"  Medical exams: {len(medical_exams['exams'])}")
print(f"  Pharmacy exams: {len(pharmacy_exams['exams'])}")
print(f"  Total exams: {len(combined_exams['exams'])}")

# Print summary
total_cards = sum(exam['totalSteps'] for exam in combined_exams['exams'])
print(f"\nTotal flashcards: {total_cards}")
print("\nExams included:")
for exam in combined_exams['exams']:
    print(f"  - {exam['name']}: {exam['totalSteps']} cards")
