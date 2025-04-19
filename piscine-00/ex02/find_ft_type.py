def all_thing_is_obj(object: any) -> int:
  type_name = type(object).__name__.capitalize()
  if isinstance(object, str):
    print(f"{object} is in the kitchen : {type(object)}")
  elif type_name in ["List", "Tuple", "Set", "Dict"]:
    print(f"{type_name} : {type(object)}")
  return (42)