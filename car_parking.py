while True:
    
    Input_time = int(input("Input Time.."))
    
    Sum = float(0)
    
    if(Input_time <= 15):
        print("Free...")
        
    elif(Input_time > 15 and Input_time <= 360):
        if(Input_time <= 180):
            Sum = Input_time//6
            
        else:
            Sum = (180//6)+((Input_time - 180)/3)
        print("%.2f"%Sum,"THB.")
        
    else:
        Sum = 200
        print(Sum,"THB.")
