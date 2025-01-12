attendance = int(input("Enter the attendance of the student: "))
medical_cause = input("Do you have a medical cause? Write as Yes or No")
if medical_cause == "Yes" :
    print("You are allowed to take the exam! You may enter!")
else:
    if attendance >=75:
        print("You are allowed to write the exam due to good attendance! Hooray! You may enter!")
    else:
        print("You are not allowed to take the exam due to poor attendance without any probable cause! Get out 😠")