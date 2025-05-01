import ColabTurtle.Turtle as t

# タートルを初期化
t.initializeTurtle()

# バッファサイズを設定（10ステップごとに画面更新）
t.set_buffer_size(10)

# 螺旋を描く
t.penup()
t.goto(t.window_width() // 2, t.window_height() // 2)
t.pendown()

size = 5
for i in range(100):
    t.forward(size)
    t.right(30)
    size += 1
    # バッファサイズで自動的に更新されるので、通常は明示的なフラッシュは不要

# 最後に残っているバッファをフラッシュ
t.flush_buffer()
