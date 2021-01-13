import tkinter as tk

# window setup
w_width = 1600
w_height = 900

# settings
max_lines = 20

root = tk.Tk()
root.title("Code Monkey")

canvas = tk.Canvas(width=w_width, height=w_height, background='white')
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


def setup_text(x, y, spacing, lines):
    render_lines = []
    for i in range(lines):
        render_line1 = canvas.create_text(x, y + (i * spacing), font=('Courier', 16), anchor=tk.NW)
        render_line2 = canvas.create_text(x, y + (i * spacing), font=('Courier', 16), anchor=tk.NW, fill='red')
        render_lines.append([render_line1, render_line2])
    return render_lines


def next_page():
    batch = next(whole_text)
    for i in range(len(batch)):
        canvas.itemconfig(render_lines[i][0], text=batch[i])
        canvas.update()


class Pointer:
    def __init__(self):
        self.writing_line = ""
        self.line_number = 0

    def add(self, char):
        self.writing_line += char
        self.update_write_line()

    def remove(self):
        self.writing_line = self.writing_line[:-1]
        self.update_write_line()

    def new_line(self):
        if self.line_number > max_lines:
            pass  # todo

        self.line_number += 1
        self.writing_line = ""

    def update_write_line(self):
        canvas.itemconfig(render_lines[self.line_number][1], text=self.writing_line)


def key_down(event):
    if event.keycode == 8:
        pointer.remove()
    elif event.keycode == 13:
        pointer.new_line()
    else:
        pointer.add(event.char)
    # print(event)


if __name__ == '__main__':
    whole_text = read_file("texts/1.txt", max_lines)
    render_lines = setup_text(10, 10, 36, max_lines)
    next_page()
    pointer = Pointer()
    canvas.bind_all('<Key>', key_down)
    tk.mainloop()
