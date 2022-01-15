message = input(">")
words = message.split(' ')
emojis = {
    "Facist": "Modi Ji",
    "Good Leader": "Arvind Kejriwal",
    "Commie": "Kanhaiya Bhaiya",
    "Mousollini": "Soniya Gandhi"
}
output = ""
for i in words:
    output +=  emojis.get(i, i) + " "
print(output)

