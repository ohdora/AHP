#4.1 Написать программу, "прячущую" заданную строку в
# текстовый или графический контейнер. Предусмотреть
# извлечение текста из контейнера.

from stegano import exifHeader

message = input('Введите ваше секретное послание: \n')

secret = exifHeader.hide("img/urfu.jpg", "img/urfu_secret.jpg",f'{message}')

result = exifHeader.reveal("img/urfu_secret.jpg")
result = result.decode()
print(result)