def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)

        comment = f'""" Этот файл  {line_count} строк кода. """\n'

        return line_count, comment


file_path = 'example.py'
line_count, comment = count_lines(file_path)
print(f'Количество строк: {line_count}')
print(comment)