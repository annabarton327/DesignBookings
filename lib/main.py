import click
import sqlite3
import designer
import client
import booking


@click.group()
def design_bookings():
    pass


# CRUD
design_bookings.add_command(designer.add_designer)
design_bookings.add_command(designer.get_designers)
design_bookings.add_command(designer.update_designer)
design_bookings.add_command(designer.remove_designer)

# design_bookings.add_command(client.add_client)
# design_bookings.add_command(client.get_clients)
# design_bookings.add_command(client.update_client)
# design_bookings.add_command(client.remove_client)

design_bookings.add_command(booking.add_booking)
design_bookings.add_command(booking.get_bookings)
design_bookings.add_command(booking.update_booking)
design_bookings.add_command(booking.remove_booking)

if __name__ == '__main__':
    design_bookings()