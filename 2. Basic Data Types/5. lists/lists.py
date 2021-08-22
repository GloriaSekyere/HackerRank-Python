if __name__ == '__main__':
    my_list = []
    N = int(input())
    for line in range(N):
        command = input()

        if command == 'print':
            print(my_list)
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif 'append' in command:
            my_list.append(int(command[7:]))
        elif 'remove' in command:
            if int(command[7:]) in my_list:
                my_list.remove(int(command[7:]))
        elif 'insert' in command:
            my_list.insert(int(command[7]), int(command[9:]))
        elif command == 'reverse':
            my_list.reverse()
