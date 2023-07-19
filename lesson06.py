# SQLite --> Structured Query Language
# CRUD --> Create Read Update Delete
import sqlite3


conn = sqlite3.connect('dtb.db')

cur = conn.cursor()
cur.execute("""
    create table if not exists `user`(
        `first_name` varchar(50),
        `last_name` varchar(50),
        `phone` varchar(13),
        `birthday` date,
        `is_active` boolean default false,
        `size_of_shoes` int
    )
""")
conn.commit()

# cur.execute("""
#     insert into `user`(`first_name`, `last_name`, `phone`, `birthday`, `is_active`, `size_of_shoes`)
#     values
#     ('Muhammadaziz', 'Ravshanov', '+998931859933', '2005-04-03', false, 42),
#     ('Imomali', 'Qurbonov', '+998938182001', '2001-02-21', false, 43),
#     ('Manguberdi', 'Abdullayev', '+998939832020', '2001-06-20', false, 44)
# """)
#conn.commit()

cur.execute("""
    select * from user
""")
rows = cur.fetchall()
for row in rows:
    print(row)





conn.close()

