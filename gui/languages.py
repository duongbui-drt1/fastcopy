"""
FastCopy v1.6 - Complete Language Translations
Deep translation for all features
Supports: English, Vietnamese, Japanese, Chinese
"""

LANGUAGES = {
    "vi": {
        "name": "Tiếng Việt",
        
        # Header
        "app_title": "⚡ FastCopy",
        "subtitle": "Copy nhanh với Robocopy | Đa luồng",
        
        # Tabs
        "copy_tab": "📋 Copy File",
        "disk_tab": "💾 Ổ Cứng",
        "settings_tab": "⚙️ Cài đặt",
        "help_tab": "❓ Hướng dẫn",
        
        # Path section
        "source": "Nguồn:",
        "dest": "Đích:",
        "select": "Chọn",
        "folder": "📁 Thư mục",
        "files": "📄 File(s)",
        "source_disk": "💾 Nguồn:",
        "dest_disk": "💾 Đích:",
        
        # Options
        "mode": "Chế độ:",
        "mode_copy": "Copy",
        "mode_mirror": "Mirror (Đồng bộ)",
        "mode_move": "Move (Di chuyển)",
        "threads": "Luồng:",
        "buffer": "Buffer:",
        "empty_dirs": "Thư mục trống",
        "parent_dir": "Thư mục mẹ",
        "retry": "Thử lại khi lỗi",
        "keep_attr": "Giữ thuộc tính",
        "default_btn": "🔄 Mặc định",
        
        # Status
        "ready": "⏸️ Sẵn sàng",
        "copying": "▶️ Đang copy...",
        "done": "✅ Hoàn thành!",
        "error": "❌ Lỗi!",
        "stopped": "⏹️ Đã dừng",
        "preparing": "Đang chuẩn bị...",
        "calculating": "Đang tính toán...",
        "elapsed": "Đã chạy",
        "remaining": "Còn lại",
        "speed": "Tốc độ",
        "files_copied": "Files",
        "size_copied": "Đã copy",
        "total_size": "Tổng",
        "errors": "Lỗi",
        
        # Buttons
        "clear_log": "🗑️ Xóa Log",
        "info": "🔍 Kiểm tra",
        "stop": "⏹️ Dừng",
        "start": "🚀 Bắt đầu Copy",
        
        # Warnings
        "warn_high_threads": "⚠️ Số luồng cao (>{}) có thể gây quá tải CPU! Cân nhắc giảm xuống.",
        "warn_low_threads": "⚠️ Số luồng thấp (<{}) sẽ khiến copy chậm hơn!",
        "warn_high_buffer": "⚠️ Buffer cao (>{} MB) sử dụng nhiều RAM! Cân nhắc giảm xuống.",
        "warn_low_buffer": "⚠️ Buffer thấp (<{} MB) sẽ khiến copy chậm hơn!",
        "warn_no_space": "⚠️ Không đủ dung lượng! Cần: {} | Còn: {}",
        "warn_low_space": "⚠️ Sau khi copy sẽ còn ít dung lượng trống ({:.1f}%)",
        
        # Dialogs
        "confirm_stop": "Bạn có chắc muốn dừng quá trình copy?",
        "confirm_stop_title": "Xác nhận dừng",
        "error_no_source": "Vui lòng chọn thư mục hoặc file nguồn!",
        "error_no_dest": "Vui lòng chọn thư mục đích!",
        "error_source_not_found": "Thư mục nguồn không tồn tại!",
        "error_title": "Lỗi",
        "info_title": "Thông tin hệ thống",
        "done_in": "Hoàn thành trong {}",
        
        # Disk tab
        "disk_info": "📊 Thông tin ổ cứng",
        "drive": "Ổ",
        "type": "Loại",
        "model": "Model",
        "filesystem": "FS",
        "total": "Tổng",
        "used": "Đã dùng",
        "free": "Còn trống",
        "percent": "% Dùng",
        "refresh": "🔄 Làm mới",
        "local": "Cục bộ",
        
        # Settings tab
        "settings_title": "⚙️ Cài đặt ứng dụng",
        "language": "Ngôn ngữ:",
        "theme": "Giao diện:",
        "light": "☀️ Sáng (Light)",
        "dark": "🌙 Tối (Dark)",
        "sys_info": "💻 Thông tin hệ thống",
        "cpu": "CPU",
        "ram": "RAM",
        "os": "Hệ điều hành",
        "optimization": "💡 Gợi ý tối ưu hóa",
        "opt_tips": """📌 Các mẹo tối ưu hóa tốc độ copy:

1️⃣ Số Luồng (Threads):
   • Mặc định: 8 luồng - phù hợp với hầu hết trường hợp
   • SSD/NVMe: Có thể tăng lên 16-32 luồng cho tốc độ nhanh hơn
   • HDD: Nên giữ 4-8 luồng để tránh đầu đọc phải di chuyển nhiều
   • Copy qua mạng LAN: 4-8 luồng là tối ưu

2️⃣ Kích thước Buffer:
   • Mặc định: 8 MB - cân bằng giữa tốc độ và RAM
   • File lớn (video, ISO): Tăng lên 32-64 MB
   • File nhỏ: 1-4 MB là đủ
   • Ổ cứng chậm hoặc mạng: 256 KB - 1 MB

3️⃣ Copy thư mục mẹ:
   • Bật: Tạo thư mục nguồn trong thư mục đích
   • Tắt: Copy trực tiếp nội dung vào thư mục đích

4️⃣ Các loại file:
   • File nhỏ nhiều: Tăng số luồng, giảm buffer
   • File lớn ít: Giảm luồng, tăng buffer

5️⃣ So sánh với Windows Explorer:
   • FastCopy nhanh hơn 2-5x nhờ đa luồng
   • Ổn định hơn nhờ cơ chế thử lại tự động
   • Giữ được timestamp và thuộc tính file
""",
        
        # Help tab
        "help_title": "📖 Hướng Dẫn Sử Dụng",
        "help_content": """🚀 HƯỚNG DẪN SỬ DỤNG FASTCOPY

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 BƯỚC 1: Chọn nguồn
• Nhấn "Chọn" ở dòng Nguồn
• Chọn thư mục hoặc file cần copy
• Có thể chọn nhiều file cùng lúc (chế độ File(s))

📌 BƯỚC 2: Chọn đích
• Nhấn "Chọn" ở dòng Đích
• Chọn thư mục nơi bạn muốn copy đến

📌 BƯỚC 3: Điều chỉnh tùy chọn
• Chế độ:
  - Copy: Sao chép file (giữ nguyên nguồn)
  - Mirror: Đồng bộ hoàn toàn (xóa file thừa ở đích)
  - Move: Di chuyển file (xóa nguồn sau khi copy)
• Luồng: Số công việc song song (khuyến nghị 8-16)
• Buffer: Bộ nhớ đệm cho mỗi file

📌 BƯỚC 4: Bắt đầu copy
• Nhấn nút "🚀 Bắt đầu Copy"
• Theo dõi tiến trình trên thanh progress
• Có thể dừng bất cứ lúc nào bằng nút "⏹️ Dừng"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 MẸO SỬ DỤNG:

• Xem thông tin ổ cứng ở tab "💾 Ổ Cứng"
• Điều chỉnh ngôn ngữ và theme ở tab "⚙️ Cài đặt"
• Kiểm tra hệ thống bằng nút "🔍 Kiểm tra"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ LƯU Ý QUAN TRỌNG:

• Chế độ Mirror sẽ XÓA các file ở đích không có ở nguồn
• Luôn backup dữ liệu quan trọng trước khi sử dụng
• Đảm bảo đủ dung lượng trống ở ổ đích
""",
        "terms_title": "📜 Điều Khoản Sử Dụng",
        "terms_content": """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           FASTCOPY v1.6
      Phần mềm copy file nhanh
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 GIẤY PHÉP:
• Đây là phần mềm miễn phí (Freeware)
• Được phép sử dụng cho mục đích cá nhân và thương mại
• Không được bán lại hoặc phân phối lại dưới tên khác

⚙️ CÔNG NGHỆ:
• Sử dụng Robocopy của Windows làm backend
• Giao diện được xây dựng bằng CustomTkinter
• Hỗ trợ đa ngôn ngữ: Tiếng Việt, English, 日本語, 中文

⚠️ MIỄN TRỪ TRÁCH NHIỆM:
• Phần mềm được cung cấp "nguyên trạng" (as-is)
• Không đảm bảo về tính chính xác hoặc phù hợp
• Người dùng tự chịu trách nhiệm về dữ liệu của mình
• Luôn backup dữ liệu quan trọng trước khi sử dụng

📧 LIÊN HỆ:
• Báo lỗi và góp ý: Liên hệ developer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      © 2024 - Dev With ❤️ by Juong
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""",
        
        # Footer
        "footer": "Dev With ❤️ by Juong",
        
        # Log messages
        "log_start": "Bắt đầu: {} → {}",
        "log_info": "Luồng: {} | Tổng: {} | {} file(s)",
        "log_done": "Hoàn thành trong {}",
        "log_stopping": "Đang dừng...",
        "log_error": "LỖI: {}",
    },
    
    "en": {
        "name": "English",
        
        # Header
        "app_title": "⚡ FastCopy",
        "subtitle": "Fast copying with Robocopy | Multi-threaded",
        
        # Tabs
        "copy_tab": "📋 Copy Files",
        "disk_tab": "💾 Disks",
        "settings_tab": "⚙️ Settings",
        "help_tab": "❓ Help",
        
        # Path section
        "source": "Source:",
        "dest": "Destination:",
        "select": "Browse",
        "folder": "📁 Folder",
        "files": "📄 File(s)",
        "source_disk": "💾 Source:",
        "dest_disk": "💾 Dest:",
        
        # Options
        "mode": "Mode:",
        "mode_copy": "Copy",
        "mode_mirror": "Mirror (Sync)",
        "mode_move": "Move",
        "threads": "Threads:",
        "buffer": "Buffer:",
        "empty_dirs": "Empty folders",
        "parent_dir": "Parent folder",
        "retry": "Retry on error",
        "keep_attr": "Keep attributes",
        "default_btn": "🔄 Default",
        
        # Status
        "ready": "⏸️ Ready",
        "copying": "▶️ Copying...",
        "done": "✅ Done!",
        "error": "❌ Error!",
        "stopped": "⏹️ Stopped",
        "preparing": "Preparing...",
        "calculating": "Calculating...",
        "elapsed": "Elapsed",
        "remaining": "Remaining",
        "speed": "Speed",
        "files_copied": "Files",
        "size_copied": "Copied",
        "total_size": "Total",
        "errors": "Errors",
        
        # Buttons
        "clear_log": "🗑️ Clear Log",
        "info": "🔍 Check",
        "stop": "⏹️ Stop",
        "start": "🚀 Start Copy",
        
        # Warnings
        "warn_high_threads": "⚠️ High threads (>{}) may overload CPU! Consider reducing.",
        "warn_low_threads": "⚠️ Low threads (<{}) will slow down copying!",
        "warn_high_buffer": "⚠️ High buffer (>{} MB) uses more RAM! Consider reducing.",
        "warn_low_buffer": "⚠️ Low buffer (<{} MB) will slow down copying!",
        "warn_no_space": "⚠️ Not enough space! Need: {} | Free: {}",
        "warn_low_space": "⚠️ After copy only {:.1f}% will be free",
        
        # Dialogs
        "confirm_stop": "Are you sure you want to stop the copy process?",
        "confirm_stop_title": "Confirm Stop",
        "error_no_source": "Please select source folder or file(s)!",
        "error_no_dest": "Please select destination folder!",
        "error_source_not_found": "Source folder does not exist!",
        "error_title": "Error",
        "info_title": "System Information",
        "done_in": "Completed in {}",
        
        # Disk tab
        "disk_info": "📊 Disk Information",
        "drive": "Drive",
        "type": "Type",
        "model": "Model",
        "filesystem": "FS",
        "total": "Total",
        "used": "Used",
        "free": "Free",
        "percent": "% Used",
        "refresh": "🔄 Refresh",
        "local": "Local",
        
        # Settings tab
        "settings_title": "⚙️ Application Settings",
        "language": "Language:",
        "theme": "Theme:",
        "light": "☀️ Light",
        "dark": "🌙 Dark",
        "sys_info": "💻 System Information",
        "cpu": "CPU",
        "ram": "RAM",
        "os": "OS",
        "optimization": "💡 Optimization Tips",
        "opt_tips": """📌 Tips for optimizing copy speed:

1️⃣ Threads:
   • Default: 8 threads - suitable for most cases
   • SSD/NVMe: Can increase to 16-32 for faster speed
   • HDD: Keep at 4-8 to avoid excessive head movement
   • LAN copy: 4-8 threads is optimal

2️⃣ Buffer Size:
   • Default: 8 MB - balance between speed and RAM
   • Large files (video, ISO): Increase to 32-64 MB
   • Small files: 1-4 MB is enough
   • Slow drive or network: 256 KB - 1 MB

3️⃣ Copy parent folder:
   • On: Creates the source folder in destination
   • Off: Copies contents directly to destination

4️⃣ File types:
   • Many small files: Increase threads, reduce buffer
   • Few large files: Reduce threads, increase buffer

5️⃣ Compared to Windows Explorer:
   • FastCopy is 2-5x faster due to multi-threading
   • More stable with automatic retry mechanism
   • Preserves timestamps and file attributes
""",
        
        # Help tab
        "help_title": "📖 User Guide",
        "help_content": """🚀 FASTCOPY USER GUIDE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 STEP 1: Select Source
• Click "Browse" on the Source line
• Choose folder or files to copy
• Can select multiple files (File(s) mode)

📌 STEP 2: Select Destination
• Click "Browse" on the Destination line
• Choose the folder where you want to copy to

📌 STEP 3: Adjust Options
• Mode:
  - Copy: Copy files (keeps source intact)
  - Mirror: Full sync (deletes extra files at dest)
  - Move: Move files (deletes source after copy)
• Threads: Parallel operations (recommended 8-16)
• Buffer: Memory buffer per file

📌 STEP 4: Start Copying
• Click "🚀 Start Copy" button
• Monitor progress on the progress bar
• Can stop anytime with "⏹️ Stop" button

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 TIPS:

• View disk info in "💾 Disks" tab
• Adjust language and theme in "⚙️ Settings" tab
• Check system with "🔍 Check" button

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ IMPORTANT NOTES:

• Mirror mode will DELETE files at destination not in source
• Always backup important data before using
• Ensure enough free space on destination drive
""",
        "terms_title": "📜 Terms of Use",
        "terms_content": """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           FASTCOPY v1.6
        Fast File Copy Software
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 LICENSE:
• This is freeware software
• May be used for personal and commercial purposes
• May not be resold or redistributed under a different name

⚙️ TECHNOLOGY:
• Uses Windows Robocopy as backend
• Interface built with CustomTkinter
• Multi-language: Vietnamese, English, 日本語, 中文

⚠️ DISCLAIMER:
• Software is provided "as-is"
• No warranty of accuracy or fitness
• Users are responsible for their own data
• Always backup important data before use

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      © 2024 - Dev With ❤️ by Juong
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""",
        
        # Footer
        "footer": "Dev With ❤️ by Juong",
        
        # Log messages
        "log_start": "Start: {} → {}",
        "log_info": "Threads: {} | Total: {} | {} file(s)",
        "log_done": "Completed in {}",
        "log_stopping": "Stopping...",
        "log_error": "ERROR: {}",
    },
    
    "ja": {
        "name": "日本語",
        
        # Header
        "app_title": "⚡ FastCopy",
        "subtitle": "Robocopyで高速コピー | マルチスレッド",
        
        # Tabs
        "copy_tab": "📋 コピー",
        "disk_tab": "💾 ディスク",
        "settings_tab": "⚙️ 設定",
        "help_tab": "❓ ヘルプ",
        
        # Path section
        "source": "ソース:",
        "dest": "宛先:",
        "select": "選択",
        "folder": "📁 フォルダ",
        "files": "📄 ファイル",
        "source_disk": "💾 ソース:",
        "dest_disk": "💾 宛先:",
        
        # Options
        "mode": "モード:",
        "mode_copy": "コピー",
        "mode_mirror": "ミラー (同期)",
        "mode_move": "移動",
        "threads": "スレッド:",
        "buffer": "バッファ:",
        "empty_dirs": "空フォルダ",
        "parent_dir": "親フォルダ",
        "retry": "エラー時再試行",
        "keep_attr": "属性を保持",
        "default_btn": "🔄 デフォルト",
        
        # Status
        "ready": "⏸️ 準備完了",
        "copying": "▶️ コピー中...",
        "done": "✅ 完了!",
        "error": "❌ エラー!",
        "stopped": "⏹️ 停止済み",
        "preparing": "準備中...",
        "calculating": "計算中...",
        "elapsed": "経過時間",
        "remaining": "残り時間",
        "speed": "速度",
        "files_copied": "ファイル",
        "size_copied": "コピー済み",
        "total_size": "合計",
        "errors": "エラー",
        
        # Buttons
        "clear_log": "🗑️ ログ消去",
        "info": "🔍 確認",
        "stop": "⏹️ 停止",
        "start": "🚀 コピー開始",
        
        # Warnings
        "warn_high_threads": "⚠️ スレッド数が多い (>{}) とCPU負荷が高まります！減らすことを検討してください。",
        "warn_low_threads": "⚠️ スレッド数が少ない (<{}) とコピーが遅くなります！",
        "warn_high_buffer": "⚠️ バッファが大きい (>{} MB) とRAM使用量が増えます！減らすことを検討してください。",
        "warn_low_buffer": "⚠️ バッファが小さい (<{} MB) とコピーが遅くなります！",
        "warn_no_space": "⚠️ 容量不足！必要: {} | 空き: {}",
        "warn_low_space": "⚠️ コピー後、空き容量が少なくなります ({:.1f}%)",
        
        # Dialogs
        "confirm_stop": "コピー処理を停止してもよろしいですか？",
        "confirm_stop_title": "停止の確認",
        "error_no_source": "ソースフォルダまたはファイルを選択してください！",
        "error_no_dest": "宛先フォルダを選択してください！",
        "error_source_not_found": "ソースフォルダが存在しません！",
        "error_title": "エラー",
        "info_title": "システム情報",
        "done_in": "{}で完了",
        
        # Disk tab
        "disk_info": "📊 ディスク情報",
        "drive": "ドライブ",
        "type": "種類",
        "model": "モデル",
        "filesystem": "FS",
        "total": "容量",
        "used": "使用済み",
        "free": "空き",
        "percent": "% 使用",
        "refresh": "🔄 更新",
        "local": "ローカル",
        
        # Settings tab
        "settings_title": "⚙️ アプリ設定",
        "language": "言語:",
        "theme": "テーマ:",
        "light": "☀️ ライト",
        "dark": "🌙 ダーク",
        "sys_info": "💻 システム情報",
        "cpu": "CPU",
        "ram": "RAM",
        "os": "OS",
        "optimization": "💡 最適化のヒント",
        "opt_tips": """📌 コピー速度を最適化するヒント：

1️⃣ スレッド数：
   • デフォルト: 8スレッド - ほとんどの場合に適切
   • SSD/NVMe: 16-32まで増やすと高速化
   • HDD: 4-8に抑えてヘッドの動きを減らす
   • LANコピー: 4-8スレッドが最適

2️⃣ バッファサイズ：
   • デフォルト: 8 MB - 速度とRAMのバランス
   • 大きなファイル: 32-64 MBに増やす
   • 小さなファイル: 1-4 MBで十分
   • 遅いドライブ/ネットワーク: 256 KB - 1 MB

3️⃣ 親フォルダをコピー：
   • オン: ソースフォルダを宛先に作成
   • オフ: 内容を直接宛先にコピー

4️⃣ Windows Explorerとの比較：
   • FastCopyはマルチスレッドで2-5倍高速
   • 自動再試行で安定
   • タイムスタンプと属性を保持
""",
        
        # Help tab
        "help_title": "📖 使用ガイド",
        "help_content": """🚀 FASTCOPYユーザーガイド

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 ステップ1: ソースを選択
• ソース行の「選択」をクリック
• コピーするフォルダまたはファイルを選択
• 複数ファイルを選択可能（ファイルモード）

📌 ステップ2: 宛先を選択
• 宛先行の「選択」をクリック
• コピー先のフォルダを選択

📌 ステップ3: オプションを調整
• モード:
  - コピー: ファイルをコピー（ソースは保持）
  - ミラー: 完全同期（宛先の余分なファイルを削除）
  - 移動: ファイルを移動（コピー後ソースを削除）
• スレッド: 並列操作数（推奨8-16）
• バッファ: ファイルごとのメモリバッファ

📌 ステップ4: コピー開始
• 「🚀 コピー開始」ボタンをクリック
• プログレスバーで進捗を確認
• 「⏹️ 停止」でいつでも停止可能

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ 重要な注意事項：
• ミラーモードは宛先のファイルを削除します
• 使用前に重要なデータをバックアップしてください
""",
        "terms_title": "📜 利用規約",
        "terms_content": """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           FASTCOPY v1.6
       高速ファイルコピーソフト
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ライセンス：
• これはフリーウェアです
• 個人・商用目的で使用可能
• 再販売や別名での再配布は禁止

⚙️ 技術：
• Windows Robocopyをバックエンドとして使用
• CustomTkinterでインターフェース構築
• 多言語対応

⚠️ 免責事項：
• ソフトウェアは「現状のまま」提供
• 正確性や適合性の保証なし
• ユーザーは自分のデータに責任を持つ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   © 2024 - Dev With ❤️ by Juong
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""",
        
        # Footer
        "footer": "Dev With ❤️ by Juong",
        
        # Log messages
        "log_start": "開始: {} → {}",
        "log_info": "スレッド: {} | 合計: {} | {} ファイル",
        "log_done": "{}で完了",
        "log_stopping": "停止中...",
        "log_error": "エラー: {}",
    },
    
    "zh": {
        "name": "中文",
        
        # Header
        "app_title": "⚡ FastCopy",
        "subtitle": "Robocopy快速复制 | 多线程",
        
        # Tabs
        "copy_tab": "📋 复制文件",
        "disk_tab": "💾 磁盘",
        "settings_tab": "⚙️ 设置",
        "help_tab": "❓ 帮助",
        
        # Path section
        "source": "源:",
        "dest": "目标:",
        "select": "选择",
        "folder": "📁 文件夹",
        "files": "📄 文件",
        "source_disk": "💾 源:",
        "dest_disk": "💾 目标:",
        
        # Options
        "mode": "模式:",
        "mode_copy": "复制",
        "mode_mirror": "镜像 (同步)",
        "mode_move": "移动",
        "threads": "线程:",
        "buffer": "缓冲:",
        "empty_dirs": "空文件夹",
        "parent_dir": "父文件夹",
        "retry": "错误时重试",
        "keep_attr": "保留属性",
        "default_btn": "🔄 默认",
        
        # Status
        "ready": "⏸️ 就绪",
        "copying": "▶️ 复制中...",
        "done": "✅ 完成!",
        "error": "❌ 错误!",
        "stopped": "⏹️ 已停止",
        "preparing": "准备中...",
        "calculating": "计算中...",
        "elapsed": "已用时间",
        "remaining": "剩余时间",
        "speed": "速度",
        "files_copied": "文件",
        "size_copied": "已复制",
        "total_size": "总计",
        "errors": "错误",
        
        # Buttons
        "clear_log": "🗑️ 清除日志",
        "info": "🔍 检查",
        "stop": "⏹️ 停止",
        "start": "🚀 开始复制",
        
        # Warnings
        "warn_high_threads": "⚠️ 线程过多 (>{}) 可能导致CPU过载！请考虑减少。",
        "warn_low_threads": "⚠️ 线程过少 (<{}) 会导致复制变慢！",
        "warn_high_buffer": "⚠️ 缓冲过大 (>{} MB) 会使用更多内存！请考虑减少。",
        "warn_low_buffer": "⚠️ 缓冲过小 (<{} MB) 会导致复制变慢！",
        "warn_no_space": "⚠️ 空间不足！需要: {} | 可用: {}",
        "warn_low_space": "⚠️ 复制后剩余空间将很少 ({:.1f}%)",
        
        # Dialogs
        "confirm_stop": "确定要停止复制过程吗？",
        "confirm_stop_title": "确认停止",
        "error_no_source": "请选择源文件夹或文件！",
        "error_no_dest": "请选择目标文件夹！",
        "error_source_not_found": "源文件夹不存在！",
        "error_title": "错误",
        "info_title": "系统信息",
        "done_in": "在{}内完成",
        
        # Disk tab
        "disk_info": "📊 磁盘信息",
        "drive": "驱动器",
        "type": "类型",
        "model": "型号",
        "filesystem": "FS",
        "total": "总计",
        "used": "已用",
        "free": "可用",
        "percent": "% 使用",
        "refresh": "🔄 刷新",
        "local": "本地",
        
        # Settings tab
        "settings_title": "⚙️ 应用设置",
        "language": "语言:",
        "theme": "主题:",
        "light": "☀️ 浅色",
        "dark": "🌙 深色",
        "sys_info": "💻 系统信息",
        "cpu": "CPU",
        "ram": "内存",
        "os": "操作系统",
        "optimization": "💡 优化建议",
        "opt_tips": """📌 优化复制速度的技巧：

1️⃣ 线程数：
   • 默认: 8线程 - 适合大多数情况
   • SSD/NVMe: 可增加到16-32以获得更快速度
   • HDD: 保持4-8以减少磁头移动
   • 局域网复制: 4-8线程最佳

2️⃣ 缓冲大小：
   • 默认: 8 MB - 速度和内存的平衡
   • 大文件（视频、ISO）: 增加到32-64 MB
   • 小文件: 1-4 MB就够了
   • 慢速驱动器/网络: 256 KB - 1 MB

3️⃣ 复制父文件夹：
   • 开启: 在目标中创建源文件夹
   • 关闭: 直接将内容复制到目标

4️⃣ 与Windows资源管理器比较：
   • FastCopy因多线程快2-5倍
   • 自动重试更稳定
   • 保留时间戳和文件属性
""",
        
        # Help tab
        "help_title": "📖 使用指南",
        "help_content": """🚀 FASTCOPY用户指南

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 步骤1: 选择源
• 点击源行上的"选择"
• 选择要复制的文件夹或文件
• 可以选择多个文件（文件模式）

📌 步骤2: 选择目标
• 点击目标行上的"选择"
• 选择要复制到的文件夹

📌 步骤3: 调整选项
• 模式:
  - 复制: 复制文件（保留源）
  - 镜像: 完全同步（删除目标中多余的文件）
  - 移动: 移动文件（复制后删除源）
• 线程: 并行操作数（建议8-16）
• 缓冲: 每个文件的内存缓冲

📌 步骤4: 开始复制
• 点击"🚀 开始复制"按钮
• 在进度条上监控进度
• 可以随时用"⏹️ 停止"按钮停止

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ 重要注意事项：
• 镜像模式会删除目标中不在源中的文件
• 使用前请务必备份重要数据
• 确保目标驱动器有足够的空间
""",
        "terms_title": "📜 使用条款",
        "terms_content": """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           FASTCOPY v1.6
         快速文件复制软件
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 许可证：
• 这是免费软件
• 可用于个人和商业目的
• 不得以其他名称转售或重新分发

⚙️ 技术：
• 使用Windows Robocopy作为后端
• 使用CustomTkinter构建界面
• 多语言支持

⚠️ 免责声明：
• 软件按"原样"提供
• 不保证准确性或适用性
• 用户对自己的数据负责
• 使用前请务必备份重要数据

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   © 2024 - Dev With ❤️ by Juong
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""",
        
        # Footer
        "footer": "Dev With ❤️ by Juong",
        
        # Log messages
        "log_start": "开始: {} → {}",
        "log_info": "线程: {} | 总计: {} | {} 个文件",
        "log_done": "在{}内完成",
        "log_stopping": "正在停止...",
        "log_error": "错误: {}",
    }
}


def get_text(lang: str, key: str, *args) -> str:
    """Get localized text with optional formatting"""
    text = LANGUAGES.get(lang, LANGUAGES["en"]).get(key, key)
    if args:
        try:
            return text.format(*args)
        except (IndexError, KeyError):
            return text
    return text


def get_available_languages() -> list:
    """Get list of available language names"""
    return [lang_data["name"] for lang_data in LANGUAGES.values()]


def get_lang_code(name: str) -> str:
    """Get language code from display name"""
    for code, data in LANGUAGES.items():
        if data["name"] == name:
            return code
    return "en"
