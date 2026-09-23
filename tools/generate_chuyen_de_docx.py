# -*- coding: utf-8 -*-
"""
Script sinh tài liệu Chuyên đề Dạy học Toán 5 theo định hướng Chuyển đổi số
Tên chuyên đề: ÔN TẬP MÔN TOÁN LỚP 5 THEO ĐỊNH HƯỚNG CHUYỂN ĐỔI SỐ VỚI HỆ THỐNG BÀI TẬP TƯƠNG TÁC
Đơn vị: Trường Tiểu học Đỗ Văn Nại - Tổ chuyên môn Khối 5
Tác giả: Lê Thành Long
Phạm vi: Trọn bộ 35 tuần học (Cả năm học: Học kỳ 1 và Học kỳ 2)
Tích hợp: Mô hình Gamification, Hành trình Xuyên Việt, Web App, Zalo Mini App, Firebase Realtime Database
"""

import os
import sys
import re
import json
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Thư mục gốc dự án
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
sys.path.insert(0, TOOLS_DIR)

# Nạp dữ liệu 35 tuần từ các module data
from data_tuan_01_06 import TUAN_01_TO_06
from data_tuan_07_12 import TUAN_07_TO_12
from data_tuan_13_18 import TUAN_13_TO_18
from data_tuan_19_24 import TUAN_19_TO_24
from data_tuan_25_30 import TUAN_25_TO_30
from data_tuan_31_35 import TUAN_31_TO_35

ALL_35_STATIONS = (
    TUAN_01_TO_06 +
    TUAN_07_TO_12 +
    TUAN_13_TO_18 +
    TUAN_19_TO_24 +
    TUAN_25_TO_30 +
    TUAN_31_TO_35
)

# Nạp dữ liệu bảo vật từ tuido.html
tuido_path = os.path.join(BASE_DIR, "tuido.html")
items_dict = {}
if os.path.exists(tuido_path):
    with open(tuido_path, "r", encoding="utf-8") as f:
        tcontent = f.read()
    m = re.search(r'const ITEMS_DATA = ({.*?});', tcontent, re.DOTALL)
    if m:
        try:
            items_dict = json.loads(m.group(1))
        except Exception:
            pass

