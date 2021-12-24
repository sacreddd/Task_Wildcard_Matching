def main():
    print("------start------")
    string_to_check = input()
    pattern_copy = input()
    list_to_check = list(string_to_check)
    pattern_copy = list(pattern_copy)
    count = 0
    result = False
    for char in list_to_check:
        if char == pattern_copy[count] or pattern_copy[count] == "?":
            result = True
        elif pattern_copy[count] == "*":
            try:
                if count == len(pattern_copy) or pattern_copy[count + 1] == "?":
                    result = True

                else:
                    while pattern_copy[count + 1] != list_to_check[count] and count <= len(list_to_check):
                        list_to_check.pop(count)
                        result = False
                    if pattern_copy[count + 1] == list_to_check[count]:
                        result = True
                        pattern_copy.pop(count)

                        print(list_to_check[count])
            except:
                result = True
                break

        else:
            result = False

        if result == False or len(pattern_copy) > len(list_to_check) or (
                count + 2 > len(pattern_copy) and len(pattern_copy) < len(list_to_check)):
            result = False
            break
        if count + 2 > len(pattern_copy):
            break
        count += 1

        # if char == string_to_check[count] or char == "?":
        #     result = True
        # elif char == "*":
        #     while pattern[count + 1] != string_to_check[count2]:
        #         result = False
        #         count2 += 1
        #     if pattern[count + 1] == string_to_check[count2]:
        #         result = True
        #     count = count2
        # else:
        #     result = False
        # count += 1
        # count2 = count
    print(result)


if __name__ == '__main__':
    main()
