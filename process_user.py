from fastapi import FastAPI, HTTPException

class Staff:
    def auth_staff(self, username: str):
        pass

class Administrator(Staff):
    def auth_staff(self):
        return f"usuário administrador"

class Employee(Staff):
    def auth_staff(self):
        return f"usuário funcionário"

class StaffFactory:
    @staticmethod
    def create_staff(staff_type: str) -> Staff:
        if staff_type == "admin":
            return Administrator()
        elif staff_type == "emp":
            return Employee()
        else:
            raise HTTPException(status_code=400, detail="Invalid user... Try again")

app = FastAPI()

@app.post("/users/{staff_type}")
def process_user(staff_type: str, username: str):
    user = Staff.auth_staff(staff_type)
    return user.auth_staff(username)
