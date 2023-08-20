from libqtile.config import Group

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
# group_labels = ["", "", "", "", "", "", "", "", "", "",]
# group_labels = ["www", "code", "term", "sys", "doc", "vid", "mus", "files", "chat", "git",]
#group_labels awesome
# group_labels = ["", "", "", "", "", "", "", "", "", "",]
#circles
group_labels = ["", "", "", "", "", "", "", "", "", "",]
#squares
# group_labels = ["󰝤", "󰝤", "󰝤", "󰝤", "󰝤", "󰝤", "󰝤", "󰝤", "󰝤", "󰝤",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        ))