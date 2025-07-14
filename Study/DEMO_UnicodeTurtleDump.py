import turtle

data = ''
for char in range(9812, 9824):
    try:
       data += chr(char) 
    except:
        pass
turtle.goto(-300, 0)
turtle.write(data, font=("Ariel", 48, "normal"))



              
