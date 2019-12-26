from projects.models import Project
from blog.models import Category, Post

p1 = Project(
    title='My First Project',
    description='A web development project.',
    technology='Django',
    image='img/project1.png'
)
p2 = Project(
    title='My Second Project',
    description='Another web development project.',
    technology='Flask',
    image='img/project2.png'
)
p3 = Project(
    title='My Third Project',
    description='A final development project.',
    technology='Django',
    image='img/project3.png'
)

p1.save()
p2.save()
p3.save()

c1 = Category(
    name='Software Development'
)

c1.save()

post1 = Post(
    title='Lorem Ipsum',
    body='Dummy text',
    categories=c1
)

post1.save()
