import mysql.connector as con

# modify this line of code according to your mySQL settings.

connector = con.connect(host='localhost', user='root', password= 'abc', database = "GKquiz")

cursor = connector.cursor()

cursor.execute("create table questions(qno integer primary key, question varchar(3000), option_a varchar(500), option_b varchar(500), option_c varchar(500), option_d varchar(500), correct_option varchar(500))")

def choices():
    
    print("Hello! Welcome to quiz maker")
    print("1. To make new questions (admin only)")
    print("2. To display (admin only)")
    print("3. To register")
    print("4. To get your registration number")
    print("5. To play quiz")
    print("6. To check scores")
    

def newq():
    
    password = 'abc+123'
    w = input(" Enter password: ")
    if w == password:
        qno = int(input("Enter question number: "))
        question = input("Enter question: ")
        option_a = input("Enter option a: ")
        option_b = input("Enter option b: ")
        option_c = input("Enter option c: ")
        option_d = input("Enter option d: ")
        correct_option = input("Enter correct option: ")
        sql_insert = "insert into questions(qno, question, option_a, option_b, option_c, option_d, correct_option)values({},'{}','{}','{}','{}','{}','{}')".format(qno, question, option_a, option_b, option_c, option_d, correct_option)
        cursor.execute(sql_insert)
        connector.commit()
    
     else:
        print(" wrong password")
        choices()

def disp():
    
    password= 'abc+123'
    psw= input("Enter the password: ")
    if password==psw:
        cursor.execute("select * from questions")
        data = cursor.fetchall()
        for row in data:
                print(row)
    else:
        print ("invalid password")
        choices()

cursor.execute("create table participant_info( reg_no int(10) auto_increment primary key, name varchar(50), age int(10),city varchar(50))")       

def participate():
    
    l= int(input("Are you new participant? (yes=1/no=2): "))
    
    if l==1:
            
            names=input("enter the participant name: ")
            name=names.upper()
            age=int(input("enter the age: "))
            city=input("enter the city: ")                                                           
            
    elif l==2:
         
            print("You can play the quiz")
            choices()
    
    sql_int="insert into participant_info(city, name, age)values('{}','{}', {})".format(city,name,age)
    cursor.execute(sql_int)
    connector.commit()

def regno():
    
    cursor.execute("select reg_no, name from participant_info")
    na=cursor.fetchall()
    nams=input("Enter your name: ")
    nam= nams.upper()
    
    for e in na:
        if nam== e[1]:
            print("your registration no is",e[0])
            print()
    
cursor.execute("create table score2(participant_no int(10) auto_increment primary key ,reg_no int(5) , scores int(50),  total_correct int(50),total_wrong int(50))")

def quiz():
            regis= int(input("Enter your registration number: ")) 
            cursor.execute("select reg_no from participant_info")
            par= cursor.fetchall()
     
            for number in par:
                n=list(number)
                if regis == number[0]:
                     score=0
                     correct=0
                     wrong=0
            
                     question=cursor.execute("select qno, question, option_a, option_b, option_c, option_d from questions")
                     q= cursor.fetchall()
             
         
                     for i in range (len(q)):
                        print(q[i])
                        ans = input("Enter your answer: ")
                        cursor.reset()
                        cursor.execute("select correct_option from questions")
                        data = cursor.fetchall()
                        
                        if (data[i] == (ans,)):
                            score+=5
                            correct+=1
                    
                            print("Correct answer! Congrats")
                        else:
                            print("Wrong answer! correct answer is", data[i])
                            wrong+=1
                        

                     sql_ins="insert into score2 (reg_no,scores, total_correct, total_wrong)values ({},{},{},{})".format(regis,score,correct,wrong)
                     cursor.execute(sql_ins)
                     connector.commit()

def score():
    cursor.execute("select * from score2")
    d = cursor.fetchall()
    reg= int(input("Enter your registration no.: "))
    for r in d:
        if reg== r[1]:
            print ("Your score:", r[2])
            print("Total correct:", r[3])
            print("Total wrong:", r[4])
            print()

def main():
    while True:
        choices()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            newq()
        elif choice == 2:
            disp()
        elif choice ==3:
            participate()
        elif choice ==  5:
            quiz()
        elif choice == 6:
            score()
            break
        elif choice == 4:
            regno()
        else:
            print("Invalid input")
main()
        



            
            
        
