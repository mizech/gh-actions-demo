import typing

class Person:
    def __init__(self, first_name: str, last_name: str, 
                 email: str, phone: str, projects: list):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.projects = projects

    def __str__(self):
        ret = f"Person: {self.first_name}, {self.last_name}, {self.email}, {self.phone}"
        ret = f"{ret}, Projects: ({", ".join(self.projects)})"
        return ret