import mysql.connector 

def DataUpdate(FirstName, LastName,PhoneNumber,EMail,Age,Location,Reason,HealthCenter,Date): 
              mydb = mysql.connector.connect( host="localhost", user="root",  passwd="root", database="APPOINTMENT_BOOKING_DATA") 
              mycursor = mydb.cursor() 
              # sql = "CREATE TABLE PATIENT_DATA(FirstName VARCHAR(255),LastName VARCHAR(255), PhoneNumber VARCHAR(255), EMail VARCHAR(255), Age VARCHAR(255), Location VARCHAR(255), Reason  VARCHAR(255), HealthCenter VARCHAR(255), Date VARCHAR(255));"
              sql='INSERT INTO PATIENT_DATA(FirstName, LastName, PhoneNumber, EMail, Age, Location, Reason, HealthCenter, Date) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}");'.format(FirstName, LastName, PhoneNumber, EMail, Age, Location, Reason, HealthCenter, Date) 
              mycursor.execute(sql) 
              mydb.commit()
              print(mycursor.rowcount,"record inserted.")
if __name__ == '__main__':
    DataUpdate("Sara", "Geller","1234354656","sara@gmail.com","30","Santa Clara","Cough","Kaiser","2nd May")