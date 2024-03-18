


info = {
    "key" : "value",
    "name" : "mehedi hasan saim",
    "learning" : "coding",
    "age" : 35,
}
info.update({"city" : "Mymensingh"})
#another way to add key and value
new_dict ={"country" : "bangladesh"}
info.update(new_dict)
new_dict ={"language" : "bangla", "year" : "2024"}
info.update(new_dict)
print(info)