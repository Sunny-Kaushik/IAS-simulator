# IAS-simulator
1) main memory- stores both data and Instruction.
2) ALU(Arithematic logic unit): this unit is capable of operating on binary data (but here in my code I have used the hexadecimal format to make my program look simple and readable).
3) Control Unit: this unit interprets the instructions in memory and causes them to be executed.
  
Both control unit and ALU contain storage locations, called as registers. The various registers used are:
1) Program counter (PC): Contains the address of the next instruction pair to be fetched from memory.(12 bits)
2) Memory address register (MAR): Specifies the address in memory of the word to be written from or read into the MBR.
3) Memory buffer register (MBR): Contains a word to be stored in memory or sent to the I/O unit, or is used to receive a word from memory or from the input/output unit.
4) Instruction register (IR): Contains the 8-bit opcode instruction being executed.
5)  Instruction buffer register (IBR): holds temporarily the right hand instruction from a word in memory.
6) Accumulator(AC): holds the result of an ALU operation.(40 bits)
7) Multiplier Quotient (MQ): stores the least significant bits of the result of the product.

 
Input Format: (This part is commented out in the code)
The user needs to input the command in a sequence followed by a number which will hold the PC value until next set of statements is given by the user.
for example:
0 100
1 101
2 LOAD M(00) ADD M(01)
3 STOR M(10)
end
