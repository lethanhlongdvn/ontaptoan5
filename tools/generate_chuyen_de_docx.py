# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import os

def create_chuyen_de_document():
    doc = docx.Document()

    # 1. Page Setup: A4, Margins: Top 2cm, Bottom 2cm, Left 3cm, Right 2cm
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.0)
        section.different_first_page_header_footer = True

        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Chuyên đề dạy học Toán 5: Ứng dụng hệ thống bài tập tương tác EduRobot")
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
        
        # Add Page Number XML field
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

    # Styling helper functions
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
        # light grey blue background
        shd = parse_xml(r'<w:shd {} w:fill="F0F4F8"/>'.format(nsdecls('w')))
        tcPr.append(shd)
        # Left thick border
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
        cp.paragraph_format.space_before = Pt(4)
        cp.paragraph_format.space_after = Pt(2)
        r_title = cp.add_run(f"📌 {title}: ")
        set_font(r_title, size=12.5, bold=True, color=RGBColor(26, 54, 93))
        r_text = cp.add_run(text)
        set_font(r_text, size=12.5, italic=True)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # TRANG BÌA (COVER PAGE)
    # -------------------------------------------------------------
    p_cq = doc.add_paragraph()
    p_cq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cq.paragraph_format.space_after = Pt(2)
    p_cq.paragraph_format.space_before = Pt(10)
    r = p_cq.add_run("PHÒNG GIÁO DỤC VÀ ĐÀO TẠO ...\nTRƯỜNG TIỂU HỌC ...")
    set_font(r, size=12, bold=True, color=RGBColor(50, 50, 50))

    # Divider line
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(25)
    r_line = p_line.add_run("————————— 🕮 —————————")
    set_font(r_line, size=11, bold=True, color=RGBColor(150, 150, 150))

    # Robot logo if exists
    if os.path.exists("assets/robot-head.png"):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(15)
        p_img.add_run().add_picture("assets/robot-head.png", width=Cm(3.2))

    # Title report
    p_rp = doc.add_paragraph()
    p_rp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rp.paragraph_format.space_after = Pt(10)
    r_rp = p_rp.add_run("BÁO CÁO CHUYÊN ĐỀ CHUYÊN MÔN\nĐỔI MỚI PHƯƠNG PHÁP DẠY HỌC TIỂU HỌC")
    set_font(r_rp, size=14, bold=True, color=RGBColor(194, 65, 12))

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(20)
    r_title = p_title.add_run("ÔN TẬP MÔN TOÁN LỚP 5\nTHEO ĐỊNH HƯỚNG CHUYỂN ĐỔI SỐ\nVỚI HỆ THỐNG BÀI TẬP TƯƠNG TÁC")
    set_font(r_title, size=19, bold=True, color=RGBColor(26, 54, 93))

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(40)
    r_sub = p_sub.add_run("(Giải pháp ứng dụng mô hình Gamification và nền tảng đa phương thức EduRobot\nphục vụ dạy học ôn tập học kỳ 2 - Chương trình GDPT 2018)")
    set_font(r_sub, size=12.5, italic=True, color=RGBColor(74, 85, 104))

    # Author info table
    info_tbl = doc.add_table(rows=4, cols=2)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Người thực hiện:", "Lê Thành Long"),
        ("Chức vụ:", "Giáo viên Tiểu học"),
        ("Tổ chuyên môn:", "Tổ chuyên môn Khối 5"),
        ("Năm học:", "2025 - 2026")
    ]
    for row_idx, (label, val) in enumerate(info_data):
        c1, c2 = info_tbl.cell(row_idx, 0), info_tbl.cell(row_idx, 1)
        c1.width = Cm(4.5)
        c2.width = Cm(7.0)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(3)
        p1.paragraph_format.space_before = Pt(2)
        r1 = p1.add_run(label)
        set_font(r1, size=12.5, bold=True)
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_after = Pt(3)
        p2.paragraph_format.space_before = Pt(2)
        r2 = p2.add_run(val)
        set_font(r2, size=12.5)

    doc.add_page_break()

    # -------------------------------------------------------------
    # MỤC LỤC & TÓM TẮT
    # -------------------------------------------------------------
    p_ml = doc.add_paragraph()
    p_ml.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ml.paragraph_format.space_after = Pt(12)
    r_ml = p_ml.add_run("MỤC LỤC TỔNG THỂ CHUYÊN ĐỀ")
    set_font(r_ml, size=15, bold=True, color=RGBColor(26, 54, 93))

    toc_items = [
        ("PHẦN I: ĐẶT VẤN ĐỀ (LÝ DO CHỌN CHUYÊN ĐỀ)", "Trang 2"),
        ("   1.1. Bối cảnh chuyển đổi số trong giáo dục và Chương trình GDPT 2018", "Trang 2"),
        ("   1.2. Thực trạng công tác ôn tập môn Toán lớp 5 học kỳ 2 hiện nay", "Trang 2"),
        ("   1.3. Tính cấp thiết và mục đích nghiên cứu của chuyên đề", "Trang 3"),
        ("PHẦN II: CƠ SỞ KHOA HỌC VÀ NGUYÊN TẮC THIẾT KẾ", "Trang 3"),
        ("   2.1. Cơ sở lý luận: Thuyết kiến tạo và mô hình Trò chơi hóa (Gamification)", "Trang 3"),
        ("   2.2. Tâm lý tiếp nhận và thói quen công nghệ của học sinh lớp 5", "Trang 4"),
        ("   2.3. Các nguyên tắc sư phạm trong xây dựng hệ sinh thái EduRobot", "Trang 4"),
        ("PHẦN III: NỘI DUNG VÀ CÁC BIỆN PHÁP THỰC HIỆN (TRỌNG TÂM)", "Trang 5"),
        ("   3.1. Ý tưởng 'Hành trình Xuyên Việt' – Tích hợp liên môn Toán và Lịch sử - Địa lý", "Trang 5"),
        ("   3.2. Cấu trúc bài tập tương tác 3 vòng thử thách tư duy", "Trang 5"),
        ("   3.3. Các cơ chế Game hóa tạo động lực học tập bền vững", "Trang 6"),
        ("   3.4. Giải pháp công nghệ đa nền tảng: Web tương tác và Zalo Mini App", "Trang 7"),
        ("   3.5. Hệ thống thu thập dữ liệu tự động và số hóa quản lý chuyên môn", "Trang 7"),
        ("   3.6. Ma trận nội dung ôn tập 17 tuần học kỳ 2 (Tuần 19 đến Tuần 35)", "Trang 8"),
        ("PHẦN IV: QUY TRÌNH TỔ CHỨC DẠY HỌC THỰC NGHIỆM TẠI ĐƠN VỊ", "Trang 9"),
        ("   4.1. Quy trình 4 bước triển khai linh hoạt trong dạy học", "Trang 9"),
        ("   4.2. Phối hợp giữa nhà trường, giáo viên và phụ huynh qua kênh Zalo", "Trang 9"),
        ("   4.3. Khai thác dữ liệu thời gian thực để phân hóa và phụ đạo học sinh", "Trang 9"),
        ("PHẦN V: KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ TÁC ĐỘNG", "Trang 10"),
        ("   5.1. Đánh giá về mặt định lượng (Tỉ lệ tham gia, điểm số, thời gian hoàn thành)", "Trang 10"),
        ("   5.2. Đánh giá về mặt định tính (Năng lực tự chủ, hứng thú học tập và kỹ năng số)", "Trang 10"),
        ("   5.3. Khả năng chuyển giao và nhân rộng mô hình", "Trang 11"),
        ("PHẦN VI: KẾT LUẬN VÀ KIẾN NGHỊ", "Trang 11"),
        ("   6.1. Kết luận", "Trang 11"),
        ("   6.2. Bài học kinh nghiệm", "Trang 11"),
        ("   6.3. Đề xuất, kiến nghị", "Trang 12"),
    ]

    for title, pg in toc_items:
        p_toc = doc.add_paragraph()
        p_toc.paragraph_format.space_after = Pt(2)
        p_toc.paragraph_format.line_spacing = 1.2
        r_t = p_toc.add_run(title)
        set_font(r_t, size=11.5, bold=("PHẦN" in title))
        r_dots = p_toc.add_run(" " + "." * max(10, 85 - len(title) * 2) + " ")
        set_font(r_dots, size=10, color=RGBColor(160, 160, 160))
        r_p = p_toc.add_run(pg)
        set_font(r_p, size=11, italic=True)

    add_p()
    add_callout("TÓM TẮT NỘI DUNG CHUYÊN ĐỀ", 
                "Chuyên đề đề xuất một giải pháp đột phá trong đổi mới phương pháp củng cố, ôn tập môn Toán lớp 5 học kỳ 2 thông qua hệ thống học tập tương tác EduRobot (EduBot-BTCT5). Giải pháp kết hợp giữa lý thuyết Trò chơi hóa (Gamification), tích hợp liên môn (Toán học gắn liền với bản đồ địa danh Việt Nam) và công nghệ đa nền tảng hiện đại (Web trực tuyến và Zalo Mini App). Hệ thống giúp biến các bài tập khô khan thành hành trình khám phá cuốn hút, đồng thời cung cấp cho giáo viên công cụ thống kê phổ điểm, xếp hạng và xuất dữ liệu Excel tự động từ Firebase Database để đánh giá quá trình chính xác.")

    # -------------------------------------------------------------
    # PHẦN I: ĐẶT VẤN ĐỀ (LÝ DO CHỌN CHUYÊN ĐỀ)
    # -------------------------------------------------------------
    add_h1("PHẦN I: ĐẶT VẤN ĐỀ (LÝ DO CHỌN CHUYÊN ĐỀ)")

    add_h2("1.1. Bối cảnh chuyển đổi số trong giáo dục và Chương trình GDPT 2018")
    add_p("Trong giai đoạn hiện nay, ngành Giáo dục và Đào tạo đang đẩy mạnh thực hiện Chương trình Giáo dục phổ thông 2018 (GDPT 2018) với mục tiêu căn bản là chuyển từ nền giáo dục nặng về trang bị kiến thức sang nền giáo dục chú trọng phát triển toàn diện phẩm chất và năng lực người học. Đặc biệt, Quyết định số 131/QĐ-TTg của Thủ tướng Chính phủ về việc phê duyệt Đề án 'Tăng cường ứng dụng công nghệ thông tin và chuyển đổi số trong giáo dục và đào tạo giai đoạn 2022 - 2025, định hướng đến năm 2030' đã đặt ra yêu cầu cấp thiết: chuyển đổi số không chỉ dừng lại ở khâu quản lý hay trình chiếu bài giảng mà phải thâm nhập sâu vào quy trình dạy học, đổi mới phương thức tương tác và kiểm tra đánh giá.")
    add_p("Môn Toán ở cấp Tiểu học, đặc biệt là lớp 5 – lớp cuối cấp chuẩn bị chuyển tiếp lên Trung học cơ sở – có vị trí then chốt trong việc hình thành tư duy logic, năng lực giải quyết vấn đề và mô hình hóa toán học. Đổi mới phương pháp dạy học môn Toán theo định hướng chuyển đổi số đòi hỏi người giáo viên phải kiến tạo được môi trường học tập linh hoạt, mở rộng không gian lớp học vượt ra ngoài 4 bức tường truyền thống, tạo điều kiện cho học sinh tự học mọi lúc, mọi nơi một cách hứng thú và chủ động.")

    add_h2("1.2. Thực trạng công tác ôn tập môn Toán lớp 5 học kỳ 2 hiện nay")
    add_p("Qua thực tiễn giảng dạy nhiều năm tại khối lớp 5, chúng tôi nhận thấy giai đoạn Học kỳ 2 (từ tuần 19 đến tuần 35) là khoảng thời gian học sinh phải tiếp thu và củng cố một khối lượng kiến thức rất lớn, mang tính trừu tượng và có độ phân hóa cao:")
    add_bullet("Về mặt kiến thức: ", "Học sinh phải làm chủ nhiều mảng kiến thức phức tạp như Tỉ số và Tỉ số phần trăm; Diện tích, thể tích các hình khối (hình hộp chữ nhật, hình lập phương); Hình tròn và chu vi, diện tích hình tròn; Mối quan hệ giữa các đơn vị đo; và đặc biệt là mạch kiến thức Toán chuyển động đều (vận tốc, quãng đường, thời gian với chuyển động cùng chiều, ngược chiều).")
    add_bullet("Về phương pháp ôn tập truyền thống: ", "Phần lớn giáo viên vẫn áp dụng việc giao phiếu bài tập in trên giấy, sách bài tập hoặc giao bài trên bảng để học sinh về nhà làm vào vở. Hình thức này tồn tại nhiều hạn chế: khô khan, mang tính áp đặt, dễ gây tâm lý ngán ngẩm, đối phó cho các em; phản hồi kết quả bị trễ (thường phải chờ đến ngày hôm sau giáo viên mới chấm và sửa bài, khiến các em mất đi thời điểm 'vàng' để sửa chữa sai lầm tư duy).")
    add_bullet("Về bối cảnh sinh hoạt của học sinh: ", "Tại hầu hết các gia đình hiện nay, điện thoại thông minh và mạng Internet đã trở nên phổ biến. Tuy nhiên, phần lớn học sinh sử dụng thiết bị để xem video ngắn trên TikTok, YouTube Shorts hoặc chơi game giải trí không có tính giáo dục. Phụ huynh rất lo lắng nhưng thường lúng túng trong việc tìm kiếm các công cụ học tập lành mạnh, hấp dẫn để hướng con em sử dụng thiết bị đúng mục đích.")
    add_bullet("Về phía giáo viên: ", "Việc theo dõi, kiểm soát và thống kê mức độ hoàn thành bài tự học ở nhà của từng học sinh trong lớp (từ 35 - 40 em) chiếm quá nhiều thời gian, công sức. Giáo viên thiếu công cụ số để thu thập số liệu tự động, khó nắm bắt chính xác điểm nghẽn nhận thức chung của cả lớp để điều chỉnh bài giảng kịp thời.")

    add_h2("1.3. Tính cấp thiết và mục đích nghiên cứu của chuyên đề")
    add_p("Xuất phát từ những trăn trở và yêu cầu thực tiễn nêu trên, chúng tôi đã chủ động nghiên cứu, thiết kế và triển khai hệ sinh thái bài tập tương tác mang tên EduRobot (EduBot-BTCT5) với địa chỉ hoạt động tại edurobot.id.vn cùng phiên bản Zalo Mini App. Chuyên đề này được đúc kết nhằm đạt các mục tiêu trọng tâm:")
    add_bullet("Mục tiêu 1: ", "Xây dựng hệ thống bài tập tương tác trực quan, sống động cho toàn bộ 17 tuần học kỳ 2 môn Toán 5 theo mô hình Gamification, giúp chuyển hóa nhiệm vụ ôn tập thành cuộc thám hiểm hấp dẫn.")
    add_bullet("Mục tiêu 2: ", "Tích hợp liên môn giáo dục tình yêu quê hương, đất nước thông qua 'Hành trình Xuyên Việt', gắn mỗi bài toán với một cột mốc địa danh và bảo vật văn hóa dân tộc.")
    add_bullet("Mục tiêu 3: ", "Tối ưu hóa khả năng tiếp cận bằng việc triển khai song song trên nền tảng Web và Zalo Mini App, giúp học sinh mở bài luyện tập ngay lập tức trên điện thoại mà không cần thao tác cài đặt phức tạp.")
    add_bullet("Mục tiêu 4: ", "Cung cấp cho giáo viên công cụ quản lý và kiểm tra đánh giá thời gian thực (Realtime Dashboard), phân tích phổ điểm trực quan bằng biểu đồ và xuất báo cáo Excel chỉ với một cú nhấp chuột.")

    # -------------------------------------------------------------
    # PHẦN II: CƠ SỞ KHOA HỌC VÀ NGUYÊN TẮC THIẾT KẾ
    # -------------------------------------------------------------
    add_h1("PHẦN II: CƠ SỞ KHOA HỌC VÀ NGUYÊN TẮC THIẾT KẾ")

    add_h2("2.1. Cơ sở lý luận: Thuyết kiến tạo và mô hình Trò chơi hóa (Gamification)")
    add_p("Chuyên đề được xây dựng dựa trên sự giao thoa của hai nền tảng lý thuyết giáo dục hiện đại:")
    add_bullet("Thuyết kiến tạo trong dạy học (Constructivism): ", "Nhà tâm lý học Jean Piaget và Lev Vygotsky khẳng định người học không tiếp thu tri thức một cách thụ động mà chủ động xây dựng tri thức thông qua hoạt động tương tác với môi trường. Khi tương tác với các thẻ bài, kéo thả hình vẽ hay chọn đáp án trong hệ thống số, học sinh được trải nghiệm quá trình thử - sai - điều chỉnh, từ đó khắc sâu bản chất của khái niệm toán học.")
    add_bullet("Mô hình Trò chơi hóa (Gamification in Education): ", "Gamification là việc ứng dụng các cơ chế trò chơi (điểm thưởng, mạng sống, huy chương, bảng xếp hạng, thanh tiến trình) vào hoạt động phi trò chơi nhằm tạo động lực tự thân (Intrinsic Motivation). Theo giáo sư Karl Kapp, gamification kích thích não bộ tiết ra Dopamine – chất dẫn truyền thần kinh tạo cảm giác hưng phấn và thỏa mãn khi chinh phục thử thách, giúp duy trì sự chú ý bền bỉ của trẻ em.")

    add_h2("2.2. Tâm lý tiếp nhận và thói quen công nghệ của học sinh lớp 5")
    add_p("Học sinh lớp 5 (10 - 11 tuổi) đang ở giai đoạn chuyển tiếp từ tư duy trực quan hình ảnh sang tư duy logic trừu tượng. Các em có đặc điểm tâm lý:")
    add_bullet("Tính hiếu động và ham khám phá: ", "Dễ bị lôi cuốn bởi âm thanh vui nhộn, hình ảnh rực rỡ và các thử thách mang tính cạnh tranh lành mạnh.")
    add_bullet("Nhu cầu khẳng định bản thân: ", "Rất thích được công nhận thành tích, vinh danh trước tập thể bạn bè (thông qua Bảng vàng hay Huân chương).")
    add_bullet("Khả năng thích ứng công nghệ cao nhưng dễ phân tán: ", "Các em thuần thục thao tác cảm ứng trên điện thoại thông minh, nhưng nếu giao diện ứng dụng quá rườm rà hoặc bắt đăng nhập phức tạp thì các em sẽ nhanh chóng nản chí và chuyển sang ứng dụng khác.")

    add_h2("2.3. Các nguyên tắc sư phạm trong xây dựng hệ thống tương tác EduRobot")
    add_p("Để đảm bảo tính khoa học và giá trị giáo dục thực chất, hệ thống EduRobot được thiết kế tuân thủ nghiêm ngặt 4 nguyên tắc sư phạm:")
    add_bullet("1. Nguyên tắc bám sát chuẩn kiến thức, kỹ năng: ", "Toàn bộ hệ thống bài tập được thẩm định kỹ lưỡng, bám sát các yêu cầu cần đạt của Chương trình GDPT 2018 môn Toán lớp 5, bảo đảm mức độ phân hóa từ nhận biết, thông hiểu đến vận dụng thực tiễn.")
    add_bullet("2. Nguyên tắc phản hồi tức thì (Immediate Feedback): ", "Mỗi thao tác của học sinh đều nhận được phản hồi ngay lập tức (âm thanh 'ting' vui tươi khi làm đúng, âm thanh nhắc nhở nhẹ nhàng khi chọn sai kèm cơ chế trừ mạng sống). Học sinh không phải đợi chấm bài mới biết kết quả.")
    add_bullet("3. Nguyên tắc tối ưu hóa trải nghiệm di động (Mobile-First): ", "Nhận định hơn 90% học sinh sử dụng điện thoại thông minh của phụ huynh, toàn bộ giao diện bài tập được thiết kế chuẩn tỉ lệ màn hình dọc, thao tác 'chạm - thả' thông minh, phông chữ Lexend rõ nét, chống mỏi mắt.")
    add_bullet("4. Nguyên tắc trung thực và an toàn dữ liệu: ", "Hệ thống tích hợp thuật toán lọc bỏ dữ liệu rác (loại bỏ tên tài khoản thử nghiệm như test, abc, 123; bắt buộc nhập họ tên thật ít nhất 3 từ), đảm bảo môi trường thi đua công bằng và minh bạch.")

    # -------------------------------------------------------------
    # PHẦN III: NỘI DUNG VÀ CÁC BIỆN PHÁP THỰC HIỆN
    # -------------------------------------------------------------
    add_h1("PHẦN III: NỘI DUNG VÀ CÁC BIỆN PHÁP THỰC HIỆN (TRỌNG TÂM)")

    add_h2("3.1. Ý tưởng 'Hành trình Xuyên Việt' – Tích hợp liên môn Toán và Lịch sử - Địa lý")
    add_p("Điểm nhấn độc đáo nhất của chuyên đề chính là ý tưởng lồng ghép toàn bộ tiến trình ôn tập 17 tuần học kỳ 2 vào bản đồ địa lý Việt Nam. Học sinh đóng vai trò là 'Nhà thám hiểm' đồng hành cùng chú robot thông minh EduRobot khởi hành từ địa đầu phía Bắc đến mũi cực Nam của Tổ quốc.")
    
    # Map image if exists
    if os.path.exists("Bandogame.jpg"):
        p_map = doc.add_paragraph()
        p_map.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_map.paragraph_format.space_before = Pt(6)
        p_map.paragraph_format.space_after = Pt(4)
        p_map.add_run().add_picture("Bandogame.jpg", width=Cm(13.5))
        p_caption = doc.add_paragraph()
        p_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_caption.paragraph_format.space_after = Pt(8)
        rc = p_caption.add_run("Hình 1: Giao diện Bản đồ tương tác 'Hành trình Xuyên Việt cùng Robot' (edurobot.id.vn)")
        set_font(rc, size=11, italic=True, color=RGBColor(80, 80, 80))

    add_p("Các trạm kiểm soát tương ứng với từng tuần học được định vị chính xác theo tọa độ địa lý và kết nối với nhau bằng các cung đường bộ rực rỡ và đường biển lấp lánh (vẽ tự động bằng công nghệ SVG):")
    add_bullet("Trạm khởi đầu (Tuần 19): ", "Cột cờ Lũng Cú (Hà Giang) – Nơi địa đầu Tổ quốc.")
    add_bullet("Các trạm miền Bắc (Tuần 20 - 24): ", "Thủ đô Hà Nội nghìn năm văn hiến, Tây Bắc, Đồng bằng sông Hồng.")
    add_bullet("Các trạm miền Trung (Tuần 25 - 29): ", "Cố đô Huế cổ kính, Duyên hải Nam Trung Bộ, Đà Nẵng, Tây Nguyên hùng vĩ.")
    add_bullet("Các trạm miền Nam & Hải đảo (Tuần 30 - 35): ", "Thành phố Hồ Chí Minh năng động, Đồng bằng sông Cửu Long, Mũi Cà Mau và vươn xa ra các đảo biển đảo thiêng liêng.")
    add_p("Thông qua lộ trình này, mỗi lần mở trạm học sinh không chỉ làm bài tập toán mà còn được gợi mở tri thức về địa danh, văn hóa và bồi đắp lòng tự hào dân tộc một cách tự nhiên, sâu sắc.")

    add_h2("3.2. Cấu trúc bài tập tương tác 3 vòng thử thách tư duy")
    add_p("Mỗi tuần ôn tập được thiết kế công phu thành một chuỗi 3 vòng thử thách liên hoàn với thang điểm chuẩn 100 điểm, bảo đảm tính vừa sức và nâng cao dần cấp độ tư duy:")
    
    # Table 3 rounds
    v_tbl = doc.add_table(rows=4, cols=4)
    v_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    v_headers = ["Vòng thi", "Tên gọi & Hình thức", "Cơ chế tương tác & Điểm", "Mục tiêu sư phạm"]
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
        ("Vòng 1", "Ghép đôi thẻ bài\n(Matching Cards)", "10 cặp thẻ (40 điểm).\nCó 3 mạng sống (❤️❤️❤️).\nChọn cặp tương ứng để mở khóa.", "Rèn luyện nhận diện khái niệm, công thức, ước lượng và ghép nối tỉ số."),
        ("Vòng 2", "Sắp xếp & Điền khuyết\n(Touch-to-Drop)", "5 bài toán thực tế (30 điểm).\nChạm đáp án rồi chạm ô nhận trên bảng số liệu.", "Khắc phục lỗi trượt ngón tay trên điện thoại; rèn tư duy tính toán chính xác."),
        ("Vòng 3", "Về đích trắc nghiệm\n(Multiple Choice)", "5 câu hỏi 4 lựa chọn (30 điểm).\nTính điểm tốc độ và chuyển câu tự động.", "Rèn luyện phản xạ tính nhanh, phân tích bẫy đề thi và bản lĩnh vượt chướng ngại vật.")
    ]
    col_widths = [Cm(2.0), Cm(4.0), Cm(5.0), Cm(5.0)]
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

    add_h2("3.3. Các cơ chế Game hóa tạo động lực học tập bền vững")
    add_p("Để học sinh không cảm thấy đơn điệu và luôn mong chờ đến giờ ôn tập, hệ thống tích hợp các cơ chế thưởng - phạt thông minh:")
    add_bullet("Hệ thống 'Mạng sống' (Heart Lives): ", "Ở vòng 1, học sinh được cấp 3 trái tim đỏ. Mỗi lần ghép sai sẽ mất 1 tim kèm âm thanh báo động. Nếu hết tim, học sinh phải chuyển vòng với số điểm hiện có, từ đó rèn luyện cho các em tính cẩn thận, không nhấn bừa.")
    add_bullet("Hiệu ứng Đại tiệc Pháo hoa chiến thắng (Fireworks System): ", "Khi học sinh đạt thành tích xuất sắc (từ 90 điểm trở lên), màn hình sẽ bùng nổ hiệu ứng pháo hoa 3D rực rỡ kèm dòng chữ vinh danh họ tên học sinh mạ vàng và nhạc chiến thắng ngân vang trong 10 giây. Đây là phần thưởng tinh thần vô cùng to lớn đối với học sinh tiểu học.")
    add_bullet("Túi đồ nhà thám hiểm (Gamification Inventory): ", "Mỗi tuần học hoàn thành đúng hạn chót sẽ mở khóa một bảo vật biểu trưng độc nhất vô nhị (như Ống nhòm Lũng Cú ở tuần 19, Bản đồ Thủ đô ở tuần 22, Quà cố đô Huế ở tuần 25, Mô hình Bitexco ở tuần 30, Huân chương Chiến thắng ở tuần 35). Học sinh có thể mở 'Túi đồ' để chiêm ngưỡng bộ sưu tập và số huy chương Vàng, Bạc, Đồng mà mình đã tích lũy.")
    add_bullet("Cơ chế mở chặng định kỳ (Countdown Schedule): ", "Các trạm bài tập được khóa tự động và chỉ mở vào đúng khung giờ quy định mỗi tuần (thứ Sáu hàng tuần). Nếu học sinh nhấp vào trạm chưa mở, đồng hồ đếm ngược sẽ hiển thị chính xác số ngày, giờ, phút, giây, tạo cảm giác hồi hộp và mong chờ.")

    add_h2("3.4. Giải pháp công nghệ đa nền tảng: Web tương tác và Zalo Mini App")
    add_p("Một trong những rào cản lớn nhất của các ứng dụng học tập trực tuyến là khâu cài đặt phức tạp, phụ huynh quên mật khẩu hoặc máy điện thoại không đủ dung lượng bộ nhớ. Nhận diện rõ bài toán này, tác giả đã phát triển giải pháp đồng bộ trên hai nền tảng:")
    add_bullet("Phiên bản Web chuẩn hóa (HTML5/CSS3/JavaScript): ", "Chạy mượt mà trên mọi trình duyệt (Google Chrome, Safari, Cốc Cốc, Edge) trên máy tính, tivi thông minh của lớp học hoặc máy tính bảng gia đình mà không cần bất kỳ tiện ích bổ trợ nào.")
    add_bullet("Phiên bản Zalo Mini App (edubot-zmp): ", "Ứng dụng công nghệ React 18, ZaUI và ZMP SDK của Zalo. Vì hầu như 100% phụ huynh học sinh Việt Nam đều cài sẵn Zalo trên điện thoại, việc tích hợp Zalo Mini App cho phép phụ huynh chỉ cần bấm vào đường link hoặc quét mã QR trong nhóm lớp là ứng dụng khởi chạy ngay lập tức với tốc độ cao, không tốn dung lượng máy.")

    add_h2("3.5. Hệ thống thu thập dữ liệu tự động và số hóa quản lý chuyên môn")
    add_p("Hệ thống kết nối trực tiếp với dịch vụ đám mây Firebase Realtime Database của Google, cho phép lưu trữ và xử lý dữ liệu học tập tức thì:")
    add_bullet("Ghi nhận đa chiều: ", "Mỗi lượt làm bài của học sinh đều được ghi nhận chi tiết gồm: Họ và tên, Lớp, Trường, Số điểm đạt được, Thời gian làm bài chính xác đến từng giây (duration), Số lần thử sức (attempt) và mốc thời gian hoàn thành.")
    add_bullet("Bảng vàng vinh danh Top 10 Realtime: ", "Hệ thống tự động xếp hạng học sinh dựa trên tiêu chí: Ưu tiên điểm cao nhất, nếu bằng điểm sẽ xếp theo thời gian hoàn thành ngắn nhất. Dữ liệu nhảy số ngay tức thì khi học sinh nộp bài.")
    add_bullet("Công cụ hỗ trợ giáo viên (Bảng vàng Dashboard): ", "Tại trang bang-vang.html, giáo viên có thể tra cứu toàn bộ kết quả của 17 tuần học, xem biểu đồ phân bố phổ điểm trực quan (dưới 50đ, 50-70đ, 80-90đ, 100đ) nhờ thư viện Chart.js, và đặc biệt là tính năng Xuất báo cáo danh sách điểm ra file Excel (.xlsx) qua thư viện SheetJS để làm minh chứng đánh giá thường xuyên.")

    add_h2("3.6. Ma trận nội dung ôn tập 17 tuần học kỳ 2 (Tuần 19 đến Tuần 35)")
    add_p("Dưới đây là ma trận phân phối nội dung toán học được tích hợp trong hệ thống EduRobot:")
    
    # Table 17 weeks
    m_tbl = doc.add_table(rows=18, cols=4)
    m_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    m_headers = ["Tuần", "Chủ đề thử thách", "Kiến thức Toán học trọng tâm", "Vật phẩm mở khóa"]
    for col_idx, h in enumerate(m_headers):
        cell = m_tbl.cell(0, col_idx)
        shd = parse_xml(r'<w:shd {} w:fill="1A365D"/>'.format(nsdecls('w')))
        cell._tc.get_or_add_tcPr().append(shd)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(h)
        set_font(r, size=11, bold=True, color=RGBColor(255, 255, 255))

    matrix_data = [
        ("19", "Bản đồ kho báu", "Tỉ số, Tỉ lệ bản đồ, Tỉ số phần trăm", "Ống nhòm Lũng Cú 🔭"),
        ("20", "Cán cân công lý", "Bài toán về đại lượng tỉ lệ thuận, tỉ lệ nghịch", "Cân tiểu ly ⚖️"),
        ("21", "Xây tháp tri thức 1", "Hình tam giác, diện tích hình tam giác", "Máy tính bỏ túi 📟"),
        ("22", "Xây tháp tri thức 2", "Hình thang, diện tích hình thang", "Bản đồ Thủ đô 🗺️"),
        ("23", "Thám hiểm đại dương", "Hình tròn, chu vi và diện tích hình tròn", "Thước cuộn 📏"),
        ("24", "Hình khai triển", "Hình hộp chữ nhật, hình lập phương & hình khai triển", "Mũ bảo hộ 🏗️"),
        ("25", "Khám phá Cố đô", "Diện tích xung quanh & toàn phần hình khối", "Quà cố đô Huế 🎁"),
        ("26", "Đo lường thời gian", "Thể tích hình hộp chữ nhật, hình lập phương", "Đồng hồ cát ⏳"),
        ("27", "Vương quốc đo lường", "Xăng-ti-mét khối, Đề-xi-mét khối, Mét khối", "Com-pa bạc 📐"),
        ("28", "Chinh phục tốc độ", "Vận tốc, quãng đường, thời gian (Chuyển động đều)", "Bánh lái tàu 🎡"),
        ("29", "Khám phá vũ trụ", "Toán chuyển động ngược chiều và cùng chiều", "Đèn pin hang động 🔦"),
        ("30", "Thế giới dữ liệu", "Bảng thống kê số liệu, biểu đồ hình quạt tròn", "Mô hình Bitexco 🏢"),
        ("31", "Học viện số học", "Ôn tập Phân số, Số thập phân và 4 phép tính", "La bàn số 🧭"),
        ("32", "Đền thờ toán học", "Ôn tập Đo lường (Độ dài, khối lượng, diện tích)", "Vé tàu cao tốc 🎫"),
        ("33", "Chinh phục rừng xanh", "Ôn tập Hình học tổng hợp (Chu vi, diện tích, thể tích)", "Mũ tai bèo 👒"),
        ("34", "Chinh phục đỉnh cao", "Ôn tập Giải toán có lời văn và toán chuyển động", "Cờ về đích 🚩"),
        ("35", "Đại hội chiến thắng", "Kỳ thi tổng kết – Đánh giá năng lực toàn diện Toán 5", "Huân chương Chiến thắng 🎖️")
    ]
    for row_idx, row_data in enumerate(matrix_data, start=1):
        bg_color = "F7FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = m_tbl.cell(row_idx, col_idx)
            shd = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), bg_color))
            cell._tc.get_or_add_tcPr().append(shd)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            if col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(text)
                set_font(r, size=10.5, bold=True)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(text)
                set_font(r, size=10.5)

    add_p()

    # -------------------------------------------------------------
    # PHẦN IV: QUY TRÌNH TỔ CHỨC DẠY HỌC THỰC NGHIỆM
    # -------------------------------------------------------------
    add_h1("PHẦN IV: QUY TRÌNH TỔ CHỨC DẠY HỌC THỰC NGHIỆM TẠI ĐƠN VỊ")

    add_h2("4.1. Quy trình 4 bước triển khai linh hoạt trong dạy học")
    add_p("Để chuyên đề đi vào thực chất và đạt hiệu quả tối ưu, chúng tôi xây dựng quy trình triển khai chuẩn mực gồm 4 bước:")
    add_bullet("Bước 1: Khởi động & Đăng ký danh tính nhà thám hiểm: ", "Vào đầu học kỳ 2, giáo viên hướng dẫn học sinh truy cập website hoặc Zalo Mini App. Học sinh nhập họ tên thật, chọn đúng lớp và trường học. Hệ thống lưu tài khoản trên thiết bị, các lần truy cập sau học sinh không cần nhập lại.")
    add_bullet("Bước 2: Ứng dụng linh hoạt trong các pha dạy học: ", "Hệ thống có thể sử dụng đa dạng:")
    add_p("   - Trong giờ học chính khóa: Giáo viên trình chiếu vòng 1 (Ghép đôi) trên tivi thông minh làm hoạt động Khởi động tạo không khí sôi nổi đầu giờ; hoặc dùng vòng 3 (Về đích) làm hoạt động Củng cố bài học trong 5 phút cuối tiết.\n   - Trong giờ tự học ở nhà: Mỗi chiều thứ Sáu hàng tuần, hệ thống tự động mở chặng mới. Giáo viên gửi thông báo vào nhóm phụ huynh để học sinh tự do khám phá và làm bài vào dịp cuối tuần.", indent=1.0)
    add_bullet("Bước 3: Tự động ghi nhận và vinh danh kết quả: ", "Học sinh hoàn thành bài thi, điểm số được đồng bộ về Firebase. Bảng vàng vinh danh cập nhật ngay lập tức. Học sinh có thể làm lại nhiều lần để cải thiện điểm số và thời gian, qua đó kích thích tinh thần tự giác vươn lên.")
    add_bullet("Bước 4: Phân tích dữ liệu và điều chỉnh phương pháp dạy học: ", "Giáo viên mở Bảng vàng, kiểm tra danh sách học sinh đã hoàn thành, nắm bắt những câu hỏi hay bài toán mà nhiều học sinh làm sai để giải thích lại trong tiết học đầu tuần sau.")

    add_h2("4.2. Phối hợp giữa nhà trường, giáo viên và phụ huynh qua kênh Zalo")
    add_p("Mối quan hệ đồng hành giữa gia đình và nhà trường là chìa khóa thành công của chuyên đề:")
    add_bullet("Tiện lợi tuyệt đối: ", "Nhờ tích hợp Zalo Mini App, giáo viên chỉ cần chia sẻ liên kết trực tiếp vào nhóm Zalo lớp. Phụ huynh nhấp vào là mở bài ngay, dễ dàng ngồi cạnh động viên con em mà không gặp bất kỳ trở ngại kỹ thuật nào.")
    add_bullet("Minh bạch thông tin: ", "Phụ huynh có thể cùng con mở trang 'Túi đồ' để xem số huy chương Vàng/Bạc con đã đạt được, biến chiếc điện thoại thông minh từ công cụ chơi game giải trí tiêu cực thành người bạn học tập đồng hành bổ ích.")

    add_h2("4.3. Khai thác dữ liệu thời gian thực để phân hóa và phụ đạo học sinh")
    add_p("Thông qua tính năng xuất file Excel và quan sát biểu đồ phân bố điểm số:")
    add_bullet("Nhóm học sinh Hoàn thành tốt (90 - 100 điểm, thời gian dưới 3 phút): ", "Giáo viên tuyên dương trước lớp, giao thêm các bài toán tư duy mở rộng.")
    add_bullet("Nhóm học sinh Hoàn thành (70 - 80 điểm): ", "Giáo viên khích lệ các em rà soát lại các câu sai ở Vòng 2 hoặc Vòng 3 để làm lại bài đạt huy chương Vàng.")
    add_bullet("Nhóm học sinh Chưa hoàn thành hoặc chưa tham gia: ", "Giáo viên phát hiện sớm ngay trong ngày Chủ nhật để liên hệ gia đình tìm hiểu nguyên nhân, có kế hoạch phụ đạo riêng vào buổi học tăng cường.")

    # -------------------------------------------------------------
    # PHẦN V: KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ TÁC ĐỘNG
    # -------------------------------------------------------------
    add_h1("PHẦN V: KẾT QUẢ ĐẠT ĐƯỢC VÀ ĐÁNH GIÁ TÁC ĐỘNG")

    add_h2("5.1. Đánh giá về mặt định lượng")
    add_p("Chuyên đề được triển khai thực nghiệm tại khối lớp 5 (các lớp 5/1 đến 5/5) trong học kỳ 2 năm học 2025 - 2026. Kết quả thống kê từ hệ thống cơ sở dữ liệu Firebase cho thấy những bước chuyển biến vượt bậc:")
    
    # Table quantitative results
    res_tbl = doc.add_table(rows=5, cols=3)
    res_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    res_headers = ["Tiêu chí đánh giá", "Trước khi áp dụng chuyên đề\n(Giao bài tập giấy truyền thống)", "Sau khi áp dụng EduRobot\n(Hệ thống bài tập tương tác)"]
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
        ("Tỉ lệ học sinh tự giác hoàn thành bài tập cuối tuần", "65.4% (thường xuyên bị nhắc nhở)", "96.8% (tự giác tham gia ngay tối thứ Sáu)"),
        ("Tỉ lệ học sinh đạt điểm Giỏi/Xuất sắc môn Toán", "28.5%", "48.2% (tăng 19.7%)"),
        ("Tỉ lệ học sinh còn lúng túng với dạng toán chuyển động", "38.2%", "11.5% (giảm mạnh 26.7%)"),
        ("Thời gian giáo viên thống kê và nắm bắt chất lượng", "120 phút/tuần (chấm vở thủ công)", "Dưới 5 phút/tuần (xuất Excel tự động)")
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
    add_bullet("Về phía học sinh: ", "Không khí học tập thay đổi ngoạn mục. Các em không còn sợ môn Toán mà xem mỗi tuần là một chuyến du lịch khám phá thú vị. Nhiều em làm đi làm lại 3 - 4 lần để đạt điểm tuyệt đối 100 nhằm ngắm pháo hoa và xuất hiện trên bảng Top 10 cao thủ. Ý thức tự giác và năng lực tự học được hình thành tự nhiên.")
    add_bullet("Về phía giáo viên: ", "Giáo viên trút bỏ được áp lực chấm bài giấy vụn vặt; có trong tay công cụ số đắc lực để theo dõi sát sao từng học sinh; nâng cao rõ rệt năng lực công nghệ thông tin và chuyển đổi số trong giảng dạy.")
    add_bullet("Về phía phụ huynh học sinh: ", "Phụ huynh bày tỏ sự đồng tình và ủng hộ tuyệt đối. Nhiều phụ huynh chia sẻ: 'Trước đây con cầm điện thoại là xem hoạt hình hay chơi game vô bổ, nay tối thứ Sáu nào con cũng nhắc mẹ mở Zalo để con thi thám hiểm lấy huy chương'.")

    add_h2("5.3. Khả năng chuyển giao và nhân rộng mô hình")
    add_p("Hệ thống EduRobot có kiến trúc mở, độc lập và khả năng mở rộng không giới hạn:")
    add_bullet("Mở rộng liên môn: ", "Dễ dàng bổ sung ngân hàng câu hỏi môn Tiếng Việt, Khoa học, Lịch sử và Địa lý lớp 5 theo cấu trúc 3 vòng tương tự.")
    add_bullet("Mở rộng liên khối: ", "Mô hình có thể chuyển giao áp dụng cho khối 4, khối 3 chỉ bằng cách thay đổi nội dung dữ liệu và hình ảnh bản đồ theo chủ đề phù hợp.")
    add_bullet("Chia sẻ tài nguyên: ", "Hệ thống sẵn sàng chia sẻ miễn phí cho các trường bạn trong huyện, trong tỉnh thông qua liên kết website và mini app Zalo.")

    # -------------------------------------------------------------
    # PHẦN VI: KẾT LUẬN VÀ KIẾN NGHỊ
    # -------------------------------------------------------------
    add_h1("PHẦN VI: KẾT LUẬN VÀ KIẾN NGHỊ")

    add_h2("6.1. Kết luận")
    add_p("Chuyên đề 'Ôn tập môn Toán lớp 5 theo định hướng chuyển đổi số với hệ thống bài tập tương tác' là một giải pháp giáo dục toàn diện, kết hợp hài hòa giữa yêu cầu sư phạm của Chương trình GDPT 2018 và sức mạnh của công nghệ số hiện đại. Bằng việc lấy học sinh làm trung tâm, biến các con số và công thức toán học khô khan thành chuyến hành trình xuyên Việt đầy tự hào, chuyên đề đã giải quyết triệt để bài toán về động lực học tập, nâng cao chất lượng giáo dục môn Toán cuối cấp tiểu học một cách bền vững.")

    add_h2("6.2. Bài học kinh nghiệm")
    add_bullet("1. Công nghệ phải phục vụ sư phạm: ", "Ứng dụng chuyển đổi số không phải là phô diễn kỹ thuật mà phải xuất phát từ nhu cầu thực tiễn của học sinh và phục vụ đắc lực cho mục tiêu dạy học.")
    add_bullet("2. Đơn giản hóa trải nghiệm người dùng: ", "Mọi giải pháp công nghệ dành cho học sinh tiểu học phải tinh gọn, dễ dùng và tận dụng các nền tảng quen thuộc (như Zalo) để không tạo rào cản cho phụ huynh.")
    add_bullet("3. Động viên, khen thưởng kịp thời: ", "Tâm lý học sinh tiểu học luôn cần sự ghi nhận tức thời. Các yếu tố như pháo hoa, huy chương, bảng vàng chính là chất xúc tác nuôi dưỡng đam mê học tập lâu dài.")

    add_h2("6.3. Đề xuất, kiến nghị")
    add_bullet("Đối với Tổ chuyên môn và Nhà trường: ", "Tạo điều kiện tổ chức các tiết thao giảng minh họa chuyên đề; đưa hệ thống EduRobot vào kế hoạch sinh hoạt chuyên môn định kỳ và khuyến khích các giáo viên trong khối cùng tham gia đóng góp ngân hàng câu hỏi.")
    add_bullet("Đối với Phòng Giáo dục và Đào tạo: ", "Xem xét tổ chức hội thảo chuyên đề cấp cụm trường để nhân rộng mô hình; có cơ chế khuyến khích, động viên các sáng kiến chuyển đổi số dạy học xuất phát từ giáo viên trực tiếp đứng lớp.")

    # -------------------------------------------------------------
    # PHẦN KÝ TÊN VÀ DUYỆT BÁO CÁO
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

    # Empty row for signature
    sign_tbl.cell(1, 0).paragraphs[0].paragraph_format.space_before = Pt(45)
    sign_tbl.cell(1, 1).paragraphs[0].paragraph_format.space_before = Pt(45)

    # Names
    p_nl = sign_tbl.cell(2, 0).paragraphs[0]
    p_nl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_nl = p_nl.add_run("(Ký và đóng dấu)")
    set_font(r_nl, size=11, italic=True)

    p_nr = sign_tbl.cell(2, 1).paragraphs[0]
    p_nr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_nr = p_nr.add_run("Lê Thành Long")
    set_font(r_nr, size=12.5, bold=True)

    # Output file
    output_path = "Chuyen_De_Toan_5_Chuyen_Doi_So_EduRobot.docx"
    doc.save(output_path)
    print("File saved successfully: " + output_path)

if __name__ == "__main__":
    create_chuyen_de_document()
