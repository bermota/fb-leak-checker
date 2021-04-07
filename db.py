#!/usr/bin/python3
"""

    Author: Bernardo Mota
    Contact email: bernardo.mota at tecnico.ulisboa.pt

    Description: This program loads the data on to the sqlite3 database from
    the dump found online.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

DATABASE_FILE_PATH = "db2.sql"
DUMP_FILE_PATH = "<REPLACE HERE WITH YOUR FILE>"


import sqlite3

conn = sqlite3.connect(DATABASE_FILE_PATH)
c = conn.cursor()

f = open(DUMP_FILE_PATH)

for line in f.readlines():
    phone = int(line.split(':')[0][3:])
    c.execute("INSERT INTO fb VALUES (?)", (phone))


conn.commit()
conn.close()
