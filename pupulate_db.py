from projects.models import Project
from blog.models import Category, Post
from voting.models import Candidate, VotingSession

# p1 = Project(
#     title='My First Project',
#     description='A web development project.',
#     technology='Django',
#     image='img/iohannis.png'
# )
# p2 = Project(
#     title='My Second Project',
#     description='Another web development project.',
#     technology='Flask',
#     image='img/dancila.png'
# )
# p1.save()
# p2.save()

can1 = Candidate(
    name='Klaus Werner Iohannis',
    description='Leader of PNL, Mayor of Sibiu',
    image='img/iohannis.png'
)

can2 = Candidate(
    name='Vasilica Viorica Dăncilă',
    description='President of the PSD',
    image='img/dancila.png'
)

can1.save()
can2.save()
sesh1 = VotingSession(
    name="Presidential Elections",
    year=2019,
    country='Romania'
)
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
