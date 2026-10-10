#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# FOSS LUBRICATION (fosslubricants.com) Multilingual Matrix Compiler
# Generates 5 international language subdirectories: /es/, /ru/, /ar/, /vi/, /id/
# Implements strict Tribology & Lubrication Dictionary to prevent AI hallucination
# Updates all English pages: strips company name text from logo, adds language switcher
# Updates sitemap.xml with xhtml:link hreflang entries
# ==============================================================================

import os
import re
import glob

SITE_DOMAIN = "https://www.fosslubricants.com"
VERSION_TAG = "v=20261010_v11"

LANGUAGES = [
    {"code": "en", "name": "English", "flag": "🇺🇸", "prefix": ""},
    {"code": "es", "name": "Español", "flag": "🇪🇸", "prefix": "/es"},
    {"code": "ru", "name": "Русский", "flag": "🇷🇺", "prefix": "/ru"},
    {"code": "ar", "name": "العربية", "flag": "🇸🇦", "prefix": "/ar", "rtl": True},
    {"code": "vi", "name": "Tiếng Việt", "flag": "🇻🇳", "prefix": "/vi"},
    {"code": "id", "name": "Indonesia", "flag": "🇮🇩", "prefix": "/id"},
]

CORE_PAGES = [
    {"file": "index.html", "slug": ""},
    {"file": "hydraulic-oil.html", "slug": "hydraulic-oil"},
    {"file": "industrial-oils.html", "slug": "industrial-oils"},
    {"file": "packaging-logistics.html", "slug": "packaging-logistics"},
    {"file": "about.html", "slug": "about"},
    {"file": "products.html", "slug": "products"},
    {"file": "news.html", "slug": "news"},
    {"file": "contact.html", "slug": "contact"},
]

NAV_TRANSLATIONS = {
    "en": {
        "home": "Home",
        "hydraulic": "Hydraulic Oils",
        "industrial": "Industrial Oils",
        "packaging": "Packaging & Logistics",
        "about": "About Factory",
        "news": "Market Insights",
        "contact": "Contact & RFQ",
        "quote_btn": "Request Quote",
    },
    "es": {
        "home": "Inicio",
        "hydraulic": "Aceites Hidráulicos",
        "industrial": "Aceites Industriales",
        "packaging": "Embalaje y Logística",
        "about": "Sobre la Fábrica",
        "news": "Inteligencia de Mercado",
        "contact": "Contacto y RFQ",
        "quote_btn": "Cotizar Ahora",
    },
    "ru": {
        "home": "Главная",
        "hydraulic": "Гидравлические масла",
        "industrial": "Индустриальные масла",
        "packaging": "Упаковка и логистика",
        "about": "О заводе",
        "news": "Аналитика рынка",
        "contact": "Контакты и RFQ",
        "quote_btn": "Запросить КП",
    },
    "ar": {
        "home": "الرئيسية",
        "hydraulic": "زيوت هيدروليكية",
        "industrial": "زيوت صناعية",
        "packaging": "التعبئة واللوجستيات",
        "about": "عن المصنع",
        "news": "تحليلات السوق",
        "contact": "الاتصال وطلب الأسعار",
        "quote_btn": "طلب تسعيرة",
    },
    "vi": {
        "home": "Trang Chủ",
        "hydraulic": "Dầu Thủy Lực",
        "industrial": "Dầu Công Nghiệp",
        "packaging": "Đóng Gói & Logistics",
        "about": "Về Nhà Máy",
        "news": "Báo Cáo Thị Trường",
        "contact": "Liên Hệ & Báo Giá",
        "quote_btn": "Yêu Cầu Báo Giá",
    },
    "id": {
        "home": "Beranda",
        "hydraulic": "Oli Hidrolik",
        "industrial": "Oli Industri",
        "packaging": "Pengemasan & Logistik",
        "about": "Tentang Pabrik",
        "news": "Wawasan Pasar",
        "contact": "Kontak & RFQ",
        "quote_btn": "Minta Penawaran",
    },
}

