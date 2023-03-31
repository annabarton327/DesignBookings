import click
import sqlite3
import designers
import clients
import bookings


@click.group()
def design_bookings():
    pass


# CRUD
design_bookings.add_command(designers.add_designer)
design_bookings.add_command(designers.get_designers)
design_bookings.add_command(designers.update_designer)
design_bookings.add_command(designers.remove_designer)

# design_bookings.add_command(clients.add_client)
# design_bookings.add_command(clients.get_clients)
# design_bookings.add_command(clients.update_client)
# design_bookings.add_command(clients.remove_client)

design_bookings.add_command(bookings.add_booking)
design_bookings.add_command(bookings.get_bookings)
design_bookings.add_command(bookings.update_booking)
design_bookings.add_command(bookings.remove_booking)

if __name__ == '__main__':
    design_bookings()