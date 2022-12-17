from pickle import TRUE
#initialising the first 100 elements of the list memory to 0
memory=[0]*15
AC=0
PC=0
MBR=0
IR="0"
IBR="0"
MQ="0"
str1=1
#describing the instructions associated with each opcode i.e, different instructions of the opcode
#---------Instructions with their opcodes in hexadecimal form-----------#
#0100 --> LOAD
#2100 --> STOR
#0500 --> ADD
#0600 --> SUB
#1100 --> MUL

# the conversion steps has been described in first instruction which will be followed by all 
def IASAssembler(str1,str2):
    if (str1 == "LOAD"):
        loc = str2[2:4] #will store the location of the memory where the instruction will be stored
        loc = str(hex(int(loc)))#since the input taken is in the form of the string, hence first convert it to integer and then hexadecimal
        loc = loc[2:]#after converting to hexadecimal 0x will be added as prefix, hence slicing it
        instC = "0100" + loc #appending the 4 bit opcode (since I have worked on hexadecimal format, therefore its in 4 bit) to the 6 bit hex address
        return instC
    elif str1 == "STOR":
        loc = str2[2:4]
        loc = str(hex(int(loc)))
        loc = loc[2:]
        instC = "2100"+loc
        return instC
    
    elif str1=="MUL":
        loc=str2[2:4]
        loc=str(hex(int(loc)))
        loc=loc[2:]
        instC="1100"+loc
        return instC
    elif str1=="SUB":
        loc=str2[2:4]
        loc=str(hex(int(loc)))
        loc=loc[2:]
        instC="0600"+loc
        return instC
    elif str1=="ADD":
        loc=str2[2:4]
        loc=str(hex(int(loc)))
        loc=loc[2:]
        instC="0500"+loc
        return instC
    elif str1=="LOAD,MQ":
        loc=str2[2:4]
        loc=str(hex(int(loc)))
        loc=loc[2:]
        instC="1000"+loc
        return instC
    elif str1=="JUMP":
         loc=str2[2:4]
         loc=str(hex(int(loc)))
         loc=loc[2:]
         instC="1300"+loc
         return instC







    


print("Input format : 1st and 2nd will consists of numbers on which the operation is to be performed\n")
print("From 2nd line enter the instructions you want to execute\n")
print("You need to enter the memory location (strictly in two digit) and data separated by space\n")
# condToincrementPC=0
# while(True):
#     userInput=input().split()
#     if (userInput[0]=="end"):
#         break
#     checkforNum = any(map(str.isdigit, userInput[1]))#checks if string contains a number or not
    
#     if checkforNum:
#         j=str(hex(int(userInput[1])))
#         memory[int(userInput[0])]=j[2:]#converting the integer to hexadecimal form while removing the "0x" part
#     else:
#         if(condToincrementPC==0):
#             PC=int(userInput[0])
#             condToincrementPC+=1
#         if len(userInput)==3:
#             q=IASAssembler(userInput[1],userInput[2]) + "00000"
#             memory[int(userInput[0])]=q
#         else:
#             str1=IASAssembler(userInput[1],userInput[2])
#             str2=IASAssembler(userInput[3],userInput[4])
#             memory[int(userInput[0])]=str1+str2




str1=1 #str here will decide that which instruction is to be executed first
#for str =0 then left instruction will be taken into account and will be worked on and for str =1 right instruction will be taken into account and will be worked on  
print(f"PC={PC}")
def pro():
    global str1
    global MAR
    global MBR
    global PC
    global IR
    global IBR
    global AC
    while(memory[PC]!=0):
        m=memory[PC]
        if(str1==1):
            IBR=m[5:10]
            IR=m[0:2]
            MAR=m[2:5]
        elif(str1==0):
            IBR="00000"
            IR=m[5:7]
            MAR=m[7:10]
        if(IR=="01"):
            MBR=memory[int(MAR,16)]
            AC=int(MBR,16)
            if(int(IBR,16)==0):
                str1=1
                PC=PC+1
            else:
                str1=0
        elif(IR=="21"):
            MBR=AC
            memory[int(MAR,16)]=MBR
            if(int(IBR,16)==0):
                str1=1
                PC=PC+1
            else:
                str1=0
        elif(IR=="05"):
            MBR=(memory[int(MAR,16)])
            AC=AC+int(MBR,16)
            if(int(IBR,16)==0):
                str1=1
                PC=PC+1
            else:
                str1=0
        elif(IR=="06"):
            MBR=(memory[int(MAR,16)])
            AC=AC-int(MBR,16)
            if(int(IBR,16)==0):
                str1=1
                PC=PC+1
            else:
                str1=0
    #
        elif(IR=="11"):
            MBR=(memory[int(MAR,16)])
            AC=AC*int(MBR,16)
            x=AC
            z=0
            for i in range(x):
                z=z+int(MBR,16)
            AC=z
                
            if(int(IBR,16)==0):
                str1=1
                pc=pc+1
            else:
                str1=0

    #



        elif(IR=="11"):
            MBR=(memory[int(MAR,16)])
            for i in range (AC):
                AC=AC+(int(MBR,16))
            if(int(IBR,16)==0):
                str1=1
                PC=PC+1
            else:
                str1=0



        elif(IR == "04"):
            print(f"-|M({MAR})|\n")
            AC = memory[MAR]
            if(AC > 0):
                AC = -AC
            elif(AC < 0):
                AC = AC
        elif(IR == "03"):
            print(f"LOAD |M({MAR})|\n")
            AC = memory[MAR]
            if(AC >= 0):
                AC = AC
            elif(AC < 0):
                AC = -AC
        elif(IR == "08"):
            print(f"ADD |M({MAR})")
            if(memory[MAR] > 0):
                AC = AC + memory[MAR]
            else:
                AC = AC-memory[MAR]
        elif(IR == 10):
            print(f"SUB |M({MAR})")
            if(memory[MAR] > 0):
                AC = AC-memory[MAR]
            else:
                AC = AC+memory[MAR]
        elif(IR == "13"):
            print(f"JUMP M({MAR}, 0:19)\n")
            PC = MAR
            MBR = memory[MAR]
            # after shifting 32 bits we'll left with 8 bits which is the opcode
            IR = (MBR >> 16)
            MAR = (MBR >> 10) % (1 << 10)#it will store the address
            IBR=MBR%(1 << 10)
        



    
sum=0
print(f"The list containing the data and instructions in hexadecimal format:\n{memory}")
print("The result printed will be in decimal form with base 10 at the specified memory location.")
memory=[0,0,0,0,0,0,0,0,0,0,'0100005001','0500205003','0500405005','0500621009',0,0]
for i in range(8):

    #taking input and converting the number to hexadecimal 
    x=int(input())


    #converting the hex to string
    x=str(hex(x))
    x=x[2:]
    memory[i]=x
for i in range(8):
    sum=sum+int(memory[i])
memory[14]=sum
PC=10
print(memory)
pro()