PAGE_TRANSLATIONS = {
    "es": {
        "lang_name": "Español",
        "home_title": "Aceites Hidráulicos Industriales y Lubricantes en Tambores de 208L | FOSS LUBRICATION",
        "home_desc": "Quanzhou Foss Lubrication Technology Co., Ltd formula y suministra aceites hidráulicos industriales de alto rendimiento (L-HM, L-HV, sin cenizas, agua-glicol) y lubricantes industriales en tambores de acero certificados UN de 208L y contenedores IBC de 1000L para exportación marítima mundial a través del Puerto de Xiamen.",
        "hero_tag": "Ingeniería de Lubricación de Precisión · Fundada en 2018 en Quanzhou, China",
        "hero_title": "Aceites Hidráulicos Industriales y Lubricantes en Tambores de Acero de 208L",
        "hero_desc": "Formulado con aceites base vírgenes hidroprocesados Grupo II/III y sistemas de aditivos premium. Cumpliendo con las normas <strong>DIN 51524-2 (HLP)</strong>, <strong>ISO 11158</strong> y <strong>Parker Denison HF-0</strong>. Suministrado en tambores de acero de 208L certificados UN y contenedores IBC de 1000L para exportación en contenedores marítimos por el Puerto de Xiamen.",
        "btn_advisor": "Usar Asesor Inteligente de Aceite",
        "btn_calc": "Calculadora de Contenedor 20GP",
        "btn_sample": "Solicitar Muestra y CoA Sellado",
        "btn_whatsapp": "Consultar por WhatsApp",
        "stat_founded": "Fundada en Quanzhou",
        "stat_drums": "Paletizado Estándar 20GP",
        "stat_tested": "Probado en Laboratorio Pre-Envío",
        "stat_cost": "Ventaja de Costo vs Petroleras",
        "packaging_specs": "Especificaciones de Embalaje de Exportación",
        "wall_thickness": "Espesor de Pared",
        "tare_weight": "Peso de Tara",
        "payload_20gp": "Carga Útil / 20GP",
        "oem_options": "Opciones OEM",
        "explore_drums": "Explorar Dimensiones de Tambor y Carga",
        "port_shipping": "Envío Portuario y Estiba de Contenedores",
        "factory_to_port": "Fábrica al Puerto",
        "fob_lead_time": "Tiempo de Carga FOB",
        "export_docs": "Documentos de Exportación",
        "pallet_protection": "Protección de Palets",
        "explore_freight": "Explorar Logística Marítima",
    },
    "ru": {
        "lang_name": "Русский",
        "home_title": "Индустриальные гидравлические масла и смазочные материалы в бочках 208 л | FOSS LUBRICATION",
        "home_desc": "Quanzhou Foss Lubrication Technology Co., Ltd производит и поставляет высокоэффективные гидравлические масла (L-HM, L-HV, бесцинковые, водно-гликолевые) и смазочные материалы в сертифицированных UN стальных бочках 208 л и кубах IBC 1000 л для экспорта через порт Сямэнь.",
        "hero_tag": "Прецизионное производство смазочных материалов · Осн. в 2018 г. в Цюаньчжоу, Китай",
        "hero_title": "Индустриальные гидравлические масла и смазки в стальных бочках 208 л",
        "hero_desc": "Произведено на основе первичных гидрокрекинговых базовых масел Группы II/III и премиальных пакетов присадок. Соответствует стандартам <strong>DIN 51524-2 (HLP)</strong>, <strong>ISO 11158</strong> и <strong>Parker Denison HF-0</strong>. Поставка в сертифицированных UN стальных бочках 208 л и IBC 1000 л для морского экспорта через порт Сямэнь.",
        "btn_advisor": "Умный подбор масла",
        "btn_calc": "Калькулятор загрузки 20GP",
        "btn_sample": "Запросить образец и CoA с печатью",
        "btn_whatsapp": "Связаться через WhatsApp",
        "stat_founded": "Основано в Цюаньчжоу",
        "stat_drums": "Стандарт паллетизации 20GP",
        "stat_tested": "Лабораторные тесты перед отправкой",
        "stat_cost": "Ценовое преимущество перед гигантами",
        "packaging_specs": "Экспортные спецификации упаковки",
        "wall_thickness": "Толщина стенок",
        "tare_weight": "Вес пустой тары",
        "payload_20gp": "Полезный объем / 20GP",
        "oem_options": "Возможности OEM",
        "explore_drums": "Характеристики бочек и загрузки",
        "port_shipping": "Морская доставка и загрузка контейнеров",
        "factory_to_port": "От завода до порта",
        "fob_lead_time": "Срок погрузки FOB",
        "export_docs": "Экспортные документы",
        "pallet_protection": "Защита паллет",
        "explore_freight": "Изучить морскую логистику",
    },
    "ar": {
        "lang_name": "العربية",
        "home_title": "زيوت هيدروليكية صناعية ومواد تشحيم في براميل فولاذية سعة 208 لتر | FOSS LUBRICATION",
        "home_desc": "تقوم شركة تشوانتشو فوس لتكنولوجيا التزييت المحدودة بتصنيع وتوريد زيوت هيدروليكية صناعية عالية الأداء (L-HM، L-HV، خالية من الرماد، ماء-جليكول) ومواد تشحيم في براميل فولاذية معتمدة من الأمم المتحدة سعة 208 لتر للتصدير العالمي عبر ميناء شيامن.",
        "hero_tag": "هندسة التزييت الدقيقة · تأسست عام 2018 في تشوانتشو، الصين",
        "hero_title": "زيوت هيدروليكية صناعية ومواد تشحيم في براميل فولاذية 208 لتر",
        "hero_desc": "مركبة من زيوت أساس بكر مهدرجة تكسير هيدروجيني مجموعة ثانية وثالثة وحزم إضافات فائقة الجودة. مطابقة لمعايير <strong>DIN 51524-2 (HLP)</strong> و <strong>ISO 11158</strong> و <strong>Parker Denison HF-0</strong>. توريد في براميل فولاذية معتمدة من الأمم المتحدة وحاويات IBC عبر ميناء شيامن.",
        "btn_advisor": "استخدم مستشار الزيت الذكي",
        "btn_calc": "حاسبة تحميل حاوية 20 قدم",
        "btn_sample": "طلب عينة دفعة وشهادة CoA مختومة",
        "btn_whatsapp": "استفسر عبر واتساب",
        "stat_founded": "تأسست في تشوانتشو",
        "stat_drums": "مشاتن قياسي لحاوية 20 قدم",
        "stat_tested": "فحص مختبري قبل الشحن",
        "stat_cost": "ميزة سعرية مقارنة بالشركات الكبرى",
        "packaging_specs": "المواصفات القياسية لتعبئة التصدير",
        "wall_thickness": "سمك الجدار",
        "tare_weight": "وزن البرميل الفارغ",
        "payload_20gp": "الحمولة / حاوية 20 قدم",
        "oem_options": "خيارات التصنيع للغير OEM",
        "explore_drums": "استكشف أبعاد البراميل ومواصفات الحاويات",
        "port_shipping": "الشحن المينائي وتجهيز الحاويات",
        "factory_to_port": "من المصنع إلى الميناء",
        "fob_lead_time": "مدة تجهيز شحن FOB",
        "export_docs": "وثائق التصدير",
        "pallet_protection": "حماية المشاتن",
        "explore_freight": "استكشف الخدمات اللوجستية البحرية",
    },
    "vi": {
        "lang_name": "Tiếng Việt",
        "home_title": "Dầu Thủy Lực Công Nghiệp & Dầu Nhờn Trong Phuy Thép 208L | FOSS LUBRICATION",
        "home_desc": "Quanzhou Foss Lubrication Technology Co., Ltd pha chế và cung cấp dầu thủy lực công nghiệp hiệu suất cao (L-HM, L-HV, không tro, nước-glycol) và dầu nhờn công nghiệp trong phuy thép tiêu chuẩn UN 208L và bồn IBC 1000L xuất khẩu toàn cầu qua Cảng Hạ Môn.",
        "hero_tag": "Kỹ Thuật Bôi Trơn Chính Xác · Thành lập 2018 tại Quanzhou, Trung Quốc",
        "hero_title": "Dầu Thủy Lực Công Nghiệp & Dầu Nhờn Trong Phuy Thép 208L",
        "hero_desc": "Được pha chế từ dầu gốc khoáng nhóm II/III hydrocracking nguyên sinh và hệ phụ gia cao cấp. Đạt tiêu chuẩn <strong>DIN 51524-2 (HLP)</strong>, <strong>ISO 11158</strong> và <strong>Parker Denison HF-0</strong>. Đóng gói trong phuy thép tiêu chuẩn UN 208L và bồn IBC 1000L xuất khẩu đường biển qua Cảng Hạ Môn.",
        "btn_advisor": "Dùng Tư Vấn Dầu Thông Minh",
        "btn_calc": "Công Cụ Tính Tải Công 20GP",
        "btn_sample": "Yêu Cầu Mẫu Thử & CoA Đóng Dấu",
        "btn_whatsapp": "Tư Vấn Qua WhatsApp",
        "stat_founded": "Thành lập tại Quanzhou",
        "stat_drums": "Đóng Pallet Tiêu Chuẩn 20GP",
        "stat_tested": "Kiểm Nghiệm Lab Trước Khi Giao",
        "stat_cost": "Ưu Thế Giá So Với Hãng Lớn",
        "packaging_specs": "Thông Số Đóng Gói Xuất Khẩu Tiêu Chuẩn",
        "wall_thickness": "Độ Dày Thành Phuy",
        "tare_weight": "Trọng Lượng Vỏ Phuy",
        "payload_20gp": "Tải Trọng / 20GP",
        "oem_options": "Tùy Chọn OEM",
        "explore_drums": "Khám Phá Kích Thước Phuy & Tải Công",
        "port_shipping": "Vận Chuyển Cảng & Đóng Công Container",
        "factory_to_port": "Từ Nhà Máy Đến Cảng",
        "fob_lead_time": "Thời Gian Xếp Hàng FOB",
        "export_docs": "Chứng Từ Xuất Khẩu",
        "pallet_protection": "Bảo Vệ Pallet",
        "explore_freight": "Khám Phá Logistics Đường Biển",
    },
    "id": {
        "lang_name": "Bahasa Indonesia",
        "home_title": "Oli Hidrolik Industri & Pelumas dalam Drum Baja 208L | FOSS LUBRICATION",
        "home_desc": "Quanzhou Foss Lubrication Technology Co., Ltd memproduksi dan memasok oli hidrolik industri berkinerja tinggi (L-HM, L-HV, bebas abu, water-glycol) dan pelumas industri dalam drum baja bersertifikat UN 208L dan IBC 1000L untuk ekspor global melalui Pelabuhan Xiamen.",
        "hero_tag": "Teknik Pelumasan Presisi · Didirikan 2018 di Quanzhou, Tiongkok",
        "hero_title": "Oli Hidrolik Industri & Pelumas dalam Drum Baja 208L",
        "hero_desc": "Diformulasikan dengan minyak dasar virgin hydrocrack Grup II/III dan paket aditif premium. Memenuhi standar <strong>DIN 51524-2 (HLP)</strong>, <strong>ISO 11158</strong>, dan <strong>Parker Denison HF-0</strong>. Dipasok dalam drum baja 208L bersertifikat UN dan tote IBC 1000L untuk ekspor kontainer via Pelabuhan Xiamen.",
        "btn_advisor": "Gunakan Penasihat Oli Pintar",
        "btn_calc": "Kalkulator Pemuatan Kontainer 20GP",
        "btn_sample": "Minta Sampel & CoA Berstempel",
        "btn_whatsapp": "Tanya via WhatsApp",
        "stat_founded": "Didirikan di Quanzhou",
        "stat_drums": "Palet Standar 20GP",
        "stat_tested": "Uji Lab Pra-Pengiriman",
        "stat_cost": "Keunggulan Biaya vs Perusahaan Besar",
        "packaging_specs": "Spesifikasi Pengemasan Ekspor Standar",
        "wall_thickness": "Ketebalan Dinding",
        "tare_weight": "Berat Tara",
        "payload_20gp": "Kapasitas / 20GP",
        "oem_options": "Pilihan OEM",
        "explore_drums": "Jelajahi Dimensi Drum & Spesifikasi Kontainer",
        "port_shipping": "Pengiriman Pelabuhan & Penataan Kontainer",
        "factory_to_port": "Dari Pabrik ke Pelabuhan",
        "fob_lead_time": "Waktu Tunggu Muat FOB",
        "export_docs": "Dokumen Ekspor",
        "pallet_protection": "Proteksi Palet",
        "explore_freight": "Jelajahi Logistik Angkutan Laut",
    },
}

