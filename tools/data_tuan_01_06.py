# -*- coding: utf-8 -*-
"""
Dữ liệu ngân hàng câu hỏi Tuần 1 đến Tuần 6 (Trạm 1 - 6)
Mỗi trạm chuẩn 48 câu hỏi:
- Vòng 1: 30 câu ghép đôi (10 câu/lượt x 3 lượt)
- Vòng 2: 12 câu điền số thực tế (4 câu/lượt x 3 lượt)
- Vòng 3: 6 câu trắc nghiệm Mức 3 (2 câu/lượt x 3 lượt)
"""

TUAN_01_TO_06 = [
    # =========================================================================
    # TRẠM 1: CỘT CỜ LŨNG CÚ (HÀ GIANG) - TUẦN 1
    # =========================================================================
    {
        "tuan": 1,
        "tram_so": 1,
        "ten_tram": "Cột cờ Lũng Cú (Hà Giang)",
        "chu_de": "Ôn tập số tự nhiên, 4 phép tính với số tự nhiên, ôn tập phân số cơ bản",
        "v1": [
            # Lượt 1
            {"q": "Số tự nhiên lớn nhất có 6 chữ số khác nhau", "a": "987 654"},
            {"q": "Lá cờ Tổ quốc trên đỉnh Cột cờ Lũng Cú rộng bao nhiêu mét vuông?", "a": "54 m²"},
            {"q": "Tính nhanh: 25 × 36 × 4", "a": "3 600"},
            {"q": "Phân số chỉ 3 phần tô màu trong 5 phần bằng nhau", "a": "3/5"},
            {"q": "Rút gọn phân số 18/24 về tối giản", "a": "3/4"},
            {"q": "Quy đồng mẫu số 2/3 và 3/5 với mẫu chung 15", "a": "10/15 và 9/15"},
            {"q": "Phân số có tử số bé hơn mẫu số", "a": "Bé hơn 1"},
            {"q": "Số trung bình cộng của 15, 25 và 50", "a": "30"},
            {"q": "Một triệu viết bằng chữ số có mấy chữ số 0?", "a": "6 chữ số 0"},
            {"q": "1/4 thế kỷ bằng bao nhiêu năm?", "a": "25 năm"},
            # Lượt 2
            {"q": "Số tự nhiên bé nhất có 6 chữ số khác nhau", "a": "102 345"},
            {"q": "Cột cờ Lũng Cú thuộc tỉnh nào ở cực Bắc nước ta?", "a": "Hà Giang"},
            {"q": "Tính nhanh: 125 × 47 × 8", "a": "47 000"},
            {"q": "Phân số chỉ 7 phần trong 10 phần bằng nhau", "a": "7/10"},
            {"q": "Rút gọn phân số 35/49 về tối giản", "a": "5/7"},
            {"q": "Quy đồng mẫu số 3/4 và 5/6 với mẫu chung 12", "a": "9/12 và 10/12"},
            {"q": "Phân số có tử số lớn hơn mẫu số", "a": "Lớn hơn 1"},
            {"q": "Số trung bình cộng của 20, 30 và 40", "a": "30"},
            {"q": "Một tỉ viết bằng chữ số có mấy chữ số 0?", "a": "9 chữ số 0"},
            {"q": "1/2 thế kỷ bằng bao nhiêu năm?", "a": "50 năm"},
            # Lượt 3
            {"q": "Đỉnh Lũng Cú có độ cao khoảng bao nhiêu mét so với mực nước biển?", "a": "1 470 m"},
            {"q": "Giá trị của chữ số 9 trong số 892 415", "a": "90 000"},
            {"q": "Tính nhanh: 50 × 68 × 2", "a": "6 800"},
            {"q": "Phân số bằng phân số 1/3 có mẫu số là 18", "a": "6/18"},
            {"q": "Rút gọn phân số 48/60 về tối giản", "a": "4/5"},
            {"q": "Quy đồng mẫu số 1/2 và 3/4 với mẫu chung 4", "a": "2/4 và 3/4"},
            {"q": "Phân số có tử số bằng mẫu số (khác 0)", "a": "Bằng 1"},
            {"q": "Số trung bình cộng của 14, 26, 38 và 42", "a": "30"},
            {"q": "Số liền trước của số 1 000 000", "a": "999 999"},
            {"q": "3/4 thế kỷ bằng bao nhiêu năm?", "a": "75 năm"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Để lên đỉnh Cột cờ Lũng Cú (Hà Giang), Robot cần leo 839 bậc đá. Robot đã leo được 539 bậc, Robot còn phải leo ... bậc đá nữa.", "a": "300"},
            {"q": "Đoàn thám hiểm mua 120 hộp chè Shan tuyết Hà Giang làm quà, buổi sáng đã tặng 2/5 số hộp chè. Buổi sáng đã tặng ... hộp chè.", "a": "48"},
            {"q": "Tìm x, biết: x × 4 + x × 6 = 2 400. Giá trị của x là ...", "a": "240"},
            {"q": "Tìm hai số có tổng là 150 và hiệu là 30. Số lớn là ...", "a": "90"},
            # Lượt 2
            {"q": "Một vườn hoa tam giác mạch ở Lũng Cú hình chữ nhật có chu vi 160 m, chiều rộng kém chiều dài 20 m. Chiều rộng vườn hoa là ... m.", "a": "30"},
            {"q": "Một đoàn học sinh gồm 40 bạn tham quan Cột cờ Lũng Cú, trong đó 3/5 số bạn là nữ. Số bạn nam là ... bạn.", "a": "16"},
            {"q": "Tìm y, biết: y × 12 - y × 2 = 1 500. Giá trị của y là ...", "a": "150"},
            {"q": "Tìm hai số có tổng là 280 và hiệu là 40. Số bé là ...", "a": "120"},
            # Lượt 3
            {"q": "Một đội công nhân tu sửa đoạn đường lên xã Lũng Cú dài 150 m trong 3 ngày. Trong 5 ngày đội đó sửa được ... m đường (năng suất như nhau).", "a": "250"},
            {"q": "Bà con vùng cao Lũng Cú thu hoạch được 350 kg ngô nương, đã bán đi 4/7 số ngô đó. Số ngô còn lại là ... kg.", "a": "150"},
            {"q": "Tìm x, biết: 25 × x × 4 = 10 000. Giá trị của x là ...", "a": "100"},
            {"q": "Hai bình chứa nước suối Lũng Cú có tất cả 240 lít nước. Nếu chuyển 20 lít từ bình 1 sang bình 2 thì hai bình bằng nhau. Bình 1 ban đầu có ... lít.", "a": "140"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Trên đường thám hiểm Cột cờ Lũng Cú, bác kiểm lâm cưa một thân gỗ dài 8 m thành các khúc dài 2 m để làm biển chỉ dẫn. Mỗi lần cưa mất 5 phút, sau mỗi lần cưa nghỉ ngơi 2 phút. Bác cưa xong thân gỗ trong bao nhiêu phút?\nA. 15 phút\nB. 19 phút\nC. 21 phút\nD. 28 phút",
                "ans_str": "B. 19 phút (Số khúc gỗ: 8 : 2 = 4 khúc -> Cần 3 lần cưa. 3 lần cưa và 2 lần nghỉ: 3 × 5 + 2 × 2 = 19 phút)"
            },
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = (1 + 3 + 5 + ... + 99) - (2 + 4 + 6 + ... + 98)\nA. 49\nB. 50\nC. 100\nD. 25",
                "ans_str": "B. 50 (Từ 1 đến 99 có 50 số lẻ; từ 2 đến 98 có 49 số chẵn. Ghép cặp: 1 + (3-2) + (5-4) + ... + (99-98) = 1 + 49 = 50)"
            },
            # Lượt 2
            {
                "q": "Hiện nay tổng số tuổi của hai bố con là 48 tuổi. Bốn năm trước, tuổi bố gấp 4 lần tuổi con. Hỏi tuổi con hiện nay là bao nhiêu?\nA. 10 tuổi\nB. 12 tuổi\nC. 14 tuổi\nD. 8 tuổi",
                "ans_str": "B. 12 tuổi (Tổng số tuổi 4 năm trước: 48 - 4 × 2 = 40 tuổi. Tuổi con 4 năm trước: 40 : (1+4) = 8 tuổi. Hiện nay tuổi con là: 8 + 4 = 12 tuổi)"
            },
            {
                "q": "Để đánh số trang của một cuốn sách hướng dẫn du lịch Hà Giang dày 120 trang, người ta phải dùng tất cả bao nhiêu chữ số?\nA. 240 chữ số\nB. 252 chữ số\nC. 260 chữ số\nD. 238 chữ số",
                "ans_str": "B. 252 chữ số (Trang 1-9: 9 chữ số; Trang 10-99: 90 × 2 = 180 chữ số; Trang 100-120: 21 × 3 = 63 chữ số. Tổng = 9 + 180 + 63 = 252 chữ số)"
            },
            # Lượt 3
            {
                "q": "Khi cộng một số tự nhiên với một số tự nhiên có hai chữ số, một bạn viết nhầm chữ số 0 vào giữa hai chữ số đó nên tổng là 1 030. Biết số tự nhiên ban đầu là 825. Tìm số có hai chữ số ban đầu.\nA. 25\nB. 35\nC. 45\nD. 15",
                "ans_str": "A. 25 (Số sau khi viết thêm số 0 vào giữa là: 1 030 - 825 = 205. Số có dạng a0b = 205 -> a = 2, b = 5. Vậy số có hai chữ số ban đầu là 25)"
            },
            {
                "q": "Trong bãi đỗ xe dưới chân Cột cờ Lũng Cú có cả xe máy (2 bánh) và ô tô con (4 bánh). Bác bảo vệ đếm được tất cả 30 chiếc xe và có tổng cộng 84 chiếc bánh xe. Hỏi có bao nhiêu chiếc ô tô?\nA. 18 chiếc ô tô\nB. 12 chiếc ô tô\nC. 14 chiếc ô tô\nD. 16 chiếc ô tô",
                "ans_str": "B. 12 chiếc ô tô (Giả sử cả 30 xe đều là xe máy thì có 60 bánh. Số bánh thiếu: 84 - 60 = 24. Mỗi ô tô hơn xe máy 2 bánh. Số ô tô: 24 : 2 = 12 chiếc)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 2: HẺM TU SẢN & SÔNG NHO QUẾ (HÀ GIANG) - TUẦN 2
    # =========================================================================
    {
        "tuan": 2,
        "tram_so": 2,
        "ten_tram": "Hẻm Tu Sản & Sông Nho Quế (Hà Giang)",
        "chu_de": "Phân số thập phân, ôn tập 4 phép tính với phân số (+, -, ×, :)",
        "v1": [
            # Lượt 1
            {"q": "Phân số thập phân có mẫu số là bao nhiêu?", "a": "10; 100; 1000..."},
            {"q": "Viết phân số 3/5 thành phân số thập phân có mẫu số là 10", "a": "6/10"},
            {"q": "Viết phân số 7/25 thành phân số thập phân có mẫu số là 100", "a": "28/100"},
            {"q": "Tính kết quả phép cộng: 2/7 + 3/7", "a": "5/7"},
            {"q": "Tính kết quả phép trừ: 5/6 - 1/6", "a": "4/6 (hoặc 2/3)"},
            {"q": "Tính kết quả phép nhân: 3/4 × 5/7", "a": "15/28"},
            {"q": "Tính kết quả phép chia: 2/5 : 3/4", "a": "8/15"},
            {"q": "Hẻm Tu Sản nằm dưới chân con đèo nổi tiếng nào?", "a": "Đèo Mã Pí Lèng"},
            {"q": "Vách đá hẻm vực Tu Sản có chiều cao hùng vĩ khoảng bao nhiêu mét?", "a": "700 m đến 800 m"},
            {"q": "Dòng sông Nho Quế có màu nước đặc trưng là màu gì?", "a": "Màu xanh ngọc bích"},
            # Lượt 2
            {"q": "Viết phân số 9/20 thành phân số thập phân có mẫu số là 100", "a": "45/100"},
            {"q": "Viết phân số 1/8 thành phân số thập phân có mẫu số là 1000", "a": "125/1000"},
            {"q": "Phân số nào trong các phân số sau là phân số thập phân: 3/10; 5/7; 9/20; 11/15", "a": "3/10"},
            {"q": "Tính kết quả: 1/4 + 3/8", "a": "5/8"},
            {"q": "Tính kết quả: 7/9 - 1/3", "a": "4/9"},
            {"q": "Tính kết quả: 4/5 × 15/16", "a": "3/4"},
            {"q": "Tính kết quả: 3/7 : 6/7", "a": "1/2"},
            {"q": "Hẻm vực Tu Sản được mệnh danh là hẻm vực sâu nhất khu vực nào?", "a": "Đông Nam Á"},
            {"q": "Tính nhanh: 3/5 × 4/7 + 3/5 × 3/7", "a": "3/5"},
            {"q": "Rút gọn phân số 60/100 về phân số tối giản", "a": "3/5"},
            # Lượt 3
            {"q": "Viết phân số 13/50 thành phân số thập phân có mẫu số là 100", "a": "26/100"},
            {"q": "Viết phân số 3/4 thành phân số thập phân có mẫu số là 100", "a": "75/100"},
            {"q": "Phân số 12/200 rút gọn thành phân số thập phân mẫu số 100", "a": "6/100"},
            {"q": "Tính kết quả: 2/3 + 1/6", "a": "5/6"},
            {"q": "Tính kết quả: 5/8 - 1/4", "a": "3/8"},
            {"q": "Tính kết quả: 5/12 × 4/15", "a": "1/9"},
            {"q": "Tính kết quả: 5/9 : 10/27", "a": "3/2 (hoặc 1 1/2)"},
            {"q": "Sông Nho Quế bắt nguồn từ vùng núi Vân Nam chảy vào tỉnh nào nước ta?", "a": "Hà Giang"},
            {"q": "Tìm phân số nghịch đảo của phân số 4/9", "a": "9/4"},
            {"q": "Tính nhanh: (1/2 + 1/3) × 6", "a": "5"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Đội thuyền du lịch ngắm Hẻm Tu Sản trên sông Nho Quế có 36 chiếc thuyền. Buổi sáng có 5/9 số thuyền xuất bến. Số thuyền còn lại tại bến là ... chiếc.", "a": "16"},
            {"q": "Một thuyền chở du khách xuôi dòng sông Nho Quế đoạn qua Hẻm Tu Sản dài 6 km hết 2/5 giờ. Vận tốc xuôi dòng của thuyền là ... km/giờ.", "a": "15"},
            {"q": "Tìm x, biết: x + 1/3 = 5/6. Giá trị của x là phân số tối giản có mẫu số là ...", "a": "2 (x = 1/2)"},
            {"q": "Một mảnh vườn hình chữ nhật ven sông Nho Quế có chiều dài 4/5 km, chiều rộng 1/2 km. Diện tích mảnh vườn đó là ... km² (nhập phân số dạng a/b).", "a": "2/5"},
            # Lượt 2
            {"q": "Đội tình nguyện viên dọn dẹp rác sông Nho Quế: ngày thứ nhất vớt được 3/8 tấn rác, ngày thứ hai vớt được nhiều hơn ngày thứ nhất 1/4 tấn. Cả hai ngày đội vớt được tất cả ... tấn rác.", "a": "1"},
            {"q": "Một đoàn khách du lịch 45 người thuê thuyền đi ngắm Hẻm Tu Sản. Mỗi thuyền chở được tối đa 6 người. Đoàn cần thuê ít nhất ... chiếc thuyền.", "a": "8"},
            {"q": "Tìm y, biết: y × 2/5 = 4/15. Giá trị của y là phân số tối giản dạng a/b, tử số là ...", "a": "2 (y = 2/3)"},
            {"q": "Một bình đựng nước khoáng cho đoàn leo núi Mã Pí Lèng có 5 lít nước. Mỗi người uống 1/4 lít nước thì chia đủ cho ... người.", "a": "20"},
            # Lượt 3
            {"q": "Đoạn đường đèo Mã Pí Lèng ngắm xuống sông Nho Quế dài 20 km. Một đội đạp xe thể thao đã đi được 3/4 đoạn đường. Quãng đường còn lại phải đi là ... km.", "a": "5"},
            {"q": "Bác lái thuyền sông Nho Quế dự trữ 60 lít dầu. Chuyến thứ nhất dùng 1/3 lượng dầu, chuyến thứ hai dùng 1/4 lượng dầu ban đầu. Sau 2 chuyến bác còn lại ... lít dầu.", "a": "25"},
            {"q": "Tìm x, biết: x : 3/4 = 8/9. Giá trị của x dưới dạng phân số tối giản có tử số là ...", "a": "2 (x = 2/3)"},
            {"q": "Một tấm biển quảng cáo du lịch Hẻm Tu Sản hình vuông có cạnh dài 3/4 m. Diện tích tấm biển đó là ... m² (nhập phân số dạng a/b).", "a": "9/16"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = (1 - 1/2) × (1 - 1/3) × (1 - 1/4) × ... × (1 - 1/10)\nA. 1/2\nB. 1/10\nC. 9/10\nD. 1/9",
                "ans_str": "B. 1/10 (Ta có: A = 1/2 × 2/3 × 3/4 × ... × 9/10. Triệt tiêu các tử số và mẫu số liên tiếp, còn lại 1/10)"
            },
            {
                "q": "Hai chiếc thuyền du lịch cùng xuất phát từ bến sông Nho Quế đi ngược chiều nhau. Thuyền A đi hết khúc sông trong 3 giờ, thuyền B đi hết khúc sông trong 6 giờ. Nếu hai thuyền cùng khởi hành thì sau bao lâu sẽ gặp nhau?\nA. 2 giờ\nB. 4,5 giờ\nC. 1,5 giờ\nD. 2,5 giờ",
                "ans_str": "A. 2 giờ (Trong 1 giờ, thuyền A đi được 1/3 khúc sông, thuyền B đi được 1/6 khúc sông. Cả 2 thuyền đi được: 1/3 + 1/6 = 1/2 khúc sông. Thời gian gặp nhau: 1 : 1/2 = 2 giờ)"
            },
            # Lượt 2
            {
                "q": "Tính tổng sau: S = 1/(1×2) + 1/(2×3) + 1/(3×4) + ... + 1/(99×100)\nA. 99/100\nB. 100/99\nC. 1/100\nD. 1",
                "ans_str": "A. 99/100 (Áp dụng: 1/(n×(n+1)) = 1/n - 1/(n+1). Tổng S = 1 - 1/2 + 1/2 - 1/3 + ... + 1/99 - 1/100 = 1 - 1/100 = 99/100)"
            },
            {
                "q": "Một cửa hàng lưu niệm đèo Mã Pí Lèng bán một tấm khăn thổ cẩm với giá lãi 20% so với giá vốn. Biết số tiền lãi là 40 000 đồng. Hỏi giá bán tấm khăn đó là bao nhiêu?\nA. 200 000 đồng\nB. 240 000 đồng\nC. 160 000 đồng\nD. 280 000 đồng",
                "ans_str": "B. 240 000 đồng (Giá vốn: 40 000 : 20 × 100 = 200 000 đồng. Giá bán = Vốn + Lãi = 200 000 + 40 000 = 240 000 đồng)"
            },
            # Lượt 3
            {
                "q": "Một vòi nước chảy vào bể chứa trên thuyền ngắm hẻm Tu Sản: vòi thứ nhất chảy một mình trong 4 giờ thì đầy bể, vòi thứ hai chảy một mình trong 6 giờ thì đầy bể. Hỏi cả hai vòi cùng chảy thì sau bao lâu bể đầy?\nA. 5 giờ\nB. 2,4 giờ (2 giờ 24 phút)\nC. 3 giờ\nD. 2,5 giờ",
                "ans_str": "B. 2,4 giờ (2 giờ 24 phút) (Trong 1 giờ hai vòi chảy: 1/4 + 1/6 = 5/12 bể. Thời gian đầy bể: 1 : 5/12 = 12/5 giờ = 2,4 giờ = 2 giờ 24 phút)"
            },
            {
                "q": "Lớp 5A có số học sinh nam bằng 2/3 số học sinh nữ. Nếu chuyển 2 bạn nam thành 2 bạn nữ thì số nam bằng 1/2 số nữ. Tính tổng số học sinh lớp 5A tham gia chuyến đi Hà Giang.\nA. 35 học sinh\nB. 40 học sinh\nC. 30 học sinh\nD. 45 học sinh",
                "ans_str": "C. 30 học sinh (Tổng số học sinh cả lớp không đổi. Ban đầu số nam chiếm 2/(2+3) = 2/5 cả lớp. Lúc sau số nam chiếm 1/(1+2) = 1/3 cả lớp. 2 bạn ứng với phân số: 2/5 - 1/3 = 1/15 (cả lớp). Tổng số học sinh lớp 5A là: 2 : 1/15 = 30 (học sinh))"
            }
        ]
    },

    # =========================================================================
    # TRẠM 3: THÁC BẢN GIỐC (CAO BẰNG) - TUẦN 3
    # =========================================================================
    {
        "tuan": 3,
        "tram_so": 3,
        "ten_tram": "Thác Bản Giốc (Cao Bằng)",
        "chu_de": "Cộng, trừ hai phân số khác mẫu số, hỗn số, giải toán phân số",
        "v1": [
            # Lượt 1
            {"q": "Quy đồng và tính kết quả: 1/2 + 1/3", "a": "5/6"},
            {"q": "Quy đồng và tính kết quả: 3/4 - 1/2", "a": "1/4"},
            {"q": "Hỗn số 2 3/5 được đọc là gì?", "a": "Hai và ba phần năm"},
            {"q": "Chuyển hỗn số 3 1/4 thành phân số", "a": "13/4"},
            {"q": "Chuyển phân số 7/2 thành hỗn số", "a": "3 1/2"},
            {"q": "Phần phân số của hỗn số luôn có giá trị như thế nào so với 1?", "a": "Bé hơn 1"},
            {"q": "Thác Bản Giốc nằm trên dòng sông biên giới nào?", "a": "Sông Quây Sơn"},
            {"q": "Thác Bản Giốc thuộc huyện Trùng Khánh của tỉnh nào?", "a": "Cao Bằng"},
            {"q": "Phương tiện đặc trưng du khách thường dùng để ngắm chân Thác Bản Giốc là gì?", "a": "Bè tre"},
            {"q": "So sánh hai hỗn số: 3 1/2 và 2 4/5", "a": "3 1/2 > 2 4/5"},
            # Lượt 2
            {"q": "Quy đồng và tính kết quả: 2/5 + 1/4", "a": "13/20"},
            {"q": "Quy đồng và tính kết quả: 5/6 - 2/3", "a": "1/6"},
            {"q": "Chuyển hỗn số 4 2/3 thành phân số", "a": "14/3"},
            {"q": "Chuyển phân số 19/4 thành hỗn số", "a": "4 3/4"},
            {"q": "Tính tổng hai hỗn số: 1 1/2 + 2 1/4", "a": "3 3/4 (hoặc 15/4)"},
            {"q": "Tính hiệu hai hỗn số: 3 1/2 - 1 1/4", "a": "2 1/4 (hoặc 9/4)"},
            {"q": "Thác Bản Giốc là thác nước tự nhiên lớn thứ mấy Đông Nam Á?", "a": "Lớn nhất Đông Nam Á"},
            {"q": "Đặc sản hạt nổi tiếng thơm bùi của vùng đất Trùng Khánh gần thác là gì?", "a": "Hạt dẻ Trùng Khánh"},
            {"q": "Tính nhanh: 2 1/3 + 3 2/3", "a": "6"},
            {"q": "So sánh hai hỗn số: 4 2/5 và 4 3/7", "a": "4 2/5 < 4 3/7 (vì 14/35 < 15/35)"},
            # Lượt 3
            {"q": "Quy đồng và tính kết quả: 3/8 + 1/6", "a": "13/24"},
            {"q": "Quy đồng và tính kết quả: 7/10 - 2/5", "a": "3/10"},
            {"q": "Chuyển hỗn số 5 3/8 thành phân số", "a": "43/8"},
            {"q": "Chuyển phân số 23/5 thành hỗn số", "a": "4 3/5"},
            {"q": "Tính tích: 1 1/2 × 2 2/3", "a": "4 (3/2 × 8/3 = 4)"},
            {"q": "Tính thương: 2 1/4 : 3/4", "a": "3 (9/4 : 3/4 = 3)"},
            {"q": "Danh thắng động nổi tiếng nằm gần Thác Bản Giốc là động gì?", "a": "Động Ngườm Ngao"},
            {"q": "Mùa nước Thác Bản Giốc đẹp hùng vĩ nhất vào khoảng tháng mấy?", "a": "Tháng 8 đến tháng 10"},
            {"q": "Tìm x, biết: x - 1/2 = 3/4", "a": "5/4 (hoặc 1 1/4)"},
            {"q": "Tính nhanh: 1 3/7 + 2 4/7", "a": "4"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Đội bè tre Thác Bản Giốc có 24 chiếc. Buổi sáng có 5/8 số bè hoạt động, buổi chiều có 3/4 số bè hoạt động. Buổi chiều nhiều hơn buổi sáng ... chiếc bè.", "a": "3"},
            {"q": "Một vườn trồng hạt dẻ Trùng Khánh đợt 1 thu hoạch được 2 1/2 tạ, đợt 2 thu hoạch nhiều hơn đợt 1 là 3/4 tạ. Cả hai đợt thu hoạch được ... tạ hạt dẻ (nhập phân số tối giản a/b).", "a": "23/4 (hoặc 5,75)"},
            {"q": "Mua 6 hộp hạt dẻ sấy đặc sản Thác Bản Giốc hết 480 000 đồng. Mua 9 hộp cùng loại như thế hết tất cả ... đồng.", "a": "720000 (hoặc 720 000)"},
            {"q": "Tìm x, biết: x + 1 1/3 = 3 5/6. Giá trị của x dưới dạng phân số tối giản là ... (nhập a/b).", "a": "5/2 (hoặc 2 1/2)"},
            # Lượt 2
            {"q": "Một đoàn khách có 35 người tham quan động Ngườm Ngao. Vé người lớn là 40 000 đồng, vé trẻ em là 20 000 đồng. Đoàn có 15 trẻ em. Tổng số tiền vé của cả đoàn là ... đồng.", "a": "1100000 (hoặc 1 100 000)"},
            {"q": "Dòng sông Quây Sơn đoạn chảy qua thác Bản Giốc: một chiếc bè tre xuôi dòng 4 km hết 1/3 giờ. Vận tốc xuôi dòng của bè tre là ... km/giờ.", "a": "12"},
            {"q": "Tìm y, biết: y - 2 1/4 = 1 1/2. Giá trị của y là phân số có tử số là ... (mẫu số là 4).", "a": "15 (y = 15/4 = 3 3/4)"},
            {"q": "Một kho hạt dẻ có 3 tấn hạt dẻ. Ngày thứ nhất xuất 1 1/4 tấn, ngày thứ hai xuất 4/5 tấn. Trong kho còn lại ... tấn hạt dẻ (nhập số thập phân hoặc phân số).", "a": "19/20 (hoặc 0,95)"},
            # Lượt 3
            {"q": "Một thửa ruộng bậc thang gần Thác Bản Giốc hình chữ nhật có chu vi 140 m, chiều dài gấp 4 lần chiều rộng. Diện tích thửa ruộng đó là ... m².", "a": "784"},
            {"q": "Một gia đình bản địa làm bánh khảo Cao Bằng: 5 kg gạo nếp làm được 8 hộp bánh. Để làm được 24 hộp bánh cùng loại cần ... kg gạo nếp.", "a": "15"},
            {"q": "Tìm x, biết: x × 1 1/2 = 4 1/2. Giá trị của x là ...", "a": "3"},
            {"q": "Bác nông dân có hai bao hạt dẻ nặng tất cả 90 kg. Nếu chuyển 5 kg từ bao 1 sang bao 2 thì hai bao bằng nhau. Ban đầu bao 1 có ... kg hạt dẻ.", "a": "50"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = 2 3/7 + 1 4/9 + 3 4/7 + 2 5/9\nA. 9\nB. 10\nC. 11\nD. 12",
                "ans_str": "B. 10 (Ghép các cặp có cùng mẫu số: (2 3/7 + 3 4/7) + (1 4/9 + 2 5/9) = 6 + 4 = 10)"
            },
            {
                "q": "Một chiếc bè du lịch trên sông Quây Sơn xuôi dòng từ bến A đến bến B hết 2 giờ và ngược dòng từ B về A hết 3 giờ. Biết cụm bèo trôi theo dòng nước từ A đến B với vận tốc dòng nước. Hỏi cụm bèo trôi từ A đến B mất bao lâu?\nA. 6 giờ\nB. 12 giờ\nC. 10 giờ\nD. 5 giờ",
                "ans_str": "B. 12 giờ (1 giờ xuôi đi được 1/2 khúc sông, 1 giờ ngược đi được 1/3 khúc sông. Vận tốc dòng nước = (1/2 - 1/3) : 2 = 1/12 khúc sông/giờ. Vậy cụm bèo trôi mất 12 giờ)"
            },
            # Lượt 2
            {
                "q": "Một đội thợ gồm 12 người dự định hoàn thành việc gia cố kè đá bờ sông Quây Sơn trong 10 ngày. Sau khi làm được 4 ngày thì có thêm 6 người nữa đến giúp. Hỏi đội thợ hoàn thành công việc sớm hơn dự định mấy ngày?\nA. 2 ngày\nB. 3 ngày\nC. 4 ngày\nD. 1 ngày",
                "ans_str": "A. 2 ngày (Số công việc còn lại 12 người làm trong 6 ngày = 72 công. Số người lúc sau: 12 + 6 = 18 người. Thời gian làm nốt: 72 : 18 = 4 ngày. Sớm hơn: 6 - 4 = 2 ngày)"
            },
            {
                "q": "Hai người cùng mua hạt dẻ Trùng Khánh. Người thứ nhất mua 3 kg loại 1 và 2 kg loại 2 hết 340 000 đồng. Người thứ hai mua 2 kg loại 1 và 3 kg loại 2 hết 310 000 đồng. Tính giá tiền 1 kg hạt dẻ loại 1.\nA. 80 000 đồng\nB. 70 000 đồng\nC. 60 000 đồng\nD. 75 000 đồng",
                "ans_str": "A. 80 000 đồng (5 kg loại 1 + 5 kg loại 2 hết 650 000 -> 1 kg mỗi loại = 130 000 đồng. Nhân 2: 2 kg loại 1 + 2 kg loại 2 = 260 000 đồng. Vậy 1 kg loại 1 = 340 000 - 260 000 = 80 000 đồng)"
            },
            # Lượt 3
            {
                "q": "Tìm hai phân số tối giản có mẫu số bằng nhau, biết tổng của chúng là 5/6 và hiệu của chúng là 1/6.\nA. 1/2 và 1/3\nB. 3/6 và 2/6\nC. 2/3 và 1/6\nD. 7/12 và 3/12",
                "ans_str": "A. 1/2 và 1/3 (Số lớn = (5/6 + 1/6) : 2 = 6/6 : 2 = 1/2. Số bé = 5/6 - 1/2 = 2/6 = 1/3)"
            },
            {
                "q": "Một mảnh đất hình chữ nhật ven thác Bản Giốc có chiều dài gấp 3 lần chiều rộng. Nếu tăng chiều rộng thêm 5 m và giảm chiều dài 5 m thì diện tích tăng thêm 175 m². Tính diện tích ban đầu của mảnh đất.\nA. 1 200 m²\nB. 1 875 m²\nC. 1 500 m²\nD. 2 400 m²",
                "ans_str": "B. 1 875 m² (Gọi chiều rộng là r, chiều dài là 3r. Ta có: (3r - 5)(r + 5) - 3r² = 175 => 10r - 25 = 175 => 10r = 200 => r = 25 m. Chiều dài = 75 m. Diện tích = 25 × 75 = 1 875 m²)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 4: HỒ BA BỂ (BẮC KẠN) - TUẦN 4
    # =========================================================================
    {
        "tuan": 4,
        "tram_so": 4,
        "ten_tram": "Hồ Ba Bể (Bắc Kạn)",
        "chu_de": "Ôn tập hình học và đo lường, làm quen khái niệm số thập phân",
        "v1": [
            # Lượt 1
            {"q": "3 m 5 dm bằng bao nhiêu đề-xi-mét?", "a": "35 dm"},
            {"q": "4 tấn 50 kg bằng bao nhiêu ki-lô-gam?", "a": "4 050 kg"},
            {"q": "2 giờ 15 phút bằng bao nhiêu phút?", "a": "135 phút"},
            {"q": "Công thức tính diện tích hình bình hành đáy a, chiều cao h là gì?", "a": "S = a × h"},
            {"q": "Công thức tính diện tích hình thoi có hai đường chéo m và n là gì?", "a": "S = (m × n) : 2"},
            {"q": "Phân số thập phân 1/10 được viết dưới dạng số thập phân là gì?", "a": "0,1"},
            {"q": "Số thập phân 0,01 có tên gọi là mấy phần trăm?", "a": "Một phần trăm"},
            {"q": "Hồ Ba Bể gồm mấy nhánh hồ thông nhau?", "a": "3 nhánh hồ (Pé Lầm, Pé Lù, Pé Lèng)"},
            {"q": "Hồ Ba Bể là hồ nước ngọt tự nhiên lớn nhất khu vực nào nước ta?", "a": "Miền Bắc (và cả nước)"},
            {"q": "Thuyền truyền thống làm bằng một thân cây gỗ của đồng bào vùng Hồ Ba Bể là thuyền gì?", "a": "Thuyền độc mộc"},
            # Lượt 2
            {"q": "5 km 20 m bằng bao nhiêu mét?", "a": "5 020 m"},
            {"q": "3 tạ 5 yến bằng bao nhiêu ki-lô-gam?", "a": "350 kg"},
            {"q": "Phân số thập phân 7/100 viết dưới dạng số thập phân là gì?", "a": "0,07"},
            {"q": "Số 0,001 đọc là gì?", "a": "Không phẩy không không một (một phần nghìn)"},
            {"q": "Một hình vuông có chu vi 36 cm, diện tích hình vuông đó là bao nhiêu cm²?", "a": "81 cm²"},
            {"q": "Một hình chữ nhật có chu vi 40 cm, chiều dài 12 cm. Chiều rộng là bao nhiêu cm?", "a": "8 cm"},
            {"q": "Hồ Ba Bể nằm ở trung tâm của Vườn quốc gia nào?", "a": "Vườn quốc gia Ba Bể"},
            {"q": "Đảo nhỏ giữa lòng Hồ Ba Bể gắn liền với truyền thuyết dân gian là đảo gì?", "a": "Đảo Bà Góa"},
            {"q": "Phần nguyên của số thập phân 15,24 là số nào?", "a": "15"},
            {"q": "Phần thập phân của số thập phân 8,75 là phần nào?", "a": "75 phần trăm"},
            # Lượt 3
            {"q": "7 m² 25 dm² bằng bao nhiêu đề-xi-mét vuông?", "a": "725 dm²"},
            {"q": "2 thế kỷ bằng bao nhiêu năm?", "a": "200 năm"},
            {"q": "Phân số thập phân 35/1000 viết dưới dạng số thập phân là gì?", "a": "0,035"},
            {"q": "Số gồm 5 đơn vị và 6 phần mười viết là gì?", "a": "5,6"},
            {"q": "Số gồm 0 đơn vị và 8 phần trăm viết là gì?", "a": "0,08"},
            {"q": "Hình thoi có độ dài hai đường chéo là 6 cm và 8 cm có diện tích là bao nhiêu cm²?", "a": "24 cm²"},
            {"q": "Loài cá đặc sản trứ danh thường được phơi khô hoặc nướng pác ngòi ở Hồ Ba Bể là gì?", "a": "Cá mương (cá tép dầu)"},
            {"q": "Thác nước hùng vĩ bắt nguồn từ sông Năng đổ vào gần Hồ Ba Bể là thác gì?", "a": "Thác Đầu Đẳng"},
            {"q": "Viết số thập phân gồm 24 đơn vị và 5 phần mười, 3 phần trăm", "a": "24,53"},
            {"q": "1 kg bằng bao nhiêu gam?", "a": "1 000 g"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Khu vực nuôi cá đặc sản ven Hồ Ba Bể hình bình hành có độ dài đáy 45 m, chiều cao tương ứng 20 m. Diện tích khu vực đó là ... m².", "a": "900"},
            {"q": "Một chiếc thuyền máy chở khách quanh 3 nhánh Hồ Ba Bể xuất phát lúc 8 giờ 15 phút và về bến lúc 10 giờ. Thuyền đã đi trong ... phút.", "a": "105"},
            {"q": "Đội thuyền độc mộc đón 64 du khách tham quan Đảo Bà Góa. Mỗi thuyền chở 4 du khách. Cần ít nhất ... lượt thuyền độc mộc để chở hết số khách.", "a": "16"},
            {"q": "Bác thợ rèn làm hàng rào hoa sắt hình thoi có cạnh dài 15 dm. Chu vi của khung sắt hình thoi đó là ... dm.", "a": "60"},
            # Lượt 2
            {"q": "Bà con vùng Hồ Ba Bể thu hoạch cá mương phơi khô: đợt 1 được 1 tạ 20 kg cá, đợt 2 được 80 kg cá. Cả hai đợt thu hoạch được tất cả ... kg cá khô.", "a": "200"},
            {"q": "Một con đường ven Hồ Ba Bể dài 1 km 200 m. Người ta trồng cây hai bên đường, cứ cách 10 m trồng 1 cây (cả 2 đầu đều trồng). Số cây cần trồng ở một bên đường là ... cây.", "a": "121"},
            {"q": "Một mảnh đất trồng rau cạnh Hồ Ba Bể hình chữ nhật có nửa chu vi là 36 m, chiều rộng kém chiều dài 8 m. Diện tích mảnh đất là ... m².", "a": "308"},
            {"q": "Một can dầu phục vụ thuyền du lịch có 20 lít dầu, mỗi chuyến đi quanh hồ tiêu thụ hết 2,5 lít dầu. Can dầu đó đủ chạy cho ... chuyến.", "a": "8"},
            # Lượt 3
            {"q": "Một tấm lưới quây cá trên Hồ Ba Bể hình chữ nhật có chu vi 180 m, chiều dài gấp đôi chiều rộng. Chiều dài tấm lưới là ... m.", "a": "60"},
            {"q": "Một đoàn khách mua 5 gói trà hoa vàng Ba Bể hết 600 000 đồng. Một đoàn khác mua 8 gói cùng loại hết tất cả ... đồng.", "a": "960000 (hoặc 960 000)"},
            {"q": "Tìm số tự nhiên x, biết: 4,5 < x < 5,8. Giá trị của x là ...", "a": "5"},
            {"q": "Một chiếc thuyền độc mộc dài 4 m 5 dm. Đổi chiều dài thuyền sang đơn vị mét dưới dạng số thập phân là ... m.", "a": "4,5"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Xung quanh một hồ nước nhỏ ven Hồ Ba Bể hình tròn khép kín có chu vi 360 m, người ta trồng cây liễu, cứ cách 9 m trồng một cây. Hỏi trồng được tất cả bao nhiêu cây liễu xung quanh hồ?\nA. 39 cây\nB. 40 cây\nC. 41 cây\nD. 42 cây",
                "ans_str": "B. 40 cây (Chu vi khép kín nên số cây bằng số khoảng cách: 360 : 9 = 40 cây)"
            },
            {
                "q": "Một đoàn 42 du khách thuê 9 chiếc thuyền tham quan Hồ Ba Bể gồm hai loại: thuyền lớn chở 6 người và thuyền nhỏ chở 4 người. Biết các thuyền đều chở đủ số người theo quy định. Hỏi có bao nhiêu chiếc thuyền lớn?\nA. 3 chiếc\nB. 4 chiếc\nC. 5 chiếc\nD. 6 chiếc",
                "ans_str": "A. 3 chiếc (Giả sử cả 9 thuyền đều là thuyền nhỏ: 9 × 4 = 36 người. Hụt đi: 42 - 36 = 6 người. Mỗi thuyền lớn hơn thuyền nhỏ: 6 - 4 = 2 người. Số thuyền lớn là: 6 : 2 = 3 chiếc)"
            },
            # Lượt 2
            {
                "q": "Một thửa ruộng hình chữ nhật ven Hồ Ba Bể nếu tăng chiều rộng thêm 4 m thì diện tích tăng thêm 160 m². Biết chiều dài gấp 2 lần chiều rộng ban đầu. Tính diện tích ban đầu của thửa ruộng.\nA. 800 m²\nB. 600 m²\nC. 750 m²\nD. 900 m²",
                "ans_str": "A. 800 m² (Chiều rộng tăng 4 m thì diện tích tăng là hình chữ nhật có chiều rộng 4 m và chiều dài bằng chiều dài ban đầu. Chiều dài ban đầu là: 160 : 4 = 40 (m). Chiều rộng ban đầu là: 40 : 2 = 20 (m). Diện tích ban đầu của thửa ruộng là: 40 × 20 = 800 (m²))"
            },
            {
                "q": "Tìm một số thập phân biết rằng nếu dời dấu phẩy của số đó sang bên phải một chữ số thì ta được số mới lớn hơn số phải tìm là 40,5 đơn vị.\nA. 4,5\nB. 4,05\nC. 0,45\nD. 45",
                "ans_str": "A. 4,5 (Dời dấu phẩy sang phải một chữ số thì số đó gấp lên 10 lần. Hiệu số phần bằng nhau: 10 - 1 = 9 phần. Số phải tìm là: 40,5 : 9 = 4,5)"
            },
            # Lượt 3
            {
                "q": "Một sân phơi cá mương hình chữ nhật có chu vi ban đầu là 48 m, chiều dài gấp 3 lần chiều rộng. Tính diện tích ban đầu của sân phơi đó.\nA. 108 m²\nB. 75 m²\nC. 147 m²\nD. 192 m²",
                "ans_str": "A. 108 m² (Nửa chu vi sân phơi là: 48 : 2 = 24 (m). Tổng số phần bằng nhau: 1 + 3 = 4 (phần). Chiều rộng sân phơi là: 24 : 4 = 6 (m). Chiều dài sân phơi là: 6 × 3 = 18 (m). Diện tích ban đầu của sân phơi là: 18 × 6 = 108 (m²))"
            },
            {
                "q": "Tổng của hai số tự nhiên là 1 025. Nếu viết thêm chữ số 2 vào bên phải số bé thì được số lớn. Tìm số lớn.\nA. 932\nB. 922\nC. 912\nD. 952",
                "ans_str": "A. 932 (Gọi số bé là a thì số lớn là a × 10 + 2. Tổng: a + a × 10 + 2 = 1 025 => 11 × a = 1 023 => a = 93. Số lớn là 932)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 5: RUỘNG BẬC THANG MÙ CANG CHẢI (YÊN BÁI) - TUẦN 5
    # =========================================================================
    {
        "tuan": 5,
        "tram_so": 5,
        "ten_tram": "Ruộng bậc thang Mù Cang Chải (Yên Bái)",
        "chu_de": "Khái niệm số thập phân (tiếp), So sánh các số thập phân, Viết số đo đại lượng dưới dạng STP",
        "v1": [
            # Lượt 1
            {"q": "Trong số thập phân 85,346, chữ số 3 thuộc hàng nào?", "a": "Hàng phần mười"},
            {"q": "Trong số thập phân 12,485, chữ số 8 có giá trị là bao nhiêu?", "a": "8/100 (hoặc 0,08)"},
            {"q": "Viết phân số 3/10 dưới dạng số thập phân", "a": "0,3"},
            {"q": "Viết phân số 45/100 dưới dạng số thập phân", "a": "0,45"},
            {"q": "So sánh hai số thập phân: 4,5 và 4,49", "a": "4,5 > 4,49"},
            {"q": "Đèo hiểm trở và ngoạn mục bậc nhất nối vào Mù Cang Chải là đèo gì?", "a": "Đèo Khau Phạ"},
            {"q": "Địa danh đồi ruộng bậc thang hình tròn đẹp nổi tiếng bậc nhất ở Mù Cang Chải là gì?", "a": "Đồi Mâm Xôi"},
            {"q": "Giống gạo nếp nương thơm dẻo trứ danh của vùng thung lũng Tú Lệ là gì?", "a": "Nếp nương Tú Lệ"},
            {"q": "Số tự nhiên liền trước của số thập phân 9,25 là số nào?", "a": "9"},
            {"q": "Số tự nhiên liền sau của số thập phân 9,25 là số nào?", "a": "10"},
            # Lượt 2
            {"q": "Trong số thập phân 234,567, chữ số 7 thuộc hàng nào?", "a": "Hàng phần nghìn"},
            {"q": "Số thập phân gồm 5 chục, 3 đơn vị, 6 phần mười và 2 phần trăm viết là gì?", "a": "53,62"},
            {"q": "Viết số thập phân bằng 0,7 nhưng có 2 chữ số ở phần thập phân", "a": "0,70"},
            {"q": "So sánh hai số thập phân: 12,08 và 12,1", "a": "12,08 < 12,1"},
            {"q": "Sắp xếp theo thứ tự từ bé đến lớn: 3,45; 3,54; 3,4; 3,5", "a": "3,4; 3,45; 3,5; 3,54"},
            {"q": "Môn thể thao mạo hiểm lượn trên bầu trời ngắm Mù Cang Chải mùa lúa chín là gì?", "a": "Dù lượn"},
            {"q": "Đồi ruộng bậc thang có hình móng vuốt kỳ vĩ ở Sáng Nhù tên là gì?", "a": "Đồi Móng Ngựa"},
            {"q": "Viết hỗn số 4 7/10 thành số thập phân", "a": "4,7"},
            {"q": "Viết hỗn số 2 15/100 thành số thập phân", "a": "2,15"},
            {"q": "Tìm chữ số x, biết: 8,3x > 8,38", "a": "x = 9"},
            # Lượt 3
            {"q": "Viết số đo 5 m 4 dm dưới dạng số thập phân có đơn vị mét", "a": "5,4 m"},
            {"q": "Viết số đo 3 m 25 cm dưới dạng số thập phân có đơn vị mét", "a": "3,25 m"},
            {"q": "Viết số đo 2 kg 50 g dưới dạng số thập phân có đơn vị ki-lô-gam", "a": "2,05 kg"},
            {"q": "Trong số 7,925, giá trị của chữ số 2 là bao nhiêu?", "a": "2/100 (hoặc 0,02)"},
            {"q": "So sánh hai số thập phân: 0,9 và 0,899", "a": "0,9 > 0,899"},
            {"q": "Đỉnh đèo Khau Phạ có độ cao khoảng bao nhiêu mét so với mực nước biển?", "a": "1 200 m đến 1 500 m"},
            {"q": "Ruộng bậc thang Mù Cang Chải được công nhận là Di tích cấp gì?", "a": "Di tích Quốc gia đặc biệt"},
            {"q": "Chuyển phân số 3/5 thành số thập phân", "a": "0,6"},
            {"q": "Chuyển phân số 7/4 thành số thập phân", "a": "1,75"},
            {"q": "Số thập phân bé nhất có hai chữ số khác nhau ở phần thập phân với phần nguyên là 0", "a": "0,12"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một thửa ruộng bậc thang hình chữ nhật ở Đồi Mâm Xôi có chiều dài 25 m, chiều rộng 12,4 m. Chu vi thửa ruộng đó là ... m.", "a": "74,8"},
            {"q": "Viết số đo khối lượng hạt lúa nếp Tú Lệ 4 tấn 250 kg dưới dạng số thập phân có đơn vị tấn là ... tấn.", "a": "4,25"},
            {"q": "Tìm số tự nhiên x lớn nhất thỏa mãn: x < 7,85. Giá trị của x là ...", "a": "7"},
            {"q": "Bà con người Mông gặt lúa nương: buổi sáng gặt được 1,2 ha, buổi chiều gặt được nhiều hơn buổi sáng 0,4 ha. Cả ngày gặt được tất cả ... ha.", "a": "2,8"},
            # Lượt 2
            {"q": "Một vận động viên bay dù lượn từ đỉnh đèo Khau Phạ xuống thung lũng lượn 3 vòng hết 0,75 giờ. Đổi 0,75 giờ ra phút là ... phút.", "a": "45"},
            {"q": "Viết số đo độ dài đoạn đường dốc lên Đồi Móng Ngựa dài 3 km 80 m dưới dạng số thập phân với đơn vị ki-lô-mét là ... km.", "a": "3,08"},
            {"q": "Tìm chữ số x thích hợp điền vào chỗ chấm: 5,64 < 5,6x < 5,66. Giá trị của x là ...", "a": "5"},
            {"q": "Một túi cốm Tú Lệ cân nặng 1 kg 500 g. Ba túi cốm như thế cân nặng tất cả ... kg.", "a": "4,5"},
            # Lượt 3
            {"q": "Thửa ruộng bậc thang thứ nhất thu được 2,4 tấn thóc, thửa thứ hai thu được 3,1 tấn thóc, thửa thứ ba thu được 2,9 tấn thóc. Trung bình mỗi thửa thu được ... tấn thóc.", "a": "2,8"},
            {"q": "Tìm số tự nhiên y bé nhất thỏa mãn: y > 15,38. Giá trị của y là ...", "a": "16"},
            {"q": "Đổi số đo diện tích một thửa ruộng nhỏ 450 m² sang đề-ca-mét vuông (dam²) được ... dam².", "a": "4,5"},
            {"q": "Một đoàn phượt thủ đi xe máy qua đèo Khau Phạ dài 32 km hết 40 phút. Vận tốc trung bình của đoàn xe là ... km/giờ.", "a": "48"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Tìm số thập phân x có hai chữ số ở phần thập phân sao cho: 0,8 < x < 0,9 và tổng các chữ số của phần thập phân bằng 12.\nA. 0,84\nB. 0,85\nC. 0,86\nD. 0,87",
                "ans_str": "A. 0,84 (Vì 0,8 < 0,8x < 0,9 nên chữ số hàng phần mười là 8. Tổng các chữ số phần thập phân bằng 12 nên chữ số hàng phần trăm là: 12 - 8 = 4. Vậy số đó là 0,84)"
            },
            {
                "q": "Từ 4 chữ số 0; 2; 5; 7, lập được bao nhiêu số thập phân có đủ 4 chữ số trên mà phần thập phân có 2 chữ số?\nA. 12 số\nB. 18 số\nC. 24 số\nD. 16 số",
                "ans_str": "B. 18 số (Số có dạng a,bc hoặc ab,cd. Cụ thể có 2 chữ số ở phần thập phân nên dạng là ab,cd. Chữ số a có 3 cách chọn (khác 0); b có 3 cách chọn; c có 2 cách chọn; d có 1 cách chọn. Số lượng: 3 × 3 × 2 × 1 = 18 số)"
            },
            # Lượt 2
            {
                "q": "Khi viết một số thập phân, một học sinh đã quên mất dấu phẩy nên được số tự nhiên gấp 100 lần số ban đầu. Biết hiệu giữa số mới và số ban đầu là 198. Tìm số thập phân ban đầu.\nA. 2\nB. 1,98\nC. 2,02\nD. 2,2",
                "ans_str": "A. 2 (Số mới gấp 100 lần số ban đầu. Hiệu số phần: 100 - 1 = 99 phần. Số ban đầu là: 198 : 99 = 2 (hoặc 2,00))"
            },
            {
                "q": "Một thửa ruộng bậc thang hình thang có đáy lớn 40 m, đáy bé 24 m. Nếu kéo dài đáy lớn thêm 5 m thì diện tích tăng thêm 45 m². Tính diện tích ban đầu của thửa ruộng hình thang đó.\nA. 576 m²\nB. 480 m²\nC. 640 m²\nD. 540 m²",
                "ans_str": "A. 576 m² (Phần tăng thêm là tam giác có đáy 5 m, diện tích 45 m² -> Chiều cao hình thang là: 45 × 2 : 5 = 18 m. Diện tích ban đầu: (40 + 24) × 18 : 2 = 64 × 9 = 576 m²)"
            },
            # Lượt 3
            {
                "q": "Cho dãy số thập phân cách đều: 1,1; 1,3; 1,5; 1,7; ... ; 4,9. Dãy số này có bao nhiêu số hạng?\nA. 19 số hạng\nB. 20 số hạng\nC. 21 số hạng\nD. 25 số hạng",
                "ans_str": "B. 20 số hạng (Khoảng cách giữa hai số liên tiếp là: 1,3 - 1,1 = 0,2. Số số hạng là: (4,9 - 1,1) : 0,2 + 1 = 3,8 : 0,2 + 1 = 19 + 1 = 20 số hạng)"
            },
            {
                "q": "Tổng của ba số là 202,5. Biết số thứ nhất gấp 2 lần số thứ hai, số thứ hai gấp 3 lần số thứ ba. Tìm số thứ nhất.\nA. 135\nB. 121,5\nC. 145\nD. 120",
                "ans_str": "B. 121,5 (Coi số thứ ba là 1 phần thì số thứ hai là 3 phần, số thứ nhất là 3 × 2 = 6 phần. Tổng số phần: 1 + 3 + 6 = 10 phần. 1 phần là: 202,5 : 10 = 20,25. Số thứ nhất là: 20,25 × 6 = 121,5)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 6: ĐỈNH FANSIPAN (LÀO CAI) - TUẦN 6
    # =========================================================================
    {
        "tuan": 6,
        "tram_so": 6,
        "ten_tram": "Đỉnh Fansipan (Lào Cai)",
        "chu_de": "Viết số đo đại lượng dưới dạng số thập phân (tiếp), Làm tròn số thập phân, Luyện tập chung",
        "v1": [
            # Lượt 1
            {"q": "Làm tròn số thập phân 4,7 đến hàng đơn vị được số nào?", "a": "5"},
            {"q": "Làm tròn số thập phân 12,34 đến hàng phần mười được số nào?", "a": "12,3"},
            {"q": "Làm tròn số thập phân 8,468 đến hàng phần trăm được số nào?", "a": "8,47"},
            {"q": "Viết số đo 4 m² 8 dm² dưới dạng số thập phân có đơn vị mét vuông", "a": "4,08 m²"},
            {"q": "Viết số đo 5 tấn 6 tạ dưới dạng số thập phân có đơn vị tấn", "a": "5,6 tấn"},
            {"q": "Đỉnh Fansipan được mệnh danh là nóc nhà của khu vực nào?", "a": "Nóc nhà Đông Dương"},
            {"q": "Độ cao chính xác của đỉnh Fansipan là bao nhiêu mét?", "a": "3 143 m"},
            {"q": "Hệ thống cáp treo Fansipan giữ kỷ lục Guinness cáp treo ba dây có chiều dài khoảng bao nhiêu mét?", "a": "Khoảng 6 292,5 m"},
            {"q": "Thung lũng tuyệt đẹp dưới chân đỉnh Fansipan nơi tàu hỏa leo núi chạy qua là gì?", "a": "Thung lũng Mường Hoa"},
            {"q": "Làm tròn số 3 143 đến hàng trăm được số nào?", "a": "3 100"},
            # Lượt 2
            {"q": "Làm tròn số thập phân 9,25 đến hàng phần mười được số nào?", "a": "9,3"},
            {"q": "Làm tròn số thập phân 25,614 đến hàng phần trăm được số nào?", "a": "25,61"},
            {"q": "Làm tròn số 19,85 đến hàng đơn vị được số nào?", "a": "20"},
            {"q": "Viết số đo 8 ha dưới dạng ki-lô-mét vuông", "a": "0,08 km²"},
            {"q": "Viết số đo 7 km 50 m dưới dạng số thập phân có đơn vị ki-lô-mét", "a": "7,05 km"},
            {"q": "Loài hoa rừng biểu tượng bung nở rực rỡ trên đỉnh Fansipan vào mùa xuân là hoa gì?", "a": "Hoa đỗ quyên"},
            {"q": "Thị xã du lịch nổi tiếng sương mù dưới chân núi Fansipan là gì?", "a": "Sa Pa"},
            {"q": "Làm tròn số nhiệt độ trên đỉnh Fansipan mùa đông là -2,6 °C đến hàng đơn vị", "a": "-3 °C"},
            {"q": "Viết phân số 1/4 dưới dạng số thập phân", "a": "0,25"},
            {"q": "Viết phân số 3/8 dưới dạng số thập phân", "a": "0,375"},
            # Lượt 3
            {"q": "Làm tròn số 150,49 đến hàng đơn vị được số nào?", "a": "150"},
            {"q": "Làm tròn số 3,1415 đến hàng phần trăm được số nào?", "a": "3,14"},
            {"q": "Làm tròn số 0,996 đến hàng phần trăm được số nào?", "a": "1,00 (hoặc 1)"},
            {"q": "Viết số đo 6 m 5 cm dưới dạng số thập phân có đơn vị mét", "a": "6,05 m"},
            {"q": "Viết số đo 3 tấn 15 kg dưới dạng số thập phân có đơn vị tấn", "a": "3,015 tấn"},
            {"q": "Đỉnh Fansipan thuộc dãy núi hùng vĩ nào của nước ta?", "a": "Dãy Hoàng Liên Sơn"},
            {"q": "Bậc thang đá từ ga cáp treo lên đỉnh Fansipan có bao nhiêu bậc?", "a": "600 bậc đá"},
            {"q": "Viết số đo 25 dm² dưới dạng số thập phân có đơn vị mét vuông", "a": "0,25 m²"},
            {"q": "Một ngày trên đỉnh Fansipan thường trải qua mấy mùa trong năm?", "a": "4 mùa"},
            {"q": "So sánh: 3,143 km và 3 143 m", "a": "Bằng nhau (=)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Chiều dài tuyến cáp treo Fansipan là 6 292,5 m. Đổi chiều dài này ra ki-lô-mét và làm tròn đến hàng phần mười ta được ... km.", "a": "6,3"},
            {"q": "Một cabin cáp treo Fansipan chở được tối đa 35 khách. Cần ít nhất ... cabin để chở hết đoàn 180 du khách lên đỉnh núi.", "a": "6"},
            {"q": "Giá vé cáp treo Fansipan cho người lớn là 800 000 đồng, trẻ em là 550 000 đồng. Một gia đình gồm 2 người lớn và 2 trẻ em phải trả tổng cộng ... đồng.", "a": "2700000 (hoặc 2 700 000)"},
            {"q": "Tàu hỏa leo núi Mường Hoa đi từ Sa Pa đến ga cáp treo dài 2 km hết 6 phút. Vận tốc của tàu hỏa leo núi là ... km/giờ.", "a": "20"},
            # Lượt 2
            {"q": "Nhiệt độ đo được tại đỉnh Fansipan lúc 6 giờ sáng là 3,4 °C, đến 12 giờ trưa tăng thêm 4,8 °C. Nhiệt độ trưa hôm đó tại đỉnh núi là ... °C.", "a": "8,2"},
            {"q": "Làm tròn số thập phân 45,785 đến hàng phần mười được kết quả là ...", "a": "45,8"},
            {"q": "Để leo 600 bậc đá lên đỉnh Fansipan, bạn Nam bước trung bình 40 bậc mỗi phút. Bạn Nam lên tới đỉnh sau ... phút.", "a": "15"},
            {"q": "Một cuộn cáp treo bằng thép nặng 15 tấn 400 kg. Đổi khối lượng cuộn cáp sang tấn dưới dạng số thập phân là ... tấn.", "a": "15,4"},
            # Lượt 3
            {"q": "Đỉnh đèo Ô Quy Hồ gần Fansipan nằm ở độ cao 2 073 m. Viết độ cao này theo đơn vị ki-lô-mét dưới dạng số thập phân là ... km.", "a": "2,073"},
            {"q": "Một nhóm thám hiểm leo bộ Fansipan trong 2 ngày: ngày thứ nhất leo được 14,5 km; ngày thứ hai leo ít hơn ngày thứ nhất 3,2 km. Cả hai ngày nhóm leo được ... km.", "a": "25,8"},
            {"q": "Tìm số tự nhiên a lớn nhất thỏa mãn: làm tròn a,48 đến hàng đơn vị được kết quả bằng 18. Giá trị của a là ...", "a": "18"},
            {"q": "Một vườn hoa đỗ quyên hình vuông có diện tích 400 m². Chu vi của vườn hoa đó là ... m.", "a": "80"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Khi làm tròn một số thập phân X có hai chữ số ở phần thập phân đến hàng phần mười, ta được kết quả là 8,5. Hỏi giá trị lớn nhất có thể của số thập phân X là bao nhiêu?\nA. 8,54\nB. 8,55\nC. 8,59\nD. 8,49",
                "ans_str": "A. 8,54 (Để làm tròn đến hàng phần mười được 8,5 thì chữ số hàng phần trăm phải từ 0 đến 4 nếu phần mười là 5, tức là từ 8,50 đến 8,54. Giá trị lớn nhất là 8,54)"
            },
            {
                "q": "Một đoàn 120 học sinh tham quan Fansipan. Công ty du lịch có chương trình ưu đãi: cứ mua 10 vé được tặng 1 vé miễn phí. Biết giá mỗi vé là 150 000 đồng. Hỏi nhà trường phải trả tất cả bao nhiêu tiền vé?\nA. 16 500 000 đồng\nB. 18 000 000 đồng\nC. 16 350 000 đồng\nD. 15 000 000 đồng",
                "ans_str": "A. 16 500 000 đồng (Mỗi nhóm 11 người nhận được 11 vé (10 vé mua + 1 vé tặng). Ta có: 120 : 11 = 10 (nhóm) dư 10 bạn. Số vé được tặng là: 10 × 1 = 10 (vé). Số vé phải mua trả tiền là: 120 - 10 = 110 (vé). Số tiền nhà trường phải trả là: 110 × 150 000 = 16 500 000 (đồng))"
            },
            # Lượt 2
            {
                "q": "Trên đường leo núi Fansipan, có một cây cầu treo dây văng. Người ta đếm được 51 cột mốc cách đều nhau 4 m từ đầu cầu đến cuối cầu. Hỏi cây cầu treo đó dài bao nhiêu mét?\nA. 204 m\nB. 200 m\nC. 196 m\nD. 208 m",
                "ans_str": "B. 200 m (Có 51 cột mốc thì có: 51 - 1 = 50 khoảng cách. Chiều dài cầu là: 50 × 4 = 200 m)"
            },
            {
                "q": "Một cửa hàng đặc sản Sa Pa bán nấm hương với giá 360 000 đồng/kg thì được lãi 20% so với giá bán. Hỏi cửa hàng đó lãi bao nhiêu phần trăm so với giá vốn?\nA. 20%\nB. 25%\nC. 15%\nD. 30%",
                "ans_str": "B. 25% (Tiền lãi: 360 000 × 20% = 72 000 đồng. Giá vốn: 360 000 - 72 000 = 288 000 đồng. Tỉ số phần trăm lãi so với vốn: 72 000 : 288 000 = 0,25 = 25%)"
            },
            # Lượt 3
            {
                "q": "Một cabin cáp treo đi từ chân núi lên đỉnh Fansipan với vận tốc 8 m/giây, cabin đối diện đi từ đỉnh xuống chân núi với vận tốc 6 m/giây. Tuyến cáp dài 6 300 m. Hỏi sau bao lâu hai cabin gặp nhau nếu xuất phát cùng lúc?\nA. 7 phút 30 giây (450 giây)\nB. 8 phút\nC. 6 phút 45 giây\nD. 9 phút",
                "ans_str": "A. 7 phút 30 giây (450 giây) (Mỗi giây cả hai cabin đi được: 8 + 6 = 14 m. Thời gian gặp nhau: 6 300 : 14 = 450 giây = 7 phút 30 giây)"
            },
            {
                "q": "Cho số thập phân A. Nếu dời dấu phẩy của số A sang bên trái một chữ số ta được số B; dời dấu phẩy sang bên phải một chữ số ta được số C. Biết A + B + C = 359,64. Tìm số A.\nA. 32,4\nB. 3,24\nC. 324\nD. 35,4",
                "ans_str": "A. 32,4 (Ta có: B = A : 10; C = A × 10. Tổng B + A + C = 0,1 × A + A + 10 × A = 11,1 × A = 359,64 => A = 359,64 : 11,1 = 32,4)"
            }
        ]
    }
]
