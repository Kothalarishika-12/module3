class Employee:
    def work(self):
        print("Employee is working")


class Manager(Employee):
    def manage_team(self):
        print("Manager is managing the team")


class ProjectManager(Manager):
    def plan_project(self):
        print("Project manager is planning the project")


p = ProjectManager()
p.work()
p.manage_team()
p.plan_project()