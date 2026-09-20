# -*- coding: utf-8 -*-
"""
Script tạo file Word Bộ đề Toán 5 từ Tuần 1 đến Tuần 18 (Trạm 1 - 18)
Dành cho EduBot - BTCT5: Hành trình thám hiểm Xuyên Việt
"""

import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Dữ liệu 18 trạm với đầy đủ 15 câu hỏi/trạm = 270 câu hỏi
STATIONS_DATA = [
    {
        "tuan": 1,
        "tram_so": 1,
        "ten_tram": "Cột cờ Lũng Cú (Hà Giang)",
        "chu_de": "Ôn tập số tự nhiên, 4 phép tính với số tự nhiên, ôn tập phân số cơ bản",
        "questions": [
            ("Số tự nhiên lớn nhất có 6 chữ số khác nhau là số nào?\nA. 999 999\nB. 987 654\nC. 987 650\nD. 897 654", "B. 987 654"),
            ("Giá trị của chữ số 7 trong số 1 785 240 là:\nA. 700\nB. 7 000\nC. 70 000\nD. 700 000", "D. 700 000 (thuộc hàng trăm nghìn)"),
            ("Làm tròn số 482 650 đến hàng chục nghìn ta được số:\nA. 480 000\nB. 482 000\nC. 490 000\nD. 500 000", "A. 480 000 (vì chữ số hàng nghìn là 2 < 5)"),
            ("Tính giá trị biểu thức bằng cách thuận tiện nhất:\n25 × 36 × 4", "3 600\n(25 × 4) × 36 = 100 × 36 = 3 600"),
            ("Phân số nào dưới đây là phân số tối giản?\nA. 15/20\nB. 18/24\nC. 7/12\nD. 9/27", "C. 7/12 (vì tử số và mẫu số không cùng chia hết cho số tự nhiên nào lớn hơn 1)"),
            ("Rút gọn phân số 42/56 về phân số tối giản:", "3/4 (chia cả tử số và mẫu số cho 14)"),
            ("Quy đồng mẫu số hai phân số 2/3 và 3/5 với mẫu số chung nhỏ nhất là 15:", "10/15 và 9/15\n(2/3 = 10/15; 3/5 = 9/15)"),
            ("Phân số nào lớn hơn 1 trong các phân số sau?\nA. 5/6\nB. 9/9\nC. 8/7\nD. 3/4", "C. 8/7 (vì có tử số lớn hơn mẫu số)"),
            ("Số trung bình cộng của ba số 35, 45 và 70 là:", "50\n(35 + 45 + 70) : 3 = 150 : 3 = 50"),
            ("1/4 thế kỷ bằng bao nhiêu năm?", "25 năm\n(100 : 4 = 25 năm)"),
            ("(Toán thực tế địa danh) Lá cờ Tổ quốc đỏ sao vàng trên đỉnh Cột cờ Lũng Cú (Hà Giang) tượng trưng cho 54 dân tộc anh em có diện tích là 54 m², chiều rộng đo được là 6 m. Tính chiều dài của lá cờ Tổ quốc đó.", "9 m\n(Chiều dài = 54 : 6 = 9 m)"),
            ("(Toán thực tế địa danh) Để lên tới chân Cột cờ Lũng Cú (Hà Giang), du khách cần bước qua tất cả 839 bậc đá. Một đoàn học sinh đã leo được 539 bậc đá. Hỏi đoàn học sinh còn phải bước thêm bao nhiêu bậc đá nữa để lên tới chân cột cờ?", "300 bậc đá\n(839 - 539 = 300 bậc đá)"),
            ("(Toán thực tế địa danh) Một vườn trồng hoa tam giác mạch ở xã Lũng Cú hình chữ nhật có chu vi là 160 m, chiều dài hơn chiều rộng 20 m. Tính diện tích của vườn hoa tam giác mạch đó.", "1 500 m²\n- Nửa chu vi: 160 : 2 = 80 m\n- Chiều dài: (80 + 20) : 2 = 50 m\n- Chiều rộng: 50 - 20 = 30 m\n- Diện tích: 50 × 30 = 1 500 m²"),
            ("(Tư duy nâng cao) Tính giá trị biểu thức sau bằng cách thuận tiện nhất:\nA = 1 + 3 + 5 + 7 + ... + 99", "2 500\n- Số số hạng: (99 - 1) : 2 + 1 = 50\n- Tổng: (1 + 99) × 50 : 2 = 2 500"),
            ("(Tư duy nâng cao) Tìm hai số tự nhiên có tổng bằng 198, biết rằng nếu xoá đi chữ số 0 ở tận cùng bên phải số lớn ta được số bé.", "Số bé: 18; Số lớn: 180\n- Xóa chữ số 0 ở tận cùng số lớn được số bé nên số lớn gấp 10 lần số bé.\n- Tổng số phần: 1 + 10 = 11 phần\n- Số bé: 198 : 11 = 18\n- Số lớn: 18 × 10 = 180")
        ]
    },
    {
        "tuan": 2,
        "tram_so": 2,
        "ten_tram": "Hẻm Tu Sản & Sông Nho Quế (Hà Giang)",
        "chu_de": "Phân số thập phân, ôn tập 4 phép tính với phân số (+, -, ×, :)",
        "questions": [
            ("Phân số nào dưới đây là phân số thập phân?\nA. 3/5\nB. 7/100\nC. 4/25\nD. 12/200", "B. 7/100 (phân số có mẫu số là 100)"),
            ("Viết phân số 3/5 thành phân số thập phân có mẫu số là 10 ta được:", "6/10 (nhân cả tử và mẫu với 2)"),
            ("Viết phân số 7/25 thành phân số thập phân có mẫu số là 100 ta được:", "28/100 (nhân cả tử và mẫu với 4)"),
            ("Tính kết quả phép tính: 3/7 + 2/7 =", "5/7"),
            ("Tính kết quả phép tính: 5/6 - 1/4 =", "7/12 (quy đồng MSC 12: 10/12 - 3/12 = 7/12)"),
            ("Tính kết quả phép tính: 4/9 × 3/8 =", "1/6 (rút gọn: (4×3)/(9×8) = 1/6)"),
            ("Tính kết quả phép tính: 5/8 : 15/16 =", "2/3 (5/8 × 16/15 = 2/3)"),
            ("Tìm x, biết: x + 1/3 = 5/6", "x = 1/2\n(x = 5/6 - 1/3 = 3/6 = 1/2)"),
            ("Tìm y, biết: y × 2/5 = 4/15", "y = 2/3\n(y = 4/15 : 2/5 = 4/15 × 5/2 = 2/3)"),
            ("Một hình chữ nhật có chiều dài 4/5 m và chiều rộng 2/3 m. Diện tích hình chữ nhật đó là:", "8/15 m²\n(4/5 × 2/3 = 8/15 m²)"),
            ("(Toán thực tế địa danh) Đội thuyền du lịch đưa khách ngắm Hẻm Tu Sản trên dòng sông Nho Quế (Hà Giang) có 36 chiếc thuyền. Buổi sáng có 5/9 số thuyền đã xuất bến. Hỏi tại bến còn lại bao nhiêu chiếc thuyền đang neo đậu?", "16 chiếc thuyền\n- Số thuyền xuất bến: 36 × 5/9 = 20 chiếc\n- Số thuyền còn lại: 36 - 20 = 16 chiếc"),
            ("(Toán thực tế địa danh) Hẻm Tu Sản là hẻm vực sâu kỳ vĩ dưới chân đèo Mã Pí Lèng. Một chiếc thuyền chở du khách xuôi dòng sông Nho Quế đoạn qua hẻm dài 6 km hết 2/5 giờ. Tính vận tốc xuôi dòng của thuyền.", "15 km/h\n(Vận tốc = 6 : 2/5 = 15 km/h)"),
            ("(Toán thực tế địa danh) Đội tình nguyện viên dọn dẹp vệ sinh môi trường hẻm Tu Sản và dòng sông Nho Quế: ngày thứ nhất vớt được 3/8 tấn rác thải, ngày thứ hai vớt được nhiều hơn ngày thứ nhất 1/4 tấn. Hỏi cả hai ngày đội đã thu gom được bao nhiêu tấn rác thải?", "1 tấn\n- Ngày thứ hai: 3/8 + 1/4 = 5/8 tấn\n- Cả hai ngày: 3/8 + 5/8 = 8/8 = 1 tấn"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n3/5 × 7/9 + 3/5 × 2/9", "3/5\n= 3/5 × (7/9 + 2/9) = 3/5 × 1 = 3/5"),
            ("(Tư duy nâng cao) Tính giá trị biểu thức:\nA = (1 - 1/2) × (1 - 1/3) × (1 - 1/4) × ... × (1 - 1/10)", "1/10\n= 1/2 × 2/3 × 3/4 × ... × 9/10 = 1/10")
        ]
    },
    {
        "tuan": 3,
        "tram_so": 3,
        "ten_tram": "Thác Bản Giốc (Cao Bằng)",
        "chu_de": "Cộng trừ hai phân số khác mẫu số, hỗn số, giải toán phân số",
        "questions": [
            ("Hỗn số 3 2/5 được đọc là:\nA. Ba phần hai mươi lăm\nB. Ba và hai phần năm\nC. Ba mươi hai phần năm\nD. Hai và ba phần năm", "B. Ba và hai phần năm"),
            ("Chuyển hỗn số 4 3/7 thành phân số ta được:", "31/7\n((4 × 7 + 3) / 7 = 31/7)"),
            ("Chuyển phân số 19/4 thành hỗn số ta được:", "4 3/4\n(19 : 4 = 4 dư 3 nên bằng 4 3/4)"),
            ("Tính: 2 1/3 + 1 2/5 =", "3 11/15 (hoặc 56/15)\n(7/3 + 7/5 = 35/15 + 21/15 = 56/15)"),
            ("Tính: 3 1/2 - 1 3/4 =", "1 3/4 (hoặc 7/4)\n(7/2 - 7/4 = 14/4 - 7/4 = 7/4)"),
            ("Điền dấu thích hợp vào chỗ chấm: 2 3/5 ... 2 4/7", ">\n(Phần nguyên bằng nhau, so sánh 3/5 = 21/35 > 4/7 = 20/35)"),
            ("Một cuộn dây thừng dài 5 m, người ta cắt lấy 2 1/4 m. Đoạn dây còn lại dài bao nhiêu mét?", "2 3/4 m (hoặc 11/4 m)\n(5 - 9/4 = 11/4 m = 2 3/4 m)"),
            ("Phân số nghịch đảo của phân số 5/8 là:", "8/5"),
            ("Tìm x, biết: x - 1 1/2 = 2 1/3", "x = 3 5/6 (hoặc 23/6)\n(x = 7/3 + 3/2 = 14/6 + 9/6 = 23/6)"),
            ("Tính: 1 1/2 × 2 2/3 =", "4\n(3/2 × 8/3 = 24/6 = 4)"),
            ("(Toán thực tế địa danh) Thác Bản Giốc (Trùng Khánh, Cao Bằng) có 24 chiếc bè tre phục vụ du khách ngắm thác trên sông Quây Sơn. Buổi sáng có 5/8 số bè tre hoạt động, buổi chiều có 3/4 số bè tre hoạt động. Hỏi buổi chiều có nhiều hơn buổi sáng bao nhiêu chiếc bè tre hoạt động?", "3 chiếc bè tre\n- Buổi sáng: 24 × 5/8 = 15 bè\n- Buổi chiều: 24 × 3/4 = 18 bè\n- Nhiều hơn: 18 - 15 = 3 bè"),
            ("(Toán thực tế địa danh) Một vườn trồng hạt dẻ đặc sản Trùng Khánh (Cao Bằng) gần Thác Bản Giốc: đợt một thu hoạch được 2 1/2 tạ hạt dẻ, đợt hai thu hoạch được nhiều hơn đợt một 3/4 tạ. Hỏi cả hai đợt thu hoạch được bao nhiêu tạ hạt dẻ?", "5 3/4 tạ (hoặc 575 kg)\n- Đợt hai: 5/2 + 3/4 = 13/4 tạ\n- Cả hai đợt: 5/2 + 13/4 = 23/4 tạ = 5 3/4 tạ"),
            ("(Toán thực tế địa danh) Nhóm du khách mua 6 hộp hạt dẻ sấy đặc sản Trùng Khánh hết 480 000 đồng. Hỏi nếu mua 9 hộp hạt dẻ cùng loại như thế thì phải trả bao nhiêu tiền?", "720 000 đồng\n- Giá 1 hộp: 480 000 : 6 = 80 000 đồng\n- Mua 9 hộp: 80 000 × 9 = 720 000 đồng"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n2 3/7 + 1 4/9 + 3 4/7 + 2 5/9", "10\n= (2 3/7 + 3 4/7) + (1 4/9 + 2 5/9)\n= 6 + 4 = 10"),
            ("(Tư duy nâng cao) Một thửa đất hình chữ nhật có chu vi 140 m, chiều dài gấp 4 lần chiều rộng. Tính diện tích thửa đất đó.", "784 m²\n- Nửa chu vi: 140 : 2 = 70 m\n- Chiều rộng: 70 : (1 + 4) = 14 m\n- Chiều dài: 14 × 4 = 56 m\n- Diện tích: 56 × 14 = 784 m²")
        ]
    },
    {
        "tuan": 4,
        "tram_so": 4,
        "ten_tram": "Hồ Ba Bể (Bắc Kạn)",
        "chu_de": "Ôn tập hình học và đo lường (chu vi, diện tích, đơn vị đo độ dài, khối lượng), làm quen số thập phân",
        "questions": [
            ("Điền số thích hợp vào chỗ chấm: 3 m 5 dm = ... dm", "35 dm"),
            ("Điền số thích hợp vào chỗ chấm: 4 tấn 50 kg = ... kg", "4 050 kg"),
            ("Điền số thích hợp vào chỗ chấm: 2 m² 45 dm² = ... dm²", "245 dm²"),
            ("Một hình chữ nhật có chiều dài 18 cm, chiều rộng 12 cm. Diện tích của hình chữ nhật đó là:", "216 cm²\n(18 × 12 = 216 cm²)"),
            ("Một mảnh vườn hình vuông có chu vi 48 m. Diện tích mảnh vườn đó là:", "144 m²\n- Cạnh vườn: 48 : 4 = 12 m\n- Diện tích: 12 × 12 = 144 m²"),
            ("Phân số thập phân 7/10 được viết dưới dạng số thập phân là:", "0,7"),
            ("Phân số thập phân 25/100 được viết dưới dạng số thập phân là:", "0,25"),
            ("Số thập phân 3,45 gồm có những hàng nào?", "3 đơn vị, 4 phần mười và 5 phần trăm"),
            ("Trong số thập phân 8,92, chữ số 9 thuộc hàng nào?", "Hàng phần mười"),
            ("Điền số thích hợp vào chỗ chấm: 5 thế kỷ = ... năm", "500 năm\n(5 × 100 = 500 năm)"),
            ("(Toán thực tế địa danh) Vườn quốc gia Ba Bể (Bắc Kạn) quản lý mặt nước Hồ Ba Bể gồm 3 nhánh hồ thông nhau. Một nhánh hồ có dạng hình chữ nhật dài 3 500 m và rộng 800 m. Tính diện tích mặt nước nhánh hồ đó theo đơn vị mét vuông.", "2 800 000 m² (hay 2,8 km²)\n(3 500 × 800 = 2 800 000 m²)"),
            ("(Toán thực tế địa danh) Một hợp tác xã khai thác cá sinh thái tại Hồ Ba Bể ngày thứ nhất đánh bắt được 1 tấn 250 kg cá, ngày thứ hai đánh bắt được bằng 4/5 ngày thứ nhất. Hỏi cả hai ngày hợp tác xã đã đánh bắt được bao nhiêu ki-lô-gam cá?", "2 250 kg cá\n- Ngày 1: 1 250 kg\n- Ngày 2: 1 250 × 4/5 = 1 000 kg\n- Cả hai ngày: 1 250 + 1 000 = 2 250 kg"),
            ("(Toán thực tế địa danh) Bến thuyền đón khách ngắm đảo Bà Góa trên Hồ Ba Bể là một khoảng sân hình chữ nhật có chu vi 120 m, chiều dài hơn chiều rộng 10 m. Tính diện tích khoảng sân bến thuyền.", "875 m²\n- Nửa chu vi: 120 : 2 = 60 m\n- Chiều dài: (60 + 10) : 2 = 35 m\n- Chiều rộng: 35 - 10 = 25 m\n- Diện tích: 35 × 25 = 875 m²"),
            ("(Tư duy nâng cao) Một thửa đất hình chữ nhật có chu vi 160 m. Nếu tăng chiều rộng thêm 10 m và giảm chiều dài đi 10 m thì mảnh đất trở thành hình vuông. Tính diện tích ban đầu của thửa đất.", "1 500 m²\n- Nửa chu vi: 160 : 2 = 80 m\n- Dài hơn rộng: 10 + 10 = 20 m\n- Chiều dài: (80 + 20) : 2 = 50 m\n- Chiều rộng: 30 m\n- Diện tích: 50 × 30 = 1 500 m²"),
            ("(Tư duy nâng cao) Viết phân số 3/8 dưới dạng số thập phân.", "0,375\n(3 : 8 = 0,375)")
        ]
    },
    {
        "tuan": 5,
        "tram_so": 5,
        "ten_tram": "Mù Cang Chải (Yên Bái)",
        "chu_de": "Khái niệm số thập phân, so sánh và xếp thứ tự các số thập phân",
        "questions": [
            ("Số thập phân gồm có \"Năm đơn vị, bảy phần mười, hai phần trăm\" được viết là:", "5,72"),
            ("Giá trị của chữ số 5 trong số thập phân 12,358 là:", "5/100 (hoặc 0,05)"),
            ("Điền dấu thích hợp vào chỗ chấm: 4,52 ... 4,509", "> (vì 4,520 > 4,509)"),
            ("Điền dấu thích hợp vào chỗ chấm: 12,08 ... 12,8", "< (vì 12,08 < 12,80)"),
            ("Sắp xếp các số sau theo thứ tự từ bé đến lớn: 3,45 ; 3,54 ; 3,05 ; 3,504", "3,05 ; 3,45 ; 3,504 ; 3,54"),
            ("Sắp xếp các số sau theo thứ tự từ lớn đến bé: 8,25 ; 8,2 ; 8,19 ; 8,09", "8,25 ; 8,2 ; 8,19 ; 8,09"),
            ("Tìm chữ số x, biết: 9,7x2 < 9,712", "x = 0"),
            ("Tìm số tự nhiên x thỏa mãn: 4,8 < x < 5,9", "x = 5"),
            ("Số thập phân nào dưới đây bằng số 0,6?\nA. 0,06\nB. 0,60\nC. 0,006\nD. 6,0", "B. 0,60"),
            ("Số thập phân 45,080 có thể viết gọn là:", "45,08 (bỏ chữ số 0 ở tận cùng bên phải phần thập phân)"),
            ("(Toán thực tế địa danh) Trong lễ hội dù lượn \"Bay trên mùa vàng\" tại đèo Khau Phạ (Mù Cang Chải), bốn phi công đã bay lượn với thời gian: phi công A bay 1,45 giờ; phi công B bay 1,5 giờ; phi công C bay 1,38 giờ; phi công D bay 1,405 giờ. Hỏi phi công nào bay lâu nhất và phi công nào bay ít thời gian nhất?", "Phi công B bay lâu nhất (1,5 giờ);\nPhi công C bay ít thời gian nhất (1,38 giờ)"),
            ("(Toán thực tế địa danh) Một thửa ruộng bậc thang tại đồi Mâm Xôi (La Pán Tẩn, Mù Cang Chải) có năng suất lúa nếp nương của 3 mùa vụ liên tiếp lần lượt là 4,5 tấn/ha; 4,38 tấn/ha và 4,62 tấn/ha. Tính năng suất trung bình của thửa ruộng qua 3 mùa vụ.", "4,5 tấn/ha\n((4,5 + 4,38 + 4,62) : 3 = 13,5 : 3 = 4,5 tấn/ha)"),
            ("(Toán thực tế địa danh) Bạn Vàng A Páo ở Mù Cang Chải giúp gia đình cân hai gùi thóc nếp nương: gùi thứ nhất nặng 18,5 kg; gùi thứ hai nặng hơn gùi thứ nhất 1,25 kg. Hỏi cả hai gùi thóc nặng bao nhiêu ki-lô-gam?", "38,25 kg\n- Gùi thứ hai: 18,5 + 1,25 = 19,75 kg\n- Cả hai gùi: 18,5 + 19,75 = 38,25 kg"),
            ("(Tư duy nâng cao) Tìm số tự nhiên x lớn nhất sao cho: x < 2026,05", "x = 2026"),
            ("(Tư duy nâng cao) Tìm một số thập phân x có hai chữ số ở phần thập phân sao cho: 0,1 < x < 0,2", "0,15 (hoặc bất kỳ số nào từ 0,11 đến 0,19)")
        ]
    },
    {
        "tuan": 6,
        "tram_so": 6,
        "ten_tram": "Đỉnh Fansipan (Lào Cai)",
        "chu_de": "Viết số đo đại lượng dưới dạng số thập phân, làm tròn số thập phân",
        "questions": [
            ("Viết số đo 5 m 6 dm dưới dạng số thập phân với đơn vị mét là:", "5,6 m"),
            ("Viết số đo 3 m 4 cm dưới dạng số thập phân với đơn vị mét là:", "3,04 m"),
            ("Viết số đo 8 km 450 m dưới dạng số thập phân với đơn vị ki-lô-mét là:", "8,45 km (hoặc 8,450 km)"),
            ("Viết số đo 4 kg 250 g dưới dạng số thập phân với đơn vị ki-lô-gam là:", "4,25 kg"),
            ("Viết số đo 7 tấn 80 kg dưới dạng số thập phân với đơn vị tấn là:", "7,08 tấn"),
            ("Làm tròn số thập phân 18,74 đến hàng đơn vị ta được số:", "19 (vì chữ số hàng phần mười là 7 ≥ 5)"),
            ("Làm tròn số thập phân 24,368 đến hàng phần mười (chữ số thập phân thứ nhất) ta được số:", "24,4 (vì chữ số hàng phần trăm là 6 ≥ 5)"),
            ("Làm tròn số thập phân 9,254 đến hàng phần trăm (chữ số thập phân thứ hai) ta được số:", "9,25 (vì chữ số hàng phần nghìn là 4 < 5)"),
            ("Viết khoảng thời gian 15 phút dưới dạng phân số và số thập phân của giờ:", "1/4 giờ = 0,25 giờ"),
            ("Điền số thích hợp vào chỗ chấm: 450 cm² = ... dm²", "4,5 dm² (450 : 100 = 4,5)"),
            ("(Toán thực tế địa danh) Đỉnh Fansipan (Lào Cai) - \"Nóc nhà Đông Dương\" có độ cao chính xác là 3 143 m so với mực nước biển. Hãy viết độ cao này dưới dạng số thập phân có đơn vị là ki-lô-mét và làm tròn đến hàng phần mười.", "3,143 km; Làm tròn đến hàng phần mười được 3,1 km"),
            ("(Toán thực tế địa danh) Một cabin cáp treo Fansipan 3 dây chở tối đa 35 hành khách. Nếu mỗi hành khách có cân nặng trung bình khoảng 62 kg thì tổng khối lượng hành khách trong một chuyến cabin đầy là bao nhiêu tấn?", "2,17 tấn\n(35 × 62 = 2 170 kg = 2,17 tấn)"),
            ("(Toán thực tế địa danh) Nhiệt độ đo được trên đỉnh Fansipan vào ba thời điểm trong ngày mùa đông lần lượt là: -1,5 °C; 2,4 °C và 0,6 °C. Hãy sắp xếp các nhiệt độ đó theo thứ tự từ thấp đến cao.", "-1,5 °C ; 0,6 °C ; 2,4 °C"),
            ("(Tư duy nâng cao) Một thanh sắt dài 2,4 m nặng 18 kg. Hỏi một thanh sắt cùng loại dài 3,6 m nặng bao nhiêu ki-lô-gam?", "27 kg\n- 1 m nặng: 18 : 2,4 = 7,5 kg\n- Thanh 3,6 m nặng: 7,5 × 3,6 = 27 kg"),
            ("(Tư duy nâng cao) Số thập phân x có hai chữ số ở phần thập phân. Khi làm tròn x đến hàng phần mười ta được số 8,5. Biết x > 8,5. Tìm giá trị lớn nhất có thể của x.", "x = 8,54\n(vì 8,54 làm tròn thành 8,5; còn 8,55 làm tròn thành 8,6)")
        ]
    },
    {
        "tuan": 7,
        "tram_so": 7,
        "ten_tram": "Thủ đô Hà Nội",
        "chu_de": "Ki-lô-mét vuông, héc-ta, bảng đơn vị đo diện tích, viết số đo diện tích dạng số thập phân",
        "questions": [
            ("Điền số thích hợp vào chỗ chấm: 1 km² = ... ha", "100 ha"),
            ("Điền số thích hợp vào chỗ chấm: 1 ha = ... m²", "10 000 m²"),
            ("Điền số thích hợp vào chỗ chấm: 4 km² 5 ha = ... ha", "405 ha (4 × 100 + 5 = 405)"),
            ("Viết số đo 25 ha dưới dạng số thập phân với đơn vị ki-lô-mét vuông:", "0,25 km² (25 : 100 = 0,25)"),
            ("Điền số thích hợp vào chỗ chấm: 35 000 m² = ... ha", "3,5 ha (35 000 : 10 000 = 3,5)"),
            ("Viết số đo 5 m² 8 dm² dưới dạng số thập phân với đơn vị mét vuông:", "5,08 m²"),
            ("Viết số đo 12 ha 400 m² dưới dạng số thập phân với đơn vị héc-ta:", "12,04 ha (400/10000 = 0,04)"),
            ("Điền dấu thích hợp vào chỗ chấm: 4 ha 50 m² ... 4,05 ha", "< (vì 4 ha 50 m² = 4,005 ha < 4,05 ha)"),
            ("Một khu đô thị mới ở Hà Nội có diện tích 15 ha. Diện tích khu đô thị đó bằng bao nhiêu mét vuông?", "150 000 m² (15 × 10 000 = 150 000)"),
            ("Diện tích một trường tiểu học ở Hà Nội là 1,2 ha. Diện tích đó bằng bao nhiêu mét vuông?", "12 000 m² (1,2 × 10 000 = 12 000)"),
            ("(Toán thực tế địa danh) Quần thể di tích Văn Miếu - Quốc Tử Giám (Hà Nội) có diện tích khuôn viên là 54 331 m². Hãy viết số đo diện tích này dưới dạng số thập phân có đơn vị là héc-ta và làm tròn đến hàng phần mười.", "5,4331 ha; Làm tròn đến hàng phần mười được 5,4 ha"),
            ("(Toán thực tế địa danh) Hồ Hoàn Kiếm (Hồ Gươm) ở trung tâm Thủ đô Hà Nội có diện tích mặt nước khoảng 12 ha. Tính diện tích mặt nước Hồ Gươm theo đơn vị mét vuông.", "120 000 m² (12 × 10 000 = 120 000 m²)"),
            ("(Toán thực tế địa danh) Thành phố Hà Nội có diện tích tự nhiên khoảng 3 359 km². Trong đó, một huyện ngoại thành có diện tích là 280 km². Hỏi diện tích của huyện đó bằng bao nhiêu héc-ta?", "28 000 ha (280 × 100 = 28 000 ha)"),
            ("(Tư duy nâng cao) Một khu đất hình chữ nhật có chu vi 1,2 km, chiều rộng bằng 2/3 chiều dài. Tính diện tích khu đất đó theo đơn vị héc-ta.", "8,64 ha\n- Nửa chu vi: 1,2 km = 600 m\n- Chiều dài: 600 : (2 + 3) × 3 = 360 m\n- Chiều rộng: 240 m\n- Diện tích: 360 × 240 = 86 400 m² = 8,64 ha"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n3,45 ha + 2,78 ha + 6,55 ha + 1,22 ha", "14 ha\n= (3,45 + 6,55) + (2,78 + 1,22) = 10 + 4 = 14 ha")
        ]
    },
    {
        "tuan": 8,
        "tram_so": 8,
        "ten_tram": "Vịnh Hạ Long & Yên Tử (Quảng Ninh)",
        "chu_de": "Phép cộng số thập phân, tính chất phép cộng, tính nhanh",
        "questions": [
            ("Đặt tính rồi tính: 35,6 + 28,75 =", "64,35"),
            ("Đặt tính rồi tính: 142,8 + 59,46 =", "202,26"),
            ("Tính nhẩm: 0,75 + 0,25 + 3,8 =", "4,8 (1 + 3,8 = 4,8)"),
            ("Tính nhẩm: 18,5 + 9,9 =", "28,4 (18,5 + 10 - 0,1 = 28,4)"),
            ("Tính bằng cách thuận tiện: 12,7 + 5,89 + 7,3 =", "25,89\n((12,7 + 7,3) + 5,89 = 20 + 5,89 = 25,89)"),
            ("Tìm x, biết: x - 14,5 = 26,75", "x = 41,25 (26,75 + 14,5 = 41,25)"),
            ("Một hình tam giác có độ dài 3 cạnh lần lượt là 4,5 cm; 5,8 cm và 6,7 cm. Chu vi của hình tam giác đó là:", "17 cm (4,5 + 5,8 + 6,7 = 17 cm)"),
            ("Một thùng có 15,5 kg sơn, người ta đổ thêm vào thùng 8,75 kg sơn nữa. Hỏi trong thùng có tất cả bao nhiêu ki-lô-gam sơn?", "24,25 kg (15,5 + 8,75 = 24,25 kg)"),
            ("Tính giá trị biểu thức: A = 4,68 + 6,03 + 3,97 =", "14,68 (4,68 + 10 = 14,68)"),
            ("Điền số thập phân thích hợp vào chỗ chấm: 3,4 + ... = 10", "6,6 (10 - 3,4 = 6,6)"),
            ("(Toán thực tế địa danh) Tàu du lịch tham quan Vịnh Hạ Long (Quảng Ninh) đi qua 3 chặng: chặng 1 dài 12,5 km; chặng 2 dài 4,75 km; chặng 3 dài 13,25 km. Hỏi cả chuyến hải trình tàu đã đi được quãng đường dài bao nhiêu ki-lô-mét?", "30,5 km\n(12,5 + 4,75 + 13,25 = 12,5 + 18 = 30,5 km)"),
            ("(Toán thực tế địa danh) Người hành hương leo bộ lên Chùa Đồng (đỉnh Yên Tử, Quảng Ninh) ở độ cao 1 068 m: buổi sáng đi được 2,45 km đường núi, buổi chiều đi tiếp được 1,8 km nữa thì tới Chùa Đồng. Hỏi người đó đã leo được bao nhiêu ki-lô-mét đường núi?", "4,25 km\n(2,45 + 1,8 = 4,25 km)"),
            ("(Toán thực tế địa danh) Ban quản lý Vịnh Hạ Long thống kê lượng khách quốc tế trong 3 ngày cuối tuần: ngày thứ sáu có 4,2 nghìn lượt; ngày thứ bảy có 6,85 nghìn lượt; ngày chủ nhật có 7,15 nghìn lượt. Hỏi cả ba ngày có bao nhiêu nghìn lượt khách quốc tế tham quan vịnh?", "18,2 nghìn lượt khách (18 200 lượt)\n(4,2 + 6,85 + 7,15 = 4,2 + 14 = 18,2)"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n1,2 + 2,3 + 3,4 + 4,5 + 5,5 + 6,6 + 7,7 + 8,8", "40\n= (1,2+8,8) + (2,3+7,7) + (3,4+6,6) + (4,5+5,5)\n= 10 + 10 + 10 + 10 = 40"),
            ("(Tư duy nâng cao) Cho tổng: S = 0,1 + 0,2 + 0,3 + ... + 0,9. Tìm S.", "4,5\n(Số số hạng: 9. S = (0,1 + 0,9) × 9 : 2 = 4,5)")
        ]
    },
    {
        "tuan": 9,
        "tram_so": 9,
        "ten_tram": "Tràng An & Cố đô Hoa Lư (Ninh Bình) 🌟 GK1",
        "chu_de": "Phép trừ số thập phân, phép nhân số thập phân, ôn tập Giữa học kỳ 1 (GK1)",
        "questions": [
            ("Đặt tính rồi tính: 75,4 - 38,26 =", "37,14"),
            ("Đặt tính rồi tính: 100 - 45,85 =", "54,15"),
            ("Tính: 4,25 × 6 =", "25,5"),
            ("Tính: 3,4 × 2,5 =", "8,5"),
            ("Tính nhẩm: 4,78 × 100 =", "478"),
            ("Tìm x, biết: x + 15,8 = 42,35", "x = 26,55 (42,35 - 15,8 = 26,55)"),
            ("Tìm y, biết: 80 - y = 34,6", "y = 45,4 (80 - 34,6 = 45,4)"),
            ("Một hình chữ nhật có chiều dài 8,5 m và chiều rộng 4,2 m. Chu vi hình chữ nhật đó là:", "25,4 m\n((8,5 + 4,2) × 2 = 25,4 m)"),
            ("Một hình vuông có cạnh dài 5,5 dm. Diện tích hình vuông đó là:", "30,25 dm²\n(5,5 × 5,5 = 30,25 dm²)"),
            ("Tính giá trị biểu thức: 50,4 - 3,2 × 5 =", "34,4\n(50,4 - 16 = 34,4)"),
            ("(Toán thực tế địa danh) Tuyến thuyền tham quan Quần thể danh thắng Tràng An (Ninh Bình) dài 15 km qua nhiều hang động. Chiếc thuyền chở khách đã đi được 9,65 km. Hỏi thuyền còn phải đi thêm bao nhiêu ki-lô-mét nữa để hoàn thành hành trình?", "5,35 km\n(15 - 9,65 = 5,35 km)"),
            ("(Toán thực tế địa danh) Vườn trồng na dai đặc sản gần Cố đô Hoa Lư (Ninh Bình) hình chữ nhật có chiều dài 45,5 m và chiều rộng 28 m. Người ta dùng 0,6 diện tích vườn để trồng na giống mới. Tính diện tích phần đất trồng na giống mới.", "764,4 m²\n- Diện tích vườn: 45,5 × 28 = 1 274 m²\n- Diện tích trồng na: 1 274 × 0,6 = 764,4 m²"),
            ("(Toán thực tế địa danh) Đoàn học sinh gồm 45 bạn đi trải nghiệm thực tế tại Tràng An và Cố đô Hoa Lư. Giá vé trọn gói cho mỗi bạn là 120,5 nghìn đồng. Hỏi đoàn phải trả tất cả bao nhiêu tiền vé?", "5 422,5 nghìn đồng (hay 5 422 500 đồng)\n(45 × 120,5 = 5 422,5)"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n8,4 × 3,7 + 8,4 × 6,3", "84\n= 8,4 × (3,7 + 6,3) = 8,4 × 10 = 84"),
            ("(Tư duy nâng cao) Tìm hai số thập phân có tổng bằng 15,6 và hiệu bằng 4,2.", "Số lớn: 9,9; Số bé: 5,7\n- Số lớn: (15,6 + 4,2) : 2 = 9,9\n- Số bé: 9,9 - 4,2 = 5,7")
        ]
    },
    {
        "tuan": 10,
        "tram_so": 10,
        "ten_tram": "Thành Nhà Hồ (Thanh Hóa)",
        "chu_de": "Phép nhân số thập phân (tiếp), phép chia số thập phân cho số tự nhiên",
        "questions": [
            ("Đặt tính rồi tính: 24,8 : 4 =", "6,2"),
            ("Đặt tính rồi tính: 91,5 : 5 =", "18,3"),
            ("Đặt tính rồi tính: 75 : 4 =", "18,75"),
            ("Đặt tính rồi tính: 3 : 8 =", "0,375"),
            ("Đặt tính rồi tính: 48,6 : 12 =", "4,05"),
            ("Tính nhẩm: 35,4 : 10 =", "3,54"),
            ("Tìm x, biết: x × 6 = 43,2", "x = 7,2 (43,2 : 6 = 7,2)"),
            ("May 5 bộ quần áo hết 14 m vải. Hỏi may mỗi bộ quần áo như thế hết bao nhiêu mét vải?", "2,8 m (14 : 5 = 2,8 m)"),
            ("Một thửa ruộng thu hoạch được 1,8 tấn thóc, chia đều vào 36 bao. Hỏi mỗi bao chứa bao nhiêu ki-lô-gam thóc?", "50 kg\n(1,8 tấn = 1 800 kg; 1 800 : 36 = 50 kg)"),
            ("Tính giá trị biểu thức: 15,6 + 28,4 : 4 =", "22,7\n(15,6 + 7,1 = 22,7)"),
            ("(Toán thực tế địa danh) Thành Nhà Hồ (Thanh Hóa) là di sản thế giới độc đáo ghép bằng những khối đá xanh khổng lồ. Một đoạn tường thành dài 52,8 m gồm 24 khối đá ghép khít nhau. Hỏi trung bình mỗi khối đá có chiều dài bao nhiêu mét?", "2,2 m\n(52,8 : 24 = 2,2 m)"),
            ("(Toán thực tế địa danh) Đội tu bổ di tích Thành Nhà Hồ cần chuyển 48,6 tấn đá xanh cổ về khu bảo tồn trong 9 chuyến xe tải có tải trọng như nhau. Hỏi mỗi chuyến xe chở bao nhiêu tấn đá?", "5,4 tấn\n(48,6 : 9 = 5,4 tấn)"),
            ("(Toán thực tế địa danh) Mảnh đất hình chữ nhật gần di sản Thành Nhà Hồ có diện tích 375 m², chiều dài là 25 m. Người ta chôn cọc rào xung quanh mảnh đất, cứ cách 2 m chôn một cọc (4 góc đều có cọc). Tính số cọc rào cần dùng.", "40 cọc rào\n- Chiều rộng: 375 : 25 = 15 m\n- Chu vi: (25 + 15) × 2 = 80 m\n- Số cọc: 80 : 2 = 40 cọc"),
            ("(Tư duy nâng cao) Một người đi bộ từ bến xe vào tham quan Thành Nhà Hồ: 3 giờ đầu đi được 12,6 km, 2 giờ sau đi được 7,9 km. Hỏi trung bình mỗi giờ người đó đi được bao nhiêu ki-lô-mét?", "4,1 km/h\n- Tổng quãng đường: 12,6 + 7,9 = 20,5 km\n- Tổng thời gian: 3 + 2 = 5 giờ\n- Vận tốc TB: 20,5 : 5 = 4,1 km/h"),
            ("(Tư duy nâng cao) Tìm x, biết: x × 4 + x × 6 = 45,5", "x = 4,55\n(x × (4 + 6) = 45,5 => x × 10 = 45,5 => x = 4,55)")
        ]
    },
    {
        "tuan": 11,
        "tram_so": 11,
        "ten_tram": "Làng Sen Quê Bác (Nghệ An)",
        "chu_de": "Chia một số tự nhiên cho số thập phân; nhân, chia nhẩm với 10, 100, 1000... và 0,1; 0,01...",
        "questions": [
            ("Đặt tính rồi tính: 15 : 2,5 =", "6"),
            ("Đặt tính rồi tính: 26 : 0,65 =", "40"),
            ("Tính nhẩm: 4,56 × 0,1 =", "0,456"),
            ("Tính nhẩm: 18,2 : 0,1 =", "182"),
            ("Tính nhẩm: 2,75 × 100 =", "275"),
            ("Điền số thích hợp vào chỗ chấm: 3,45 × ... = 345", "100"),
            ("Điền số thích hợp vào chỗ chấm: 89,2 × ... = 0,892", "0,01"),
            ("Tìm x, biết: x × 1,5 = 45", "x = 30 (45 : 1,5 = 30)"),
            ("Một sợi dây dài 18 m được cắt thành các đoạn ngắn dài 1,2 m. Hỏi cắt được bao nhiêu đoạn dây như thế?", "15 đoạn (18 : 1,2 = 15)"),
            ("Có 45 lít dầu chia đều vào các chai, mỗi chai chứa 0,75 lít. Hỏi rót được tất cả bao nhiêu chai dầu?", "60 chai (45 : 0,75 = 60)"),
            ("(Toán thực tế địa danh) Đầm sen cạnh ngôi nhà tranh Quê Bác ở Làng Sen (Kim Liên, Nghệ An) có diện tích 750 m². Người ta ước tính cứ mỗi 2,5 m² mặt nước có trung bình 6 bông sen đang nở rộ. Hỏi cả đầm sen có khoảng bao nhiêu bông sen nở?", "1 800 bông sen\n- Số phần diện tích: 750 : 2,5 = 300\n- Số bông sen: 300 × 6 = 1 800 bông"),
            ("(Toán thực tế địa danh) Đoàn du khách về nguồn thăm Làng Sen Quê Bác đi ô tô từ thành phố Vinh quãng đường dài 14 km với vận tốc 35 km/h. Hỏi ô tô đi hết bao nhiêu thời gian (tính theo giờ và phút)?", "0,4 giờ = 24 phút\n(14 : 35 = 0,4 giờ = 24 phút)"),
            ("(Toán thực tế địa danh) Vườn chè xanh ở quê ngoại Bác Hồ (Làng Hoàng Trù) thu hoạch được 150 kg lá chè tươi. Người ta đóng gói vào các túi nhỏ mỗi túi 0,5 kg chè. Hỏi đóng được bao nhiêu túi chè?", "300 túi chè\n(150 : 0,5 = 300 túi)"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n45,8 × 0,25 × 4", "45,8\n= 45,8 × (0,25 × 4) = 45,8 × 1 = 45,8"),
            ("(Tư duy nâng cao) Khi nhân một số với 0,5; bạn An đã viết nhầm thành chia số đó cho 0,5 nên được kết quả là 84. Hỏi kết quả đúng của phép nhân là bao nhiêu?", "21\n- Số ban đầu: 84 × 0,5 = 42\n- Kết quả đúng: 42 × 0,5 = 21")
        ]
    },
    {
        "tuan": 12,
        "tram_so": 12,
        "ten_tram": "Ngã ba Đồng Lộc (Hà Tĩnh)",
        "chu_de": "Phép chia một số thập phân cho số thập phân, tính giá trị biểu thức, tính thuận tiện",
        "questions": [
            ("Đặt tính rồi tính: 17,55 : 3,9 =", "4,5"),
            ("Đặt tính rồi tính: 46,8 : 1,5 =", "31,2"),
            ("Đặt tính rồi tính: 0,72 : 0,45 =", "1,6"),
            ("Đặt tính rồi tính: 19,72 : 5,8 =", "3,4"),
            ("Tính giá trị biểu thức: (15,8 + 4,2) : 2,5 =", "8\n(20 : 2,5 = 8)"),
            ("Tính giá trị biểu thức: 45,6 : 1,2 - 18,5 =", "19,5\n(38 - 18,5 = 19,5)"),
            ("Tìm y, biết: y × 2,4 = 18,72", "y = 7,8 (18,72 : 2,4 = 7,8)"),
            ("Tìm x, biết: x : 1,6 = 3,25", "x = 5,2 (3,25 × 1,6 = 5,2)"),
            ("Biết 4,5 lít dầu cân nặng 3,6 kg. Hỏi 7,2 lít dầu cùng loại cân nặng bao nhiêu ki-lô-gam?", "5,76 kg\n- 1 lít nặng: 3,6 : 4,5 = 0,8 kg\n- 7,2 lít nặng: 7,2 × 0,8 = 5,76 kg"),
            ("Một hình chữ nhật có diện tích 28,8 m², chiều dài là 6,4 m. Chiều rộng hình chữ nhật đó là:", "4,5 m (28,8 : 6,4 = 4,5 m)"),
            ("(Toán thực tế địa danh) Khuôn viên Tượng đài Chiến thắng tại Ngã ba Đồng Lộc (Hà Tĩnh) có một thảm cỏ hình chữ nhật diện tích 345,6 m², chiều rộng là 14,4 m. Tính chiều dài của thảm cỏ đó.", "24 m\n(345,6 : 14,4 = 24 m)"),
            ("(Toán thực tế địa danh) Đoàn xe chở đá dăm tu sửa tuyến đường qua Ngã ba Đồng Lộc: xe thứ nhất chở 4,8 tấn, xe thứ hai chở gấp 1,25 lần xe thứ nhất. Hỏi cả hai xe chở được bao nhiêu tấn đá dăm?", "10,8 tấn\n- Xe thứ hai: 4,8 × 1,25 = 6 tấn\n- Cả hai xe: 4,8 + 6 = 10,8 tấn"),
            ("(Toán thực tế địa danh) Ban quản lý khu di tích Ngã ba Đồng Lộc mua 10 chậu hoa cúc vạn thọ trồng quanh đài tưởng niệm 10 cô gái thanh niên xung phong hết tổng cộng 475,5 nghìn đồng. Hỏi mỗi chậu hoa có giá trung bình bao nhiêu nghìn đồng?", "47,55 nghìn đồng (47 550 đồng)\n(475,5 : 10 = 47,55)"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n2,4 × 4,8 + 2,4 × 6,2 - 2,4", "24\n= 2,4 × (4,8 + 6,2 - 1) = 2,4 × 10 = 24"),
            ("(Tư duy nâng cao) Một phép chia hai số thập phân có số chia là 2,5. Bạn Bình viết nhầm dấu phẩy của số bị chia sang bên phải một chữ số nên được thương là 18,4. Tìm thương đúng của phép chia đó.", "1,84\n(Dấu phẩy sang phải 1 chữ số làm số bị chia tăng 10 lần => Thương đúng: 18,4 : 10 = 1,84)")
        ]
    },
    {
        "tuan": 13,
        "tram_so": 13,
        "ten_tram": "Vườn quốc gia Phong Nha - Kẻ Bàng (Quảng Bình)",
        "chu_de": "Hình tam giác, các yếu tố đáy và đường cao, diện tích hình tam giác",
        "questions": [
            ("Công thức tính diện tích hình tam giác có độ dài đáy a và chiều cao h (cùng đơn vị đo) là:", "S = a × h : 2"),
            ("Một hình tam giác có độ dài đáy 12 cm và chiều cao 8 cm. Diện tích của hình tam giác đó là:", "48 cm² (12 × 8 : 2 = 48 cm²)"),
            ("Một hình tam giác có đáy 3,5 m và chiều cao 2,4 m. Diện tích tam giác đó là:", "4,2 m² (3,5 × 2,4 : 2 = 4,2 m²)"),
            ("Một hình tam giác vuông có hai cạnh góc vuông lần lượt là 6 cm và 8 cm. Diện tích tam giác vuông đó là:", "24 cm² (6 × 8 : 2 = 24 cm²)"),
            ("Một hình tam giác có diện tích 30 cm², chiều cao là 6 cm. Độ dài đáy của tam giác đó là:", "10 cm (30 × 2 : 6 = 10 cm)"),
            ("Một hình tam giác có diện tích 45 m², độ dài đáy là 15 m. Chiều cao của tam giác đó là:", "6 m (45 × 2 : 15 = 6 m)"),
            ("Một hình tam giác có đáy 2,5 dm và chiều cao 16 cm. Diện tích tam giác bằng bao nhiêu xăng-ti-mét vuông?", "200 cm²\n(2,5 dm = 25 cm; S = 25 × 16 : 2 = 200 cm²)"),
            ("Nếu tăng độ dài đáy của một hình tam giác lên gấp đôi và giữ nguyên chiều cao thì diện tích của nó thay đổi thế nào?", "Diện tích tăng lên gấp đôi"),
            ("Một hình tam giác đều có ba cạnh bằng nhau, mỗi cạnh dài 15 cm. Chu vi của hình tam giác đó là:", "45 cm (15 × 3 = 45 cm)"),
            ("Diện tích hình tam giác vuông có hai cạnh góc vuông là 4,5 dm và 3,2 dm là:", "7,2 dm² (4,5 × 3,2 : 2 = 7,2 dm²)"),
            ("(Toán thực tế địa danh) Cửa Động Phong Nha (Quảng Bình) nhìn từ xa có hình dạng một tam giác khổng lồ với đáy rộng khoảng 25 m và chiều cao khoảng 10 m. Tính diện tích mặt cắt hình tam giác của cửa động đó.", "125 m²\n(25 × 10 : 2 = 125 m²)"),
            ("(Toán thực tế địa danh) Tấm biển chỉ dẫn vào hang Sơn Đoòng trong Vườn quốc gia Phong Nha - Kẻ Bàng có dạng hình tam giác đều cạnh 60 cm, chiều cao tương ứng là 52 cm. Tính diện tích tấm biển báo hình tam giác đó.", "1 560 cm²\n(60 × 52 : 2 = 1 560 cm²)"),
            ("(Toán thực tế địa danh) Bãi cỏ hình tam giác bên bờ sông Son đón khách tham quan Động Phong Nha có đáy dài 48 m. Người ta mở rộng đáy thêm 12 m thì diện tích tăng thêm 150 m². Tính diện tích mảnh đất tam giác ban đầu.", "600 m²\n- Chiều cao tam giác: 150 × 2 : 12 = 25 m\n- Diện tích ban đầu: 48 × 25 : 2 = 600 m²"),
            ("(Tư duy nâng cao) Một hình tam giác có chiều cao bằng 3/4 độ dài đáy và tổng độ dài đáy và chiều cao là 28 cm. Tính diện tích hình tam giác đó.", "96 cm²\n- Chiều cao: 28 : (3 + 4) × 3 = 12 cm\n- Độ dài đáy: 28 - 12 = 16 cm\n- Diện tích: 16 × 12 : 2 = 96 cm²"),
            ("(Tư duy nâng cao) Cho hình tam giác ABC có diện tích là 120 cm². Trên cạnh BC lấy điểm M sao cho BM = 1/3 BC. Tính diện tích hình tam giác ABM.", "40 cm²\n(Chung chiều cao hạ từ đỉnh A xuống đáy BC, đáy BM = 1/3 BC nên S_ABM = 120 : 3 = 40 cm²)")
        ]
    },
    {
        "tuan": 14,
        "tram_so": 14,
        "ten_tram": "Thành cổ Quảng Trị, Cầu Hiền Lương & Sông Bến Hải",
        "chu_de": "Hình thang, đáy lớn, đáy bé, chiều cao, diện tích hình thang",
        "questions": [
            ("Công thức tính diện tích hình thang có hai đáy a, b và chiều cao h (cùng đơn vị đo) là:", "S = (a + b) × h : 2"),
            ("Một hình thang có đáy lớn 15 cm, đáy bé 9 cm và chiều cao 6 cm. Diện tích hình thang là:", "72 cm² ((15 + 9) × 6 : 2 = 72 cm²)"),
            ("Một hình thang có đáy lớn 4,5 m; đáy bé 2,5 m và chiều cao 3 m. Diện tích hình thang là:", "10,5 m² ((4,5 + 2,5) × 3 : 2 = 10,5 m²)"),
            ("Một hình thang có diện tích 60 m², chiều cao 5 m. Tổng độ dài hai đáy của hình thang đó là:", "24 m (60 × 2 : 5 = 24 m)"),
            ("Một hình thang có diện tích 90 cm², tổng độ dài hai đáy là 18 cm. Chiều cao của hình thang đó là:", "10 cm (90 × 2 : 18 = 10 cm)"),
            ("Hình thang vuông có một cạnh bên vuông góc với hai đáy. Cạnh bên vuông góc đó chính là yếu tố nào của hình thang?", "Chiều cao của hình thang"),
            ("Một hình thang có đáy bé 8 dm, đáy lớn gấp đôi đáy bé, chiều cao 5 dm. Diện tích hình thang đó là:", "60 dm²\n- Đáy lớn: 8 × 2 = 16 dm\n- Diện tích: (16 + 8) × 5 : 2 = 60 dm²"),
            ("Trung bình cộng hai đáy của một hình thang là 14 cm, chiều cao là 7 cm. Diện tích hình thang đó là:", "98 cm² (14 × 7 = 98 cm²)"),
            ("Một hình thang có đáy lớn 2,4 m; đáy bé 1,6 m; chiều cao 1,5 m. Diện tích hình thang đó là:", "3 m² ((2,4 + 1,6) × 1,5 : 2 = 3 m²)"),
            ("Diện tích hình thang sẽ thay đổi thế nào nếu chiều cao tăng gấp 3 lần và giữ nguyên độ dài hai đáy?", "Diện tích tăng lên gấp 3 lần"),
            ("(Toán thực tế địa danh) Đê bao sông Bến Hải (gần Cầu Hiền Lương lịch sử) có mặt cắt ngang là một hình thang với đáy lớn 6,5 m; đáy bé 3,5 m và chiều cao 2,4 m. Tính diện tích mặt cắt ngang của thân đê đó.", "12 m²\n((6,5 + 3,5) × 2,4 : 2 = 10 × 2,4 : 2 = 12 m²)"),
            ("(Toán thực tế địa danh) Vườn hoa hình thang trong khuôn viên Di tích Thành cổ Quảng Trị có đáy lớn 32 m, đáy bé 24 m và chiều cao 18 m. Người ta dùng 1/4 diện tích vườn để trồng hoa cúc trắng tưởng niệm. Tính diện tích đất trồng hoa cúc trắng.", "126 m²\n- Diện tích vườn: (32 + 24) × 18 : 2 = 504 m²\n- Diện tích trồng hoa: 504 : 4 = 126 m²"),
            ("(Toán thực tế địa danh) Cột cờ Hiền Lương lịch sử bên bờ sông Bến Hải có một khoảng sân hình thang với đáy bé 12 m, đáy lớn bằng 3/2 đáy bé và chiều cao 10 m. Tính diện tích khoảng sân hình thang đó.", "150 m²\n- Đáy lớn: 12 × 3/2 = 18 m\n- Diện tích: (18 + 12) × 10 : 2 = 150 m²"),
            ("(Tư duy nâng cao) Một thửa ruộng hình thang có diện tích 420 m², chiều cao 14 m. Tính độ dài mỗi đáy, biết đáy lớn hơn đáy bé 10 m.", "Đáy lớn: 35 m; Đáy bé: 25 m\n- Tổng hai đáy: 420 × 2 : 14 = 60 m\n- Đáy lớn: (60 + 10) : 2 = 35 m\n- Đáy bé: 35 - 10 = 25 m"),
            ("(Tư duy nâng cao) Một mảnh đất hình thang có đáy bé 20 m, đáy lớn 30 m. Nếu tăng đáy lớn thêm 5 m thì diện tích tăng thêm 45 m². Tính diện tích mảnh đất hình thang ban đầu.", "450 m²\n- Chiều cao: 45 × 2 : 5 = 18 m\n- Diện tích ban đầu: (30 + 20) × 18 : 2 = 450 m²")
        ]
    },
    {
        "tuan": 15,
        "tram_so": 15,
        "ten_tram": "Quần thể Di tích Cố đô Huế (Thừa Thiên Huế)",
        "chu_de": "Đường tròn, hình tròn, chu vi và diện tích hình tròn",
        "questions": [
            ("Trong một hình tròn, đường kính d gấp mấy lần bán kính r?", "2 lần (d = 2 × r)"),
            ("Công thức tính chu vi hình tròn có đường kính d là:", "C = d × 3,14 (hoặc C = r × 2 × 3,14)"),
            ("Công thức tính diện tích hình tròn có bán kính r là:", "S = r × r × 3,14"),
            ("Một hình tròn có bán kính 5 cm. Chu vi của hình tròn đó là:", "31,4 cm (5 × 2 × 3,14 = 31,4 cm)"),
            ("Một hình tròn có đường kính 8 dm. Chu vi của hình tròn đó là:", "25,12 dm (8 × 3,14 = 25,12 dm)"),
            ("Một hình tròn có bán kính 4 cm. Diện tích của hình tròn đó là:", "50,24 cm² (4 × 4 × 3,14 = 50,24 cm²)"),
            ("Một hình tròn có đường kính 10 m. Diện tích của hình tròn đó là:", "78,5 m² (r = 5 m; S = 5 × 5 × 3,14 = 78,5 m²)"),
            ("Một hình tròn có chu vi 18,84 cm. Đường kính của hình tròn đó là:", "6 cm (18,84 : 3,14 = 6 cm)"),
            ("Một hình tròn có diện tích 28,26 dm². Bán kính của hình tròn đó là:", "3 dm (r × r = 28,26 : 3,14 = 9 => r = 3 dm)"),
            ("Một bánh xe đạp có đường kính 0,65 m. Khi bánh xe lăn được 1 vòng trên mặt đất thì xe đi được quãng đường dài bao nhiêu mét?", "2,041 m (0,65 × 3,14 = 2,041 m)"),
            ("(Toán thực tế địa danh) Chiếc nón bài thơ xứ Huế truyền thống có đường kính vành nón dưới cùng là 40 cm. Tính chu vi của vành nón tròn đó.", "125,6 cm\n(40 × 3,14 = 125,6 cm)"),
            ("(Toán thực tế địa danh) Trong khuôn viên Đại Nội Cố đô Huế có một hồ hoa sen hình tròn với bán kính 6 m. Tính diện tích mặt hồ hoa sen hình tròn đó.", "113,04 m²\n(6 × 6 × 3,14 = 113,04 m²)"),
            ("(Toán thực tế địa danh) Một chiếc xe xích lô du lịch chở khách ngắm dòng sông Hương và Cầu Tràng Tiền (Huế) có bánh xe đường kính 0,8 m. Khi xe lăn bánh được 100 vòng thì đã đi được quãng đường bao nhiêu mét?", "251,2 m\n- Chu vi bánh xe: 0,8 × 3,14 = 2,512 m\n- Quãng đường: 2,512 × 100 = 251,2 m"),
            ("(Tư duy nâng cao) Một bồn hoa hình tròn có bán kính 3 m. Người ta làm một lối đi dạo bao quanh bồn hoa rộng 1 m. Tính diện tích của lối đi dạo đó.", "21,98 m²\n- Bán kính hình tròn lớn: 3 + 1 = 4 m\n- S hình tròn lớn: 4 × 4 × 3,14 = 50,24 m²\n- S bồn hoa: 3 × 3 × 3,14 = 28,26 m²\n- S lối đi: 50,24 - 28,26 = 21,98 m²"),
            ("(Tư duy nâng cao) Nếu bán kính của một hình tròn tăng lên gấp 2 lần thì diện tích của hình tròn đó tăng lên gấp mấy lần?", "Tăng lên 4 lần\n(Vì S = (2r) × (2r) × 3,14 = 4 × (r × r × 3,14))")
        ]
    },
    {
        "tuan": 16,
        "tram_so": 16,
        "ten_tram": "Cầu Rồng & Ngũ Hành Sơn (Đà Nẵng)",
        "chu_de": "Diện tích các hình phẳng phức hợp, ôn tập các phép tính với số thập phân",
        "questions": [
            ("Tính diện tích hình gồm một hình chữ nhật kích thước 8 m × 5 m và một hình tam giác có đáy 8 m, chiều cao 3 m ghép liền:", "52 m²\n- S chữ nhật: 8 × 5 = 40 m²\n- S tam giác: 8 × 3 : 2 = 12 m²\n- Tổng diện tích: 40 + 12 = 52 m²"),
            ("Một tấm bìa hình vuông cạnh 10 cm, người ta khoét một hình tròn bán kính 3 cm ở chính giữa. Diện tích phần bìa còn lại là:", "71,74 cm²\n- S hình vuông: 10 × 10 = 100 cm²\n- S hình tròn: 3 × 3 × 3,14 = 28,26 cm²\n- Còn lại: 100 - 28,26 = 71,74 cm²"),
            ("Tính bằng cách thuận tiện: 45,8 × 2,5 + 54,2 × 2,5 =", "250\n= (45,8 + 54,2) × 2,5 = 100 × 2,5 = 250"),
            ("Tính bằng cách thuận tiện: 125,5 : 5 + 74,5 : 5 =", "40\n= (125,5 + 74,5) : 5 = 200 : 5 = 40"),
            ("Một bồn hoa hình bán nguyệt (nửa hình tròn) có đường kính 4 m. Diện tích bồn hoa đó là:", "6,28 m²\n(r = 2 m; S = (2 × 2 × 3,14) : 2 = 6,28 m²)"),
            ("Tìm x, biết: x : 0,25 + x × 6 = 150", "x = 15\n(x × 4 + x × 6 = 150 => x × 10 = 150 => x = 15)"),
            ("Một sân chơi hình chữ nhật có chu vi 72 m, chiều rộng bằng 4/5 chiều dài. Diện tích sân chơi đó là:", "320 m²\n- Nửa chu vi: 36 m\n- Chiều dài: 36 : (4+5) × 5 = 20 m; Rộng: 16 m\n- S = 20 × 16 = 320 m²"),
            ("Tính chu vi nửa hình tròn có đường kính 10 cm (gồm cung tròn và đường kính):", "25,7 cm\n((10 × 3,14 : 2) + 10 = 15,7 + 10 = 25,7 cm)"),
            ("Tính giá trị biểu thức: (3,6 × 1,5) + (4,8 : 1,2) =", "9,4\n(5,4 + 4 = 9,4)"),
            ("Tìm số trung bình cộng của bốn số thập phân: 4,2 ; 5,8 ; 6,5 và 7,5", "6\n((4,2 + 5,8 + 6,5 + 7,5) : 4 = 24 : 4 = 6)"),
            ("(Toán thực tế địa danh) Cầu Rồng (Đà Nẵng) bắc qua sông Hàn có tổng chiều dài 666 m. Chiều dài phần thân rồng uốn lượn bằng thép chiếm khoảng 0,85 tổng chiều dài cầu. Tính chiều dài phần thân rồng uốn lượn (làm tròn đến hàng phần mười).", "566,1 m\n(666 × 0,85 = 566,1 m)"),
            ("(Toán thực tế địa danh) Làng nghề đá mỹ nghệ dưới chân danh thắng Ngũ Hành Sơn (Đà Nẵng) chế tác bức phù điêu hình thang có đáy lớn 3,6 m; đáy bé 2,4 m và chiều cao 1,8 m. Tính diện tích của bức phù điêu bằng đá đó.", "5,4 m²\n((3,6 + 2,4) × 1,8 : 2 = 6 × 1,8 : 2 = 5,4 m²)"),
            ("(Toán thực tế địa danh) Sân khấu ngoài trời bên bờ sông Hàn gần Cầu Rồng có dạng hình chữ nhật dài 24 m, rộng 15 m. Chính giữa sân khấu người ta lát đá hoa cương hình tròn bán kính 4 m. Tính diện tích phần sân khấu còn lại không lát đá hoa cương.", "309,76 m²\n- S sân khấu: 24 × 15 = 360 m²\n- S hình tròn: 4 × 4 × 3,14 = 50,24 m²\n- Phần còn lại: 360 - 50,24 = 309,76 m²"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n(12,5 × 8) × (0,25 × 40) × (0,5 × 20)", "10 000\n= 100 × 10 × 10 = 10 000"),
            ("(Tư duy nâng cao) Một thửa đất hình chữ nhật có chu vi 120 m. Nếu tăng chiều rộng thêm 5 m và giảm chiều dài đi 5 m thì diện tích tăng thêm 25 m². Tính diện tích ban đầu của thửa đất đó.", "875 m²\n- Nửa chu vi: 60 m\n- Hiệu dài và rộng: 10 m\n- Chiều dài: 35 m; Chiều rộng: 25 m\n- Diện tích: 35 × 25 = 875 m²")
        ]
    },
    {
        "tuan": 17,
        "tram_so": 17,
        "ten_tram": "Phố cổ Hội An (Quảng Nam)",
        "chu_de": "Hệ thống hóa chu vi, diện tích các hình phẳng, bài toán chuyển động đều và thực tế",
        "questions": [
            ("Hình thoi có độ dài hai đường chéo là m và n thì diện tích là:", "S = m × n : 2"),
            ("Một hình thoi có độ dài hai đường chéo là 16 cm và 12 cm. Diện tích của hình thoi đó là:", "96 cm² (16 × 12 : 2 = 96 cm²)"),
            ("Một hình bình hành có độ dài đáy 15 cm và chiều cao 8 cm. Diện tích của hình bình hành đó là:", "120 cm² (15 × 8 = 120 cm²)"),
            ("Một hình thang có hai đáy lần lượt là 12 cm và 8 cm, chiều cao 5 cm. Diện tích hình thang đó là:", "50 cm² ((12 + 8) × 5 : 2 = 50 cm²)"),
            ("Một hình tròn có chu vi 31,4 dm. Diện tích của hình tròn đó là:", "78,5 dm²\n(r = 31,4 : 3,14 : 2 = 5 dm; S = 5 × 5 × 3,14 = 78,5 dm²)"),
            ("Một người đi xe đạp đi quãng đường 36 km hết 2,4 giờ. Vận tốc của người đi xe đạp là:", "15 km/h (36 : 2,4 = 15 km/h)"),
            ("Một cano đi trên sông với vận tốc 24,5 km/h. Trong 2,5 giờ cano đi được quãng đường bao nhiêu ki-lô-mét?", "61,25 km (24,5 × 2,5 = 61,25 km)"),
            ("Tính: 4,8 × 1,25 × 8 =", "48\n= 4,8 × (1,25 × 8) = 4,8 × 10 = 48"),
            ("Một mảnh đất hình chữ nhật có chu vi 84 m, chiều dài gấp 3 lần chiều rộng. Diện tích mảnh đất đó là:", "330,75 m²\n- Nửa chu vi: 42 m\n- Chiều rộng: 42 : 4 = 10,5 m; Dài: 31,5 m\n- Diện tích: 31,5 × 10,5 = 330,75 m²"),
            ("Tính diện tích hình tam giác vuông có hai cạnh góc vuông là 7,5 cm và 4,8 cm:", "18 cm² (7,5 × 4,8 : 2 = 18 cm²)"),
            ("(Toán thực tế địa danh) Nghệ nhân làm đèn lồng truyền thống tại Phố cổ Hội An (Quảng Nam) tạo ra chiếc đèn lồng có mặt bên hình thoi với hai đường chéo dài 25 cm và 18 cm. Tính diện tích mặt giấy dán vừa vặn cho một mặt hình thoi đó.", "225 cm²\n(25 × 18 : 2 = 225 cm²)"),
            ("(Toán thực tế địa danh) Chùa Cầu cổ kính tại Phố cổ Hội An bắc qua một con lạch nhỏ thông ra sông Hoài. Sàn cầu bằng gỗ hình chữ nhật có chiều dài khoảng 18 m và chiều rộng khoảng 3,5 m. Tính diện tích mặt sàn của Chùa Cầu.", "63 m²\n(18 × 3,5 = 63 m²)"),
            ("(Toán thực tế địa danh) Vào đêm rằm phố cổ Hội An, một chiếc thuyền hoa chở du khách thả đèn hoa đăng trôi xuôi dòng sông Hoài với vận tốc 4,5 km/h. Hỏi sau 40 phút chiếc thuyền hoa đi được quãng đường dài bao nhiêu ki-lô-mét?", "3 km\n(40 phút = 2/3 giờ; Quãng đường = 4,5 × 2/3 = 3 km)"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n1,5 × 4,6 + 1,5 × 7,8 - 1,5 × 2,4", "15\n= 1,5 × (4,6 + 7,8 - 2,4) = 1,5 × 10 = 15"),
            ("(Tư duy nâng cao) Một mảnh vườn hình chữ nhật có chiều dài hơn chiều rộng 12 m. Nếu bớt chiều dài 4 m và tăng chiều rộng 4 m thì diện tích tăng thêm 64 m². Tính diện tích ban đầu của mảnh vườn.", "364 m²\n- Dài ban đầu: 26 m; Rộng ban đầu: 14 m\n- Diện tích: 26 × 14 = 364 m²")
        ]
    },
    {
        "tuan": 18,
        "tram_so": 18,
        "ten_tram": "Đảo Lý Sơn (Quảng Ngãi) 🏆 CK1",
        "chu_de": "Ôn tập đo lường, tổng hợp toàn diện kiến thức Học kỳ 1 (Cuối học kỳ 1 - CK1)",
        "questions": [
            ("Viết số đo 4 m 5 cm dưới dạng số thập phân với đơn vị mét là:", "4,05 m"),
            ("Viết số đo 3 tấn 25 kg dưới dạng số thập phân với đơn vị tấn là:", "3,025 tấn"),
            ("Viết số đo 5 ha 60 m² dưới dạng số thập phân với đơn vị héc-ta là:", "5,006 ha"),
            ("Đặt tính rồi tính: 48,25 + 36,9 =", "85,15"),
            ("Đặt tính rồi tính: 120 - 45,78 =", "74,22"),
            ("Đặt tính rồi tính: 34,5 × 4,6 =", "158,7"),
            ("Đặt tính rồi tính: 81,6 : 2,4 =", "34"),
            ("Một hình thang có hai đáy lần lượt là 18 m và 12 m, chiều cao 8 m. Diện tích hình thang đó là:", "120 m² ((18 + 12) × 8 : 2 = 120 m²)"),
            ("Một hình tròn có bán kính 6 dm. Diện tích của hình tròn đó là:", "113,04 dm² (6 × 6 × 3,14 = 113,04 dm²)"),
            ("Điền số thập phân thích hợp vào chỗ chấm: 2 giờ 45 phút = ... giờ", "2,75 giờ (45/60 = 0,75)"),
            ("(Toán thực tế địa danh) Huyện đảo Lý Sơn (Quảng Ngãi) được mệnh danh là \"Vương quốc tỏi\". Một thửa ruộng hình thang trồng tỏi có đáy lớn 28 m, đáy bé 22 m và chiều cao 16 m. Trung bình mỗi mét vuông thu hoạch được 1,5 kg tỏi khô. Hỏi vụ mùa đó thửa ruộng thu hoạch được tất cả bao nhiêu ki-lô-gam tỏi khô?", "600 kg tỏi khô\n- Diện tích ruộng: (28 + 22) × 16 : 2 = 400 m²\n- Sản lượng tỏi: 400 × 1,5 = 600 kg"),
            ("(Toán thực tế địa danh) Tàu cao tốc đưa du khách từ cảng Sa Kỳ (Quảng Ngãi) ra Đảo Lý Sơn vượt quãng đường biển dài 27 km hết 0,75 giờ (45 phút). Tính vận tốc của tàu cao tốc trên biển.", "36 km/h\n(27 : 0,75 = 36 km/h)"),
            ("(Toán thực tế địa danh) Khu vực đài Cột cờ Tổ quốc trên đỉnh Thới Lới (Đảo Lý Sơn) sừng sững khẳng định chủ quyền biển đảo có dạng hình chữ nhật dài 15,5 m và rộng 8,4 m. Người ta dùng gạch chống trượt hình vuông cạnh 40 cm để lát toàn bộ khoảng sân. Hỏi cần bao nhiêu viên gạch (bỏ qua mép vữa)?", "814 viên gạch\n- S sân: 15,5 × 8,4 = 130,2 m² = 1 302 000 cm²\n- S 1 viên gạch: 40 × 40 = 1 600 cm²\n- Số gạch: 1 302 000 : 1 600 ≈ 813,75 => Cần 814 viên"),
            ("(Tư duy nâng cao) Tính bằng cách thuận tiện nhất:\n3,7 × 4,8 + 4,8 × 7,3 - 4,8", "48\n= 4,8 × (3,7 + 7,3 - 1) = 4,8 × 10 = 48"),
            ("(Tư duy nâng cao) Hai thùng dầu chứa tất cả 160 lít dầu. Nếu chuyển 15 lít từ thùng thứ nhất sang thùng thứ hai thì số dầu ở thùng thứ hai gấp 3 lần thùng thứ nhất. Hỏi ban đầu mỗi thùng có bao nhiêu lít dầu?", "Thùng 1: 55 lít; Thùng 2: 105 lít\n- Thùng 1 lúc sau: 160 : (1 + 3) = 40 lít\n- Thùng 2 lúc sau: 120 lít\n- Ban đầu Thùng 1: 40 + 15 = 55 lít\n- Ban đầu Thùng 2: 120 - 15 = 105 lít")
        ]
    }
]

def build_station_table(doc, station):
    """Xây dựng bảng 3 cột: TT, Đề, Đáp án đúng theo đúng yêu cầu người dùng"""
    
    # Tiêu đề trạm
    h_p = doc.add_paragraph()
    h_p.paragraph_format.space_before = Pt(12)
    h_p.paragraph_format.space_after = Pt(4)
    h_p.paragraph_format.keep_with_next = True
    
    r_title = h_p.add_run(f"TRẠM {station['tram_so']} (TUẦN {station['tuan']}): {station['ten_tram'].upper()}")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(13)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(26, 54, 93) # Navy blue

    # Phụ đề chủ đề
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(8)
    sub_p.paragraph_format.keep_with_next = True
    
    r_sub = sub_p.add_run(f"🎯 Trọng tâm kiến thức: {station['chu_de']}")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(74, 85, 104)

    # Bảng 3 cột: TT | Đề | Đáp án đúng
    # Độ rộng trang A4 khả dụng: 21 - 2.5 - 2.0 = 16.5 cm
    col_widths = [Cm(1.2), Cm(11.3), Cm(4.0)]
    
    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Header Row
    hdr_cells = table.rows[0].cells
    hdr_titles = ["TT", "Đề bài", "Đáp án đúng"]
    for idx, name in enumerate(hdr_titles):
        cell = hdr_cells[idx]
        cell.width = col_widths[idx]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(name)
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        
        # Style header background
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(r'<w:shd {} w:fill="1A365D"/>'.format(nsdecls('w')))
        tcPr.append(shd)

    # Question Rows
    for q_idx, (question_text, answer_text) in enumerate(station['questions'], start=1):
        row_cells = table.add_row().cells
        
        # Col 0: TT
        row_cells[0].width = col_widths[0]
        p0 = row_cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.paragraph_format.space_before = Pt(3)
        p0.paragraph_format.space_after = Pt(3)
        r0 = p0.add_run(str(q_idx))
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(10.5)
        r0.font.bold = True

        # Col 1: Đề
        row_cells[1].width = col_widths[1]
        p1 = row_cells[1].paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p1.paragraph_format.space_before = Pt(3)
        p1.paragraph_format.space_after = Pt(3)
        p1.paragraph_format.line_spacing = 1.2
        r1 = p1.add_run(question_text)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10.5)

        # Highlight địa danh / nâng cao
        if "(Toán thực tế địa danh)" in question_text:
            p1.runs[0].text = question_text.replace("(Toán thực tế địa danh) ", "🏛️ ")
            p1.runs[0].font.color.rgb = RGBColor(43, 108, 176)
        elif "(Tư duy nâng cao)" in question_text:
            p1.runs[0].text = question_text.replace("(Tư duy nâng cao) ", "⭐ ")
            p1.runs[0].font.color.rgb = RGBColor(197, 48, 48)

        # Col 2: Đáp án đúng
        row_cells[2].width = col_widths[2]
        p2 = row_cells[2].paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p2.paragraph_format.space_before = Pt(3)
        p2.paragraph_format.space_after = Pt(3)
        p2.paragraph_format.line_spacing = 1.15
        r2 = p2.add_run(answer_text)
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(10)
        r2.font.bold = True
        r2.font.color.rgb = RGBColor(40, 116, 166)

        # Zebra striping for rows
        if q_idx % 2 == 0:
            for cell in row_cells:
                tcPr = cell._tc.get_or_add_tcPr()
                shd = parse_xml(r'<w:shd {} w:fill="F7FAFC"/>'.format(nsdecls('w')))
                tcPr.append(shd)

    # Set thin borders for the table
    for row in table.rows:
        for cell in row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            borders = parse_xml(r'''
                <w:tcBorders {} >
                    <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                    <w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                    <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E0"/>
                </w:tcBorders>
            '''.format(nsdecls('w')))
            tcPr.append(borders)

def setup_document_styles():
    doc = docx.Document()
    
    # Margins: Top 2cm, Bottom 2cm, Left 2.5cm, Right 2cm
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.0)
        
        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("EDUBOT.ID.VN - BỘ ĐỀ TOÁN 5 XUYÊN VIỆT (HỌC KỲ 1: TUẦN 1 - 18)")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(120, 120, 120)

        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun = fp.add_run("Trang ")
        frun.font.name = "Times New Roman"
        frun.font.size = Pt(9)
        frun.font.color.rgb = RGBColor(100, 100, 100)
        
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        fp._p.append(fldSimple)

        frun2 = fp.add_run(" / ")
        frun2.font.name = "Times New Roman"
        frun2.font.size = Pt(9)
        frun2.font.color.rgb = RGBColor(100, 100, 100)

        fldSimple_n = OxmlElement('w:fldSimple')
        fldSimple_n.set(qn('w:instr'), 'NUMPAGES')
        fp._p.append(fldSimple_n)
        
    return doc

def generate_master_document(target_path):
    """Tạo file Word tổng hợp toàn bộ 18 trạm (Tuần 1 - 18)"""
    doc = setup_document_styles()

    # Trang bìa / Tiêu đề mở đầu
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(4)
    run_t = p_title.add_run("BỘ ĐỀ ÔN TẬP TOÁN LỚP 5 - HỌC KỲ 1\nHÀNH TRÌNH THÁM HIỂM XUYÊN VIỆT")
    run_t.font.name = "Times New Roman"
    run_t.font.size = Pt(17)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(26, 54, 93)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(2)
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run("HỆ THỐNG 18 TRẠM KIẾN THỨC (TUẦN 1 - 18) GẮN LIỀN VỚI ĐỊA DANH VIỆT NAM\nPhục vụ kiểm duyệt đề - Hệ thống bài tập tương tác EduRobot.id.vn")
    run_sub.font.name = "Times New Roman"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(74, 85, 104)

    # Thêm bảng tổng quan 18 trạm
    intro_tbl = doc.add_table(rows=1, cols=4)
    intro_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Cm(1.5), Cm(2.2), Cm(6.5), Cm(6.3)]
    hdr_titles = ["Trạm", "Tuần", "Địa danh thắng cảnh", "Chủ đề trọng tâm"]
    for i, title in enumerate(hdr_titles):
        c = intro_tbl.rows[0].cells[i]
        c.width = widths[i]
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(title)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        tcPr = c._tc.get_or_add_tcPr()
        shd = parse_xml(r'<w:shd {} w:fill="2B6CB0"/>'.format(nsdecls('w')))
        tcPr.append(shd)

    for st in STATIONS_DATA:
        row = intro_tbl.add_row().cells
        row[0].width = widths[0]
        row[1].width = widths[1]
        row[2].width = widths[2]
        row[3].width = widths[3]
        
        row[0].paragraphs[0].text = str(st["tram_so"])
        row[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row[1].paragraphs[0].text = f"Tuần {st['tuan']}"
        row[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row[2].paragraphs[0].text = st["ten_tram"]
        row[3].paragraphs[0].text = st["chu_de"]
        for c in row:
            for p in c.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for run in p.runs:
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(9.5)
            tcPr = c._tc.get_or_add_tcPr()
            borders = parse_xml(r'''
                <w:tcBorders {} >
                    <w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                    <w:left w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                    <w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                </w:tcBorders>
            '''.format(nsdecls('w')))
            tcPr.append(borders)

    # Sang trang cho từng trạm
    for st in STATIONS_DATA:
        doc.add_page_break()
        build_station_table(doc, st)

    doc.save(target_path)
    print(f"Master docx saved: {target_path}")

def generate_individual_documents(output_folder):
    """Tạo từng file Word độc lập cho mỗi trạm (Tuần 1 đến Tuần 18)"""
    for st in STATIONS_DATA:
        doc = setup_document_styles()
        
        # Tiêu đề file
        p_title = doc.add_paragraph()
        p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_title.paragraph_format.space_before = Pt(6)
        p_title.paragraph_format.space_after = Pt(2)
        run_t = p_title.add_run(f"ĐỀ KIỂM TRA TOÁN 5 - TUẦN {st['tuan']}")
        run_t.font.name = "Times New Roman"
        run_t.font.size = Pt(15)
        run_t.font.bold = True
        run_t.font.color.rgb = RGBColor(26, 54, 93)

        build_station_table(doc, st)
        
        file_name = f"De_Tuan_{st['tuan']:02d}_Tram_{st['tram_so']:02d}.docx"
        file_path = os.path.join(output_folder, file_name)
        doc.save(file_path)
    print(f"Generated 18 individual week files in: {output_folder}")

if __name__ == "__main__":
    output_dir = r"c:\Users\Admin\Desktop\EduBot-BTCT5\Đề"
    os.makedirs(output_dir, exist_ok=True)
    
    master_file = os.path.join(output_dir, "Bo_De_Toan_5_Tuan_1_den_18.docx")
    generate_master_document(master_file)
    generate_individual_documents(output_dir)
    print("ALL DONE SUCCESSFULLY!")
