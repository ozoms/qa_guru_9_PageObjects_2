from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    birthday: str
    subject: str
    hobby: str
    name_file: str
    name_file: str
    address: str
    region: str
    city: str


sasha = User(
    first_name='Sasha',
    last_name='Sol',
    email='name@example.com',
    gender='Male',
    number='1234567891',
    birthday=('May', '1980', '11'),
    subject='Computer Science',
    hobby='Music',
    name_file='foto.jpg',
    address='Mira 1',
    region='NCR',
    city='Delhi'
)
