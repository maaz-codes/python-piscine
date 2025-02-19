def all_things_is_obj(object: any) -> int:
  if type(object) is list:
    print(f"List : {type(object)}")
  elif type(object) is tuple:
    print(f"Tuple : {type(object)}")
  elif type(object) is set:
    print(f"Set: {type(object)}")
  elif type(object) is dict:
    print(f"Dict: {type(object)}")
  return (42)