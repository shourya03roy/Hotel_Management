import mysql.connector as sql
from mysql.connector import Error
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
try:
    connection =sql.connect(host='localhost',database='hotel',user='root',passwd='root')
    cursor = connection.cursor()
    def add_roomtype():
        print("Enter Details of Newly Created Room Type ")
        roomno=int(input("Enter Newly Created Room No ")) 
        id2=int(input("Enter ROOM TYPE ID "))
        id1=int(input("Enter ROOM ID "))
        type1=input("Enter Type of Room ")
        cap=int(input("Enter Capacity "))
        rent=int(input("Enter Rent for Type of room "))
        status=int(input("Enter Status 1 for working and 0 for not Working "))
        sql_insert_query = (""" INSERT INTO roomtype(room_id,type,capacity,rentpd,room_type_id,roomno,func_status) VALUES(%d,%s,%d,%d,%d,%d,%d)"""%(id1,"'"+type1+"'",cap,rent,id2,roomno,status))
        cursor.execute(sql_insert_query)
        connection.commit()
        print ("Record inserted successfully into python_users table")
    def modify_roomtype_type():
        id1=int(input("Enter ROOM TYPE ID for Modify "))
        print("Re Enter Details of Newly Created Room Type ")
        type1=input("Enter Type of Room ")
        sql_update = (""" UPDATE ROOMTYPE SET TYPE=%s where room_id=%d"""%("'"+type1+"'",id1))
        cursor.execute(sql_update)
        connection.commit()
        print ("Record inserted successfully into python_users table")
    def modify_roomtype_capacity():
        id1=int(input("Enter ROOM TYPE ID for Modify ")) 
        print("Re Enter Details of Newly Created Room Type ")
        cap=int(input("Enter Capacity of Room "))
        sql_update = (""" UPDATE ROOMTYPE SET CAPACITY=%d where room_id=%d"""%(cap,id1))
        cursor.execute(sql_update)
        connection.commit()
        print ("Record inserted successfully into python_users table")
    def modify_roomtype_rent():
        id1=int(input("Enter ROOM TYPE ID for Modify "))
        print("Re Enter Details of Newly Created Room Type ")
        cap=int(input("Enter Rent of Room per day "))
        sql_update = (""" UPDATE ROOMTYPE SET RENTPD=%d where room_id=%d"""%(cap,id1)) 
        cursor.execute(sql_update)
        connection.commit()
        print ("Record inserted successfully into python_users table")
        print("MySQL connection is closed")
    def modify_roomtype_roomno():
        id1=int(input("Enter ROOM ID for Modify "))
        print("Re Enter Details of ROOM ")
        roomno=int(input("Enter Room No of Room "))
        sql_update = (""" UPDATE ROOMTYPE SET ROOMNO=%d where room_id=%d"""%(roomno,id1))
        cursor = connection.cursor()
        cursor.execute(sql_update)
        connection.commit()
        print ("Record inserted successfully into python_users table")
    def modify_roomtype_status():
         id1=int(input("Enter ROOM ID for Modify "))
         print("Re Enter Details of ROOM ")
         status=int(input("Enter Status of Room 1 for WORKING AND 0 FOR NOT WORKING "))
         sql_update = (""" UPDATE ROOMTYPE SET func_status=%d where room_id=%d"""%(status,id1))
         cursor = connection.cursor()
         cursor.execute(sql_update)
         connection.commit() 
         print ("Record inserted successfully into python_users table")
    def add_guest():
         print("Enter Details of Newly Created Room Type ")
         id1=int(input("Enter GUEST ID "))
         firstname=input("Enter First Name of Guest ")
         lastname=input("Enter Last Name of Guest ")
         mdate=input("Enter Date of membership of Guest ")
         address=input("Enter Address of Guest ")
         city=input("Enter City of Guest ")
         pincode=input("Enter Pincode of city of Guest ")
         mobileno=input("Enter Mobile No of city of Guest ")
         sql_insert_query = (""" INSERT INTO GUEST(id,FIRSTNAME,LASTNAME,MDATE,ADDRESS,CITY,PIN,MOBILENO) VALUES (%d,%s,%s,%s,%s,%s,%s,%s)"""%(id1,"'"+firstname+"'","'"+lastname+"'","'"+mdate+"'","'"+address+"'","'"+city+"'","'"+pincode+"'","'"+mobileno+"'")) 
         print(sql_insert_query)
         cursor.execute(sql_insert_query)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def modify_guest_firstname():
         id1=int(input("Enter GUEST ID for Modify "))
         print("Re Enter Details of Guest ")
         firstname=input("Enter First Name of Guest ")
         sql_update = (""" UPDATE GUEST SET FIRSTNAME=%s where id=%d"""%("'"+firstname+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table") 
    def modify_guest_lastname():
         id1=int(input("Enter GUEST ID for Modify "))
         print("Re Enter Details of Guest ")
         lastname=input("Enter Last Name of Guest ")
         sql_update = (""" UPDATE GUEST SET LASTNAME=%s where id=%d"""%("'"+lastname+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def modify_guest_mdate():
         id1=int(input("Enter GUEST ID for Modify "))
         print("Re Enter Details of Guest ")
         mdate=input("Enter Date of Membership of Guest ")
         sql_update = (""" UPDATE GUEST SET MDATE=%s where id=%d"""%("'"+mdate+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def modify_guest_address():
         id1=int(input("Enter GUEST ID for Modify "))
         print("Re Enter Details of Guest ")
         address=input("Enter Address of Guest ")
         sql_update = (""" UPDATE GUEST SET ADDRESS=%s where id=%d"""%("'"+address+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def modify_guest_city():
         id1=int(input("Enter GUEST ID for Modify "))
         print("Re Enter Details of Guest ")
         city=input("Enter City of Guest ")
         sql_update = (""" UPDATE GUEST SET CITY=%s where id=%d"""%("'"+city+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table") 
    def modify_guest_pincode():
         id1=int(input("Enter GUEST ID for Modify "))
         print("Re Enter Details of Guest ")
         pin=input("Enter Pincode of Guest ")
         sql_update = (""" UPDATE GUEST SET PIN=%s where id=%d"""%("'"+pin+"'",id1))
         cursor = connection.cursor()
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def modify_guest_mobileno():
         id1=int(input("Enter GUEST ID for Modify "))
         print("Re Enter Details of Guest ")
         mobileno=input("Enter Mobile No of Guest ")
         sql_update = (""" UPDATE GUEST SET MOBILENO=%s where id=%d"""%("'"+mobileno+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def new_booking():
         print("Enter Details of New Booking ")
         id1=int(input("Enter New Booking ID "))
         cindate2=input("Enter Check In Date ")
         cindate=parse(cindate2)
         noofdaysstay=int(input("Enter No of Days Stay "))
         roomtypeid=int(input("Enter Room Type id for booking "))
         noofrooms=int(input("Enter No of Rooms "))
         guestid=int(input("Enter Guest id "))
         madeby=input("Enter Made By ")
         cindate1=datetime.date(cindate)
         reservationdate=datetime.date(datetime.now())
         reservationdate1=reservationdate.strftime('%Y-%m-%d')
         coutdate=cindate1+relativedelta(days=noofdaysstay)
         coutdate2=coutdate.strftime('%Y-%m-%d')
         print(cindate2) 
         print(coutdate2)
         sql_insert_query1 = (""" INSERT INTO reservation
         (id,noofrooms,cindate,coutdate,madeby,guestid,reservationdate,no_of_days_stay,roomtypeid)
         VALUES
         (%d,%d,%s,%s,%s,%d,%s,%d,%d)"""%(id1,noofrooms,"'"+cindate2+"'","'"+coutdate2+"'","'"+madeby+"'",guestid,"'"+reservationdate1+"'",noofdaysstay,roomtypeid))
         cursor.execute(sql_insert_query1)
         print ("Record inserted successfully into python_users table")
         for i in range(0,noofrooms): 
             id2=int(input("Enter Room ID "))
             roomno2=int(input("Enter Room No "))
             roomtypeid1=roomtypeid
             reservationid1=id1
             sql_insert_query = (""" INSERT INTO reservedroom (id,roomno,roomtypeid,reservationid)
             VALUES (%d,%d,%d,%d)"""%(id2,roomno2,roomtypeid1,reservationid1))
             cursor.execute(sql_insert_query)
             print ("Record inserted successfully into python_users table")
         connection.commit()    
    def cancel_booking():#
         id1=int(input("Enter Reservation ID for Cancel Booking "))
         val=1
         sql_update = (""" UPDATE RESERVATION SET cancelled=%d where id=%d"""%(val,id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table")
         if(connection.is_connected()):
             cancelleddate=datetime.date(datetime.now())
             cancelleddate1=cancelleddate.strftime('%Y-%m-%d')
         sql_update = (""" UPDATE RESERVATION SET cancelleddate=%s where
         id=%d"""%("'"+cancelleddate1+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         if(connection.is_connected()):
            val1=0
         sql_update = (""" UPDATE RESERVEDROOM SET STATUS=%d where
         RESERVATIONid=%d"""%(val1,id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def guest_arrived():
         print("Enter Details of Guest at Check In Time ")
         id1=int(input("Enter Guest ID "))
         reservationid=int(input("Enter Reservation ID "))
         cindate=input("Enter Check In Date ")
         cintime=input("Enter Check In Time ")
         roomid=int(input("Enter Room ID "))
         
         sql_insert_query = (""" INSERT INTO OCCUPIEDROOM (guest_id,cindate,cintime,roomid,reservationid)
         VALUES (%d,%s,%s,%d,%d)"""%(id1,"'"+cindate+"'","'"+cintime+"'",roomid,reservationid))
         cursor.execute(sql_insert_query)
         connection.commit()
         print("Enter Details of HOSTED at Check In Time ")
         id11=int(input("Enter Room ID "))
         guestid=int(input("Enter Guest ID "))
         sql_insert_query = (""" INSERT INTO hostedat (room_id,guestid,occupiedroomid) VALUES
         (%d,%d,%d)"""%(id11,guestid,id1))
         print(sql_insert_query)
         cursor.execute(sql_insert_query)
         connection.commit()
         print ("Record inserted successfully into python_users table")
    def guest_checkout():
         id1=int(input("Enter Reservation ID for Check Out "))
         coutdate=input("Enter Check Out Date ") 
         couttime=input("Enter Check Out Time ")
         val=0     
         sql_update = (""" UPDATE occupiedroom SET coutdate=%s where
         reservationid=%d"""%("'"+coutdate+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         sql_update = (""" UPDATE occupiedroom SET couttime=%s where
         reservationid=%d"""%("'"+couttime+"'",id1))
         cursor.execute(sql_update)
         connection.commit()
         sql_update = (""" UPDATE reservation SET cancelled=%s where id=%d"""%(val,id1))
         cursor.execute(sql_update)
         connection.commit()
         print ("Record inserted successfully into python_users table") 
    def billing():
         sql_select = ("SELECT GUESTID,ID FROM RESERVATION WHERE CANCELLED=0 AND BILLPAID=0")
         cursor = connection.cursor()
         cursor.execute(sql_select) 
         result = cursor.fetchall()
         print("Bill going to generate ")
         print("Customer Id Reservation Id ")
         for x in result:
             print(x[0]," ",x[1])   
    def billpay(): 
         print("Make Paymnet ")
         reservationid=int(input("Enter Reservation Id :"))
         sql_select = """SELECT G.FIRSTNAME,G.LASTNAME,RT.RENTPD,R.NO_OF_DAYS_STAY,
         R.CINDATE,R.COUTDATE FROM ROOMTYPE RT,RESERVEDROOM RR,RESERVATION R , GUEST G
         WHERE R.ID="{}" AND RR.ROOMTYPEID=RT.ROOM_TYPE_ID AND G.ID=R.GUESTID""".format(reservationid)
         cursor.execute(sql_select)
         result = cursor.fetchall()
         print(result)
         for x in result:
             fname=x[0]
             sname=x[1]
             rent=x[2]
             nod=x[3]
             amtpayable=rent*nod
             gst=amtpayable*18/100
             netamt=amtpayable+gst
             print("Mr / Mrs / Ms ",fname," ",sname)
             print("Total Bill Payable : ",netamt)
             val=1
             sql_update = (""" UPDATE RESERVATION SET cancelled=%d , billpaid=%d where id=%d"""%(val,val,reservationid))
             cursor.execute(sql_update)
             connection.commit()
             print ("Record inserted successfully into python_users table")
  
    while(True):
         print()
         print("************************************************************************************ Main Menu***********************************************************************")
         print()
         print("1. Room Type Details ")
         print("2. Reservation ")
         print("3. Guest Details ") 
         print("4. Guest Arrival Check In ")
         print("5. Guest Departure Check Out ")
         print("6. Billing ")
         print("7. Exit ")
         ch=int(input("Enter Choice from above "))
         if (ch<1 or ch >=7):
             break;
         if (ch==1):
             while(True):
                 print()
                 print("************************************************************************Room Type Details Menu**************************************************************************")
                 print()
                 print("1. Add Room Type ")
                 print("2. Modify Room Type ")
                 print("3. Modify Room Capacity ")
                 print("4. Modify Room Rent per Day ")
                 print("5. Modify Room No ")
                 print("6. Modify Room Status ")
                 print("7. Exit ")
                 ch1=int(input("Enter Choice from above "))
                 if (ch1==7): 
                     break;
                 if (ch1==1):
                     add_roomtype()
                 if (ch1==2):
                     modify_roomtype_type()
                 if (ch1==3):
                     modify_roomtype_capacity()
                 if (ch1==4):
                     modify_roomtype_rent()
                 if (ch1==5):
                     modify_roomtype_roomno()
                 if (ch1==6):
                     modify_roomtype_status()
            
                         
         if (ch==2):
             while(True):
                 print()
                 print("************************************************************************Reservation Menu**************************************************************************")
                 print()
                 print("1. New Booking ")
                 print("2. Modify Booking Date ")
                 print("3. Cancel Booking ")
                 print("4. Exit ") 
                 ch_res=int(input("Enter Choice from above "))
                 if (ch_res==4):
                     break;
                 if (ch_res==1):
                     new_booking()
                 if (ch_res==2):
                     cancel_booking()
                     new_booking()
                 if (ch_res==3):
                     cancel_booking()       
                         
         if (ch==3):
                 while(True):
                     print()
                     print("************************************************************************Guest Details Menu**************************************************************************")
                     print()
                     print("1. Add New Guest ")
                     print("2. Modify Guest First Name ")
                     print("3. Modify Guest Last Name ")
                     print("4. Modify Guest Membership Date ")
                     print("5. Modify Guest Address ")
                     print("6. Modify Guest City ")
                     print("7. Modify Guest Pincode ")
                     print("8. Modify Guest Mobile No ")
                     print("9. Exit ")
                     ch_guest=int(input("Enter Choice from above "))
                     if (ch_guest==9):
                         break;
                     if (ch_guest==1):
                         add_guest()
                     if (ch_guest==2):
                         modify_guest_firstname()
                     if (ch_guest==3):
                         modify_guest_lastname()
                     if (ch_guest==4):
                         modify_guest_mdate()
                     if (ch_guest==5):
                         modify_guest_address()
                     if (ch_guest==6):
                         modify_guest_city()
                     if (ch_guest==7):
                         modify_guest_pincode()
                     if (ch_guest==8):
                         modify_guest_mobileno()
        
         if (ch==4):
             guest_arrived()
         if (ch==5):
             guest_checkout()
         if (ch==6):
             billing()
             billpay()
except Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))         
finally:#closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")        
