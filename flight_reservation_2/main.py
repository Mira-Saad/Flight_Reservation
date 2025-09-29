import tkinter as tk
import home
import booking
import reservations
import edit_reservation

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("800x600")
        self.frames = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (home.HomePage, booking.BookingPage, reservations.ReservationsPage, edit_reservation.EditReservationPage):
            frame = F(container, self)  # Pass the container and controller (App)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(home.HomePage)

    def show_frame(self, page_class, *args):
        frame = self.frames[page_class]
        if hasattr(frame, "refresh"):
            frame.refresh(*args)
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
