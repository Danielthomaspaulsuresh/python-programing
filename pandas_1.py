import pandas as pd
"""
a = [1,2,3]

var = pd.Series(a,index=["x","y","Z"])

print(var["y"])


calories = {"day1":250, "day2":380,"day3":450}

var = pd.Series(calories, index=["day1","day2"])
print(var)

data = {

    "calories" : [420,320,390],
    "duration": [50,40,46]
}
df = pd.DataFrame(data)
print(df.loc[[0,1]])

pd.options.display.max_rows = 9999
df = pd.read_csv("data.csv")

print(df)
print(pd.options.display.max_rows)


pd.options.display.max_rows = 9999
#df = pd.read_json("sample4.json")
#print(df.to_string())

data = {
  "people" : [
    {
       "firstName": "Joe",
       "lastName": "Jackson",
       "gender": "male",
       "age": 28,
       "number": "7349282382"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "Emily",
       "lastName": "Jones",
       "gender": "female",
       "age": 24,
       "number": "456754675"
    }
  ]
}
df = pd.DataFrame(data)
print(df)
"""
df = pd.read_csv("data.csv")

print(df.head(10))

df = pd.read_csv("data.csv")

print(df.tail(10))

df = pd.read_csv("data.csv")

print(df.info())