import tkinter

# window setup
w_width = 800
w_height = 480

root = tkinter.Tk()
root.title("Code Monkey")

canvas = tkinter.Canvas(width=w_width, height=w_height, background='white')
canvas.pack()


def read_file(file_name, read_size):
    rows = []
    row_count = 0

    for row in open(file_name, "r"):
        row_count += 1
        rows.append([row_count, row.strip()])

    current_batch = []
    for row in rows:
        current_batch.append(row)
        if row[0] % read_size == 0 and row[0] != 0:
            yield current_batch
            current_batch = []

    if len(current_batch) > 0:
        yield current_batch


if __name__ == '__main__':
    print("main!")

    gen = read_file("texts/1.txt", 3)

    for batch in gen:
        print(batch)

    # tkinter.mainloop()