def get_page_url(lang_code, slug):
    prefix = "" if lang_code == "en" else f"/{lang_code}"
    if not slug:
        return f"{prefix}/" if prefix else "/"
    return f"{prefix}/{slug}"

def generate_hreflang_tags(slug):
    tags = []
    for lang in LANGUAGES:
        code = lang["code"]
        url = f"{SITE_DOMAIN}{get_page_url(code, slug)}"
        tags.append(f'  <link rel="alternate" hreflang="{code}" href="{url}">')
    default_url = f"{SITE_DOMAIN}{get_page_url('en', slug)}"
    tags.append(f'  <link rel="alternate" hreflang="x-default" href="{default_url}">')
    return "\n".join(tags)

def generate_lang_switcher_html(current_lang, slug):
    current_upper = current_lang.upper()
    options_html = []
    for lang in LANGUAGES:
        code = lang["code"]
        is_active = (code == current_lang)
        active_class = " active" if is_active else ""
        url = get_page_url(code, slug)
        options_html.append(f'''            <a href="{url}" class="lang-option{active_class}" role="menuitem" data-code="{code}">
              <span class="lang-flag">{lang["flag"]}</span>
              <span class="lang-title">{lang["name"]}</span>
              <span class="lang-code-pill">{code.upper()}</span>
            </a>''')
    
    return f'''<div class="lang-switcher">
          <button class="lang-toggle" type="button" aria-expanded="false" aria-label="Select Language">
            <span class="lang-globe">🌐</span>
            <span class="lang-current">{current_upper}</span>
            <svg class="lang-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="lang-dropdown" role="menu">
{chr(10).join(options_html)}
          </div>
        </div>'''

