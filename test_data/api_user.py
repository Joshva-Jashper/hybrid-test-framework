from faker import Faker
faker = Faker()

body_email = faker.email()
user_body_={
    "name": "Joshva",
    "email": body_email,
    "password": faker.password(),
    "title": "Mr",
    "birth_date": "15",
    "birth_month": "August",
    "birth_year": "2004",
    "firstname": "Joshva",
    "lastname": "Jaspher",
    "company": "TechCorp",
    "address1": "123 Street Name",
    "address2": "Apt 4B",
    "country": "India",
    "zipcode": "600001",
    "state": "Tamil Nadu",
    "city": "Chennai",
    "mobile_number": "9876543210"
}

user_name = faker.user_name()

user_body_update_={
    "name": user_name,
    "email": "traceywillis@example.com",
    "password": "securepassword123",
    "title": "Mr",
    "birth_date": "15",
    "birth_month": "August",
    "birth_year": "2004",
    "firstname": "Joshva",
    "lastname": "Jaspher",
    "company": "TechCorp",
    "address1": "123 Street Name",
    "address2": "Apt 4B",
    "country": "India",
    "zipcode": "600001",
    "state": "Tamil Nadu",
    "city": "Chennai",
    "mobile_number": "931234123"
}

user_broken = f"""{{
    "name": "{user_name}",
    "email": "traceywillis@example.com",
    "password": "securepassword123",
    "title": "Mr",
    "birth_date": "15",
    "birth_month": "August",
    "birth_year": "2004",
    "firstname": "Joshva",
    "lastname": "Jaspher",
    "company": "TechCorp",
    "address1": "123 Street Name",
    "address2": "Apt 4B",
    "country": "India",
    "zipcode": "600001",
    "state": "Tamil Nadu",
    "city": "Chennai",
    "mobile_number": "931234123"
""" 

user_missing_feild={
    "name": user_name,
    "email": "traceywillis@example.com",
    "password": "securepassword123",
    "title": "Mr",
    "birth_date": "15",
    "birth_month": "August",
    "birth_year": "2004",
    "firstname": "Joshva",
    "lastname": "Jaspher",
    "company": "TechCorp",
    "address1": "123 Street Name",
    "address2": "Apt 4B",
    "zipcode": "600001",
    "state": "Tamil Nadu",
    "city": "Chennai"
}
