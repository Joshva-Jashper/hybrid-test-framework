
from faker import Faker



product_scheme={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "name": {
      "type": "string"
    },
    "price": {
      "type": "string"
    },
    "brand": {
      "type": "string"
    },
    "category": {
      "type": "object",
      "properties": {
        "usertype": {
          "type": "object",
          "properties": {
            "usertype": {
              "type": "string"
            }
          },
          "required": [
            "usertype"
          ]
        },
        "category": {
          "type": "string"
        }
      },
      "required": [
        "usertype",
        "category"
      ]
    }
  },
  "required": [
    "id",
    "name",
    "price",
    "brand",
    "category"
  ]
}

brand_scheme = {
  "id": 1,
  "brand": "Polo"
}

faker = Faker()


user_body={
    "name": "Joshva",
    "email": faker.email(),
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
    "mobile_number": "9876543210"
}

user_body_dup_email={
    "name": "Joshva",
    "email": "joshva@gmail.com",
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
    "mobile_number": "9876543210"
}
username = faker.user_name()
email = "joshva@gmail.com"



user_body_update={
    "name": username,
    "email": email,
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

delete_name = faker.user_name()
delete_email = faker.email()
delete_password = faker.password()

user_body_delete={
    "name": delete_name,
    "email": delete_email,
    "password": delete_password,
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
