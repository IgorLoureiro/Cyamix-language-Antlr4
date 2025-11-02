def write_code_to_c_file(code: str, filename: str):
    with open( "generated/" + filename + '.c', "w") as f:
        f.write(code)
