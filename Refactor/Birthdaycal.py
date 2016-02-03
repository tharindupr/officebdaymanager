__name__='birthdaycal'
def birthdaycal(idnumber):
    #print(idnumber)
    year=int('19'+idnumber[:2])
    if(int(idnumber[2:5])>500):
        dmonth=int(idnumber[2:5])-500
    else:
        dmonth=int(idnumber[2:5])
    #print(dmonth)
    dayssum=0
    pmonthsum=0
    month=0
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in days:
        
        dayssum+=i
        month+=1
        #print(dayssum)
        if(dmonth-dayssum<=0):
            #print(dmonth-pmonthsum)
            day=dmonth-pmonthsum
            month=month
            break
        
        pmonthsum=dayssum
     
    return(str(year)+'/'+str(month)+'/'+str(day))