def generate_nav_links_html(lang_code, active_slug):
    nav = NAV_TRANSLATIONS[lang_code]
    p = "" if lang_code == "en" else f"/{lang_code}"
    
    links = [
        {"slug": "", "url": f"{p}/" if p else "/", "label": nav["home"]},
        {"slug": "hydraulic-oil", "url": f"{p}/hydraulic-oil", "label": nav["hydraulic"]},
        {"slug": "industrial-oils", "url": f"{p}/industrial-oils", "label": nav["industrial"]},
        {"slug": "packaging-logistics", "url": f"{p}/packaging-logistics", "label": nav["packaging"]},
        {"slug": "about", "url": f"{p}/about", "label": nav["about"]},
        {"slug": "news", "url": f"{p}/news", "label": nav["news"]},
        {"slug": "contact", "url": f"{p}/contact", "label": nav["contact"]},
    ]
    
    items = []
    for item in links:
        is_active = (item["slug"] == active_slug)
        active_class = ' class="nav-link active"' if is_active else ' class="nav-link"'
        items.append(f'          <li><a href="{item["url"]}"{active_class}>{item["label"]}</a></li>')
    return "\n".join(items)

def update_english_file(filepath, slug):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Logo: strip .site-logo-text
    logo_pattern = r'<a href="/" class="site-logo-link"[^>]*>[\s\S]*?<img src="([^"]+)" alt="([^"]+)" class="site-logo-img"[^>]*>[\s\S]*?<div class="site-logo-text">[\s\S]*?</div>\s*</a>'
    clean_logo = r'<a href="/" class="site-logo-link" aria-label="FOSS LUBRICATION Homepage">\n        <img src="/assets/images/foss-official-logo.png" alt="FOSS LUBRICATION Logo - 福斯润滑" class="site-logo-img" width="135" height="48">\n      </a>'
    content = re.sub(logo_pattern, clean_logo, content)

    # 2. Add Language Switcher into .header-actions if not present
    if 'class="lang-switcher"' not in content:
        switcher_html = generate_lang_switcher_html("en", slug)
        # Place before quote button in header-actions
        actions_pattern = r'(<div class="header-actions">)(\s*)(<a href="[^"]*" class="btn btn-primary btn-sm">)'
        content = re.sub(actions_pattern, r'\1\n        ' + switcher_html + r'\n        \3', content)

    # 3. Add hreflang tags if not present
    if 'hreflang="es"' not in content:
        hreflang_html = generate_hreflang_tags(slug)
        content = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1\n' + hreflang_html, content)

    # 4. Bump version tag
    content = content.replace("main.css?v=20261010_v10", f"main.css?{VERSION_TAG}")
    content = content.replace("app.js?v=20261010_v9", f"app.js?{VERSION_TAG}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated English file: {filepath}")


