from models.person import Person

def exec():
    tmeyer = Person(first_name="Thorsten", last_name="Meyer", 
                email="thorsten.meyer@gmx.com", phone="012345",
                projects=["Alpha", "Beta", "Gamma"])
    print(tmeyer)

if __name__ == "__main__":
    exec()