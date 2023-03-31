import click
import sqlite3


con = sqlite3.connect("lib/db/design_database.db")
cur = con.cursor()


@click.command()
def get_bookings():
    res = cur.execute(f'''SELECT
      clients.name as client_name, 
      designers.name as designer_name, 
      bookings.consultation_date,
      bookings.room,
      bookings.id
      FROM (bookings 
      INNER JOIN clients ON bookings.designer_id = clients.id
      INNER JOIN designers ON bookings.designer_id = designers.id)''')

    for booking in res.fetchall():
        click.echo(
            f"{booking[4]}: {booking[0]} has an appointment with {booking[1]} to re-design their {booking[3]} on {booking[2]}"
        )


@click.command()
@click.option('--id', help='ID of the booking you wish to delete')
def remove_booking(id):
    fetch_res = cur.execute(
        f'''SELECT id FROM bookings WHERE id = {id}''')
    booking = fetch_res.fetchone()

    cur.execute(f'''DELETE FROM bookings WHERE id = {id}''')
    con.commit()

    click.echo(f'Successfully deleted booking: {booking}')


@click.command()
@click.option('--id', help='ID of the booking you wish to update')
@click.option('--type', help='type of the booking you wish to update')
@click.option('--room', help='room of the booking you wish to update')
@click.option('--designer_id', help='designer_id of the booking you wish to update')
@click.option('--client_id', help='client_id of the booking you wish to update')
@click.option('--consultation_date', help='consultation_date of the booking you wish to update')
def update_booking(id, type, room, designer_id, client_id, consultation_date):
    fetch_res = cur.execute(
        f'''SELECT * FROM bookings WHERE id = {id}''')
    booking = fetch_res.fetchone()

    cur.execute(
        f'''UPDATE bookings SET
            type = "{type if type else booking[1]}", 
            room = "{room if room else booking[2]}", 
            designer_id = {designer_id if designer_id else booking[3]}, 
            client_id = {client_id if client_id else booking[4]},
            consultation_date = "{consultation_date if consultation_date else booking[5]}"
            WHERE id = {id}
        ''')

    con.commit()

    fetch_res = cur.execute(
        f'''SELECT * FROM bookings WHERE id = {id}''')
    booking = fetch_res.fetchone()

    click.echo(f'Updated the booking: {booking}')


@click.command()
@click.option('--type', help='type of the booking you wish to add')
@click.option('--room', help='room of the booking you wish to add')
@click.option('--designer_id', help='designer_id of the booking you wish to add')
@click.option('--client_id', help='client_id of the booking you wish to add')
@click.option('--consultation_date', help='consultation_date of the booking you wish to add')
def add_booking(type, room, designer_id, client_id, consultation_date):
    if not type or not room or not designer_id or not client_id or not consultation_date:
        click.echo("You must provide all fields to create a booking!")
        return

    cur.execute(f'''
        INSERT INTO bookings (
          type,
          room,
          designer_id,
          client_id,
          consultation_date
        )
        VALUES ("{type}", "{room}", "{designer_id}", "{client_id}", "{consultation_date}");
    ''')

    con.commit()

    fetch_res = cur.execute(
        f'''SELECT * FROM bookings''')
    booking = fetch_res.fetchall()

    click.echo(f'Created the booking: {booking[-1]}')
