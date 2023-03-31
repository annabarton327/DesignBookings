# Designers Readme

ENTER THE PIPENV SHELL: `pipenv shell`
RECREATE DATABASE: `sqlite3 lib/db/design_database.db < lib/db/design_schema.sql`
SEED THE DATABASE: `python lib/db/seed.py`

# Running the CLI
Running the CLI: `python lib/main.py`

# Adding a Designer 
Step 1: `python lib/main.py`
Step 2: --field="input"
-- *Make sure to do all of the fields!* -- 

# Updating a Designer 
Step 1: `python lib/main.py`
Step 2: *Make sure to add the ID of the designer you are updating*
Step 3: *You only need to input the field you wish to update, instead of all*