def sync_schema(html_content, page_url, lang_code):
    title_m = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
    title = title_m.group(1).strip() if title_m else ""
    desc_m = re.search(r'<meta name="description" content="(.*?)">', html_content, re.DOTALL)
    desc = desc_m.group(1).strip() if desc_m else ""

    def repl_script(match):
        raw_json = match.group(1)
        try:
            import json
            data = json.loads(raw_json)
            nodes = data.get("@graph", [data])
            for node in nodes:
                types = node.get("@type", [])
                if isinstance(types, str):
                    types = [types]
                if "WebPage" in types:
                    node["name"] = title
                    node["description"] = desc
                    node["inLanguage"] = lang_code
                    node["url"] = page_url
                    node["@id"] = f"{page_url}#webpage"
            formatted_json = json.dumps(data, indent=2, ensure_ascii=False)
            return '<script type="application/ld+json">\n' + formatted_json + '\n  </script>'
        except Exception as e:
            return match.group(0)

    html_content = re.sub(r'<script type="application/ld\+json">(.*?)</script>', repl_script, html_content, flags=re.DOTALL)
    return html_content

def build_localized_page(en_content, lang_code, slug):
    t = PAGE_TRANSLATIONS[lang_code]
    nav = NAV_TRANSLATIONS[lang_code]
    is_rtl = (lang_code == "ar")
    html_attr = f'lang="{lang_code}" dir="rtl"' if is_rtl else f'lang="{lang_code}"'

    content = en_content

    # 1. Update <html lang="...">
    content = re.sub(r'<html lang="[^"]*"[^>]*>', f'<html {html_attr}>', content)

    # 2. Update canonical URL & Schema
    page_url = f"{SITE_DOMAIN}{get_page_url(lang_code, slug)}"
    content = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{page_url}">', content)
    content = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{page_url}">', content)

    # Update Schema WebPage url and @id
    base_en_url = f"{SITE_DOMAIN}/{slug}" if slug else f"{SITE_DOMAIN}/"
    content = content.replace(f'"{base_en_url}#webpage"', f'"{page_url}#webpage"')
    content = content.replace(f'"{base_en_url}"', f'"{page_url}"')
    content = re.sub(r'"inLanguage":\s*"en"', f'"inLanguage": "{lang_code}"', content)

    # 3. Update hreflang tags
    hreflangs = generate_hreflang_tags(slug)
    content = re.sub(r'(\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*">)+', '\n' + hreflangs, content)

    # 4. Update Header Logo Link to localized home
    p = f"/{lang_code}/"
    content = re.sub(
        r'<a href="/" class="site-logo-link" aria-label="FOSS LUBRICATION Homepage">',
        f'<a href="{p}" class="site-logo-link" aria-label="FOSS LUBRICATION {t["lang_name"]}">',
        content
    )

    # 5. Update Navigation links
    new_nav = generate_nav_links_html(lang_code, slug)
    content = re.sub(r'(<ul class="nav-links">)[\s\S]*?(</ul>)', r'\1\n' + new_nav + r'\n        \2', content)

    # 6. Update Quote button in header
    content = re.sub(
        r'(<a href="[^"]*" class="btn btn-primary btn-sm">)[^<]*(</a>)',
        r'\1' + nav["quote_btn"] + r'\2',
        content
    )

    # 7. Update Language Switcher
    new_switcher = generate_lang_switcher_html(lang_code, slug)
    content = re.sub(r'<div class="lang-switcher">[\s\S]*?</div>\s*</div>', new_switcher + '\n      </div>', content)

    # 8. Localize Page Content based on dictionary
    content = content.replace("Precision Lubrication Engineering · Est. 2018 Quanzhou, China", t["hero_tag"])
    content = content.replace("Industrial Hydraulic Oils & Lubricants in 208L Steel Drums", t["hero_title"])
    content = content.replace("Quanzhou Foss Lubrication Technology Co., Ltd blends and supplies high-performance industrial hydraulic oils (L-HM, L-HV, Ashless, Water-Glycol) and industrial lubricants in UN-certified 208L steel drums and 1000L IBC totes for worldwide container export via Xiamen Port.", t["home_desc"])
    content = content.replace("Use Smart Oil Advisor", t["btn_advisor"])
    content = content.replace("20GP Container Loading Calculator", t["btn_calc"])
    content = content.replace("Request Batch Sample & Stamped CoA", t["btn_sample"])
    content = content.replace("Inquire via WhatsApp", t["btn_whatsapp"])
    content = content.replace("Founded in Quanzhou", t["stat_founded"])
    content = content.replace("20GP Standard Palletized", t["stat_drums"])
    content = content.replace("Pre-Shipment Lab Tested", t["stat_tested"])
    content = content.replace("Cost Advantage vs Majors", t["stat_cost"])
    content = content.replace("Standard Export Packaging Specs", t["packaging_specs"])
    content = content.replace("Wall Thickness:", f"{t['wall_thickness']}:")
    content = content.replace("Tare Weight:", f"{t['tare_weight']}:")
    content = content.replace("Payload / 20GP:", f"{t['payload_20gp']}:")
    content = content.replace("OEM Options:", f"{t['oem_options']}:")
    content = content.replace("Explore Drum Dimensions & Container Specs", t["explore_drums"])
    content = content.replace("Port Shipping & Container Staging", t["port_shipping"])
    content = content.replace("Factory to Port:", f"{t['factory_to_port']}:")
    content = content.replace("FOB Loading Lead Time:", f"{t['fob_lead_time']}:")
    content = content.replace("Export Documents:", f"{t['export_docs']}:")
    content = content.replace("Pallet Protection:", f"{t['pallet_protection']}:")
    content = content.replace("Explore Ocean Freight Logistics", t["explore_freight"])

    # 9. Localize Titles & Meta Descriptions
    if slug == "":
        content = re.sub(r'<title>[^<]*</title>', f'<title>{t["home_title"]}</title>', content)
        content = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{t["home_desc"]}">', content)
        content = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{t["home_title"]}">', content)
        content = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{t["home_desc"]}">', content)
    elif slug == "hydraulic-oil":
        h_title = f"{nav['hydraulic']} (DIN 51524 HLP/HVLP) | FOSS LUBRICATION"
        content = re.sub(r'<title>[^<]*</title>', f'<title>{h_title}</title>', content)
    elif slug == "industrial-oils":
        i_title = f"{nav['industrial']} (L-CKD, L-DAH, L-QB) | FOSS LUBRICATION"
        content = re.sub(r'<title>[^<]*</title>', f'<title>{i_title}</title>', content)
    elif slug == "packaging-logistics":
        p_title = f"{nav['packaging']} (UN 1A1 208L) | FOSS LUBRICATION"
        content = re.sub(r'<title>[^<]*</title>', f'<title>{p_title}</title>', content)
    elif slug == "about":
        a_title = f"{nav['about']} (Quanzhou, China) | FOSS LUBRICATION"
        content = re.sub(r'<title>[^<]*</title>', f'<title>{a_title}</title>', content)
    elif slug == "products":
        pr_title = f"{nav['hydraulic']} & {nav['industrial']} | FOSS LUBRICATION"
        content = re.sub(r'<title>[^<]*</title>', f'<title>{pr_title}</title>', content)
    elif slug == "news":
        n_title = f"{nav['news']} & Daily Oil Forecasts | FOSS LUBRICATION"
        content = re.sub(r'<title>[^<]*</title>', f'<title>{n_title}</title>', content)
    elif slug == "contact":
        c_title = f"{nav['contact']} - Quanzhou Factory | FOSS LUBRICATION"
        content = re.sub(r'<title>[^<]*</title>', f'<title>{c_title}</title>', content)

    # 10. Localize internal links within page (e.g. href="/hydraulic-oil" -> href="/es/hydraulic-oil")
    for cp in CORE_PAGES:
        s = cp["slug"]
        if s:
            content = re.sub(rf'href="/{s}"', f'href="/{lang_code}/{s}"', content)
            content = re.sub(rf'href="{s}"', f'href="/{lang_code}/{s}"', content)
        else:
            content = re.sub(r'href="/"', f'href="/{lang_code}/"', content)

    # 11. Ensure absolute paths for assets and meta links
    content = re.sub(r'srcset="assets/images/', r'srcset="/assets/images/', content)
    content = re.sub(r'src="assets/images/', r'src="/assets/images/', content)
    content = re.sub(r'href="css/', r'href="/css/', content)
    content = re.sub(r'src="js/', r'src="/js/', content)
    content = content.replace('href="sitemap.xml"', 'href="/sitemap.xml"')
    content = content.replace('href="robots.txt"', 'href="/robots.txt"')
    content = content.replace('href="ai/products.json"', 'href="/ai/products.json"')
    content = content.replace('href="ai/summary.json"', 'href="/ai/summary.json"')
    content = content.replace('href="llms.txt"', 'href="/llms.txt"')
    content = content.replace('href="site.webmanifest"', 'href="/site.webmanifest"')
    content = content.replace('href="favicon.ico"', 'href="/favicon.ico"')
    content = content.replace('href="apple-touch-icon.png"', 'href="/apple-touch-icon.png"')

    content = sync_schema(content, page_url, lang_code)
    return content

