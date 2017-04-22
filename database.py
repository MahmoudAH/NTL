import sqlite3
def main():
    db=sqlite3.connect("information.db")
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists admin(Name text, age int)")
    db.execute("insert into admin (Name ,age) values(?,?)",("mahmoud",21))
    db.execute("insert into admin (Name ,age) values(?,?)",("naglaa",18))
    db.commit()
     #db.execute("delete from admin where name ='mahmoud'")
    #db.execute("Update admin set age=15 where name='mahmoud'")
    cusror=db.execute("select * from admin")
    for row in cusror:
        print("Name:{},age:{}".format(row["Name"],row["age"]) )

if __name__ == '__main__':main()
