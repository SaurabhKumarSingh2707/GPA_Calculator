print("################# GPA CALCULATOR #################")
# getting marks as input 
pc=int(input("Enter the c programming marks:"))
chem=int(input("Enter the Chemistry marks:"))
eee=int(input("Enter the EEE marks:"))
eng=int(input("Enter the English marks:"))
mat=int(input("Enter the Maths marks:"))
chemLab=int(input("Enter the Chemistry lab marks:"))
print("##################################################")

if pc in range(90,100):
    gp1=10
elif pc in range(80,90):
    gp1=9
elif pc in range(70,80):
    gp1=8
elif pc in range(60,70):
    gp1=7
elif pc in range(50,60):
    gp1=6
else:
    gp1=0    
    
if chem in range(90,100):
    gp2=10
elif chem in range(80,90):
    gp2=9
elif chem in range(70,80):
    gp2=8
elif chem in range(60,70):
    gp2=7
elif chem in range(50,60):
    gp2=6
else:
    gp2=0 
    
if eee in range(90,100):
    gp3=10
elif eee in range(80,90):
    gp3=9
elif eee in range(70,80):
    gp3=8
elif eee in range(60,70):
    gp3=7
elif eee in range(50,60):
    gp3=6
else:
    gp3=0 
    
    
if eng in range(90,100):
    gp4=10
elif eng in range(80,90):
    gp4=9
elif eng in range(70,80):
    gp4=8
elif eng in range(60,70):
    gp4=7
elif eng in range(50,60):
    gp4=6
else:
    gp4=0 
    
if mat in range(90,100):
    gp5=10
elif mat in range(80,90):
    gp5=9
elif mat in range(70,80):
    gp5=8
elif mat in range(60,70):
    gp5=7
elif mat in range(50,60):
    gp5=6
else:
    gp5=0 
    
    
if chemLab in range(45,50):
    gp6=10
elif chemLab in range(40,45):
    gp6=9
elif chemLab in range(35,40):
    gp6=8
elif chemLab in range(30,35):
    gp6=7
elif chemLab in range(25,30):
    gp6=6
else:
    gp6=0 
    
    
cd1=4
cd2=3
cd3=3
cd4=3
cd5=3
cd6=1

GPA = ((cd1*gp1)+(cd2*gp2)+(cd3*gp3)+(cd4*gp4)+(cd5*gp5)+(cd6*gp6))/(cd1+cd2+cd3+cd4+cd5+cd6)
print("Your GPA is :",GPA)
print("##################################################")