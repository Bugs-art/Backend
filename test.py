from config import me

print(me)

print(me["first"])

# print full name
print(me["first"] + " " + me["last"])

# modify values
me["first"] = "Frank S."
print(me["first"])


# add new keys
me["preferred_color"] = "Blue"
print(me)



# print the full address
# format: num street, city
address = me["address"]
print["address"]
print(str(address["number"]) + " " + address["street"] + " " + address["city"])
