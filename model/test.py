import re

# s = '19980101-01-001-004/m  １２月/t  ３１日/t  ，/w  中共中央/nt  总书记/n  、/w  国家/n  主席/n  江/nr  泽民/nr  发表/v  １９９８年/t  新年/t  讲话/n  《/w  迈向/v  充满/v  希望/n  的/u  新/a  世纪/n  》/w  。/w  （/w  新华社/nt  记者/n  兰/nr  红光/nr  摄/Vg  ）/w  '
#
# p_name = '\w+/nr(\s{2}\w+/nr)?'
#
# r = re.finditer(p_name, s)
#
# for t in r:
#     print(t.group().replace('/nr', '').replace(' ', ''))
#
# print(re.search(p_name, s))


# for i in range(5):
#     print(i)
#     if i == 3:
#         break
# else:
#     print('-' * 20)

p_n = '\]\w+'

s = 'sdasdasdsad]sd asdsad]er  122'
print(s)
print(re.sub(p_n, '', s))
