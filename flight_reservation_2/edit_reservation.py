import tkinter as tk
from tkinter import messagebox
from database import connect_db
# from .reservations import ReservationsPage
import reservations

class EditReservationPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.res_id = None

        tk.Label(self, text="Edit Reservation", font=("Arial", 20)).pack(pady=20)

        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]

        for field in fields:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            tk.Label(frame, text=field, width=15, anchor="w").pack(side="left")
            entry = tk.Entry(frame, width=30)
            entry.pack(side="left")
            self.entries[field] = entry

        tk.Button(self, text="Update", command=self.update_reservation).pack(pady=20)

    def refresh(self, values):
        self.res_id = values[0]
        keys = list(self.entries.keys())
        for i, key in enumerate(keys):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, values[i+1])

    def update_reservation(self):
        data = [e.get() for e in self.entries.values()]
        if any(v == "" for v in data):
            messagebox.showerror("Error", "All fields are required")
            return

        conn = connect_db()
        c = conn.cursor()
        c.execute("""
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?
        """, (*data, self.res_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reservation updated!")
        self.controller.show_frame(reservations.ReservationsPage)
