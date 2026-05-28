import pandas as pd
data = {
    "Name" : ["Kashish", "Shrutik", "Swati", "Priya", "Prateek","Bishal", "Arya", "Yash"],
    "Maths" : [85, 92, 78, None, 95, 88, 72, 90],
    "Science" : [78, 85, None, 82, 91, 76, 68, 88],
     "English": [90, 88, 85, 79, None, 92, 75, 86]
}
dt = pd.DataFrame(data)
print(dt)

#ab yaha swati prateek aur priya ke marks missing hai  NaN check karenge aur fix karenge
print(dt.isnull().sum()) #checking how many nulls are there
dt["Maths"] =dt["Maths"].fillna((dt["Maths"].mean())) #FIXING NULL VALUES
dt["Science"] = dt["Science"].fillna((dt["Science"].mean()))
dt["English"] = dt["English"].fillna(dt["English"].mean())
print(dt)

#ADDING NEW COLUMNE
dt["TOTAL"] = dt['Maths'] + dt["Science"] + dt["English"]
print(dt)
dt["Percentage"] = (dt["TOTAL"] / 300) * 100
print(dt)
# Top student dhundho!
#Percentage ke hisaab se descending sort karo
print(dt.sort_values("Percentage" , ascending = False))
print(dt[["Maths", "Science", "English"]].mean())
