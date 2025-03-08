import hashlib
import re
import secrets
import requests
from datetime import date
from typing import List, Optional, Dict

class PersonalData:
    def __init__(self, name : str, email : str, password: str, birthday: str):
        self.name = name
        self.email = email if self.validate_email(email) else None
        self._password_hash = self.hash_password(password)
        self.birthday = birthday if self.validate_birthday(birthday) else None

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha512(password.encode()).hexdigest()

    def verify_password(self, passik: str) -> bool:
        return self._password_hash == self.hash_password(passik)

    @property
    def password(self) -> str: #getter
        return self._password_hash

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_birthday(birthday: str) -> bool:
        try:
            birth_year = int(birthday[:4])
            today = date.today().year
            return 0 <= today - birth_year <= 120
        except ValueError as e:
            print("Invalid birthday.", e)
            return False

class Employee:
    def __init__(self, technology_stack : List[str], experience_level: str):
        self.technology_stack = technology_stack if self.validate_stack(technology_stack) else None
        self.experience_level = experience_level if self.validate_experience(experience_level) else None

    @staticmethod
    def validate_stack(tech_stack: list[str]) -> bool:
        if len(tech_stack) == 0:
            raise ValueError("Stack cannot be empty")
        return True

    @staticmethod
    def validate_experience(exp_level: str) -> bool:
        if exp_level.lower() not in ['senior', 'middle', 'junior']:
            raise ValueError("Invalid experience level. (Senior or Middle or Junior)")
        return True

class User:
    def __init__(self, personal_data : PersonalData, employee_data : Employee, token: Optional[str] = None):
        self.personal_data = personal_data
        self.employee_data = employee_data
        self.token = token

    def __str__(self):
        return (f"User: {self.personal_data.name} "
                f"Email: {self.personal_data.email} "
                f"Technologies stack: {self.employee_data.technology_stack} "
                f"Experience: {self.employee_data.experience_level} "
                f"Token: {'Loggen in' if self.token else 'Not logged in'} ")

class UsersManager:
    users_by_email: Dict[str, User] = {}

    def create(self, user: User):
        self.users_by_email[user.personal_data.email] = user

    def update(self, email: str, **kwargs):
        user = self.users_by_email.get(email)
        if not user:
            return
        for key, value in kwargs.items():
            if hasattr(user.personal_data, key):
                setattr(user.personal_data, key, value)
            elif hasattr(user.employee_data, key):
                setattr(user.employee_data, key, value)

    def delete(self, email: str):
        if email in self.users_by_email:
            del self.users_by_email[email]

    def retrieve(self, email: str) -> Optional[User]:
        return self.users_by_email.get(email)

    def list(self, limit: Optional[int] = None, offset: Optional[int] = 0, order: Optional[str] = "asc") -> List[str]:
        users = self.users_by_email.values()
        user_list = sorted(users, key=lambda u: u.personal_data.name, reverse=(order == "desc"))
        limit_with_offset = offset + limit if limit else None
        return [str(user) for user in user_list[offset:limit_with_offset]]

class AuthManager:

    sessions = []

    def __init__(self, users_manager: UsersManager):
        self.users_manager = users_manager
        self.user = None

    @staticmethod
    def gen_token():
        return secrets.token_urlsafe(64)

    def login(self, email: str, password: str) -> Optional[str]:
        self.user = self.users_manager.retrieve(email)
        if self.user and self.user.personal_data.verify_password(password):
            self.user.token = self.gen_token()
            self.sessions.append(email)
            return self.user.token

    def is_authorized(self, email: str, token: str) -> bool:
        self.user = self.users_manager.retrieve(email)
        user_email = self.user.personal_data.email
        return user_email in self.sessions and self.user.token == token

    def logout(self, email: str):
        self.user = self.users_manager.retrieve(email)
        if self.is_authorized(email, self.user.token):
            self.sessions.remove(email)
            self.user.token = None

class JobSearchManager:

    API_URL = "https://jobicy.com/api/v2/remote-jobs"

    def __init__(self, auth_manager: AuthManager):
        self.auth_manager = auth_manager

    def list(self, email: str, token: str, technology_stack: list[str], size: Optional[int] = 1) -> dict:
        if self.auth_manager.is_authorized(email, token):
            response = requests.get(self.API_URL, params={'tag': technology_stack, 'count': size} )
            if response.ok:
                return response.json()
        else:
            print("You are not authorized. Please log in first.")

    def print_results(self, user: User, size: Optional[int]) -> None:
        jobs = self.list(user.personal_data.email, user.token, user.employee_data.technology_stack, size)["jobs"]
        if jobs:
            print(f"Jobs for {user.personal_data.name}")
            for idx, job in enumerate(jobs):
                job_type = ', '.join(job['jobType'])
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(f"Job #{idx+1}: {job['jobTitle']}")
                print(f"Type: {job_type}")
                print(f"Location: {job['jobGeo']}")
                print(f"Level: {job['jobLevel']}")
                print(f"Published at: {job['pubDate']}")
                print()

# person1 = PersonalData("Vadim", "abc@a.a", "12345678", "10102020")
# person2 = PersonalData("Daryna", "abc@a.b", "12345678", "10102020")
# skills1 = Employee(["python", "js"], "Senior")
# skills2 = Employee(["python", "d"], "Senior")
# user1 = User(person1, skills1)
# user2 = User(person2, skills2)
# man = UsersManager()
# man.create(user1)
# man.create(user2)
# auth = AuthManager(man)
# token_data = auth.login("abc@a.a", "12345678")
# # auth.logout("abc@a.a")
# a = JobSearchManager(auth)
# a.print_results(user1, 2)

