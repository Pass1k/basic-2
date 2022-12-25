count = int(input('Количество видеокарт: '))
video_card = []
new_video_card = []

for i in range(1, count + 1):
    video_card.append(int(input(f'{i} Видеокарта: ')))

maximum = max(video_card)

for i in video_card:
    if i != maximum:
        new_video_card.append(i)

#3070 2060 3090 3070 3090

print('Старый список видеокарт:',video_card)
print('Новый список видеокарт:',new_video_card)
