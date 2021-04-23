#Imports Packages
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

#Power Rule Button is clicked.
    def button_clicked1(self):
        self.getChoice1()
        
        #Tells the user they selected the power rule.
        self.label1.setText("Power Rule Selected")
        self.label1.move(100,250)
        self.update2()
        
        #Tells the user what degree their original polynomial was.
        x = self.label2.text()
        self.label2.setText("Degree of Original Polynomial: "+x)
        self.update3()
        
 #Gets the number of degrees the Polynomial has       
    def getChoice1(self):
        items = ('0','1','2','3','4','5')
        choice, okPressed = QInputDialog.getItem(self, "Polynomial Degree","Largest Degree of Polynomial you are Taking Derivative of:", items, 0, False)
        if okPressed:
            self.label2.setText(choice)
            self.update3()
        self.AskForNums()
 
 #Asks for the coefficients with each term of the polynomial
    def AskForNums(self):
        choice = self.label2.text()
        #If the polynomial is degree 0...
        if choice == '0':
        #Asks for the coefficients of the polynomial
            w, okPressed = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 0:")
            if okPressed:
            # Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #No variable, only a number means derivative of 0.
                self.label3.setText('Polynomial Given: '+str(w))
                self.label4.setText("Your Derivative is: 0")
                self.update4()
                self.update5()
                
         #If the polynomial is degree 1...       
        if choice == '1':
        #Asks for the coefficients of the polynomial
            d,okPressed1 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 1:")
            w, okPressed2 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 0:")
            if okPressed2:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                self.label3.setText('Polynomial Given: '+str(d)+'x + '+str(w))
                self.label4.setText('Your Derivative is: '+str(d))
                self.update4()
                self.update5()
         
        #If the polynomial is degree 2...
        if choice == '2':
        #Asks for the coefficients of the polynomial
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 2:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 1:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 0:")
            if okPressed3:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*2
                self.label3.setText('Polynomial Given: '+str(a)+'x^2 + '+str(b)+'x + '+str(c))
                self.label4.setText('Your Derivative is: '+str(a1)+'x + '+str(b))
                self.update4()
                self.update5()
         
        #If the polynomial is degree 3...
        if choice == '3':
        #Asks for the coefficients of the polynomial
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 3:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 2:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 1:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 0:")
            if okPressed4:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                aAlmost = a*3
                a1 = round(aAlmost, 1)
                b1 = b*2
                self.label3.setText('Polynomial Given: '+str(a)+'x^3 + '+str(b)+'x^2 + '+str(c)+'x + '+str(d))
                self.label4.setText('Your Derivative is: '+str(a1)+'x^2 + '+str(b1)+'x + '+str(c))
                self.update4()
                self.update5()
                
         #If the the polynomial is degree 4...       
        if choice == '4':
        #Asks for the coefficients of the polynomial
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 4:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 3:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 2:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 1:")
            e, okPressed5 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 0:")
            if okPressed5:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*4
                bAlmost = b*3
                b1 = round(bAlmost, 1)
                c1 = c*2
                self.label3.setText('Polynomial Given: '+str(a)+'x^4 + '+str(b)+'x^3 + '+str(c)+'x^2 + '+str(d)+'x + '+str(e))
                self.label4.setText('Your Derivative is: '+str(a1)+'x^3 + '+str(b1)+'x^2 + '+str(c1)+'x + '+str(d))
                self.update4()
                self.update5()
                
         #If the polynomial is degree 5...       
        if choice == '5':
        #Asks for the coefficients of the polynomial
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 5:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 4:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 3:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 2:")
            e, okPressed5 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 1:")
            f, okPressed6 = QInputDialog.getDouble(self, "Coefficient","Type the coefficient with power 0:")
            if okPressed6:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*5
                b1 = b*4
                cAlmost = c*3
                c1 = round(cAlmost, 1)
                d1 = d*2
                self.label3.setText('Polynomial Given: '+str(a)+'x^5 + '+str(b)+'x^4 + '+str(c)+'x^3 + '+str(d)+'x^2 + '+str(e)+'x + '+str(f))
                self.label4.setText('Your Derivative is: '+str(a1)+'x^4 + '+str(b1)+'x^3 + '+str(c1)+'x^2 + '+str(d1)+'x + '+str(e))
                self.update4()
                self.update5()
                
                

    #Product Rule Button is clicked.
    def button_clicked2(self):
        #Finds the degree of each polynomial in the product.
        self.getChoice2()
        self.getChoice3()
        #Tells the user they selected the product rule.
        self.label1.setText("Product Rule Selected")
        self.label1.move(100,250)
        self.update2()
        
        #Does the derivative for each polynomial
        self.MultDiv()
        
        #Records the original polynomials and their derivatives
        a = self.label5.text()
        b = self.label6.text()
        c = self.label7.text()
        d = self.label8.text()
        
        
        
        #Tells the user what degree their original polynomial was.
        x = self.label2.text()
        y = self.label3.text()
        self.label2.setText("Degree of first Polynomial: "+x+" and Degree of second polynomial: "+y)
        self.update3()
        
        #Tells the user what they inputted.
        self.label3.setText('Polynomial Given: ('+a+')('+b+')')
        #Tells the user their derivative.
        self.label4.setText('Your Derivative is: ('+a+')('+d+') +')
        self.label9.setText('('+b+')('+c+')')
        self.update4()
        self.update5()
        self.update6()
        
        #clear the dummy variables
        self.label5.setText("")
        self.label6.setText("")
        self.label7.setText("")
        self.label8.setText("")
        
        
    #Quotient Rule Button is clicked.    
    def button_clicked3(self):
        #Finds the degree of each polynomial in quotient.
        self.getChoice2()
        self.getChoice3()
        
        #Tells the user they selected the quotient rule.
        self.label1.setText("Quotient Rule Selected")
        self.label1.move(100,250)
        self.update2()
        
        #Does the derivative for each polynomial
        self.MultDiv()
        
        #Records the original polynomials and their derivatives.
        a = self.label5.text()
        b = self.label6.text()
        c = self.label7.text()
        d = self.label8.text()
        
        
        #Tells the user what degree their original polynomial was.
        x = self.label2.text()
        y = self.label3.text()
        self.label2.setText("Degree of Numerator: "+x+" and Degree of Denominator: "+y)
        self.update3()
        
        #Tells the user what they gave the program.
        self.label3.setText('Polynomial Given: ('+a+')/('+b+')')
        
        #Tells the user their derivative.
        self.label4.setText('Your Derivative is: ('+b+')('+c+') -')
        self.label9.setText('('+a+')('+d+')') 
        self.label10.setText('/ ('+b+')^2')
        self.update4()
        self.update5()
        self.update6()
        self.update7()
        
        #clear the dummy variables
        self.label5.setText("")
        self.label6.setText("")
        self.label7.setText("")
        self.label8.setText("")
     

    #Finds degree of first polynomial or the numerator through a pop up combo box. 
    def getChoice2(self):
        items = ('0','1','2','3','4','5')
        choice, okPressed = QInputDialog.getItem(self, "Polynomial Degree","Largest Degree of NUMERATOR(if dividing) OR FIRST Polynomial:", items, 0, False)
        if okPressed:
            self.label2.setText(choice)
            self.update3()
            
    #Finds the degree of the second polynomial or the denominator through another pop up combo box.    
    def getChoice3(self):
        items = ('0','1','2','3','4','5')
        choice, okPressed = QInputDialog.getItem(self, "Polynomial Degree","Largest Degree of DENOMINATOR(if dividing) OR SECOND Polynomial:", items, 0, False)
        if okPressed:
            self.label3.setText(choice)
            self.update4()
       


     #This finds the derivatives of both the first/numerator polynomial and the second/denominator polynomial.
    def MultDiv(self):
        #NUMERATOR/FIRST POLYNOMIAL!!!
        
        choice1 = self.label2.text()
        #If the polynomial is degree 0...
        if choice1 == '0':
        #Asks for the coefficients of the polynomial
            w, okPressed = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 0:")
            if okPressed:
            # Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #No variable, only a number means derivative of 0.
                self.label5.setText(str(w))
                self.label7.setText("0")
                
                
         #If the polynomial is degree 1...       
        if choice1 == '1':
        #Asks for the coefficients of the polynomial
            d,okPressed1 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 1:")
            w, okPressed2 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 0:")
            if okPressed2:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                self.label5.setText(str(d)+'x + '+str(w))
                self.label7.setText(str(d))
                
                
        if choice1 == '2':
        #If the polynomial is degree 2...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 2:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 1:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 0:")
            if okPressed3:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*2
                self.label5.setText(str(a)+'x^2 + '+str(b)+'x + '+str(c))
                self.label7.setText(str(a1)+'x + '+str(b))
                
                
        if choice1 == '3':
        #If the polynomial is degree 3...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 3:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 2:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 1:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 0:")
            if okPressed4:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                aAlmost = a*3
                a1 = round(aAlmost, 1)
                b1 = b*2
                self.label5.setText(str(a)+'x^3 + '+str(b)+'x^2 + '+str(c)+'x + '+str(d))
                self.label7.setText(str(a1)+'x^2 + '+str(b1)+'x + '+str(c))
                
                
        if choice1 == '4':
        #If the polynomial is degree 4...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 4:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 3:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 2:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 1:")
            e, okPressed5 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 0:")
            if okPressed5:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*4
                bAlmost = b*3
                b1 = round(bAlmost, 1)
                c1 = c*2
                self.label5.setText(str(a)+'x^4 + '+str(b)+'x^3 + '+str(c)+'x^2 + '+str(d)+'x + '+str(e))
                self.label7.setText(str(a1)+'x^3 + '+str(b1)+'x^2 + '+str(c1)+'x + '+str(d))
             
                
        if choice1 == '5':
        #If the polynomial is degree 5...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 5:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 4:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 3:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 2:")
            e, okPressed5 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 1:")
            f, okPressed6 = QInputDialog.getDouble(self, "Coefficient","FIRST POLYNOMIAL/NUMERATOR:Type the coefficient with power 0:")
            if okPressed6:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*5
                b1 = b*4
                cAlmost = c*3
                c1 = round(cAlmost, 1)
                d1 = d*2
                self.label5.setText(str(a)+'x^5 + '+str(b)+'x^4 + '+str(c)+'x^3 + '+str(d)+'x^2 + '+str(e)+'x + '+str(f))
                self.label7.setText(str(a1)+'x^4 + '+str(b1)+'x^3 + '+str(c1)+'x^2 + '+str(d1)+'x + '+str(e))
               
               
               
        #DENOMINATOR/SECOND POLYNOMIAL!!!
        
        choice2 = self.label3.text()
        #If the polynomial is degree 0...
        if choice2 == '0':
        #Asks for the coefficients of the polynomial
            w, okPressed = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 0:")
            if okPressed:
            # Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #No variable, only a number means derivative of 0.
                self.label6.setText(str(w))
                self.label8.setText("0")
                
                
         #If the polynomial is degree 1...       
        if choice2 == '1':
        #Asks for the coefficients of the polynomial
            d,okPressed1 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 1:")
            w, okPressed2 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 0:")
            if okPressed2:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                self.label6.setText(str(d)+'x + '+str(w))
                self.label8.setText(str(d))
                
                
        if choice2 == '2':
        #If the polynomial is degree 2...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 2:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 1:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 0:")
            if okPressed3:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*2
                self.label6.setText(str(a)+'x^2 + '+str(b)+'x + '+str(c))
                self.label8.setText(str(a1)+'x + '+str(b))
                
                
        if choice2 == '3':
        #If the polynomial is degree 3...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 3:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 2:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 1:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 0:")
            if okPressed4:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                aAlmost = a*3
                a1 = round(aAlmost, 1)
                b1 = b*2
                self.label6.setText(str(a)+'x^3 + '+str(b)+'x^2 + '+str(c)+'x + '+str(d))
                self.label8.setText(str(a1)+'x^2 + '+str(b1)+'x + '+str(c))
                
                
        if choice2 == '4':
        #If the polynomial is degree 4...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 4:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 3:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 2:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 1:")
            e, okPressed5 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 0:")
            if okPressed5:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*4
                bAlmost = b*3
                b1 = round(bAlmost, 1)
                c1 = c*2
                self.label6.setText(str(a)+'x^4 + '+str(b)+'x^3 + '+str(c)+'x^2 + '+str(d)+'x + '+str(e))
                self.label8.setText(str(a1)+'x^3 + '+str(b1)+'x^2 + '+str(c1)+'x + '+str(d))
             
                
        if choice2 == '5':
        #If the polynomial is degree 5...
            a, okPressed1 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 5:")
            b, okPressed2 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 4:")
            c, okPressed3 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 3:")
            d, okPressed4 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 2:")
            e, okPressed5 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 1:")
            f, okPressed6 = QInputDialog.getDouble(self, "Coefficient","SECOND POLYNOMIAL/DENOMINATOR:Type the coefficient with power 0:")
            if okPressed6:
            #Writes what the given polynomial was, what the derivative is, and updates the sizes of the labels.
            #Take exponent n, multiply it by the coefficient, then display new coefficient as this multiplied by x to the n-1 power. Drop last number.
                a1 = a*5
                b1 = b*4
                cAlmost = c*3
                c1 = round(cAlmost, 1)
                d1 = d*2
                self.label6.setText(str(a)+'x^5 + '+str(b)+'x^4 + '+str(c)+'x^3 + '+str(d)+'x^2 + '+str(e)+'x + '+str(f))
                self.label8.setText(str(a1)+'x^4 + '+str(b1)+'x^3 + '+str(c1)+'x^2 + '+str(d1)+'x + '+str(e))
        
        
        
        
        
        
        
    #Trigonometry button is pressed, this event occurs.
    def button_clicked4(self):
        #Tells the user they selected the trigonometry derivative.
        self.label1.setText("Trigonometry Derivatives Selected")
        self.label1.move(50,250)
        self.update2()
        
        #Gets the choice of the user on what type of trigonometic polynomial they want to take the derivative of, and takes that derivative using polynomial_answer.
        self.getChoice4()
        self.polynomial_answer()
        
        x = self.label2.text()
        #Writes the polynomial chosen by the user.
        self.label3.setText('Polynomial Given: '+x)
        self.update4()
        #Clears the dummy variables.
        self.label2.setText('')
        
        
    def getChoice4(self):
        #Creates a list of items, then asks the user to choose one of the items to take the derivative of, and records that choice in a label.
        items = ('sin(x)','cos(x)','tan(x)','csc(x)','sec(x)','cot(x)','sin^-1(x)','cos^-1(x)','tan^-1(x)','csc^-1(x)','sec^-1(x)','cot^-1(x)')
        choice, okPressed = QInputDialog.getItem(self, "Trigonometry Option","Choose an option to take the derivative of:", items, 0, False)
        if okPressed:
            self.label2.setText(choice)
            self.update3()
     
     
     
    def polynomial_answer(self):
        
        #Grabs the choice from getChoice4 that was stored in the label.
        choice = self.label2.text()
        
        #If the choice of the user is sin(x), it sets a label to contain the derivative of that choice.
        if choice == 'sin(x)':
            self.label4.setText('Your derivative is: cos(x)')
            self.update5()
         
         #If the choice of the user is cos(x), it sets a label to contain the derivative of that choice.
        if choice == 'cos(x)':
            self.label4.setText('Your derivative is: -sin(x)')
            self.update5()
         
         #If the choice of the user is tan(x), it sets a label to contain the derivative of that choice.
        if choice == 'tan(x)':
            self.label4.setText('Your derivative is: sec^2(x)')
            self.update5()
         
         #If the choice of the user is csc(x), it sets a label to contain the derivative of that choice.
        if choice == 'csc(x)':
            self.label4.setText('Your derivative is: -csc(x)cot(x)')
            self.update5()
         
         #If the choice of the user is sec(x), it sets a label to contain the derivative of that choice.
        if choice == 'sec(x)':
            self.label4.setText('Your derivative is: sec(x)tan(x)')
            self.update5()
         
          #If the choice of the user is cot(x), it sets a label to contain the derivative of that choice.
        if choice == 'cot(x)':
            self.label4.setText('Your derivative is: -csc^2(x)')
            self.update5()
         
         #If the choice of the user is sin^-1(x), it sets a label to contain the derivative of that choice.
        if choice == 'sin^-1(x)':
            self.label4.setText('Your derivative is: 1/(sqrt(1-x^2))')
            self.update5()
            
         #If the choice of the user is cos^-1(x), it sets a label to contain the derivative of that choice.
        if choice == 'cos^-1(x)':
            self.label4.setText('Your derivative is: -1/(sqrt(1-x^2))')
            self.update5()
          
         #If the choice of the user is tan^-1(x), it sets a label to contain the derivative of that choice. 
        if choice == 'tan^-1(x)':
            self.label4.setText('Your derivative is: 1/(1+x^2)')
            self.update5()
         
         #If the choice of the user is csc^-1(x), it sets a label to contain the derivative of that choice.
        if choice == 'csc^-1(x)':
            self.label4.setText('Your derivative is: -1/(|x|*sqrt(1-x^2))')
            self.update5()
            
         #If the choice of the user is sec^-1(x), it sets a label to contain the derivative of that choice.
        if choice == 'sec^-1(x)':
            self.label4.setText('Your derivative is: 1/(|x|*sqrt(1-x^2))')
            self.update5()
            
         #If the choice of the user is cot^-1(x), it sets a label to contain the derivative of that choice.
        if choice == 'cot^-1(x)':
            self.label4.setText('Your derivative is: -1/(1+x^2)')
            self.update5()
            


     

    #Restarts the app, clearing all the labels except the welcome label.
    def restart(self):
        self.label1.setText("")
        self.label2.setText("")
        self.label3.setText("")
        self.label4.setText("")
        self.label9.setText("")
        self.label10.setText("")
    




    def initUI(self):
        #Window Size
        self.setGeometry(200, 200, 1050, 600)
        
        #Window Title
        self.setWindowTitle('Fully Functional Derivative Calulator!')
        
        #Welcome label, adding text, moving it, and putting a border around it.
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome! Please select the rule you will be applying to your polynomial.")
        self.label.move(250,10)
        self.label.setStyleSheet("border: 1px solid black;")
  
        self.label.adjustSize()
        
        #Creating the button for the Power Rule
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Power Rule")
        self.b1.clicked.connect(self.button_clicked1)
        self.b1.move(450,50)
        self.b1.adjustSize()
        self.b1.setStyleSheet("background-color: lightsalmon;")
        
        #Creating the button for the Product Rule
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(450,100)
        self.b2.setText("Product Rule")
        self.b2.clicked.connect(self.button_clicked2)
        self.b2.adjustSize()
        self.b2.setStyleSheet("background-color: lightsalmon;")
        
        #Creating the button for the Quotient Rule
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.move(450,150)
        self.b3.setText("Quotient Rule")
        self.b3.clicked.connect(self.button_clicked3)
        self.b3.adjustSize()
        self.b3.setStyleSheet("background-color: lightsalmon;")
        
        #Creating the button for the Trigonometry Derivatives
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.move(385,200)
        self.b4.setText("Some Trigonometry Derivatives")
        self.b4.clicked.connect(self.button_clicked4)
        self.b4.adjustSize()
        self.b4.setStyleSheet("background-color: lightsalmon;")
        
        #Creating the restart button
        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setText("Restart")
        self.b5.move(450,550)
        self.b5.adjustSize()
        #Connects to the restart function
        self.b5.clicked.connect(self.restart)
        #Changes the color of the button
        self.b5.setStyleSheet("background-color: lightsalmon;")
        
        #Creating and moving all the labels
        self.label1 = QtWidgets.QLabel(self)
        self.label2 = QtWidgets.QLabel(self)
        self.label2.move(100,300)
        self.label3 = QtWidgets.QLabel(self)
        self.label3.move(100,350)
        self.label4 = QtWidgets.QLabel(self)
        self.label4.move(100,400)
        self.label9 = QtWidgets.QLabel(self)
        self.label9.move(240,420)
        self.label10 = QtWidgets.QLabel(self)
        self.label10.move(240,440)
        
        #dummy labels used as variables in a way between definitions.
        self.label5 = QtWidgets.QLabel(self)
        self.label6 = QtWidgets.QLabel(self)
        self.label7 = QtWidgets.QLabel(self)
        self.label8 = QtWidgets.QLabel(self)


#All the label adjustments (for non-dummy labels)
    def update(self):
        self.label.adjustSize()
        
    def update2(self):
        self.label1.adjustSize()
        
    def update3(self):
        self.label2.adjustSize()
        
    def update4(self):
        self.label3.adjustSize()
        
    def update5(self):
        self.label4.adjustSize()
        
    def update6(self):
        self.label9.adjustSize()
        
    def update7(self):
        self.label10.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    #Changes background color of app
    win.setStyleSheet("background-color: oldlace;")
    win.show()
    sys.exit(app.exec_())

window()