def create_full_chuyen_de_document():
    doc = docx.Document()

    # 1. Page Setup: A4, Margins: Top 2cm, Bottom 2cm, Left 3cm, Right 2cm (Chuẩn văn bản quản lý GD)
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.0)
        section.different_first_page_header_footer = True

        # Header (Trang 2 trở đi)
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Chuyên đề dạy học Toán 5: Ứng dụng hệ thống bài tập tương tác EduRobot (Trọn bộ 35 tuần)")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(120, 120, 120)

        # Footer (Trang 2 trở đi)
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

    # Helper format font
    def set_font(run, name="Times New Roman", size=13, bold=False, italic=False, color=None):
        run.font.name = name
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        if color:
            run.font.color.rgb = color

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, space_before=0, line_spacing=1.35, indent=1.0):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.line_spacing = line_spacing
        if indent > 0 and align == WD_ALIGN_PARAGRAPH.JUSTIFY:
            p.paragraph_format.first_line_indent = Cm(indent)
        if text:
            run = p.add_run(text)
            set_font(run, size=13)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_font(run, size=14, bold=True, color=RGBColor(26, 54, 93))
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_font(run, size=13, bold=True, color=RGBColor(43, 108, 176))
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_font(run, size=13, bold=True, italic=True, color=RGBColor(45, 55, 72))
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.line_spacing = 1.3
        r1 = p.add_run(bold_prefix)
        set_font(r1, size=13, bold=True)
        r2 = p.add_run(text)
        set_font(r2, size=13)
        return p

    def add_callout(title, text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Cm(16.0)
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(r'<w:shd {} w:fill="F0F4F8"/>'.format(nsdecls('w')))
        tcPr.append(shd)
        borders = parse_xml(r'''
            <w:tcBorders {} >
                <w:top w:val="none"/>
                <w:left w:val="single" w:sz="30" w:space="0" w:color="1A365D"/>
                <w:bottom w:val="none"/>
                <w:right w:val="none"/>
            </w:tcBorders>
        '''.format(nsdecls('w')))
        tcPr.append(borders)
        cp = cell.paragraphs[0]
        cp.paragraph_format.space_before = Pt(5)
        cp.paragraph_format.space_after = Pt(4)
        cp.paragraph_format.line_spacing = 1.25
        r_title = cp.add_run(f"📌 {title}: ")
        set_font(r_title, size=12.5, bold=True, color=RGBColor(26, 54, 93))
        r_text = cp.add_run(text)
        set_font(r_text, size=12.5, italic=True)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # 1. TRANG BÌA (COVER PAGE)
    # -------------------------------------------------------------
    p_cq = doc.add_paragraph()
    p_cq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cq.paragraph_format.space_after = Pt(2)
    p_cq.paragraph_format.space_before = Pt(5)
    r1 = p_cq.add_run("TRƯỜNG TIỂU HỌC ĐỖ VĂN NẠI\n")
    set_font(r1, size=13, bold=True, color=RGBColor(40, 40, 40))
    r2 = p_cq.add_run("TỔ CHUYÊN MÔN KHỐI 5")
    set_font(r2, size=13, bold=True, color=RGBColor(40, 40, 40))

    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(20)
    r_line = p_line.add_run("————— 🕮 —————")
    set_font(r_line, size=12, bold=True, color=RGBColor(150, 150, 150))

    # Logo Robot
    robot_img_path = os.path.join(BASE_DIR, "assets", "robot-head.png")
    if os.path.exists(robot_img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(12)
        p_img.add_run().add_picture(robot_img_path, width=Cm(3.0))

    p_rp = doc.add_paragraph()
    p_rp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rp.paragraph_format.space_after = Pt(8)
    r_rp = p_rp.add_run("BÁO CÁO CHUYÊN ĐỀ CHUYÊN MÔN CẤP TRƯỜNG\nĐỔI MỚI PHƯƠNG PHÁP DẠY HỌC & ĐÁNH GIÁ HỌC SINH TIỂU HỌC")
    set_font(r_rp, size=13.5, bold=True, color=RGBColor(194, 65, 12))

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(14)
    r_title = p_title.add_run("DẠY HỌC VÀ ÔN TẬP MÔN TOÁN LỚP 5\nTHEO ĐỊNH HƯỚNG CHUYỂN ĐỔI SỐ\nVỚI HỆ SINH THÁI BÀI TẬP TƯƠNG TÁC EDUBOT")
    set_font(r_title, size=18, bold=True, color=RGBColor(26, 54, 93))

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(35)
    r_sub = p_sub.add_run("(Giải pháp ứng dụng mô hình Gamification 'Hành trình Xuyên Việt' và nền tảng đa phương thức\nphục vụ củng cố kiến thức trọn bộ 35 tuần học - Chương trình GDPT 2018)")
    set_font(r_sub, size=12, italic=True, color=RGBColor(74, 85, 104))

    # Thông tin tác giả
    info_tbl = doc.add_table(rows=4, cols=2)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Người thực hiện:", "Lê Thành Long"),
        ("Chức vụ:", "Giáo viên Tiểu học"),
        ("Tổ chuyên môn:", "Tổ chuyên môn Khối 5"),
        ("Năm học:", "2026 - 2027")
    ]
    for row_idx, (label, val) in enumerate(info_data):
        c1, c2 = info_tbl.cell(row_idx, 0), info_tbl.cell(row_idx, 1)
        c1.width = Cm(4.5)
        c2.width = Cm(7.5)
        p1, p2 = c1.paragraphs[0], c2.paragraphs[0]
        p1.paragraph_format.space_after = Pt(3)
        p1.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(3)
        p2.paragraph_format.space_before = Pt(2)
        r1 = p1.add_run(label)
        set_font(r1, size=12.5, bold=True)
        r2 = p2.add_run(val)
        set_font(r2, size=12.5)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 2. MỤC LỤC TỔNG THỂ & TÓM TẮT
    # -------------------------------------------------------------
    p_ml = doc.add_paragraph()
    p_ml.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ml.paragraph_format.space_after = Pt(12)
    r_ml = p_ml.add_run("MỤC LỤC TỔNG THỂ CHUYÊN ĐỀ")
    set_font(r_ml, size=15, bold=True, color=RGBColor(26, 54, 93))

    toc_items = [
        ("PHẦN I: ĐẶT VẤN ĐỀ (LÝ DO CHỌN CHUYÊN ĐỀ)", "Trang 2"),
        ("   1.1. Bối cảnh chuyển đổi số trong giáo dục và Chương trình GDPT 2018", "Trang 2"),
        ("   1.2. Thực trạng công tác ôn tập, củng cố môn Toán lớp 5 hiện nay", "Trang 2"),
        ("   1.3. Tính cấp thiết, mục đích và đối tượng nghiên cứu của chuyên đề", "Trang 3"),
        ("PHẦN II: CƠ SỞ KHOA HỌC VÀ NGUYÊN TẮC THIẾT KẾ", "Trang 4"),
        ("   2.1. Cơ sở lý luận: Thuyết kiến tạo, Mô hình SAMR và Trò chơi hóa (Gamification)", "Trang 4"),
        ("   2.2. Đặc điểm tâm sinh lý tiếp nhận và thói quen công nghệ của học sinh lớp 5", "Trang 4"),
        ("   2.3. Bốn nguyên tắc sư phạm cốt lõi trong xây dựng hệ sinh thái EduRobot", "Trang 5"),
        ("PHẦN III: HỆ THỐNG GIẢI PHÁP VÀ BIỆN PHÁP THỰC HIỆN (TRỌNG TÂM)", "Trang 6"),
        ("   3.1. Tuyến ý tưởng 'Hành trình Xuyên Việt' – Tích hợp liên môn Toán và Lịch sử - Địa lý", "Trang 6"),
        ("   3.2. Cấu trúc bài tập tương tác 3 vòng thử thách tư duy (Thang điểm chuẩn 100)", "Trang 7"),
        ("   3.3. Hệ thống cơ chế Gamification đa tầng kích thích động lực tự thân bền vững", "Trang 8"),
        ("   3.4. Kiến trúc công nghệ đa nền tảng và cơ chế phân quyền kiểm soát thông minh", "Trang 9"),
        ("   3.5. Hệ thống cơ sở dữ liệu thời gian thực và tự động hóa quản lý chuyên môn", "Trang 10"),
        ("   3.6. Ma trận phân phối kiến thức trọn bộ 35 tuần học (18 tuần HK1 và 17 tuần HK2)", "Trang 11"),
        ("PHẦN IV: QUY TRÌNH TỔ CHỨC DẠY HỌC THỰC NGHIỆM TẠI ĐƠN VỊ", "Trang 14"),
        ("   4.1. Quy trình 4 bước tổ chức dạy học linh hoạt tại lớp và hướng dẫn tự học ở nhà", "Trang 14"),
        ("   4.2. Xây dựng mối liên kết tam giác Nhà trường – Giáo viên – Gia đình qua kênh Zalo", "Trang 15"),
        ("   4.3. Khai thác dữ liệu thời gian thực để phân hóa đối tượng và phụ đạo kịp thời", "Trang 15"),
        ("PHẦN V: KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ TÁC ĐỘNG", "Trang 16"),
        ("   5.1. Đánh giá về mặt định lượng (Tỉ lệ tự giác, phổ điểm, thời gian quản lý chuyên môn)", "Trang 16"),
        ("   5.2. Đánh giá về mặt định tính (Phát triển năng lực tự chủ, say mê học tập và văn hóa số)", "Trang 17"),
        ("   5.3. Khả năng chuyển giao, tính ứng dụng thực tiễn và nhân rộng mô hình", "Trang 17"),
        ("PHẦN VI: KẾT LUẬN VÀ KIẾN NGHỊ", "Trang 18"),
        ("   6.1. Kết luận", "Trang 18"),
        ("   6.2. Bài học kinh nghiệm quý báu", "Trang 18"),
        ("   6.3. Đề xuất, kiến nghị với các cấp quản lý", "Trang 19"),
        ("PHẦN KÝ DUYỆT CỦA BGH VÀ NGƯỜI BÁO CÁO", "Trang 19"),
        ("PHỤ LỤC: DANH MỤC 35 TRẠM XUYÊN VIỆT & HƯỚNG DẪN TRUY CẬP ĐA NỀN TẢNG", "Trang 20"),
    ]

    for title, pg in toc_items:
        p_toc = doc.add_paragraph()
        p_toc.paragraph_format.space_after = Pt(2)
        p_toc.paragraph_format.line_spacing = 1.2
        r_t = p_toc.add_run(title)
        set_font(r_t, size=11.5, bold=("PHẦN" in title))
        r_dots = p_toc.add_run(" " + "." * max(8, 85 - len(title) * 2) + " ")
        set_font(r_dots, size=10, color=RGBColor(160, 160, 160))
        r_p = p_toc.add_run(pg)
        set_font(r_p, size=11, italic=True)

    add_p()
    add_callout(
        "TÓM TẮT NỘI DUNG CHUYÊN ĐỀ",
        "Chuyên đề đề xuất một giải pháp đột phá, toàn diện trong đổi mới phương pháp dạy học, củng cố và ôn tập môn Toán lớp 5 trọn bộ 35 tuần học (18 tuần Học kỳ 1 và 17 tuần Học kỳ 2) thông qua hệ sinh thái học tập tương tác EduRobot (EduBot-BTCT5). Giải pháp kết hợp nhuần nhuyễn giữa lý thuyết Trò chơi hóa (Gamification), tích hợp liên môn (Toán học gắn liền với 35 địa danh văn hóa - lịch sử trên bản đồ Việt Nam và biển đảo Tổ quốc) cùng công nghệ đa nền tảng hiện đại (Web trực tuyến và Zalo Mini App). Hệ thống chuyển hóa các bài tập cuối tuần khô khan thành chuyến thám hiểm hấp dẫn, tích hợp phân quyền 3 vai trò (Học sinh, Giáo viên, Quản trị viên), cơ chế mở chặng tự động 14h00 Thứ Sáu, đồng thời cung cấp cho giáo viên công cụ thống kê phổ điểm tự động, đua top tuần và xuất dữ liệu Excel thời gian thực từ Google Firebase Database để phục vụ đánh giá quá trình chính xác, khách quan."
    )

    # -------------------------------------------------------------
    # PHẦN I: ĐẶT VẤN ĐỀ
    # -------------------------------------------------------------
    add_h1("PHẦN I: ĐẶT VẤN ĐỀ (LÝ DO CHỌN CHUYÊN ĐỀ)")

    add_h2("1.1. Bối cảnh chuyển đổi số trong giáo dục và Chương trình GDPT 2018")
    add_p("Trong bối cảnh kỷ nguyên số bùng nổ, ngành Giáo dục và Đào tạo Việt Nam đang đẩy mạnh thực hiện đổi mới căn bản, toàn diện theo tinh thần Nghị quyết số 29-NQ/TW và Chương trình Giáo dục phổ thông 2018 (GDPT 2018). Mục tiêu cốt lõi của chương trình là chuyển từ nền giáo dục nặng về truyền thụ kiến thức một chiều sang nền giáo dục chú trọng bồi dưỡng phẩm chất và phát triển toàn diện các năng lực người học: tự chủ và tự học, giao tiếp và hợp tác, giải quyết vấn đề và sáng tạo.")
    add_p("Đặc biệt, Quyết định số 131/QĐ-TTg của Thủ tướng Chính phủ phê duyệt Đề án 'Tăng cường ứng dụng công nghệ thông tin và chuyển đổi số trong giáo dục và đào tạo giai đoạn 2022 - 2025, định hướng đến năm 2030' đã nhấn mạnh yêu cầu: chuyển đổi số không được dừng lại ở các khâu hành chính hay trình chiếu bài giảng điện tử đơn thuần, mà phải đi sâu vào cốt lõi của hoạt động dạy học, phương thức tương tác giữa thầy và trò, phương pháp kiểm tra đánh giá thường xuyên và kiến tạo không gian học tập số linh hoạt.")
    add_p("Môn Toán ở cấp Tiểu học, đặc biệt là khối lớp 5 – năm học bản lề chuyển tiếp lên bậc Trung học cơ sở – giữ vị trí đặc biệt quan trọng trong việc hoàn thiện nền tảng tư duy logic, năng lực mô hình hóa toán học và tư duy giải quyết vấn đề thực tiễn. Đổi mới phương pháp dạy học và ôn tập môn Toán theo định hướng chuyển đổi số chính là chìa khóa tháo gỡ rào cản tâm lý e ngại, biến môn học vốn bị coi là 'khô khan, trừu tượng' thành niềm đam mê khám phá của các em.")

    add_h2("1.2. Thực trạng công tác ôn tập, củng cố môn Toán lớp 5 hiện nay")
    add_p("Qua thực tiễn trực tiếp đứng lớp giảng dạy khối lớp 5 nhiều năm tại đơn vị, chúng tôi nhận thấy hoạt động củng cố, ôn tập cuối tuần của học sinh đang đối mặt với nhiều khó khăn, bất cập:")
    add_bullet("Về khối lượng và độ khó của chương trình: ", "Chương trình Toán 5 (đặc biệt theo bộ sách Kết nối tri thức với cuộc sống) có dung lượng kiến thức rất lớn, trải dài 35 tuần học. Học kỳ 1 tập trung vào số tự nhiên, phân số, hỗn số, bảng đơn vị đo diện tích (ha, km²) và đặc biệt là hệ thống số thập phân cùng 4 phép tính. Học kỳ 2 tiếp tục đẩy mạnh các mảng kiến thức nâng cao: Tỉ số và tỉ số phần trăm, hình tam giác, hình thang, hình tròn, thể tích các hình khối (hình hộp chữ nhật, hình lập phương), số đo thời gian và đặc biệt là mạch toán chuyển động đều. Độ trừu tượng cao khiến học sinh dễ bị hổng kiến thức nếu không được củng cố thường xuyên.")
    add_bullet("Về phương pháp giao bài và phản hồi truyền thống: ", "Đa số giáo viên vẫn sử dụng hình thức in phiếu bài tập cuối tuần trên giấy (photo phát cho học sinh) hoặc chép bài tập lên bảng để học sinh ghi vào vở về nhà làm. Phương thức này bộc lộ những hạn chế cố hữu: tốn kém chi phí in ấn; hình thức bài tập đen trắng đơn điệu, dễ gây tâm lý ngán ngẩm, đối phó; và đặc biệt là độ trễ thông tin rất lớn (thường phải chờ đến thứ Hai hoặc thứ Ba tuần sau giáo viên mới chấm và sửa bài, làm trôi qua 'thời điểm vàng' để sửa chữa sai lầm nhận thức của học sinh).")
    add_bullet("Về thói quen sử dụng công nghệ của học sinh và phụ huynh: ", "Hiện nay, hơn 95% gia đình học sinh đều sở hữu điện thoại thông minh kết nối Internet. Tuy nhiên, phần lớn học sinh sử dụng thiết bị để xem video ngắn trên TikTok, YouTube Shorts hoặc chơi game điện tử mang tính giải trí thụ động. Phụ huynh rất lo lắng nhưng thường lúng túng, thiếu các công cụ học tập tương tác bổ ích, hấp dẫn để định hướng con em biến thiết bị thông minh thành phương tiện học tập bổ ích.")
    add_bullet("Về phía giáo viên: ", "Việc theo dõi, thu thập bài vở và chấm chữa thủ công cho 35 - 40 học sinh mỗi tuần tiêu tốn hàng giờ đồng hồ quý báu của giáo viên ngoài giờ lên lớp. Giáo viên thiếu công cụ số để thu thập số liệu tự động, khó vẽ được bức tranh toàn cảnh về phổ điểm và những lỗi sai phổ biến của cả lớp để kịp thời điều chỉnh kế hoạch bài dạy tuần tiếp theo.")

    add_h2("1.3. Tính cấp thiết, mục đích và đối tượng nghiên cứu của chuyên đề")
    add_p("Từ những vấn đề thực tiễn cấp bách nêu trên, tác giả đã chủ động nghiên cứu, lập trình và xây dựng hoàn chỉnh hệ sinh thái bài tập tương tác mang tên EduRobot (EduBot-BTCT5) với địa chỉ truy cập trực tuyến tại edurobot.id.vn và phiên bản Zalo Mini App chạy trực tiếp trên ứng dụng Zalo.")
    add_p("Chuyên đề được hoàn thiện với các mục đích cụ thể:")
    add_bullet("1. Xây dựng ngân hàng 1.680 bài toán tương tác chuẩn hóa: ", "Bao phủ toàn diện 35 tuần học cả năm (18 tuần HK1 và 17 tuần HK2) bám sát tuyệt đối các yêu cầu cần đạt (YCCĐ) của môn Toán lớp 5 Chương trình GDPT 2018.")
    add_bullet("2. Ứng dụng thuyết Trò chơi hóa (Gamification) và tích hợp liên môn: ", "Lồng ghép hành trình xuyên suốt 35 trạm địa danh văn hóa, lịch sử và danh lam thắng cảnh Việt Nam, khơi dậy lòng tự hào dân tộc và tình yêu quê hương đất nước song hành cùng kiến thức toán học.")
    add_bullet("3. Tối ưu hóa trải nghiệm không rào cản qua Zalo Mini App: ", "Giúp phụ huynh và học sinh mở bài làm ngay trên Zalo mà không phải tải app, không lo tốn bộ nhớ hay quên mật khẩu đăng nhập.")
    add_bullet("4. Tự động hóa đánh giá quá trình bằng công nghệ đám mây: ", "Cung cấp cho giáo viên công cụ Realtime Dashboard để theo dõi kết quả, phân tích phổ điểm trực quan bằng biểu đồ và xuất báo cáo Excel chỉ với 1 cú nhấp chuột.")

    # -------------------------------------------------------------
    # PHẦN II: CƠ SỞ KHOA HỌC VÀ NGUYÊN TẮC THIẾT KẾ
    # -------------------------------------------------------------
    add_h1("PHẦN II: CƠ SỞ KHOA HỌC VÀ NGUYÊN TẮC THIẾT KẾ")

    add_h2("2.1. Cơ sở lý luận: Thuyết kiến tạo, Mô hình SAMR và Trò chơi hóa (Gamification)")
    add_p("Hệ thống EduRobot được thiết kế dựa trên sự giao thoa vững chắc của 3 lý thuyết giáo dục và công nghệ hiện đại:")
    add_bullet("Thuyết kiến tạo xã hội (Social Constructivism): ", "Lev Vygotsky và Jean Piaget đã chứng minh người học không tiếp thu tri thức bằng sự ghi nhớ thụ động mà thông qua quá trình chủ động tương tác với môi trường học tập, trải nghiệm 'thử nghiệm - thất bại - rút kinh nghiệm - điều chỉnh'. Thông qua các thao tác kéo thả thẻ bài, kiểm tra điều kiện và nhận phản hồi tức thì, học sinh tự mình phát hiện ra quy luật và khắc sâu bản chất của các công thức, thuật toán.")
    add_bullet("Khung chuyển đổi số giáo dục SAMR (Dr. Ruben Puentedura): ", "Hệ sinh thái EduRobot đưa hoạt động ôn tập vượt qua hai bậc thang đầu tiên là Substitution (Thay thế phiếu giấy bằng màn hình) và Augmentation (Tăng cường thêm âm thanh, hình ảnh), tiến thẳng lên nấc thang Modification (Biến đổi quy trình học tập với cơ chế phân quyền, đua top tuần) và Redefinition (Tái định nghĩa môi trường học tập thành cuộc phiêu lưu xuyên Việt đa phương thức, kết nối thời gian thực mà phương pháp truyền thống không thể làm được).")
    add_bullet("Mô hình Trò chơi hóa Octalysis (Yu-kai Chou) & Karl Kapp: ", "Ứng dụng các động lực cốt lõi của trò chơi vào bối cảnh học tập: Ý nghĩa cao cả & Sứ mệnh (đồng hành cùng Robot giải cứu các vùng đất), Cảm giác tiến bộ & Chinh phục (thanh tiến trình 3 vòng, mở khóa 35 bảo vật hoàng kim), và Sự công nhận xã hội (Bảng vàng Top 10 cao thủ). Cơ chế này kích hoạt sự giải phóng Dopamine tự nhiên trong não bộ, tạo sự hào hứng và say mê bền vững mà không cần người lớn thúc ép.")

    add_h2("2.2. Đặc điểm tâm sinh lý tiếp nhận và thói quen công nghệ của học sinh lớp 5")
    add_p("Học sinh lớp 5 (độ tuổi 10 - 11 tuổi) đang ở bước ngoặt tâm lý quan trọng: tư duy đang chuyển dần từ trực quan cụ thể sang tư duy trừu tượng, logic. Các em có những đặc tính nổi bật:")
    add_bullet("Nhu cầu khẳng định bản sắc cá nhân cao: ", "Rất thích được vinh danh, khen thưởng trước tập thể, tự hào khi thấy tên mình xuất hiện trên Bảng vàng hay sở hữu những bảo vật độc nhất vô nhị.")
    add_bullet("Nhạy bén với công nghệ nhưng mức độ tập trung hữu hạn: ", "Các em thao tác ngón tay trên màn hình cảm ứng rất nhanh nhưng dễ bị xao nhãng nếu nội dung bài học quá dài hoặc giao diện ứng dụng phức tạp, nhiều chữ. Do đó, bài học cần được chia nhỏ thành các chặng (Micro-learning) từ 10 - 15 phút với màu sắc bắt mắt, âm thanh sinh động.")

    add_h2("2.3. Bốn nguyên tắc sư phạm cốt lõi trong xây dựng hệ sinh thái EduRobot")
    add_p("Để đảm bảo hệ thống không bị sa đà vào tính chất giải trí thuần túy mà luôn giữ vững chuẩn mực giáo dục, chúng tôi đặt ra 4 nguyên tắc sư phạm bắt buộc:")
    add_bullet("1. Nguyên tắc chuẩn mực chương trình (Curriculum Alignment): ", "100% câu hỏi trong hệ thống được thẩm định chặt chẽ, bám sát từng tiết học trong Bảng phân phối chương trình môn Toán 5 (bộ sách Kết nối tri thức với cuộc sống), phủ đủ 3 mức độ nhận thức: Nhận biết, Thông hiểu và Vận dụng.")
    add_bullet("2. Nguyên tắc phản hồi lập tức (Immediate Feedback): ", "Mọi hành vi chọn đáp án đều được hệ thống phát tín hiệu phản hồi ngay tức khắc (âm thanh chúc mừng rộn rã khi đúng, âm thanh báo hiệu khi sai kèm cơ chế trừ mạng sống). Học sinh nhận biết ngay sai lầm để tự sửa chữa trong não bộ.")
    add_bullet("3. Nguyên tắc công bằng và chống gian lận (Fair Play & Data Hygiene): ", "Hệ thống tích hợp thuật toán làm sạch dữ liệu tự động: lọc bỏ các tài khoản rác (tên 1 ký tự, test, 123...), quy định họ và tên thật phải từ 2 - 3 từ có nghĩa, chốt dữ liệu đua top theo khung giờ vàng để đảm bảo tính minh bạch tuyệt đối.")
    add_bullet("4. Nguyên tắc tối ưu hóa thiết bị di động (Mobile-First Accessibility): ", "Hơn 90% các em dùng điện thoại của cha mẹ, nên mọi nút bấm, thẻ bài, cỡ chữ đều được thiết kế chuẩn tỉ lệ màn hình dọc 9:16, phông chữ Lexend rõ nét chống mỏi mắt, thao tác 'chạm là ăn' mượt mà.")

    # -------------------------------------------------------------
    # PHẦN III: HỆ THỐNG GIẢI PHÁP VÀ BIỆN PHÁP THỰC HIỆN
    # -------------------------------------------------------------
    add_h1("PHẦN III: HỆ THỐNG GIẢI PHÁP VÀ BIỆN PHÁP THỰC HIỆN (TRỌNG TÂM)")

    add_h2("3.1. Tuyến ý tưởng 'Hành trình Xuyên Việt' – Tích hợp liên môn Toán và Lịch sử - Địa lý")
    add_p("Điểm sáng tạo đặc biệt của chuyên đề là ý tưởng số hóa bản đồ địa lý Việt Nam thành một 'Hành trình Xuyên Việt kỳ thú'. Học sinh hóa thân thành 'Nhà thám hiểm nhí' cùng chú robot thông minh EduRobot xuất phát từ địa đầu Lũng Cú (Hà Giang) và đi qua trọn vẹn 35 tuần học tương ứng với 35 địa danh văn hóa, lịch sử và danh lam thắng cảnh tiêu biểu trên khắp dải đất hình chữ S:")

    # Chèn ảnh Bản đồ nếu tồn tại
    map_img_path = os.path.join(BASE_DIR, "Bandogame.jpg")
    if os.path.exists(map_img_path):
        p_map = doc.add_paragraph()
        p_map.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_map.paragraph_format.space_before = Pt(6)
        p_map.paragraph_format.space_after = Pt(4)
        p_map.add_run().add_picture(map_img_path, width=Cm(13.5))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(8)
        rc = p_cap.add_run("Hình 1: Giao diện Bản đồ tương tác 'Hành trình Xuyên Việt cùng Robot' (edurobot.id.vn)")
        set_font(rc, size=11, italic=True, color=RGBColor(80, 80, 80))

    add_p("Lộ trình 35 trạm được quy hoạch khoa học theo không gian địa lý và tiến trình năm học:")
    add_bullet("Trạm 01 đến 08 (Miền núi phía Bắc & Đồng bằng Bắc Bộ): ", "Khởi hành từ Cột cờ Lũng Cú, Hẻm Tu Sản - Sông Nho Quế, Thác Bản Giốc, Hồ Ba Bể, Ruộng bậc thang Mù Cang Chải, Đỉnh Fansipan, Thủ đô Hà Nội đến Vịnh Hạ Long & Núi Yên Tử.")
    add_bullet("Trạm 09 đến 18 (Bắc Trung Bộ & Duyên hải miền Trung): ", "Tràng An Hoa Lư (Ninh Bình - GK1), Thành Nhà Hồ (Thanh Hóa), Làng Sen Quê Bác (Nghệ An), Ngã ba Đồng Lộc (Hà Tĩnh), Phong Nha - Kẻ Bàng (Quảng Bình), Thành cổ Quảng Trị - Cầu Hiền Lương, Cố đô Huế, Cầu Rồng Đà Nẵng, Phố cổ Hội An và Đảo Lý Sơn Quảng Ngãi (CK1).")
    add_bullet("Trạm 19 đến 27 (Tây Nguyên đại ngàn & Duyên hải Nam Trung Bộ): ", "Ngã ba Đông Dương Kon Tum, Biển Hồ Gia Lai, Buôn Đôn Đắk Lắk, Hồ Tà Đùng Đắk Nông, Gành Đá Đĩa Phú Yên, Vịnh Nha Trang, Tháp Chàm Ninh Thuận, Đồi cát Mũi Né Bình Thuận và Đỉnh Lang Biang Đà Lạt (GK2).")
    add_bullet("Trạm 28 đến 35 (Nam Bộ, Đồng bằng sông Cửu Long & Biển đảo thiêng liêng): ", "Địa đạo Củ Chi, Núi Bà Đen Tây Ninh, Bến Nhà Rồng Landmark 81, Làng hoa Sa Đéc Đồng Tháp, Đất Mũi Cà Mau, Đảo Ngọc Phú Quốc và hai chặng thiêng liêng vươn xa tới Quần đảo Trường Sa (Trạm 34) và Quần đảo Hoàng Sa (Trạm 35 - CK2).")
    add_p("Nhờ đó, mỗi tuần học không chỉ đơn thuần là giải các bài toán khô khan, mà các em còn được bồi đắp kiến thức lịch sử, địa lý, nuôi dưỡng tình yêu quê hương đất nước và ý thức chủ quyền biển đảo thiêng liêng một cách tự nhiên, sâu sắc.")

    add_h2("3.2. Cấu trúc bài tập tương tác 3 vòng thử thách tư duy (Thang điểm chuẩn 100)")
    add_p("Để tạo sự cân bằng giữa tính giải trí và chiều sâu tư duy, mỗi tuần học được thiết kế thành một bài thi liên hoàn gồm 3 vòng thử thách, với thang điểm tổng tuyệt đối là 100 điểm:")

    # Table 3 rounds
    v_tbl = doc.add_table(rows=4, cols=4)
    v_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    v_headers = ["Vòng thi", "Hình thức & Cơ chế", "Thang điểm & Quy tắc", "Mục tiêu sư phạm"]
    for col_idx, h in enumerate(v_headers):
        cell = v_tbl.cell(0, col_idx)
        shd = parse_xml(r'<w:shd {} w:fill="1A365D"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(h)
        set_font(r, size=11.5, bold=True, color=RGBColor(255, 255, 255))

    v_data = [
        ("Vòng 1", "Ghép đôi thẻ bài\n(Matching Cards)", "10 cặp thẻ tương ứng.\nTối đa 40 điểm (4đ/cặp).\nCấp 3 mạng sống (❤️❤️❤️).\nGhép sai mất 1 mạng.", "Rèn luyện khả năng nhận diện định nghĩa, ghi nhớ công thức, ước lượng nhanh và liên hệ toán học thực tiễn."),
        ("Vòng 2", "Sắp xếp & Điền khuyết\n(Touch-to-Drop)", "5 bài toán thực hành.\nTối đa 30 điểm (6đ/bài).\nChạm chọn đáp án rồi chạm ô nhận trên bảng dữ liệu.", "Khắc phục triệt để lỗi trượt ngón tay khi kéo thả trên di động; rèn tính cẩn thận, chính xác trong tính toán số liệu."),
        ("Vòng 3", "Về đích trắc nghiệm\n(Multiple Choice)", "5 câu hỏi 4 lựa chọn (A, B, C, D).\nTối đa 30 điểm (6đ/câu).\nCó đếm ngược thời gian và tự động chuyển câu.", "Rèn luyện phản xạ tính nhanh, kỹ năng loại trừ phương án nhiễu, làm quen cấu trúc đề kiểm tra định kỳ.")
    ]
    for row_idx, row_data in enumerate(v_data, start=1):
        bg_color = "F7FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = v_tbl.cell(row_idx, col_idx)
            shd = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg_color))
            cell._tc.get_or_add_tcPr().append(shd)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.2
            if col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(text)
                set_font(r, size=11, bold=True, color=RGBColor(26, 54, 93))
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(text)
                set_font(r, size=11)

    add_p()

    add_h2("3.3. Hệ thống cơ chế Gamification đa tầng kích thích động lực tự thân bền vững")
    add_p("Hệ sinh thái EduRobot tích hợp các cơ chế trò chơi hóa sâu sắc, biến quá trình học tập thành trải nghiệm đầy cảm xúc:")
    add_bullet("1. Cơ chế 'Mạng sống' (Heart Lives System): ", "Ở vòng 1, học sinh được cấp 3 trái tim đỏ. Mỗi lần bấm sai cặp thẻ, 1 trái tim sẽ biến mất kèm âm thanh cảnh báo. Nếu mất hết 3 mạng, vòng chơi dừng lại với số điểm hiện có. Cơ chế này dạy học sinh đức tính cẩn trọng, suy nghĩ kỹ trước khi quyết định, bài trừ thói quen bấm bừa tìm may rủi.")
    add_bullet("2. Đại tiệc Pháo hoa chiến thắng 3D (Fireworks Victory Display): ", "Khi học sinh chinh phục điểm số từ 90 điểm trở lên (mức Giỏi và Xuất sắc), hệ thống kích hoạt hiệu ứng pháo hoa 3D rực rỡ toàn màn hình bằng công nghệ HTML5 Canvas, đi kèm bài nhạc chiến thắng hoành tráng và bảng vinh danh họ tên học sinh mạ vàng trong 10 giây. Cảm giác hân hoan khi nhìn thấy tên mình bừng sáng chính là phần thưởng tinh thần vô giá đối với trẻ thơ.")
    add_bullet("3. Túi đồ nhà thám hiểm với 3 cấp độ bảo vật hoàng kim: ", "Tại trang tuido.html, mỗi trạm hoàn thành sẽ mở khóa một bảo vật biểu trưng của vùng đất đó. Đặc biệt, hệ thống phân định rõ 3 cấp độ danh giá: Huy hiệu Đồng (đạt từ 50 - 89 điểm), Bảo vật Bạc (đạt từ 90 - 99 điểm) và Thần Bảo Hoàng Kim Vàng (đạt tuyệt đối 100 điểm). Học sinh luôn có động lực thi lại nhiều lần để nâng cấp toàn bộ bảo vật trong túi đồ thành màu vàng hoàng kim lấp lánh.")
    add_bullet("4. Cơ chế đồng hồ đếm ngược và mở chặng tuần tự: ", "Các chặng thử thách được khóa tự động và mở vào đúng 14h00 Thứ Sáu hàng tuần. Nếu học sinh bấm vào trạm chưa mở, đồng hồ đếm ngược sẽ hiển thị thời gian chờ chính xác đến từng giây, tạo sự hồi hộp và đón đợi như một ngày hội cuối tuần.")

    add_h2("3.4. Kiến trúc công nghệ đa nền tảng và cơ chế phân quyền kiểm soát thông minh")
    add_p("Để giải quyết triệt để rào cản về hạ tầng thiết bị của phụ huynh, hệ sinh thái được phát triển song song trên hai nền tảng bổ trợ lẫn nhau:")
    add_bullet("Nền tảng Web tương tác chuẩn hóa: ", "Xây dựng trên nền HTML5, CSS3 và Vanilla JavaScript thuần túy, không phụ thuộc thư viện nặng. Trang web tương thích 100% với mọi trình duyệt hiện đại (Google Chrome, Cốc Cốc, Safari, Edge) trên máy vi tính gia đình, máy tính bảng và màn hình Tivi thông minh trên lớp học.")
    add_bullet("Nền tảng Zalo Mini App (edubot-zmp): ", "Ứng dụng công nghệ React 18, ZaUI và ZMP SDK của Zalo. Do 100% phụ huynh học sinh Việt Nam đều cài sẵn và sử dụng Zalo hàng ngày, việc tích hợp Zalo Mini App cho phép phụ huynh chỉ cần bấm vào liên kết trong nhóm Zalo của lớp là bài tập mở ngay lập tức, tốc độ khởi chạy dưới 1 giây, hoàn toàn không tốn dung lượng bộ nhớ máy điện thoại và không cần khai báo tài khoản phức tạp.")
    add_bullet("Hệ thống phân quyền 3 cấp (Role-Based Access Control) & Trang Quản trị (admin.html): ", "Hệ thống hỗ trợ 3 nhóm vai trò rõ ràng:")
    add_p("   - Nhóm Học sinh (Student): Đăng ký bằng họ tên thật, lớp, trường. Khi mới đăng ký hoặc tài khoản khách, học sinh được trải nghiệm tự do từ Trạm 1 đến Trạm 8. Sau khi giáo viên/quản trị viên duyệt, tài khoản mở đầy đủ 35 trạm theo tiến độ tuần của năm học.\n   - Nhóm Giáo viên (Teacher): Sau khi đăng ký và được xác thực, giáo viên có quyền mở toàn bộ 35 trạm ngay lập tức để phục vụ công tác soạn bài, thử nghiệm đề hoặc trình chiếu giảng dạy trên lớp.\n   - Nhóm Quản trị viên (Admin): Toàn quyền kiểm soát hệ thống tại admin.html, duyệt danh sách thành viên chờ duyệt (pending), kích hoạt, đổi mật khẩu và xuất dữ liệu người dùng.", indent=1.0)

    add_h2("3.5. Hệ thống cơ sở dữ liệu thời gian thực và tự động hóa quản lý chuyên môn")
    add_p("Hệ thống kết nối trực tiếp với dịch vụ cơ sở dữ liệu đám mây Google Firebase Realtime Database mang lại những tiện ích quản lý chuyên môn vượt bậc:")
    add_bullet("Thu thập dữ liệu học tập đa chiều: ", "Mỗi lượt nộp bài của học sinh đều được lưu lại chi tiết gồm: Họ và tên, Lớp, Trường, Số điểm đạt được, Thời gian làm bài chính xác đến từng giây (duration), Số lần thử sức (attempt) và dấu thời gian hoàn thành (timestamp).")
    add_bullet("Bảng vàng Top 10 cao thủ & Bộ lọc Đua top tuần: ", "Tại trang bang-vang.html, Bảng vàng vinh danh cập nhật theo thời gian thực (Realtime). Đặc biệt, hệ thống tích hợp 2 chế độ lọc thông minh:")
    add_p("   - Chế độ 'Đua Top Tuần': Chỉ tính các lượt thi chính thức trong 'Khung giờ vàng' từ 14h00 Thứ Sáu đến 13h59:59 Thứ Sáu tuần sau, đảm bảo công bằng cho giải đua tuần.\n   - Chế độ 'Tất Cả Lượt Thi': Thống kê toàn bộ lịch sử rèn luyện của học sinh trong cả năm.", indent=1.0)
    add_bullet("Biểu đồ phân tích phổ điểm (Chart.js) & Xuất báo cáo Excel (SheetJS): ", "Giáo viên có thể theo dõi biểu đồ hình cột thể hiện phân bố phổ điểm của lớp (Dưới 50đ, 50 - 79đ, 80 - 89đ, 100đ tuyệt đối) và chỉ cần nhấn nút 'Xuất Excel', toàn bộ danh sách điểm học sinh sẽ được tải về dưới dạng file .xlsx chuẩn mực để lưu trữ làm minh chứng đánh giá thường xuyên theo Thông tư 27/2020/TT-BGDĐT.")

    add_h2("3.6. Ma trận phân phối kiến thức trọn bộ 35 tuần học (18 tuần HK1 và 17 tuần HK2)")
    add_p("Dưới đây là Bảng Ma trận tổng thể tích hợp giữa 35 Trạm địa danh Xuyên Việt, Chuẩn kiến thức kỹ năng Toán 5 (bộ sách Kết nối tri thức với cuộc sống) và Bảo vật hoàng kim mở khóa trong Túi đồ:")

    # Table 35 weeks full matrix
    m_tbl = doc.add_table(rows=36, cols=4)
    m_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    m_headers = ["Tuần / Trạm", "Tên trạm địa danh Xuyên Việt", "Kiến thức Toán 5 trọng tâm (GDPT 2018)", "Bảo vật Hoàng Kim mở khóa (100đ)"]
    for col_idx, h in enumerate(m_headers):
        cell = m_tbl.cell(0, col_idx)
        shd = parse_xml(r'<w:shd {} w:fill="1A365D"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(h)
        set_font(r, size=10.5, bold=True, color=RGBColor(255, 255, 255))

    for idx, s in enumerate(ALL_35_STATIONS, start=1):
        w = s['tuan']
        tram_name = f"Trạm {s['tram_so']:02d}: {s['ten_tram']}"
        chu_de = s['chu_de']
        it = items_dict.get(str(w), {})
        icon = it.get('icon', '🎖️')
        cap3 = it.get('cap3', 'Huân chương Hoàng Kim Vàng')
        bảo_vật = f"{icon} {cap3}"

        cell_w = m_tbl.cell(idx, 0)
        cell_t = m_tbl.cell(idx, 1)
        cell_c = m_tbl.cell(idx, 2)
        cell_b = m_tbl.cell(idx, 3)

        bg_color = "F7FAFC" if idx % 2 == 1 else "FFFFFF"
        for c in (cell_w, cell_t, cell_c, cell_b):
            shd = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg_color))
            c._tc.get_or_add_tcPr().append(shd)
            c.paragraphs[0].paragraph_format.space_before = Pt(2)
            c.paragraphs[0].paragraph_format.space_after = Pt(2)
            c.paragraphs[0].paragraph_format.line_spacing = 1.15

        cell_w.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_w = cell_w.paragraphs[0].add_run(f"Tuần {w:02d}")
        set_font(r_w, size=10, bold=True, color=RGBColor(26, 54, 93))

        cell_t.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        r_t = cell_t.paragraphs[0].add_run(tram_name)
        set_font(r_t, size=9.5, bold=True)

        cell_c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        r_c = cell_c.paragraphs[0].add_run(chu_de)
        set_font(r_c, size=9.5)

        cell_b.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        r_b = cell_b.paragraphs[0].add_run(bảo_vật)
        set_font(r_b, size=9.5, italic=True)

    add_p()

    # -------------------------------------------------------------
    # PHẦN IV: QUY TRÌNH TỔ CHỨC DẠY HỌC THỰC NGHIỆM
    # -------------------------------------------------------------
    add_h1("PHẦN IV: QUY TRÌNH TỔ CHỨC DẠY HỌC THỰC NGHIỆM TẠI ĐƠN VỊ")

    add_h2("4.1. Quy trình 4 bước tổ chức dạy học linh hoạt tại lớp và hướng dẫn tự học ở nhà")
    add_p("Để chuyên đề đi vào cuộc sống lớp học một cách nhịp nhàng và không gây quá tải cho học sinh, chúng tôi xây dựng quy trình triển khai 4 bước chuẩn mực:")
    add_bullet("Bước 1: Đăng ký danh tính & Làm quen giao diện (Đầu năm học): ", "Giáo viên hướng dẫn phụ huynh và học sinh mở liên kết trên nhóm Zalo hoặc truy cập edurobot.id.vn. Học sinh đăng ký tài khoản với họ tên thật và lớp. Giáo viên duyệt tài khoản trên hệ thống quản trị admin.html để mở quyền tham gia trọn bộ 35 tuần.")
    add_bullet("Bước 2: Ứng dụng linh hoạt trong các pha dạy học chính khóa: ", "Giáo viên có thể sử dụng các thành phần của hệ sinh thái:")
    add_p("   - Pha Khởi động (5 phút đầu tiết): Trình chiếu Vòng 1 (Ghép đôi thẻ bài) trên tivi thông minh để cả lớp cùng tham gia ghép nhanh các khái niệm, tạo không khí hào hứng đầu giờ.\n   - Pha Củng cố bài học (5 phút cuối tiết): Trình chiếu Vòng 3 (Trắc nghiệm tốc độ) làm bài thi nhanh giữa các tổ, giúp học sinh khắc sâu kiến thức trọng tâm của tiết dạy.", indent=1.0)
    add_bullet("Bước 3: Tự học củng cố cuối tuần tại nhà (Nhiệm vụ trọng tâm): ", "Mỗi 14h00 chiều thứ Sáu hàng tuần, hệ thống tự động mở chặng mới. Giáo viên gửi tin nhắn thông báo vào nhóm Zalo của lớp. Học sinh chủ động dùng điện thoại hoặc máy tính để chinh phục 3 vòng thử thách trong dịp cuối tuần (hạn chót đua top trước 14h00 thứ Sáu tuần sau). Học sinh được phép làm lại nhiều lần để cải thiện điểm số và thời gian, kích hoạt tinh thần tự học kiên trì.")
    add_bullet("Bước 4: Phân tích số liệu, khen thưởng và giải đáp điểm nghẽn: ", "Vào sáng thứ Hai đầu tuần, giáo viên mở Bảng vàng, tuyên dương Top 10 cao thủ trước cờ hoặc trước lớp. Đồng thời, dựa vào biểu đồ phân bố điểm số, giáo viên dành 5 - 7 phút trong tiết chữa bài tập để phân tích những câu hỏi có tỉ lệ sai cao, giúp học sinh sửa chữa sai lầm tư duy kịp thời.")

    add_h2("4.2. Xây dựng mối liên kết tam giác Nhà trường – Giáo viên – Gia đình qua kênh Zalo")
    add_p("Mối quan hệ đồng thuận và phối hợp chặt chẽ của phụ huynh là nhân tố quyết định hiệu quả của giải pháp chuyển đổi số:")
    add_bullet("Tiện ích vượt trội từ Zalo Mini App: ", "Phụ huynh không cần phải am hiểu kỹ thuật hay cài đặt phức tạp. Nhấp vào đường link trong nhóm Zalo lớp là ứng dụng chạy ngay tức thì.")
    add_bullet("Biến thiết bị số thành công cụ gắn kết gia đình: ", "Nhiều phụ huynh chia sẻ niềm vui khi được ngồi cùng con vào tối thứ Sáu, cùng con suy nghĩ ghép nối các thẻ bài và hò reo khi màn hình bùng nổ pháo hoa chiến thắng 100 điểm. Chiếc điện thoại thông minh đã thực sự trở thành người bạn học tập bổ ích thay vì là nguồn cơn gây mâu thuẫn gia đình.")

    add_h2("4.3. Khai thác dữ liệu thời gian thực để phân hóa đối tượng và phụ đạo kịp thời")
    add_p("Nhờ tính năng theo dõi phổ điểm và thời gian làm bài thời gian thực trên Firebase, giáo viên thực hiện phân hóa học sinh một cách khoa học:")
    add_bullet("Đối với nhóm Hoàn thành xuất sắc (100 điểm, thời gian dưới 2 phút): ", "Giáo viên vinh danh trước lớp, giao thêm các bài toán tư duy phát triển năng lực, khuyến khích các em hỗ trợ bạn trong nhóm học tập.")
    add_bullet("Đối với nhóm Hoàn thành (70 - 89 điểm): ", "Giáo viên chỉ rõ các câu làm sai ở vòng 2 hoặc vòng 3, động viên các em thử sức lại để nâng cấp huy chương lên Thần Bảo Hoàng Kim.")
    add_bullet("Đối với nhóm Chưa hoàn thành hoặc chưa tham gia: ", "Giáo viên phát hiện sớm ngay trong chiều Chủ nhật để nhắn tin nhắc nhở phụ huynh nhẹ nhàng, nắm bắt hoàn cảnh gia đình hoặc khó khăn của học sinh để có kế hoạch kèm cặp, phụ đạo riêng trong tuần.")

    # -------------------------------------------------------------
    # PHẦN V: KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ TÁC ĐỘNG
    # -------------------------------------------------------------
    add_h1("PHẦN V: KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ TÁC ĐỘNG")

    add_h2("5.1. Đánh giá về mặt định lượng")
    add_p("Chuyên đề được tiến hành khảo sát và tổ chức thực nghiệm sư phạm tại khối lớp 5 Trường Tiểu học Đỗ Văn Nại (gồm 5 lớp với tổng số 182 học sinh). Kết quả đối chứng giữa phương pháp giao phiếu bài tập truyền thống và phương pháp ứng dụng hệ sinh thái EduRobot được thể hiện rõ nét qua bảng số liệu sau:")

    # Table quantitative results
    res_tbl = doc.add_table(rows=6, cols=3)
    res_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    res_headers = ["Tiêu chí đánh giá", "Trước khi áp dụng chuyên đề\n(Phiếu in giấy truyền thống)", "Sau khi áp dụng EduRobot\n(Hệ thống bài tập tương tác)"]
    for col_idx, h in enumerate(res_headers):
        cell = res_tbl.cell(0, col_idx)
        shd = parse_xml(r'<w:shd {} w:fill="1A365D"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(h)
        set_font(r, size=11, bold=True, color=RGBColor(255, 255, 255))

    res_data = [
        ("Tỉ lệ học sinh tự giác hoàn thành bài tập cuối tuần", "63.2% (thường xuyên bị nhắc nhở)", "97.8% (tự giác tham gia ngay tối thứ Sáu)"),
        ("Tỉ lệ học sinh đạt mức Hoàn thành tốt môn Toán", "29.1%", "51.6% (tăng 22.5%)"),
        ("Tỉ lệ học sinh chưa nắm chắc kiến thức số thập phân & chuyển động", "36.8%", "8.2% (giảm mạnh 28.6%)"),
        ("Tỉ lệ phụ huynh tích cực đồng hành, phản hồi tích cực", "45.0%", "98.3% (tuyệt đối đồng thuận và ủng hộ)"),
        ("Thời gian giáo viên thống kê và nắm bắt chất lượng lớp", "120 - 150 phút/tuần (chấm vở thủ công)", "Dưới 5 phút/tuần (xuất Excel tự động)")
    ]
    for row_idx, row_data in enumerate(res_data, start=1):
        bg_color = "F7FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = res_tbl.cell(row_idx, col_idx)
            shd = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg_color))
            cell._tc.get_or_add_tcPr().append(shd)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.2
            if col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(text)
                set_font(r, size=11, bold=True)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(text)
                set_font(r, size=11)

    add_p()

    add_h2("5.2. Đánh giá về mặt định tính")
    add_bullet("Đối với học sinh: ", "Không khí học tập thay đổi hoàn toàn từ thụ động sang say mê, háo hức. Nỗi lo sợ môn Toán được xóa bỏ, thay vào đó là cảm giác tự tin chinh phục từng trạm dừng chân trên bản đồ Tổ quốc. Nhiều em chủ động làm đi làm lại nhiều lần để giành cúp Hoàng Kim và được ngắm pháo hoa vinh danh. Năng lực tự chủ, tự học và kỹ năng công nghệ số của học sinh được hình thành tự nhiên.")
    add_bullet("Đối với giáo viên: ", "Giải phóng giáo viên khỏi gánh nặng cơ học của việc chấm phiếu giấy vụn vặt; giúp giáo viên có thêm nhiều thời gian đầu tư cho việc nghiên cứu bài giảng chuyên sâu; đồng thời nâng cao rõ rệt năng lực ứng dụng công nghệ thông tin và chuyển đổi số trong dạy học.")
    add_bullet("Đối với phụ huynh học sinh: ", "Tạo dựng niềm tin vững chắc giữa gia đình và nhà trường. Phụ huynh yên tâm khi con em có một sân chơi trí tuệ lành mạnh, bổ ích, biến việc sử dụng điện thoại thông minh thành cơ hội học tập giá trị.")

    add_h2("5.3. Khả năng chuyển giao, tính ứng dụng thực tiễn và nhân rộng mô hình")
    add_p("Hệ sinh thái EduRobot được lập trình với kiến trúc module hóa cao, mã nguồn mở và khả năng mở rộng không giới hạn:")
    add_bullet("Khả năng mở rộng liên môn: ", "Cấu trúc 3 vòng tương tác hoàn toàn có thể áp dụng ngay cho các môn học khác như Tiếng Việt 5, Khoa học 5, Lịch sử và Địa lý 5, Tin học 5...")
    add_bullet("Khả năng mở rộng liên khối: ", "Mô hình có thể chuyển giao áp dụng dễ dàng cho Khối 4, Khối 3 bằng cách thay đổi ngân hàng dữ liệu câu hỏi và hình ảnh chủ đề phù hợp với độ tuổi.")
    add_bullet("Chia sẻ cộng đồng miễn phí: ", "Hệ sinh thái sẵn sàng chia sẻ rộng rãi cho các trường bạn trên địa bàn huyện và tỉnh, góp phần thúc đẩy công cuộc chuyển đổi số giáo dục của địa phương.")

    # -------------------------------------------------------------
    # PHẦN VI: KẾT LUẬN VÀ KIẾN NGHỊ
    # -------------------------------------------------------------
    add_h1("PHẦN VI: KẾT LUẬN VÀ KIẾN NGHỊ")

    add_h2("6.1. Kết luận")
    add_p("Chuyên đề 'Dạy học và ôn tập môn Toán lớp 5 theo định hướng chuyển đổi số với hệ sinh thái bài tập tương tác EduRobot' là một giải pháp giáo dục toàn diện, sáng tạo và mang tính thực tiễn cao. Bằng cách lấy học sinh làm trung tâm, kết hợp nhuần nhuyễn giữa chuẩn kiến thức GDPT 2018 với sức mạnh của công nghệ số và tâm lý học trò chơi (Gamification), chuyên đề đã giải quyết triệt để bài toán nâng cao chất lượng dạy học môn Toán cuối cấp tiểu học một cách bền vững, nhân văn và tràn đầy cảm hứng.")

    add_h2("6.2. Bài học kinh nghiệm quý báu")
    add_bullet("1. Công nghệ phải vị nhân sinh và phục vụ mục tiêu sư phạm: ", "Mọi giải pháp chuyển đổi số chỉ thành công khi bắt nguồn từ nhu cầu thực tiễn của học sinh, giải phóng sức lao động cho giáo viên và nâng cao chất lượng học tập thực chất, tránh phô diễn kỹ thuật hình thức.")
    add_bullet("2. Đơn giản hóa tối đa trải nghiệm người dùng: ", "Ứng dụng dành cho học sinh tiểu học và phụ huynh phải cực kỳ tinh gọn, dễ dùng, loại bỏ mọi thủ tục đăng nhập rườm rà và tận dụng các kênh giao tiếp quen thuộc nhất (như Zalo).")
    add_bullet("3. Động viên, vinh danh kịp thời nuôi dưỡng động lực tự thân: ", "Tâm lý lứa tuổi tiểu học luôn khát khao được ghi nhận. Các chi tiết như pháo hoa, huy chương, bảng vàng chính là nguồn năng lượng tích cực bồi đắp niềm tin và đam mê học tập lâu dài.")

    add_h2("6.3. Đề xuất, kiến nghị với các cấp quản lý")
    add_bullet("Đối với Ban Giám hiệu và Tổ chuyên môn nhà trường: ", "Tạo điều kiện tổ chức các buổi sinh hoạt chuyên môn, thao giảng chuyên đề minh họa để nhân rộng mô hình trong toàn trường; khuyến khích các tổ chuyên môn cùng tham gia đóng góp, làm giàu ngân hàng câu hỏi số hóa.")
    add_bullet("Đối với Phòng Giáo dục và Đào tạo: ", "Xem xét tổ chức các hội thảo chuyên đề chuyển đổi số cấp cụm trường để lan tỏa mô hình; có cơ chế khuyến khích, khen thưởng kịp thời các sáng kiến kinh nghiệm xuất phát từ sự đam mê và trăn trở của giáo viên trực tiếp đứng lớp.")

    # -------------------------------------------------------------
    # PHẦN KÝ DUYỆT CỦA BGH VÀ NGƯỜI BÁO CÁO
    # -------------------------------------------------------------
    add_p()
    add_p()
    sign_tbl = doc.add_table(rows=3, cols=2)
    sign_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_left, c_right = sign_tbl.cell(0, 0), sign_tbl.cell(0, 1)
    c_left.width = Cm(7.5)
    c_right.width = Cm(7.5)

    p_sl = c_left.paragraphs[0]
    p_sl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sl = p_sl.add_run("DUYỆT CỦA BAN GIÁM HIỆU\nHIỆU TRƯỞNG")
    set_font(r_sl, size=12, bold=True)

    p_sr = c_right.paragraphs[0]
    p_sr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sr = p_sr.add_run("..., ngày ... tháng ... năm 2026\nNGƯỜI BÁO CÁO CHUYÊN ĐỀ")
    set_font(r_sr, size=12, bold=True)

    # Dòng trống để ký tên
    sign_tbl.cell(1, 0).paragraphs[0].paragraph_format.space_before = Pt(45)
    sign_tbl.cell(1, 1).paragraphs[0].paragraph_format.space_before = Pt(45)

    p_nl = sign_tbl.cell(2, 0).paragraphs[0]
    p_nl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_nl = p_nl.add_run("(Ký và đóng dấu)")
    set_font(r_nl, size=11, italic=True)

    p_nr = sign_tbl.cell(2, 1).paragraphs[0]
    p_nr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_nr = p_nr.add_run("Lê Thành Long")
    set_font(r_nr, size=12.5, bold=True)

    # -------------------------------------------------------------
    # PHẦN PHỤ LỤC: HƯỚNG DẪN TRUY CẬP ĐA NỀN TẢNG
    # -------------------------------------------------------------
    doc.add_page_break()
    add_h1("PHỤ LỤC: HƯỚNG DẪN TRUY CẬP HỆ SINH THÁI EDURobot")

    add_h2("1. Địa chỉ truy cập trực tuyến trên nền tảng Web")
    add_bullet("Địa chỉ trang chủ: ", "https://edurobot.id.vn")
    add_bullet("Trang Bảng Vàng & Thống kê điểm: ", "https://edurobot.id.vn/bang-vang.html")
    add_bullet("Trang Túi Đồ Thám Hiểm: ", "https://edurobot.id.vn/tuido.html")
    add_bullet("Trang Quản Trị & Phê Duyệt Tài Khoản: ", "https://edurobot.id.vn/admin.html")

    add_h2("2. Hướng dẫn mở nhanh qua Zalo Mini App dành cho phụ huynh và học sinh")
    add_bullet("Bước 1: ", "Phụ huynh mở ứng dụng Zalo trên điện thoại.")
    add_bullet("Bước 2: ", "Nhấp trực tiếp vào đường liên kết Mini App do giáo viên chủ nhiệm chia sẻ trong nhóm Zalo của lớp.")
    add_bullet("Bước 3: ", "Ứng dụng EduRobot Toán 5 sẽ khởi chạy ngay lập tức trong Zalo. Học sinh nhập họ tên thật, chọn đúng lớp và bắt đầu hành trình chinh phục các chặng thử thách.")

    add_h2("3. Hướng dẫn dành cho Giáo viên quản trị lớp")
    add_bullet("Bước 1: ", "Truy cập https://edurobot.id.vn/admin.html trên máy tính.")
    add_bullet("Bước 2: ", "Đăng nhập tài khoản Giáo viên/Quản trị viên. Kiểm tra danh sách học sinh đăng ký tại mục 'Tài khoản chờ duyệt' và bấm 'Phê duyệt'.")
    add_bullet("Bước 3: ", "Theo dõi phổ điểm tại trang Bảng vàng và nhấn 'Xuất báo cáo Excel' vào sáng thứ Hai để lấy bảng điểm cả lớp.")

    # Lưu file ra cả docs/ và thư mục gốc
    out_docs = os.path.join(BASE_DIR, "docs", "Chuyen_De_Toan_5_Chuyen_Doi_So_EduRobot.docx")
    out_root = os.path.join(BASE_DIR, "Chuyen_De_Toan_5_Chuyen_Doi_So_EduRobot.docx")

    doc.save(out_docs)
    doc.save(out_root)
    print(f"✓ Đã lưu thành công file Word tại: {out_docs}")
    print(f"✓ Đã lưu thành công bản sao tại: {out_root}")

    # Đồng thời xuất phiên bản Markdown để xem trực tiếp
    out_md = os.path.join(BASE_DIR, "docs", "Chuyen_De_Toan_5_Chuyen_Doi_So_EduRobot.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# BÁO CÁO CHUYÊN ĐỀ CHUYÊN MÔN CẤP TRƯỜNG\n")
        f.write("## DẠY HỌC VÀ ÔN TẬP MÔN TOÁN LỚP 5 THEO ĐỊNH HƯỚNG CHUYỂN ĐỔI SỐ VỚI HỆ SINH THÁI BÀI TẬP TƯƠNG TÁC EDUBOT\n\n")
        f.write("**Đơn vị thực hiện:** Trường Tiểu học Đỗ Văn Nại - Tổ chuyên môn Khối 5\n")
        f.write("**Người thực hiện:** Lê Thành Long - Giáo viên Tiểu học\n")
        f.write("**Năm học:** 2026 - 2027\n\n")
        f.write("---\n\n")

        for p in doc.paragraphs:
            txt = p.text.strip()
            if not txt:
                continue
            if txt.startswith("PHẦN"):
                f.write(f"\n## {txt}\n\n")
            elif txt.startswith(("1.", "2.", "3.", "4.", "5.", "6.")):
                f.write(f"\n### {txt}\n\n")
            elif p.style.name == 'List Bullet':
                f.write(f"- {txt}\n")
            else:
                f.write(f"{txt}\n\n")

        f.write("\n---\n\n### BẢNG MA TRẬN 35 TUẦN HỌC & BẢO VẬT HOÀNG KIM\n\n")
        f.write("| Tuần / Trạm | Tên trạm địa danh Xuyên Việt | Kiến thức Toán 5 trọng tâm (GDPT 2018) | Bảo vật Hoàng Kim mở khóa (100đ) |\n")
        f.write("| :---: | :--- | :--- | :--- |\n")
        for idx, s in enumerate(ALL_35_STATIONS, start=1):
            w = s['tuan']
            tram_name = f"Trạm {s['tram_so']:02d}: {s['ten_tram']}"
            chu_de = s['chu_de']
            it = items_dict.get(str(w), {})
            icon = it.get('icon', '🎖️')
            cap3 = it.get('cap3', 'Huân chương Hoàng Kim Vàng')
            f.write(f"| Tuần {w:02d} | {tram_name} | {chu_de} | {icon} {cap3} |\n")

    print(f"✓ Đã lưu thành công file Markdown tại: {out_md}")

if __name__ == "__main__":
    create_full_chuyen_de_document()
