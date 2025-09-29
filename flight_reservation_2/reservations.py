import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db
# from .home import HomePage
import home
from edit_reservation import EditReservationPage

class ReservationsPage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        tk.Label(self, text="Reservations List", font=("Arial", 20)).pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("ID","Name","Flight","Departure","Destination","Date","Seat"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        tk.Button(self, text="Edit", command=self.edit_reservation).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete_reservation).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(home.HomePage)).pack()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM reservations")
        for row in c.fetchall():
            self.tree.insert("", "end", values=row)
        conn.close()

    def edit_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a reservation to edit")
            return
        values = self.tree.item(selected[0])["values"]
        self.controller.show_frame(EditReservationPage, values)

    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a reservation to delete")
            return
        res_id = self.tree.item(selected[0])["values"][0]
        conn = connect_db()
        c = conn.cursor()
        c.execute("DELETE FROM reservations WHERE id=?", (res_id,))
        conn.commit()
        conn.close()
        self.refresh()
