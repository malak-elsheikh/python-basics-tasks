# Job Eligibility Portal
python_skill=input("Do you know python (yes/no): ").lower()
experience=int(input("Enter your years of experience or number of projects: "))
degree=input("Do you have a CS degree or Bootcamp? (yes/no) ").lower()
if python_skill=="yes" and (experience>=2 or degree=="yes"):
    print("Congratulations! you are accepted to the next interview stage.")
else:
    print("Sorry, your qualifications don't match the job requirments.")
