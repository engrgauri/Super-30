employee = {"name": "Amit","department": "Engineering",
            "skills": {"language": "Python","database": "PostgreSQL","cloud": "AWS"},
            "salary": 80000
            }

# Print employee name
print(employee["name"])
# Print department
print(employee["department"])
# Print complete skills dictionary
print(employee["skills"])
# Print programming language
print(employee["skills"]["language"])
# Print database
print(employee["skills"]["database"])
# Print cloud technology
print(employee["skills"]["cloud"])
# Change "Python" to "Python + JavaScript"
employee["skills"]["language"] = "Python + JavaScript"
print(employee)
# Change salary
employee["salary"] = 50000
print(employee)
# Add "experience": 3
employee["experience"] = 3
print(employee)
# Add another skill under the skills dictionary
employee["skills"]["frontend"] = 'HTML'
print(employee)
