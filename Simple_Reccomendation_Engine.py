"""Recommends pathway for competition math."""
prealg = "Prealgebra (Rusczyk, Patrick, Boppana)"
intro_alg = "Introduction to Algebra (Rusczyk)"
comp_math_middle = "Competition Math for Middle School (Batterson)"
vol_1 = "AOPS Volume 1 (Rusczyk and Lehoczky)"
vol_2 = "AOPS Volume 2 (Rusczyk and Lehoczky)"
precalc = "Precalculus (Rusczyk)"
intermed_count_prob = "Intermediate Counting and Probability (Patrick)"
calc = "Calculus (Patrick)"
ACOPS = "Art and Craft of Problem Solving (Zeitz)"
IMO_geo = "Lemmas in Olympiad Geometry (Adreescu, Korsky, and Pohoata)"
IMO_num_theory = "Modern Olympiad Number Theory (Khurmi)"
IMO_combinatorics = "102 Combinatorial Problems... IMO Team (Adreescu, Feng)"
# Course options to choose from for our recommendation.


# Collect user attributes to inform our recommendation.
# Attributes include grade level, competition goals, and study availability.
grade = input("What grade are you in? ")
math_comp_goal = input("Do you want to practice for AMCs, AIME, IMO, or Putnam? ")
study_days = input("How many days a week are you planning to study? ")

# Minimum amount of study time to be consistent is an hour a day.
min_study_time = 1

# Make a course recommendation based on the user's attributes.
rec = ""
if grade in range(6, 9) or math_comp_goal == "AMCs":
    # Textbooks cater to younger learners.
    rec = [prealg, intro_alg, comp_math_middle, vol_1]
elif grade in range(9, 13) or math_comp_goal == "AIME":
    # Textbooks cater to slightly more advanced learners
    rec = [vol_2, precalc, intermed_count_prob]
elif grade == "college" or math_comp_goal == "IMO" or math_comp_goal == "Putnam":
    # Textbooks cater to highly advanced learners.
    rec = [calc, ACOPS, IMO_geo, IMO_num_theory, IMO_combinatorics]

print(f"We recommend the following math textbooks: {rec}.")
print(f"Study for a min of {min_study_time} daily for {study_days} weekly.")
