input_file = 'test.txt'
with open(input_file,"r",encoding="utf-8") as f:
    text = f.read()
    so_tu = len(text.split())
    so_dong = len(text.splitlines())
    so_ki_tu = len(text)
    print(f'ten file: {input_file}')
    print(so_tu)
    print(so_dong)
    print(so_ki_tu)

    