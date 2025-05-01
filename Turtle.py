class Turtle:
    def __init__(self):
        # ...existing code...
        self._buffer = []
        self._buffer_size = 1  # デフォルトは毎回描画（1ステップごと）
        self._buffer_count = 0
        # ...existing code...
    
    def set_buffer_size(self, steps):
        """バッファサイズを設定する。steps回の描画コマンドごとに画面を更新する。
        
        Args:
            steps: 画面更新の間隔（ステップ数）
        """
        if steps < 1:
            steps = 1
        self._buffer_size = steps
        
    def _add_to_buffer(self, command):
        """描画コマンドをバッファに追加し、必要に応じて描画を実行する。
        
        Args:
            command: SVG形式の描画コマンド
        """
        self._buffer.append(command)
        self._buffer_count += 1
        
        if self._buffer_count >= self._buffer_size:
            self._flush_buffer()
    
    def _flush_buffer(self):
        """バッファに蓄積されたコマンドをすべて描画する。"""
        if not self._buffer:
            return
            
        # バッファ内のすべてのコマンドを結合して描画
        combined_commands = "".join(self._buffer)
        # 既存の描画メソッドを使って実際に描画する
        self._display_svg(combined_commands)
        
        # バッファとカウンターをリセット
        self._buffer = []
        self._buffer_count = 0
    
    def flush(self):
        """バッファを強制的にフラッシュして描画を更新する。"""
        self._flush_buffer()
    
    # 以下の既存の描画メソッドをバッファリング対応に修正
    
    def forward(self, distance):
        # ...existing code...
        # 描画コマンドの生成部分
        command = self._create_forward_command(distance)  # 仮想的なメソッド名
        self._add_to_buffer(command)  # 直接描画ではなくバッファに追加
        # ...existing code...
    
    def right(self, angle):
        # ...existing code...
        command = self._create_right_command(angle)  # 仮想的なメソッド名
        self._add_to_buffer(command)
        # ...existing code...
    
    # その他の描画関連メソッドも同様に修正
    # ...existing code...