def minion_game(str):
    # your code goes here
    str = str.upper()
    vowels = 'AEIOU'

    combinations = []
    v_score = 0
    c_score = 0

    for i in range(len(str)):
        for j in range(i+1, len(str) + 1):
            combinations.append(str[i:j])
    # print(combinations)

    for v in combinations:
        if v[0] in vowels:
            v_score += 1

    for c in combinations:
        if c[0] not in vowels:
            c_score += 1

    if v_score > c_score:
        print(f"Kevin {v_score}")
    elif v_score == c_score:
        print("Draw")
    else:
        print(f"Stuart {c_score}")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)