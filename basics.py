# basics.py - Day 1, Lesson 1

# 1. VARIABLES: a name that stores a value
college = "IOE"
semester = 8
cgpa = 3.6
is_final_year = True

print("College:", college)
print("Semester:", semester)

# 2. F-STRINGS: put variables inside text
print(f"I study at {college} and I'm in semester {semester}.")

# 3. LISTS: an ordered collection of items
documents = ["syllabus.pdf", "exam_notice.pdf", "regulations.pdf"]
print(documents[0])      # first item (counting starts at 0!)
print(len(documents))    # how many items

# 4. LOOPS: do something for each item
for doc in documents:
    print(f"Reading {doc}...")

# 5. IF STATEMENTS: make decisions
for doc in documents:
    if "notice" in doc:
        print(f"{doc} is a notice")
    else:
        print(f"{doc} is not a notice")

# 6. FUNCTIONS: reusable blocks of code
def greet_student(name, semester):
    return f"Namaste {name}! Welcome to semester {semester}."

message = greet_student("Ram", 8)
print(message)