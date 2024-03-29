SUPPORTED_SYM = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
       , 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
       , '~', '`', '!', '@', '#', '$', '%', '^', '&', '-', '_', '—', '=', '|', ':', ';', '\'', '\"', '<', '>', '/', '.', ',', '#']
MAX_QUERY_LENGTH = 50
# Функция для удаления неподдерживаемых символов из строки, а также замена английских символов в строке на русские
def clean_q(string):
    for i in string:
        if not i.lower() in SUPPORTED_SYM:
            string = string.replace(i, '')
    return string