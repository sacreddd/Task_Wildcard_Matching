def main():
    print("------start------")
    string_to_check = input()
    pattern = list(input())
    list_to_check = list(string_to_check)
    pattern_index = 0
    result = False
    for char in list_to_check:
        if char == pattern[pattern_index] or pattern[pattern_index] == "?":
            result = True
        elif pattern[pattern_index] == "*":
            try:
                if pattern_index == len(pattern) or pattern[pattern_index + 1] == "?" or pattern[pattern_index + 1] == "*":
                    result = True
                else:
                    while pattern[pattern_index + 1] != list_to_check[pattern_index] and pattern_index <= len(list_to_check):
                        list_to_check.pop(pattern_index)
                        result = False
                    if pattern[pattern_index + 1] == list_to_check[pattern_index]:
                        result = True
                        pattern.pop(pattern_index)
            except:
                # result = True
                break
        else:
            result = False
        if result == False or len(pattern) > len(list_to_check) or (pattern_index + 2 > len(pattern) < len(list_to_check)):
            result = False
            break
        # if count + 2 > len(pattern_copy):
        #     break
        pattern_index += 1
    print(result)


if __name__ == '__main__':
    main()
