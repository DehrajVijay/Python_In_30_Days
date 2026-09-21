"""
Student Grade Book — Day 4 project.
Data shape: dict of student -> dict of subject -> marks.
Produces a ranked report card, per-subject toppers, and answers
enrolment questions with set algebra.
Day 5 adds the menu loop, Day 6 turns these blocks into functions,
Day 7 loads the marks from a CSV file instead of hardcoding them.
"""

from collections import Counter

GRADES = {
    "Priya Sharma": {"Maths": 91, "Physics": 78, "English": 84},
    "Telish Shrama": {"Maths": 67, "Chemistry": 72, "English": 75},
    "Sonia Soni": {"Maths": 88, "Physics": 95, "Chemistry": 81},
    "Sonika Sharma": {"Physics": 59, "English": 66},
}

WIDTH = 54
BAR = "-" * WIDTH
BANDS = "FDCBA"
CUTS = (50, 65, 75, 85)

# - 1. PER- STUDENT SUMMARY---
summary = {}
for student, subjects in GRADES.items():
    total = sum(subjects.values())
    count = len(subjects)
    avg = total / count

    # How many cut-offs did this average clear? 0 → F, 4 → A.
    grade = BANDS[sum([avg >= cut for cut in CUTS])]
    summary[student] = (count, total, avg, grade)

ranked = sorted(summary.items(), key=lambda kv: kv[1][2], reverse=True)

print("=" * WIDTH)
print("SPRINGFIELD PUBLIC SCHOOL · GRADE BOOK".center(WIDTH))
print("=" * WIDTH)
print(f"{'STUDENT':<20}{'SUBJECTS':>8}{'TOTAL':>8}{'AVERAGE':>10}{'GRADE':>8}")
print(BAR)

for student, (count, total, avg, grade) in ranked:
    print(f"{student:<20}{count:>8}{total:>8}{avg:>10.2f}{grade:>8}")

print(BAR)
class_total = sum(sum(s.values()) for s in GRADES.values())
class_count = sum(len(s) for s in GRADES.values())
print(
    f"{'CLASS':<20}{class_count:>8}{class_total:>8}{class_total / class_count:>10.2f}"
)
# ── 2 · per-subject toppers ─────────────────────────────────────
# Re-shape the data: subject -> {student: mark}
by_subject = {}
for student, subjects in GRADES.items():
    for subject, mark in subjects.items():
        by_subject.setdefault(subject, {})[student] = mark

print("\n" + "=" * WIDTH)
print("SUBJECT TOPPERS".center(WIDTH))
print("=" * WIDTH)


for subject in sorted(by_subject):
    marks = by_subject[subject]
    topper = max(marks, key=marks.get)
    print(f"{subject:<12}{topper:<20}{marks[topper]:>4}")

# ── 3 · enrolment sets ──────────────────────────────────────────
maths = {s for s, subs in GRADES.items() if "Maths" in subs}
physics = {s for s, subs in GRADES.items() if "Physics" in subs}
chemistry = {s for s, subs in GRADES.items() if "Chemistry" in subs}

print("\n" + "=" * WIDTH)
print("ENROLMENT — SET ALGEBRA".center(WIDTH))
print("=" * WIDTH)
print(f"Maths AND Physics    : {', '.join(sorted(maths & physics))}")
print(f"Maths NOT Physics    : {', '.join(sorted(maths - physics))}")
print(f"Physics OR Chemistry : {', '.join(sorted(physics | chemistry))}")
print(f"Exactly one of M / P : {', '.join(sorted(maths ^ physics))}")
print(f"Everyone takes Maths : {maths >= set(GRADES)}")
print(f"M and P share nobody : {maths.isdisjoint(physics)}")

# ── 4 · what each student is missing ────────────────────────────
all_subjects = set(by_subject)

print("\n" + "=" * WIDTH)
print("GAPS PER STUDENT".center(WIDTH))
print("=" * WIDTH)

for student, subjects in GRADES.items():
    missing = sorted(all_subjects - set(subjects))
    print(f"{student:<16}missing: {', '.join(missing) if missing else 'nothing'}")

# ── 5 · subject popularity with Counter ─────────────────────────
enrolment = Counter()
for subjects in GRADES.values():
    enrolment.update(subjects.keys())

print("\n" + "=" * WIDTH)
print("SUBJECT POPULARITY".center(WIDTH))
print("=" * WIDTH)

for subject, n in enrolment.most_common():
    print(f"{subject:<12}{n:>3}  {'*' * n}")

# ── 6 · deduplication, both ways ────────────────────────────────
mentions = []
for subjects in GRADES.values():
    mentions.extend(subjects.keys())

print("\nRaw subject mentions : " + str(len(mentions)))
print("Distinct subjects    : " + str(len(set(mentions))))
print("Order preserved      : " + str(list(dict.fromkeys(mentions))))
