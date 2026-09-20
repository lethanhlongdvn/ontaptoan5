# -*- coding: utf-8 -*-
"""
Dữ liệu ngân hàng câu hỏi Tuần 13 đến Tuần 18 (Trạm 13 - 18)
Mỗi trạm chuẩn 48 câu hỏi:
- Vòng 1: 30 câu ghép đôi (10 câu/lượt x 3 lượt)
- Vòng 2: 12 câu điền số thực tế (4 câu/lượt x 3 lượt)
- Vòng 3: 6 câu trắc nghiệm Mức 3 (2 câu/lượt x 3 lượt)
"""

TUAN_13_TO_18 = [
    # =========================================================================
    # TRẠM 13: VQG PHONG NHA - KẺ BÀNG (QUẢNG BÌNH) - TUẦN 13
    # =========================================================================
    {
        "tuan": 13,
        "tram_so": 13,
        "ten_tram": "VQG Phong Nha - Kẻ Bàng (Quảng Bình)",
        "chu_de": "Hình thang, diện tích hình thang, diện tích hình tam giác",
        "v1": [
            # Lượt 1
            {"q": "Hình thang là hình tứ giác có đặc điểm gì?", "a": "Có một cặp cạnh đối diện song song"},
            {"q": "Hai cạnh song song của hình thang được gọi là gì?", "a": "Hai đáy (đáy lớn và đáy bé)"},
            {"q": "Đoạn thẳng vuông góc nối giữa hai đáy của hình thang gọi là gì?", "a": "Chiều cao của hình thang"},
            {"q": "Công thức tính diện tích hình thang có hai đáy a, b và chiều cao h là gì?", "a": "S = ((a + b) × h) : 2"},
            {"q": "Hình thang có một góc vuông được gọi là hình gì?", "a": "Hình thang vuông"},
            {"q": "Hang động tự nhiên lớn nhất thế giới nằm trong VQG Phong Nha - Kẻ Bàng là hang gì?", "a": "Hang Sơn Đoòng"},
            {"q": "Động khô dài nhất châu Á với hệ thống thạch nhũ lung linh ở Quảng Bình là động gì?", "a": "Động Thiên Đường"},
            {"q": "Dòng sông xanh ngọc bích nơi thuyền chở du khách vào Động Phong Nha là sông gì?", "a": "Sông Son"},
            {"q": "Tính diện tích hình thang có hai đáy 6 cm và 4 cm, chiều cao 5 cm", "a": "25 cm²"},
            {"q": "Trung bình cộng hai đáy của hình thang bằng gì?", "a": "(a + b) : 2"},
            # Lượt 2
            {"q": "Hình thang có hai cạnh bên bằng nhau và hai góc kề một đáy bằng nhau là hình gì?", "a": "Hình thang cân"},
            {"q": "Tính diện tích hình thang có đáy lớn 8 m, đáy bé 5 m và chiều cao 4 m", "a": "26 m²"},
            {"q": "Nếu giữ nguyên hai đáy của hình thang và gấp chiều cao lên 2 lần thì diện tích thay đổi thế nào?", "a": "Gấp lên 2 lần"},
            {"q": "Diện tích hình thang bằng tích của trung bình cộng hai đáy với cái gì?", "a": "Chiều cao"},
            {"q": "Một hình thang có diện tích 40 cm², chiều cao 5 cm. Tổng độ dài hai đáy là bao nhiêu cm?", "a": "16 cm (40 × 2 : 5 = 16)"},
            {"q": "Hang Sơn Đoòng có chiều dài ước tính khoảng bao nhiêu ki-lô-mét?", "a": "Hơn 9 km"},
            {"q": "Vòm hang Sơn Đoòng lớn tới mức có thể chứa được một tòa nhà cao bao nhiêu tầng?", "a": "Tòa nhà 40 tầng"},
            {"q": "Bức tường thạch nhũ khổng lồ cao gần 90 m bên trong hang Sơn Đoòng được gọi là gì?", "a": "Bức tường Việt Nam"},
            {"q": "Tính diện tích hình thang vuông có hai đáy 10 cm và 6 cm, cạnh bên vuông góc dài 4 cm", "a": "32 cm²"},
            {"q": "Muốn tính chiều cao hình thang khi biết diện tích và hai đáy ta làm thế nào?", "a": "h = (S × 2) : (a + b)"},
            # Lượt 3
            {"q": "Tính diện tích hình thang có hai đáy 1,2 m và 0,8 m, chiều cao 0,5 m", "a": "0,5 m²"},
            {"q": "Một hình thang có tổng hai đáy là 24 cm và chiều cao là 7 cm. Diện tích là bao nhiêu cm²?", "a": "84 cm²"},
            {"q": "Nếu đáy lớn và đáy bé cùng gấp 2 lần, chiều cao giữ nguyên thì diện tích hình thang thay đổi thế nào?", "a": "Gấp lên 2 lần"},
            {"q": "Hai cạnh bên của hình thang không song song cắt nhau tại đâu?", "a": "Tại một điểm ngoài hình thang"},
            {"q": "Động Phong Nha nổi tiếng với mấy tiêu chí nhất thế giới do Hoàng gia Anh bình chọn?", "a": "7 tiêu chí nhất"},
            {"q": "Người đầu tiên phát hiện ra lối vào hang Sơn Đoòng năm 1991 là ai?", "a": "Ông Hồ Khanh (người dân địa phương)"},
            {"q": "Hệ thống hang động Phong Nha - Kẻ Bàng được kiến tạo trong vùng núi đá vôi (Karst) bao nhiêu triệu năm?", "a": "Hơn 400 triệu năm"},
            {"q": "Tính trung bình cộng hai đáy hình thang biết diện tích là 50 m² và chiều cao 5 m", "a": "10 m"},
            {"q": "Tính diện tích hình tam giác có đáy 12 cm và chiều cao 7 cm", "a": "42 cm²"},
            {"q": "Đổi 0,8 ha sang mét vuông", "a": "8 000 m²"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một mảnh đất hình thang lối vào Động Thiên Đường có đáy lớn 35 m, đáy bé 25 m và chiều cao 18 m. Diện tích mảnh đất đó là ... m².", "a": "540"},
            {"q": "Một chiếc thuyền chở khách ngược dòng sông Son vào Động Phong Nha dài 6 km hết 45 phút. Vận tốc thuyền ngược dòng là ... km/giờ.", "a": "8"},
            {"q": "Thửa ruộng hình thang có đáy lớn 40 m, đáy bé bằng 3/4 đáy lớn, chiều cao 16 m. Diện tích thửa ruộng là ... m².", "a": "560"},
            {"q": "Tìm x, biết: (x + 8) × 5 : 2 = 45. Giá trị của x là ...", "a": "10"},
            # Lượt 2
            {"q": "Cầu thang gỗ phục vụ du khách khám phá Động Thiên Đường dài 1 000 m. Một du khách đi với vận tốc trung bình 40 m/phút. Du khách đi hết cầu thang sau ... phút.", "a": "25"},
            {"q": "Một bồn hoa hình thang có diện tích 36 m², chiều cao 4,5 m. Tổng độ dài hai đáy của bồn hoa đó là ... m.", "a": "16"},
            {"q": "Một đoàn thám hiểm Sơn Đoòng có 10 người, mỗi người mang theo 12,5 kg hành lý. Tổng khối lượng hành lý của cả đoàn là ... kg.", "a": "125"},
            {"q": "Tính giá trị biểu thức: (15,4 + 9,6) × 8,5 : 2. Kết quả là ...", "a": "106,25"},
            # Lượt 3
            {"q": "Một thửa đất hình thang vuông có đáy bé 15 m, đáy lớn 25 m và cạnh bên vuông góc với đáy dài 12 m. Diện tích thửa đất là ... m².", "a": "240"},
            {"q": "Một hố sụt trong hang Sơn Đoòng có thảm rừng nguyên sinh hình tam giác với đáy 120 m và chiều cao 65 m. Diện tích thảm rừng là ... m².", "a": "3900"},
            {"q": "Tìm chiều cao của hình thang có diện tích 150 m², đáy lớn 22 m và đáy bé 18 m. Chiều cao là ... m.", "a": "7,5"},
            {"q": "Đội tuần tra VQG Phong Nha đi bộ kiểm tra rừng: ngày thứ nhất đi được 14,2 km; ngày thứ hai đi được 16,8 km. Trung bình mỗi ngày đội đi được ... km.", "a": "15,5"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một thửa ruộng hình thang có đáy lớn 45 m, đáy bé 30 m. Nếu mở rộng đáy lớn thêm 5 m thì diện tích thửa ruộng tăng thêm 40 m². Tính diện tích thửa ruộng hình thang ban đầu.\nA. 600 m²\nB. 560 m²\nC. 640 m²\nD. 720 m²",
                "ans_str": "A. 600 m² (Phần tăng thêm là tam giác có đáy 5 m, diện tích 40 m². Chiều cao hình thang là: 40 × 2 : 5 = 16 m. Diện tích ban đầu: (45 + 30) × 16 : 2 = 75 × 8 = 600 m²)"
            },
            {
                "q": "Một đoàn thám hiểm hang Sơn Đoòng gồm 12 người vượt qua vách đá cao bằng dây thừng. Mỗi người leo mất trung bình 15 phút, sau mỗi lần leo phải nghỉ ngơi kiểm tra an toàn 5 phút rồi người tiếp theo mới bắt đầu. Hỏi người cuối cùng leo xong vách đá sau bao lâu?\nA. 3 giờ 55 phút (235 phút)\nB. 4 giờ\nC. 3 giờ 40 phút\nD. 4 giờ 15 phút",
                "ans_str": "A. 3 giờ 55 phút (235 phút) (12 người leo thì có 12 lượt leo và 11 lần nghỉ kiểm tra. Tổng thời gian: 12 × 15 + 11 × 5 = 180 + 55 = 235 phút = 3 giờ 55 phút)"
            },
            # Lượt 2
            {
                "q": "Một hình thang có đáy bé bằng 2/3 đáy lớn và chiều cao là 12 m. Biết diện tích hình thang là 180 m². Tính độ dài đáy lớn của hình thang đó.\nA. 18 m\nB. 12 m\nC. 24 m\nD. 15 m",
                "ans_str": "A. 18 m (Tổng hai đáy: 180 × 2 : 12 = 30 m. Tổng số phần bằng nhau: 2 + 3 = 5 phần. Đáy lớn là: 30 : 5 × 3 = 18 m)"
            },
            {
                "q": "Một thửa ruộng hình thang có diện tích 450 m², chiều cao 15 m. Nếu đáy lớn giảm đi 4 m và đáy bé tăng thêm 4 m thì diện tích thửa ruộng mới sẽ như thế nào so với diện tích ban đầu?\nA. Không đổi\nB. Tăng 30 m²\nC. Giảm 30 m²\nD. Tăng 60 m²",
                "ans_str": "A. Không đổi (Tổng hai đáy: (a - 4) + (b + 4) = a + b, tổng hai đáy không đổi và chiều cao giữ nguyên nên diện tích không đổi)"
            },
            # Lượt 3
            {
                "q": "Cho hình thang ABCD có đáy nhỏ AB = 10 cm, đáy lớn CD = 20 cm. Chiều cao hình thang là 12 cm. Hai đường chéo AC và BD cắt nhau tại O. Tính diện tích tam giác AOB.\nA. 20 cm²\nB. 25 cm²\nC. 30 cm²\nD. 15 cm²",
                "ans_str": "A. 20 cm² (Diện tích hình thang ABCD là: (10 + 20) × 12 : 2 = 180 (cm²). Tỉ số đáy AB/CD = 10/20 = 1/2 nên tỉ số diện tích tam giác S(AOB)/S(BOC) = 1/2 và OA/OC = 1/2. Khi đó S(AOB) chiếm 1 phần thì S(BOC) = S(AOD) = 2 phần, S(COD) = 4 phần. Tổng số phần bằng nhau: 1 + 2 + 2 + 4 = 9 (phần). Diện tích tam giác AOB là: 180 : 9 × 1 = 20 (cm²))"
            },
            {
                "q": "Một thuyền máy du lịch xuôi dòng từ bến sông Son đến cửa hang Phong Nha mất 20 phút, và chạy ngược dòng từ cửa hang về bến mất 30 phút. Biết vận tốc dòng nước là 2 km/giờ. Tính chiều dài quãng đường sông đó.\nA. 4 km\nB. 6 km\nC. 5 km\nD. 4,5 km",
                "ans_str": "A. 4 km (20 phút = 1/3 giờ; 30 phút = 1/2 giờ. Tỉ số thời gian xuôi/ngược = (1/3)/(1/2) = 2/3 => Tỉ số vận tốc xuôi/ngược = 3/2. Hiệu vận tốc = 2 lần vận tốc dòng nước = 2 × 2 = 4 km/giờ. Vận tốc xuôi dòng = 4 : (3 - 2) × 3 = 12 km/giờ. Quãng đường = 12 × 1/3 = 4 km)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 14: THÀNH CỔ QUẢNG TRỊ, CẦU HIỀN LƯƠNG & SÔNG BẾN HẢI - TUẦN 14
    # =========================================================================
    {
        "tuan": 14,
        "tram_so": 14,
        "ten_tram": "Thành cổ Quảng Trị, Cầu Hiền Lương & Sông Bến Hải",
        "chu_de": "Đường tròn, hình tròn, chu vi và diện tích hình tròn",
        "v1": [
            # Lượt 1
            {"q": "Đoạn thẳng nối từ tâm đến một điểm trên đường tròn gọi là gì?", "a": "Bán kính của hình tròn"},
            {"q": "Đoạn thẳng đi qua tâm và nối hai điểm trên đường tròn gọi là gì?", "a": "Đường kính của hình tròn"},
            {"q": "Đường kính gấp mấy lần bán kính?", "a": "Gấp 2 lần (d = 2 × r)"},
            {"q": "Công thức tính chu vi hình tròn theo bán kính r là gì?", "a": "C = r × 2 × 3,14"},
            {"q": "Công thức tính chu vi hình tròn theo đường kính d là gì?", "a": "C = d × 3,14"},
            {"q": "Cuộc chiến đấu bảo vệ Thành cổ Quảng Trị mùa hè đỏ lửa năm 1972 diễn ra trong bao nhiêu ngày đêm?", "a": "81 ngày đêm"},
            {"q": "Dòng sông lịch sử chảy qua thị xã Quảng Trị nơi thả hoa đăng tri ân các anh hùng liệt sĩ là sông gì?", "a": "Sông Thạch Hãn"},
            {"q": "Cây cầu lịch sử bắc qua sông Bến Hải từng chia cắt hai miền Nam - Bắc đất nước suốt 20 năm là cầu gì?", "a": "Cầu Hiền Lương"},
            {"q": "Tính chu vi hình tròn có bán kính r = 5 cm", "a": "31,4 cm"},
            {"q": "Tính chu vi hình tròn có đường kính d = 10 cm", "a": "31,4 cm"},
            # Lượt 2
            {"q": "Công thức tính diện tích hình tròn có bán kính r là gì?", "a": "S = r × r × 3,14"},
            {"q": "Tính diện tích hình tròn có bán kính r = 2 cm", "a": "12,56 cm²"},
            {"q": "Nếu gấp bán kính của hình tròn lên 2 lần thì chu vi tăng gấp mấy lần?", "a": "Gấp 2 lần"},
            {"q": "Nếu gấp bán kính của hình tròn lên 2 lần thì diện tích tăng gấp mấy lần?", "a": "Gấp 4 lần (2 × 2 = 4)"},
            {"q": "Tính bán kính hình tròn có chu vi là 18,84 cm", "a": "3 cm (18,84 : 3,14 : 2 = 3)"},
            {"q": "Vĩ tuyến nào đi qua dòng sông Bến Hải chia cắt hai miền đất nước theo hiệp định Giơ-ne-vơ 1954?", "a": "Vĩ tuyến 17"},
            {"q": "Chiều dài cây cầu Hiền Lương lịch sử là bao nhiêu mét?", "a": "Khoảng 178 m"},
            {"q": "Đài tưởng niệm trung tâm Thành cổ Quảng Trị được thiết kế theo hình gì tượng trưng cho nấm mồ chung?", "a": "Hình bát giác (nồi hương khổng lồ)"},
            {"q": "Tính diện tích hình tròn có bán kính r = 10 cm", "a": "314 cm²"},
            {"q": "Tính chu vi hình tròn có bán kính r = 1 m", "a": "6,28 m"},
            # Lượt 3
            {"q": "Tính diện tích hình tròn có đường kính d = 4 cm", "a": "12,56 cm² (r = 2 cm)"},
            {"q": "Tính diện tích hình tròn có bán kính r = 1 cm", "a": "3,14 cm²"},
            {"q": "Nếu gấp đường kính lên 3 lần thì diện tích hình tròn tăng gấp mấy lần?", "a": "Gấp 9 lần (3 × 3 = 9)"},
            {"q": "Một hình tròn có diện tích 28,26 cm². Bán kính của hình tròn đó là bao nhiêu cm?", "a": "3 cm (3 × 3 × 3,14 = 28,26)"},
            {"q": "Nửa chu vi hình tròn có bán kính r được tính như thế nào?", "a": "r × 3,14"},
            {"q": "Địa đạo Vịnh Mốc huyền thoại trong lòng đất nằm ở huyện nào tỉnh Quảng Trị?", "a": "Huyện Vĩnh Linh"},
            {"q": "Nghĩa trang quốc gia lớn nhất cả nước quy tập hài cốt các liệt sĩ Trường Sơn tại Quảng Trị là nghĩa trang nào?", "a": "Nghĩa trang Liệt sĩ Quốc gia Trường Sơn"},
            {"q": "Tính chu vi bánh xe rùa có đường kính 0,65 m", "a": "2,041 m"},
            {"q": "Tính diện tích nửa hình tròn có bán kính r = 2 cm", "a": "6,28 cm²"},
            {"q": "Đổi 2,5 giờ sang phút", "a": "150 phút"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một bồn hoa hình tròn trong khuôn viên Thành cổ Quảng Trị có bán kính 3 m. Diện tích bồn hoa đó là ... m² (lấy pi = 3,14).", "a": "28,26"},
            {"q": "Bánh xe đạp của một học sinh qua Cầu Hiền Lương có đường kính 0,6 m. Chu vi của bánh xe đạp đó là ... m.", "a": "1,884"},
            {"q": "Một chiếc đèn hoa đăng hình tròn thả trên sông Thạch Hãn có chu vi 94,2 cm. Bán kính của chiếc đèn đó là ... cm.", "a": "15"},
            {"q": "Thành cổ Quảng Trị có chu vi tường thành dạng hình vuông dài 2 160 m. Độ dài mỗi cạnh của tường thành là ... m.", "a": "540"},
            # Lượt 2
            {"q": "Bánh xe ô tô chở đoàn viếng di tích có bán kính 0,35 m. Khi bánh xe lăn được 1 000 vòng thì ô tô đã đi được quãng đường dài ... m.", "a": "2198 (hoặc 2 198)"},
            {"q": "Một biển báo giao thông hình tròn đặt tại đầu cầu Hiền Lương có đường kính 50 cm. Diện tích biển báo đó là ... cm².", "a": "1962,5"},
            {"q": "Tìm bán kính của một hình tròn có diện tích bằng 50,24 cm². Bán kính là ... cm.", "a": "4"},
            {"q": "Người ta cắm cờ giải phóng hai bên lan can cầu Hiền Lương dài 178 m, cứ cách 2 m cắm một lá cờ (cả 2 đầu cầu đều cắm). Số lá cờ ở một bên cầu là ... lá cờ.", "a": "90"},
            # Lượt 3
            {"q": "Một hồ nước hình tròn trong công viên Hòa Bình Quảng Trị có đường kính 20 m. Chu vi bờ hồ nước đó là ... m.", "a": "62,8"},
            {"q": "Tính diện tích một mặt bàn tròn có chu vi 12,56 dm. Diện tích mặt bàn tròn đó là ... dm².", "a": "12,56"},
            {"q": "Một bánh xe lăn được 100 vòng đi được quãng đường 188,4 m. Bán kính của bánh xe đó là ... m.", "a": "0,3"},
            {"q": "Một khu đất hình chữ nhật có chiều dài 35 m, chiều rộng 20 m. Người ta đào một giếng nước hình tròn bán kính 2 m. Diện tích đất còn lại là ... m².", "a": "687,44"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một bồn hoa hình tròn ở Thành cổ Quảng Trị có bán kính 4 m. Người ta làm một lối đi xung quanh bồn hoa đó rộng 1 m. Tính diện tích của lối đi xung quanh bồn hoa đó (lấy pi = 3,14).\nA. 28,26 m²\nB. 31,4 m²\nC. 25,12 m²\nD. 21,98 m²",
                "ans_str": "A. 28,26 m² (Bán kính hình tròn lớn cả lối đi là: 4 + 1 = 5 m. Diện tích hình tròn lớn: 5 × 5 × 3,14 = 78,5 m². Diện tích bồn hoa nhỏ: 4 × 4 × 3,14 = 50,24 m². Diện tích lối đi: 78,5 - 50,24 = 28,26 m²)"
            },
            {
                "q": "Một bánh xe đạp có bán kính 0,325 m (đường kính 0,65 m). Người đi xe đạp qua Cầu Hiền Lương dài 178 m và đoạn đường tiếp nối, đếm được bánh xe lăn đúng 400 vòng. Hỏi người đó đã đi được quãng đường dài bao nhiêu mét?\nA. 816,4 m\nB. 753,6 m\nC. 800 m\nD. 820 m",
                "ans_str": "A. 816,4 m (Chu vi bánh xe: 0,65 × 3,14 = 2,041 m. Quãng đường xe đi được: 2,041 × 400 = 816,4 m)"
            },
            # Lượt 2
            {
                "q": "Hai hình tròn có hiệu hai bán kính là 3 cm. Biết tỉ số chu vi của hai hình tròn đó là 2/3. Tính bán kính của hình tròn lớn.\nA. 9 cm\nB. 6 cm\nC. 12 cm\nD. 15 cm",
                "ans_str": "A. 9 cm (Tỉ số chu vi bằng tỉ số bán kính = 2/3. Hiệu số phần: 3 - 2 = 1 phần tương ứng 3 cm. Bán kính hình tròn lớn là: 3 × 3 = 9 cm)"
            },
            {
                "q": "Cho hình vuông ABCD có cạnh dài 8 cm. Vẽ hình tròn nội tiếp tiếp xúc với 4 cạnh của hình vuông. Tính diện tích phần hình vuông nằm ngoài hình tròn.\nA. 13,76 cm²\nB. 14,5 cm²\nC. 16 cm²\nD. 12,56 cm²",
                "ans_str": "A. 13,76 cm² (Bán kính hình tròn nội tiếp là: 8 : 2 = 4 cm. Diện tích hình vuông: 8 × 8 = 64 cm². Diện tích hình tròn: 4 × 4 × 3,14 = 50,24 cm². Diện tích phần nằm ngoài: 64 - 50,24 = 13,76 cm²)"
            },
            # Lượt 3
            {
                "q": "Nếu tăng bán kính của một hình tròn thêm 10% thì diện tích của hình tròn đó tăng thêm bao nhiêu phần trăm?\nA. 21%\nB. 20%\nC. 10%\nD. 11%",
                "ans_str": "A. 21% (Bán kính mới = 110% = 1,1 bán kính cũ. Diện tích mới = 1,1 × 1,1 = 1,21 = 121% diện tích cũ. Diện tích tăng thêm: 121% - 100% = 21%)"
            },
            {
                "q": "Một máy bơm nước trên sông Bến Hải tưới đồng ruộng có vòi phun xoay tròn với bán kính tưới xa tối đa 10 m. Tính diện tích mặt ruộng tối đa mà vòi nước có thể tưới tới.\nA. 314 m²\nB. 628 m²\nC. 157 m²\nD. 31,4 m²",
                "ans_str": "A. 314 m² (Diện tích bề mặt tưới là hình tròn bán kính 10 m: S = 10 × 10 × 3,14 = 314 m²)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 15: QUẦN THỂ DI TÍCH CỐ ĐÔ HUẾ (THỪA THIÊN HUẾ) - TUẦN 15
    # =========================================================================
    {
        "tuan": 15,
        "tram_so": 15,
        "ten_tram": "Quần thể Di tích Cố đô Huế (Thừa Thiên Huế)",
        "chu_de": "Chu vi và diện tích hình tròn (tiếp), hình phẳng phức hợp, ôn tập số thập phân",
        "v1": [
            # Lượt 1
            {"q": "Một nửa hình tròn có bán kính r = 4 cm có diện tích là bao nhiêu?", "a": "25,12 cm² (4 × 4 × 3,14 : 2 = 25,12)"},
            {"q": "Hình quạt tròn 1/4 hình tròn có diện tích bằng diện tích hình tròn chia cho mấy?", "a": "Chia cho 4"},
            {"q": "Một mặt bàn tròn Cố đô có bán kính 0,5 m. Diện tích mặt bàn là bao nhiêu?", "a": "0,785 m²"},
            {"q": "Tính chu vi hình tròn có bán kính 0,5 m", "a": "3,14 m"},
            {"q": "Số thập phân 0,125 viết dưới dạng phân số tối giản là gì?", "a": "1/8"},
            {"q": "Cố đô Huế từng là kinh đô của triều đại phong kiến cuối cùng nào ở nước ta?", "a": "Triều nhà Nguyễn (1802 - 1945)"},
            {"q": "Cây cầu biểu tượng soi bóng dòng sông Hương thơ mộng ở xứ Huế là cầu gì?", "a": "Cầu Tràng Tiền (cầu Tiền Trường)"},
            {"q": "Cầu Tràng Tiền nổi tiếng trong ca dao với bao nhiêu vài và bao nhiêu nhịp?", "a": "6 vài 12 nhịp"},
            {"q": "Tháp Phước Duyên cổ kính tại Chùa Thiên Mụ có bao nhiêu tầng?", "a": "7 tầng"},
            {"q": "Tính nhẩm: 4,5 × 0,4", "a": "1,8"},
            # Lượt 2
            {"q": "Tính diện tích hình tròn có đường kính d = 6 dm", "a": "28,26 dm² (r = 3 dm)"},
            {"q": "Tính chu vi hình tròn có đường kính d = 2 dm", "a": "6,28 dm"},
            {"q": "Muốn tính diện tích hình phẳng phức hợp ghép từ hình chữ nhật và 2 nửa hình tròn ta làm thế nào?", "a": "Cộng diện tích hình chữ nhật với diện tích một hình tròn"},
            {"q": "Tính giá trị biểu thức: 12,5 × 4 - 3,5 × 4", "a": "36"},
            {"q": "Tìm x, biết: x : 2,5 = 4", "a": "x = 10"},
            {"q": "Cửa ngõ chính vào Hoàng thành Huế phía trước có Kỳ Đài gọi là gì?", "a": "Ngọ Môn"},
            {"q": "Dòng sông thơ mộng êm đềm chảy qua trung tâm thành phố Huế là sông gì?", "a": "Sông Hương"},
            {"q": "Di sản phi vật thể đại diện của nhân loại được bảo tồn tại Cố đô Huế là gì?", "a": "Nhã nhạc cung đình Huế"},
            {"q": "Lăng tẩm của vị vua nào có kiến trúc độc đáo kết hợp Á - Âu bằng sành sứ?", "a": "Lăng Khải Định"},
            {"q": "Tính nhẩm: 0,75 : 0,25", "a": "3"},
            # Lượt 3
            {"q": "Tính diện tích hình tròn có bán kính r = 3 cm", "a": "28,26 cm²"},
            {"q": "Chu vi hình tròn tăng lên mấy lần khi đường kính tăng lên 3 lần?", "a": "Gấp 3 lần"},
            {"q": "Diện tích hình tròn tăng lên mấy lần khi bán kính tăng lên 4 lần?", "a": "Gấp 16 lần"},
            {"q": "Tính chu vi nửa hình tròn có đường kính 4 cm (kể cả đường kính)", "a": "10,28 cm (4 × 3,14 : 2 + 4 = 10,28)"},
            {"q": "Số thập phân gồm 8 đơn vị và 5 phần trăm viết là gì?", "a": "8,05"},
            {"q": "Lăng tẩm mang phong cách hài hòa non nước thiên nhiên bậc nhất xứ Huế là lăng nào?", "a": "Lăng Tự Đức (Khiêm Lăng)"},
            {"q": "Món chè cung đình nổi tiếng với hương sen bọc hạt sen xứ Huế là gì?", "a": "Chè hạt sen long nhãn"},
            {"q": "Kỳ Đài Huế (cột cờ trước Ngọ Môn) cao bao nhiêu tầng đài xây bằng gạch vôi?", "a": "3 tầng đài"},
            {"q": "Tính nhanh: 3,7 × 2,5 × 4", "a": "37"},
            {"q": "Tìm số tự nhiên y, biết: 4,8 < y < 5,2", "a": "y = 5"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Cầu Tràng Tiền (Huế) dài 402,6 m gồm 6 vài. Độ dài trung bình của mỗi vài cầu là ... m.", "a": "67,1"},
            {"q": "Hồ Tịnh Tâm trong Hoàng thành Huế hình chữ nhật có chiều dài 200 m, chiều rộng 150 m. Diện tích mặt nước hồ sen là ... ha.", "a": "3"},
            {"q": "Một chiếc nón bài thơ xứ Huế có vành đáy hình tròn đường kính 40 cm. Chu vi của vành nón là ... cm.", "a": "125,6"},
            {"q": "Một đoàn ca Huế trên sông Hương biểu diễn trên thuyền rồng từ 19 giờ 30 phút đến 21 giờ. Buổi biểu diễn kéo dài ... phút.", "a": "90"},
            # Lượt 2
            {"q": "Sân Điện Thái Hòa hình chữ nhật có kích thước 60 m và 40 m. Người ta dùng 1/8 diện tích làm lối đi lễ. Diện tích lối đi là ... m².", "a": "300"},
            {"q": "Một chiếc gương cung đình hình tròn có diện tích 78,5 dm². Bán kính của chiếc gương đó là ... dm.", "a": "5"},
            {"q": "Mua 5 hộp mè xửng đặc sản Huế hết 175 000 đồng. Mua 8 hộp mè xửng như thế hết tất cả ... đồng.", "a": "280000 (hoặc 280 000)"},
            {"q": "Tìm x, biết: x × 3,14 = 31,4. Giá trị của x là ...", "a": "10"},
            # Lượt 3
            {"q": "Một bồn hoa cung đình gồm một hình chữ nhật dài 6 m, rộng 4 m và hai nửa hình tròn gắn ở hai đầu chiều rộng. Diện tích bồn hoa đó là ... m² (lấy pi = 3,14).", "a": "36,56 (24 + 4 × 3,14 = 36,56)"},
            {"q": "Một chiếc xe xích lô chở khách du lịch quanh Đại Nội Huế có bánh xe sau đường kính 0,7 m. Khi bánh xe lăn được 500 vòng thì xích lô đã đi được ... m.", "a": "1099"},
            {"q": "Tính giá trị biểu thức: (45,8 - 25,8) × 3,14 : 2. Kết quả là ...", "a": "31,4"},
            {"q": "Một can dầu tràm Huế chứa 5 lít dầu cân nặng 4,5 kg. Mười can dầu như thế cân nặng tất cả ... kg.", "a": "45"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một sân khấu biểu diễn Nhã nhạc cung đình Huế gồm một hình vuông có cạnh 10 m và 4 nửa hình tròn có đường kính là 4 cạnh hình vuông đó nằm phía ngoài. Tính tổng diện tích của cả sân khấu (lấy pi = 3,14).\nA. 257 m²\nB. 157 m²\nC. 214 m²\nD. 314 m²",
                "ans_str": "A. 257 m² (Diện tích hình vuông là: 10 × 10 = 100 m². Bốn nửa hình tròn ghép thành 2 hình tròn có đường kính 10 m (bán kính r = 5 m). Tổng diện tích 4 nửa hình tròn là: 2 × (5 × 5 × 3,14) = 157 m². Tổng diện tích sân khấu: 100 + 157 = 257 m²)"
            },
            {
                "q": "Một bồn hoa hình vuông cạnh 6 m. Ở chính giữa bồn hoa người ta xây một hồ nước hình tròn tiếp xúc với 4 cạnh của hình vuông. Tính diện tích phần đất trồng hoa còn lại xung quanh hồ nước.\nA. 7,74 m²\nB. 8,25 m²\nC. 6,84 m²\nD. 9,14 m²",
                "ans_str": "A. 7,74 m² (Bán kính hồ nước hình tròn: 6 : 2 = 3 m. Diện tích hình vuông: 6 × 6 = 36 m². Diện tích hồ nước: 3 × 3 × 3,14 = 28,26 m². Diện tích phần trồng hoa còn lại: 36 - 28,26 = 7,74 m²)"
            },
            # Lượt 2
            {
                "q": "Một chiếc thuyền rồng du lịch chở khách trên sông Hương xuôi dòng từ chùa Thiên Mụ về chợ Đông Ba dài 5 km hết 15 phút, và ngược dòng từ chợ Đông Ba về chùa Thiên Mụ mất 25 phút. Tính vận tốc của dòng nước trên sông Hương.\nA. 4 km/giờ\nB. 2 km/giờ\nC. 3 km/giờ\nD. 5 km/giờ",
                "ans_str": "A. 4 km/giờ (15 phút = 0,25 giờ; 25 phút = 5/12 giờ. Vận tốc xuôi dòng: 5 : 0,25 = 20 km/giờ. Vận tốc ngược dòng: 5 : (5/12) = 12 km/giờ. Vận tốc dòng nước: (20 - 12) : 2 = 4 km/giờ)"
            },
            {
                "q": "Cho hai hình tròn đồng tâm O. Bán kính hình tròn lớn là 6 cm, bán kính hình tròn nhỏ là 4 cm. Tính diện tích phần hình vành khăn nằm giữa hai hình tròn đó (lấy pi = 3,14).\nA. 62,8 cm²\nB. 31,4 cm²\nC. 50,24 cm²\nD. 78,5 cm²",
                "ans_str": "A. 62,8 cm² (Diện tích hình tròn lớn: 6 × 6 × 3,14 = 113,04 cm². Diện tích hình tròn nhỏ: 4 × 4 × 3,14 = 50,24 cm². Diện tích hình vành khăn: 113,04 - 50,24 = 62,8 cm²)"
            },
            # Lượt 3
            {
                "q": "Tìm hai số thập phân có tổng là 49,5 và biết rằng nếu dời dấu phẩy của số bé sang bên phải một chữ số thì được số lớn.\nA. 4,5 và 45\nB. 5,5 và 44\nC. 4,95 và 44,55\nD. 3,5 và 46",
                "ans_str": "A. 4,5 và 45 (Dời dấu phẩy sang phải 1 chữ số tức là số lớn gấp 10 lần số bé. Tổng số phần bằng nhau: 10 + 1 = 11 phần. Số bé là: 49,5 : 11 = 4,5; Số lớn là: 4,5 × 10 = 45)"
            },
            {
                "q": "Một người nghệ nhân thêu tranh xứ Huế dự định hoàn thành một bức tranh thêu Cố đô trong 15 ngày. Do cải tiến kỹ thuật, mỗi ngày người đó thêu thêm được 20% định mức ban đầu. Hỏi người nghệ nhân hoàn thành bức tranh đó trong bao nhiêu ngày?\nA. 12,5 ngày (12 ngày rưỡi)\nB. 12 ngày\nC. 13 ngày\nD. 10 ngày",
                "ans_str": "A. 12,5 ngày (Mỗi ngày thêu được 120% = 1,2 định mức. Thời gian hoàn thành là: 15 : 1,2 = 12,5 ngày)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 16: CẦU RỒNG & NGŨ HÀNH SƠN (ĐÀ NẴNG) - TUẦN 16
    # =========================================================================
    {
        "tuan": 16,
        "tram_so": 16,
        "ten_tram": "Cầu Rồng & Ngũ Hành Sơn (Đà Nẵng)",
        "chu_de": "Ôn tập số thập phân (tiếp), ôn tập các phép tính với số thập phân (+, -, ×, :), biểu thức",
        "v1": [
            # Lượt 1
            {"q": "Tính kết quả phép tính: 24,5 + 15,7 - 10,2", "a": "30"},
            {"q": "Tính kết quả phép tính: 3,5 × 4 : 2", "a": "7"},
            {"q": "Cây cầu hình rồng thép bắc qua sông Hàn có khả năng phun lửa và phun nước là cầu gì?", "a": "Cầu Rồng (Đà Nẵng)"},
            {"q": "Chiều dài tổng thể của Cầu Rồng Đà Nẵng là bao nhiêu mét?", "a": "666 m"},
            {"q": "Danh thắng Ngũ Hành Sơn gồm 5 ngọn núi đá vôi mang tên theo thuyết ngũ hành nào?", "a": "Kim, Mộc, Thủy, Hỏa, Thổ"},
            {"q": "Ngọn núi lớn nhất và đẹp nhất trong quần thể Ngũ Hành Sơn là ngọn núi nào?", "a": "Thủy Sơn"},
            {"q": "Tượng Phật Bà Quan Âm cao nhất Việt Nam (67 m) ngự tại ngôi chùa nào ở bán đảo Sơn Trà?", "a": "Chùa Linh Ứng (Bãi Bụt)"},
            {"q": "Tính nhẩm: 15 : 0,5", "a": "30"},
            {"q": "Tính nhẩm: 4,8 × 0,25", "a": "1,2 (4,8 : 4 = 1,2)"},
            {"q": "Tìm x, biết: x + 4,8 = 12", "a": "x = 7,2"},
            # Lượt 2
            {"q": "Tính kết quả phép tính: 100 - (24,5 + 35,5)", "a": "40"},
            {"q": "Tính kết quả phép tính: 1,2 × (3,4 + 6,6)", "a": "12"},
            {"q": "Cầu Rồng thường trình diễn phun lửa và phun nước vào những tối nào trong tuần?", "a": "Thứ Bảy và Chủ Nhật"},
            {"q": "Bãi biển quyến rũ hàng đầu hành tinh tại Đà Nẵng do tạp chí Forbes bình chọn là biển nào?", "a": "Bãi biển Mỹ Khê"},
            {"q": "Làng nghề đá mỹ nghệ truyền thống hàng trăm năm dưới chân núi Ngũ Hành Sơn là làng gì?", "a": "Làng đá mỹ nghệ Non Nước"},
            {"q": "Đỉnh núi cao nhất bán đảo Sơn Trà nơi có bàn cờ đá ông tiên là đỉnh gì?", "a": "Đỉnh Bàn Cờ"},
            {"q": "Tính giá trị biểu thức: 45,6 : 3 + 5,4 : 3", "a": "17 ((45,6 + 5,4) : 3 = 17)"},
            {"q": "Tính giá trị biểu thức: 2,5 × 7,8 × 4", "a": "78"},
            {"q": "Tìm y, biết: y × 4 = 18,4", "a": "y = 4,6"},
            {"q": "Tính nhẩm: 0,36 : 0,09", "a": "4"},
            # Lượt 3
            {"q": "Tính kết quả: 0,8 × 0,5 × 0,2", "a": "0,08"},
            {"q": "Tính kết quả: 54 : 4,5", "a": "12"},
            {"q": "Tính kết quả: 15,5 × 2 + 15,5 × 8", "a": "155"},
            {"q": "Tìm x, biết: x : 1,2 = 5", "a": "x = 6"},
            {"q": "Cây cầu quay duy nhất ở Việt Nam bắc qua sông Hàn tại Đà Nẵng là cầu gì?", "a": "Cầu sông Hàn"},
            {"q": "Cây cầu đi bộ nổi tiếng hình đôi bàn tay khổng lồ trên đỉnh Bà Nà là cầu gì?", "a": "Cầu Vàng (Golden Bridge)"},
            {"q": "Động đá huyền ảo lớn nhất trên đỉnh Thủy Sơn là động gì?", "a": "Động Huyền Không"},
            {"q": "Tính nhanh: 1,25 × 16", "a": "20 (1,25 × 8 × 2 = 20)"},
            {"q": "Một ngày có 24 giờ, 1,5 ngày bằng bao nhiêu giờ?", "a": "36 giờ"},
            {"q": "Tìm số tự nhiên liền sau của số 99,99", "a": "100"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Cầu Rồng dài 666 m, mặt cầu rộng 37,5 m. Diện tích mặt Cầu Rồng là ... m².", "a": "24975"},
            {"q": "Một vòi rồng phun nước trên cầu trong 3 phút phun được 4,5 m³ nước. Trong 5 phút vòi phun được ... m³ nước.", "a": "7,5"},
            {"q": "Tìm x, biết: (x + 3,5) × 4 = 30. Giá trị của x là ...", "a": "4"},
            {"q": "Một nhóm du khách leo thang máy lên đỉnh Thủy Sơn (Ngũ Hành Sơn) cao 43 m với vận tốc 1,25 m/giây. Thời gian thang máy chạy là ... giây (làm tròn số thập phân).", "a": "34,4"},
            # Lượt 2
            {"q": "Một cơ sở điêu khắc đá Non Nước tạc 5 pho tượng đá hết 12,5 ngày. Để tạc 8 pho tượng cùng loại như thế cần ... ngày (năng suất như nhau).", "a": "20"},
            {"q": "Một chiếc cano du lịch trên sông Hàn chạy 18 km hết 0,45 giờ. Vận tốc của cano là ... km/giờ.", "a": "40"},
            {"q": "Tính giá trị biểu thức: 48,6 : 3,6 + 1,5 × 4. Kết quả là ...", "a": "19,5"},
            {"q": "Tìm y, biết: 85,5 - y : 2 = 70. Giá trị của y là ...", "a": "31"},
            # Lượt 3
            {"q": "Đoàn xe 6 chiếc chở 270 du khách từ sân bay Đà Nẵng đi bán đảo Sơn Trà. Trung bình mỗi xe chở ... hành khách.", "a": "45"},
            {"q": "Một mảnh sân hình chữ nhật cạnh bờ biển Mỹ Khê có chu vi 120 m, chiều dài hơn chiều rộng 12 m. Diện tích mảnh sân là ... m².", "a": "864"},
            {"q": "Một bể cá cảnh nước mặn tại Đà Nẵng có chiều dài 2,5 m; chiều rộng 1,2 m và mực nước sâu 0,8 m. Lượng nước trong bể là ... m³.", "a": "2,4"},
            {"q": "Tính nhanh giá trị biểu thức: 3,75 × 12 - 3,75 × 2. Kết quả là ...", "a": "37,5"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một cano du lịch chạy trên sông Hàn xuôi dòng từ Cầu Rồng đến cửa biển dài 12 km hết 24 phút, và chạy ngược dòng về lại Cầu Rồng hết 40 phút. Tính vận tốc dòng nước trên sông Hàn.\nA. 6 km/giờ\nB. 5 km/giờ\nC. 4 km/giờ\nD. 3 km/giờ",
                "ans_str": "A. 6 km/giờ (24 phút = 0,4 giờ; 40 phút = 2/3 giờ. Vận tốc xuôi dòng: 12 : 0,4 = 30 km/giờ. Vận tốc ngược dòng: 12 : (2/3) = 18 km/giờ. Vận tốc dòng nước: (30 - 18) : 2 = 6 km/giờ)"
            },
            {
                "q": "Tìm số thập phân X có hai chữ số ở phần thập phân, biết rằng nếu lấy X nhân với 4 rồi trừ đi 4,5 thì bằng X nhân với 2 cộng thêm 5,5.\nA. 5\nB. 4,5\nC. 5,2\nD. 4,8",
                "ans_str": "A. 5 (Ta có: 4X - 4,5 = 2X + 5,5 => 2X = 10 => X = 5 (hoặc 5,00))"
            },
            # Lượt 2
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = (13,75 × 4 - 27,5 × 2) × (1/2 + 1/4 + 1/8 + 1/16)\nA. 0\nB. 1\nC. 15/16\nD. 27,5",
                "ans_str": "A. 0 (Ta có: 13,75 × 4 = 55; 27,5 × 2 = 55. Do đó ngoặc thứ nhất bằng: 55 - 55 = 0. Vậy tích A = 0)"
            },
            {
                "q": "Hai người thợ đá mỹ nghệ Non Nước cùng làm chung một tác phẩm đá thì sau 6 ngày sẽ hoàn thành. Nếu người thứ nhất làm một mình thì phải mất 10 ngày mới xong. Hỏi nếu người thứ hai làm một mình thì mất bao nhiêu ngày mới xong?\nA. 15 ngày\nB. 12 ngày\nC. 14 ngày\nD. 18 ngày",
                "ans_str": "A. 15 ngày (Mỗi ngày cả 2 người làm 1/6 công việc; người thứ nhất làm 1/10 công việc. Mỗi ngày người thứ hai làm: 1/6 - 1/10 = 1/15 công việc. Vậy người thứ hai làm một mình mất 15 ngày)"
            },
            # Lượt 3
            {
                "q": "Một mảnh đất hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Nếu giảm chiều dài đi 4 m và tăng chiều rộng thêm 4 m thì diện tích tăng thêm 96 m². Tính diện tích ban đầu của mảnh đất.\nA. 588 m²\nB. 648 m²\nC. 768 m²\nD. 540 m²",
                "ans_str": "A. 588 m² (Gọi chiều rộng là r thì chiều dài là 3 × r. Khi giảm dài 4 m và tăng rộng 4 m, diện tích mới là: (3 × r - 4) × (r + 4) = 3 × r × r + 8 × r - 16. Diện tích tăng thêm là: 8 × r - 16 = 96 => 8 × r = 112 => r = 14 (m). Chiều dài ban đầu là: 14 × 3 = 42 (m). Diện tích ban đầu của mảnh đất là: 42 × 14 = 588 (m²))"
            },
            {
                "q": "Trong một bãi đỗ xe du lịch tại Ngũ Hành Sơn có tất cả 40 chiếc xe gồm xe ô tô con 4 bánh và xe khách lớn 6 bánh. Bác bảo vệ đếm được tất cả 190 bánh xe. Hỏi có bao nhiêu chiếc xe khách loại 6 bánh?\nA. 15 chiếc\nB. 25 chiếc\nC. 20 chiếc\nD. 18 chiếc",
                "ans_str": "A. 15 chiếc (Giả sử cả 40 xe đều là ô tô con 4 bánh: 40 × 4 = 160 bánh. Số bánh thiếu: 190 - 160 = 30 bánh. Mỗi xe khách 6 bánh nhiều hơn xe con: 6 - 4 = 2 bánh. Số xe khách 6 bánh là: 30 : 2 = 15 chiếc)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 17: PHỐ CỔ HỘI AN (QUẢNG NAM) - TUẦN 17
    # =========================================================================
    {
        "tuan": 17,
        "tram_so": 17,
        "ten_tram": "Phố cổ Hội An (Quảng Nam)",
        "chu_de": "Hệ thống hóa các hình phẳng, ôn tập diện tích và chu vi hình phẳng, toán thực tế",
        "v1": [
            # Lượt 1
            {"q": "Hình nào có 4 cạnh bằng nhau và 4 góc vuông?", "a": "Hình vuông"},
            {"q": "Hình nào có 2 cặp cạnh đối diện song song và bằng nhau, 4 góc vuông?", "a": "Hình chữ nhật"},
            {"q": "Hình nào có 2 cặp cạnh đối diện song song và bằng nhau nhưng không bắt buộc góc vuông?", "a": "Hình bình hành"},
            {"q": "Hình nào có 4 cạnh bằng nhau và hai đường chéo vuông góc với nhau?", "a": "Hình thoi"},
            {"q": "Công thức tính diện tích hình thoi có hai đường chéo d1 và d2 là gì?", "a": "S = (d1 × d2) : 2"},
            {"q": "Công trình kiến trúc biểu tượng trên tờ tiền 20.000 đồng tại Phố cổ Hội An là gì?", "a": "Chùa Cầu (Cầu Nhật Bản)"},
            {"q": "Dòng sông êm đềm chảy qua trung tâm phố cổ Hội An nơi du khách thả hoa đăng là sông gì?", "a": "Sông Hoài (nhánh sông Thu Bồn)"},
            {"q": "Vật phẩm trang trí lung linh rực rỡ đặc trưng khắp các con phố Hội An về đêm là gì?", "a": "Đèn lồng Hội An"},
            {"q": "Làng nghề rau truyền thống xanh tươi nổi tiếng ven phố cổ Hội An là làng gì?", "a": "Làng rau Trà Quế"},
            {"q": "Tính diện tích hình thoi có độ dài hai đường chéo là 8 cm và 10 cm", "a": "40 cm²"},
            # Lượt 2
            {"q": "Hình nào có đúng một cặp cạnh đối diện song song?", "a": "Hình thang"},
            {"q": "Hình tròn có đường kính 10 cm thì chu vi là bao nhiêu cm?", "a": "31,4 cm"},
            {"q": "Tính diện tích hình bình hành có đáy 12 cm và chiều cao tương ứng 6 cm", "a": "72 cm²"},
            {"q": "Tính chu vi hình thoi có cạnh dài 7 cm", "a": "28 cm"},
            {"q": "Tổng ba góc trong một hình tam giác luôn bằng bao nhiêu độ?", "a": "180 độ"},
            {"q": "Làng nghề làm đồ gốm thủ công đất nung hơn 500 năm tuổi ở Hội An là làng gì?", "a": "Làng gốm Thanh Hà"},
            {"q": "Món ăn đặc sản sợi mì vàng óng ăn kèm thịt xá xíu đặc trưng nhất Hội An là gì?", "a": "Mì Quảng (hoặc Cao lầu Hội An)"},
            {"q": "Chùa Cầu Hội An được xây dựng vào khoảng thế kỷ thứ mấy?", "a": "Thế kỷ 17"},
            {"q": "Tính diện tích tam giác vuông có hai cạnh góc vuông là 6 cm và 8 cm", "a": "24 cm²"},
            {"q": "Hình thoi có chu vi 40 cm thì độ dài mỗi cạnh là bao nhiêu?", "a": "10 cm"},
            # Lượt 3
            {"q": "Muốn tính diện tích hình thang ta lấy tổng hai đáy nhân chiều cao rồi làm gì?", "a": "Chia cho 2"},
            {"q": "Hình chữ nhật có chiều dài gấp đôi chiều rộng, nửa chu vi 30 cm. Diện tích là bao nhiêu?", "a": "200 cm² (rộng 10, dài 20)"},
            {"q": "Một hình tròn có diện tích 12,56 cm² thì bán kính là bao nhiêu cm?", "a": "2 cm"},
            {"q": "Tính chu vi hình bình hành có hai cạnh liên tiếp là 8 cm và 5 cm", "a": "26 cm"},
            {"q": "Lễ hội đêm rằm lung linh tắt đèn điện thắp sáng hoa đăng diễn ra vào ngày nào âm lịch?", "a": "Ngày 14 âm lịch hàng tháng"},
            {"q": "Làng nghề mộc truyền thống tinh xảo nằm đối diện phố cổ bên kia sông Thu Bồn là làng gì?", "a": "Làng mộc Kim Bồng"},
            {"q": "Phố cổ Hội An được UNESCO công nhận là Di sản Văn hóa Thế giới năm nào?", "a": "Năm 1999"},
            {"q": "Tính diện tích hình vuông có chu vi bằng 28 cm", "a": "49 cm² (cạnh 7 cm)"},
            {"q": "So sánh diện tích hình chữ nhật 6 cm × 4 cm và hình vuông cạnh 5 cm", "a": "Hình vuông lớn hơn (25 cm² > 24 cm²)"},
            {"q": "Đổi 0,45 km² sang héc-ta", "a": "45 ha"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một chiếc đèn lồng Hội An có khung mặt bên hình thoi với hai đường chéo dài 25 cm và 18 cm. Diện tích mặt khung hình thoi đó là ... cm².", "a": "225"},
            {"q": "Một luống trồng rau thơm tại Làng rau Trà Quế hình thang có đáy lớn 15 m, đáy bé 10 m và chiều cao 4 m. Diện tích luống rau là ... m².", "a": "50"},
            {"q": "Một chiếc thuyền nan chở khách ngắm sông Hoài đi được 3,6 km trong 45 phút. Vận tốc của thuyền nan là ... km/giờ.", "a": "4,8"},
            {"q": "Một viên gạch gốm Thanh Hà hình vuông có cạnh dài 30 cm. Diện tích viên gạch đó là ... cm².", "a": "900"},
            # Lượt 2
            {"q": "Một ngôi nhà cổ ở Hội An có khoảng sân gạch hình chữ nhật rộng 6 m, dài 8,5 m. Người ta dùng gạch vuông cạnh 50 cm để lát sân. Cần ít nhất ... viên gạch.", "a": "204"},
            {"q": "Đội làm đèn lồng 4 người trong 5 ngày làm được 120 chiếc đèn. Để làm được 240 chiếc đèn cùng loại trong 5 ngày cần ... người (năng suất như nhau).", "a": "8"},
            {"q": "Một bồn hoa hình tròn ở công viên Hội An có chu vi 15,7 m. Bán kính bồn hoa đó là ... m.", "a": "2,5"},
            {"q": "Tìm x, biết: x × 6,5 - x × 1,5 = 45. Giá trị của x là ...", "a": "9"},
            # Lượt 3
            {"q": "Một tấm lụa tơ tằm Hội An hình chữ nhật có chiều dài 2,4 m và chiều rộng 0,75 m. Diện tích tấm lụa là ... m².", "a": "1,8"},
            {"q": "Mua 6 bát Cao lầu Hội An hết 210 000 đồng. Mua 10 bát như thế hết tất cả ... đồng.", "a": "350000 (hoặc 350 000)"},
            {"q": "Một mảnh vườn hình bình hành có đáy 20 m và chiều cao 14,5 m. Diện tích mảnh vườn là ... m².", "a": "290"},
            {"q": "Tính giá trị biểu thức: (35,4 + 14,6) : 2,5 - 8,5. Kết quả là ...", "a": "11,5"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một mảnh đất hình chữ nhật tại Hội An có chu vi gấp 6 lần chiều rộng. Biết chiều dài hơn chiều rộng 15 m. Tính diện tích mảnh đất đó.\nA. 450 m²\nB. 500 m²\nC. 400 m²\nD. 600 m²",
                "ans_str": "A. 450 m² (Nửa chu vi gấp 3 lần chiều rộng, suy ra chiều dài gấp 2 lần chiều rộng. Chiều dài hơn chiều rộng 1 phần = 15 m. Chiều rộng: 15 m; Chiều dài: 15 × 2 = 30 m. Diện tích: 30 × 15 = 450 m²)"
            },
            {
                "q": "Một nghệ nhân gốm Thanh Hà làm một đĩa gốm trang trí hình tròn có đường kính 30 cm. Chính giữa đĩa là một bông hoa hình vuông có đường chéo bằng đường kính hình tròn. Tính diện tích phần gốm tráng men nằm ngoài hình vuông hoa (lấy pi = 3,14).\nA. 256,5 cm²\nB. 280 cm²\nC. 314 cm²\nD. 225 cm²",
                "ans_str": "A. 256,5 cm² (Bán kính hình tròn: 30 : 2 = 15 cm. Diện tích hình tròn: 15 × 15 × 3,14 = 706,5 cm². Hình vuông có hai đường chéo vuông góc dài 30 cm nên diện tích hình vuông là: (30 × 30) : 2 = 450 cm². Diện tích phần nằm ngoài: 706,5 - 450 = 256,5 cm²)"
            },
            # Lượt 2
            {
                "q": "Hai người thợ làm lồng đèn Hội An: người thứ nhất làm được 5 chiếc đèn mất 2,5 giờ; người thứ hai làm được 4 chiếc đèn mất 1,6 giờ. Hỏi ai làm nhanh hơn và nhanh hơn bao nhiêu phút cho mỗi chiếc đèn?\nA. Người thứ hai nhanh hơn 6 phút\nB. Người thứ nhất nhanh hơn 6 phút\nC. Người thứ hai nhanh hơn 10 phút\nD. Hai người bằng nhau",
                "ans_str": "A. Người thứ hai nhanh hơn 6 phút (Người 1 làm 1 đèn hết: 2,5 : 5 = 0,5 giờ = 30 phút. Người 2 làm 1 đèn hết: 1,6 : 4 = 0,4 giờ = 24 phút. Người 2 nhanh hơn: 30 - 24 = 6 phút)"
            },
            {
                "q": "Một thửa ruộng hình thang có đáy lớn 36 m, đáy bé bằng 2/3 đáy lớn. Chiều cao kém đáy bé 4 m. Người ta trồng lúa trên thửa ruộng đó, trung bình cứ 100 m² thu được 65 kg thóc. Hỏi cả thửa ruộng thu hoạch được bao nhiêu tạ thóc?\nA. 3,9 tạ\nB. 4,5 tạ\nC. 39 tạ\nD. 45 tạ",
                "ans_str": "A. 3,9 tạ (Đáy bé: 36 × 2/3 = 24 m. Chiều cao: 24 - 4 = 20 m. Diện tích: (36 + 24) × 20 : 2 = 600 m². Số thóc thu hoạch: 600 : 100 × 65 = 390 kg = 3,9 tạ)"
            },
            # Lượt 3
            {
                "q": "Một thuyền thả hoa đăng trên sông Hoài đi từ bến A đến bến B hết 30 phút và quay về từ B đến A hết 45 phút. Biết khúc sông AB dài 3 km. Tính vận tốc của dòng nước chảy trên sông Hoài.\nA. 1 km/giờ\nB. 2 km/giờ\nC. 1,5 km/giờ\nD. 0,5 km/giờ",
                "ans_str": "A. 1 km/giờ (30 phút = 0,5 giờ; 45 phút = 0,75 giờ. Vận tốc xuôi dòng: 3 : 0,5 = 6 km/giờ. Vận tốc ngược dòng: 3 : 0,75 = 4 km/giờ. Vận tốc dòng nước: (6 - 4) : 2 = 1 km/giờ)"
            },
            {
                "q": "Một khu đất hình vuông được mở rộng về một phía thêm 6 m để trở thành khu đất hình chữ nhật có chu vi 68 m. Tính diện tích khu đất ban đầu khi chưa mở rộng.\nA. 196 m²\nB. 225 m²\nC. 144 m²\nD. 256 m²",
                "ans_str": "A. 196 m² (Nửa chu vi hình chữ nhật: 68 : 2 = 34 m. Vì mở rộng về một phía 6 m nên chiều dài hơn chiều rộng 6 m. Chiều rộng (chính là cạnh hình vuông ban đầu): (34 - 6) : 2 = 14 m. Diện tích hình vuông ban đầu: 14 × 14 = 196 m²)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 18: ĐẢO LÝ SƠN (QUẢNG NGÃI) - TUẦN 18 🏆 CK1
    # =========================================================================
    {
        "tuan": 18,
        "tram_so": 18,
        "ten_tram": "Đảo Lý Sơn (Quảng Ngãi) 🏆 CK1",
        "chu_de": "Ôn tập đo lường toàn diện, tổng ôn tập Cuối học kỳ 1",
        "v1": [
            # Lượt 1
            {"q": "1 tấn bằng bao nhiêu tạ?", "a": "10 tạ"},
            {"q": "1 tạ bằng bao nhiêu yến?", "a": "10 yến"},
            {"q": "1 yến bằng bao nhiêu ki-lô-gam?", "a": "10 kg"},
            {"q": "1 tấn bằng bao nhiêu ki-lô-gam?", "a": "1 000 kg"},
            {"q": "1 ha bằng bao nhiêu mét vuông?", "a": "10 000 m²"},
            {"q": "Huyện đảo tiền tiêu Lý Sơn thuộc tỉnh nào của vùng Duyên hải Nam Trung Bộ?", "a": "Quảng Ngãi"},
            {"q": "Đảo Lý Sơn được mệnh danh là vương quốc của loài nông sản gia vị trứ danh nào?", "a": "Tỏi Lý Sơn (Tỏi cô đơn)"},
            {"q": "Cổng đá tự nhiên hình vòm tuyệt đẹp hình thành từ nham thạch núi lửa ở Lý Sơn là cổng gì?", "a": "Cổng Tò Vò"},
            {"q": "Đỉnh núi cao nhất đảo Lý Sơn có lòng chảo núi lửa cổ chứa hồ nước ngọt là đỉnh gì?", "a": "Đỉnh Thới Lới"},
            {"q": "Hải đội lịch sử anh hùng có nhiệm vụ đo đạc cắm mốc chủ quyền tại Hoàng Sa xuất phát từ Lý Sơn là gì?", "a": "Hải đội Hoàng Sa"},
            # Lượt 2
            {"q": "Khoảng cách từ Cảng Sa Kỳ (đất liền) ra đảo Lý Sơn khoảng bao nhiêu hải lý?", "a": "Khoảng 15 hải lý (~28 km)"},
            {"q": "Tính nhẩm phép nhân: 0,125 × 8", "a": "1"},
            {"q": "Tính nhẩm phép chia: 45 : 0,1", "a": "450"},
            {"q": "Số thập phân gồm 2 trăm, 5 đơn vị và 3 phần trăm viết là gì?", "a": "205,03"},
            {"q": "Đổi 4 km 50 m sang ki-lô-mét dưới dạng số thập phân", "a": "4,05 km"},
            {"q": "Đổi 3 tấn 25 kg sang tấn dưới dạng số thập phân", "a": "3,025 tấn"},
            {"q": "Đổi 2 ha 500 m² sang héc-ta", "a": "2,05 ha"},
            {"q": "Một hòn đảo nhỏ tuyệt đẹp nằm cách đảo Lớn Lý Sơn khoảng 3 hải lý là đảo gì?", "a": "Đảo Bé (xã An Bình)"},
            {"q": "Chùa cổ độc đáo nằm trọn trong lòng hang đá núi lửa ở Lý Sơn là chùa gì?", "a": "Chùa Hang"},
            {"q": "Tính nhanh: 3,65 × 4,7 + 3,65 × 5,3", "a": "36,5"},
            # Lượt 3
            {"q": "Tính kết quả: (15,5 + 4,5) : 0,5", "a": "40 (20 × 2 = 40)"},
            {"q": "Tìm x, biết: x × 0,25 = 12", "a": "x = 48"},
            {"q": "Đổi 1,5 giờ sang phút", "a": "90 phút"},
            {"q": "Tính diện tích hình tròn có bán kính 5 cm", "a": "78,5 cm²"},
            {"q": "Tính diện tích tam giác có đáy 10 cm, chiều cao 8 cm", "a": "40 cm²"},
            {"q": "Tính diện tích hình thang có hai đáy 12 cm và 8 cm, chiều cao 6 cm", "a": "60 cm²"},
            {"q": "Loài tỏi đặc biệt chỉ có một tép duy nhất với hàm lượng dinh dưỡng cao ở Lý Sơn gọi là gì?", "a": "Tỏi cô đơn (tỏi mồ côi)"},
            {"q": "Đài tưởng niệm và nhà trưng bày đội hùng binh Hoàng Sa kiêm quản Bắc Hải đặt tại xã nào Lý Sơn?", "a": "Xã An Vĩnh (Lý Sơn)"},
            {"q": "Biển đảo thiêng liêng nào của Tổ quốc do Hải đội Hoàng Sa kiêm quản suốt nhiều thế kỷ?", "a": "Quần đảo Hoàng Sa và Trường Sa"},
            {"q": "Tính giá trị biểu thức: 100 - 2,5 × 8", "a": "80"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một ruộng hành tỏi ở Lý Sơn hình chữ nhật có chiều dài 40 m, chiều rộng 25 m. Người ta thu hoạch được trung bình 1,5 kg tỏi trên mỗi mét vuông. Cả ruộng thu được ... tạ tỏi.", "a": "15"},
            {"q": "Tàu cao tốc Super Biển Đông chạy từ cảng Sa Kỳ ra đảo Lý Sơn vượt quãng đường 28 km hết 35 phút (tương đương 7/12 giờ). Vận tốc tàu là ... km/giờ.", "a": "48"},
            {"q": "Một gia đình nông dân Lý Sơn thu hoạch đợt 1 được 2,4 tạ tỏi, đợt 2 được nhiều hơn đợt 1 là 80 kg tỏi. Cả hai đợt gia đình thu được ... kg tỏi.", "a": "560"},
            {"q": "Tìm x, biết: x : 3,5 + 2,4 = 10,4. Giá trị của x là ...", "a": "28"},
            # Lượt 2
            {"q": "Cột cờ Tổ quốc trên đỉnh Thới Lới (Lý Sơn) có chiều cao 20 m. Một đoàn 36 học sinh đứng xếp hàng nghiêm trang chào cờ. Biết cứ 4 bạn xếp 1 hàng, xếp được tất cả ... hàng.", "a": "9"},
            {"q": "Một hồ chứa nước ngọt núi lửa trên đỉnh Thới Lới có dung tích 270 000 m³. Mỗi ngày đảo tiêu thụ 1 500 m³ nước. Lượng nước hồ dự trữ đủ dùng trong ... ngày.", "a": "180"},
            {"q": "Một hộp tỏi cô đơn Lý Sơn đặc biệt 500 g có giá 400 000 đồng. Giá tiền 1 kg tỏi cô đơn đó là ... đồng.", "a": "800000 (hoặc 800 000)"},
            {"q": "Tính nhanh giá trị biểu thức: 14,8 × 0,25 + 25,2 × 0,25. Kết quả là ...", "a": "10"},
            # Lượt 3
            {"q": "Một ca nô du lịch đi từ đảo Lớn sang đảo Bé dài 5,5 km hết 11 phút. Vận tốc của ca nô là ... km/giờ.", "a": "30"},
            {"q": "Một thửa đất trồng tỏi hình thang có diện tích 360 m², chiều cao 12 m. Đáy lớn hơn đáy bé 10 m. Chiều dài đáy lớn là ... m.", "a": "35"},
            {"q": "Tìm y, biết: 45,6 - y × 2,5 = 30,6. Giá trị của y là ...", "a": "6"},
            {"q": "Một bể chứa nước hình tròn có bán kính 3 m. Diện tích nắp đậy bể nước hình tròn đó là ... m².", "a": "28,26"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một tàu cao tốc rời cảng Sa Kỳ ra đảo Lý Sơn và một tàu rời đảo Lý Sơn vào Sa Kỳ xuất phát cùng lúc lúc 7 giờ 30 phút. Quãng đường biển dài 28 km. Vận tốc tàu thứ nhất là 26 km/giờ, tàu thứ hai là 30 km/giờ. Hỏi hai tàu gặp nhau lúc mấy giờ?\nA. 8 giờ\nB. 8 giờ 15 phút\nC. 7 giờ 50 phút\nD. 8 giờ 05 phút",
                "ans_str": "A. 8 giờ (Tổng vận tốc hai tàu: 26 + 30 = 56 km/giờ. Thời gian đi để gặp nhau: 28 : 56 = 0,5 giờ = 30 phút. Hai tàu gặp nhau lúc: 7 giờ 30 phút + 30 phút = 8 giờ)"
            },
            {
                "q": "Bác Ba bán hai bao tỏi cô đơn Lý Sơn được tất cả 1 800 000 đồng. Biết bao thứ nhất nặng gấp đôi bao thứ hai và giá 1 kg tỏi ở cả hai bao như nhau. Bác Ba đã bán bao thứ nhất được bao nhiêu tiền?\nA. 1 200 000 đồng\nB. 1 400 000 đồng\nC. 900 000 đồng\nD. 600 000 đồng",
                "ans_str": "A. 1 200 000 đồng (Tổng số phần bằng nhau: 2 + 1 = 3 phần. Giá trị bao thứ nhất (2 phần): 1 800 000 : 3 × 2 = 1 200 000 đồng)"
            },
            # Lượt 2
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = (1 + 1/3 + 1/6 + 1/10 + 1/15) × 30\nA. 50\nB. 52\nC. 48\nD. 60",
                "ans_str": "A. 50 (Nhân phân phối 30 vào từng số hạng trong ngoặc: A = 30 × 1 + 30 × 1/3 + 30 × 1/6 + 30 × 1/10 + 30 × 1/15 = 30 + 10 + 5 + 3 + 2 = 50)"
            },
            {
                "q": "Một thửa ruộng hình chữ nhật trồng tỏi ở Lý Sơn có chiều dài hơn chiều rộng 12 m. Nếu mở rộng chiều dài thêm 4 m và chiều rộng thêm 4 m thì diện tích thửa ruộng tăng thêm 256 m². Tính diện tích ban đầu của thửa ruộng đó.\nA. 864 m²\nB. 640 m²\nC. 720 m²\nD. 580 m²",
                "ans_str": "A. 864 m² (Phần diện tích tăng thêm gồm: 4 × chiều dài + 4 × chiều rộng + 4 × 4 = 256 => 4 × (chiều dài + chiều rộng) = 240 => Chiều dài + chiều rộng = 60 (m). Chiều rộng thửa ruộng ban đầu là: (60 - 12) : 2 = 24 (m). Chiều dài thửa ruộng ban đầu là: 24 + 12 = 36 (m). Diện tích ban đầu của thửa ruộng là: 36 × 24 = 864 (m²))"
            },
            # Lượt 3
            {
                "q": "Một đơn vị hải quân trên đảo Lý Sơn có 45 chiến sĩ ăn hết số gạo dự trữ trong 30 ngày. Sau 10 ngày ăn, có thêm 15 chiến sĩ mới chuyển ra đảo. Hỏi số gạo còn lại đủ cho toàn đơn vị ăn trong bao nhiêu ngày nữa (mức ăn mỗi người như nhau)?\nA. 15 ngày\nB. 18 ngày\nC. 20 ngày\nD. 12 ngày",
                "ans_str": "A. 15 ngày (Số ngày ăn còn lại của 45 người: 30 - 10 = 20 ngày. Tổng số suất ăn còn lại: 45 × 20 = 900 suất. Số chiến sĩ lúc sau: 45 + 15 = 60 người. Số ngày ăn còn lại là: 900 : 60 = 15 ngày)"
            },
            {
                "q": "Tổng số tuổi của ba cha con là 56 tuổi. Biết tuổi của cha gấp 3 lần tổng số tuổi của hai người con, và người anh hơn người em 2 tuổi. Tính tuổi của người em.\nA. 6 tuổi\nB. 7 tuổi\nC. 8 tuổi\nD. 5 tuổi",
                "ans_str": "A. 6 tuổi (Coi tổng số tuổi của hai người con là 1 phần thì tuổi của người cha là 3 phần như thế. Tổng số phần bằng nhau là: 1 + 3 = 4 (phần). Tổng số tuổi của hai người con là: 56 : 4 = 14 (tuổi). Tuổi của người em là: (14 - 2) : 2 = 6 (tuổi))"
            }
        ]
    }
]
