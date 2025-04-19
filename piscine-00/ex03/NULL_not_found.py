def NULL_not_found(object: any) -> int:
  var_name = ""
  for name, value in globals().items():
    if object is value:
      var_name = name
  if var_name == "":
    print("Type not Found")
    return 1
  else:
    print(f"{var_name}: {object} {type(object)}")
    return 0