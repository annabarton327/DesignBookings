import click
import sqlite3


con = sqlite3.connect("lib/db/design_database.db")
cur = con.cursor()


@click.command()
def get_designers():
    res = cur.execute(f'''SELECT * FROM designers''')
    for designer in res.fetchall():
        click.echo(designer)


@click.command()
@click.option('--id', help='ID of the designer you wish to delete')
def remove_designer(id):
    fetch_res = cur.execute(
        f'''SELECT * FROM designers WHERE id = {id}''')
    designer = fetch_res.fetchone()

    cur.execute(f'''DELETE FROM designers WHERE id = {id}''')
    con.commit()

    click.echo(f'Successfully deleted designer: {designer}')


@click.command()
@click.option('--id', help='ID of the designer you wish to update')
@click.option('--name', help='name of the designer you wish to update')
@click.option('--address', help='address of the designer you wish to update')
@click.option('--phone_number', help='phone_number of the designer you wish to update')
@click.option('--company', help='company of the designer you wish to update')
def update_designer(id, name, address, phone_number, company):
    fetch_res = cur.execute(
        f'''SELECT * FROM designers WHERE id = {id}''')
    designer = fetch_res.fetchone()

    cur.execute(
        f'''UPDATE designers
            SET name = "{name if name else designer[1]}", 
            address = "{address if address else designer[2]}", 
            phone_number = "{phone_number if phone_number else designer[3]}", 
            company = "{company if company else designer[4]}"
            WHERE id = {id}
        ''')

    con.commit()

    fetch_res = cur.execute(
        f'''SELECT * FROM designers WHERE id = {id}''')
    designer = fetch_res.fetchone()

    click.echo(f'Updated the designer: {designer}')


@click.command()
@click.option('--name', help='name of the designer you wish to create')
@click.option('--address', help='address of the designer you wish to create')
@click.option('--phone_number', help='phone_number of the designer you wish to create')
@click.option('--company', help='company of the designer you wish to create')
def add_designer(name, address, phone_number, company):
    if not name or not address or not phone_number or not company:
        click.echo("You must provide all fields to create a designer!")
        return

    cur.execute(f'''
        INSERT INTO designers (name, address, phone_number, company)
        VALUES ("{name}", "{address}", "{phone_number}", "{company}");
    ''')

    con.commit()

    fetch_res = cur.execute(
        f'''SELECT * FROM designers''')
    designer = fetch_res.fetchall()

    click.echo(f'Created the designer: {designer[-1]}')