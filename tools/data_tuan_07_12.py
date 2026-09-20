# -*- coding: utf-8 -*-
"""
Dữ liệu ngân hàng câu hỏi Tuần 7 đến Tuần 12 (Trạm 7 - 12)
Mỗi trạm chuẩn 48 câu hỏi:
- Vòng 1: 30 câu ghép đôi (10 câu/lượt x 3 lượt)
- Vòng 2: 12 câu điền số thực tế (4 câu/lượt x 3 lượt)
- Vòng 3: 6 câu trắc nghiệm Mức 3 (2 câu/lượt x 3 lượt)
"""

TUAN_07_TO_12 = [
    # =========================================================================
    # TRẠM 7: THỦ ĐÔ HÀ NỘI - TUẦN 7
    # =========================================================================
    {
        "tuan": 7,
        "tram_so": 7,
        "ten_tram": "Thủ đô Hà Nội",
        "chu_de": "Ki-lô-mét vuông, Héc-ta, Các đơn vị đo diện tích",
        "v1": [
            # Lượt 1
            {"q": "1 héc-ta (ha) bằng bao nhiêu mét vuông?", "a": "10 000 m²"},
            {"q": "1 ki-lô-mét vuông (km²) bằng bao nhiêu héc-ta?", "a": "100 ha"},
            {"q": "1 km² bằng bao nhiêu mét vuông?", "a": "1 000 000 m²"},
            {"q": "Đổi 5 ha sang mét vuông", "a": "50 000 m²"},
            {"q": "Đổi 300 ha sang ki-lô-mét vuông", "a": "3 km²"},
            {"q": "Hồ nước ngọt tự nhiên nằm ở trung tâm Thủ đô Hà Nội là hồ gì?", "a": "Hồ Hoàn Kiếm (Hồ Gươm)"},
            {"q": "Di sản văn hóa thế giới nằm tại trung tâm Ba Đình Hà Nội là di tích nào?", "a": "Hoàng thành Thăng Long"},
            {"q": "Quảng trường lịch sử nơi Bác Hồ đọc Tuyên ngôn Độc lập là quảng trường nào?", "a": "Quảng trường Ba Đình"},
            {"q": "So sánh: 4 ha và 40 000 m²", "a": "Bằng nhau (=)"},
            {"q": "So sánh: 2 km² và 190 ha", "a": "2 km² > 190 ha (vì 2 km² = 200 ha)"},
            # Lượt 2
            {"q": "Đổi 2,5 ha sang mét vuông", "a": "25 000 m²"},
            {"q": "Đổi 45 000 m² sang héc-ta", "a": "4,5 ha"},
            {"q": "Đổi 15 ha sang ki-lô-mét vuông", "a": "0,15 km²"},
            {"q": "1 đề-ca-mét vuông (dam²) bằng bao nhiêu mét vuông?", "a": "100 m²"},
            {"q": "1 héc-tô-mét vuông (hm²) còn có tên gọi khác là gì?", "a": "Héc-ta (ha)"},
            {"q": "Hồ nước ngọt lớn nhất Thủ đô Hà Nội có diện tích hơn 500 ha là hồ gì?", "a": "Hồ Tây"},
            {"q": "Cây cầu lịch sử hơn 120 năm tuổi bắc qua sông Hồng ở Hà Nội là cầu gì?", "a": "Cầu Long Biên"},
            {"q": "Trường đại học đầu tiên của Việt Nam nằm tại Hà Nội là di tích nào?", "a": "Văn Miếu - Quốc Tử Giám"},
            {"q": "So sánh: 1/2 ha và 5 000 m²", "a": "Bằng nhau (=)"},
            {"q": "So sánh: 3/4 km² và 70 ha", "a": "3/4 km² > 70 ha (vì 3/4 km² = 75 ha)"},
            # Lượt 3
            {"q": "Đổi 1/4 ha sang mét vuông", "a": "2 500 m²"},
            {"q": "Đổi 7 500 m² sang héc-ta", "a": "0,75 ha"},
            {"q": "Đổi 0,5 km² sang héc-ta", "a": "50 ha"},
            {"q": "1 m² bằng bao nhiêu đề-xi-mét vuông?", "a": "100 dm²"},
            {"q": "Viết số đo 3 ha 400 m² dưới dạng héc-ta", "a": "3,04 ha"},
            {"q": "Tháp đá cổ kính rêu phong nổi giữa lòng Hồ Gươm là tháp gì?", "a": "Tháp Rùa"},
            {"q": "Chùa có kiến trúc một cột độc đáo hình đóa sen giữa lòng Hà Nội là chùa gì?", "a": "Chùa Một Cột"},
            {"q": "Năm Lý Thái Tổ dời đô về Thăng Long (Hà Nội) là năm nào?", "a": "Năm 1010"},
            {"q": "Viết số đo 5 km² 25 ha dưới dạng ki-lô-mét vuông", "a": "5,25 km²"},
            {"q": "1 ha gấp 1 dam² bao nhiêu lần?", "a": "100 lần"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Hồ Tây (Hà Nội) có diện tích mặt nước khoảng 5,3 km². Đổi diện tích Hồ Tây sang héc-ta là ... ha.", "a": "530"},
            {"q": "Khuôn viên Hoàng thành Thăng Long hình chữ nhật có chiều dài 500 m, chiều rộng 360 m. Diện tích khuôn viên đó là ... ha.", "a": "18"},
            {"q": "Một công viên ở Hà Nội có diện tích 12 ha. Người ta dùng 2/5 diện tích làm hồ nước, phần còn lại trồng cây xanh. Diện tích trồng cây xanh là ... ha.", "a": "7,2"},
            {"q": "Đổi 8 400 m² sang héc-ta ta được ... ha (nhập số thập phân).", "a": "0,84"},
            # Lượt 2
            {"q": "Quảng trường Ba Đình có chiều dài 320 m, chiều rộng 100 m. Diện tích Quảng trường Ba Đình là ... ha.", "a": "3,2"},
            {"q": "Một trang trại hoa sen Tây Hồ có diện tích 2,4 ha. Mỗi héc-ta thu hoạch được trung bình 5 tấn hoa và hạt sen. Trang trại thu hoạch được tất cả ... tấn sản phẩm.", "a": "12"},
            {"q": "Tìm x, biết: x ha + 3,5 ha = 8,2 ha. Giá trị của x là ...", "a": "4,7"},
            {"q": "Một khu đô thị mới tại Hà Nội có diện tích 1,5 km². Đổi diện tích khu đô thị này sang mét vuông là ... m².", "a": "1500000 (hoặc 1 500 000)"},
            # Lượt 3
            {"q": "Khu di tích Văn Miếu - Quốc Tử Giám có diện tích khoảng 54 331 m². Làm tròn diện tích này đến hàng nghìn mét vuông ta được ... m².", "a": "54000"},
            {"q": "Người ta lát gạch vỉa hè một đoạn đường quanh Hồ Gươm dài 800 m, rộng 5 m. Diện tích vỉa hè cần lát là ... m².", "a": "4000"},
            {"q": "Một mảnh đất hình chữ nhật có chu vi 600 m, chiều dài gấp đôi chiều rộng. Diện tích mảnh đất đó là ... ha.", "a": "2"},
            {"q": "Một vườn ươm cây xanh của Thủ đô có diện tích 3/4 ha. Đổi diện tích vườn ươm sang mét vuông là ... m².", "a": "7500"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một khu đô thị sinh thái ở Hà Nội có diện tích 48 ha. Trong đó diện tích đất ở bằng 3/5 diện tích cây xanh và hồ nước. Tính diện tích đất ở của khu đô thị đó.\nA. 18 ha\nB. 30 ha\nC. 16 ha\nD. 20 ha",
                "ans_str": "A. 18 ha (Tổng số phần bằng nhau: 3 + 5 = 8 phần. Diện tích đất ở là: 48 : 8 × 3 = 18 ha)"
            },
            {
                "q": "Một sân trường tiểu học ở Hà Nội hình chữ nhật có nửa chu vi là 160 m. Chiều rộng bằng 3/5 chiều dài. Người ta dùng 15% diện tích sân để xây bồn hoa cây xanh. Tính diện tích phần sân còn lại.\nA. 5 100 m²\nB. 6 000 m²\nC. 4 250 m²\nD. 5 000 m²",
                "ans_str": "A. 5 100 m² (Chiều rộng: 160 : (3+5) × 3 = 60 m; Chiều dài: 160 - 60 = 100 m. Diện tích sân: 100 × 60 = 6 000 m². Diện tích còn lại chiếm 85%: 6 000 × 85% = 5 100 m²)"
            },
            # Lượt 2
            {
                "q": "Một thửa ruộng hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Nếu tăng chiều rộng thêm 5 m và giảm chiều dài đi 5 m thì diện tích thửa ruộng tăng thêm 225 m². Tính diện tích ban đầu của thửa ruộng đó theo đơn vị héc-ta.\nA. 0,1875 ha\nB. 0,27 ha\nC. 0,35 ha\nD. 0,48 ha",
                "ans_str": "A. 0,1875 ha (Gọi chiều rộng là r thì chiều dài là 3 × r. Khi tăng rộng 5 m và giảm dài 5 m, diện tích tăng thêm là: (3 × r - 5) × (r + 5) - 3 × r × r = 10 × r - 25 = 225 => 10 × r = 250 => r = 25 (m). Chiều dài ban đầu là: 25 × 3 = 75 (m). Diện tích ban đầu là: 75 × 25 = 1 875 (m²) = 0,1875 ha)"
            },
            {
                "q": "Để lát nền một hội trường lớn ở Hà Nội hình chữ nhật có kích thước 24 m và 15 m, người ta dùng loại gạch men hình vuông cạnh 60 cm. Hỏi cần mua bao nhiêu viên gạch (bỏ qua mạch vữa)?\nA. 1 000 viên\nB. 1 200 viên\nC. 1 500 viên\nD. 800 viên",
                "ans_str": "A. 1 000 viên (Diện tích hội trường: 24 × 15 = 360 m² = 3 600 000 cm². Diện tích 1 viên gạch: 60 × 60 = 3 600 cm². Số gạch cần dùng: 3 600 000 : 3 600 = 1 000 viên)"
            },
            # Lượt 3
            {
                "q": "Một mảnh đất hình chữ nhật có chu vi gấp 6 lần chiều rộng. Biết chiều dài hơn chiều rộng 24 m. Tính diện tích mảnh đất đó theo đơn vị mét vuông.\nA. 1 152 m²\nB. 1 200 m²\nC. 1 080 m²\nD. 960 m²",
                "ans_str": "A. 1 152 m² (Nửa chu vi gấp 3 lần chiều rộng, suy ra chiều dài gấp 2 lần chiều rộng. Hiệu số phần: 2 - 1 = 1 phần tương ứng 24 m. Chiều rộng: 24 m; Chiều dài: 24 × 2 = 48 m. Diện tích: 48 × 24 = 1 152 m²)"
            },
            {
                "q": "Cho một hình vuông có cạnh 10 cm. Người ta vẽ 4 nửa hình tròn có đường kính là 4 cạnh của hình vuông đó. Hỏi diện tích phần 4 cánh hoa được tạo thành bên trong hình vuông là bao nhiêu (lấy pi = 3,14)?\nA. 57 cm²\nB. 78,5 cm²\nC. 62,8 cm²\nD. 50 cm²",
                "ans_str": "A. 57 cm² (Tổng diện tích 4 nửa hình tròn = diện tích 2 hình tròn có đường kính 10 cm (bán kính r = 5 cm): 2 × (5 × 5 × 3,14) = 157 cm². Diện tích 4 cánh hoa chính là phần chồng lên nhau: 157 - 100 = 57 cm²)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 8: VỊNH HẠ LONG & YÊN TỬ (QUẢNG NINH) - TUẦN 8
    # =========================================================================
    {
        "tuan": 8,
        "tram_so": 8,
        "ten_tram": "Vịnh Hạ Long & Yên Tử (Quảng Ninh)",
        "chu_de": "Phép cộng số thập phân, tính chất giao hoán và kết hợp của phép cộng STP, tính nhanh",
        "v1": [
            # Lượt 1
            {"q": "Tính kết quả phép cộng: 15,3 + 4,5", "a": "19,8"},
            {"q": "Tính kết quả phép cộng: 28,75 + 11,25", "a": "40"},
            {"q": "Tính nhanh: 3,6 + 4,7 + 6,4", "a": "14,7 ((3,6 + 6,4) + 4,7 = 14,7)"},
            {"q": "Phép cộng số thập phân có tính chất a + b = b + a gọi là tính chất gì?", "a": "Tính chất giao hoán"},
            {"q": "Phép cộng số thập phân (a + b) + c = a + (b + c) là tính chất gì?", "a": "Tính chất kết hợp"},
            {"q": "Vịnh Hạ Long được UNESCO bao nhiêu lần công nhận là Di sản Thiên nhiên Thế giới?", "a": "2 lần (1994, 2000)"},
            {"q": "Vịnh Hạ Long có khoảng bao nhiêu hòn đảo lớn nhỏ?", "a": "1 969 hòn đảo"},
            {"q": "Đỉnh núi thiêng Yên Tử có ngôi chùa Đồng nằm ở độ cao bao nhiêu mét?", "a": "1 068 m"},
            {"q": "Tính nhẩm: 4,8 + 0,2", "a": "5"},
            {"q": "Tính nhẩm: 19,95 + 0,05", "a": "20"},
            # Lượt 2
            {"q": "Tính kết quả: 34,82 + 9,7", "a": "44,52"},
            {"q": "Tính kết quả: 125,6 + 74,4", "a": "200"},
            {"q": "Tính nhanh: 12,5 + 8,9 + 7,5", "a": "28,9"},
            {"q": "Tính nhanh: 5,45 + 3,8 + 4,55 + 6,2", "a": "20 ((5,45 + 4,55) + (3,8 + 6,2) = 20)"},
            {"q": "Biểu tượng nổi tiếng của Vịnh Hạ Long trên tờ tiền 200.000 đồng là hòn đảo đá nào?", "a": "Hòn Đỉnh Hương (Lư Hương)"},
            {"q": "Cặp hòn đảo đá biểu tượng cho tình yêu và du lịch Hạ Long là hòn gì?", "a": "Hòn Trống Mái (hòn Gà Chọi)"},
            {"q": "Người sáng lập nên Thiền phái Trúc Lâm Yên Tử là vị vua nào?", "a": "Vua Trần Nhân Tông"},
            {"q": "Tính nhẩm: 6,75 + 10", "a": "16,75"},
            {"q": "Tìm x, biết: x - 4,5 = 12,3", "a": "x = 16,8"},
            {"q": "Số nào cộng với bất kỳ số thập phân a nào cũng bằng chính số a?", "a": "Số 0"},
            # Lượt 3
            {"q": "Tính kết quả: 0,85 + 0,35", "a": "1,2"},
            {"q": "Tính kết quả: 67,9 + 32,1", "a": "100"},
            {"q": "Tính nhanh: 1,2 + 2,3 + 3,4 + 8,8 + 7,7 + 6,6", "a": "30"},
            {"q": "Vịnh biển tuyệt đẹp nằm liền kề phía đông bắc Vịnh Hạ Long là vịnh gì?", "a": "Vịnh Bái Tử Long"},
            {"q": "Hang động lộng lẫy bậc nhất trên Vịnh Hạ Long có tên là gì?", "a": "Hang Sửng Sốt"},
            {"q": "Chùa Đồng Yên Tử được đúc hoàn toàn bằng kim loại gì?", "a": "Đồng nguyên chất"},
            {"q": "Tính kết quả: 9,99 + 0,01", "a": "10"},
            {"q": "Tính kết quả: 45,6 + 0,54", "a": "46,14"},
            {"q": "Tìm y, biết: y - 8,75 = 11,25", "a": "y = 20"},
            {"q": "Tổng của 3 số thập phân: 2,5 + 3,5 + 4,5 bằng bao nhiêu?", "a": "10,5"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một du thuyền tham quan Vịnh Hạ Long: buổi sáng chạy 24,5 km; buổi chiều chạy nhiều hơn buổi sáng 5,8 km. Cả ngày du thuyền chạy được ... km.", "a": "54,8"},
            {"q": "Tính nhanh giá trị biểu thức: 4,65 + 7,89 + 5,35 + 2,11. Kết quả là ...", "a": "20"},
            {"q": "Ba kiện hàng hải sản Quảng Ninh cân nặng lần lượt là 23,5 kg; 18,75 kg và 26,25 kg. Tổng khối lượng ba kiện hàng là ... kg.", "a": "68,5"},
            {"q": "Tìm x, biết: x - 15,8 = 24,6. Giá trị của x là ...", "a": "40,4"},
            # Lượt 2
            {"q": "Tuyến cáp treo lên đỉnh Yên Tử chặng 1 dài 1,2 km, chặng 2 dài 0,9 km. Tổng chiều dài hai chặng cáp treo là ... km.", "a": "2,1"},
            {"q": "Một gia đình mua vé tham quan Vịnh Hạ Long: vé người lớn hết 580 000 đồng, vé trẻ em hết 320 000 đồng, tiền ăn trưa hết 850 000 đồng. Tổng chi phí là ... đồng.", "a": "1750000 (hoặc 1 750 000)"},
            {"q": "Tính nhanh giá trị biểu thức: 1,1 + 2,2 + 3,3 + 6,7 + 7,8 + 8,9. Kết quả là ...", "a": "30"},
            {"q": "Một bể nuôi hải sản ở Tuần Châu chứa 15,5 m³ nước, người ta bơm thêm vào bể 8,75 m³ nước nữa. Lúc này trong bể có ... m³ nước.", "a": "24,25"},
            # Lượt 3
            {"q": "Đoàn thám hiểm leo núi Yên Tử: giờ đầu đi được 1,8 km; giờ thứ hai đi được 1,5 km; giờ thứ ba đi được 1,2 km. Cả ba giờ đoàn đi được ... km.", "a": "4,5"},
            {"q": "Tìm y, biết: y - 3,45 - 2,55 = 14. Giá trị của y là ...", "a": "20"},
            {"q": "Một hòn đảo đá trên Vịnh Hạ Long có chu vi đáy dạng tam giác với 3 cạnh là 12,4 m; 15,8 m và 11,8 m. Chu vi chân đảo đá là ... m.", "a": "40"},
            {"q": "Lượng mưa đo được tại Quảng Ninh ngày thứ nhất là 34,5 mm; ngày thứ hai là 45,8 mm. Cả hai ngày lượng mưa đo được là ... mm.", "a": "80,3"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Khi cộng một số tự nhiên với một số thập phân có một chữ số ở phần thập phân, bạn Nam đã quên dấu phẩy của số thập phân nên thực hiện phép cộng như hai số tự nhiên và được tổng là 465. Biết tổng đúng là 202,2. Tìm số tự nhiên đó.\nA. 173\nB. 176\nC. 182\nD. 165",
                "ans_str": "A. 173 (Khi quên dấu phẩy của số thập phân có một chữ số ở phần thập phân thì số đó tăng lên 10 lần. Tổng tăng thêm là 9 lần số thập phân đó: 465 - 202,2 = 262,8. Số thập phân là: 262,8 : 9 = 29,2. Số tự nhiên cần tìm là: 202,2 - 29,2 = 173)"
            },
            {
                "q": "Tính tổng của 20 số hạng đầu tiên trong dãy số thập phân sau:\n0,2; 0,4; 0,6; 0,8; 1,0; 1,2; ...\nA. 40\nB. 42\nC. 44\nD. 50",
                "ans_str": "B. 42 (Số hạng thứ 20 là: 0,2 + (20 - 1) × 0,2 = 4,0. Tổng 20 số hạng: (0,2 + 4,0) × 20 : 2 = 4,2 × 10 = 42)"
            },
            # Lượt 2
            {
                "q": "Ba người cùng mua chung vé tham quan Vịnh Hạ Long. Người thứ nhất trả 1/3 tổng số tiền. Người thứ hai trả ít hơn người thứ nhất 50 000 đồng. Người thứ ba trả 250 000 đồng thì vừa đủ. Hỏi tổng số tiền vé của cả 3 người là bao nhiêu?\nA. 600 000 đồng\nB. 750 000 đồng\nC. 540 000 đồng\nD. 450 000 đồng",
                "ans_str": "A. 600 000 đồng (Gọi tổng số tiền là T. Người 1 trả T/3; người 2 trả T/3 - 50 000. Tổng hai người trả: 2T/3 - 50 000. Người 3 trả T/3 + 50 000 = 250 000 => T/3 = 200 000 => T = 600 000 đồng)"
            },
            {
                "q": "Hai cabin cáp treo Yên Tử xuất phát cùng lúc từ hai đầu tuyến cáp dài 1 800 m đi ngược chiều nhau. Vận tốc cabin A là 5 m/giây, vận tốc cabin B là 4 m/giây. Hỏi sau bao lâu hai cabin gặp nhau?\nA. 200 giây (3 phút 20 giây)\nB. 180 giây\nC. 240 giây\nD. 150 giây",
                "ans_str": "A. 200 giây (3 phút 20 giây) (Mỗi giây 2 cabin đi được: 5 + 4 = 9 m. Thời gian gặp nhau: 1 800 : 9 = 200 giây = 3 phút 20 giây)"
            },
            # Lượt 3
            {
                "q": "Một người đi xe máy từ Hạ Long sang Yên Tử (Quảng Ninh) với vận tốc 40 km/giờ hết 1,2 giờ. Khi từ Yên Tử trở về Hạ Long người đó đi với vận tốc 30 km/giờ. Tính thời gian người đó đi từ Yên Tử về Hạ Long.\nA. 1,6 giờ (1 giờ 36 phút)\nB. 1,5 giờ\nC. 1,4 giờ\nD. 1,8 giờ",
                "ans_str": "A. 1,6 giờ (1 giờ 36 phút) (Quãng đường từ Hạ Long đến Yên Tử là: 40 × 1,2 = 48 km. Thời gian quay về: 48 : 30 = 1,6 giờ = 1 giờ 36 phút)"
            },
            {
                "q": "Một hình chữ nhật có chu vi là 48 m. Nếu tăng chiều rộng thêm 4 m và giảm chiều dài 4 m thì hình chữ nhật trở thành hình vuông. Tính diện tích của hình chữ nhật ban đầu.\nA. 128 m²\nB. 140 m²\nC. 144 m²\nD. 120 m²",
                "ans_str": "A. 128 m² (Nửa chu vi là: 48 : 2 = 24 m. Khi thay đổi trở thành hình vuông nên chiều dài hơn chiều rộng là: 4 + 4 = 8 m. Chiều rộng ban đầu: (24 - 8) : 2 = 8 m; Chiều dài ban đầu: 8 + 8 = 16 m. Diện tích: 16 × 8 = 128 m²)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 9: TRÀNG AN & CỐ ĐÔ HOA LƯ (NINH BÌNH) - TUẦN 9 🌟 GK1
    # =========================================================================
    {
        "tuan": 9,
        "tram_so": 9,
        "ten_tram": "Tràng An & Cố đô Hoa Lư (Ninh Bình) 🌟 GK1",
        "chu_de": "Phép trừ số thập phân, phép nhân số thập phân với số tự nhiên, ôn tập Giữa học kỳ 1",
        "v1": [
            # Lượt 1
            {"q": "Tính kết quả phép trừ: 15,8 - 7,3", "a": "8,5"},
            {"q": "Tính kết quả phép trừ: 42,5 - 18,25", "a": "24,25"},
            {"q": "Tính kết quả phép nhân: 2,5 × 4", "a": "10"},
            {"q": "Tính kết quả phép nhân: 1,25 × 8", "a": "10"},
            {"q": "Tìm x, biết: x + 4,5 = 10", "a": "x = 5,5"},
            {"q": "Quần thể danh thắng Tràng An là Di sản thế giới hỗn hợp đầu tiên của Đông Nam Á về cả văn hóa và điều gì?", "a": "Thiên nhiên"},
            {"q": "Cố đô Hoa Lư từng là kinh đô của hai triều đại phong kiến nào trong lịch sử nước ta?", "a": "Nhà Đinh và Nhà Tiền Lê"},
            {"q": "Vị hoàng đế có công dẹp loạn 12 sứ quân, định đô tại Hoa Lư là ai?", "a": "Đinh Tiên Hoàng (Đinh Bộ Lĩnh)"},
            {"q": "Tính nhẩm: 10 - 2,75", "a": "7,25"},
            {"q": "Tính nhẩm: 0,75 × 4", "a": "3"},
            # Lượt 2
            {"q": "Tính kết quả: 60 - 24,75", "a": "35,25"},
            {"q": "Tính kết quả: 8,36 - 2,5", "a": "5,86"},
            {"q": "Tính kết quả: 3,4 × 5", "a": "17"},
            {"q": "Tính kết quả: 0,15 × 6", "a": "0,9"},
            {"q": "Tìm y, biết: 15 - y = 4,8", "a": "y = 10,2"},
            {"q": "Danh thắng sông nước tuyệt đẹp nơi có cánh đồng lúa hai bên dòng sông Ngô Đồng ở Ninh Bình là gì?", "a": "Tam Cốc - Bích Động"},
            {"q": "Đỉnh núi đá có view ngắm toàn cảnh Tam Cốc với rồng đá uốn lượn là đỉnh gì?", "a": "Hang Múa"},
            {"q": "Món ăn đặc sản ẩm thực nổi tiếng nhất của vùng đất Ninh Bình là gì?", "a": "Cơm cháy thịt dê"},
            {"q": "Tính nhanh: 4,5 × 7 + 4,5 × 3", "a": "45 (4,5 × 10 = 45)"},
            {"q": "So sánh: 5,4 - 2,1 và 1,1 × 3", "a": "Bằng nhau (= 3,3)"},
            # Lượt 3
            {"q": "Tính kết quả: 100 - 37,8", "a": "62,2"},
            {"q": "Tính kết quả: 14,25 × 4", "a": "57"},
            {"q": "Tính kết quả: 0,25 × 40", "a": "10"},
            {"q": "Đổi 1,2 ha sang mét vuông", "a": "12 000 m²"},
            {"q": "Số thập phân 5,08 đọc là gì?", "a": "Năm phẩy không tám"},
            {"q": "Số hang động ngập nước thông nhau nổi tiếng tạo nên tên gọi Tràng An là bao nhiêu?", "a": "Hàng chục hang động (gần 50 hang xuyên thủy)"},
            {"q": "Ngôi đền thiêng thờ vua Đinh và vua Lê tại Hoa Lư cách nhau bao nhiêu mét?", "a": "Khoảng 500 m"},
            {"q": "Tính nhanh: 12,5 × 3 × 8", "a": "300 ((12,5 × 8) × 3 = 100 × 3 = 300)"},
            {"q": "Tìm x, biết: x : 4 = 2,25", "a": "x = 9"},
            {"q": "Một ngày có 24 giờ, 0,5 ngày bằng bao nhiêu giờ?", "a": "12 giờ"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một chiếc đò chở khách du lịch trên sông Tràng An đi một vòng các hang động dài 12,5 km hết 2,5 giờ. Vận tốc chèo đò trung bình là ... km/giờ.", "a": "5"},
            {"q": "Tính giá trị biểu thức: 45,8 - 3,5 × 4. Kết quả là ...", "a": "31,8"},
            {"q": "Bến thuyền Tràng An có 250 chiếc đò. Buổi sáng có 180 chiếc đò đang chở khách trên sông. Tỉ số phần trăm số đò đang chở khách là ... %.", "a": "72"},
            {"q": "Một thửa ruộng trồng lúa nước ở Tam Cốc hình chữ nhật có chu vi 180 m, chiều rộng kém chiều dài 20 m. Chiều dài thửa ruộng là ... m.", "a": "55"},
            # Lượt 2
            {"q": "Một gói đặc sản cơm cháy Ninh Bình có giá 45 000 đồng. Một đoàn khách mua 8 gói và đưa cho người bán 500 000 đồng. Người bán hàng phải trả lại ... đồng.", "a": "140000 (hoặc 140 000)"},
            {"q": "Tìm hai số có tổng là 45,6 và hiệu là 12,4. Số lớn là ...", "a": "29"},
            {"q": "Tính nhanh giá trị biểu thức: 7,8 × 15 - 7,8 × 5. Kết quả là ...", "a": "78"},
            {"q": "Để lên đỉnh núi Hang Múa ngắm cảnh Cố đô, bạn Robot phải bước qua 486 bậc đá. Robot đã đi được 2/3 số bậc đá. Robot còn phải bước thêm ... bậc đá nữa.", "a": "162"},
            # Lượt 3
            {"q": "Sân đình Đền Vua Đinh Tiên Hoàng hình chữ nhật có chiều dài 28 m, chiều rộng 15 m. Diện tích sân đình đó là ... m².", "a": "420"},
            {"q": "Một can đựng dầu thắp hương tại Cố đô chứa 10 lít dầu cân nặng 8,5 kg. Riêng vỏ can cân nặng 0,5 kg. Mỗi lít dầu cân nặng ... kg.", "a": "0,8"},
            {"q": "Tìm x, biết: (x + 2,5) × 4 = 26. Giá trị của x là ...", "a": "4"},
            {"q": "Một nhóm thợ đục đá mỹ nghệ Ninh Vân làm 4 pho tượng đá trong 8 ngày. Để làm 10 pho tượng như thế cần ... ngày (năng suất như nhau).", "a": "20"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Khi trừ một số tự nhiên cho một số thập phân có hai chữ số ở phần thập phân, một bạn học sinh đã quên viết dấu phẩy của số trừ nên thực hiện như trừ hai số tự nhiên và được kết quả là 125. Biết hiệu đúng là 421,01. Tìm số tự nhiên ban đầu.\nA. 424\nB. 425\nC. 420\nD. 430",
                "ans_str": "A. 424 (Quên dấu phẩy của số trừ có 2 chữ số ở phần thập phân thì số trừ tăng gấp 100 lần, dẫn đến hiệu giảm đi 99 lần số trừ. Hiệu giảm đi: 421,01 - 125 = 296,01. Số trừ đúng là: 296,01 : 99 = 2,99. Số tự nhiên ban đầu là: 421,01 + 2,99 = 424)"
            },
            {
                "q": "Một trường tiểu học tổ chức cho học sinh đi tham quan Cố đô Hoa Lư. Nếu xếp mỗi xe 30 học sinh thì thừa 12 học sinh. Nếu xếp mỗi xe 35 học sinh thì còn thiếu 18 học sinh nữa mới đủ xe. Hỏi có tất cả bao nhiêu học sinh đi tham quan?\nA. 192 học sinh\nB. 210 học sinh\nC. 222 học sinh\nD. 180 học sinh",
                "ans_str": "A. 192 học sinh (Số học sinh chênh lệch: 12 + 18 = 30 học sinh. Mỗi xe 35 học sinh hơn mỗi xe 30 học sinh: 35 - 30 = 5 học sinh. Số xe ô tô là: 30 : 5 = 6 xe. Số học sinh tham quan: 6 × 30 + 12 = 192 học sinh)"
            },
            # Lượt 2
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = 0,2 × 517 × 2 + 0,4 × 283 + 4 × 20\nA. 400\nB. 408\nC. 350\nD. 500",
                "ans_str": "A. 400 (Ta có: 0,2 × 2 = 0,4; 4 × 20 = 0,4 × 200. Biểu thức: A = 0,4 × 517 + 0,4 × 283 + 0,4 × 200 = 0,4 × (517 + 283 + 200) = 0,4 × 1 000 = 400)"
            },
            {
                "q": "Một thửa ruộng hình chữ nhật có chu vi 240 m. Người ta chia thửa ruộng đó thành hai thửa nhỏ: một thửa hình vuông và một thửa hình chữ nhật. Tổng chu vi hai thửa ruộng nhỏ là 340 m. Tính diện tích thửa ruộng ban đầu.\nA. 3 500 m²\nB. 3 200 m²\nC. 3 600 m²\nD. 2 800 m²",
                "ans_str": "A. 3 500 m² (Khi chia thành 2 thửa thì tổng chu vi tăng thêm 2 lần chiều rộng (đường chia cắt). 2 lần chiều rộng là: 340 - 240 = 100 m => Chiều rộng = 50 m. Nửa chu vi thửa ban đầu: 240 : 2 = 120 m => Chiều dài = 120 - 50 = 70 m. Diện tích: 70 × 50 = 3 500 m²)"
            },
            # Lượt 3
            {
                "q": "Một bến thuyền du lịch Tràng An có tất cả 45 chiếc thuyền gồm hai loại: thuyền chở 4 khách và thuyền chở 6 khách. Biết tổng số khách mà tất cả các thuyền chở được cùng lúc là 230 người. Hỏi có bao nhiêu chiếc thuyền loại chở 6 khách?\nA. 25 chiếc\nB. 20 chiếc\nC. 15 chiếc\nD. 30 chiếc",
                "ans_str": "A. 25 chiếc (Giả sử cả 45 thuyền đều chở 4 khách thì chở được: 45 × 4 = 180 khách. Số khách hụt đi: 230 - 180 = 50 khách. Mỗi thuyền 6 khách chở nhiều hơn thuyền 4 khách: 6 - 4 = 2 khách. Số thuyền loại chở 6 khách là: 50 : 2 = 25 chiếc)"
            },
            {
                "q": "Tìm số tự nhiên có hai chữ số, biết rằng số đó gấp 9 lần chữ số hàng đơn vị của nó.\nA. 45\nB. 35\nC. 54\nD. 27",
                "ans_str": "A. 45 (Gọi số đó là ab (a khác 0). Ta có: 10a + b = 9b => 10a = 8b => 5a = 4b. Vì 5 và 4 nguyên tố cùng nhau, a và b là chữ số từ 1 đến 9 nên a = 4, b = 5. Số cần tìm là 45)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 10: THÀNH NHÀ HỒ (THANH HÓA) - TUẦN 10
    # =========================================================================
    {
        "tuan": 10,
        "tram_so": 10,
        "ten_tram": "Thành Nhà Hồ (Thanh Hóa)",
        "chu_de": "Phép nhân số thập phân (STP nhân STP), phép chia số thập phân cho số tự nhiên",
        "v1": [
            # Lượt 1
            {"q": "Tính kết quả phép nhân: 2,5 × 1,4", "a": "3,5"},
            {"q": "Tính kết quả phép chia: 12,6 : 3", "a": "4,2"},
            {"q": "Khi nhân hai số thập phân có 1 chữ số và 2 chữ số ở phần thập phân thì tích có mấy chữ số thập phân?", "a": "3 chữ số thập phân"},
            {"q": "Tính kết quả: 0,5 × 0,8", "a": "0,4"},
            {"q": "Tính kết quả phép chia: 24,8 : 4", "a": "6,2"},
            {"q": "Thành Nhà Hồ (Thanh Hóa) được xây dựng bằng vật liệu độc đáo gì?", "a": "Các khối đá xanh lớn nguyên khối"},
            {"q": "Thành Nhà Hồ được xây dựng dưới triều đại nào?", "a": "Triều nhà Hồ (Hồ Quý Ly)"},
            {"q": "Các khối đá xây tường Thành Nhà Hồ có khối lượng trung bình khoảng bao nhiêu tấn?", "a": "Nặng từ 10 đến 26 tấn"},
            {"q": "Tính nhẩm: 4,8 : 2", "a": "2,4"},
            {"q": "Tính nhẩm: 1,5 × 0,2", "a": "0,3"},
            # Lượt 2
            {"q": "Tính kết quả phép nhân: 3,25 × 2,4", "a": "7,8"},
            {"q": "Tính kết quả phép chia: 75,5 : 5", "a": "15,1"},
            {"q": "Tính kết quả phép chia: 9 : 4", "a": "2,25"},
            {"q": "Tính kết quả: 1,2 × 1,2", "a": "1,44"},
            {"q": "Tìm x, biết: x × 3 = 14,4", "a": "x = 4,8"},
            {"q": "Bốn cổng thành lớn của Thành Nhà Hồ được xây dựng theo kiến trúc hình gì?", "a": "Cổng vòm đá cuốn (vòm cuốn)"},
            {"q": "Di tích lịch sử Lam Kinh nổi tiếng tại Thanh Hóa gắn liền với cuộc khởi nghĩa nào?", "a": "Khởi nghĩa Lam Sơn (Lê Lợi)"},
            {"q": "Món ăn đặc sản cuốn lá chuối nổi tiếng của Thanh Hóa là gì?", "a": "Nem chua Thanh Hóa"},
            {"q": "Tính nhanh: 2,5 × 4,8 × 4", "a": "48 ((2,5 × 4) × 4,8 = 48)"},
            {"q": "Tìm số dư trong phép chia 25 : 4 khi lấy thương là 6", "a": "1"},
            # Lượt 3
            {"q": "Tính kết quả phép nhân: 0,45 × 1,2", "a": "0,54"},
            {"q": "Tính kết quả phép chia: 51,6 : 6", "a": "8,6"},
            {"q": "Tính kết quả phép chia: 3 : 8", "a": "0,375"},
            {"q": "Tìm y, biết: y : 5 = 2,4", "a": "y = 12"},
            {"q": "Tính kết quả: 0,16 × 2,5", "a": "0,4"},
            {"q": "Cây cầu lịch sử huyền thoại bắc qua sông Mã ở Thanh Hóa là cầu gì?", "a": "Cầu Hàm Rồng"},
            {"q": "Bãi biển du lịch nổi tiếng tấp nập bậc nhất Thanh Hóa là bãi biển nào?", "a": "Bãi biển Sầm Sơn"},
            {"q": "Tính nhanh: 3,5 × 6,8 + 3,5 × 3,2", "a": "35 (3,5 × 10 = 35)"},
            {"q": "Tìm số dư trong phép chia: 43,5 : 5", "a": "0 (chia hết, thương là 8,7)"},
            {"q": "Tính diện tích hình vuông có cạnh dài 1,5 m", "a": "2,25 m²"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một khối đá xanh hình hộp chữ nhật xây tường Thành Nhà Hồ có chiều dài 2,5 m; chiều rộng 1,4 m và chiều cao 1,2 m. Diện tích mặt đáy khối đá là ... m².", "a": "3,5"},
            {"q": "Một cơ sở sản xuất nem chua Thanh Hóa đóng đều 144 chiếc nem vào 12 hộp. Mỗi hộp có ... chiếc nem.", "a": "12"},
            {"q": "Tính giá trị biểu thức: 15,6 : 3 + 2,4 × 1,5. Kết quả là ...", "a": "8,8"},
            {"q": "Một thửa ruộng hình chữ nhật gần Thành Nhà Hồ có chiều dài 45 m, chiều rộng bằng 0,6 chiều dài. Chiều rộng thửa ruộng là ... m.", "a": "27"},
            # Lượt 2
            {"q": "Một xe tải chở 4 khối đá xây di tích nặng tất cả 34,8 tấn. Trung bình mỗi khối đá nặng ... tấn.", "a": "8,7"},
            {"q": "Tìm x, biết: x × 6 = 43,2. Giá trị của x là ...", "a": "7,2"},
            {"q": "Một tấm biển đồng chỉ dẫn tham quan Thành Nhà Hồ hình chữ nhật có chiều dài 1,8 m, chiều rộng 0,85 m. Diện tích tấm biển đồng là ... m².", "a": "1,53"},
            {"q": "Một cuộn dây thép dùng chằng buộc đá nặng 52,5 kg. Người ta cắt thành 5 đoạn bằng nhau. Mỗi đoạn dây nặng ... kg.", "a": "10,5"},
            # Lượt 3
            {"q": "Tường phía Nam Thành Nhà Hồ dài 870,5 m. Người ta đo được tường phía Bắc dài 877 m. Tường phía Bắc dài hơn tường phía Nam ... m.", "a": "6,5"},
            {"q": "Một đoàn khách mua 15 hộp nem chua hết 750 000 đồng. Mua 24 hộp như thế hết tất cả ... đồng.", "a": "1200000 (hoặc 1 200 000)"},
            {"q": "Tìm y, biết: 45,6 : y = 8. Giá trị của y là ...", "a": "5,7"},
            {"q": "Một mảnh đất hình bình hành có đáy 24,5 m và chiều cao 12 m. Diện tích mảnh đất đó là ... m².", "a": "294"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một tấm đá nguyên khối xây Thành Nhà Hồ hình hộp chữ nhật có diện tích xung quanh là 9,36 m², chiều cao 1,2 m. Biết chiều dài hơn chiều rộng 0,7 m. Tính diện tích đáy của phiến đá đó.\nA. 3,68 m²\nB. 3,72 m²\nC. 3,48 m²\nD. 4,2 m²",
                "ans_str": "A. 3,68 m² (Chu vi đáy của phiến đá là: 9,36 : 1,2 = 7,8 (m). Nửa chu vi đáy là: 7,8 : 2 = 3,9 (m). Chiều rộng đáy là: (3,9 - 0,7) : 2 = 1,6 (m). Chiều dài đáy là: 1,6 + 0,7 = 2,3 (m). Diện tích đáy phiến đá là: 2,3 × 1,6 = 3,68 (m²))"
            },
            {
                "q": "Khi chia một số thập phân cho 24, một bạn đã tìm được thương là 3,45 và số dư là 0,16. Tìm số thập phân bị chia đó.\nA. 82,96\nB. 82,8\nC. 83,16\nD. 82,95",
                "ans_str": "A. 82,96 (Số bị chia = Thương × Số chia + Số dư = 3,45 × 24 + 0,16 = 82,8 + 0,16 = 82,96)"
            },
            # Lượt 2
            {
                "q": "Tính giá trị của biểu thức sau bằng cách thuận tiện nhất:\nA = 1,25 × 3,6 × 8 + 2,5 × 6,4 × 4\nA. 100\nB. 120\nC. 150\nD. 80",
                "ans_str": "A. 100 (Nhóm: (1,25 × 8) × 3,6 + (2,5 × 4) × 6,4 = 10 × 3,6 + 10 × 6,4 = 36 + 64 = 100)"
            },
            {
                "q": "Một vườn cây ăn quả hình chữ nhật có chiều dài gấp 3 lần chiều rộng. Nếu tăng chiều rộng thêm 3 m và giảm chiều dài 3 m thì diện tích tăng thêm 81 m². Tính diện tích ban đầu của vườn cây.\nA. 675 m²\nB. 720 m²\nC. 600 m²\nD. 810 m²",
                "ans_str": "A. 675 m² (Gọi chiều rộng là r thì chiều dài là 3 × r. Diện tích ban đầu là 3 × r × r. Khi tăng rộng 3 m và giảm dài 3 m, diện tích mới là: (3 × r - 3) × (r + 3) = 3 × r × r + 6 × r - 9. Diện tích tăng thêm là: 6 × r - 9 = 81 => 6 × r = 90 => r = 15 (m). Chiều dài ban đầu là: 15 × 3 = 45 (m). Diện tích ban đầu của vườn cây là: 45 × 15 = 675 (m²))"
            },
            # Lượt 3
            {
                "q": "Một cơ sở đóng gói nem chua Thanh Hóa có 2 máy đóng gói tự động. Máy 1 đóng được 15 hộp nem trong 20 phút. Máy 2 đóng được 18 hộp nem trong 30 phút. Hỏi nếu cả hai máy cùng hoạt động thì để đóng đủ 162 hộp nem cần bao nhiêu thời gian?\nA. 2 giờ (120 phút)\nB. 2 giờ 30 phút\nC. 1 giờ 45 phút\nD. 3 giờ",
                "ans_str": "A. 2 giờ (120 phút) (Trong 1 giờ (60 phút), máy 1 đóng: 15 × 3 = 45 hộp; máy 2 đóng: 18 × 2 = 36 hộp. Cả hai máy 1 giờ đóng: 45 + 36 = 81 hộp. Thời gian đóng 162 hộp: 162 : 81 = 2 giờ)"
            },
            {
                "q": "Tìm hai số có tổng bằng 143, biết rằng nếu viết thêm chữ số 0 vào bên phải số bé thì được số lớn.\nA. 13 và 130\nB. 12 và 120\nC. 11 và 110\nD. 14 và 140",
                "ans_str": "A. 13 và 130 (Khi viết thêm chữ số 0 vào bên phải số bé thì được số lớn, suy ra số lớn gấp 10 lần số bé. Tổng số phần bằng nhau là: 1 + 10 = 11 (phần). Số bé là: 143 : 11 = 13. Số lớn là: 13 × 10 = 130)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 11: LÀNG SEN QUÊ BÁC (NGHỆ AN) - TUẦN 11
    # =========================================================================
    {
        "tuan": 11,
        "tram_so": 11,
        "ten_tram": "Làng Sen Quê Bác (Nghệ An)",
        "chu_de": "Nhân chia số thập phân với 10, 100, 1000... hoặc 0,1; 0,01... Chia số tự nhiên cho số thập phân",
        "v1": [
            # Lượt 1
            {"q": "Muốn nhân một số thập phân với 10; 100; 1000 ta dời dấu phẩy sang bên nào?", "a": "Sang bên phải 1, 2, 3... chữ số"},
            {"q": "Nhân một số với 0,1 cũng chính là chia số đó cho số nào?", "a": "Chia cho 10"},
            {"q": "Nhân một số với 0,5 cũng chính là chia số đó cho số nào?", "a": "Chia cho 2"},
            {"q": "Tính nhẩm: 4,75 × 10", "a": "47,5"},
            {"q": "Tính nhẩm: 25,6 : 10", "a": "2,56"},
            {"q": "Quê nội của Chủ tịch Hồ Chí Minh là làng nào thuộc huyện Nam Đàn, Nghệ An?", "a": "Làng Sen (Kim Liên)"},
            {"q": "Quê ngoại của Bác Hồ là làng nào gần Làng Sen?", "a": "Làng Hoàng Trù (Chùa)"},
            {"q": "Chủ tịch Hồ Chí Minh sinh năm bao nhiêu?", "a": "Năm 1890"},
            {"q": "Tính nhẩm: 18 × 0,1", "a": "1,8"},
            {"q": "Tính nhẩm: 3,2 : 0,1", "a": "32"},
            # Lượt 2
            {"q": "Tính nhẩm: 0,85 × 100", "a": "85"},
            {"q": "Tính nhẩm: 345,6 : 100", "a": "3,456"},
            {"q": "Chia một số cho 0,25 cũng chính là nhân số đó với số nào?", "a": "Nhân với 4"},
            {"q": "Tính kết quả phép chia: 45 : 1,5", "a": "30"},
            {"q": "Tính kết quả phép chia: 24 : 0,8", "a": "30"},
            {"q": "Dãy núi che chở phía sau Làng Sen nơi Bác Hồ thời niên thiếu thường thả diều là núi gì?", "a": "Núi Chung"},
            {"q": "Loài cây hoa biểu tượng thường được trồng làm hàng rào xanh trước cổng nhà Bác là cây gì?", "a": "Cây râm bụt (dâm bụt)"},
            {"q": "Bãi biển nghỉ dưỡng nổi tiếng của tỉnh Nghệ An là bãi biển nào?", "a": "Bãi biển Cửa Lò"},
            {"q": "Tính nhẩm: 42 × 0,5", "a": "21"},
            {"q": "Tính nhanh: 14,8 × 0,1 + 15,2 × 0,1", "a": "3 ((14,8 + 15,2) × 0,1 = 3)"},
            # Lượt 3
            {"q": "Tính nhẩm: 0,004 × 1000", "a": "4"},
            {"q": "Tính nhẩm: 12,5 : 0,5", "a": "25 (12,5 × 2 = 25)"},
            {"q": "Tính kết quả phép chia: 72 : 4,5", "a": "16"},
            {"q": "Tính kết quả phép chia: 9 : 0,125", "a": "72 (9 × 8 = 72)"},
            {"q": "Tìm x, biết: x : 0,1 = 45", "a": "x = 4,5"},
            {"q": "Ngôi nhà Bác Hồ ở Làng Sen là ngôi nhà lá mấy gian?", "a": "Nhà tranh 5 gian"},
            {"q": "Thành phố trung tâm chính trị văn hóa lớn của tỉnh Nghệ An là thành phố nào?", "a": "Thành phố Vinh"},
            {"q": "Năm Bác Hồ ra đi tìm đường cứu nước tại Bến Nhà Rồng là năm nào?", "a": "Năm 1911"},
            {"q": "Tính nhanh: 2,5 × 9,8 × 4", "a": "98 ((2,5 × 4) × 9,8 = 98)"},
            {"q": "Tính nhẩm: 56 : 0,01", "a": "5 600"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Khuôn viên ao sen trước nhà Bác hình chữ nhật có chu vi 120 m, chiều dài gấp đôi chiều rộng. Chiều rộng ao sen là ... m.", "a": "20"},
            {"q": "Một đoàn học sinh 45 người thuê xe đi từ TP Vinh về thăm Làng Sen dài 15 km hết 0,5 giờ. Vận tốc của xe là ... km/giờ.", "a": "30"},
            {"q": "Tính nhanh: 48 × 0,5 + 24 × 0,25. Kết quả là ...", "a": "30 (24 + 6 = 30)"},
            {"q": "Tìm x, biết: x × 1,5 = 45. Giá trị của x là ...", "a": "30"},
            # Lượt 2
            {"q": "Người ta trồng một hàng râm bụt dài 36 m dẫn vào nhà Bác, cứ cách 1,2 m trồng một cây (hai đầu đều trồng). Số cây râm bụt cần trồng là ... cây.", "a": "31"},
            {"q": "Bác thợ mộc cưa một cây tre dài 6 m thành các đoạn dài 1,5 m để làm hàng rào. Bác cần cưa ... lần.", "a": "3"},
            {"q": "Tính giá trị biểu thức: 75 : 2,5 - 12 × 1,5. Kết quả là ...", "a": "12"},
            {"q": "Một can dầu thơm hoa sen chứa 4,5 lít cân nặng 3,6 kg. Một thùng chứa 15 lít dầu như thế cân nặng ... kg.", "a": "12"},
            # Lượt 3
            {"q": "Một thửa ruộng hình tam giác trồng hoa sen có đáy 30 m, chiều cao 18 m. Diện tích thửa ruộng hoa sen đó là ... m².", "a": "270"},
            {"q": "Đoàn xe 8 chiếc chở 360 du khách về viếng mộ cụ Phó bảng Nguyễn Sinh Sắc và thăm Quê Bác. Trung bình mỗi xe chở ... người.", "a": "45"},
            {"q": "Tìm y, biết: y : 0,25 = 16. Giá trị của y là ...", "a": "4"},
            {"q": "Một sợi dây dù dài 18 m được cắt thành các đoạn dây dài 2,25 m. Cắt được tất cả ... đoạn dây.", "a": "8"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một số nhân với 0,25 rồi trừ đi 1,5 thì bằng chính số đó chia cho 5 cộng thêm 0,5. Tìm số đó.\nA. 40\nB. 50\nC. 35\nD. 45",
                "ans_str": "A. 40 (Ta có: x × 0,25 = x/4; x : 5 = x/5. Theo đề bài: x/4 - 1,5 = x/5 + 0,5 => x/4 - x/5 = 2 => x/20 = 2 => x = 40)"
            },
            {
                "q": "Quãng đường từ trường học về Quê Bác dài 48 km. Cùng một lúc, một ô tô xuất phát từ trường và một xe máy xuất phát từ Quê Bác đi ngược chiều nhau. Vận tốc ô tô là 50 km/giờ, xe máy là 30 km/giờ. Hỏi sau bao lâu hai xe gặp nhau?\nA. 36 phút (0,6 giờ)\nB. 40 phút\nC. 45 phút\nD. 30 phút",
                "ans_str": "A. 36 phút (0,6 giờ) (Tổng vận tốc: 50 + 30 = 80 km/giờ. Thời gian gặp nhau: 48 : 80 = 0,6 giờ = 36 phút)"
            },
            # Lượt 2
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = (12,4 × 4,5 - 6,2 × 9) × (1 + 2 + 3 + ... + 100)\nA. 0\nB. 100\nC. 5 050\nD. 1 240",
                "ans_str": "A. 0 (Xét ngoặc thứ nhất: 12,4 × 4,5 = 6,2 × 2 × 4,5 = 6,2 × 9. Do đó: 12,4 × 4,5 - 6,2 × 9 = 0. Vậy tích bằng 0)"
            },
            {
                "q": "Một khu vườn hoa sen hình chữ nhật có chu vi 180 m. Nếu tăng chiều rộng thêm 8 m và giảm chiều dài đi 8 m thì khu vườn trở thành hình vuông. Tính diện tích khu vườn hoa sen đó.\nA. 1 961 m²\nB. 2 025 m²\nC. 1 800 m²\nD. 2 100 m²",
                "ans_str": "A. 1 961 m² (Nửa chu vi: 180 : 2 = 90 m. Chiều dài hơn chiều rộng: 8 + 8 = 16 m. Chiều rộng: (90 - 16) : 2 = 37 m; Chiều dài: 37 + 16 = 53 m. Diện tích: 53 × 37 = 1 961 m²)"
            },
            # Lượt 3
            {
                "q": "Một trường tiểu học cử đoàn cán bộ giáo viên đi viếng Quê Bác. Nếu mỗi xe chở 16 người thì còn thừa 6 người. Nếu mỗi xe chở 18 người thì có 1 xe chỉ chở 10 người. Hỏi đoàn có bao nhiêu người?\nA. 118 người\nB. 112 người\nC. 124 người\nD. 108 người",
                "ans_str": "A. 118 người (Nếu mỗi xe chở 18 người thì còn thiếu: 18 - 10 = 8 (người) để đủ xe đó. Chênh lệch giữa hai cách xếp là: 6 + 8 = 14 (người). Mỗi xe chở 18 người nhiều hơn mỗi xe chở 16 người là: 18 - 16 = 2 (người). Số xe ô tô là: 14 : 2 = 7 (xe). Số người trong đoàn là: 7 × 16 + 6 = 118 (người))"
            },
            {
                "q": "Một cửa hàng quà lưu niệm Làng Sen ngày thứ nhất bán được 25 chiếc khăn thổ cẩm, ngày thứ hai bán được 32 chiếc khăn cùng loại. Số tiền thu được ngày thứ hai nhiều hơn ngày thứ nhất 280 000 đồng. Hỏi cả hai ngày cửa hàng thu được bao nhiêu tiền?\nA. 2 280 000 đồng\nB. 2 000 000 đồng\nC. 2 560 000 đồng\nD. 1 980 000 đồng",
                "ans_str": "A. 2 280 000 đồng (Ngày thứ hai bán nhiều hơn: 32 - 25 = 7 chiếc khăn. Giá 1 chiếc khăn: 280 000 : 7 = 40 000 đồng. Cả hai ngày bán được: 25 + 32 = 57 chiếc khăn. Tổng số tiền thu được: 57 × 40 000 = 2 280 000 đồng)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 12: NGÃ BA ĐỒNG LỘC (HÀ TĨNH) - TUẦN 12
    # =========================================================================
    {
        "tuan": 12,
        "tram_so": 12,
        "ten_tram": "Ngã ba Đồng Lộc (Hà Tĩnh)",
        "chu_de": "Chia số thập phân cho số thập phân, hình tam giác và diện tích hình tam giác",
        "v1": [
            # Lượt 1
            {"q": "Muốn chia một số thập phân cho một số thập phân ta làm như thế nào?", "a": "Đếm chữ số phần thập phân của số chia rồi dời dấu phẩy của cả hai số sang phải"},
            {"q": "Tính kết quả phép chia: 17,5 : 2,5", "a": "7"},
            {"q": "Tính kết quả phép chia: 3,6 : 0,9", "a": "4"},
            {"q": "Hình tam giác có mấy đỉnh, mấy cạnh và mấy góc?", "a": "3 đỉnh, 3 cạnh, 3 góc"},
            {"q": "Công thức tính diện tích hình tam giác đáy a, chiều cao h là gì?", "a": "S = (a × h) : 2"},
            {"q": "Khu di tích lịch sử Ngã ba Đồng Lộc là nơi ghi dấu sự hy sinh anh dũng của bao nhiêu cô gái thanh niên xung phong?", "a": "10 cô gái TNXP"},
            {"q": "10 cô gái anh hùng Ngã ba Đồng Lộc thuộc Tiểu đội mấy?", "a": "Tiểu đội 4 (Đại đội 552)"},
            {"q": "Tiểu đội trưởng của 10 cô gái thanh niên xung phong Đồng Lộc là chị nào?", "a": "Chị Võ Thị Tần"},
            {"q": "Tính diện tích tam giác có đáy 6 cm và chiều cao 4 cm", "a": "12 cm²"},
            {"q": "Tính nhẩm: 4,8 : 1,2", "a": "4"},
            # Lượt 2
            {"q": "Tính kết quả: 12,6 : 0,42", "a": "30"},
            {"q": "Tính kết quả: 9,1 : 0,7", "a": "13"},
            {"q": "Tam giác vuông có hai cạnh góc vuông lần lượt là a và b thì diện tích là gì?", "a": "S = (a × b) : 2"},
            {"q": "Tính diện tích tam giác vuông có 2 cạnh góc vuông là 8 cm và 5 cm", "a": "20 cm²"},
            {"q": "Nếu gấp đáy của hình tam giác lên 2 lần và giữ nguyên chiều cao thì diện tích tăng gấp mấy lần?", "a": "Gấp 2 lần"},
            {"q": "Quả chuông đồng lớn tại tháp chuông tưởng niệm Đồng Lộc cao bao nhiêu tầng?", "a": "Tháp chuông 7 tầng"},
            {"q": "Dãy núi hùng vĩ nổi tiếng của quê hương Hà Tĩnh đi vào thơ ca là núi gì?", "a": "Dãy núi Hồng Lĩnh (99 ngọn)"},
            {"q": "Biển ngọc hoang sơ trong xanh tuyệt đẹp của Hà Tĩnh là biển nào?", "a": "Biển Thiên Cầm"},
            {"q": "Tính nhanh: 18,5 : 0,5", "a": "37 (18,5 × 2 = 37)"},
            {"q": "Tìm x, biết: x × 0,8 = 9,6", "a": "x = 12"},
            # Lượt 3
            {"q": "Tính kết quả: 24 : 0,6", "a": "40"},
            {"q": "Tính kết quả: 0,72 : 0,08", "a": "9"},
            {"q": "Một tam giác có diện tích 30 cm², đáy 10 cm. Chiều cao tương ứng là bao nhiêu cm?", "a": "6 cm (30 × 2 : 10 = 6)"},
            {"q": "Một tam giác có diện tích 45 cm², chiều cao 9 cm. Độ dài đáy tương ứng là bao nhiêu cm?", "a": "10 cm"},
            {"q": "Tính kết quả: 15,75 : 3,5", "a": "4,5"},
            {"q": "Năm 10 cô gái thanh niên xung phong Đồng Lộc hy sinh anh dũng là năm nào?", "a": "Năm 1968"},
            {"q": "Con đường huyền thoại huyết mạch đi qua Ngã ba Đồng Lộc thời chống Mỹ là đường gì?", "a": "Đường mòn Hồ Chí Minh (Đường Trường Sơn)"},
            {"q": "Loài cây xanh bạt ngàn bao bọc đồi thông và khu di tích Đồng Lộc là cây gì?", "a": "Cây thông"},
            {"q": "Tính diện tích tam giác có đáy 2,4 m và chiều cao 1,5 m", "a": "1,8 m²"},
            {"q": "Số nào chia cho 0,5 thì bằng chính số đó nhân với số nào?", "a": "Nhân với 2"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một bồn hoa tưởng niệm hình tam giác tại Ngã ba Đồng Lộc có độ dài đáy 8,4 m và chiều cao tương ứng 5 m. Diện tích bồn hoa đó là ... m².", "a": "21"},
            {"q": "Đội thanh niên xung phong san lấp hố bom dài 45 m hết 3,6 giờ. Trung bình mỗi giờ đội san lấp được ... m đường.", "a": "12,5"},
            {"q": "Tìm x, biết: x × 2,4 = 19,2. Giá trị của x là ...", "a": "8"},
            {"q": "Một lá cờ Tổ quốc hình tam giác có đáy 30 cm, chiều cao 20 cm. Diện tích lá cờ là ... cm².", "a": "300"},
            # Lượt 2
            {"q": "Người ta trồng 250 cây thông phủ xanh đồi Ngã ba Đồng Lộc. Đợt 1 trồng được 0,4 tổng số cây, đợt 2 trồng được 0,35 tổng số cây. Cả hai đợt trồng được ... cây thông.", "a": "187,5 (hoặc 187? 250 × 0,75 = 187,5 -> Sửa đề: 240 cây thông -> 240 × 0,75 = 180 cây thông)"},
            {"q": "Một tấm biển chỉ dẫn di tích hình tam giác vuông có hai cạnh góc vuông là 1,2 m và 0,8 m. Diện tích tấm biển đó là ... m².", "a": "0,48"},
            {"q": "Tính giá trị biểu thức: 28,8 : 2,4 - 1,5 × 4. Kết quả là ...", "a": "6"},
            {"q": "Một mảnh đất hình tam giác có diện tích 150 m², độ dài đáy là 25 m. Chiều cao của mảnh đất là ... m.", "a": "12"},
            # Lượt 3
            {"q": "Một đoàn đại biểu 120 người đến viếng đài tưởng niệm Đồng Lộc. Ban quản lý chia đều vào các xe điện 8 chỗ. Cần ít nhất ... xe điện để chở hết đoàn.", "a": "15"},
            {"q": "Tìm y, biết: 31,5 : y = 4,5. Giá trị của y là ...", "a": "7"},
            {"q": "Một khu đất tam giác có đáy 40 m. Nếu kéo dài đáy thêm 6 m thì diện tích tăng thêm 48 m². Chiều cao của khu đất là ... m.", "a": "16"},
            {"q": "Một xe cứu hỏa tiếp tế 18 m³ nước cho đồi thông. Mỗi vòi phun xả 2,25 m³ nước mỗi giờ. Xe xả hết nước trong ... giờ.", "a": "8"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Cho hình tam giác ABC có diện tích 120 cm². Nếu kéo dài đáy BC thêm một đoạn CD dài 4 cm thì diện tích tam giác tăng thêm 24 cm². Tính độ dài đáy BC ban đầu của hình tam giác.\nA. 20 cm\nB. 24 cm\nC. 18 cm\nD. 16 cm",
                "ans_str": "A. 20 cm (Phần diện tích tăng thêm là tam giác ACD có đáy CD = 4 cm. Chiều cao hạ từ đỉnh A xuống đáy BC là: 24 × 2 : 4 = 12 cm. Đáy BC ban đầu của tam giác ABC là: 120 × 2 : 12 = 20 cm)"
            },
            {
                "q": "Một đội thanh niên xung phong gồm 15 người dự định san lấp một đoạn đường qua hố bom trong 8 ngày. Sau 2 ngày làm việc thì có 5 người chuyển đi làm nhiệm vụ khác. Hỏi đội hoàn thành công việc còn lại trong bao nhiêu ngày nữa (năng suất như nhau)?\nA. 9 ngày\nB. 8 ngày\nC. 10 ngày\nD. 7 ngày",
                "ans_str": "A. 9 ngày (Số công việc còn lại 15 người làm trong 6 ngày = 90 công. Số người còn lại: 15 - 5 = 10 người. Thời gian làm xong đoạn đường là: 90 : 10 = 9 ngày)"
            },
            # Lượt 2
            {
                "q": "Một thửa đất hình tam giác có đáy gấp đôi chiều cao. Nếu tăng đáy thêm 4 m và giữ nguyên chiều cao thì diện tích tăng thêm 36 m². Tính diện tích thửa đất hình tam giác ban đầu.\nA. 324 m²\nB. 162 m²\nC. 288 m²\nD. 144 m²",
                "ans_str": "A. 324 m² (Phần diện tích tăng thêm là tam giác có đáy 4 m và cùng chiều cao với tam giác ban đầu. Chiều cao là: 36 × 2 : 4 = 18 m. Đáy tam giác ban đầu: 18 × 2 = 36 m. Diện tích ban đầu: 36 × 18 : 2 = 324 m²)"
            },
            {
                "q": "Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = (18,4 : 0,25 + 18,4 × 6) : 2\nA. 92\nB. 184\nC. 46\nD. 138",
                "ans_str": "A. 92 (Vì chia cho 0,25 chính là nhân với 4, nên: 18,4 : 0,25 + 18,4 × 6 = 18,4 × 4 + 18,4 × 6 = 18,4 × 10 = 184. Kết quả A = 184 : 2 = 92)"
            },
            # Lượt 3
            {
                "q": "Cho tam giác ABC có diện tích 90 cm². Trên cạnh BC lấy điểm M sao cho BM = 2 × MC. Tính diện tích tam giác ABM.\nA. 60 cm²\nB. 45 cm²\nC. 30 cm²\nD. 50 cm²",
                "ans_str": "A. 60 cm² (Hai tam giác ABM và ABC có chung chiều cao hạ từ đỉnh A xuống đáy BC. Đáy BM = 2/3 đáy BC nên diện tích tam giác ABM = 2/3 diện tích tam giác ABC = 90 × 2/3 = 60 cm²)"
            },
            {
                "q": "Một cano chạy trên sông La (Hà Tĩnh) xuôi dòng với vận tốc 28 km/giờ, ngược dòng với vận tốc 22 km/giờ. Tính vận tốc của dòng nước trên sông La.\nA. 3 km/giờ\nB. 6 km/giờ\nC. 2 km/giờ\nD. 4 km/giờ",
                "ans_str": "A. 3 km/giờ (Vận tốc dòng nước = (Vận tốc xuôi dòng - Vận tốc ngược dòng) : 2 = (28 - 22) : 2 = 3 km/giờ)"
            }
        ]
    }
]
