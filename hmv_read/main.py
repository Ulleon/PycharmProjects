def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            cook_book[dish_name] = []
            ingredient_count = int(file.readline().strip())

            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip().split(' | ')
                ingredient_name = ingredient_line[0]
                quantity = int(ingredient_line[1])
                measure = ingredient_line[2]

                ingredient_info = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                cook_book[dish_name].append(ingredient_info)
    return cook_book


file_name = 'recipes.txt'
cook_book = read_recipes(file_name)
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count, cook_book=cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)

def merge_files(file_names, output_file):
    lines_count = []
    content = []

    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines_count.append(len(lines))
            content.append(lines)

    sorted_files = [f for _, f in sorted(zip(lines_count, file_names))]

    with open(output_file, 'w', encoding='utf-8') as result_file:
        for file_name in sorted_files:
            lines = content[file_names.index(file_name)]
            result_file.write(file_name + '\n')
            result_file.write(str(len(lines)) + '\n')
            result_file.writelines(lines)
            result_file.write('\n')


# Пример использования
file_names = ['file1.txt', 'file2.txt']
output_file = 'output.txt'
merge_files(file_names, output_file)
