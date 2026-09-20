# -*- coding: utf-8 -*-
"""
Dữ liệu ngân hàng câu hỏi Tuần 19 đến Tuần 24 (Trạm 19 - 24)
Mỗi trạm chuẩn 48 câu hỏi:
- Vòng 1: 30 câu ghép đôi (10 câu/lượt x 3 lượt)
- Vòng 2: 12 bài điền số thực tế (4 câu/lượt x 3 lượt)
- Vòng 3: 6 câu trắc nghiệm Mức 3 (2 câu/lượt x 3 lượt)
"""

TUAN_19_TO_24 = [
    # =========================================================================
    # TRẠM 19: KON TUM (BỜ Y - NGÃ BA ĐÔNG DƯƠNG) - TUẦN 19
    # =========================================================================
    {
        "tuan": 19,
        "tram_so": 19,
        "ten_tram": "Kon Tum (Bờ Y - Ngã ba Đông Dương)",
        "chu_de": "Tỉ số, tỉ số phần trăm, tỉ lệ bản đồ, tìm hai số khi biết tổng và tỉ số",
        "souvenirs": {
            "cap1": "Huy hiệu Cột mốc Bờ Y Đồng (50đ)",
            "cap2": "Mô hình Nhà thờ Gỗ Bạc (90đ)",
            "cap3": "Chuông bạc Kon Klor Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Tỉ số của 3 và 5 được viết là gì?", "a": "3 : 5 (hoặc 3/5)"},
            {"q": "Tỉ số phần trăm của 3 và 4 là bao nhiêu?", "a": "75% (3 : 4 = 0,75 = 75%)"},
            {"q": "Viết số thập phân 0,45 dưới dạng tỉ số phần trăm", "a": "45%"},
            {"q": "Tìm hai số có tổng là 30 và tỉ số là 1/2", "a": "10 và 20"},
            {"q": "Trên bản đồ tỉ lệ 1 : 1 000, độ dài 1 cm ứng với độ dài thật là bao nhiêu mét?", "a": "10 m (1 000 cm = 10 m)"},
            {"q": "Cột mốc ngã ba biên giới Bờ Y là điểm giao nhau của 3 quốc gia nào?", "a": "Việt Nam - Lào - Campuchia"},
            {"q": "Ngã ba Đông Dương tại Kon Tum nổi tiếng với câu nói dân gian nào?", "a": "Một tiếng gà gáy ba nước cùng nghe"},
            {"q": "Ngôi nhà thờ bằng gỗ cổ kính hơn 100 năm tuổi nổi tiếng ở TP Kon Tum là gì?", "a": "Nhà thờ Gỗ Kon Tum"},
            {"q": "Cây cầu treo lớn nhất Tây Nguyên bắc qua dòng sông Đắk Bla là cầu gì?", "a": "Cầu treo Kon Klor"},
            {"q": "Dòng sông duy nhất ở Tây Nguyên chảy ngược theo hướng Tây là sông nào?", "a": "Sông Đắk Bla"},
            # Lượt 2
            {"q": "Tỉ số phần trăm của 12 và 50 là bao nhiêu?", "a": "24%"},
            {"q": "Viết phân số 3/5 dưới dạng tỉ số phần trăm", "a": "60%"},
            {"q": "Tìm hai số có tổng là 45 và tỉ số là 2/3", "a": "18 và 27"},
            {"q": "Trên bản đồ tỉ lệ 1 : 100 000, khoảng cách 2 cm ứng với độ dài thật là bao nhiêu km?", "a": "2 km (200 000 cm = 2 km)"},
            {"q": "Tổng số phần bằng nhau của hai số có tỉ số là 3/5 là mấy phần?", "a": "8 phần (3 + 5 = 8)"},
            {"q": "Cửa khẩu quốc tế nối Kon Tum với nước bạn Lào tại Bờ Y là cửa khẩu gì?", "a": "Cửa khẩu Bờ Y"},
            {"q": "Nhà rông lớn nhất Kon Tum nằm ở đầu cầu treo Kon Klor là nhà rông nào?", "a": "Nhà rông Kon Klor"},
            {"q": "Độ cao của cột mốc ngã ba Đông Dương Bờ Y là bao nhiêu mét so với mực nước biển?", "a": "Khoảng 1 086 m"},
            {"q": "Viết tỉ số phần trăm 125% dưới dạng số thập phân", "a": "1,25"},
            {"q": "Tính: 25% của 200 là bao nhiêu?", "a": "50"},
            # Lượt 3
            {"q": "Viết phân số 7/20 dưới dạng tỉ số phần trăm", "a": "35%"},
            {"q": "Tỉ số phần trăm của 4 và 5 là bao nhiêu?", "a": "80%"},
            {"q": "Tìm hai số có tổng là 100 và tỉ số là 1/4", "a": "20 và 80"},
            {"q": "Khoảng cách thực tế là 5 km, trên bản đồ tỉ lệ 1 : 50 000 vẽ dài bao nhiêu cm?", "a": "10 cm (500 000 : 50 000 = 10)"},
            {"q": "Số học sinh nữ bằng 3/4 số học sinh nam. Tỉ số của số nam so với cả lớp là gì?", "a": "4/7"},
            {"q": "Loài hoa rừng trắng muốt nở rộ khắp sườn đồi Kon Tum mùa xuân là hoa gì?", "a": "Hoa cà phê"},
            {"q": "Món ăn đặc sản cuốn hàng chục loại lá rừng độc đáo của Kon Tum là gì?", "a": "Gỏi lá Kon Tum"},
            {"q": "Tỉnh Kon Tum thuộc vùng kinh tế trọng điểm nào của nước ta?", "a": "Tây Nguyên (Bắc Tây Nguyên)"},
            {"q": "Tính: 50% của 84 là bao nhiêu?", "a": "42"},
            {"q": "Tìm x, biết: x% của 50 bằng 15", "a": "x = 30% (15 : 50 = 30%)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Trên bản đồ du lịch Kon Tum tỉ lệ 1 : 20 000, quãng đường từ Nhà thờ Gỗ đến cầu treo Kon Klor đo được 7,5 cm. Khoảng cách thật giữa hai địa danh đó là ... m.", "a": "1500"},
            {"q": "Đoàn thám hiểm leo cột mốc ngã ba biên giới Bờ Y có 40 người gồm hai nhóm: nam và nữ. Biết số nữ bằng 2/3 số nam. Số nữ trong đoàn là ... người.", "a": "16"},
            {"q": "Một vườn cà phê ở Kon Tum rộng 2 ha. Người ta đã thu hoạch được 65% diện tích. Diện tích cà phê chưa thu hoạch là ... m².", "a": "7000"},
            {"q": "Tìm hai số có tổng là 144 và tỉ số là 3/5. Số lớn là ...", "a": "90"},
            # Lượt 2
            {"q": "Cầu treo Kon Klor dài 292 m. Trên bản đồ tỉ lệ 1 : 10 000, cây cầu này được vẽ với độ dài là ... cm (làm tròn số thập phân).", "a": "2,92"},
            {"q": "Một cửa hàng bán gỏi lá Kon Tum: buổi sáng và buổi chiều bán được tất cả 150 suất ăn. Biết số suất buổi sáng bằng 3/2 số suất buổi chiều. Buổi sáng bán được ... suất.", "a": "90"},
            {"q": "Lớp 5A có 35 học sinh, trong đó có 28 bạn tham gia chuyến đi Bờ Y. Tỉ số phần trăm học sinh tham gia chuyến đi là ... %.", "a": "80"},
            {"q": "Hai kho dự trữ cà phê của Kon Tum có tất cả 280 tấn. Biết kho A chứa bằng 3/4 kho B. Kho B chứa ... tấn cà phê.", "a": "160"},
            # Lượt 3
            {"q": "Một đoàn xe máy chở khách từ TP Kon Tum lên Cửa khẩu Bờ Y dài 80 km. Sau 1 giờ xe đã đi được 60% quãng đường. Xe còn phải đi tiếp ... km nữa.", "a": "32"},
            {"q": "Khuôn viên Nhà thờ Gỗ Kon Tum hình chữ nhật có chu vi 180 m, chiều rộng bằng 4/5 chiều dài. Chiều dài khuôn viên là ... m.", "a": "50"},
            {"q": "Tìm y, biết: y × 40% = 28. Giá trị của y là ...", "a": "70"},
            {"q": "Bà con Ba Na thu hoạch được 450 kg măng le rừng. Đã sấy khô 2/5 số măng đó. Số măng tươi còn lại là ... kg.", "a": "270"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một mảnh đất hình chữ nhật cạnh sông Đắk Bla có chu vi là 140 m. Chiều rộng bằng 2/5 chiều dài. Người ta dùng 20% diện tích đất để làm nhà rông sinh hoạt. Tính diện tích phần đất làm nhà rông.\nA. 200 m²\nB. 250 m²\nC. 180 m²\nD. 220 m²",
                "ans_str": "A. 200 m² (Nửa chu vi: 140 : 2 = 70 m. Chiều rộng: 70 : (2+5) × 2 = 20 m; Chiều dài: 70 - 20 = 50 m. Diện tích mảnh đất: 50 × 20 = 1 000 m². Diện tích đất làm nhà rông: 1 000 × 20% = 200 m²)"
            },
            {
                "q": "Hiện nay tuổi mẹ gấp 3 lần tuổi con. Biết rằng 5 năm nữa tổng số tuổi của hai mẹ con là 58 tuổi. Hỏi hiện nay mẹ bao nhiêu tuổi?\nA. 36 tuổi\nB. 39 tuổi\nC. 33 tuổi\nD. 42 tuổi",
                "ans_str": "A. 36 tuổi (Tổng số tuổi hai mẹ con hiện nay: 58 - 5 × 2 = 48 tuổi. Tổng số phần bằng nhau: 3 + 1 = 4 phần. Tuổi con hiện nay: 48 : 4 = 12 tuổi. Tuổi mẹ hiện nay: 12 × 3 = 36 tuổi)"
            },
            # Lượt 2
            {
                "q": "Một trường tiểu học ở Kon Tum có 450 học sinh. Số học sinh dân tộc Ba Na bằng 4/5 số học sinh dân tộc Kinh. Biết trường chỉ có học sinh của hai dân tộc này. Hỏi trường có bao nhiêu học sinh dân tộc Ba Na?\nA. 200 học sinh\nB. 250 học sinh\nC. 220 học sinh\nD. 180 học sinh",
                "ans_str": "A. 200 học sinh (Tổng số phần bằng nhau: 4 + 5 = 9 phần. Số học sinh Ba Na: 450 : 9 × 4 = 200 học sinh)"
            },
            {
                "q": "Một người bán cà phê thu được 18 000 000 đồng tiền bán hàng, trong đó số tiền lãi bằng 20% tiền vốn. Tính số tiền vốn của người đó.\nA. 15 000 000 đồng\nB. 14 400 000 đồng\nC. 16 000 000 đồng\nD. 15 500 000 đồng",
                "ans_str": "A. 15 000 000 đồng (Tiền bán bằng: 100% + 20% = 120% tiền vốn. Tiền vốn là: 18 000 000 : 120 × 100 = 15 000 000 đồng)"
            },
            # Lượt 3
            {
                "q": "Hai người cùng góp vốn mở homestay ven cầu treo Kon Klor với tổng số vốn là 360 triệu đồng. Sau đó người thứ nhất rút bớt 40 triệu đồng thì số vốn còn lại của người thứ nhất bằng 3/5 số vốn người thứ hai. Tính số vốn ban đầu của người thứ nhất.\nA. 160 triệu đồng\nB. 140 triệu đồng\nC. 150 triệu đồng\nD. 180 triệu đồng",
                "ans_str": "A. 160 triệu đồng (Tổng số vốn sau khi rút bớt: 360 - 40 = 320 triệu đồng. Vốn còn lại của người 1: 320 : (3+5) × 3 = 120 triệu đồng. Vốn ban đầu người 1: 120 + 40 = 160 triệu đồng)"
            },
            {
                "q": "Trên bản đồ tỉ lệ 1 : 5 000, một khu bảo tồn hình chữ nhật có chiều dài 8 cm, chiều rộng 5 cm. Tính diện tích thực tế của khu bảo tồn đó theo đơn vị héc-ta.\nA. 10 ha\nB. 1 ha\nC. 100 ha\nD. 20 ha",
                "ans_str": "A. 10 ha (Chiều dài thực tế: 8 × 5 000 = 40 000 cm = 400 m. Chiều rộng thực tế: 5 × 5 000 = 25 000 cm = 250 m. Diện tích thực tế: 400 × 250 = 100 000 m² = 10 ha)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 20: GIA LAI (BIỂN HỒ TƠ NƯNG) - TUẦN 20
    # =========================================================================
    {
        "tuan": 20,
        "tram_so": 20,
        "ten_tram": "Gia Lai (Biển Hồ Tơ Nưng)",
        "chu_de": "Tìm hai số khi biết tổng và tỉ số (tiếp), tìm hai số khi biết hiệu và tỉ số",
        "souvenirs": {
            "cap1": "Huy hiệu Giọt ngọc Tơ Nưng Đồng (50đ)",
            "cap2": "Hoa dã quỳ Chư Đăng Ya Bạc (90đ)",
            "cap3": "Đôi mắt Pleiku Hoàng Kim Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Tìm hai số có hiệu là 20 và tỉ số là 1/3", "a": "10 và 30"},
            {"q": "Hiệu số phần bằng nhau của hai số có tỉ số là 2/7 là mấy phần?", "a": "5 phần (7 - 2 = 5)"},
            {"q": "Muốn tìm hai số khi biết hiệu và tỉ số, bước 1 ta tìm cái gì?", "a": "Hiệu số phần bằng nhau"},
            {"q": "Tìm hai số có hiệu là 15 và tỉ số là 2/5", "a": "10 và 25"},
            {"q": "Biển Hồ Tơ Nưng được nhạc sĩ Nguyễn Cường ví như điều gì của Pleiku?", "a": "Đôi mắt Pleiku"},
            {"q": "Biển Hồ Tơ Nưng thực chất được hình thành từ miệng của cái gì?", "a": "Miệng núi lửa cổ đã tắt"},
            {"q": "Ngọn núi lửa hình phễu nổi tiếng rực sắc hoa dã quỳ vàng ở Gia Lai là núi gì?", "a": "Núi lửa Chư Đăng Ya"},
            {"q": "Hàng thông trăm tuổi cổ kính dẫn vào đồi chè tuyệt đẹp ở Gia Lai là gì?", "a": "Hàng thông Biển Hồ chè"},
            {"q": "Tìm x, biết: x - 12 = 36", "a": "x = 48"},
            {"q": "Tìm hai số có tổng là 50 và hiệu là 10", "a": "20 và 30"},
            # Lượt 2
            {"q": "Tìm hai số có hiệu là 36 và số lớn gấp 4 lần số bé", "a": "Số bé: 12; Số lớn: 48"},
            {"q": "Tìm hai số có hiệu là 40 và tỉ số là 3/5", "a": "60 và 100"},
            {"q": "Một sợi dây dài hơn sợi dây kia 18 m và dài gấp 3 lần sợi dây kia. Độ dài sợi dây ngắn là gì?", "a": "9 m (18 : 2 = 9)"},
            {"q": "Thành phố trung tâm hành chính của tỉnh Gia Lai là thành phố nào?", "a": "Thành phố Pleiku"},
            {"q": "Món ăn đặc sản sợi phở ăn kèm hai tô (một tô khô, một tô nước dùng) ở Gia Lai là gì?", "a": "Phở hai tô (Phở khô Gia Lai)"},
            {"q": "Mùa hoa dã quỳ vàng nở rộ khắp sườn núi Chư Đăng Ya vào tháng mấy?", "a": "Tháng 11 hàng năm"},
            {"q": "Quảng trường lớn nhất TP Pleiku có tượng Bác Hồ với các dân tộc Tây Nguyên là gì?", "a": "Quảng trường Đại Đoàn Kết"},
            {"q": "Tìm y, biết: y : 3 - 5 = 10", "a": "y = 45"},
            {"q": "Tìm hai số có tổng là 80 và tỉ số là 1/3", "a": "20 và 60"},
            {"q": "Hiệu của hai số bằng 0 khi nào?", "a": "Khi hai số bằng nhau"},
            # Lượt 3
            {"q": "Tìm hai số có hiệu là 24 và tỉ số là 1/4", "a": "8 và 32"},
            {"q": "Tìm hai số có hiệu là 50 và tỉ số là 4/9", "a": "40 và 90"},
            {"q": "Bố hơn con 28 tuổi. Tuổi con bằng 1/5 tuổi bố. Tuổi con là bao nhiêu?", "a": "7 tuổi (28 : 4 = 7)"},
            {"q": "Hồ Tơ Nưng có độ sâu trung bình khoảng bao nhiêu mét?", "a": "Khoảng 16 m đến 19 m"},
            {"q": "Thác nước hùng vĩ bậc nhất Gia Lai nằm giữa thung lũng nguyên sinh là thác gì?", "a": "Thác Phú Cường"},
            {"q": "Công trình thủy điện nổi tiếng đầu tiên trên sông Sê San tại Gia Lai là gì?", "a": "Thủy điện Ialy"},
            {"q": "Dân tộc bản địa sinh sống lâu đời với truyền thống cồng chiêng ở Gia Lai là dân tộc nào?", "a": "Gia Rai và Ba Na"},
            {"q": "Tìm hai số có hiệu là 14 và số lớn bằng 8/6 số bé", "a": "42 và 56"},
            {"q": "Tính nhanh: 12,5 × 4 - 2,5 × 4", "a": "40"},
            {"q": "Viết số thập phân 0,08 dưới dạng tỉ số phần trăm", "a": "8%"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Đội thuyền chèo kayak trên Biển Hồ Tơ Nưng có số thuyền đôi nhiều hơn số thuyền đơn là 12 chiếc. Biết số thuyền đơn bằng 3/5 số thuyền đôi. Số thuyền đôi là ... chiếc.", "a": "30"},
            {"q": "Vườn chè cổ thụ Biển Hồ có chiều dài hơn chiều rộng 120 m, chiều rộng bằng 2/3 chiều dài. Chiều dài vườn chè là ... m.", "a": "360"},
            {"q": "Một đoàn du khách tham quan lễ hội hoa dã quỳ Chư Đăng Ya gồm người lớn và trẻ em. Người lớn nhiều hơn trẻ em 24 người và số trẻ em bằng 3/7 số người lớn. Có ... trẻ em.", "a": "18"},
            {"q": "Tìm hai số có hiệu là 45 và tỉ số là 2/5. Số bé là ...", "a": "30"},
            # Lượt 2
            {"q": "Quảng trường Đại Đoàn Kết (Pleiku) có diện tích sân lớn hơn diện tích vườn hoa là 4 ha. Diện tích vườn hoa bằng 1/3 diện tích sân. Diện tích sân quảng trường là ... ha.", "a": "6"},
            {"q": "Hai đội công nhân hái cà phê ở Chư Păh: đội một hái nhiều hơn đội hai 15 tạ quả tươi. Biết đội hai hái bằng 4/7 đội một. Đội một hái được ... tạ quả tươi.", "a": "35"},
            {"q": "Một gia đình trồng tiêu ở Gia Lai: vụ này thu được lượng tiêu đen nhiều hơn tiêu sọ là 36 tạ. Biết lượng tiêu sọ bằng 1/4 tiêu đen. Lượng tiêu đen thu được là ... tạ.", "a": "48"},
            {"q": "Tìm y, biết: y - 25% × y = 60. Giá trị của y là ...", "a": "80"},
            # Lượt 3
            {"q": "Hồ Tơ Nưng có diện tích mặt nước mùa mưa nhiều hơn mùa khô là 60 ha. Biết diện tích mùa khô bằng 3/4 diện tích mùa mưa. Diện tích mặt nước mùa mưa là ... ha.", "a": "240"},
            {"q": "Đường hoa dã quỳ lên núi Chư Đăng Ya dài hơn đoạn đường bằng là 1 500 m. Biết đoạn đường bằng dài bằng 2/5 đoạn đường dốc hoa. Đoạn đường hoa dài ... m.", "a": "2500"},
            {"q": "Tìm hai số có hiệu là 72 và tỉ số là 5/9. Số lớn là ...", "a": "162"},
            {"q": "Một cửa hàng đặc sản Pleiku bán mật ong hoa cà phê: can loại 1 nhiều hơn can loại 2 là 15 lít, tỉ số là 5/2. Can loại 1 có ... lít mật ong.", "a": "25"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một mảnh đất hình chữ nhật trồng hoa dã quỳ ở Chư Đăng Ya có chiều dài hơn chiều rộng 25 m. Nếu kéo dài chiều rộng thêm 5 m thì chiều rộng bằng 2/3 chiều dài. Tính diện tích mảnh đất ban đầu.\nA. 2 100 m²\nB. 1 800 m²\nC. 2 000 m²\nD. 1 600 m²",
                "ans_str": "A. 2 100 m² (Khi kéo dài chiều rộng thêm 5 m thì chiều dài hơn chiều rộng mới là: 25 - 5 = 20 (m). Hiệu số phần bằng nhau: 3 - 2 = 1 (phần). Chiều dài mảnh đất là: 20 : 1 × 3 = 60 (m). Chiều rộng ban đầu là: 60 - 25 = 35 (m). Diện tích mảnh đất ban đầu là: 60 × 35 = 2 100 (m²))"
            },
            {
                "q": "Hiện nay tuổi chú hơn tuổi cháu là 24 tuổi. Biết rằng 3 năm trước, tuổi chú gấp 4 lần tuổi cháu. Hỏi hiện nay cháu bao nhiêu tuổi?\nA. 11 tuổi\nB. 8 tuổi\nC. 12 tuổi\nD. 10 tuổi",
                "ans_str": "A. 11 tuổi (Hiệu số tuổi không thay đổi theo thời gian, 3 năm trước chú vẫn hơn cháu 24 tuổi. Tuổi cháu 3 năm trước: 24 : (4 - 1) = 8 tuổi. Tuổi cháu hiện nay: 8 + 3 = 11 tuổi)"
            },
            # Lượt 2
            {
                "q": "Một trang trại bò sữa tại Gia Lai có số bò sữa nhiều hơn số bê con là 180 con. Sau khi bán đi 20 con bê thì số bê còn lại bằng 1/5 số bò. Hỏi ban đầu trang trại có bao nhiêu con bê?\nA. 70 con\nB. 60 con\nC. 50 con\nD. 80 con",
                "ans_str": "A. 70 con (Sau khi bán 20 con bê thì số bò nhiều hơn số bê còn lại là: 180 + 20 = 200 con. Số bê còn lại: 200 : (5 - 1) = 50 con. Số bê ban đầu: 50 + 20 = 70 con)"
            },
            {
                "q": "Tìm một phân số có giá trị bằng 3/5, biết rằng nếu thêm 8 đơn vị vào tử số và giữ nguyên mẫu số thì ta được phân số mới có giá trị bằng 7/9.\nA. 27/45\nB. 36/60\nC. 45/75\nD. 18/30",
                "ans_str": "A. 27/45 (Gọi phân số cần tìm là a/b. Theo đề bài ta có: a/b = 3/5 và (a + 8)/b = 7/9. Suy ra: (a + 8)/b - a/b = 8/b = 7/9 - 3/5 = 8/45 => b = 45. Tử số là: a = 45 × 3/5 = 27. Vậy phân số cần tìm là 27/45)"
            },
            # Lượt 3
            {
                "q": "Hai thùng đựng trà Biển Hồ có tất cả 160 hộp. Nếu lấy 15 hộp từ thùng 1 chuyển sang thùng 2 thì thùng 2 nhiều hơn thùng 1 là 20 hộp. Hỏi ban đầu thùng 1 có bao nhiêu hộp trà?\nA. 85 hộp\nB. 75 hộp\nC. 90 hộp\nD. 80 hộp",
                "ans_str": "A. 85 hộp (Lúc sau thùng 1 có: (160 - 20) : 2 = 70 hộp. Ban đầu thùng 1 có: 70 + 15 = 85 hộp)"
            },
            {
                "q": "Hai người thợ cùng dệt một tấm thổ cẩm truyền thống Gia Lai. Người thứ nhất dệt mỗi ngày được 1,5 m; người thứ hai mỗi ngày dệt được 1,2 m. Sau một số ngày làm việc, người thứ nhất dệt được nhiều hơn người thứ hai 4,5 m vải. Hỏi cả hai người đã dệt được tổng cộng bao nhiêu mét vải?\nA. 40,5 m\nB. 36 m\nC. 45 m\nD. 42 m",
                "ans_str": "A. 40,5 m (Mỗi ngày người thứ nhất dệt nhiều hơn người thứ hai: 1,5 - 1,2 = 0,3 m. Số ngày làm việc: 4,5 : 0,3 = 15 ngày. Cả hai người dệt được: (1,5 + 1,2) × 15 = 2,7 × 15 = 40,5 m)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 21: ĐẮK LẮK (BUÔN ĐÔN, THÁC DRAY NUR) - TUẦN 21
    # =========================================================================
    {
        "tuan": 21,
        "tram_so": 21,
        "ten_tram": "Đắk Lắk (Buôn Đôn, Thác Dray Nur)",
        "chu_de": "Tìm giá trị phần trăm của một số, giải toán về tỉ số phần trăm, máy tính cầm tay",
        "souvenirs": {
            "cap1": "Vòng ngà voi Bản Đôn Đồng (50đ)",
            "cap2": "Cồng chiêng Đại ngàn Bạc (90đ)",
            "cap3": "Hạt cà phê Vàng Buôn Ma Thuột (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Tìm 20% của số 150", "a": "30 (150 × 20 : 100 = 30)"},
            {"q": "Tìm 10% của số 450", "a": "45"},
            {"q": "Muốn tìm giá trị phần trăm của một số, ta lấy số đó nhân với số phần trăm rồi làm gì?", "a": "Chia cho 100"},
            {"q": "Tìm một số biết 25% của nó bằng 50", "a": "200 (50 : 25 × 100 = 200)"},
            {"q": "Địa danh Buôn Đôn ở Đắk Lắk nổi tiếng khắp cả nước với nghề truyền thống gì?", "a": "Săn bắt và thuần dưỡng voi rừng"},
            {"q": "Thành phố được mệnh danh là Thủ phủ Cà phê của Việt Nam là thành phố nào?", "a": "Thành phố Buôn Ma Thuột"},
            {"q": "Cặp thác nước đôi hùng vĩ và thơ mộng bậc nhất trên sông Sêrêpôk là gì?", "a": "Thác Dray Nur và Thác Dray Sáp"},
            {"q": "Không gian văn hóa nào của đồng bào Tây Nguyên được UNESCO công nhận là Kiệt tác di sản thế giới?", "a": "Không gian văn hóa Cồng chiêng Tây Nguyên"},
            {"q": "Tính nhẩm: 50% của 240", "a": "120"},
            {"q": "Tính nhẩm: 75% của 80", "a": "60"},
            # Lượt 2
            {"q": "Tìm 35% của số 200", "a": "70"},
            {"q": "Tìm 12% của số 500", "a": "60"},
            {"q": "Tìm một số biết 40% của nó bằng 80", "a": "200"},
            {"q": "Dòng sông chảy ngược kỳ vĩ mang dòng nước đỏ qua Đắk Lắk là sông gì?", "a": "Sông Sêrêpôk"},
            {"q": "Hồ nước ngọt tự nhiên lớn thứ hai Việt Nam (sau Hồ Ba Bể) nằm tại Đắk Lắk là hồ gì?", "a": "Hồ Lắk"},
            {"q": "Cây cầu treo bằng tre nứa dài nhất vắt qua rặng si cổ thụ ở Buôn Đôn là gì?", "a": "Cầu treo Buôn Đôn"},
            {"q": "Vua voi huyền thoại của Buôn Đôn từng bắt và thuần dưỡng gần 300 con voi là ai?", "a": "Vua voi Khun Yu Nốp"},
            {"q": "Tính: 15% của 300 kg", "a": "45 kg"},
            {"q": "Lãi suất tiết kiệm 0,5% một tháng. Gửi 1 000 000 đồng sau 1 tháng được lãi bao nhiêu?", "a": "5 000 đồng"},
            {"q": "Nút bấm nào trên máy tính cầm tay dùng để xóa toàn bộ phép tính?", "a": "Nút AC (hoặc ON/C)"},
            # Lượt 3
            {"q": "Tìm 2,5% của số 400", "a": "10"},
            {"q": "Tìm 120% của số 50", "a": "60"},
            {"q": "Một lớp có 40 học sinh, 60% là nữ. Số học sinh nam là bao nhiêu?", "a": "16 học sinh (40% của 40 = 16)"},
            {"q": "Đàn voi thuần dưỡng ở Buôn Đôn hiện nay được bảo tồn theo mô hình du lịch gì?", "a": "Du lịch thân thiện với voi (không cưỡi voi)"},
            {"q": "Lễ hội văn hóa lớn định kỳ 2 năm một lần tổ chức tại Buôn Ma Thuột là gì?", "a": "Lễ hội Cà phê Buôn Ma Thuột"},
            {"q": "Bảo tàng thế giới chuyên đề cà phê độc đáo hàng đầu thế giới nằm tại TP nào?", "a": "Buôn Ma Thuột (Đắk Lắk)"},
            {"q": "Nhà dài truyền thống của người Ê Đê ở Đắk Lắk dài tới hàng chục mét theo chế độ gì?", "a": "Chế độ mẫu hệ"},
            {"q": "Tìm một số biết 10% của nó bằng 25", "a": "250"},
            {"q": "Tính nhanh: 30% của 120", "a": "36"},
            {"q": "Nút % trên máy tính cầm tay có chức năng gì?", "a": "Tính tỉ số phần trăm"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một vườn cà phê ở Buôn Ma Thuột vụ này thu hoạch được 8 tấn cà phê quả tươi. Sau khi phơi và sơ chế thì lượng nhân thu được chiếm 22% khối lượng quả tươi. Khối lượng cà phê nhân thu được là ... kg.", "a": "1760"},
            {"q": "Một chú voi ở Buôn Đôn mỗi ngày ăn hết khoảng 150 kg thức ăn xanh. Trong đó cỏ và lá cây chiếm 60%. Khối lượng cỏ và lá cây chú voi ăn mỗi ngày là ... kg.", "a": "90"},
            {"q": "Giá vé tham quan Thác Dray Nur là 50 000 đồng. Nhân dịp lễ hội được giảm giá 15%. Giá vé sau khi giảm là ... đồng.", "a": "42500 (hoặc 42 500)"},
            {"q": "Tìm một số biết 30% của số đó là 75. Số đó là ...", "a": "250"},
            # Lượt 2
            {"q": "Rừng quốc gia Yok Đôn có đàn voi rừng sinh sống. Năm ngoái kiểm đếm có 80 con voi, năm nay số lượng voi tăng thêm 5%. Số voi rừng năm nay là ... con.", "a": "84"},
            {"q": "Một cửa hàng đặc sản Đắk Lắk bán cà phê bột giá 200 000 đồng/kg. Khách mua từ 5 kg trở lên được chiết khấu 10%. Mua 6 kg cà phê đó phải trả ... đồng.", "a": "1080000 (hoặc 1 080 000)"},
            {"q": "Bác nông dân gửi tiết kiệm 50 000 000 đồng với lãi suất 0,6% một tháng. Sau một tháng cả tiền gửi và tiền lãi là ... đồng.", "a": "50300000"},
            {"q": "Một trường học ở TP Buôn Ma Thuột có 800 học sinh. Số học sinh tham gia câu lạc bộ Cồng chiêng chiếm 15%. Có ... học sinh tham gia câu lạc bộ.", "a": "120"},
            # Lượt 3
            {"q": "Thác Dray Nur có chiều dài mặt nước đổ xuống khoảng 250 m. Chiều cao thác bằng 12% chiều dài. Chiều cao của thác là ... m.", "a": "30"},
            {"q": "Một hồ nuôi cá ở Hồ Lắk dự định thu hoạch 5 tấn cá. Thực tế đã thu hoạch được 110% kế hoạch. Thực tế đã thu hoạch được ... tấn cá.", "a": "5,5"},
            {"q": "Tìm x, biết: 45% của x bằng 180. Giá trị của x là ...", "a": "400"},
            {"q": "Một gói hạt macca Đắk Lắk nặng 500 g chứa 70% chất béo và khoáng chất có lợi. Khối lượng chất có lợi trong gói hạt là ... g.", "a": "350"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một hợp tác xã cà phê Buôn Ma Thuột xuất khẩu 120 tấn cà phê sang châu Âu. Tháng đầu xuất được 35% tổng số cà phê, tháng thứ hai xuất được 40% số còn lại. Hỏi sau hai tháng còn lại bao nhiêu tấn cà phê chưa xuất khẩu?\nA. 46,8 tấn\nB. 48 tấn\nC. 42 tấn\nD. 50 tấn",
                "ans_str": "A. 46,8 tấn (Tháng đầu xuất: 120 × 35% = 42 tấn. Còn lại: 120 - 42 = 78 tấn. Tháng hai xuất: 78 × 40% = 31,2 tấn. Còn lại sau hai tháng: 78 - 31,2 = 46,8 tấn)"
            },
            {
                "q": "Một người bán một bao tiêu Đắk Lắk với giá 3 600 000 đồng thì được lãi 20% theo giá bán. Hỏi người đó lãi bao nhiêu phần trăm so với giá vốn?\nA. 25%\nB. 20%\nC. 15%\nD. 30%",
                "ans_str": "A. 25% (Tiền lãi: 3 600 000 × 20% = 720 000 đồng. Tiền vốn: 3 600 000 - 720 000 = 2 880 000 đồng. Tỉ số phần trăm lãi so với vốn: 720 000 : 2 880 000 = 0,25 = 25%)"
            },
            # Lượt 2
            {
                "q": "Một đàn voi ở Buôn Đôn gồm cả voi trưởng thành và voi con có tất cả 25 con. Trong một đợt kiểm tra sức khỏe, số voi trưởng thành chiếm 68% cả đàn. Hỏi có bao nhiêu con voi con?\nA. 8 con\nB. 7 con\nC. 6 con\nD. 9 con",
                "ans_str": "A. 8 con (Tỉ số phần trăm voi con: 100% - 68% = 32%. Số voi con là: 25 × 32% = 8 con)"
            },
            {
                "q": "Giá một chiếc khăn thổ cẩm dệt thủ công ở Buôn Đôn là 250 000 đồng. Cửa hàng giảm giá 10%, sau đó một tuần lại tăng giá thêm 10%. Hỏi giá chiếc khăn lúc này là bao nhiêu?\nA. 247 500 đồng\nB. 250 000 đồng\nC. 245 000 đồng\nD. 252 500 đồng",
                "ans_str": "A. 247 500 đồng (Sau khi giảm 10%, giá còn: 250 000 × 90% = 225 000 đồng. Sau khi tăng lại 10%, giá là: 225 000 × 110% = 247 500 đồng)"
            },
            # Lượt 3
            {
                "q": "Một thửa ruộng hình chữ nhật có chiều dài 50 m, chiều rộng 30 m. Người ta tăng chiều dài thêm 20% và giảm chiều rộng đi 20%. Hỏi diện tích thửa ruộng thay đổi như thế nào?\nA. Giảm 4%\nB. Tăng 4%\nC. Không đổi\nD. Giảm 2%",
                "ans_str": "A. Giảm 4% (Chiều dài mới bằng 120% = 1,2; Chiều rộng mới bằng 80% = 0,8. Diện tích mới bằng: 1,2 × 0,8 = 0,96 = 96% diện tích cũ. Diện tích giảm: 100% - 96% = 4%)"
            },
            {
                "q": "Lượng nước trong hạt cà phê tươi là 20%, trong hạt cà phê phơi khô là 10%. Hỏi phơi 450 kg hạt cà phê tươi thì thu được bao nhiêu ki-lô-gam hạt cà phê khô?\nA. 400 kg\nB. 380 kg\nC. 405 kg\nD. 420 kg",
                "ans_str": "A. 400 kg (Lượng thuần hạt cà phê trong 450 kg cà phê tươi là: 450 × (100% - 20%) = 360 kg. Trong cà phê khô, thuần hạt chiếm: 100% - 10% = 90%. Khối lượng cà phê khô thu được là: 360 : 90% = 400 kg)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 22: ĐẮK NÔNG (HỒ TÀ ĐÙNG) - TUẦN 22
    # =========================================================================
    {
        "tuan": 22,
        "tram_so": 22,
        "ten_tram": "Đắk Nông (Hồ Tà Đùng)",
        "chu_de": "Thể tích của một hình, xăng-ti-mét khối, đề-xi-mét khối, đổi đơn vị thể tích",
        "souvenirs": {
            "cap1": "Huy hiệu Đảo xanh Tà Đùng Đồng (50đ)",
            "cap2": "Thạch anh núi lửa Chư Blúk Bạc (90đ)",
            "cap3": "Vương miện Vịnh Tà Đùng Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "1 đề-xi-mét khối (dm³) bằng bao nhiêu xăng-ti-mét khối (cm³)?", "a": "1 000 cm³"},
            {"q": "1 đề-xi-mét khối (dm³) tương đương với bao nhiêu lít?", "a": "1 lít"},
            {"q": "1 lít bằng bao nhiêu xăng-ti-mét khối?", "a": "1 000 cm³"},
            {"q": "Đổi 4 dm³ sang xăng-ti-mét khối", "a": "4 000 cm³"},
            {"q": "Đổi 2 500 cm³ sang đề-xi-mét khối", "a": "2,5 dm³"},
            {"q": "Hồ Tà Đùng ở Đắk Nông được mệnh danh là danh thắng gì trên Tây Nguyên?", "a": "Vịnh Hạ Long trên Tây Nguyên"},
            {"q": "Hồ Tà Đùng có khoảng bao nhiêu hòn đảo lớn nhỏ nhấp nhô tuyệt đẹp?", "a": "Hơn 40 hòn đảo"},
            {"q": "Hệ thống hang động núi lửa dài nhất Đông Nam Á tại Đắk Nông có tên là gì?", "a": "Hang động núi lửa Chư Blúk"},
            {"q": "Công viên địa chất Đắk Nông được UNESCO công nhận là gì?", "a": "Công viên Địa chất Toàn cầu UNESCO"},
            {"q": "So sánh: 1,5 dm³ và 1 500 cm³", "a": "Bằng nhau (=)"},
            # Lượt 2
            {"q": "Đổi 0,8 dm³ sang xăng-ti-mét khối", "a": "800 cm³"},
            {"q": "Đổi 750 cm³ sang đề-xi-mét khối", "a": "0,75 dm³"},
            {"q": "3 dm³ 50 cm³ bằng bao nhiêu xăng-ti-mét khối?", "a": "3 050 cm³"},
            {"q": "Một hình lập phương có cạnh 1 dm thì thể tích là bao nhiêu?", "a": "1 dm³ (1 000 cm³)"},
            {"q": "Nếu hình A được ghép từ 12 hình lập phương nhỏ 1 cm³ thì thể tích hình A là gì?", "a": "12 cm³"},
            {"q": "Đỉnh núi cao nhất tỉnh Đắk Nông soi bóng xuống Hồ Tà Đùng là đỉnh gì?", "a": "Đỉnh Tà Đùng (1 982 m)"},
            {"q": "Loại đá bán quý lấp lánh hình thành từ dòng dung nham núi lửa Đắk Nông là đá gì?", "a": "Đá thạch anh (hoặc đá Opal, Chalcedony)"},
            {"q": "Sông Đồng Nai đoạn chảy qua Đắk Nông tạo nên hồ chứa thủy điện nào?", "a": "Thủy điện Đồng Nai 3 (Hồ Tà Đùng)"},
            {"q": "So sánh: 2 dm³ 5 cm³ và 2 050 cm³", "a": "2 dm³ 5 cm³ < 2 050 cm³ (vì 2 005 cm³ < 2 050 cm³)"},
            {"q": "Đổi 5 lít sang đề-xi-mét khối", "a": "5 dm³"},
            # Lượt 3
            {"q": "Đổi 12 dm³ sang lít", "a": "12 lít"},
            {"q": "Đổi 3/4 dm³ sang xăng-ti-mét khối", "a": "750 cm³"},
            {"q": "Số thập phân 0,005 dm³ bằng bao nhiêu xăng-ti-mét khối?", "a": "5 cm³"},
            {"q": "Hình hộp chữ nhật được tạo thành từ bao nhiêu mặt hình chữ nhật?", "a": "6 mặt"},
            {"q": "Hình lập phương có mấy đỉnh, mấy cạnh và mấy mặt?", "a": "8 đỉnh, 12 cạnh, 6 mặt"},
            {"q": "Loài vượn má vàng quý hiếm được bảo tồn nghiêm ngặt tại VQG Tà Đùng là gì?", "a": "Vượn đen má hung (má vàng)"},
            {"q": "Dân tộc Mạ và M’Nông ở Đắk Nông có sử thi truyền miệng nổi tiếng là gì?", "a": "Sử thi Ot Ndrong"},
            {"q": "Tính: 350 cm³ + 650 cm³ bằng bao nhiêu dm³?", "a": "1 dm³"},
            {"q": "Tính: 5 dm³ - 1 200 cm³ bằng bao nhiêu cm³?", "a": "3 800 cm³"},
            {"q": "Đổi 1/2 lít sang xăng-ti-mét khối", "a": "500 cm³"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một can đựng nước khoáng mang theo thám hiểm Hồ Tà Đùng có thể tích 5 dm³. Đổi thể tích can nước sang xăng-ti-mét khối là ... cm³.", "a": "5000"},
            {"q": "Một bể kính nuôi cá cảnh nhỏ hình hộp chữ nhật có thể tích 24 dm³. Hiện tại bể chứa 3/4 thể tích nước. Lượng nước trong bể là ... lít.", "a": "18"},
            {"q": "Một khối đá thạch anh Chư Blúk có thể tích 1 250 cm³. Đổi thể tích khối đá này sang đề-xi-mét khối dưới dạng số thập phân là ... dm³.", "a": "1,25"},
            {"q": "Một hộp quà lưu niệm lưu giữ đất bazan Tà Đùng hình lập phương có cạnh 8 cm. Thể tích hộp quà đó là ... cm³.", "a": "512"},
            # Lượt 2
            {"q": "Một thuyền du lịch chạy trên Hồ Tà Đùng tiêu thụ hết 12,5 lít dầu cho chuyến đi 2 giờ. Thể tích dầu tiêu thụ đổi ra đề-xi-mét khối là ... dm³.", "a": "12,5"},
            {"q": "Người ta xếp các khối lập phương nhỏ 1 cm³ thành một hình hộp chữ nhật có chiều dài 6 cm, chiều rộng 4 cm, chiều cao 5 cm. Cần tất cả ... khối lập phương nhỏ.", "a": "120"},
            {"q": "Một bình nước hình trụ có thể tích 1,8 dm³. Người ta đã uống hết 650 cm³ nước. Lượng nước còn lại trong bình là ... cm³.", "a": "1150"},
            {"q": "Tìm x, biết: x dm³ + 450 cm³ = 2 dm³. Giá trị của x là ... (nhập số thập phân).", "a": "1,55"},
            # Lượt 3
            {"q": "Hồ Tà Đùng có hơn 40 đảo lớn nhỏ, một hòn đảo đất đỏ có diện tích mặt nước bao quanh hình tam giác với đáy 150 m và chiều cao 80 m. Diện tích mặt nước là ... m².", "a": "6000"},
            {"q": "Một thùng nhựa chứa nước sinh hoạt trên nhà bè Tà Đùng có thể tích 120 dm³. Người ta dùng một xô 15 dm³ để múc nước. Cần múc ... xô thì đầy thùng.", "a": "8"},
            {"q": "Đổi 4 080 cm³ sang đề-xi-mét khối ta được kết quả là ... dm³.", "a": "4,08"},
            {"q": "Một khối gỗ lũa Tà Đùng chiếm thể tích 3,5 dm³, nặng 2,8 kg. Một khối gỗ cùng loại có thể tích 5 dm³ sẽ nặng ... kg.", "a": "4"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một hình lập phương A có cạnh 4 cm. Một hình lập phương B có cạnh dài gấp đôi cạnh hình lập phương A. Hỏi thể tích hình lập phương B gấp mấy lần thể tích hình lập phương A?\nA. 8 lần\nB. 4 lần\nC. 6 lần\nD. 2 lần",
                "ans_str": "A. 8 lần (Khi cạnh gấp 2 lần thì thể tích gấp: 2 × 2 × 2 = 8 lần)"
            },
            {
                "q": "Người ta dùng các hình lập phương nhỏ cạnh 1 cm để xếp thành một hình hộp chữ nhật có kích thước dài 8 cm, rộng 6 cm, cao 5 cm rồi sơn tất cả 6 mặt ngoài. Hỏi có bao nhiêu hình lập phương nhỏ được sơn đúng 2 mặt?\nA. 52 hình\nB. 48 hình\nC. 60 hình\nD. 56 hình",
                "ans_str": "A. 52 hình (Các khối sơn 2 mặt nằm ở các cạnh trừ đi các góc: 4 × (8 - 2) + 4 × (6 - 2) + 4 × (5 - 2) = 4 × 6 + 4 × 4 + 4 × 3 = 24 + 16 + 12 = 52 hình)"
            },
            # Lượt 2
            {
                "q": "Một bể kính nuôi cá hình hộp chữ nhật có chiều dài 40 cm, chiều rộng 25 cm và mực nước đang cao 15 cm. Người ta thả vào bể một khối đá san hô thì thấy nước dâng lên cao 18 cm. Tính thể tích của khối đá san hô đó.\nA. 3 000 cm³ (3 dm³)\nB. 2 500 cm³\nC. 3 500 cm³\nD. 4 000 cm³",
                "ans_str": "A. 3 000 cm³ (3 dm³) (Mực nước dâng thêm: 18 - 15 = 3 cm. Thể tích khối đá bằng thể tích nước dâng lên: 40 × 25 × 3 = 3 000 cm³ = 3 dm³)"
            },
            {
                "q": "Người ta xếp 216 khối lập phương nhỏ cạnh 1 cm thành một khối lập phương lớn. Hỏi cạnh của khối lập phương lớn dài bao nhiêu xăng-ti-mét?\nA. 6 cm\nB. 8 cm\nC. 7 cm\nD. 5 cm",
                "ans_str": "A. 6 cm (Ta có: 6 × 6 × 6 = 216. Vậy cạnh khối lập phương lớn dài 6 cm)"
            },
            # Lượt 3
            {
                "q": "Một bình chứa nước dạng hình hộp chữ nhật có đáy là hình vuông cạnh 20 cm, đang chứa 6 lít nước. Hỏi chiều cao của cột nước trong bình là bao nhiêu xăng-ti-mét?\nA. 15 cm\nB. 12 cm\nC. 18 cm\nD. 20 cm",
                "ans_str": "A. 15 cm (6 lít = 6 dm³ = 6 000 cm³. Diện tích đáy bình: 20 × 20 = 400 cm². Chiều cao mực nước: 6 000 : 400 = 15 cm)"
            },
            {
                "q": "Một thuyền du lịch chở 12 người tham quan Hồ Tà Đùng. Vé người lớn là 120 000 đồng, vé trẻ em là 80 000 đồng. Tổng số tiền vé thu được là 1 200 000 đồng. Hỏi đoàn có bao nhiêu người lớn?\nA. 6 người lớn\nB. 8 người lớn\nC. 7 người lớn\nD. 5 người lớn",
                "ans_str": "A. 6 người lớn (Giả sử cả 12 người đều mua vé trẻ em thì hết: 12 × 80 000 = 960 000 đồng. Số tiền hụt đi: 1 200 000 - 960 000 = 240 000 đồng. Chênh lệch mỗi vé: 120 000 - 80 000 = 40 000 đồng. Số người lớn là: 240 000 : 40 000 = 6 người)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 23: PHÚ YÊN (GÀNH ĐÁ ĐĨA & MŨI ĐIỆN) - TUẦN 23
    # =========================================================================
    {
        "tuan": 23,
        "tram_so": 23,
        "ten_tram": "Phú Yên (Gành Đá Đĩa & Mũi Điện)",
        "chu_de": "Mét khối, bảng đơn vị đo thể tích, hình khai triển hình lập phương và hình hộp chữ nhật",
        "souvenirs": {
            "cap1": "Phiến đá lục giác Bazan Đồng (50đ)",
            "cap2": "Hải đăng Mũi Điện Bạc (90đ)",
            "cap3": "Ánh bình minh Đại Lãnh Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "1 mét khối (m³) bằng bao nhiêu đề-xi-mét khối (dm³)?", "a": "1 000 dm³"},
            {"q": "1 mét khối (m³) bằng bao nhiêu xăng-ti-mét khối (cm³)?", "a": "1 000 000 cm³"},
            {"q": "1 mét khối nước chứa được bao nhiêu lít nước?", "a": "1 000 lít"},
            {"q": "Đổi 3,5 m³ sang đề-xi-mét khối", "a": "3 500 dm³"},
            {"q": "Đổi 4 200 dm³ sang mét khối", "a": "4,2 m³"},
            {"q": "Kỳ quan thiên nhiên gồm hàng vạn cột đá bazan hình lục giác xếp chồng tại Phú Yên là gì?", "a": "Gành Đá Đĩa (Ghềnh Đá Đĩa)"},
            {"q": "Ngọn hải đăng cổ kính tại Mũi Đại Lãnh (Phú Yên) đón ánh bình minh đầu tiên tên là gì?", "a": "Hải đăng Mũi Điện"},
            {"q": "Vịnh biển lịch sử nơi gắn liền với huyền thoại Tàu Không Số đường Hồ Chí Minh trên biển là gì?", "a": "Vịnh Vũng Rô"},
            {"q": "Đầm nước lợ trứ danh nức tiếng với đặc sản sò huyết ở Phú Yên là đầm nào?", "a": "Đầm Ô Loan"},
            {"q": "Hình khai triển của một hình lập phương gồm bao nhiêu hình vuông bằng nhau?", "a": "6 hình vuông bằng nhau"},
            # Lượt 2
            {"q": "Đổi 0,25 m³ sang đề-xi-mét khối", "a": "250 dm³"},
            {"q": "Đổi 850 000 cm³ sang mét khối", "a": "0,85 m³"},
            {"q": "Đổi 1/2 m³ sang lít", "a": "500 lít"},
            {"q": "Một hình lập phương có cạnh 1 m thì thể tích là bao nhiêu?", "a": "1 m³"},
            {"q": "Mỗi đơn vị đo thể tích liền kề gấp hoặc kém nhau bao nhiêu lần?", "a": "1 000 lần"},
            {"q": "Gành Đá Đĩa được hình thành do dòng dung nham núi lửa gặp phải cái gì rồi đông cứng?", "a": "Gặp nước biển lạnh"},
            {"q": "Bãi biển cong cong tuyệt đẹp nằm ngay dưới chân ngọn hải đăng Mũi Điện là bãi gì?", "a": "Bãi Môn"},
            {"q": "Tháp Chăm cổ kính tọa lạc trên đỉnh núi Nhạn bên dòng sông Đà Rằng là tháp gì?", "a": "Tháp Nhạn"},
            {"q": "Tính: 2 m³ 50 dm³ bằng bao nhiêu mét khối?", "a": "2,05 m³"},
            {"q": "Hình hộp chữ nhật có bao nhiêu đường chéo chính nối các đỉnh đối diện?", "a": "4 đường chéo"},
            # Lượt 3
            {"q": "Đổi 15 m³ sang lít", "a": "15 000 lít"},
            {"q": "Đổi 7 500 lít sang mét khối", "a": "7,5 m³"},
            {"q": "Đổi 0,008 m³ sang xăng-ti-mét khối", "a": "8 000 cm³"},
            {"q": "Tính: 1,2 m³ + 800 dm³ bằng bao nhiêu mét khối?", "a": "2 m³"},
            {"q": "Tính: 3 m³ - 1 500 lít bằng bao nhiêu lít?", "a": "1 500 lít"},
            {"q": "Bộ phim điện ảnh nổi tiếng chuyển thể từ truyện của Nguyễn Nhật Ánh quay tại Phú Yên là gì?", "a": "Tôi thấy hoa vàng trên cỏ xanh"},
            {"q": "Cây cầu gỗ dài nhất Việt Nam bắc qua đầm Bình Bá ở Phú Yên là cầu gì?", "a": "Cầu gỗ Ông Cọp"},
            {"q": "Cột mốc tọa độ Mũi Điện đánh dấu điểm cực gì trên đất liền nước ta?", "a": "Điểm cực Đông trên đất liền"},
            {"q": "Số mét khối ký hiệu bằng chữ gì?", "a": "m³"},
            {"q": "Hình lập phương có cạnh 2 m thì thể tích là bao nhiêu m³?", "a": "8 m³ (2 × 2 × 2 = 8)"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một bể chứa nước ngọt cho trạm gác hải đăng Mũi Điện hình hộp chữ nhật có thể tích 15 m³. Hiện tại bể chứa 80% nước. Thể tích nước có trong bể là ... lít.", "a": "12000"},
            {"q": "Đoàn tàu Không Số vận chuyển vũ khí cập bến Vũng Rô: một khoang tàu có thể tích 45 m³. Thể tích khoang tàu đó đổi ra đề-xi-mét khối là ... dm³.", "a": "45000"},
            {"q": "Một khối đá bazan hình lăng trụ lục giác ở Gành Đá Đĩa có thể tích 0,45 m³. Khối đá đó có thể tích là ... dm³.", "a": "450"},
            {"q": "Tìm x, biết: x m³ - 1 200 dm³ = 2,8 m³. Giá trị của x là ...", "a": "4"},
            # Lượt 2
            {"q": "Một xe téc chở nước sinh hoạt ra hải đăng Mũi Điện chứa được 8 m³ nước. Người ta dùng máy bơm với công suất 2,5 m³/giờ. Bơm đầy xe téc sau ... giờ (làm tròn số thập phân).", "a": "3,2"},
            {"q": "Tháp Nhạn có bệ tháp hình vuông mỗi cạnh dài 10 m. Chu vi chân tháp Nhạn là ... m.", "a": "40"},
            {"q": "Một bể nuôi sò huyết Ô Loan hình chữ nhật chứa 24 m³ nước biển. Biết chiều dài 6 m, chiều rộng 4 m. Mực nước trong bể sâu ... m.", "a": "1"},
            {"q": "Tính giá trị biểu thức: 4,5 m³ + 2 500 dm³ : 1 000. Kết quả là ... m³.", "a": "7"},
            # Lượt 3
            {"q": "Hải đăng Mũi Điện cao 26,5 m so với mặt đất và cao 110 m so với mực nước biển. Ánh đèn hải đăng quét xa 27 hải lý (~50 km). Đổi 50 km ra mét là ... m.", "a": "50000"},
            {"q": "Một hòm thư chứa nhật ký trên đỉnh Mũi Điện hình hộp chữ nhật có thể tích 18 dm³. Đổi thể tích này sang mét khối là ... m³.", "a": "0,018"},
            {"q": "Một hồ chứa nước trên núi Nhạn có thể tích 120 m³. Đã xả ra 3/4 lượng nước. Trong hồ còn lại ... lít nước.", "a": "30000"},
            {"q": "Tìm y, biết: y × 1,5 = 4,5 m³. Giá trị của y là ... m³.", "a": "3"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một bể nước ngầm phục vụ trạm Hải đăng Mũi Điện hình hộp chữ nhật có chiều dài 4 m, chiều rộng 2,5 m và chiều sâu 2 m. Hiện bể đang cạn. Người ta mở hai vòi nước cùng chảy vào bể: vòi 1 chảy 1,5 m³/giờ, vòi 2 chảy 1 m³/giờ. Hỏi sau bao lâu bể đầy nước?\nA. 8 giờ\nB. 10 giờ\nC. 7,5 giờ\nD. 9 giờ",
                "ans_str": "A. 8 giờ (Thể tích bể: 4 × 2,5 × 2 = 20 m³. Cả 2 vòi 1 giờ chảy: 1,5 + 1 = 2,5 m³. Thời gian đầy bể: 20 : 2,5 = 8 giờ)"
            },
            {
                "q": "Một chiếc tàu du lịch chạy từ bến Vũng Rô ra Mũi Điện dài 12 km hết 36 phút. Khi về xuôi gió tàu chạy nhanh hơn 4 km/giờ. Tính thời gian tàu chạy từ Mũi Điện về lại Vũng Rô.\nA. 30 phút\nB. 32 phút\nC. 33 phút\nD. 28 phút",
                "ans_str": "A. 30 phút (Đổi: 36 phút = 0,6 giờ. Vận tốc lúc đi là: 12 : 0,6 = 20 (km/giờ). Vận tốc lúc về là: 20 + 4 = 24 (km/giờ). Thời gian tàu chạy lúc về là: 12 : 24 = 0,5 (giờ) = 30 phút)"
            },
            # Lượt 2
            {
                "q": "Người ta làm một chiếc lồng nuôi tôm hùm ở Vũng Rô hình lập phương có cạnh 3 m bằng lưới thép. Hỏi thể tích không gian trong chiếc lồng đó là bao nhiêu mét khối?\nA. 27 m³\nB. 9 m³\nC. 18 m³\nD. 36 m³",
                "ans_str": "A. 27 m³ (Thể tích hình lập phương: 3 × 3 × 3 = 27 m³)"
            },
            {
                "q": "Một tấm bìa hình chữ nhật có kích thước 40 cm và 30 cm. Người ta cắt bỏ ở 4 góc 4 hình vuông bằng nhau có cạnh 5 cm rồi gấp các mép lên để được một chiếc hộp không nắp. Tính thể tích của chiếc hộp đó.\nA. 3 000 cm³ (3 dm³)\nB. 2 500 cm³\nC. 3 500 cm³\nD. 4 000 cm³",
                "ans_str": "A. 3 000 cm³ (3 dm³) (Chiều dài đáy hộp: 40 - 2 × 5 = 30 cm. Chiều rộng đáy hộp: 30 - 2 × 5 = 20 cm. Chiều cao hộp là 5 cm. Thể tích hộp: 30 × 20 × 5 = 3 000 cm³ = 3 dm³)"
            },
            # Lượt 3
            {
                "q": "Một khối đá bazan Gành Đá Đĩa nặng 2,6 tấn. Biết 1 m³ đá đó nặng 2,5 tấn. Hỏi thể tích của khối đá bazan đó là bao nhiêu mét khối?\nA. 1,04 m³\nB. 1,05 m³\nC. 1,08 m³\nD. 1,02 m³",
                "ans_str": "A. 1,04 m³ (Thể tích khối đá: 2,6 : 2,5 = 1,04 m³)"
            },
            {
                "q": "Một khách du lịch đến Mũi Điện đón bình minh. Người đó leo 1 000 bậc thang đá từ chân núi lên đỉnh hải đăng. Cứ leo được 100 bậc thì dừng nghỉ 1 phút. Mỗi bậc thang bước mất 1,5 giây. Hỏi người đó lên tới đỉnh hải đăng sau bao lâu?\nA. 34 phút\nB. 30 phút\nC. 35 phút\nD. 32 phút",
                "ans_str": "A. 34 phút (Thời gian bước: 1 000 × 1,5 = 1 500 giây = 25 phút. Số lần nghỉ: 1 000 : 100 - 1 = 9 lần nghỉ (lên tới đỉnh không tính nghỉ trên đường). Thời gian nghỉ: 9 × 1 = 9 phút. Tổng thời gian: 25 + 9 = 34 phút)"
            }
        ]
    },

    # =========================================================================
    # TRẠM 24: KHÁNH HÒA (VỊNH NHA TRANG, THÁP TRẦM HƯƠNG) - TUẦN 24
    # =========================================================================
    {
        "tuan": 24,
        "tram_so": 24,
        "ten_tram": "Khánh Hòa (Vịnh Nha Trang, Tháp Trầm Hương)",
        "chu_de": "Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật",
        "souvenirs": {
            "cap1": "Vỏ ốc ngọc Nha Trang Đồng (50đ)",
            "cap2": "Tháp Trầm Hương Bạc (90đ)",
            "cap3": "San hô biển Ngọc Hoàng Kim Vàng (100đ)"
        },
        "v1": [
            # Lượt 1
            {"q": "Công thức tính diện tích xung quanh của hình hộp chữ nhật là gì?", "a": "Sxq = Chu vi đáy × Chiều cao = (a + b) × 2 × c"},
            {"q": "Công thức tính diện tích toàn phần của hình hộp chữ nhật là gì?", "a": "Stp = Sxq + 2 × Sđáy = Sxq + 2 × a × b"},
            {"q": "Diện tích xung quanh của hình hộp chữ nhật bằng tổng diện tích của mấy mặt bên?", "a": "4 mặt bên"},
            {"q": "Diện tích toàn phần của hình hộp chữ nhật bằng tổng diện tích của mấy mặt?", "a": "6 mặt"},
            {"q": "Tính diện tích xung quanh của hình hộp chữ nhật có chu vi đáy 20 cm, chiều cao 5 cm", "a": "100 cm²"},
            {"q": "Tháp biểu tượng kiến trúc hình búp sen màu cam hồng bên bờ biển Nha Trang là tháp gì?", "a": "Tháp Trầm Hương"},
            {"q": "Quần thể đền tháp Chăm Pa cổ kính trên đồi Cù Lao nhìn ra cửa sông Cái Nha Trang là gì?", "a": "Tháp Bà Ponagar"},
            {"q": "Vịnh Nha Trang được công nhận là một trong 29 vịnh biển đẹp nhất thế giới vào năm nào?", "a": "Năm 2003"},
            {"q": "Hòn đảo lớn nhất trong Vịnh Nha Trang nơi có khu vui chơi giải trí VinWonders là đảo nào?", "a": "Đảo Hòn Tre"},
            {"q": "Viện nghiên cứu hải dương học lâu đời và quy mô hàng đầu Đông Nam Á tại Nha Trang là gì?", "a": "Viện Hải dương học Nha Trang"},
            # Lượt 2
            {"q": "Một hình hộp chữ nhật có chiều dài 6 cm, chiều rộng 4 cm và chiều cao 5 cm. Tính chu vi đáy", "a": "20 cm ((6 + 4) × 2 = 20)"},
            {"q": "Một hình hộp chữ nhật có dài 6 cm, rộng 4 cm, cao 5 cm. Tính diện tích 2 đáy", "a": "48 cm² (2 × 6 × 4 = 48)"},
            {"q": "Một hình hộp chữ nhật có dài 6 cm, rộng 4 cm, cao 5 cm. Tính diện tích xung quanh", "a": "100 cm² (20 × 5 = 100)"},
            {"q": "Một hình hộp chữ nhật có dài 6 cm, rộng 4 cm, cao 5 cm. Tính diện tích toàn phần", "a": "148 cm² (100 + 48 = 148)"},
            {"q": "Hộp không có nắp thì diện tích toàn phần gồm diện tích xung quanh cộng thêm mấy đáy?", "a": "1 đáy"},
            {"q": "Đặc sản tự nhiên vô cùng quý hiếm trên các đảo đá vôi Khánh Hòa là gì?", "a": "Tổ yến (Yến sào Khánh Hòa)"},
            {"q": "Khánh Hòa được mệnh danh trong câu thơ dân gian là xứ sở của hai thứ gì?", "a": "Xứ Trầm biển Yến"},
            {"q": "Khu bảo tồn biển đầu tiên của Việt Nam nằm tại hòn đảo nào trong Vịnh Nha Trang?", "a": "Đảo Hòn Mun"},
            {"q": "Tính diện tích xung quanh hình hộp chữ nhật có đáy vuông cạnh 3 cm, chiều cao 4 cm", "a": "48 cm² (12 × 4 = 48)"},
            {"q": "Nếu chiều cao hình hộp chữ nhật gấp 2 lần, chu vi đáy giữ nguyên thì diện tích xung quanh thay đổi thế nào?", "a": "Gấp 2 lần"},
            # Lượt 3
            {"q": "Tính diện tích toàn phần hình hộp chữ nhật có dài 5 cm, rộng 2 cm, cao 3 cm", "a": "62 cm² (Sxq = 42, 2Sđáy = 20)"},
            {"q": "Một hình hộp chữ nhật có Sxq = 80 cm², chiều cao 4 cm. Chu vi đáy là bao nhiêu cm?", "a": "20 cm (80 : 4 = 20)"},
            {"q": "Tính diện tích 1 mặt đáy hình hộp chữ nhật biết dài 1,5 m và rộng 0,8 m", "a": "1,2 m²"},
            {"q": "Hồ cá nhân tạo độc đáo hình con tàu cổ hóa thạch ngoài đảo Nha Trang là hồ cá nào?", "a": "Hồ cá Trí Nguyên (Hòn Miễu)"},
            {"q": "Vịnh biển kín gió nước sâu bậc nhất nước ta nằm ở phía bắc Khánh Hòa là vịnh gì?", "a": "Vịnh Cam Ranh"},
            {"q": "Tháp Bà Ponagar được xây dựng để thờ nữ thần nào trong tín ngưỡng Chăm Pa?", "a": "Nữ thần Thiên Y A Na (Po Nagar)"},
            {"q": "Cáp treo vượt biển nối đất liền Nha Trang ra đảo Hòn Tre dài bao nhiêu mét?", "a": "Khoảng 3 320 m"},
            {"q": "Tính diện tích một hộp chữ nhật không nắp có dài 4 dm, rộng 3 dm và cao 2 dm", "a": "40 dm² (Sxq = 28, Sđáy = 12)"},
            {"q": "Hình lập phương có phải là trường hợp đặc biệt của hình hộp chữ nhật không?", "a": "Có (khi dài = rộng = cao)"},
            {"q": "Đổi 2,4 m² sang đề-xi-mét vuông", "a": "240 dm²"}
        ],
        "v2": [
            # Lượt 1
            {"q": "Một thùng các-tông đựng tổ yến sào Nha Trang hình hộp chữ nhật có chiều dài 40 cm, chiều rộng 30 cm và chiều cao 20 cm. Diện tích xung quanh chiếc thùng đó là ... cm².", "a": "2800"},
            {"q": "Bác thợ mộc làm một bể kính nuôi cá cảnh biển Nha Trang (không có nắp) dài 80 cm, rộng 50 cm và cao 45 cm. Diện tích kính cần dùng để làm bể là ... cm².", "a": "15700"},
            {"q": "Người ta sơn toàn bộ 4 bức tường xung quanh một phòng trưng bày trầm hương dài 8 m, rộng 5 m và cao 3,5 m. Biết tổng diện tích các cửa là 9 m². Diện tích tường cần sơn là ... m².", "a": "82"},
            {"q": "Một chiếc hộp đựng trầm hương hình hộp chữ nhật có chu vi đáy 48 cm, chiều cao 10 cm và diện tích đáy 140 cm². Diện tích toàn phần của chiếc hộp là ... cm².", "a": "760"},
            # Lượt 2
            {"q": "Một bể bơi mini trong khu nghỉ dưỡng Nha Trang hình hộp chữ nhật dài 12 m, rộng 5 m và sâu 1,5 m. Người ta ốp gạch men toàn bộ đáy và 4 thành bể bơi. Diện tích ốp gạch là ... m².", "a": "111"},
            {"q": "Một khối hộp chữ nhật có diện tích xung quanh là 120 cm², chiều cao 6 cm. Nửa chu vi mặt đáy của khối hộp đó là ... cm.", "a": "10"},
            {"q": "Tuyến cáp treo vượt biển Nha Trang dài 3 320 m. Một cabin chạy với vận tốc 5 m/giây. Thời gian cabin vượt biển là ... giây.", "a": "664"},
            {"q": "Một hộp quà lưu niệm ốc biển Nha Trang có diện tích toàn phần là 240 cm², diện tích xung quanh là 160 cm². Diện tích một mặt đáy của hộp là ... cm².", "a": "40"},
            # Lượt 3
            {"q": "Một phòng học tại Viện Hải dương học dài 9 m, rộng 6 m và cao 4 m. Người ta quét vôi trần nhà và 4 bức tường phía trong. Biết diện tích các cửa sổ là 15 m². Diện tích cần quét vôi là ... m².", "a": "159"},
            {"q": "Một thùng tôn đựng hải sản không nắp có chiều dài 1,2 m; chiều rộng 0,8 m và chiều cao 0,6 m. Diện tích tôn cần dùng làm thùng là ... m².", "a": "3,36"},
            {"q": "Tìm chiều cao của hình hộp chữ nhật có diện tích xung quanh 180 dm², chiều dài 10 dm và chiều rộng 5 dm. Chiều cao là ... dm.", "a": "6"},
            {"q": "Một kiện hàng yến sào hình hộp chữ nhật có kích thước 6 dm, 4 dm và 3 dm. Thể tích kiện hàng đó là ... dm³.", "a": "72"}
        ],
        "v3": [
            # Lượt 1
            {
                "q": "Một bể chứa nước biển nuôi sinh vật biển tại Viện Hải dương học Nha Trang hình hộp chữ nhật có chiều dài 3 m, chiều rộng 2 m và chiều cao 1,5 m. Người ta lát gạch men xung quanh và đáy bể bằng những viên gạch hình vuông cạnh 20 cm. Hỏi cần mua bao nhiêu viên gạch (bỏ qua mép vữa)?\nA. 525 viên\nB. 500 viên\nC. 550 viên\nD. 600 viên",
                "ans_str": "A. 525 viên (Diện tích lát gạch = Sxq + Sđáy = (3 + 2) × 2 × 1,5 + 3 × 2 = 15 + 6 = 21 m² = 210 000 cm². Diện tích 1 viên gạch: 20 × 20 = 400 cm². Số gạch cần dùng: 210 000 : 400 = 525 viên)"
            },
            {
                "q": "Một phòng trưng bày san hô hình hộp chữ nhật có chiều dài 8 m, chiều rộng 5 m và chiều cao 3,5 m. Người ta thuê quét sơn trần nhà và 4 bức tường phía trong phòng với giá 25 000 đồng/m². Biết tổng diện tích các cửa là 12 m². Hỏi chi phí quét sơn là bao nhiêu tiền?\nA. 2 975 000 đồng\nB. 3 000 000 đồng\nC. 2 850 000 đồng\nD. 3 100 000 đồng",
                "ans_str": "A. 2 975 000 đồng (Diện tích quét sơn = Sxq + Strần - Scửa = (8 + 5) × 2 × 3,5 + 8 × 5 - 12 = 91 + 40 - 12 = 119 m². Tiền sơn: 119 × 25 000 = 2 975 000 đồng)"
            },
            # Lượt 2
            {
                "q": "Một hình hộp chữ nhật có chiều dài gấp đôi chiều rộng và chiều cao bằng 4 cm. Biết diện tích xung quanh của hình hộp chữ nhật là 144 cm². Tính diện tích toàn phần của hình hộp chữ nhật đó.\nA. 288 cm²\nB. 240 cm²\nC. 216 cm²\nD. 256 cm²",
                "ans_str": "A. 288 cm² (Chu vi đáy: 144 : 4 = 36 cm. Nửa chu vi đáy: 36 : 2 = 18 cm. Chiều rộng: 18 : (2 + 1) = 6 cm; Chiều dài: 6 × 2 = 12 cm. Diện tích 2 mặt đáy: 2 × 12 × 6 = 144 cm². Diện tích toàn phần: 144 + 144 = 288 cm²)"
            },
            {
                "q": "Một bể bơi hình hộp chữ nhật có chiều dài 25 m, chiều rộng 10 m và sâu 1,8 m. Hiện tại trong bể đã có sẵn 300 m³ nước. Hỏi phải bơm thêm vào bể bao nhiêu mét khối nước nữa để nước đầy tới cách miệng bể 0,3 m?\nA. 75 m³\nB. 100 m³\nC. 125 m³\nD. 150 m³",
                "ans_str": "A. 75 m³ (Mực nước cần đạt: 1,8 - 0,3 = 1,5 m. Thể tích nước cần có: 25 × 10 × 1,5 = 375 m³. Lượng nước cần bơm thêm: 375 - 300 = 75 m³)"
            },
            # Lượt 3
            {
                "q": "Người ta ghép 8 hình lập phương nhỏ cạnh 3 cm thành một hình lập phương lớn. Sau đó sơn toàn bộ các mặt ngoài của hình lập phương lớn. Tính diện tích phần được sơn của hình lập phương lớn.\nA. 216 cm²\nB. 144 cm²\nC. 288 cm²\nD. 180 cm²",
                "ans_str": "A. 216 cm² (Hình lập phương lớn gồm 2 × 2 × 2 = 8 khối nhỏ nên cạnh hình lập phương lớn là: 3 × 2 = 6 cm. Diện tích được sơn: 6 × 6 × 6 = 216 cm²)"
            },
            {
                "q": "Một chiếc tàu cano chở du khách khám phá Vịnh Nha Trang từ bến tàu ra đảo Hòn Mun dài 10 km hết 20 phút. Vận tốc của cano là bao nhiêu km/giờ?\nA. 30 km/giờ\nB. 25 km/giờ\nC. 35 km/giờ\nD. 40 km/giờ",
                "ans_str": "A. 30 km/giờ (20 phút = 1/3 giờ. Vận tốc cano: 10 : 1/3 = 30 km/giờ)"
            }
        ]
    }
]
