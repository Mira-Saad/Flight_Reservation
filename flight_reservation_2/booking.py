import tkinter as tk
from tkinter import messagebox
from database import connect_db
#from home import HomePage
import home

class BookingPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        tk.Label(self, text="Book a New Flight", font=("Arial", 20)).pack(pady=20)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]

        for field in fields:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            tk.Label(frame, text=field, width=15, anchor="w").pack(side="left")
            entry = tk.Entry(frame, width=30)
            entry.pack(side="left")
            self.entries[field] = entry

        tk.Button(self, text="Submit", command=self.save_reservation).pack(pady=20)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(home.HomePage)).pack()


    def save_reservation(self):
        data = [e.get() for e in self.entries.values()]
        if any(v == "" for v in data):
            messagebox.showerror("Error", "All fields are required")
            return

        conn = connect_db()
        c = conn.cursor()
        c.execute("""
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation booked!")
        self.controller.show_frame(home.HomePage)
