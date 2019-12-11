from projects.models import Project

Project.objects.bulk_create([
    Project(title='My First Project', description='A web development project.', technology='Django',
            image='img/project1.png'),
    Project(title='My Second Project', description='Another web development project.', technology='Flask',
            image='img/project2.png'),
    Project(title='My Third Project', description='A final development project.', technology='Django',
            image='img/project3.png')
])
