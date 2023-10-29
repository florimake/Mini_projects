def likes(names):
    if int(len(names)) == 0:
        print(f'--> "no one likes this"')
    elif int(len(names)) == 1:
        print(f'--> "{names[0]} likes this"')
    elif int(len(names)) == 2:
        print(f'--> "{names[0]} and {names[1]} like this"')
    elif int(len(names)) == 3:
        print(f'--> "{names[0]}, {names[1]} and {names[2]} like this"')      
    elif int(len(names)) > 3:
        print(f'--> "{names[0]}, {names[1]} and {int(len(names))-2} others like this"')
        
          
likes(["Claudia","Nicu", "Arpad", "Florin", "Mark", "Max"])