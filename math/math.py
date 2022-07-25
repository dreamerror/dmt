import logic

project = logic.Productivity()
project.set_count(2)
print(project.get_productivity())
project.set_qualification(8)
print(project.get_productivity())
