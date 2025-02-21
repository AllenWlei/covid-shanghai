import re
# -*- coding: utf-8 -*-

# Read start_date.txt to end_date-1.txt
dateArr = range(20220306, 20220311)
addCount = 0
addArr = []

# Fix wrong plot locations by replacing the keyword
fixDict = {
    '浦东新区竹园小学（长岛校区）': '浦东新区竹园小学（沪东校区）',
    '闵行区知新村': '闵行区浦江镇知新村',
    '闵行区普联路150弄': '闵行区浦连路150弄',
    '浦东新区南码头东三街35弄': '浦东新区南码头路街道东三街35弄',
    '青浦区崧润路德康雅苑': '青浦区崧润路49弄德康雅苑',
    '虹口区广灵二路商业二村': '虹口区商业二村',
    '徐汇区田林4村': '徐汇区田林四村',
}

# Parse addresses from txt
for date in dateArr:
    path = str(date) + '.txt'

    fr = open(path, 'r', encoding='UTF-8')
    data = fr.read()
    passage = data.split('\n')

    for line in passage:
        matchArr = re.findall(r'于(.*?)[。，]', line, re.M)
        for addStr in matchArr:
            addCount += 1
            # Correct wrong address and typo
            if addStr in fixDict:
                addStr = fixDict[addStr]
            print('<li>' + str(addCount) + '. ' + addStr + '</li>')
            if addStr not in addArr:
                addArr.append(addStr)

# Update demo.html with new address array
with open('demo.html', 'r+', encoding='utf-8') as f:
    lines = []
    for line in f.readlines():
        startIndex = line.find('var adds = ')
        if startIndex >= 0:
            # print(line)
            lines.append(' '* startIndex + 'var adds = ' + str(addArr) + '\n')
        else:
            lines.append(line)
    f.close()

with open('demo.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    f.close()

print(addArr)
print("共处理" + str(addCount) + "条地址；去重后共计" + str(len(addArr)) + "个地点。")
