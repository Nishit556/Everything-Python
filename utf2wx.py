from wxconv import WXC
import ast

con = WXC(order='utf2wx')

file = open("dictionary_string.txt", encoding="utf8")

contents = file.read()
dictionary = ast.literal_eval(contents)

file.close()

Dict={}

if __name__ == '__main__':
    for key in dictionary:
        Dict[key]=con.convert(key)
    # print(Dict)
    utf2wx = open('utf_wx.txt', 'w',encoding='utf-8')
    utf2wx.write(str(Dict))
    utf2wx.close()