# -*- coding: utf-8 -*-
"""
Dữ liệu ngân hàng câu hỏi Tuần 31 đến Tuần 35 (Trạm 31 - 35)
Mỗi trạm chuẩn 48 câu hỏi:
- Vòng 1: 30 câu ghép đôi (10 câu/lượt x 3 lượt)
- Vòng 2: 12 bài điền số thực tế (4 câu/lượt x 3 lượt)
- Vòng 3: 6 câu trắc nghiệm Mức 3 (2 câu/lượt x 3 lượt)
"""

TUAN_31_TO_35 = [
    # =========================================================================
    # TRẠM 31: ĐỒNG THÁP (SA ĐÉC, TRÀM CHIM, SEN THÁP MƯỜI) - TUẦN 31
    # =========================================================================
    {
        "tuan": 31,
        "tram_so": 31,
        "ten_tram": "Đồng Tháp (Sa Đéc, Tràm Chim, Sen Tháp Mười)",
        "chu_de": "Ôn tập số tự nhiên, phân số, số thập phân; đọc viết, so sánh và xếp thứ tự số",
        "souvenirs": {
            "cap1": "Chiếc giỏ hoa Sa Đéc Đồng (50đ)",
            "cap2": "Cánh chim Sếu Tràm Chim Bạc (90đ)",
            "cap3": "Búp sen Ngọc Tháp Mười Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Số tự nhiên lớn nhất có 7 chữ số là số nào?", "a": "9 999 999"},
            {"q": "Giá trị của chữ số 5 trong số 25 841 020 là bao nhiêu?", "a": "5 000 000 (năm triệu)"},
            {"q": "Phân số 15/35 rút gọn về phân số tối giản là gì?", "a": "3/7 (chia cả tử và mẫu cho 5)"},
            {"q": "Số thập phân gồm 7 đơn vị và 8 phần trăm viết là gì?", "a": "7,08"},
            {"q": "So sánh: 0,85 và 0,849", "a": "0,85 > 0,849"},
            {"q": "Thủ phủ hoa kiểng lớn nhất miền Tây Nam Bộ nằm tại thành phố nào?", "a": "Làng hoa Sa Đéc (TP Sa Đéc)"},
            {"q": "Vườn quốc gia nổi tiếng là nơi cư trú của loài Sếu đầu đỏ quý hiếm ở Đồng Tháp là gì?", "a": "VQG Tràm Chim (Tam Nông)"},
            {"q": "Vùng đất trứ danh với câu thơ 'Tháp Mười đẹp nhất bông sen' là địa danh nào?", "a": "Đồng sen Tháp Mười"},
            {"q": "Ngôi nhà cổ nổi tiếng gắn liền với chuyện tình văn học lãng mạn tại Sa Đéc là gì?", "a": "Nhà cổ Huỳnh Thủy Lê"},
            {"q": "Số thập phân 3,1415 làm tròn đến hàng phần trăm được số nào?", "a": "3,14"},
            # Lượt 2
            {"q": "Số gồm 3 chục triệu, 5 trăm nghìn và 4 chục viết là gì?", "a": "30 500 040"},
            {"q": "Quy đồng mẫu số hai phân số 3/4 và 5/6 với MSC nhỏ nhất là bao nhiêu?", "a": "9/12 và 10/12 (MSC = 12)"},
            {"q": "Phân số nào bé hơn 1 trong các phân số sau: 5/4; 7/7; 8/9; 11/10?", "a": "8/9"},
            {"q": "Chuyển phân số 23/100 thành số thập phân", "a": "0,23"},
            {"q": "Xếp theo thứ tự từ bé đến lớn: 2,15; 2,05; 2,5; 2,51", "a": "2,05; 2,15; 2,5; 2,51"},
            {"q": "Khu di tích lịch sử nơi an nghỉ của cụ Phó bảng Nguyễn Sinh Sắc (thân sinh Bác Hồ) ở đâu?", "a": "TP Cao Lãnh (Đồng Tháp)"},
            {"q": "Đặc sản nem chua nổi tiếng truyền thống nức tiếng vùng đất Sa Đéc là gì?", "a": "Nem Lai Vung"},
            {"q": "Cây cầu dây văng lớn bắc qua sông Tiền kết nối Đồng Tháp với Tiền Giang là cầu gì?", "a": "Cầu Cao Lãnh"},
            {"q": "Tìm số tự nhiên x, biết: 8,9 < x < 10,1", "a": "x = 9 và x = 10"},
            {"q": "Số nghịch đảo của phân số 7/12 là gì?", "a": "12/7"},
            # Lượt 3
            {"q": "Số tự nhiên bé nhất có 5 chữ số khác nhau là số nào?", "a": "10 234"},
            {"q": "Chuyển hỗn số 3 2/5 thành phân số", "a": "17/5"},
            {"q": "Chuyển phân số thập phân 45/1000 thành số thập phân", "a": "0,045"},
            {"q": "Trong số thập phân 12,345 chữ số 4 thuộc hàng nào?", "a": "Hàng phần trăm"},
            {"q": "So sánh hai phân số: 5/8 và 7/12", "a": "5/8 > 7/12 (15/24 > 14/24)"},
            {"q": "Loài sen khổng lồ có lá to như chiếc nia người ngồi lên không chìm ở chùa Phước Kiển là gì?", "a": "Sen Vua (Sen nia)"},
            {"q": "Khu căn cứ kháng chiến xưa nằm giữa rừng tràm rậm rạp Đồng Tháp Mười là gì?", "a": "Khu di tích Xẻo Quýt"},
            {"q": "Vựa trái cây trứ danh với đặc sản xoài cát chu thơm ngọt ở Đồng Tháp là gì?", "a": "Xoài cát Cao Lãnh"},
            {"q": "Tính: 3/4 + 1/2", "a": "5/4 (hoặc 1 1/4)"},
            {"q": "Số thập phân 0,75 viết dưới dạng phân số tối giản là gì?", "a": "3/4"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Làng hoa Sa Đéc trồng hơn 2 000 loài hoa kiểng. Trong dịp Tết, một nhà vườn xuất bán 3 500 chậu cúc mâm xôi, đã bán được 80% số chậu. Số chậu cúc còn lại là ... chậu.", "a": "700"},
            {"q": "Khu du lịch Đồng sen Tháp Mười rộng 25 ha. Người ta dùng 3/5 diện tích trồng sen lấy hoa và hạt. Diện tích trồng sen là ... ha.", "a": "15"},
            {"q": "Đàn Sếu đầu đỏ bay về VQG Tràm Chim gồm 36 con. Số sếu non bằng 1/3 số sếu trưởng thành. Đàn có ... con sếu non.", "a": "9"},
            {"q": "Tìm x là số tự nhiên, biết: 15,2 < x < 16,8. Giá trị của x là ...", "a": "16"},
            # Lượt 2
            {"q": "Một cơ sở làm nem Lai Vung đóng gói 450 chùm nem trong 3 ngày. Trong 5 ngày cơ sở đó đóng được ... chùm nem (năng suất như nhau).", "a": "750"},
            {"q": "Cầu Cao Lãnh dài hơn 2 000 m bắc qua sông Tiền. Một chiếc xe buýt chạy qua cầu với vận tốc 40 km/h hết 3 phút. Chiều dài quãng đường xe đi là ... m.", "a": "2000"},
            {"q": "Một vườn xoài cát Cao Lãnh thu hoạch được 4,5 tấn xoài. Người ta bán đi 60% số xoài đó. Khối lượng xoài còn lại là ... tạ.", "a": "18"},
            {"q": "Tìm phân số có tử số là 8 và bằng phân số 2/5. Mẫu số của phân số đó là ...", "a": "20"},
            # Lượt 3
            {"q": "Một hồ sen Tháp Mười hình chữ nhật có chu vi 160 m, chiều dài gấp 3 lần chiều rộng. Diện tích hồ sen là ... m².", "a": "1200"},
            {"q": "Một hộp trà sen Đồng Tháp có giá 120 000 đồng. Khách mua 5 hộp được giảm 10%. Số tiền khách phải trả là ... đồng.", "a": "540000 (hoặc 540 000)"},
            {"q": "Xếp các số sau theo thứ tự giảm dần: 3,45; 3,54; 3,5; 3,4. Số lớn nhất trong dãy là ...", "a": "3,54"},
            {"q": "Một bạn học sinh đếm được một chiếc lá sen Vua có đường kính 2 m. Bán kính chiếc lá sen đó là ... m.", "a": "1"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một thửa đất trồng hoa tại Sa Đéc hình chữ nhật có chiều dài 40 m, chiều rộng 25 m. Người ta làm các lối đi bê tông xung quanh và chính giữa chia thửa đất thành 4 luống nhỏ bằng nhau. Biết diện tích các lối đi chiếm 15% diện tích thửa đất. Tính tổng diện tích của 4 luống hoa.\nA. 850 m²\nB. 800 m²\nC. 900 m²\nD. 750 m²",
                "ans_str": "A. 850 m² (Diện tích thửa đất: 40 × 25 = 1 000 m². Diện tích lối đi: 1 000 × 15% = 150 m². Diện tích 4 luống hoa: 1 000 - 150 = 850 m²)"
            },
            {
                "q": "Tìm hai số có tổng bằng 231, biết rằng nếu viết thêm chữ số 0 vào bên phải số bé thì được số lớn.\nA. 21 và 210\nB. 22 và 220\nC. 19 và 190\nD. 24 và 240",
                "ans_str": "A. 21 và 210 (Khi viết thêm chữ số 0 vào bên phải số bé thì được số lớn, suy ra số lớn gấp 10 lần số bé. Tổng số phần bằng nhau là: 1 + 10 = 11 (phần). Số bé là: 231 : 11 = 21. Số lớn là: 21 × 10 = 210)"
            },
            # Lượt 2
            {
                "q": "Một chiếc xuồng máy chở khách ngắm rừng tràm Xẻo Quýt xuôi dòng 12 km hết 30 phút và quay ngược dòng hết 45 phút. Tính vận tốc của dòng nước trên kênh rạch.\nA. 4 km/giờ\nB. 2 km/giờ\nC. 3 km/giờ\nD. 5 km/giờ",
                "ans_str": "A. 4 km/giờ (Vận tốc xuôi dòng: 12 : 0,5 = 24 km/giờ. Vận tốc ngược dòng: 12 : 0,75 = 16 km/giờ. Vận tốc dòng nước: (24 - 16) : 2 = 4 km/giờ)"
            },
            {
                "q": "Một hợp tác xã sen Tháp Mười có số hạt sen tươi loại 1 gấp 3 lần loại 2. Sau khi xuất khẩu 15 tạ hạt sen loại 1 thì số hạt sen loại 1 còn lại bằng số hạt sen loại 2. Tính tổng số tạ hạt sen ban đầu của cả hai loại.\nA. 30 tạ\nB. 25 tạ\nC. 35 tạ\nD. 40 tạ",
                "ans_str": "A. 30 tạ (Ban đầu loại 1 là 3 phần, loại 2 là 1 phần. Hiệu giữa loại 1 và loại 2 là: 3 - 1 = 2 phần. 2 phần ứng với 15 tạ xuất đi => 1 phần = 7,5 tạ. Tổng số hạt sen ban đầu: 7,5 × (3 + 1) = 30 tạ)"
            },
            # Lượt 3
            {
                "q": "Khi cộng một số tự nhiên với một số thập phân có một chữ số ở phần thập phân, một bạn quên viết dấu phẩy của số thập phân nên được tổng là 382. Biết tổng đúng là 134,5. Tìm số tự nhiên ban đầu.\nA. 107\nB. 105\nC. 110\nD. 100",
                "ans_str": "A. 107 (Số thập phân bị tăng gấp 10 lần nên tổng tăng 9 lần số thập phân. 9 lần số thập phân: 382 - 134,5 = 247,5. Số thập phân đúng: 247,5 : 9 = 27,5. Số tự nhiên ban đầu: 134,5 - 27,5 = 107)"
            },
            {
                "q": "Có bao nhiêu số thập phân có hai chữ số ở phần thập phân mà lớn hơn 5,2 và bé hơn 5,3?\nA. 9 số\nB. 10 số\nC. 8 số\nD. Vô số",
                "ans_str": "A. 9 số (Ta có 5,2 = 5,20 và 5,3 = 5,30. Các số có 2 chữ số ở phần thập phân là từ 5,21 đến 5,29. Có tất cả: 29 - 21 + 1 = 9 số)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 32: CÀ MAU (ĐẤT MŨI CÀ MAU) - TUẦN 32
    # =========================================================================
    {
        "tuan": 32,
        "tram_so": 32,
        "ten_tram": "Cà Mau (Đất Mũi Cà Mau)",
        "chu_de": "Ôn tập 4 phép tính (+, -, ×, :) với số tự nhiên, phân số, số thập phân; ôn tập tỉ số",
        "souvenirs": {
            "cap1": "Chiếc mỏ neo Mũi Cà Mau Đồng (50đ)",
            "cap2": "Cột mốc Tọa độ GPS 0001 Bạc (90đ)",
            "cap3": "Con thuyền Cực Nam No Gió Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Tính kết quả phép tính: 245 + 155", "a": "400"},
            {"q": "Tính kết quả phép tính: 500 - 175", "a": "325"},
            {"q": "Tính kết quả phép tính: 25 × 16", "a": "400 (25 × 4 × 4 = 400)"},
            {"q": "Tính kết quả phép tính: 360 : 12", "a": "30"},
            {"q": "Cột mốc tọa độ Quốc gia thiêng liêng đặt tại Đất Mũi Cà Mau có số hiệu là gì?", "a": "Cột mốc GPS 0001"},
            {"q": "Biểu tượng kiến trúc nổi tiếng tại Công viên Văn hóa Mũi Cà Mau có hình gì?", "a": "Con tàu no gió hướng ra biển lớn"},
            {"q": "Vườn quốc gia Mũi Cà Mau nổi tiếng thế giới với hệ sinh thái rừng gì?", "a": "Rừng ngập mặn (rừng đước)"},
            {"q": "Hai loài cây tiên phong giữ đất lấn biển đặc trưng nhất của rừng Cà Mau là gì?", "a": "Cây đước và cây mắm"},
            {"q": "Tính kết quả: 3,5 + 4,75", "a": "8,25"},
            {"q": "Tính kết quả: 10 - 2,65", "a": "7,35"},
            # Lượt 2
            {"q": "Tính kết quả: 2/3 + 3/4", "a": "17/12 (hoặc 1 5/12)"},
            {"q": "Tính kết quả: 5/6 - 1/3", "a": "3/6 (hoặc 1/2)"},
            {"q": "Tính kết quả: 4/5 × 15/16", "a": "3/4"},
            {"q": "Tính kết quả: 3/7 : 6/14", "a": "1"},
            {"q": "Tính kết quả: 2,5 × 4,4", "a": "11"},
            {"q": "Tính kết quả: 15,6 : 3", "a": "5,2"},
            {"q": "Đặc sản giáp xác thơm ngon chắc thịt nổi tiếng bậc nhất đất Cà Mau là gì?", "a": "Cua Năm Căn (Cua Cà Mau)"},
            {"q": "Dòng sông lớn sâu rộng bậc nhất miền Tây chảy qua Cà Mau đổ ra biển Đông và Tây là gì?", "a": "Sông Cửa Lớn"},
            {"q": "Hòn đảo xanh tuyệt đẹp gắn liền với huyền thoại anh hùng khởi nghĩa Hòn Khoai là gì?", "a": "Đảo Hòn Khoai"},
            {"q": "Nghề truyền thống gác kèo ong lấy mật tự nhiên độc đáo trong rừng tràm U Minh gọi là gì?", "a": "Nghề gác kèo ong"},
            # Lượt 3
            {"q": "Tính nhanh: 125 × 79 × 8", "a": "79 000 ((125 × 8) × 79 = 79 000)"},
            {"q": "Tính nhanh: 4,8 × 6,5 + 4,8 × 3,5", "a": "48 (4,8 × 10 = 48)"},
            {"q": "Tính nhanh: 3/5 × 4/7 + 3/5 × 3/7", "a": "3/5"},
            {"q": "Tìm x, biết: x : 0,5 = 24", "a": "x = 12"},
            {"q": "Tìm y, biết: y × 100 = 45,6", "a": "y = 0,456"},
            {"q": "Cà Mau là tỉnh duy nhất trên đất liền nước ta có mấy mặt giáp biển?", "a": "3 mặt giáp biển (Đông, Nam, Tây)"},
            {"q": "Vườn quốc gia U Minh Hạ ở Cà Mau nổi tiếng với loài cây lâm nghiệp chủ đạo nào?", "a": "Cây tràm (rừng tràm U Minh)"},
            {"q": "Món ăn tôm đặc sản sấy khô đậm vị ngọt của vùng đất Năm Căn Cà Mau là gì?", "a": "Tôm khô Cà Mau"},
            {"q": "Tìm hai số có tổng là 90 và tỉ số là 2/3", "a": "36 và 54"},
            {"q": "Tìm hai số có hiệu là 25 và tỉ số là 1/2", "a": "25 và 50"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một chiếc cano cao tốc chở khách từ TP Cà Mau ra Đất Mũi dài 108 km đi hết 2,4 giờ. Vận tốc của cano là ... km/giờ.", "a": "45"},
            {"q": "Một hợp tác xã cua Năm Căn xuất bán 450 kg cua gạch và cua thịt. Trong đó số cua thịt gấp đôi số cua gạch. Khối lượng cua thịt là ... kg.", "a": "300"},
            {"q": "Rừng đước Mũi Cà Mau mỗi năm bồi đắp lấn biển thêm khoảng 80 m. Sau 5 năm, dải đất bồi lấn thêm ... m.", "a": "400"},
            {"q": "Tính giá trị biểu thức: (15,5 + 24,5) : 0,25. Kết quả là ...", "a": "160"},
            # Lượt 2
            {"q": "Một mẻ tôm khô Năm Căn: cứ 10 kg tôm tươi luộc và phơi thì thu được 1,2 kg tôm khô. Để thu được 24 kg tôm khô cần ... kg tôm tươi.", "a": "200"},
            {"q": "Một thợ rừng gác kèo ong ở U Minh Hạ thu hoạch được 45 lít mật ong đợt 1, đợt 2 thu hoạch nhiều hơn đợt 1 là 15 lít. Cả hai đợt thu được ... lít mật ong.", "a": "105"},
            {"q": "Biểu tượng Con tàu Mũi Cà Mau có cánh buồm cao 20,5 m. Thân tàu dài 32 m. Tỉ số giữa chiều cao buồm và chiều dài thân tàu là phân số tối giản ... (nhập 41/64).", "a": "41/64"},
            {"q": "Tìm x, biết: x × 3,5 - x × 1,5 = 30. Giá trị của x là ...", "a": "15"},
            # Lượt 3
            {"q": "Một vuông tôm sinh thái dưới tán rừng đước hình chữ nhật có chu vi 240 m, chiều dài hơn chiều rộng 20 m. Diện tích vuông tôm là ... m².", "a": "3500"},
            {"q": "Đoàn xe du lịch chở 180 khách tham quan Đất Mũi Cà Mau. Mỗi xe chở 45 người. Cần ít nhất ... xe ô tô.", "a": "4"},
            {"q": "Tính nhanh giá trị biểu thức: 1,25 × 3,7 × 8. Kết quả là ...", "a": "37"},
            {"q": "Hải đăng Hòn Khoai nằm ở độ cao 318 m so với mực nước biển. Đổi độ cao này sang ki-lô-mét dưới dạng số thập phân là ... km.", "a": "0,318"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một cano xuôi dòng từ Năm Căn ra Đất Mũi Cà Mau dài 45 km hết 1 giờ 15 phút (1,25 giờ), khi quay về ngược dòng hết 1 giờ 52 phút 30 giây (1,875 giờ). Tính vận tốc của dòng nước trên sông Cửa Lớn.\nA. 6 km/giờ\nB. 4 km/giờ\nC. 5 km/giờ\nD. 3 km/giờ",
                "ans_str": "A. 6 km/giờ (Vận tốc xuôi dòng: 45 : 1,25 = 36 km/giờ. Vận tốc ngược dòng: 45 : 1,875 = 24 km/giờ. Vận tốc dòng nước: (36 - 24) : 2 = 6 km/giờ)"
            },
            {
                "q": "Một người bán cua Cà Mau mua vào với giá 250 000 đồng/kg. Người đó bán ra với giá lãi 20% so với giá vốn. Hỏi khách mua 4 kg cua phải trả bao nhiêu tiền?\nA. 1 200 000 đồng\nB. 1 000 000 đồng\nC. 1 150 000 đồng\nD. 1 250 000 đồng",
                "ans_str": "A. 1 200 000 đồng (Giá bán 1 kg cua: 250 000 × 120% = 300 000 đồng. Mua 4 kg hết: 300 000 × 4 = 1 200 000 đồng)"
            },
            # Lượt 2
            {
                "q": "Một vuông tôm rừng ngập mặn hình chữ nhật có chu vi 300 m. Nếu tăng chiều rộng thêm 10 m và giảm chiều dài 10 m thì diện tích tăng thêm 400 m². Tính diện tích ban đầu của vuông tôm.\nA. 5 000 m²\nB. 5 400 m²\nC. 5 600 m²\nD. 6 000 m²",
                "ans_str": "A. 5 000 m² (Nửa chu vi vuông tôm là: 300 : 2 = 150 (m). Khi tăng chiều rộng 10 m và giảm chiều dài 10 m thì diện tích tăng thêm là: (chiều dài - 10) × (chiều rộng + 10) - chiều dài × chiều rộng = 10 × (chiều dài - chiều rộng) - 100 = 400 => 10 × (chiều dài - chiều rộng) = 500 => Chiều dài hơn chiều rộng là: 50 (m). Chiều dài ban đầu là: (150 + 50) : 2 = 100 (m). Chiều rộng ban đầu là: 150 - 100 = 50 (m). Diện tích ban đầu của vuông tôm là: 100 × 50 = 5 000 (m²))"
            },
            {
                "q": "Tìm một số biết rằng nếu lấy số đó nhân với 4 rồi trừ đi 15 thì bằng số đó chia cho 0,25 cộng thêm 0.\nA. Mọi số đều thỏa mãn\nB. Không có số nào\nC. Số 0\nD. Số 15",
                "ans_str": "B. Không có số nào (Vì chia cho 0,25 chính là nhân với 4. Ta có phương trình: 4x - 15 = 4x => -15 = 0 (vô lý). Do đó không có số nào thỏa mãn)"
            },
            # Lượt 3
            {
                "q": "Tổng của ba số bằng 150. Biết số thứ nhất hơn số thứ hai 15 đơn vị, số thứ hai hơn số thứ ba 15 đơn vị. Tìm số thứ nhất.\nA. 65\nB. 50\nC. 35\nD. 70",
                "ans_str": "A. 65 (Coi số thứ ba là 1 phần thì số thứ hai là 1 phần + 15, số thứ nhất là 1 phần + 30. Tổng 3 số: 3 phần + 45 = 150 => 3 phần = 105 => Số thứ ba = 35. Số thứ hai = 50; Số thứ nhất = 65)"
            },
            {
                "q": "Một can đựng đầy mật ong rừng U Minh cân nặng 12,5 kg. Người ta rót ra một nửa lượng mật ong thì can mật ong còn lại cân nặng 6,5 kg. Hỏi riêng vỏ can cân nặng bao nhiêu ki-lô-gam?\nA. 0,5 kg\nB. 0,6 kg\nC. 0,8 kg\nD. 1 kg",
                "ans_str": "A. 0,5 kg (Một nửa lượng mật ong nặng: 12,5 - 6,5 = 6 kg. Toàn bộ lượng mật ong trong can nặng: 6 × 2 = 12 kg. Khối lượng vỏ can là: 12,5 - 12 = 0,5 kg)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 33: KIÊN GIANG (ĐẢO NGỌC PHÚ QUỐC) - TUẦN 33
    # =========================================================================
    {
        "tuan": 33,
        "tram_so": 33,
        "ten_tram": "Kiên Giang (Đảo Ngọc Phú Quốc)",
        "chu_de": "Ôn tập hình học toàn diện (hình phẳng, chu vi, diện tích; hình khối, thể tích)",
        "souvenirs": {
            "cap1": "Vỏ trai đảo ngọc Đồng (50đ)",
            "cap2": "Cabin cáp treo Hòn Thơm Bạc (90đ)",
            "cap3": "Viên ngọc trai Phú Quốc Hoàng Gia Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Công thức tính diện tích hình tam giác đáy a, chiều cao h là gì?", "a": "S = (a × h) : 2"},
            {"q": "Công thức tính diện tích hình thang có hai đáy a, b và chiều cao h là gì?", "a": "S = ((a + b) × h) : 2"},
            {"q": "Công thức tính chu vi hình tròn bán kính r là gì?", "a": "C = r × 2 × 3,14"},
            {"q": "Công thức tính diện tích hình tròn bán kính r là gì?", "a": "S = r × r × 3,14"},
            {"q": "Đảo Phú Quốc thuộc tỉnh nào của vùng Đồng bằng Sông Cửu Long?", "a": "Tỉnh Kiên Giang"},
            {"q": "Phú Quốc được vinh dự là thành phố đầu tiên nào của Việt Nam?", "a": "Thành phố đảo đầu tiên"},
            {"q": "Bãi biển cát trắng mịn màng hình vầng trăng khuyết đẹp bậc nhất Phú Quốc là bãi gì?", "a": "Bãi Sao (Bãi Khem)"},
            {"q": "Tuyến cáp treo vượt biển ba dây dài nhất thế giới tại Phú Quốc nối sang đảo nào?", "a": "Cáp treo Hòn Thơm (7 899,9 m)"},
            {"q": "Đặc sản trang sức quý giá được nuôi cấy tự nhiên tại Phú Quốc là gì?", "a": "Ngọc trai Phú Quốc"},
            {"q": "Tính diện tích hình tam giác có đáy 8 cm và chiều cao 5 cm", "a": "20 cm²"},
            # Lượt 2
            {"q": "Tính diện tích hình thang có đáy lớn 10 cm, đáy bé 6 cm, chiều cao 4 cm", "a": "32 cm²"},
            {"q": "Tính chu vi hình tròn có bán kính r = 3 cm", "a": "18,84 cm"},
            {"q": "Tính diện tích hình tròn có bán kính r = 2 cm", "a": "12,56 cm²"},
            {"q": "Công thức tính diện tích xung quanh của hình hộp chữ nhật là gì?", "a": "Sxq = (a + b) × 2 × c"},
            {"q": "Công thức tính thể tích của hình hộp chữ nhật là gì?", "a": "V = a × b × c"},
            {"q": "Đặc sản gia vị hạt cay nồng thơm lừng nổi tiếng cả nước tại Phú Quốc là gì?", "a": "Hồ tiêu Phú Quốc"},
            {"q": "Nước mắm truyền thống Phú Quốc nổi tiếng được làm từ loài cá nào?", "a": "Cá cơm tươi than cườm"},
            {"q": "Công viên chăm sóc và bảo tồn động vật bán hoang dã lớn nhất Việt Nam tại Phú Quốc là gì?", "a": "Vinpearl Safari Phú Quốc"},
            {"q": "Thành phố không ngủ lung linh sắc màu với dòng sông Venice tại Bắc đảo Phú Quốc là gì?", "a": "Grand World Phú Quốc"},
            {"q": "Tính thể tích hình lập phương có cạnh 4 cm", "a": "64 cm³ (4 × 4 × 4 = 64)"},
            # Lượt 3
            {"q": "Tính diện tích toàn phần của hình lập phương cạnh 3 cm", "a": "54 cm² (3 × 3 × 6 = 54)"},
            {"q": "Hình tròn có đường kính 8 cm thì bán kính là bao nhiêu cm?", "a": "4 cm"},
            {"q": "Hình thang có diện tích 50 cm², chiều cao 5 cm. Tổng hai đáy là bao nhiêu?", "a": "20 cm (50 × 2 : 5 = 20)"},
            {"q": "Một tam giác có diện tích 30 cm², đáy 12 cm. Chiều cao là bao nhiêu?", "a": "5 cm (30 × 2 : 12 = 5)"},
            {"q": "Nếu bán kính hình tròn gấp lên 3 lần thì diện tích gấp lên mấy lần?", "a": "9 lần (3 × 3 = 9)"},
            {"q": "Chiều dài tuyến cáp treo Hòn Thơm vượt biển đạt kỷ lục Guinness là bao nhiêu mét?", "a": "7 899,9 m (gần 7,9 km)"},
            {"q": "Thị trấn hoàng hôn mang phong cách Địa Trung Hải rực rỡ bên bờ biển Nam Phú Quốc là gì?", "a": "Thị trấn Hoàng Hôn (Sunset Town)"},
            {"q": "Cây cầu độc đáo có hai nhánh không chạm nhau nơi ngắm hoàng hôn tuyệt đẹp ở Phú Quốc là gì?", "a": "Cầu Hôn (Kiss Bridge)"},
            {"q": "Tính thể tích hình hộp chữ nhật có kích thước 5 cm, 4 cm và 2 cm", "a": "40 cm³"},
            {"q": "Hình hộp chữ nhật có mấy mặt, mấy đỉnh và mấy cạnh?", "a": "6 mặt, 8 đỉnh, 12 cạnh"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Tuyến cáp treo Hòn Thơm dài 7 899,9 m. Một cabin chạy với vận tốc 8,5 m/giây. Thời gian cabin vượt biển sang Hòn Thơm là ... giây (làm tròn số tự nhiên: 929 giây).", "a": "929"},
            {"q": "Một hồ bơi trong khu nghỉ dưỡng Bãi Sao hình hộp chữ nhật dài 25 m, rộng 12 m và sâu 1,8 m. Thể tích nước tối đa của hồ bơi là ... m³.", "a": "540"},
            {"q": "Một bồn hoa ngọc trai hình tròn ở trung tâm Dương Đông có chu vi 31,4 m. Diện tích bồn hoa đó là ... m².", "a": "78,5"},
            {"q": "Một luống hồ tiêu Phú Quốc hình thang có đáy lớn 18 m, đáy bé 12 m và chiều cao 6 m. Diện tích luống tiêu là ... m².", "a": "90"},
            # Lượt 2
            {"q": "Một thùng gỗ ủ nước mắm truyền thống hình trụ có diện tích đáy 3,14 m², chiều cao 2,5 m. Thể tích thùng gỗ đó là ... m³.", "a": "7,85"},
            {"q": "Một lồng kính trưng bày viên ngọc trai hình lập phương có cạnh 30 cm. Diện tích kính để làm 5 mặt lồng (không đáy) là ... cm².", "a": "4500"},
            {"q": "Cầu Hôn (Kiss Bridge) gồm hai nhánh dài 400 m mỗi nhánh. Khoảng cách khe hở giữa hai mũi cầu là 30 cm. Đổi 30 cm sang mét là ... m.", "a": "0,3"},
            {"q": "Một thửa đất trồng tiêu hình chữ nhật có chu vi 200 m, chiều dài gấp 4 lần chiều rộng. Diện tích thửa đất là ... m².", "a": "1600"},
            # Lượt 3
            {"q": "Một chiếc cano chạy quanh đảo Phú Quốc hết 3 giờ với vận tốc 35 km/h. Quãng đường cano đi được là ... km.", "a": "105"},
            {"q": "Một sân chơi trẻ em hình bán nguyệt (nửa hình tròn) có đường kính 20 m. Diện tích sân chơi đó là ... m².", "a": "157"},
            {"q": "Người ta sơn 4 bức tường xung quanh một phòng nghỉ resort dài 7 m, rộng 5 m, cao 3 m. Diện tích tường cần sơn là ... m² (bỏ qua cửa 8 m²).", "a": "64"},
            {"q": "Tìm thể tích của khối lập phương có diện tích một mặt bằng 25 cm². Thể tích là ... cm³.", "a": "125"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một chiếc hồ nuôi trai cấy ngọc hình tròn có bán kính 10 m. Người ta làm một lối đi dạo bằng gỗ xung quanh hồ rộng 2 m. Tính diện tích lối đi dạo đó (lấy pi = 3,14).\nA. 138,16 m²\nB. 125,6 m²\nC. 150,72 m²\nD. 144,5 m²",
                "ans_str": "A. 138,16 m² (Bán kính ngoài: 10 + 2 = 12 m. Diện tích hình tròn lớn: 12 × 12 × 3,14 = 452,16 m². Diện tích hồ trai: 10 × 10 × 3,14 = 314 m². Diện tích lối đi: 452,16 - 314 = 138,16 m²)"
            },
            {
                "q": "Một bể cá cảnh hình hộp chữ nhật có chiều dài 60 cm, chiều rộng 40 cm và đang chứa nước sâu 20 cm. Người ta thả vào bể 5 viên đá phong thủy hình lập phương cạnh 10 cm chìm hoàn toàn trong nước. Hỏi mực nước trong bể dâng lên thêm bao nhiêu xăng-ti-mét?\nA. 2,08 cm\nB. 2,5 cm\nC. 3 cm\nD. 2 cm",
                "ans_str": "A. 2,08 cm (Thể tích 5 viên đá: 5 × (10 × 10 × 10) = 5 000 cm³. Diện tích đáy bể: 60 × 40 = 2 400 cm². Mực nước dâng thêm: 5 000 : 2 400 ≈ 2,08 cm)"
            },
            # Lượt 2
            {
                "q": "Một vườn hoa hình chữ nhật có chiều dài gấp đôi chiều rộng. Ở bốn góc vườn người ta xây 4 bồn hoa hình tam giác vuông có hai cạnh góc vuông bằng 4 m. Phần đất còn lại ở giữa để lát gạch có diện tích là 768 m². Tính chiều dài ban đầu của khu vườn.\nA. 40 m\nB. 36 m\nC. 48 m\nD. 44 m",
                "ans_str": "A. 40 m (Tổng diện tích 4 bồn hoa góc: 4 × (4 × 4 : 2) = 32 m². Diện tích khu vườn ban đầu: 768 + 32 = 800 m². Gọi chiều rộng là r, chiều dài 2r => 2r² = 800 => r² = 400 => r = 20 m. Chiều dài: 20 × 2 = 40 m)"
            },
            {
                "q": "Hai người cùng chèo thuyền kayak trên biển Phú Quốc xuất phát từ Bãi Sao đi cùng hướng. Người thứ nhất đi với vận tốc 6 km/giờ, người thứ hai đi với vận tốc 4,5 km/giờ. Sau 1 giờ 20 phút hai thuyền cách nhau bao nhiêu ki-lô-mét?\nA. 2 km\nB. 1,5 km\nC. 2,5 km\nD. 3 km",
                "ans_str": "A. 2 km (1 giờ 20 phút = 4/3 giờ. Hiệu vận tốc hai người: 6 - 4,5 = 1,5 km/giờ. Khoảng cách hai thuyền: 1,5 × 4/3 = 2 km)"
            },
            # Lượt 3
            {
                "q": "Một khối gỗ hình lập phương có diện tích toàn phần là 150 cm². Người ta gọt bớt một góc của khối gỗ thành một khối lập phương nhỏ cạnh 2 cm. Hỏi diện tích toàn phần của khối gỗ còn lại là bao nhiêu?\nA. 150 cm²\nB. 142 cm²\nC. 138 cm²\nD. 146 cm²",
                "ans_str": "A. 150 cm² (Khi cắt bỏ một khối lập phương nhỏ ở đỉnh của khối lập phương lớn thì diện tích mất đi 3 mặt vuông nhỏ nhưng đồng thời lại xuất hiện thêm 3 mặt vuông nhỏ mới bên trong. Do đó diện tích toàn phần của khối gỗ không thay đổi, vẫn là 150 cm²)"
            },
            {
                "q": "Một mảnh đất hình thang có diện tích 360 m², đáy lớn 28 m, đáy bé 20 m. Người ta mở rộng đáy lớn thêm 5 m thì diện tích tăng thêm bao nhiêu mét vuông?\nA. 37,5 m²\nB. 35 m²\nC. 40 m²\nD. 45 m²",
                "ans_str": "A. 37,5 m² (Chiều cao hình thang: 360 × 2 : (28 + 20) = 720 : 48 = 15 m. Diện tích phần tăng thêm: 5 × 15 : 2 = 37,5 m²)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 34: KHÁNH HÒA (QUẦN ĐẢO TRƯỜNG SA THIÊNG LIÊNG) - TUẦN 34
    # =========================================================================
    {
        "tuan": 34,
        "tram_so": 34,
        "ten_tram": "Khánh Hòa (Quần đảo Trường Sa thiêng liêng)",
        "chu_de": "Ôn tập đo lường toàn diện (độ dài, khối lượng, diện tích, thể tích, thời gian), toán chuyển động đều",
        "souvenirs": {
            "cap1": "Quả bàng vuông Trường Sa Đồng (50đ)",
            "cap2": "Cột mốc Chủ quyền Đảo Bạc (90đ)",
            "cap3": "Ngôi sao Hải quân Trường Sa Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Bảng đơn vị đo độ dài từ lớn đến bé: km, hm, dam, m, dm, cm, ...?", "a": "mm"},
            {"q": "Hai đơn vị đo độ dài liền nhau gấp hoặc kém nhau bao nhiêu lần?", "a": "10 lần"},
            {"q": "Hai đơn vị đo khối lượng liền nhau gấp hoặc kém nhau bao nhiêu lần?", "a": "10 lần"},
            {"q": "Hai đơn vị đo diện tích liền nhau gấp hoặc kém nhau bao nhiêu lần?", "a": "100 lần"},
            {"q": "Hai đơn vị đo thể tích liền nhau gấp hoặc kém nhau bao nhiêu lần?", "a": "1 000 lần"},
            {"q": "Quần đảo Trường Sa thiêng liêng trực thuộc huyện đảo Trường Sa của tỉnh nào?", "a": "Tỉnh Khánh Hòa"},
            {"q": "Loài cây kiên cường biểu tượng cho sức sống mãnh liệt nơi đảo xa Trường Sa là cây gì?", "a": "Cây bàng vuông (và cây phong ba)"},
            {"q": "Đảo lớn nhất và là trung tâm chỉ huy hành chính của quần đảo Trường Sa là đảo nào?", "a": "Đảo Trường Sa Lớn"},
            {"q": "Những công trình nhà giàn thép sừng sững trên thềm lục địa phía Nam bảo vệ biển trời là gì?", "a": "Nhà giàn DK1"},
            {"q": "Đổi 2 km 50 m sang mét", "a": "2 050 m"},
            # Lượt 2
            {"q": "Đổi 3 tấn 50 kg sang ki-lô-gam", "a": "3 050 kg"},
            {"q": "Đổi 4 ha sang mét vuông", "a": "40 000 m²"},
            {"q": "Đổi 2,5 m³ sang lít", "a": "2 500 lít"},
            {"q": "Đổi 1,5 giờ sang phút", "a": "90 phút"},
            {"q": "1 hải lý (dặm biển) xấp xỉ bằng bao nhiêu mét?", "a": "Khoảng 1 852 m"},
            {"q": "Ngọn hải đăng cổ sừng sững dẫn đường tàu thuyền trên đảo Song Tử Tây xây năm nào?", "a": "Năm 1993"},
            {"q": "Đảo nổi xanh mát nhất quần đảo Trường Sa rợp bóng cây bàng vuông là đảo nào?", "a": "Đảo Nam Yết"},
            {"q": "Chiến sĩ hải quân nhân dân Việt Nam canh giữ biển đảo Trường Sa mang tên thân thương là gì?", "a": "Người lính Hải quân (Chiến sĩ Trường Sa)"},
            {"q": "Tính: 3 giờ 25 phút + 1 giờ 35 phút", "a": "5 giờ"},
            {"q": "Một tàu hải quân đi 90 hải lý trong 5 giờ. Vận tốc là bao nhiêu hải lý/h (hải lý/giờ gọi là gút - knot)?", "a": "18 gút (knot)"},
            # Lượt 3
            {"q": "Đổi 45 000 m² sang héc-ta", "a": "4,5 ha"},
            {"q": "Đổi 350 dm³ sang mét khối", "a": "0,35 m³"},
            {"q": "Đổi 2 thế kỷ bằng bao nhiêu năm?", "a": "200 năm"},
            {"q": "Tính: 5 km² 20 ha bằng bao nhiêu héc-ta?", "a": "520 ha (500 + 20 = 520)"},
            {"q": "Công thức tính vận tốc khi biết quãng đường s và thời gian t là gì?", "a": "v = s : t"},
            {"q": "Bảo vật quốc gia bằng đá thiêng tại chùa Trường Sa Lớn được đúc từ đá gì?", "a": "Đá san hô hoặc gốm sứ tâm linh"},
            {"q": "Huyện đảo Trường Sa có bao nhiêu xã và thị trấn?", "a": "3 đơn vị (Thị trấn Trường Sa, xã Song Tử Tây, xã Sinh Tồn)"},
            {"q": "Lời thề bất tử của anh hùng liệt sĩ bảo vệ cờ Tổ quốc trên đảo Gạc Ma năm 1988 là gì?", "a": "Vòng tròn bất tử"},
            {"q": "Đổi 0,75 tấn sang ki-lô-gam", "a": "750 kg"},
            {"q": "Một máy bay tuần thám bay 1 200 km trong 2 giờ. Vận tốc bay là bao nhiêu?", "a": "600 km/giờ"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một chuyến tàu hải quân chở hàng và quà Tết từ đất liền ra đảo Trường Sa dài 250 hải lý (~463 km) với vận tốc 12,5 hải lý/giờ. Thời gian tàu chạy liên tục là ... giờ.", "a": "20"},
            {"q": "Một bể ngầm chứa nước ngọt trên đảo Trường Sa Lớn hình hộp chữ nhật có dung tích 120 m³. Mỗi ngày đảo dùng hết 4 m³ nước. Lượng nước đủ dùng trong ... ngày.", "a": "30"},
            {"q": "Các chiến sĩ trồng rau xanh trong nhà giàn DK1 trong các khay đất hình hộp chữ nhật: 20 khay, mỗi khay cần 0,15 m³ đất phù sa. Tổng lượng đất chuyển ra đảo là ... m³.", "a": "3"},
            {"q": "Một lá cờ Tổ quốc trên đảo Trường Sa hình chữ nhật có chiều dài 6 m, chiều rộng 4 m. Diện tích lá cờ là ... m².", "a": "24"},
            # Lượt 2
            {"q": "Một đàn chim hải âu bay lượn quanh đảo: giờ thứ nhất bay được 45 km, giờ thứ hai bay được 55 km. Vận tốc bay trung bình của chim hải âu là ... km/giờ.", "a": "50"},
            {"q": "Đảo Nam Yết có chu vi bờ cát dạng hình tròn khép kín dài 1 884 m. Bán kính của hòn đảo là khoảng ... m (lấy pi = 3,14).", "a": "300"},
            {"q": "Một máy lọc nước biển thành nước ngọt trên đảo sản xuất được 250 lít nước ngọt mỗi giờ. Trong 8 giờ máy lọc được ... m³ nước ngọt.", "a": "2"},
            {"q": "Tính giá trị biểu thức: 4,5 tấn + 2 500 kg : 1 000. Kết quả là ... tấn.", "a": "7"},
            # Lượt 3
            {"q": "Một ngọn hải đăng ở Trường Sa chớp sáng 3 nháy mỗi chu kỳ 15 giây. Trong 1 giờ ngọn hải đăng thực hiện ... chu kỳ chớp sáng.", "a": "240"},
            {"q": "Một cây bàng vuông cổ thụ trên đảo che bóng mát một vùng đất hình tròn có bán kính 8 m. Diện tích bóng râm che phủ là ... m² (lấy pi = 3,14).", "a": "200,96"},
            {"q": "Hai tàu hải quân xuất phát cùng lúc từ hai đảo cách nhau 60 hải lý đi ngược chiều nhau. Vận tốc tàu A là 16 hải lý/h, tàu B là 14 hải lý/h. Sau ... giờ hai tàu gặp nhau.", "a": "2"},
            {"q": "Một thùng quà học sinh đất liền gửi tặng Trường Sa nặng 45 kg gồm sách vở và bánh kẹo. Biết khối lượng sách vở gấp 4 lần bánh kẹo. Bánh kẹo nặng ... kg.", "a": "9"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một tàu cứu hộ xuất phát từ đất liền ra vùng biển Trường Sa với vận tốc 24 hải lý/giờ. Sau khi tàu chạy được 2 giờ thì có một thủy phi cơ xuất phát đuổi theo với vận tốc 120 hải lý/giờ. Hỏi sau bao lâu kể từ lúc cất cánh, thủy phi cơ đuổi kịp tàu cứu hộ?\nA. 30 phút (0,5 giờ)\nB. 45 phút\nC. 40 phút\nD. 1 giờ",
                "ans_str": "A. 30 phút (0,5 giờ) (Quãng đường tàu đi trước: 24 × 2 = 48 hải lý. Hiệu vận tốc: 120 - 24 = 96 hải lý/giờ. Thời gian đuổi kịp: 48 : 96 = 0,5 giờ = 30 phút)"
            },
            {
                "q": "Trên đảo Trường Sa có một bể chứa nước mưa hình hộp chữ nhật có kích thước đáy 8 m và 5 m, chiều sâu 2,5 m. Hiện tại bể đang chứa lượng nước bằng 60% thể tích bể. Sau một trận mưa lớn kéo dài, lượng nước trong bể tăng thêm 25 m³. Hỏi lúc này mực nước trong bể cách miệng bể bao nhiêu mét?\nA. 0,375 m\nB. 0,5 m\nC. 0,25 m\nD. 0,4 m",
                "ans_str": "A. 0,375 m (Thể tích bể: 8 × 5 × 2,5 = 100 m³. Lượng nước ban đầu: 100 × 60% = 60 m³. Lượng nước sau mưa: 60 + 25 = 85 m³. Chiều cao mực nước: 85 : (8 × 5) = 85 : 40 = 2,125 m. Mực nước cách miệng bể: 2,5 - 2,125 = 0,375 m)"
            },
            # Lượt 2
            {
                "q": "Một đơn vị hải quân trên đảo Trường Sa có số gạo dự trữ đủ cho 30 chiến sĩ ăn trong 40 ngày. Sau khi ăn được 10 ngày thì có thêm một số chiến sĩ đến đảo, do đó số gạo còn lại chỉ đủ ăn trong 20 ngày nữa. Hỏi có bao nhiêu chiến sĩ mới đến đảo (mức ăn như nhau)?\nA. 15 chiến sĩ\nB. 10 chiến sĩ\nC. 20 chiến sĩ\nD. 12 chiến sĩ",
                "ans_str": "A. 15 chiến sĩ (Số ngày ăn còn lại của 30 người: 40 - 10 = 30 ngày. Tổng số suất ăn còn lại: 30 × 30 = 900 suất. Số người ăn trong 20 ngày: 900 : 20 = 45 người. Số chiến sĩ mới đến: 45 - 30 = 15 chiến sĩ)"
            },
            {
                "q": "Một trạm hải đăng chạy bằng năng lượng mặt trời trên đảo Trường Sa: ban ngày tích điện được 12 kWh, ban đêm đèn tiêu thụ 0,8 kWh mỗi giờ trong 10 giờ đêm. Hỏi lượng điện tích lũy còn dư lại mỗi ngày là bao nhiêu?\nA. 4 kWh\nB. 5 kWh\nC. 3 kWh\nD. 2 kWh",
                "ans_str": "A. 4 kWh (Điện tiêu thụ ban đêm: 0,8 × 10 = 8 kWh. Lượng điện dư: 12 - 8 = 4 kWh)"
            },
            # Lượt 3
            {
                "q": "Một cano tuần tra chạy quanh một hòn đảo hình chữ nhật có chu vi 12 km. Khi xuôi dòng gió biển cano chạy với vận tốc 24 km/giờ, khi ngược dòng cano chạy với vận tốc 16 km/giờ. Tính vận tốc trung bình của cano trên toàn bộ chuyến tuần tra quanh đảo.\nA. 19,2 km/giờ\nB. 20 km/giờ\nC. 18,5 km/giờ\nD. 20,5 km/giờ",
                "ans_str": "A. 19,2 km/giờ (Coi quãng đường xuôi và ngược bằng nhau = 6 km. Thời gian xuôi: 6 : 24 = 0,25 giờ. Thời gian ngược: 6 : 16 = 0,375 giờ. Tổng thời gian: 0,25 + 0,375 = 0,625 giờ. Vận tốc trung bình: 12 : 0,625 = 19,2 km/giờ)"
            },
            {
                "q": "Để đo chiều cao một cột cờ chủ quyền Tổ quốc trên đảo Trường Sa, chiến sĩ cắm một cọc thẳng đứng cao 1,5 m thì thấy bóng cọc dài 1 m. Cùng lúc đó, bóng của cột cờ trên mặt đất đo được dài 16 m. Tính chiều cao của cột cờ Tổ quốc đó.\nA. 24 m\nB. 20 m\nC. 22 m\nD. 25 m",
                "ans_str": "A. 24 m (Tỉ số giữa chiều cao vật và chiều dài bóng: 1,5 : 1 = 1,5 lần. Chiều cao cột cờ: 16 × 1,5 = 24 m)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 35: ĐÀ NẴNG (QUẦN ĐẢO HOÀNG SA THIÊNG LIÊNG) - TUẦN 35 🏆 CK2
    # =========================================================================
    {
        "tuan": 35,
        "tram_so": 35,
        "ten_tram": "Đà Nẵng (Quần đảo Hoàng Sa thiêng liêng) 🏆 CK2",
        "chu_de": "Tổng ôn tập toàn diện Cuối năm (Đề thi đánh giá năng lực Cuối năm lớp 5)",
        "souvenirs": {
            "cap1": "Huy chương Chiến sĩ Hoàng Sa Đồng (50đ)",
            "cap2": "Phiến đá Chủ quyền Quần đảo Hoàng Sa Bạc (90đ)",
            "cap3": "Cúp Vàng Quán Quân Xuyên Việt (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Số tự nhiên lớn nhất có 8 chữ số khác nhau là số nào?", "a": "98 765 432"},
            {"q": "Tính kết quả phép tính: 4,85 + 5,15", "a": "10"},
            {"q": "Tính kết quả phép tính: 20 - 7,45", "a": "12,55"},
            {"q": "Tính kết quả phép tính: 1,25 × 8", "a": "10"},
            {"q": "Tính kết quả phép tính: 45 : 1,5", "a": "30"},
            {"q": "Quần đảo Hoàng Sa thiêng liêng trực thuộc quyền quản lý hành chính của huyện đảo Hoàng Sa thuộc thành phố nào?", "a": "Thành phố Đà Nẵng"},
            {"q": "Nhà trưng bày Hoàng Sa lưu giữ hàng trăm tư liệu, bản đồ khẳng định chủ quyền của nước ta nằm trên đường biển nào tại Đà Nẵng?", "a": "Đường Hoàng Sa (bán đảo Sơn Trà)"},
            {"q": "Đội dân binh hùng dũng thời các chúa Nguyễn hàng năm dong thuyền ra Hoàng Sa đo đạc, cắm mốc chủ quyền là đội gì?", "a": "Hải đội Hoàng Sa"},
            {"q": "Diện tích hình thang có hai đáy a, b và chiều cao h tính theo công thức nào?", "a": "S = ((a + b) × h) : 2"},
            {"q": "Hình tròn có bán kính r = 5 cm có diện tích là bao nhiêu?", "a": "78,5 cm²"},
            # Lượt 2
            {"q": "Rút gọn phân số 48/64 về phân số tối giản", "a": "3/4"},
            {"q": "Tính: 3/4 + 2/5", "a": "23/20 (hoặc 1 3/20)"},
            {"q": "Tính: 5/6 - 3/8", "a": "11/24"},
            {"q": "Tính: 2 1/3 × 1 1/2", "a": "7/2 (hoặc 3 1/2)"},
            {"q": "Tính: 4 1/2 : 3/4", "a": "6"},
            {"q": "Châu bản, mộc bản triều Nguyễn khẳng định chủ quyền Việt Nam đối với Hoàng Sa được UNESCO công nhận là gì?", "a": "Di sản tư liệu thế giới"},
            {"q": "Quần đảo Hoàng Sa gồm bao nhiêu cụm đảo chính?", "a": "2 cụm đảo (Cụm Lưỡi Liềm và Cụm An Vĩnh)"},
            {"q": "Đảo có diện tích tự nhiên lớn nhất trong quần đảo Hoàng Sa là đảo nào?", "a": "Đảo Phú Lâm"},
            {"q": "Đổi 4 ha 500 m² sang héc-ta dưới dạng số thập phân", "a": "4,05 ha"},
            {"q": "Đổi 2,8 m³ sang lít", "a": "2 800 lít"},
            # Lượt 3
            {"q": "Tìm x, biết: x + 4,5 = 12,8", "a": "x = 8,3"},
            {"q": "Tìm y, biết: y × 2,5 = 20", "a": "y = 8"},
            {"q": "Tính chu vi hình tròn có đường kính d = 10 dm", "a": "31,4 dm"},
            {"q": "Thể tích hình lập phương cạnh 5 dm là bao nhiêu lít?", "a": "125 lít (125 dm³)"},
            {"q": "Một ô tô đi 120 km hết 2 giờ 30 phút. Vận tốc của ô tô là bao nhiêu?", "a": "48 km/giờ"},
            {"q": "Bia chủ quyền của nước ta tại Hoàng Sa được dựng từ thời nhà Nguyễn khẳng định điều gì?", "a": "Chủ quyền ngàn đời bất khả xâm phạm của Việt Nam"},
            {"q": "Tên gọi truyền thống của vùng biển bãi cát vàng Hoàng Sa trong các thư tịch cổ là gì?", "a": "Bãi Cát Vàng (Hoàng Sa Chử)"},
            {"q": "Chặng 35 này là chặng về đích của hành trình thám hiểm Xuyên Việt gồm bao nhiêu trạm thi?", "a": "35 trạm thi toàn quốc"},
            {"q": "Tìm số tự nhiên x lớn nhất thỏa mãn: x < 45,89", "a": "x = 45"},
            {"q": "Học xong chương trình Toán 5, em đã chinh phục xong cấp học nào?", "a": "Cấp Tiểu học (Sẵn sàng lên Lớp 6)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một chiếc tàu hải giám tuần tra vùng biển Hoàng Sa chạy với vận tốc 18 hải lý/giờ trong 15 giờ. Quãng đường tàu đi được là ... hải lý.", "a": "270"},
            {"q": "Nhà trưng bày Hoàng Sa tại Đà Nẵng đón 450 học sinh trong 3 đợt. Đợt 1 đón 1/3 tổng số học sinh, đợt 2 đón 40% số học sinh. Đợt 3 đón ... học sinh.", "a": "120"},
            {"q": "Một bia đá chủ quyền hình hộp chữ nhật có kích thước dài 1,2 m; rộng 0,8 m và cao 2 m. Thể tích khối bia đá đó là ... m³.", "a": "1,92"},
            {"q": "Tìm hai số có tổng là 120 và tỉ số là 1/3. Số lớn là ...", "a": "90"},
            # Lượt 2
            {"q": "Tàu cá của ngư dân Đà Nẵng đánh bắt hải sản ở ngư trường Hoàng Sa: chuyến này thu được 15 tấn cá ngừ và cá thu. Trong đó cá ngừ chiếm 65%. Khối lượng cá ngừ là ... tấn.", "a": "9,75"},
            {"q": "Một bồn hoa mô phỏng hình dáng quần đảo Hoàng Sa hình tam giác có đáy 24 m, chiều cao 15 m. Diện tích bồn hoa là ... m².", "a": "180"},
            {"q": "Cùng lúc 7 giờ sáng, hai tàu xuất phát từ Đà Nẵng và Hoàng Sa đi ngược chiều nhau. Vận tốc tàu một là 30 km/h, tàu hai là 20 km/h. Quãng đường dài 300 km. Hai tàu gặp nhau lúc ... giờ.", "a": "13"},
            {"q": "Tìm x, biết: (x + 2,4) : 1,5 = 6. Giá trị của x là ...", "a": "6,6"},
            # Lượt 3
            {"q": "Khối sa bàn quần đảo Hoàng Sa hình chữ nhật có chu vi 16 m, chiều dài hơn chiều rộng 2 m. Diện tích sa bàn đó là ... m².", "a": "15"},
            {"q": "Một bể kính hình lập phương cạnh 0,6 m chứa đầy nước biển mẫu từ Hoàng Sa. Lượng nước biển trong bể là ... lít.", "a": "216"},
            {"q": "Tính giá trị biểu thức: 45,6 : 2,4 + 12,5 × 4. Kết quả là ...", "a": "69"},
            {"q": "Em đã hoàn thành trọn vẹn 35 trạm thám hiểm Toán 5 Xuyên Việt. Tổng số trạm đã vượt qua là ... trạm.", "a": "35"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một tàu cứu hộ của Vùng 3 Hải quân xuất phát từ Đà Nẵng đi Hoàng Sa dài 315 km. Trong 3 giờ đầu tàu chạy với vận tốc 35 km/giờ. Sau đó biển động, tàu phải giảm vận tốc xuống 30 km/giờ. Hỏi tàu đến vùng biển Hoàng Sa sau tổng cộng bao nhiêu thời gian?\nA. 10 giờ\nB. 9 giờ\nC. 8 giờ 30 phút\nD. 9 giờ 30 phút",
                "ans_str": "A. 10 giờ (Quãng đường đi trong 3 giờ đầu: 35 × 3 = 105 km. Quãng đường còn lại: 315 - 105 = 210 km. Thời gian đi chặng sau: 210 : 30 = 7 giờ. Tổng thời gian: 3 + 7 = 10 giờ)"
            },
            {
                "q": "Một bể nước ngầm trên đảo hình hộp chữ nhật có chu vi đáy 24 m, chiều dài gấp đôi chiều rộng và chiều sâu 2 m. Hiện bể đang cạn nước. Người ta bơm nước vào bể với công suất 12 m³/giờ. Hỏi sau bao lâu nước trong bể đầy cách miệng 0,5 m?\nA. 4 giờ\nB. 5 giờ\nC. 3,5 giờ\nD. 4,5 giờ",
                "ans_str": "A. 4 giờ (Nửa chu vi đáy: 24 : 2 = 12 m. Chiều rộng: 12 : (2 + 1) = 4 m; Chiều dài: 4 × 2 = 8 m. Mực nước cần đạt: 2 - 0,5 = 1,5 m. Thể tích nước cần bơm: 8 × 4 × 1,5 = 48 m³. Thời gian bơm: 48 : 12 = 4 giờ)"
            },
            # Lượt 2
            {
                "q": "Kỳ thi khảo sát chất lượng Cuối năm lớp 5 có 20 câu hỏi. Mỗi câu trả lời đúng được cộng 5 điểm, mỗi câu trả lời sai hoặc không làm bị trừ 2 điểm. Bạn Robot tham gia thi và đạt tổng cộng 72 điểm. Hỏi bạn Robot đã trả lời đúng bao nhiêu câu hỏi?\nA. 16 câu\nB. 17 câu\nC. 15 câu\nD. 18 câu",
                "ans_str": "A. 16 câu (Giả sử Robot làm đúng cả 20 câu thì được: 20 × 5 = 100 điểm. Số điểm hụt đi: 100 - 72 = 28 điểm. Mỗi câu sai hụt đi: 5 + 2 = 7 điểm. Số câu làm sai là: 28 : 7 = 4 câu. Số câu làm đúng là: 20 - 4 = 16 câu)"
            },
            {
                "q": "Cho hai số thập phân A và B có tổng bằng 104,5. Biết rằng nếu dời dấu phẩy của số A sang bên phải một chữ số thì được số B. Tìm số A.\nA. 9,5\nB. 8,5\nC. 10,5\nD. 7,5",
                "ans_str": "A. 9,5 (Dời dấu phẩy sang phải một chữ số thì số B gấp 10 lần số A. Tổng số phần bằng nhau: 10 + 1 = 11 phần. Số A là: 104,5 : 11 = 9,5; Số B là 95)"
            },
            # Lượt 3
            {
                "q": "Một khu vườn hoa hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Người ta mở rộng khu vườn bằng cách tăng cả chiều dài và chiều rộng thêm 5 m thì diện tích tăng thêm 325 m². Tính diện tích khu vườn ban đầu.\nA. 675 m²\nB. 972 m²\nC. 864 m²\nD. 1 080 m²",
                "ans_str": "A. 675 m² (Diện tích tăng thêm gồm: 5 × chiều dài + 5 × chiều rộng + 5 × 5 = 325 => 5 × (chiều dài + chiều rộng) = 300 => Chiều dài + chiều rộng = 60 (m). Tổng số phần bằng nhau: 3 + 1 = 4 (phần). Chiều rộng ban đầu là: 60 : 4 = 15 (m). Chiều dài ban đầu là: 15 × 3 = 45 (m). Diện tích ban đầu của khu vườn là: 45 × 15 = 675 (m²))"
            },
            {
                "q": "Một cano xuôi dòng từ cảng A ra cụm đảo B mất 2 giờ, khi quay ngược dòng từ B về A mất 3 giờ. Biết khoảng cách AB là 60 km. Tính vận tốc của dòng nước biển.\nA. 5 km/giờ\nB. 4 km/giờ\nC. 6 km/giờ\nD. 3 km/giờ",
                "ans_str": "A. 5 km/giờ (Vận tốc xuôi dòng: 60 : 2 = 30 km/giờ. Vận tốc ngược dòng: 60 : 3 = 20 km/giờ. Vận tốc dòng nước: (30 - 20) : 2 = 5 km/giờ)"
            }
        ]
    }
]
