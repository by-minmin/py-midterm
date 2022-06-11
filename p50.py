alls = set(['John','Tina','Mary','Fiona','Chaire','Eva','Ben','Bill','Bert'])
ea = set(['John','Mary','Fiona','Chaire','Ben','Bill'])
ma = set(['Mary','Fiona','Chaire','Eva','Ben'])

print("英文及數學都及格 : ",ma & ea)
print("數學不及格 : ", alls - ma)
print("英文及格數學不及格 : ", ea - ma)