import tkinter as tk
# from booking import BookingPage
import booking
from reservations import ReservationsPage

class HomePage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        tk.Label(self, text="Welcome to Flight Reservation", font=("Arial", 24)).pack(pady=50)

        tk.Button(self, text="Book Flight", width=20, 
                  command=lambda: self.controller.show_frame(booking.BookingPage)).pack(pady=10)

        tk.Button(self, text="View Reservations", width=20,
                  command=lambda: self.controller.show_frame(ReservationsPage)).pack(pady=10)