def rebuild_sitemap():
    urls = []
    # 1. Core pages (all 6 languages)
    for cp in CORE_PAGES:
        slug = cp["slug"]
        for lang in LANGUAGES:
            code = lang["code"]
            loc = f"{SITE_DOMAIN}{get_page_url(code, slug)}"
            priority = "1.0" if slug == "" and code == "en" else ("0.9" if slug in ["", "hydraulic-oil", "news"] else "0.8")
            changefreq = "daily" if slug in ["", "news"] else ("weekly" if slug in ["hydraulic-oil", "industrial-oils", "products"] else "monthly")
            
            # Build alternates
            alternates = []
            for a_lang in LANGUAGES:
                a_code = a_lang["code"]
                a_url = f"{SITE_DOMAIN}{get_page_url(a_code, slug)}"
                alternates.append(f'    <xhtml:link rel="alternate" hreflang="{a_code}" href="{a_url}"/>')
            alternates.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_DOMAIN}{get_page_url("en", slug)}"/>')
            
            urls.append(f'''  <url>
    <loc>{loc}</loc>
    <lastmod>2026-10-10</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
{chr(10).join(alternates)}
  </url>''')

    # 2. News articles (English)
    news_files = sorted(glob.glob("news/*.html"))
    for nf in news_files:
        n_slug = os.path.splitext(os.path.basename(nf))[0]
        n_loc = f"{SITE_DOMAIN}/news/{n_slug}"
        urls.append(f'''  <url>
    <loc>{n_loc}</loc>
    <lastmod>2026-10-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>''')

    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>
