from models.user_model import User
from tkinter import messagebox

class UserController:
    def __init__(self):
        self.model = User()

    def register(self, nombre, contrasenia):
        try:
            success, message = self.model.registrar_usuario(nombre, contrasenia)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        except Exception as e:
            print(f"Error in UserController.register: {e}")
            messagebox.showerror("Error", "An error occurred during registration. Please check the console for details.")

    def login(self, nombre, contrasenia):
        if self.model.validar_usuario(nombre, contrasenia):
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password!")
