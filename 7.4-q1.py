def Get_Winnings(m):
    if m.isnumeric()==True:
        if m == 1:
            return 75000
        if m == 2:
            m=int(m)+149998
            return m
        if m == 3:
            m=int(m)+224997
            return m
        if m == 4:
            m=int(m)+299996
            return m
        if m == 5:
            m=int(m)+374995
            return m
        else:
            return m=='Invalid'
    else:
        return m=='Invalid'
medals=input("Enter Gold Medals Won: ")
Get_Winnings(medals)
print("Your prize money is:",medals)
 #use as reference
"https://courses.projectstem.org/courses/216500/pages/7-dot-4-returning-values?module_item_id=45673849"