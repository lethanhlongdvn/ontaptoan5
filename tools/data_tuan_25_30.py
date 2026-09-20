# -*- coding: utf-8 -*-
"""
Dữ liệu ngân hàng câu hỏi Tuần 25 đến Tuần 30 (Trạm 25 - 30)
Mỗi trạm chuẩn 48 câu hỏi:
- Vòng 1: 30 câu ghép đôi (10 câu/lượt x 3 lượt)
- Vòng 2: 12 bài điền số thực tế (4 câu/lượt x 3 lượt)
- Vòng 3: 6 câu trắc nghiệm Mức 3 (2 câu/lượt x 3 lượt)
"""

TUAN_25_TO_30 = [
    # =========================================================================
    # TRẠM 25: NINH THUẬN (THÁP PO KLONG GARAI) - TUẦN 25
    # =========================================================================
    {
        "tuan": 25,
        "tram_so": 25,
        "ten_tram": "Ninh Thuận (Tháp Po Klong Garai)",
        "chu_de": "Diện tích hình lập phương, thể tích hình hộp chữ nhật, thể tích hình lập phương",
        "souvenirs": {
            "cap1": "Chùm nho ngọc Ninh Thuận Đồng (50đ)",
            "cap2": "Tượng thần Shiva Po Klong Garai Bạc (90đ)",
            "cap3": "Hạt ngọc Vĩnh Hy Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Công thức tính diện tích xung quanh của hình lập phương cạnh a là gì?", "a": "Sxq = a × a × 4"},
            {"q": "Công thức tính diện tích toàn phần của hình lập phương cạnh a là gì?", "a": "Stp = a × a × 6"},
            {"q": "Công thức tính thể tích của hình hộp chữ nhật có 3 kích thước a, b, c là gì?", "a": "V = a × b × c"},
            {"q": "Công thức tính thể tích của hình lập phương cạnh a là gì?", "a": "V = a × a × a"},
            {"q": "Tính diện tích xung quanh của hình lập phương cạnh 5 cm", "a": "100 cm² (5 × 5 × 4 = 100)"},
            {"q": "Quần thể tháp Chăm Po Klong Garai cổ kính nằm trên ngọn đồi nào tại Ninh Thuận?", "a": "Đồi Trầu (Phan Rang)"},
            {"q": "Loại cây ăn quả đặc sản trứ danh phủ bóng những giàn xanh tại Ninh Thuận là gì?", "a": "Nho Ninh Thuận (Nho Ba Mọi)"},
            {"q": "Vịnh biển tuyệt mỹ được ví như viên ngọc bích hoang sơ ở Ninh Thuận là vịnh nào?", "a": "Vịnh Vĩnh Hy"},
            {"q": "Cánh đồng muối lớn nhất nước ta tại Ninh Thuận có sản lượng hàng trăm nghìn tấn là gì?", "a": "Cánh đồng muối Cà Ná"},
            {"q": "Tính thể tích của hình lập phương có cạnh 2 cm", "a": "8 cm³ (2 × 2 × 2 = 8)"},
            # Lượt 2
            {"q": "Tính diện tích toàn phần của hình lập phương có cạnh 3 dm", "a": "54 dm² (3 × 3 × 6 = 54)"},
            {"q": "Tính thể tích hình hộp chữ nhật có dài 5 cm, rộng 4 cm, cao 3 cm", "a": "60 cm³"},
            {"q": "Một hình lập phương có diện tích một mặt là 16 cm². Tính diện tích toàn phần", "a": "96 cm² (16 × 6 = 96)"},
            {"q": "Một hình lập phương có diện tích xung quanh là 36 cm². Tính diện tích một mặt", "a": "9 cm² (36 : 4 = 9)"},
            {"q": "Nếu gấp cạnh hình lập phương lên 2 lần thì thể tích gấp lên mấy lần?", "a": "8 lần (2 × 2 × 2 = 8)"},
            {"q": "Lễ hội truyền thống lớn nhất trong năm của đồng bào Chăm tại tháp Po Klong Garai là gì?", "a": "Lễ hội Kate"},
            {"q": "Làng gốm cổ truyền Bàu Trúc ở Ninh Thuận được UNESCO công nhận di sản là làm bằng gì?", "a": "Gốm làm thủ công bằng tay (không dùng bàn xoay)"},
            {"q": "Đồi cát vàng mênh mông uốn lượn cạnh TP Phan Rang là đồi cát gì?", "a": "Đồi cát Nam Cương"},
            {"q": "Tính thể tích hình lập phương có cạnh 10 cm theo đơn vị đề-xi-mét khối", "a": "1 dm³ (1 000 cm³ = 1 dm³)"},
            {"q": "Một hình lập phương có diện tích toàn phần 24 cm². Cạnh của nó là bao nhiêu cm?", "a": "2 cm (24 : 6 = 4 = 2 × 2)"},
            # Lượt 3
            {"q": "Tính thể tích hình hộp chữ nhật có diện tích đáy 25 cm² và chiều cao 8 cm", "a": "200 cm³ (25 × 8 = 200)"},
            {"q": "Một hình lập phương có Stp = 150 dm². Tính thể tích của hình lập phương đó", "a": "125 dm³ (cạnh 5 dm)"},
            {"q": "Nếu gấp cạnh hình lập phương lên 3 lần thì diện tích toàn phần tăng mấy lần?", "a": "9 lần (3 × 3 = 9)"},
            {"q": "Tính diện tích một mặt hình lập phương có thể tích 27 cm³", "a": "9 cm² (cạnh 3 cm)"},
            {"q": "Công viên đá Ninh Thuận với vô số tảng đá tự nhiên kỳ thú nằm trong VQG nào?", "a": "Vườn quốc gia Núi Chúa"},
            {"q": "Vườn quốc gia Núi Chúa ở Ninh Thuận được UNESCO công nhận danh hiệu gì năm 2021?", "a": "Khu dự trữ sinh quyển thế giới"},
            {"q": "Món đặc sản bánh giòn rụm nhân tôm mực đổ khuôn đất nung ở Phan Rang là gì?", "a": "Bánh căn Phan Rang"},
            {"q": "Tính diện tích xung quanh của hình lập phương cạnh 1,2 m", "a": "5,76 m²"},
            {"q": "Đổi 0,5 m³ sang lít", "a": "500 lít"},
            {"q": "Một bể cá hình lập phương không có nắp cạnh 40 cm. Diện tích kính làm bể là bao nhiêu?", "a": "8 000 cm² (40 × 40 × 5 = 8 000)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một chiếc thùng gỗ đóng nho Ba Mọi hình lập phương có cạnh 4 dm. Diện tích toàn phần của chiếc thùng gỗ đó là ... dm².", "a": "96"},
            {"q": "Một bể chứa nước tưới giàn nho hình hộp chữ nhật có chiều dài 3 m, chiều rộng 2 m và chiều sâu 1,5 m. Thể tích bể nước là ... m³.", "a": "9"},
            {"q": "Một khối tượng đá thần Shiva nhỏ hình lập phương có thể tích 64 cm³. Độ dài mỗi cạnh của khối tượng là ... cm.", "a": "4"},
            {"q": "Một hộp quà bánh căn hình lập phương có diện tích xung quanh là 144 cm². Cạnh của hộp quà đó là ... cm.", "a": "6"},
            # Lượt 2
            {"q": "Một bình gốm Bàu Trúc hình hộp chữ nhật có kích thước đáy 15 cm và 12 cm, chiều cao 20 cm. Thể tích bình gốm là ... cm³.", "a": "3600"},
            {"q": "Một bồn chứa muối hạt Cà Ná hình lập phương có cạnh dài 1,5 m. Thể tích bồn chứa muối đó là ... m³.", "a": "3,375"},
            {"q": "Người ta dán giấy màu xung quanh một hộp quà lưu niệm tháp Chăm hình lập phương cạnh 10 cm. Diện tích giấy dán xung quanh là ... cm².", "a": "400"},
            {"q": "Một chiếc tàu ngắm san hô Vịnh Vĩnh Hy có đáy kính hình hộp chữ nhật dài 4 m, rộng 2,5 m, chiều cao 0,8 m. Thể tích khoang đáy tàu là ... m³.", "a": "8"},
            # Lượt 3
            {"q": "Người ta sơn toàn bộ 6 mặt của một thùng đựng nho hình lập phương cạnh 0,8 m. Diện tích cần sơn là ... m².", "a": "3,84"},
            {"q": "Một bể nước ngầm hình hộp chữ nhật dài 5 m, rộng 3 m. Khi đổ vào bể 18 m³ nước thì mực nước trong bể sâu ... m.", "a": "1,2"},
            {"q": "Tính thể tích của hình lập phương có diện tích toàn phần bằng 216 cm². Thể tích là ... cm³.", "a": "216"},
            {"q": "Một thùng hàng chứa 120 hộp nho sấy dẻo, mỗi hộp có thể tích 500 cm³. Tổng thể tích của các hộp nho là ... dm³.", "a": "60"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một bể cá cảnh hình hộp chữ nhật có chiều dài 80 cm, chiều rộng 50 cm và mực nước sâu 35 cm. Người ta thả vào bể một khối đá san hô Vĩnh Hy thì thấy mực nước dâng lên cao 40 cm. Tính thể tích của khối đá san hô đó theo đơn vị đề-xi-mét khối.\nA. 20 dm³\nB. 16 dm³\nC. 24 dm³\nD. 18 dm³",
                "ans_str": "A. 20 dm³ (Mực nước dâng thêm: 40 - 35 = 5 cm. Thể tích san hô: 80 × 50 × 5 = 20 000 cm³ = 20 dm³)"
            },
            {
                "q": "Một khối gỗ hình lập phương có cạnh 9 cm. Người ta đem cưa khối gỗ đó thành các khối lập phương nhỏ cạnh 3 cm. Hỏi cưa được tất cả bao nhiêu khối lập phương nhỏ (bỏ qua hao phí khi cưa)?\nA. 27 khối\nB. 9 khối\nC. 18 khối\nD. 36 khối",
                "ans_str": "A. 27 khối (Số khối nhỏ bằng: (9 : 3) × (9 : 3) × (9 : 3) = 3 × 3 × 3 = 27 khối)"
            },
            # Lượt 2
            {
                "q": "Người ta xếp 1 000 khối lập phương nhỏ cạnh 1 cm thành một khối lập phương lớn rồi sơn toàn bộ 6 mặt của khối lập phương lớn. Hỏi có bao nhiêu khối lập phương nhỏ không được sơn mặt nào?\nA. 512 khối\nB. 729 khối\nC. 384 khối\nD. 486 khối",
                "ans_str": "A. 512 khối (Cạnh khối lập phương lớn là 10 cm. Các khối không được sơn mặt nào nằm ở phần lõi bên trong có kích thước: (10 - 2) × (10 - 2) × (10 - 2) = 8 × 8 × 8 = 512 khối)"
            },
            {
                "q": "Một bể bơi mini hình hộp chữ nhật có chiều dài gấp đôi chiều rộng và chiều cao 1,5 m. Biết diện tích xung quanh của bể bơi là 54 m². Tính thể tích của bể bơi đó.\nA. 108 m³\nB. 54 m³\nC. 72 m³\nD. 90 m³",
                "ans_str": "A. 108 m³ (Chu vi đáy của bể bơi là: 54 : 1,5 = 36 (m). Nửa chu vi đáy là: 36 : 2 = 18 (m). Chiều rộng của bể là: 18 : (2 + 1) = 6 (m). Chiều dài của bể là: 6 × 2 = 12 (m). Thể tích của bể bơi là: 12 × 6 × 1,5 = 108 (m³))"
            },
            # Lượt 3
            {
                "q": "Nếu tăng cạnh của một hình lập phương thêm 50% thì thể tích của hình lập phương đó tăng thêm bao nhiêu phần trăm?\nA. 237,5%\nB. 150%\nC. 125%\nD. 225%",
                "ans_str": "A. 237,5% (Cạnh mới bằng 150% = 1,5 cạnh cũ. Thể tích mới bằng: 1,5 × 1,5 × 1,5 = 3,375 = 337,5% thể tích cũ. Thể tích tăng thêm: 337,5% - 100% = 237,5%)"
            },
            {
                "q": "Một cano du lịch trên Vịnh Vĩnh Hy đi xuôi dòng từ bến ra bãi san hô dài 15 km hết 30 phút. Vận tốc dòng nước là 3 km/giờ. Tính vận tốc thực của cano khi nước yên lặng.\nA. 27 km/giờ\nB. 30 km/giờ\nC. 33 km/giờ\nD. 25 km/giờ",
                "ans_str": "A. 27 km/giờ (30 phút = 0,5 giờ. Vận tốc xuôi dòng: 15 : 0,5 = 30 km/giờ. Vận tốc thực của cano: 30 - 3 = 27 km/giờ)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 26: BÌNH THUẬN (ĐỒI CÁT MŨI NÉ, BÀU TRẮNG) - TUẦN 26
    # =========================================================================
    {
        "tuan": 26,
        "tram_so": 26,
        "ten_tram": "Bình Thuận (Đồi cát Mũi Né, Bàu Trắng)",
        "chu_de": "Thực hành ước lượng thể tích, các đơn vị đo thời gian, đổi đơn vị thời gian",
        "souvenirs": {
            "cap1": "Đồng hồ cát Mũi Né Đồng (50đ)",
            "cap2": "Đóa sen Bàu Trắng Bạc (90đ)",
            "cap3": "Ngọn đuốc Kê Gà Hoàng Kim Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "1 thế kỷ bằng bao nhiêu năm?", "a": "100 năm"},
            {"q": "1 năm không nhuận có bao nhiêu ngày?", "a": "365 ngày"},
            {"q": "1 năm nhuận có bao nhiêu ngày?", "a": "366 ngày"},
            {"q": "Năm nhuận tháng Hai có bao nhiêu ngày?", "a": "29 ngày"},
            {"q": "1 ngày có bao nhiêu giờ?", "a": "24 giờ"},
            {"q": "1 giờ bằng bao nhiêu phút?", "a": "60 phút"},
            {"q": "1 phút bằng bao nhiêu giây?", "a": "60 giây"},
            {"q": "Đồi cát bay Mũi Né nổi tiếng với hiện tượng gì thay đổi liên tục theo từng giờ?", "a": "Hình dáng và màu sắc đồi cát (thay đổi theo chiều gió)"},
            {"q": "Hồ nước ngọt tự nhiên tuyệt đẹp mọc đầy hoa sen giữa đồi cát trinh nữ ở Bình Thuận là gì?", "a": "Bàu Trắng (Bàu Sen)"},
            {"q": "Ngọn hải đăng cổ kính bằng đá cao và lâu đời nhất Việt Nam tại Bình Thuận là gì?", "a": "Hải đăng Kê Gà"},
            # Lượt 2
            {"q": "Đổi 2,5 giờ sang phút", "a": "150 phút (2,5 × 60 = 150)"},
            {"q": "Đổi 90 phút sang giờ dưới dạng số thập phân", "a": "1,5 giờ"},
            {"q": "Đổi 3/4 giờ sang phút", "a": "45 phút"},
            {"q": "Đổi 1 phút 15 giây sang giây", "a": "75 giây"},
            {"q": "Tháng nào trong năm luôn có 31 ngày trong các tháng sau: 4; 6; 7; 9?", "a": "Tháng 7"},
            {"q": "Trò chơi cảm giác mạnh trượt từ đỉnh đồi cát dốc xuống Mũi Né gọi là trò gì?", "a": "Trượt cát (bằng ván trượt)"},
            {"q": "Phương tiện mô-tô 4 bánh địa hình vượt đồi cát Bàu Trắng thường gọi là gì?", "a": "Xe mô-tô địa hình (ATV)"},
            {"q": "Món quà đặc sản quả đỏ mọng ngọt thanh bạt ngàn tại Bình Thuận là gì?", "a": "Thanh long Bình Thuận"},
            {"q": "Năm 2024 thuộc thế kỷ thứ mấy?", "a": "Thế kỷ 21"},
            {"q": "Đổi 150 giây sang phút và giây", "a": "2 phút 30 giây"},
            # Lượt 3
            {"q": "Đổi 1/2 ngày sang giờ", "a": "12 giờ"},
            {"q": "Đổi 2 ngày 4 giờ sang giờ", "a": "52 giờ (48 + 4 = 52)"},
            {"q": "Đổi 1,2 phút sang giây", "a": "72 giây"},
            {"q": "Tính: 3 giờ 20 phút + 2 giờ 15 phút", "a": "5 giờ 35 phút"},
            {"q": "Tính: 4 giờ 45 phút - 1 giờ 30 phút", "a": "3 giờ 15 phút"},
            {"q": "Trường Dục Thanh nơi người thanh niên Nguyễn Tất Thành từng dạy học năm 1910 nằm tại TP nào?", "a": "TP Phan Thiết (Bình Thuận)"},
            {"q": "Nước mắm truyền thống nức tiếng hàng trăm năm của Bình Thuận là nước mắm gì?", "a": "Nước mắm Phan Thiết"},
            {"q": "Lâu đài lưu trữ rượu vang châu Âu độc đáo đầu tiên tại Mũi Né là gì?", "a": "Lâu đài Rượu Vang RD"},
            {"q": "Năm 1900 có phải là năm nhuận không?", "a": "Không phải (năm tròn trăm phải chia hết cho 400)"},
            {"q": "Năm 2000 có phải là năm nhuận không?", "a": "Có (chia hết cho 400)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một du khách thuê xe địa hình chạy vòng quanh đồi cát Bàu Trắng xuất phát lúc 8 giờ 15 phút và kết thúc lúc 9 giờ 45 phút. Du khách đã chơi trong ... phút.", "a": "90"},
            {"q": "Một chiếc đồng hồ cát Mũi Né chảy hết cát trong 2 phút 30 giây. Đổi thời gian đó ra giây là ... giây.", "a": "150"},
            {"q": "Một xe tải chở 12 tấn thanh long xuất phát từ Phan Thiết lúc 5 giờ sáng đến TP.HCM lúc 8 giờ 30 phút sáng. Thời gian xe chạy là ... giờ (nhập số thập phân).", "a": "3,5"},
            {"q": "Bác thợ làm nước mắm Phan Thiết: mỗi thùng gỗ ủ chượp cá cơm trong 12 tháng. Đổi 12 tháng sang năm là ... năm.", "a": "1"},
            # Lượt 2
            {"q": "Hải đăng Kê Gà được xây dựng từ năm 1897 và hoàn thành năm 1899. Công trình được xây dựng trong ... năm.", "a": "2"},
            {"q": "Một bạn học sinh tham gia trò trượt cát 6 lượt. Mỗi lượt trượt và leo lên lại hết trung bình 4 phút 15 giây. Tổng thời gian bạn ấy chơi là ... phút ... giây (nhập số phút trước: 25 phút 30 giây -> nhập 25,5 phút).", "a": "25,5"},
            {"q": "Tính giá trị biểu thức: 1,5 giờ × 4 + 45 phút. Kết quả là ... giờ ... phút (hoặc nhập số phút: 6 giờ 45 phút -> 405 phút).", "a": "405"},
            {"q": "Bác Ba hái thanh long: sáng hái được 3 giờ 45 phút, chiều hái được 2 giờ 30 phút. Tổng thời gian bác Ba hái thanh long là ... giờ ... phút (nhập 6 giờ 15 phút hoặc 6,25 giờ).", "a": "6,25"},
            # Lượt 3
            {"q": "Một ca nô du lịch đưa khách từ đất liền ra đảo Kê Gà cách bờ 500 m hết 2 phút 30 giây. Đổi thời gian ca nô chạy sang phút dưới dạng phân số là ... phút (nhập phân số a/b).", "a": "5/2 (hoặc 2,5)"},
            {"q": "Đoàn tàu hỏa Thống Nhất chạy từ ga Mương Mán (Bình Thuận) vào ga Sài Gòn hết 3 giờ 36 phút. Viết thời gian này dưới dạng số thập phân là ... giờ.", "a": "3,6"},
            {"q": "Tìm x, biết: x + 1 giờ 15 phút = 3 giờ. Giá trị của x là ... giờ (nhập số thập phân).", "a": "1,75"},
            {"q": "Một ngày có 24 giờ. 0,25 ngày bằng ... giờ.", "a": "6"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một người đi xe máy từ Phan Thiết đến Mũi Né dài 22 km. Người đó khởi hành lúc 7 giờ 30 phút và đi với vận tốc 40 km/giờ. Dọc đường người đó dừng lại chụp ảnh vườn thanh long hết 15 phút. Hỏi người đó đến Mũi Né lúc mấy giờ?\nA. 8 giờ 18 phút\nB. 8 giờ 15 phút\nC. 8 giờ 20 phút\nD. 8 giờ 30 phút",
                "ans_str": "A. 8 giờ 18 phút (Thời gian đi trên đường: 22 : 40 = 0,55 giờ = 33 phút. Tổng thời gian cả đi và nghỉ: 33 + 15 = 48 phút. Đến Mũi Né lúc: 7 giờ 30 phút + 48 phút = 8 giờ 18 phút)"
            },
            {
                "q": "Một người thợ làm việc từ 7 giờ 30 phút đến 11 giờ 30 phút thì làm được 3 sản phẩm thủ công mỹ nghệ từ vỏ sò ốc. Hỏi người đó làm 5 sản phẩm như thế mất bao nhiêu thời gian (năng suất như nhau)?\nA. 6 giờ 40 phút\nB. 6 giờ 30 phút\nC. 7 giờ\nD. 6 giờ 15 phút",
                "ans_str": "A. 6 giờ 40 phút (Thời gian làm 3 sản phẩm: 11 giờ 30 phút - 7 giờ 30 phút = 4 giờ = 240 phút. Thời gian làm 1 sản phẩm: 240 : 3 = 80 phút. Thời gian làm 5 sản phẩm: 80 × 5 = 400 phút = 6 giờ 40 phút)"
            },
            # Lượt 2
            {
                "q": "Năm 2024 là năm nhuận có ngày 29 tháng 2 là ngày Thứ Năm. Hỏi ngày 29 tháng 2 của năm nhuận tiếp theo (năm 2028) sẽ là ngày Thứ mấy trong tuần?\nA. Thứ Ba\nB. Thứ Tư\nC. Thứ Hai\nD. Thứ Sáu",
                "ans_str": "A. Thứ Ba (Từ 29/2/2024 đến 29/2/2028 có 4 năm, gồm 3 năm thường (365 ngày) và 1 năm nhuận 2028 (366 ngày). Tổng số ngày: 365 × 3 + 366 = 1 461 ngày. Ta có: 1 461 : 7 = 208 tuần dư 5 ngày. Đếm tiếp 5 ngày từ Thứ Năm: Thứ Sáu, Thứ Bảy, Chủ Nhật, Thứ Hai, Thứ Ba. Vậy là ngày Thứ Ba)"
            },
            {
                "q": "Một chiếc đồng hồ quả lắc cứ mỗi giờ chạy nhanh 15 giây. Người ta chỉnh lại đồng hồ cho đúng giờ lúc 6 giờ sáng ngày thứ Hai. Hỏi đến 6 giờ sáng ngày thứ Ba (sau đúng 24 giờ), đồng hồ đó chỉ mấy giờ?\nA. 6 giờ 6 phút sáng\nB. 6 giờ 15 phút sáng\nC. 6 giờ 10 phút sáng\nD. 6 giờ 4 phút sáng",
                "ans_str": "A. 6 giờ 6 phút sáng (Sau 24 giờ, đồng hồ chạy nhanh thêm: 24 × 15 = 360 giây = 6 phút. Vậy đồng hồ chỉ: 6 giờ 6 phút)"
            },
            # Lượt 3
            {
                "q": "Một xe ô tô chở khách du lịch chạy từ TP.HCM ra Mũi Né dài 210 km. Xe khởi hành lúc 6 giờ sáng, đi được 2,5 giờ thì dừng lại nghỉ ăn sáng 30 phút. Sau đó xe đi tiếp với vận tốc 60 km/giờ trong 1,5 giờ nữa thì tới nơi. Tính vận tốc trung bình của xe trong chặng đường đầu.\nA. 48 km/giờ\nB. 50 km/giờ\nC. 52 km/giờ\nD. 45 km/giờ",
                "ans_str": "A. 48 km/giờ (Quãng đường chặng sau xe đi được: 60 × 1,5 = 90 km. Quãng đường chặng đầu: 210 - 90 = 120 km. Vận tốc chặng đầu: 120 : 2,5 = 48 km/giờ)"
            },
            {
                "q": "Hiện nay anh 15 tuổi, em 9 tuổi. Hỏi cách đây mấy năm thì tuổi anh gấp đôi tuổi em?\nA. 3 năm trước\nB. 4 năm trước\nC. 2 năm trước\nD. 5 năm trước",
                "ans_str": "A. 3 năm trước (Anh hơn em: 15 - 9 = 6 tuổi. Hiệu số tuổi không đổi. Khi tuổi anh gấp đôi tuổi em thì tuổi em bằng hiệu số tuổi: 6 tuổi. Số năm cách đây là: 9 - 6 = 3 năm trước)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 27: LÂM ĐỒNG (ĐỈNH LANG BIANG, ĐÀ LẠT) - TUẦN 27 🌟 GK2
    # =========================================================================
    {
        "tuan": 27,
        "tram_so": 27,
        "ten_tram": "Lâm Đồng (Đỉnh Lang Biang, Đà Lạt) 🌟 GK2",
        "chu_de": "Cộng trừ số đo thời gian, nhân chia số đo thời gian với một số, ôn tập Giữa học kỳ 2",
        "souvenirs": {
            "cap1": "Cành hoa bất tử Đà Lạt Đồng (50đ)",
            "cap2": "Chiếc sừng hươu Lang Biang Bạc (90đ)",
            "cap3": "Trái tim ngàn hoa Đà Lạt Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Tính: 2 giờ 35 phút + 1 giờ 40 phút", "a": "4 giờ 15 phút (3 giờ 75 phút = 4 giờ 15 phút)"},
            {"q": "Tính: 5 giờ 20 phút - 2 giờ 45 phút", "a": "2 giờ 35 phút (4 giờ 80 phút - 2 giờ 45 phút)"},
            {"q": "Tính: 1 giờ 15 phút × 3", "a": "3 giờ 45 phút"},
            {"q": "Tính: 8 giờ 40 phút : 4", "a": "2 giờ 10 phút"},
            {"q": "Đỉnh Lang Biang huyền thoại (Đà Lạt) có độ cao bao nhiêu mét so với mực nước biển?", "a": "2 167 m (đỉnh cao nhất Bà)"},
            {"q": "Thành phố Đà Lạt được mệnh danh là thành phố ngàn loài gì?", "a": "Thành phố ngàn hoa"},
            {"q": "Hồ nước thơ mộng nằm ngay trái tim trung tâm thành phố Đà Lạt là hồ gì?", "a": "Hồ Xuân Hương"},
            {"q": "Thung lũng nổi tiếng gắn liền với tình yêu đôi lứa ở Đà Lạt là gì?", "a": "Thung lũng Tình Yêu"},
            {"q": "Tính nhẩm: 45 phút + 45 phút", "a": "1 giờ 30 phút (1,5 giờ)"},
            {"q": "Đổi 3 giờ 12 phút sang phút", "a": "192 phút"},
            # Lượt 2
            {"q": "Tính: 3 ngày 14 giờ + 2 ngày 18 giờ", "a": "6 ngày 8 giờ (5 ngày 32 giờ = 6 ngày 8 giờ)"},
            {"q": "Tính: 6 ngày 5 giờ - 2 ngày 12 giờ", "a": "3 ngày 17 giờ (5 ngày 29 giờ - 2 ngày 12 giờ)"},
            {"q": "Tính: 2 phút 25 giây × 4", "a": "9 phút 40 giây (8 phút 100 giây = 9 phút 40 giây)"},
            {"q": "Tính: 7 phút 30 giây : 3", "a": "2 phút 30 giây"},
            {"q": "Nhà ga xe lửa cổ đẹp nhất Đông Dương với đầu tàu răng cưa độc đáo nằm ở đâu?", "a": "Ga Đà Lạt"},
            {"q": "Đồi chè xanh ngát hàng trăm năm tuổi tại ngoại ô Đà Lạt là đồi chè nào?", "a": "Đồi chè Cầu Đất"},
            {"q": "Thác nước tuyệt đẹp tuôn trào bọt trắng xóa có máng trượt uốn lượn ở Đà Lạt là thác gì?", "a": "Thác Datanla"},
            {"q": "Bác sĩ người Pháp có công tìm ra cao nguyên Lang Biang và thành lập Đà Lạt là ai?", "a": "Bác sĩ Alexandre Yersin"},
            {"q": "Đổi 2,25 giờ sang giờ và phút", "a": "2 giờ 15 phút"},
            {"q": "Tính: 15 giờ 30 phút : 5", "a": "3 giờ 6 phút"},
            # Lượt 3
            {"q": "Tính: 4 giờ 50 phút + 3 giờ 30 phút", "a": "8 giờ 20 phút"},
            {"q": "Tính: 10 giờ - 4 giờ 25 phút", "a": "5 giờ 35 phút"},
            {"q": "Tính: 3 giờ 15 phút × 5", "a": "16 giờ 15 phút"},
            {"q": "Tính: 13 giờ 20 phút : 4", "a": "3 giờ 20 phút"},
            {"q": "Chợ đêm Đà Lạt nổi tiếng với tên gọi dân gian là chợ gì?", "a": "Chợ Âm Phủ"},
            {"q": "Dinh thự mùa hè xa hoa của vị vua cuối cùng triều Nguyễn tại Đà Lạt là gì?", "a": "Dinh Bảo Đại (Dinh III)"},
            {"q": "Loài hoa dại màu tím lãng mạn nở rộ khắp các con dốc Đà Lạt vào mùa xuân là hoa gì?", "a": "Hoa phượng tím"},
            {"q": "Tên đỉnh núi Lang Biang bắt nguồn từ thiên tình sử thiêng liêng của chàng K'Lang và ai?", "a": "Nàng H'Biang"},
            {"q": "Tính nhẩm: 1,5 giờ × 6", "a": "9 giờ"},
            {"q": "Một ngày đêm trên Trái Đất quay được mấy vòng xung quanh trục của nó?", "a": "1 vòng"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Xe jeep chở khách từ chân núi lên đỉnh Radar Lang Biang đi hết 15 phút, dừng lại ngắm cảnh 1 giờ 15 phút và chạy xuống hết 18 phút. Tổng thời gian chuyến đi là ... phút.", "a": "108"},
            {"q": "Người ta đi thuyền đạp vịt quanh Hồ Xuân Hương: vòng 1 đi hết 25 phút 30 giây, vòng 2 đi hết 28 phút 45 giây. Cả hai vòng đi hết ... phút ... giây (nhập số giây: 54 phút 15 giây -> 3 255 giây hoặc nhập 54,25 phút).", "a": "54,25"},
            {"q": "Một người thợ làm mứt dâu tây Đà Lạt: làm 1 mẻ mứt hết 1 giờ 45 phút. Người đó làm 4 mẻ mứt như thế hết ... giờ.", "a": "7"},
            {"q": "Một đoàn tàu cổ chạy từ Ga Đà Lạt xuống Trại Mát dài 7 km đi hết 25 phút. Đi và về 2 lượt (4 chuyến) hết ... phút.", "a": "100"},
            # Lượt 2
            {"q": "Một nghệ nhân cắm hoa Đà Lạt cắm 6 giỏ hoa nghệ thuật hết 2 giờ 30 phút. Trung bình mỗi giỏ hoa cắm hết ... phút.", "a": "25"},
            {"q": "Tàu máng trượt thác Datanla trượt xuống hết 4 phút 20 giây, kéo lên hết 6 phút 40 giây. Đi một vòng trượt hết ... phút.", "a": "11"},
            {"q": "Tìm x, biết: x × 3 = 4 giờ 30 phút. Giá trị của x là ... giờ ... phút (nhập số thập phân: 1,5 giờ).", "a": "1,5"},
            {"q": "Một vườn dâu tây công nghệ cao mở cửa đón khách từ 7 giờ 30 phút sáng đến 17 giờ chiều. Thời gian mở cửa là ... giờ ... phút (nhập 9,5 giờ).", "a": "9,5"},
            # Lượt 3
            {"q": "Thời gian bay từ sân bay Liên Khương (Đà Lạt) về sân bay Tân Sơn Nhất là 50 phút. Chuyến bay khởi hành lúc 14 giờ 25 phút sẽ hạ cánh lúc ... giờ ... phút (nhập theo dạng hh:mm, ví dụ 15:15).", "a": "15:15"},
            {"q": "Bác nông dân sấy hồng giòn Đà Lạt: mẻ 1 sấy hết 3 ngày 8 giờ, mẻ 2 sấy hết 2 ngày 18 giờ. Cả hai mẻ sấy hết ... ngày ... giờ (nhập 6 ngày 2 giờ).", "a": "6 ngày 2 giờ"},
            {"q": "Tính giá trị biểu thức: (2 giờ 15 phút + 1 giờ 45 phút) × 2. Kết quả là ... giờ.", "a": "8"},
            {"q": "Một vận động viên chạy marathon quanh hồ Tuyền Lâm dài 21 km hết 1 giờ 45 phút. Đổi thời gian đó ra giờ dưới dạng số thập phân là ... giờ.", "a": "1,75"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một chiếc xe ô tô du lịch chở khách từ TP.HCM lên Đà Lạt dài 300 km. Xe xuất phát lúc 6 giờ sáng, dọc đường nghỉ ăn trưa và vượt đèo Bảo Lộc hết 1 giờ 30 phút. Xe đến Đà Lạt lúc 13 giờ 30 phút cùng ngày. Tính vận tốc chuyển động thực tế của ô tô trên đường (không tính thời gian nghỉ).\nA. 50 km/giờ\nB. 45 km/giờ\nC. 55 km/giờ\nD. 60 km/giờ",
                "ans_str": "A. 50 km/giờ (Tổng thời gian từ 6h đến 13h30 là 7 giờ 30 phút. Thời gian xe chạy thực tế: 7 giờ 30 phút - 1 giờ 30 phút = 6 giờ. Vận tốc thực tế: 300 : 6 = 50 km/giờ)"
            },
            {
                "q": "Một người thợ làm 3 chiếc giỏ mây đựng hoa khô Đà Lạt hết 4 giờ 30 phút. Người thứ hai làm 4 chiếc giỏ cùng loại hết 5 giờ 20 phút. Hỏi ai làm nhanh hơn và mỗi chiếc giỏ làm nhanh hơn bao nhiêu phút?\nA. Người thứ hai nhanh hơn 10 phút\nB. Người thứ nhất nhanh hơn 10 phút\nC. Người thứ hai nhanh hơn 15 phút\nD. Hai người làm nhanh như nhau",
                "ans_str": "A. Người thứ hai nhanh hơn 10 phút (Người 1 làm 1 giỏ hết: 4 giờ 30 phút : 3 = 270 : 3 = 90 phút. Người 2 làm 1 giỏ hết: 5 giờ 20 phút : 4 = 320 : 4 = 80 phút. Người 2 làm nhanh hơn: 90 - 80 = 10 phút)"
            },
            # Lượt 2
            {
                "q": "Một bể kính trồng hoa sen đá Đà Lạt hình hộp chữ nhật có chiều dài 60 cm, chiều rộng 40 cm và chiều cao 30 cm. Người ta rải một lớp sỏi trắng dày 5 cm ở đáy bể. Tính thể tích lớp sỏi trắng đó theo đơn vị đề-xi-mét khối.\nA. 12 dm³\nB. 10 dm³\nC. 15 dm³\nD. 14 dm³",
                "ans_str": "A. 12 dm³ (Thể tích lớp sỏi: 60 × 40 × 5 = 12 000 cm³ = 12 dm³)"
            },
            {
                "q": "Một đội tình nguyện viên dọn vệ sinh đồi thông Đà Lạt gồm 18 người dự định hoàn thành trong 6 ngày. Nếu muốn hoàn thành sớm hơn 2 ngày thì cần bổ sung thêm bao nhiêu người (năng suất như nhau)?\nA. 9 người\nB. 6 người\nC. 12 người\nD. 8 người",
                "ans_str": "A. 9 người (Số ngày muốn hoàn thành: 6 - 2 = 4 ngày. Tổng số công: 18 × 6 = 108 công. Số người cần có: 108 : 4 = 27 người. Số người cần bổ sung: 27 - 18 = 9 người)"
            },
            # Lượt 3
            {
                "q": "Một cửa hàng hoa Đà Lạt bán một bó hoa cẩm tú cầu với giá lãi 25% so với giá bán. Hỏi cửa hàng đó lãi bao nhiêu phần trăm so với giá vốn?\nA. 33,33% (hoặc 33 1/3%)\nB. 25%\nC. 20%\nD. 30%",
                "ans_str": "A. 33,33% (Coi giá bán là 100% thì tiền lãi là 25%, giá vốn là: 100% - 25% = 75%. Tỉ số phần trăm lãi so với vốn: 25 : 75 = 1/3 ≈ 33,33%)"
            },
            {
                "q": "Một người đi bộ lên dốc đồi Robin ngắm cáp treo Đà Lạt dài 3 km với vận tốc 4 km/giờ, lúc xuống dốc người đó đi với vận tốc 6 km/giờ. Tính vận tốc trung bình của người đó trên cả quãng đường đi và về.\nA. 4,8 km/giờ\nB. 5 km/giờ\nC. 4,5 km/giờ\nD. 5,2 km/giờ",
                "ans_str": "A. 4,8 km/giờ (Thời gian lên dốc: 3 : 4 = 0,75 giờ. Thời gian xuống dốc: 3 : 6 = 0,5 giờ. Tổng quãng đường cả đi và về: 3 + 3 = 6 km. Tổng thời gian: 0,75 + 0,5 = 1,25 giờ. Vận tốc trung bình: 6 : 1,25 = 4,8 km/giờ)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 28: TP. HỒ CHÍ MINH (ĐỊA ĐẠO CỦ CHI, RỪNG SÁC) - TUẦN 28
    # =========================================================================
    {
        "tuan": 28,
        "tram_so": 28,
        "ten_tram": "TP. Hồ Chí Minh (Địa đạo Củ Chi, Rừng Sác)",
        "chu_de": "Vận tốc của một chuyển động đều, đơn vị đo vận tốc",
        "souvenirs": {
            "cap1": "Vành mũ tai bèo Đồng (50đ)",
            "cap2": "Chiếc khăn rằn Chiến khu Bạc (90đ)",
            "cap3": "Ngôi sao Đất Thép Thành Đồng Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Muốn tính vận tốc ta lấy quãng đường chia cho cái gì?", "a": "Thời gian (v = s : t)"},
            {"q": "Đơn vị vận tốc thông dụng của ô tô, xe máy là gì?", "a": "km/giờ (km/h)"},
            {"q": "Đơn vị vận tốc thông dụng của người chạy bộ, bơi lội là gì?", "a": "m/giây (m/s)"},
            {"q": "Một người đi xe máy đi được 90 km trong 2 giờ. Vận tốc là bao nhiêu?", "a": "45 km/giờ (90 : 2 = 45)"},
            {"q": "Một con báo hoa mai chạy 120 m trong 4 giây. Vận tốc là bao nhiêu?", "a": "30 m/giây (120 : 4 = 30)"},
            {"q": "Địa đạo Củ Chi được mệnh danh là vùng đất huyền thoại gì trong kháng chiến?", "a": "Đất thép thành đồng"},
            {"q": "Tổng chiều dài các đường hầm của Địa đạo Củ Chi trong lòng đất là hơn bao nhiêu km?", "a": "Hơn 250 km đường hầm"},
            {"q": "Chiến khu Rừng Sác anh hùng nằm ở huyện ven biển nào của TP.HCM?", "a": "Huyện Cần Giờ"},
            {"q": "Bếp Hoàng Cầm nổi tiếng trong địa đạo Củ Chi có đặc điểm thần kỳ gì?", "a": "Bếp nấu giấu khói (nấu ăn không lộ khói)"},
            {"q": "Một người đi bộ đi được 10 km trong 2,5 giờ. Vận tốc là bao nhiêu?", "a": "4 km/giờ"},
            # Lượt 2
            {"q": "Đổi vận tốc 36 km/giờ sang mét/giây", "a": "10 m/giây (36 000 m : 3 600 s = 10)"},
            {"q": "Đổi vận tốc 15 m/giây sang ki-lô-mét/giờ", "a": "54 km/giờ (15 × 3,6 = 54)"},
            {"q": "Một ô tô đi được 150 km trong 3 giờ. Vận tốc của ô tô là bao nhiêu?", "a": "50 km/giờ"},
            {"q": "Một con chim bồ câu bay 12 km trong 15 phút. Vận tốc là bao nhiêu km/giờ?", "a": "48 km/giờ (15 phút = 0,25 giờ)"},
            {"q": "Một người chạy cự ly 100 m hết 12,5 giây. Vận tốc chạy là bao nhiêu m/s?", "a": "8 m/giây (100 : 12,5 = 8)"},
            {"q": "Đoàn quân chiến đấu quả cảm xuất quỷ nhập thần trong Rừng Sác Cần Giờ là trung đoàn nào?", "a": "Trung đoàn 10 Đặc công Rừng Sác"},
            {"q": "Khu dự trữ sinh quyển Cần Giờ còn được mệnh danh là gì của TP.HCM?", "a": "Lá phổi xanh của thành phố"},
            {"q": "Món ăn mộc mạc làm từ củ mì (sắn) chấm muối vừng của chiến sĩ Củ Chi là gì?", "a": "Khoai mì luộc chấm muối mè"},
            {"q": "Một người đi xe đạp đi 18 km trong 1,2 giờ. Vận tốc là bao nhiêu?", "a": "15 km/giờ"},
            {"q": "Đổi 54 km/giờ sang mét/phút", "a": "900 m/phút (54 000 : 60 = 900)"},
            # Lượt 3
            {"q": "Một tàu hỏa đi được 240 km trong 4 giờ. Vận tốc của tàu hỏa là gì?", "a": "60 km/giờ"},
            {"q": "Một người bơi cự ly 50 m hết 25 giây. Vận tốc bơi là bao nhiêu?", "a": "2 m/giây"},
            {"q": "Một con ốc sên bò được 12 cm trong 1 phút. Vận tốc là bao nhiêu cm/phút?", "a": "12 cm/phút"},
            {"q": "Đổi vận tốc 72 km/giờ sang mét/giây", "a": "20 m/giây (72 : 3,6 = 20)"},
            {"q": "Tính vận tốc của ca nô biết ca nô đi được 42 km trong 1 giờ 45 phút", "a": "24 km/giờ (1 giờ 45 phút = 1,75 giờ)"},
            {"q": "Hầm địa đạo Củ Chi được đào sâu thành mấy tầng trong lòng đất?", "a": "3 tầng hầm"},
            {"q": "Cây cầu vượt biển dài nhất Việt Nam trong tương lai kết nối Cần Giờ với Vũng Tàu là dự án gì?", "a": "Cầu Cần Giờ"},
            {"q": "Rừng ngập mặn Cần Giờ chủ yếu là các loài cây gì giữ đất lấn biển?", "a": "Cây đước, cây mắm, cây bần"},
            {"q": "Một vận động viên đi bộ đi 6 km trong 45 phút. Vận tốc là bao nhiêu km/h?", "a": "8 km/giờ (6 : 0,75 = 8)"},
            {"q": "Nếu thời gian đi giảm đi một nửa trên cùng quãng đường thì vận tốc thay đổi thế nào?", "a": "Gấp lên 2 lần"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một xe buýt du lịch chở học sinh từ trung tâm TP.HCM đi Địa đạo Củ Chi dài 65 km hết 1 giờ 18 phút (1,3 giờ). Vận tốc của xe buýt là ... km/giờ.", "a": "50"},
            {"q": "Một chiến sĩ đặc công Rừng Sác bơi vượt sông Lòng Tàu rộng 600 m hết 10 phút. Vận tốc bơi của chiến sĩ là ... m/phút.", "a": "60"},
            {"q": "Một ca nô cao tốc chạy từ bến Bạch Đằng về Cần Giờ dài 45 km hết 45 phút. Vận tốc của ca nô là ... km/giờ.", "a": "60"},
            {"q": "Một bạn học sinh chạy thử nghiệm đoạn hầm địa đạo Củ Chi dài 120 m hết 1,5 phút. Vận tốc chạy trong hầm là ... m/giây (làm tròn số thập phân).", "a": "1,33 (hoặc 80 m/phút)"},
            # Lượt 2
            {"q": "Một chiếc tàu chở hàng đi trên sông Sài Gòn dài 36 km hết 2 giờ 15 phút. Vận tốc của tàu là ... km/giờ.", "a": "16"},
            {"q": "Một đàn khỉ ở Đảo Khỉ Cần Giờ chuyền cành: một chú khỉ chuyền 180 m hết 30 giây. Vận tốc chuyền của chú khỉ là ... m/giây.", "a": "6"},
            {"q": "Một xe máy đi từ Củ Chi về Tây Ninh dài 48 km hết 1,2 giờ. Vận tốc của xe máy là ... km/giờ.", "a": "40"},
            {"q": "Một người đi bộ thể dục quanh công viên Tao Đàn đi được 3 vòng dài 2,4 km hết 36 phút. Vận tốc đi bộ là ... km/giờ.", "a": "4"},
            # Lượt 3
            {"q": "Đoàn xe quân sự tham quan di tích chạy quãng đường 90 km hết 2 giờ 15 phút (2,25 giờ). Vận tốc của đoàn xe là ... km/giờ.", "a": "40"},
            {"q": "Một chiếc phà Bình Khánh chở khách qua sông Soài Rạp dài 800 m hết 8 phút. Vận tốc của phà là ... km/giờ.", "a": "6"},
            {"q": "Tìm vận tốc của một chiếc máy bay trực thăng biết máy bay bay 180 km trong 45 phút. Vận tốc là ... km/giờ.", "a": "240"},
            {"q": "Một con cá heo bơi ở vùng biển Cần Giờ bơi được 75 m trong 5 giây. Vận tốc bơi của cá heo là ... m/giây.", "a": "15"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một ô tô khởi hành từ Bến xe Miền Đông lúc 6 giờ 15 phút đi tham quan Địa đạo Củ Chi. Dọc đường ô tô dừng nghỉ 15 phút. Ô tô đến Củ Chi lúc 8 giờ. Biết quãng đường dài 75 km. Tính vận tốc của ô tô.\nA. 50 km/giờ\nB. 45 km/giờ\nC. 48 km/giờ\nD. 52 km/giờ",
                "ans_str": "A. 50 km/giờ (Thời gian ô tô đi cả đoạn đường (kể cả thời gian nghỉ) là: 8 giờ - 6 giờ 15 phút = 1 giờ 45 phút = 105 phút. Thời gian thực tế ô tô chạy là: 105 - 15 = 90 (phút) = 1,5 giờ. Vận tốc của ô tô là: 75 : 1,5 = 50 (km/giờ))"
            },
            {
                "q": "Một cano xuôi dòng trên sông Lòng Tàu (Cần Giờ) từ bến A đến bến B dài 36 km hết 1,2 giờ. Biết vận tốc của dòng nước là 3 km/giờ. Tính thời gian cano chạy ngược dòng từ B về lại A.\nA. 1,5 giờ (1 giờ 30 phút)\nB. 1,6 giờ\nC. 1,8 giờ\nD. 2 giờ",
                "ans_str": "A. 1,5 giờ (1 giờ 30 phút) (Vận tốc xuôi dòng: 36 : 1,2 = 30 km/giờ. Vận tốc thực cano: 30 - 3 = 27 km/giờ. Vận tốc ngược dòng: 27 - 3 = 24 km/giờ. Thời gian ngược dòng: 36 : 24 = 1,5 giờ = 1 giờ 30 phút)"
            },
            # Lượt 2
            {
                "q": "Hai người đi xe đạp cùng xuất phát một lúc từ hai đầu đoạn đường Rừng Sác dài 36 km đi ngược chiều nhau. Người thứ nhất đi với vận tốc 13 km/giờ, người thứ hai đi với vận tốc 11 km/giờ. Hỏi sau bao lâu hai người gặp nhau?\nA. 1,5 giờ (1 giờ 30 phút)\nB. 1,2 giờ\nC. 1,8 giờ\nD. 2 giờ",
                "ans_str": "A. 1,5 giờ (1 giờ 30 phút) (Tổng vận tốc hai người: 13 + 11 = 24 km/giờ. Thời gian gặp nhau: 36 : 24 = 1,5 giờ = 1 giờ 30 phút)"
            },
            {
                "q": "Một đoàn xe máy chở khách vượt qua cây cầu Dần Xây (Cần Giờ) dài 400 m. Người lái xe quan sát thấy từ lúc đầu xe lên cầu đến khi đuôi xe rời khỏi cầu hết 30 giây. Biết đoàn xe dài 50 m. Tính vận tốc của đoàn xe theo đơn vị km/giờ.\nA. 54 km/giờ\nB. 48 km/giờ\nC. 60 km/giờ\nD. 45 km/giờ",
                "ans_str": "A. 54 km/giờ (Quãng đường xe đi được: 400 + 50 = 450 m. Vận tốc: 450 : 30 = 15 m/giây = 15 × 3,6 = 54 km/giờ)"
            },
            # Lượt 3
            {
                "q": "Một người đi xe máy từ trung tâm TP.HCM đi Củ Chi trong 1 giờ đầu đi được 42 km. Trong 30 phút sau do đường đông nên người đó chỉ đi được 15 km. Tính vận tốc trung bình của người đó trên cả quãng đường.\nA. 38 km/giờ\nB. 40 km/giờ\nC. 36 km/giờ\nD. 35 km/giờ",
                "ans_str": "A. 38 km/giờ (Tổng quãng đường: 42 + 15 = 57 km. Tổng thời gian: 1 giờ + 0,5 giờ = 1,5 giờ. Vận tốc trung bình: 57 : 1,5 = 38 km/giờ)"
            },
            {
                "q": "Một con báo rừng Sác đuổi theo một con thỏ rừng cách nó 60 m. Vận tốc của báo là 18 m/giây, vận tốc của thỏ là 12 m/giây. Hỏi sau bao lâu con báo đuổi kịp con thỏ?\nA. 10 giây\nB. 12 giây\nC. 15 giây\nD. 8 giây",
                "ans_str": "A. 10 giây (Mỗi giây báo rút ngắn khoảng cách: 18 - 12 = 6 m. Thời gian đuổi kịp: 60 : 6 = 10 giây)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 29: TÂY NINH (NÚI BÀ ĐEN) - TUẦN 29
    # =========================================================================
    {
        "tuan": 29,
        "tram_so": 29,
        "ten_tram": "Tây Ninh (Núi Bà Đen)",
        "chu_de": "Quãng đường, thời gian của chuyển động đều, toán chuyển động ngược chiều và cùng chiều",
        "souvenirs": {
            "cap1": "Chuông gió đỉnh Mây Núi Bà Đồng (50đ)",
            "cap2": "Tượng Phật Bà Tây Bổ Đà Sơn Bạc (90đ)",
            "cap3": "Vương trượng Núi Bà Đen Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Muốn tính quãng đường ta lấy vận tốc nhân với cái gì?", "a": "Thời gian (s = v × t)"},
            {"q": "Muốn tính thời gian ta lấy quãng đường chia cho cái gì?", "a": "Vận tốc (t = s : v)"},
            {"q": "Một ô tô đi với vận tốc 60 km/h trong 2,5 giờ. Quãng đường đi được là bao nhiêu?", "a": "150 km (60 × 2,5 = 150)"},
            {"q": "Một người chạy bộ với vận tốc 8 km/h. Để đi hết 12 km cần bao nhiêu thời gian?", "a": "1,5 giờ (1 giờ 30 phút)"},
            {"q": "Núi Bà Đen ở Tây Ninh được mệnh danh là danh sơn gì của vùng đất Nam Bộ?", "a": "Nóc nhà Nam Bộ"},
            {"q": "Độ cao chính xác của đỉnh Núi Bà Đen là bao nhiêu mét?", "a": "986 m"},
            {"q": "Tượng Phật Bà bằng đồng đỏ trên đỉnh Núi Bà Đen lập kỷ lục châu Á có tên là gì?", "a": "Tượng Phật Bà Tây Bổ Đà Sơn"},
            {"q": "Công trình tôn giáo nguy nga tráng lệ bậc nhất tại Tây Ninh là gì?", "a": "Tòa thánh Cao Đài Tây Ninh"},
            {"q": "Tính quãng đường người đi xe đạp đi trong 3 giờ với vận tốc 15 km/h", "a": "45 km"},
            {"q": "Tính thời gian xe máy đi 80 km với vận tốc 40 km/h", "a": "2 giờ"},
            # Lượt 2
            {"q": "Công thức tính thời gian gặp nhau của hai vật chuyển động ngược chiều là gì?", "a": "t = s : (v1 + v2)"},
            {"q": "Công thức tính thời gian đuổi kịp của hai vật chuyển động cùng chiều là gì?", "a": "t = s : (v1 - v2) (với v1 > v2)"},
            {"q": "Hệ thống cáp treo Núi Bà Đen có nhà ga cáp treo đạt kỷ lục Guinness gì?", "a": "Nhà ga cáp treo lớn nhất thế giới"},
            {"q": "Hồ nước nhân tạo ngọt lớn nhất Việt Nam nằm giáp ranh Tây Ninh và Bình Dương là gì?", "a": "Hồ Dầu Tiếng"},
            {"q": "Gia vị đặc sản cay mặn thơm lừng trứ danh của vùng đất Tây Ninh là gì?", "a": "Muối tôm Tây Ninh (Muối ớt Tây Ninh)"},
            {"q": "Một cano chạy 30 km/h trong 45 phút. Quãng đường đi được là bao nhiêu?", "a": "22,5 km (30 × 0,75 = 22,5)"},
            {"q": "Một người đi 15 km với vận tốc 10 km/h hết bao nhiêu phút?", "a": "90 phút (1,5 giờ)"},
            {"q": "Hai xe đi ngược chiều cách nhau 90 km, tổng vận tốc là 60 km/h. Sau bao lâu gặp nhau?", "a": "1,5 giờ (1 giờ 30 phút)"},
            {"q": "Hai xe đi cùng chiều, xe sau cách xe trước 20 km, hiệu vận tốc là 10 km/h. Sau bao lâu đuổi kịp?", "a": "2 giờ"},
            {"q": "Đặc sản bánh cuốn dẻo phơi sương nổi tiếng của huyện Trảng Bàng, Tây Ninh là gì?", "a": "Bánh tráng phơi sương Trảng Bàng"},
            # Lượt 3
            {"q": "Một tàu bay bay với vận tốc 800 km/h trong 1 giờ 15 phút. Quãng đường bay là bao nhiêu?", "a": "1 000 km (800 × 1,25 = 1 000)"},
            {"q": "Một vận động viên bơi với vận tốc 1,5 m/s. Để bơi hết 90 m cần bao nhiêu giây?", "a": "60 giây (1 phút)"},
            {"q": "Một xe lửa đi với vận tốc 50 km/h trong 3,6 giờ. Quãng đường đi được là bao nhiêu?", "a": "180 km"},
            {"q": "Chùa cổ linh thiêng tọa lạc lưng chừng Núi Bà Đen hơn 300 năm tuổi là chùa gì?", "a": "Chùa Bà Tây Ninh (Linh Sơn Tiên Thạch Tự)"},
            {"q": "Cột mốc tọa độ trên đỉnh Núi Bà Đen được khắc trên chất liệu gì?", "a": "Khối đá hoa cương (granite)"},
            {"q": "Ma Thiên Lãnh là thung lũng hoang sơ huyền bí nằm giữa 3 ngọn núi nào ở Tây Ninh?", "a": "Núi Bà Đen, Núi Phụng và Núi Heo"},
            {"q": "Tính thời gian người đi bộ đi 9 km với vận tốc 4,5 km/h", "a": "2 giờ"},
            {"q": "Một chú ngựa phi với vận tốc 35 km/h trong 2 giờ được quãng đường là bao nhiêu?", "a": "70 km"},
            {"q": "Tính: 1,5 giờ × 60", "a": "90 phút"},
            {"q": "Khi hai xe chuyển động cùng chiều đuổi nhau, khoảng cách giữa hai xe mỗi giờ giảm đi một đoạn bằng gì?", "a": "Hiệu vận tốc hai xe (v1 - v2)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một xe ô tô du lịch đi từ TP.HCM lên Tòa thánh Tây Ninh dài 90 km với vận tốc 45 km/giờ. Thời gian ô tô chạy là ... giờ.", "a": "2"},
            {"q": "Tuyến cáp treo Vân Sơn đưa khách lên đỉnh Núi Bà Đen dài 2 055 m chạy với vận tốc 6 m/giây. Thời gian cabin đi từ chân núi lên đỉnh là ... giây (làm tròn số thập phân: 342,5 giây).", "a": "342,5"},
            {"q": "Một người lái xe máy từ TP Tây Ninh vào hồ Dầu Tiếng dài 28 km với vận tốc 40 km/giờ. Người đó đến nơi sau ... phút.", "a": "42"},
            {"q": "Cùng lúc 7 giờ sáng, một ô tô đi từ Tây Ninh về TP.HCM với vận tốc 50 km/h và một xe máy đi từ TP.HCM lên Tây Ninh với vận tốc 40 km/h. Quãng đường dài 90 km. Hai xe gặp nhau lúc ... giờ.", "a": "8"},
            # Lượt 2
            {"q": "Một đoàn người leo núi theo cung đường cột điện Núi Bà Đen dài 3,6 km với vận tốc trung bình 0,9 km/giờ. Đoàn leo tới đỉnh sau ... giờ.", "a": "4"},
            {"q": "Một người đi xe đạp xuất phát lúc 6 giờ sáng với vận tốc 12 km/h. Lúc 7 giờ sáng, một người đi xe máy đuổi theo với vận tốc 36 km/h. Người đi xe máy đuổi kịp người đi xe đạp sau ... phút.", "a": "30"},
            {"q": "Hồ Dầu Tiếng có diện tích mặt nước 270 km². Chiều dài đập chính là 1 100 m. Đổi 1 100 m sang ki-lô-mét là ... km.", "a": "1,1"},
            {"q": "Một ca nô chạy trên lòng hồ Dầu Tiếng với vận tốc 35 km/h trong 1 giờ 12 phút (1,2 giờ). Quãng đường ca nô chạy được là ... km.", "a": "42"},
            # Lượt 3
            {"q": "Bác Năm mua bánh tráng Trảng Bàng: xe giao hàng đi với vận tốc 45 km/h hết 40 phút. Quãng đường giao hàng dài ... km.", "a": "30"},
            {"q": "Hai vận động viên chạy vòng quanh chân Núi Bà Đen xuất phát cùng lúc từ một điểm. Vận động viên A chạy 10 km/h, vận động viên B chạy 8 km/h. Sau 1,5 giờ hai người cách nhau ... km.", "a": "3"},
            {"q": "Một xe khách đi từ Mộc Bài về Tây Ninh dài 35 km hết 50 phút. Vận tốc xe khách là ... km/giờ.", "a": "42"},
            {"q": "Để lên đỉnh Núi Bà Đen cao 986 m, một người bước trung bình mỗi bước cao 20 cm (0,2 m). Người đó cần bước ít nhất ... bước chân.", "a": "4930"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Quãng đường từ TP.HCM đi Núi Bà Đen (Tây Ninh) dài 100 km. Lúc 6 giờ 30 phút sáng, một ô tô xuất phát từ TP.HCM đi Tây Ninh với vận tốc 55 km/giờ. Cùng lúc đó, một xe máy xuất phát từ Tây Ninh về TP.HCM với vận tốc 45 km/giờ. Hỏi hai xe gặp nhau lúc mấy giờ?\nA. 7 giờ 30 phút\nB. 7 giờ 45 phút\nC. 8 giờ\nD. 7 giờ 15 phút",
                "ans_str": "A. 7 giờ 30 phút (Tổng vận tốc: 55 + 45 = 100 km/giờ. Thời gian đi để gặp nhau: 100 : 100 = 1 giờ. Thời điểm gặp nhau: 6 giờ 30 phút + 1 giờ = 7 giờ 30 phút)"
            },
            {
                "q": "Lúc 7 giờ sáng, một người đi xe máy từ Trảng Bàng đi Tây Ninh với vận tốc 36 km/giờ. Sau đó 30 phút, một ô tô cũng xuất phát từ Trảng Bàng đuổi theo xe máy với vận tốc 54 km/giờ. Hỏi ô tô đuổi kịp xe máy lúc mấy giờ?\nA. 8 giờ 30 phút\nB. 8 giờ\nC. 9 giờ\nD. 8 giờ 15 phút",
                "ans_str": "A. 8 giờ 30 phút (30 phút = 0,5 giờ. Trong 30 phút xe máy đã đi được: 36 × 0,5 = 18 km. Hiệu vận tốc: 54 - 36 = 18 km/giờ. Thời gian ô tô đuổi kịp: 18 : 18 = 1 giờ. Ô tô đuổi kịp lúc: 7 giờ 30 phút + 1 giờ = 8 giờ 30 phút)"
            },
            # Lượt 2
            {
                "q": "Một cano chạy trên hồ Dầu Tiếng từ bến A sang bến B. Nếu chạy với vận tốc 30 km/giờ thì đến B sớm hơn 30 phút so với khi chạy với vận tốc 24 km/giờ. Tính khoảng cách giữa hai bến A và B.\nA. 60 km\nB. 50 km\nC. 72 km\nD. 48 km",
                "ans_str": "A. 60 km (Đổi: 30 phút = 0,5 giờ. Trên cùng quãng đường AB, vận tốc và thời gian là hai đại lượng tỉ lệ nghịch. Tỉ số vận tốc là: 30/24 = 5/4 nên tỉ số thời gian đi tương ứng là 4/5. Thời gian cano chạy với vận tốc 30 km/giờ là: 0,5 : (5 - 4) × 4 = 2 (giờ). Khoảng cách giữa hai bến A và B là: 30 × 2 = 60 (km))"
            },
            {
                "q": "Một tàu hỏa dài 120 m vượt qua một đường hầm dài 480 m xuyên lòng núi hết 30 giây. Tính vận tốc của đoàn tàu hỏa theo đơn vị km/giờ.\nA. 72 km/giờ\nB. 60 km/giờ\nC. 54 km/giờ\nD. 80 km/giờ",
                "ans_str": "A. 72 km/giờ (Quãng đường tàu đi được từ lúc đầu tàu vào hầm đến khi đuôi tàu ra khỏi hầm: 480 + 120 = 600 m. Vận tốc tàu: 600 : 30 = 20 m/giây = 20 × 3,6 = 72 km/giờ)"
            },
            # Lượt 3
            {
                "q": "Hai người đi bộ cùng xuất phát từ chân Núi Bà Đen đi vòng quanh chân núi dài 18 km theo cùng một hướng. Người thứ nhất đi với vận tốc 5 km/giờ, người thứ hai đi với vận tốc 4 km/giờ. Hỏi sau bao lâu người thứ nhất lại gặp người thứ hai lần đầu tiên?\nA. 18 giờ\nB. 9 giờ\nC. 12 giờ\nD. 15 giờ",
                "ans_str": "A. 18 giờ (Để người thứ nhất gặp lại người thứ hai thì người thứ nhất phải đi nhiều hơn người thứ hai đúng 1 vòng quanh chân núi (18 km). Hiệu vận tốc: 5 - 4 = 1 km/giờ. Thời gian gặp lại: 18 : 1 = 18 giờ)"
            },
            {
                "q": "Một con chim đại bàng từ đỉnh Núi Bà Đen bay xuôi gió với vận tốc 45 km/giờ, khi bay ngược gió với vận tốc 35 km/giờ. Tính vận tốc của gió.\nA. 5 km/giờ\nB. 10 km/giờ\nC. 4 km/giờ\nD. 6 km/giờ",
                "ans_str": "A. 5 km/giờ (Vận tốc gió: (45 - 35) : 2 = 5 km/giờ)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 30: TP. HỒ CHÍ MINH (BẾN NHÀ RỒNG, LANDMARK 81) - TUẦN 30
    # =========================================================================
    {
        "tuan": 30,
        "tram_so": 30,
        "ten_tram": "TP. Hồ Chí Minh (Bến Nhà Rồng, Landmark 81)",
        "chu_de": "Thu thập, phân loại, sắp xếp số liệu; biểu đồ hình quạt tròn; xác suất thực nghiệm",
        "souvenirs": {
            "cap1": "Bánh lái Tàu Bến Nhà Rồng Đồng (50đ)",
            "cap2": "Mô hình Tòa tháp Landmark 81 Bạc (90đ)",
            "cap3": "Kim khánh Thành phố Bác Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Biểu đồ hình quạt tròn thường dùng để biểu thị cái gì?", "a": "Tỉ số phần trăm của các phần trong toàn thể"},
            {"q": "Hình tròn trên biểu đồ quạt tròn tương ứng với bao nhiêu phần trăm?", "a": "100%"},
            {"q": "Một nửa hình tròn trên biểu đồ quạt tròn tương ứng với bao nhiêu phần trăm?", "a": "50%"},
            {"q": "Một phần tư hình tròn trên biểu đồ quạt tròn tương ứng với bao nhiêu phần trăm?", "a": "25%"},
            {"q": "Bến cảng lịch sử nơi người thanh niên yêu nước Nguyễn Tất Thành ra đi tìm đường cứu nước là gì?", "a": "Bến Nhà Rồng (Bảo tàng Hồ Chí Minh)"},
            {"q": "Bác Hồ ra đi tìm đường cứu nước trên con tàu Đô đốc Latouche-Tréville vào ngày tháng năm nào?", "a": "Ngày 5 tháng 6 năm 1911"},
            {"q": "Tòa tháp cao nhất Việt Nam và thuộc top những tòa nhà cao nhất thế giới tại TP.HCM là gì?", "a": "Landmark 81"},
            {"q": "Số tầng của tòa tháp Landmark 81 là bao nhiêu tầng?", "a": "81 tầng"},
            {"q": "Tung một đồng xu 10 lần có 6 lần xuất hiện mặt ngửa. Tỉ số số lần xuất hiện mặt ngửa là gì?", "a": "6/10 (hoặc 3/5)"},
            {"q": "Trên biểu đồ quạt tròn, phần quạt biểu thị 20% ứng với góc ở tâm bao nhiêu độ?", "a": "72 độ (360 × 20% = 72)"},
            # Lượt 2
            {"q": "Biểu đồ quạt tròn có 3 phần: phần A chiếm 40%, phần B chiếm 35%. Phần C chiếm bao nhiêu?", "a": "25% (100% - 40% - 35% = 25%)"},
            {"q": "Số lần lặp lại của một sự kiện chia cho tổng số lần thực hiện gọi là gì?", "a": "Tỉ số của số lần lặp lại sự kiện"},
            {"q": "Chiều cao tổng thể đỉnh tháp của Landmark 81 là bao nhiêu mét?", "a": "461,3 m"},
            {"q": "Cây cầu dây văng hiện đại nối quận 1 với bán đảo Thủ Thiêm bắc qua sông Sài Gòn là cầu gì?", "a": "Cầu Ba Son (Cầu Thủ Thiêm 2)"},
            {"q": "Công trình chợ truyền thống mang biểu tượng tháp đồng hồ 4 mặt nổi tiếng ở trung tâm TP.HCM là gì?", "a": "Chợ Bến Thành"},
            {"q": "Di tích lịch sử nơi xe tăng húc đổ cổng sắt trưa ngày 30/4/1975 giải phóng miền Nam là gì?", "a": "Dinh Độc Lập (Hội trường Thống Nhất)"},
            {"q": "Gieo một con xúc xắc 20 lần có 4 lần xuất hiện mặt 6 chấm. Tỉ số lặp lại là bao nhiêu?", "a": "4/20 (hoặc 1/5, 20%)"},
            {"q": "Trong hộp có 3 viên bi xanh và 2 viên bi đỏ. Lấy ngẫu nhiên 1 viên, có mấy khả năng xảy ra?", "a": "2 khả năng (xanh hoặc đỏ)"},
            {"q": "Biểu đồ quạt biểu thị kết quả học tập: 50% Giỏi, 30% Khá. Còn lại là Đạt chiếm bao nhiêu?", "a": "20%"},
            {"q": "Tên gọi trước đây của Bến Nhà Rồng trong thời Pháp thuộc là gì?", "a": "Cảng Sài Gòn"},
            # Lượt 3
            {"q": "Tòa tháp Landmark 81 lấy cảm hứng thiết kế từ hình ảnh biểu tượng văn hóa nào của Việt Nam?", "a": "Bó tre truyền thống vươn lên bầu trời"},
            {"q": "Dòng sông uốn lượn ôm trọn bán đảo Thủ Thiêm và trung tâm TP.HCM là sông gì?", "a": "Sông Sài Gòn"},
            {"q": "Tuyến đường sắt đô thị ngầm hiện đại đầu tiên tại TP.HCM là tuyến Metro số mấy?", "a": "Tuyến Metro số 1 (Bến Thành - Suối Tiên)"},
            {"q": "Tung đồng xu 50 lần có 28 lần mặt sấp. Số lần xuất hiện mặt ngửa là bao nhiêu?", "a": "22 lần (50 - 28 = 22)"},
            {"q": "Một trường có 500 học sinh. Biểu đồ quạt cho biết có 20% học sinh đi xe đạp. Số bạn đi xe đạp là?", "a": "100 bạn (500 × 20% = 100)"},
            {"q": "Một hình tròn tương ứng với góc ở tâm bằng bao nhiêu độ?", "a": "360 độ"},
            {"q": "Phố đi bộ hiện đại rộng lớn trước trụ sở UBND TP.HCM nối thẳng ra Bến Bạch Đằng là phố nào?", "a": "Phố đi bộ Nguyễn Huệ"},
            {"q": "Nhà thờ chính tòa cổ kính xây bằng gạch ngói đỏ Marseille tại trung tâm TP.HCM là nhà thờ nào?", "a": "Nhà thờ Đức Bà Sài Gòn"},
            {"q": "Biểu đồ quạt: mục chi tiêu ăn uống chiếm 50%, tiền nhà chiếm 30%, tiết kiệm chiếm bao nhiêu?", "a": "20%"},
            {"q": "Tỉ số của số lần xuất hiện sự kiện A luôn nằm trong khoảng từ mấy đến mấy?", "a": "Từ 0 đến 1 (hoặc từ 0% đến 100%)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Khảo sát 200 du khách tham quan Bến Nhà Rồng: biểu đồ quạt tròn cho biết có 45% khách quốc tế, còn lại là khách nội địa. Số khách nội địa là ... người.", "a": "110"},
            {"q": "Tòa tháp Landmark 81 có chiều cao 461,3 m. Thang máy chạy với vận tốc 8 m/giây. Thời gian thang máy chạy từ tầng hầm lên đỉnh đài quan sát là ... giây (làm tròn số thập phân: 57,7 giây).", "a": "57,7"},
            {"q": "Bạn Nam thực hiện tung một con xúc xắc 6 mặt 50 lần, đếm được mặt chẵn xuất hiện 28 lần. Tỉ số phần trăm số lần xuất hiện mặt chẵn là ... %.", "a": "56"},
            {"q": "Một công ty lữ hành tại TP.HCM thống kê phương tiện du khách chọn: 50% chọn xe buýt 2 tầng, 30% chọn buýt đường sông, còn lại chọn taxi. Tỉ số phần trăm chọn taxi là ... %.", "a": "20"},
            # Lượt 2
            {"q": "Đài quan sát Landmark 81 SkyView nằm ở 3 tầng cao nhất: tầng 79, 80 và 81. Trong một ngày đón 1 500 lượt khách, trong đó có 60% khách lên vào buổi tối. Số khách buổi tối là ... người.", "a": "900"},
            {"q": "Tàu buýt đường sông (Saigon Waterbus) từ bến Bạch Đằng đi Thủ Đức dài 10,8 km hết 36 phút (0,6 giờ). Vận tốc của buýt sông là ... km/giờ.", "a": "18"},
            {"q": "Một hộp kín chứa 40 viên bi quà tặng lưu niệm gồm hai màu xanh và đỏ. Lấy ngẫu nhiên 100 lần (có hoàn lại) thấy có 65 lần bi đỏ. Ước lượng số bi đỏ trong hộp là khoảng ... viên.", "a": "26 (40 × 65% = 26)"},
            {"q": "Biểu đồ quạt tròn thể hiện phương tiện đến trường của 400 học sinh: đi bộ chiếm 15%, xe đạp chiếm 25%, xe đưa đón chiếm 40%, còn lại bố mẹ chở. Số học sinh được bố mẹ chở là ... bạn.", "a": "80"},
            # Lượt 3
            {"q": "Cầu Ba Son có chiều dài 1 465 m, nhịp chính dây văng dài 200 m. Nhịp chính chiếm khoảng ... % chiều dài toàn cầu (làm tròn số tự nhiên).", "a": "14"},
            {"q": "Tại chợ Bến Thành, một quầy hàng bán 240 chiếc nón lá lưu niệm trong 3 ngày: ngày 1 bán được 35%, ngày 2 bán được 40%. Ngày 3 bán được ... chiếc nón lá.", "a": "60"},
            {"q": "Gieo đồng xu 80 lần thấy có 44 lần xuất hiện mặt ngửa. Tỉ số của số lần xuất hiện mặt sấp là phân số tối giản ... (nhập a/b).", "a": "9/20 (36/80 = 9/20)"},
            {"q": "Phố đi bộ Nguyễn Huệ dài 670 m, rộng 64 m. Diện tích mặt phố đi bộ là ... m².", "a": "42880"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Biểu đồ hình quạt tròn biểu thị cơ cấu 600 du khách lên đài quan sát Landmark 81: khách châu Á chiếm 50%, khách châu Âu chiếm 30%, khách châu Mỹ chiếm 15%, còn lại là khách châu Úc. Hỏi có bao nhiêu du khách châu Úc?\nA. 30 người\nB. 25 người\nC. 35 người\nD. 40 người",
                "ans_str": "A. 30 người (Tỉ số phần trăm khách châu Úc: 100% - (50% + 30% + 15%) = 5%. Số khách châu Úc: 600 × 5% = 30 người)"
            },
            {
                "q": "Một nhóm bạn thực hiện thí nghiệm quay vòng quay may mắn có 4 ô màu: Xanh, Đỏ, Vàng, Trắng. Sau 120 lần quay, kim chỉ vào ô màu Đỏ 36 lần, ô màu Xanh 48 lần, ô màu Vàng 24 lần. Tính tỉ số phần trăm số lần kim chỉ vào ô màu Trắng.\nA. 10%\nB. 15%\nC. 12%\nD. 8%",
                "ans_str": "A. 10% (Số lần chỉ ô màu Trắng: 120 - (36 + 48 + 24) = 12 lần. Tỉ số phần trăm: 12 : 120 × 100 = 10%)"
            },
            # Lượt 2
            {
                "q": "Một cano du lịch trên sông Sài Gòn chạy xuôi dòng từ Bến Bạch Đằng về Bến Nhà Rồng và cầu Ba Son dài 15 km hết 30 phút, ngược dòng hết 45 phút. Tính vận tốc của cano khi nước yên lặng.\nA. 25 km/giờ\nB. 20 km/giờ\nC. 28 km/giờ\nD. 24 km/giờ",
                "ans_str": "A. 25 km/giờ (Vận tốc xuôi dòng: 15 : 0,5 = 30 km/giờ. Vận tốc ngược dòng: 15 : 0,75 = 20 km/giờ. Vận tốc cano khi nước yên lặng: (30 + 20) : 2 = 25 km/giờ)"
            },
            {
                "q": "Trong một hộp kín có 15 quả bóng bàn màu trắng và một số quả màu vàng. Bạn Mai bốc ngẫu nhiên 1 quả, ghi lại màu rồi bỏ lại vào hộp. Sau 100 lần bốc, Mai thấy bóng trắng xuất hiện 60 lần. Hỏi trong hộp có khoảng bao nhiêu quả bóng bàn màu vàng?\nA. 10 quả\nB. 12 quả\nC. 8 quả\nD. 15 quả",
                "ans_str": "A. 10 quả (Tỉ số bóng trắng: 60%. Vậy 15 quả bóng trắng ứng với 60% tổng số bóng. Tổng số bóng trong hộp: 15 : 60% = 25 quả. Số bóng vàng: 25 - 15 = 10 quả)"
            },
            # Lượt 3
            {
                "q": "Thang máy Landmark 81 đưa khách lên tầng quan sát cao 360 m. Chiều lên thang máy đi với vận tốc 8 m/s, chiều xuống đi với vận tốc 6 m/s. Tính vận tốc trung bình của thang máy cả chiều lên và chiều xuống (bỏ qua thời gian dừng đón khách).\nA. 6,86 m/giây\nB. 7 m/giây\nC. 7,2 m/giây\nD. 6,5 m/giây",
                "ans_str": "A. 6,86 m/giây (Thời gian lên: 360 : 8 = 45 giây. Thời gian xuống: 360 : 6 = 60 giây. Tổng quãng đường: 360 × 2 = 720 m. Tổng thời gian: 45 + 60 = 105 giây. Vận tốc trung bình: 720 : 105 ≈ 6,86 m/giây)"
            },
            {
                "q": "Khảo sát sở thích thể thao của 400 học sinh: Bóng đá chiếm 45%, Cầu lông chiếm 30%, Bơi lội chiếm 15%, còn lại là Bóng rổ. Số học sinh thích bóng đá nhiều hơn số học sinh thích bóng rổ bao nhiêu bạn?\nA. 140 bạn\nB. 120 bạn\nC. 150 bạn\nD. 130 bạn",
                "ans_str": "A. 140 bạn (Tỉ số bóng rổ: 100% - (45% + 30% + 15%) = 10%. Hiệu tỉ số bóng đá và bóng rổ: 45% - 10% = 35%. Số học sinh chênh lệch: 400 × 35% = 140 bạn)"
            }
        ]
    }
]
