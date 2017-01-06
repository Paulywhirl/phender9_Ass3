from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('homepage.html')


@app.route('/Employee')
def Employee_Page():
    return render_template('Employee.html')


#################################################################################
@app.route('/customer_index')
def viewCustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from Customer")
    cursor.execute(query)
    users = cursor.fetchall()
    cnx.close()
    return render_template('customerIndex.html', users=users)


@app.route('/addCustomer')
def toAddCustomer():
    return render_template('/addCustomer.html')


@app.route('/submitC', methods=["POST"])
def addCustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    CID = (request.form.get('CID'))
    Fname = (request.form['fName'])
    Lname = (request.form['lName'])
    Email = (request.form['email'])
    Sex = (request.form['sex'])
    insert_stmt = (
        "INSERT INTO Customer (idCustomer, FirstName, LastName, EmailAddress, Sex)"
        " VALUES ("+CID+",'"+Fname+"','"+Lname+"','"+Email+"','"+Sex+"')"
    )
    cursor.execute(insert_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/deleteCustomer')
def toDeleteCustomer():
    return render_template('/deleteCustomer.html')


@app.route('/deleteC', methods=["POST"])
def deleteCustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    CID = (request.form.get('CID'))
    delete_stmt = (
        "delete from Customer where idCustomer =" +CID
    )

    cursor.execute(delete_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/modifyCustomer')
def toModifyCustomer():
    return render_template('/modifyCustomer.html')


@app.route('/modifyC', methods=["POST"])
def ModifyCustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    CID = (request.form.get('CID'))
    First = (request.form['first'])
    Last = (request.form['last'])
    Email = (request.form['email'])
    if First is not None:
        modify_stmt = (
            "update Customer set FirstName= '" + First + "' where idCustomer = " + CID
        )
        cursor.execute(modify_stmt)
        cnx.commit()
    if Last is not None:
        modify_stmt = (
            "update Customer set LastName= '" + Last + "' where idCustomer = " + CID
        )
        cursor.execute(modify_stmt)
        cnx.commit()
    if Email is not None:
        modify_stmt = (
            "update Customer set EmailAddress= '" + Email + "' where idCustomer = " + CID
        )
        cursor.execute(modify_stmt)
        cnx.commit()

    cnx.close()
    return render_template('/executed.html')


#################################################################################
@app.route('/movieIndex')
def viewMovies():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("Select * from Movie")
    cursor.execute(query)
    movies = cursor.fetchall()
    cnx.close()
    return render_template('movieIndex.html', movies=movies)


@app.route('/addMovie')
def toAddMovie():
    return render_template('/addMovie.html')


@app.route('/submit', methods=["POST"])
def addMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    ID = (request.form.get('ID'))
    mName = (request.form['mName'])
    mYear = (request.form['mYear'])
    insert_stmt = (
        "INSERT INTO Movie VALUES('"+ID+"',"+mName+","+mYear+")"
    )
    cursor.execute(insert_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/deleteMovie')
def toDeleteMovie():
    return render_template('/deleteMovie.html')


@app.route('/delete', methods=["POST"])
def deleteMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    ID = (request.form.get('ID'))
    delete_stmt = (

        "delete from Movie where idMovie= "+ID
    )
    cursor.execute(delete_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')

@app.route('/modifyMovie')
def toModifyMovie():
    return render_template('/modifyMovie.html')


@app.route('/modifyM', methods=["POST"])
def ModifyMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    MID = (request.form.get('MID'))
    Name = (request.form['mName'])
    year = (request.form['year'])
    if Name is not None:
        modify_stmt = (
            "update Movie set MovieName= '" + Name + "' where idMovie = " + MID
        )
        cursor.execute(modify_stmt)
        cnx.commit()
    if year is not None:
        modify_stmt = (
            "update Movie set MovieYear= '" + year + "' where idMovie = " + MID
        )
        cursor.execute(modify_stmt)
        cnx.commit()

    cnx.close()
    return render_template('/executed.html')


#################################################################################

@app.route('/genreIndex')
def viewGenres():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("Select * from Genre ORDER by Genre")
    cursor.execute(query)
    genres = cursor.fetchall()
    cnx.close()
    return render_template('genreIndex.html', genres=genres)


@app.route('/addGenre')
def toAddGenre():
    return render_template('/addGenre.html')


@app.route('/submitG', methods=["POST"])
def addGenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    Mid = (request.form.get('MID'))
    Genre = (request.form['genre'])
    insert_stmt = (
        "INSERT INTO Genre VALUES('"+Genre+"',"+Mid+")"
    )
    cursor.execute(insert_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/deleteGenre')
def toDeleteGenre():
    return render_template('/deleteGenre.html')


@app.route('/deleteG', methods=["POST"])
def deleteGenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    Mid = (request.form.get('Mid'))
    Genre = (request.form['genre'])
    delete_stmt = (

        "delete from Genre where Genre='"+Genre+"' and Movie_idMovie="+Mid
    )
    cursor.execute(delete_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


#################################################################################

@app.route('/roomIndex')
def viewRoom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * from TheatreRoom")
    cursor.execute(query)
    rooms = cursor.fetchall()
    cnx.close()
    return render_template('/roomIndex.html', rooms=rooms)


@app.route('/addRoom')
def toAddRoom():
    return render_template('/addRoom.html')


@app.route('/submitR', methods=["POST"])
def addRoom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    RID = (request.form.get('RID'))
    Capacity = (request.form.get('Cap'))
    insert_stmt = (
        "INSERT INTO TheatreRoom (RoomNumber, Capacity)"
        " VALUES ("+RID+","+Capacity+")"
    )
    cursor.execute(insert_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/deleteRoom')
def toDeleteRoom():
    return render_template('/deleteRoom.html')


@app.route('/deleteR', methods=["POST"])
def deleteRoom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    RID = (request.form.get('RID'))
    delete_stmt = (
        "delete from TheatreRoom where RoomNumber = "+RID
    )

    cursor.execute(delete_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/modifyRoom')
def toModifyRoom():
    return render_template('/modifyRoom.html')


@app.route('/modifyR', methods=["POST"])
def modifyRoom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    RID = (request.form.get('RID'))
    Cap = (request.form['Cap'])
    if Cap is not None:
        modify_stmt = (
            "update TheatreRoom set Capacity= '" + Cap + "' where RoomNumber = " + RID
        )
        cursor.execute(modify_stmt)
        cnx.commit()

    cnx.close()
    return render_template('/executed.html')


#################################################################################


@app.route('/showingIndex')
def viewShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select s.idShowing, s.ShowingDateTime, m.MovieName, s.TheatreRoom_RoomNumber, s.TicketPrice"
             " from Showing s left outer join Movie m on s.Movie_idMovie = m.idMovie order by s.ShowingDateTime")
    cursor.execute(query)
    showings = cursor.fetchall()
    cnx.close()
    return render_template('/showingIndex.html', showings=showings)


@app.route('/addShowing')
def toAddShowing():
    return render_template('/addShowing.html')


@app.route('/submitS', methods=["POST"])
def addShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SID = (request.form.get('SID'))
    SDT = (request.form['SDT'])
    MID = (request.form['MID'])
    room = (request.form['RID'])
    TP = (request.form['Price'])
    insert_stmt = (
        "INSERT INTO Showing"
        " VALUES ("+SID+",'"+SDT+"','"+MID+"','"+room+"','"+TP+"')"
    )
    cursor.execute(insert_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/deleteShowing')
def toDeleteShowing():
    return render_template('/deleteShowing.html')


@app.route('/deleteS', methods=["POST"])
def deleteShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SID = (request.form.get('SID'))
    delete_stmt = (
        "delete from Showing where idShowing = "+SID
    )

    cursor.execute(delete_stmt)
    cnx.commit()
    cnx.close()
    return render_template('/executed.html')


@app.route('/modifyShowing')
def toModifyShowing():
    return render_template('/modifyShowing.html')


@app.route('/modifyS', methods=["POST"])
def modifyShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SID = (request.form.get('SID'))
    SDT = (request.form['SDT'])
    MID = (request.form.get('MID'))
    room = (request.form.get('RID'))
    TP = (request.form.get('Price'))
    if SDT is not None:
        modify_stmt = (
            "update Showing set ShowingDateTime= '" + SDT + "' where idShowing = " + SID
        )
        cursor.execute(modify_stmt)
        cnx.commit()
    if MID is not None:
        modify_stmt = (
            "update Showing set Movie_idMovie = '" + MID + "' where idShowing = " + SID
        )
        cursor.execute(modify_stmt)
        cnx.commit()
    if room is not None:
        modify_stmt = (
            "update Showing set TheatreRoom_RoomNumber= '" + TP + "' where idShowing = " + SID
        )
        cursor.execute(modify_stmt)
        cnx.commit()
    if TP is not None:
        modify_stmt = (
            "update Showing set TicketPrice= '" + TP + "' where idShowing = " + SID
        )
        cursor.execute(modify_stmt)
        cnx.commit()

    cnx.close()
    return render_template('/executed.html')


#################################################################################
@app.route('/attendances')
def attendIndex():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select c.FirstName, c.LastName, s.ShowingDateTime, m.MovieName, a.Rating from Attend a left outer join"
             " Customer c on a.Customer_idCustomer=c.idCustomer left outer join Showing s on"
             " a.Showing_idShowing=s.idShowing left outer join Movie m on s.Movie_idMovie=m.idMovie order by a.Rating")
    cursor.execute(query)
    attendances = cursor.fetchall()
    cnx.close()
    return render_template('/attendances.html', attendances=attendances)

#################################################################################
@app.route('/Customer')
def Customer_Page():
    return render_template('Customer.html')

@app.route('/customerPage', methods=["POST"])
def login():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    cid = (request.form.get('CID'))
    query = (
        "select FirstName, LastName from Customer where idCustomer = "+cid
        )
    cursor.execute(query)
    names = cursor.fetchall()
    if not names:
        cnx.close()
        return render_template('/errorCustomer.html')
    cnx.close()
    return render_template('/customerMenu.html', names=names)

@app.route('/COTS')
def COTS():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    g_query = (
        "select distinct Genre from Genre"
    )
    num_query = (
        "create view NumOfP as select Showing_idShowing, count(*) as Scount from Attend group by Showing_idShowing"
    )
    o_query = (
        "create view NumOfS as select s.idShowing, r.Capacity from Showing s left outer join TheatreRoom r on s.TheatreRoom_roomNumber=r.RoomNumber"
    )
    last_query = (
        "create view NumLeft as select s.idShowing, (s.Capacity-p.Scount) as seatsAvailable from"
        " NumOfS s left OUTER JOIN NumOfP p on s.idShowing=p.Showing_idShowing"
    )
    cursor.execute(g_query)
    genres = cursor.fetchall()
    cursor.execute(num_query)
    cursor.execute(o_query)
    cursor.execute(last_query)
    query = (
        "select * from NumLeft"
    )
    cursor.execute(query)
    showingIDS = cursor.fetchall()

    dropEverything = (
        "Drop view NumLeft, NumOfS, NumOfP;"
    )
    cursor.execute(dropEverything)
    moviesYo = (
        "select * from Movie"
    )
    cursor.execute(moviesYo)
    movies = cursor.fetchall()

    cnx.close()
    return render_template('/checkShowings.html', genres=genres, showings=showingIDS, movies=movies)

@app.route('/attendy')
def yattend():
    return render_template('/insertAttend.html')


@app.route('/attend', methods=["POST"])
def attend():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SID = (request.form.get('SID'))
    CID = (request.form.get('CID'))
    query = (
        "Insert into Attend ("+SID+","+CID+")"
    )
    cursor.execute(query)
    cnx.close()
    return render_template('/bought.html')

@app.route('/rate')
def rate():
    return render_template('/rate.html')

@app.route('/rateS', methods=["POST"])
def rateS():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    SID = (request.form.get('SID'))
    CID = (request.form.get('CID'))
    rate = (request.form.get('rate'))
    query = (
        "Insert into Atten ("+CID+","+SID+","+rate+")"
    )
    cursor.execute(query)
    cnx.cloe()
    return render_template('/customerMenu.html')

@app.route('/showFirst')
def showStuff():
    return render_template('/showFirst.html')

@app.route('/showShowings', methods=["POST"])
def showShowings():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    CID = (request.form.get('CID'))
    query = (
        "select c.FirstName, m.MovieName, a.Rating from Showing s left outer join Attend a on s.idShowing=a.Showing_idShowing"
        " left outer join Movie m on s.Movie_idMovie=m.idMovie left outer join Customer c on a.Customer_idCustomer=c.idCustomer"
        " where c.idCustomer = 1;"
    )
    cursor.execute(query)
    stuffs = cursor.fetchall()
    cnx.close()
    return render_template('/showShowings.html', stuffs=stuffs)

@app.route('/custProfile')
def custProfile():
    return render_template('/custProfile.html')

@app.route('/Profile', methods=["POST"])
def Profile():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    CID = (request.form.get('CID'))
    query = (
        "select * from Customer where idCustomer="+CID
    )
    cursor.execute(query)
    yous = cursor.fetchall()
    cnx.close()
    return render_template('/Profile.html', yous=yous)

#################################################################################

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
