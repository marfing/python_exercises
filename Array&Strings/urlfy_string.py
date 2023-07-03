
def urlify_string(string1):
    output = ""
    for c in string1:
        if c != " ":
            output += c
        else:
            output += "%20"
    return output

test="prova a prendermi"
print(f"Prova a prendermi diventa: {urlify_string(test)}")