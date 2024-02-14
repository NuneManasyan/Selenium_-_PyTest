from faker import Faker

fake = Faker()

credentials = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
              }


existing_course  = "selenium"
non_existing_course = "millenium"