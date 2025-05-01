from Turtle import Turtle

def draw_spiral():
    """バッファリング機能を使った描画例：螺旋を描く"""
    t = Turtle()
    
    # バッファサイズを設定（10ステップごとに描画）
    t.set_buffer_size(10)
    
    # 螺旋を描く
    size = 1
    for i in range(100):
        t.forward(size)
        t.right(30)
        size += 0.5
    
    # 最後に残ったバッファをフラッシュして描画を確実に完了
    t.flush()

if __name__ == "__main__":
    draw_spiral()
