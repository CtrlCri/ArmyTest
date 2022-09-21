
def str_without_space(str):
    new_str = ""
    for c in str:
        if c != " ":
            new_str += c
    return new_str

def str_to_list(str):
    list = []
    for c in str:
        if (c >= '0' and c <= '9'):
            if (c <= '5'):
                list.append(c)
        else: list.append(c)

    return list


if __name__ == "__main__":
    str = input("write a phrase: ")
    str = str_without_space(str)
    listed = str_to_list(str)
    print( listed )