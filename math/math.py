import logic

project = logic.Productivity()

project.count = 2
print(project.count)
print(project.productivity)

project.set_count(3)
print(project.get_count())
print(project.productivity)

project.qualification = 8
print(project.qualification)
print(project.productivity)