'''
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print(f"Generated sitemap.xml with {len(urls)} URLs.")

def main():
    print("=== [1/4] Updating all English pages ===")
    for cp in CORE_PAGES:
        fpath = cp["file"]
        if os.path.exists(fpath):
            update_english_file(fpath, cp["slug"])

    # Update news files
    for nf in glob.glob("news/*.html"):
        with open(nf, "r", encoding="utf-8") as f:
            content = f.read()
        # Clean logo in news
        content = re.sub(
            r'<div class="site-logo-text">[\s\S]*?</div>',
            '',
            content
        )
        # Add switcher if not present
        if 'class="lang-switcher"' not in content:
            switcher = generate_lang_switcher_html("en", "news")
            content = re.sub(
                r'(<div class="header-actions">)(\s*)(<a href="[^"]*" class="btn btn-primary btn-sm">)',
                r'\1\n        ' + switcher + r'\n        \3',
                content
            )
        content = content.replace("main.css?v=20261010_v10", f"main.css?{VERSION_TAG}")
        content = content.replace("app.js?v=20261010_v9", f"app.js?{VERSION_TAG}")
        with open(nf, "w", encoding="utf-8") as f:
            f.write(content)

    print("=== [2/4] Generating 5 International Language Subdirectories ===")
    for lang in LANGUAGES:
        code = lang["code"]
        if code == "en":
            continue
        os.makedirs(code, exist_ok=True)
        print(f"Generating language matrix for: {lang['name']} ({code})")
        for cp in CORE_PAGES:
            en_file = cp["file"]
            if not os.path.exists(en_file):
                continue
            with open(en_file, "r", encoding="utf-8") as f:
                en_content = f.read()
            localized = build_localized_page(en_content, code, cp["slug"])
            target_path = os.path.join(code, en_file)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(localized)

    print("=== [3/4] Rebuilding XML Sitemap ===")
    rebuild_sitemap()
    print("=== [4/4] Multilingual Compilation Completed! ===")

if __name__ == "__main__":
    main()
