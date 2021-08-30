def minion_game(string):
    if (len(string) > 0) and (len(string) <= (10**6)):
        
        vowels = ["A","E","I","O","U"]
        length = len(string)
        kevin_score = 0

        for index, letter in enumerate(string):
            if letter in vowels:
                kevin_score  += length - index

        total = int((length/2)*((2*length)+((length-1)*-1)))
        stuart_score = total - kevin_score

        # Find winner
        if stuart_score > kevin_score:
            print("Stuart", stuart_score)
        elif stuart_score == kevin_score:
            print("Draw")
        elif stuart_score < kevin_score:
            print("Kevin", kevin_score)


if __name__ == '__main__':
    s = input()
    minion_game(s)

