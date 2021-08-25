import textwrap

def wrap(string, max_width):
    if len(string) > 0 and len(string) < 100:
        if max_width > 0 and max_width < len(string):
            string_list = []
            for i in range(0,len(string), max_width):
                string_list.append(string[i:i+max_width])
            result = "\n".join(string_list)
            return result   

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)