from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Создаём PDF
def create_checklist_pdf():
    filename = "assets/checklist-zemli-bulgaria.pdf"
    
    # Создаём документ
    doc = SimpleDocTemplate(filename, pagesize=A4,
                           topMargin=2*cm, bottomMargin=2*cm,
                           leftMargin=2*cm, rightMargin=2*cm)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Стили
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#191435',
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor='#191435',
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=13,
        textColor='#2a1f4d',
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#191435',
        spaceAfter=6,
        leading=14
    )
    
    # Заголовок
    story.append(Paragraph("Чек-лист покупки земли в Болгарии", title_style))
    story.append(Paragraph("от собственников", ParagraphStyle('subtitle', parent=styles['Normal'], fontSize=14, alignment=TA_CENTER, textColor='#64748b')))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Полное руководство от Devenvest", ParagraphStyle('brand', parent=styles['Normal'], fontSize=11, alignment=TA_CENTER, textColor='#BFAC8C', fontName='Helvetica-Bold')))
    story.append(Spacer(1, 1*cm))
    
    # ЭТАП 1
    story.append(Paragraph("ЭТАП 1: Поиск и первичный отбор участков", heading_style))
    
    story.append(Paragraph("✅ 1.1. Определение критериев", subheading_style))
    criteria = [
        "Цель покупки (инвестиции/строительство/сельхоз)",
        "Бюджет (включая резерв 15-20% на доп. расходы)",
        "Предпочитаемый регион и расстояние от моря/города",
        "Минимальная площадь участка",
        "Наличие коммуникаций или возможность подключения"
    ]
    for item in criteria:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 1.2. Источники поиска", subheading_style))
    sources = [
        "Официальные реестры: www.cadastre.bg",
        "Местные агентства недвижимости",
        "Прямые объявления от собственников",
        "Местные газеты и доски объявлений",
        "Рекомендации местных жителей"
    ]
    for item in sources:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 1.3. Первичный осмотр", subheading_style))
    inspection = [
        "Физический осмотр границ участка",
        "Фотофиксация со всех сторон",
        "Проверка доступа (дороги, проезд)",
        "Оценка рельефа и состояния земли",
        "Опрос соседей о проблемах района"
    ]
    for item in inspection:
        story.append(Paragraph(f"• {item}", body_style))
    
    # ЭТАП 2
    story.append(PageBreak())
    story.append(Paragraph("ЭТАП 2: Юридическая проверка", heading_style))
    
    story.append(Paragraph("✅ 2.1. Проверка документов собственника", subheading_style))
    docs = [
        "Акт за собственост (свидетельство о собственности)",
        "Удостоверение личности владельца",
        "Доверенность (если продаёт представитель)",
        "Подтверждение права наследования (если применимо)"
    ]
    for item in docs:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 2.2. Выписка из кадастра", subheading_style))
    cadastre = [
        "Запрос выписки через www.cadastre.bg (20 лв)",
        "Проверка площади, границ и кадастрового номера",
        "Сверка данных с реальными границами",
        "Проверка отсутствия обременений и арестов"
    ]
    for item in cadastre:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 2.3. Назначение земли", subheading_style))
    purpose = [
        "Категория: земеделска (сельхоз), горска (лесная), урбанизирана (городская)",
        "Проверка через общинский план (ОУП)",
        "Возможность изменения статуса",
        "Ограничения на строительство"
    ]
    for item in purpose:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 2.4. Обременения и долги", subheading_style))
    encumbrances = [
        "Ипотеки и залоги",
        "Судебные споры",
        "Долги по налогам",
        "Сервитуты (права проезда третьих лиц)",
        "Арендные обязательства"
    ]
    for item in encumbrances:
        story.append(Paragraph(f"• {item}", body_style))
    
    # ЭТАП 3
    story.append(PageBreak())
    story.append(Paragraph("ЭТАП 3: Техническая проверка", heading_style))
    
    story.append(Paragraph("✅ 3.1. Коммуникации", subheading_style))
    utilities = [
        "Электричество: наличие подключения или ближайшей точки",
        "Вода: центральное водоснабжение или скважина",
        "Канализация: центральная или септик",
        "Газ (если требуется)",
        "Интернет и мобильная связь"
    ]
    for item in utilities:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 3.2. Инфраструктура", subheading_style))
    infrastructure = [
        "Качество подъездных дорог (асфальт/грунт)",
        "Расстояние до ближайшего города/села",
        "Доступность магазинов, школ, больниц",
        "Общественный транспорт",
        "Безопасность района"
    ]
    for item in infrastructure:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 3.3. Геология и экология", subheading_style))
    geology = [
        "Тип почвы и её плодородность",
        "Уровень грунтовых вод",
        "Риск наводнений/оползней",
        "Близость к промышленным объектам",
        "Экологическая чистота района"
    ]
    for item in geology:
        story.append(Paragraph(f"• {item}", body_style))
    
    # ЭТАП 4
    story.append(PageBreak())
    story.append(Paragraph("ЭТАП 4: Оценка стоимости", heading_style))
    
    story.append(Paragraph("✅ 4.1. Рыночный анализ", subheading_style))
    market = [
        "Средняя цена за кв.м в районе",
        "Сравнение с аналогичными участками",
        "Динамика цен за последний год",
        "Факторы влияющие на стоимость"
    ]
    for item in market:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 4.2. Независимая оценка", subheading_style))
    valuation = [
        "Заказ оценки у лицензированного оценщика (200-500 лв)",
        "Проверка справедливости цены продавца",
        "Учёт затрат на подключение коммуникаций",
        "Потенциал роста стоимости"
    ]
    for item in valuation:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 4.3. Скрытые расходы", subheading_style))
    costs = [
        "Налог на покупку (около 3%)",
        "Нотариальные услуги (1-3% от суммы)",
        "Юридическое сопровождение (500-1500 лв)",
        "Перевод документов (если требуется)",
        "Страхование сделки"
    ]
    for item in costs:
        story.append(Paragraph(f"• {item}", body_style))
    
    # ЭТАП 5
    story.append(PageBreak())
    story.append(Paragraph("ЭТАП 5: Переговоры и сделка", heading_style))
    
    story.append(Paragraph("✅ 5.1. Подготовка к переговорам", subheading_style))
    negotiation = [
        "Определение целевой цены и максимума",
        "Аргументы для снижения цены",
        "Условия оплаты (предоплата, рассрочка)",
        "Сроки оформления сделки"
    ]
    for item in negotiation:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 5.2. Предварительный договор", subheading_style))
    preliminary = [
        "Задаток (обычно 10-15%)",
        "Условия расторжения",
        "Сроки завершения сделки",
        "Ответственность сторон"
    ]
    for item in preliminary:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 5.3. Оформление сделки", subheading_style))
    deal = [
        "Подписание договора купли-продажи у нотариуса",
        "Полная оплата (обычно через банк)",
        "Регистрация в Агентстве по кадастру (7-14 дней)",
        "Получение акта за собственост"
    ]
    for item in deal:
        story.append(Paragraph(f"• {item}", body_style))
    
    # ЭТАП 6
    story.append(PageBreak())
    story.append(Paragraph("ЭТАП 6: После покупки", heading_style))
    
    story.append(Paragraph("✅ 6.1. Регистрация", subheading_style))
    registration = [
        "Получение свидетельства о собственности",
        "Регистрация в налоговой (в течение 14 дней)",
        "Оформление страховки (опционально)"
    ]
    for item in registration:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 6.2. Налоги", subheading_style))
    taxes = [
        "Годовой налог на недвижимость (0.01-0.45% от кадастровой стоимости)",
        "Налог на прибыль при продаже (10% если продано в течение 3 лет)",
        "Подача налоговой декларации (до 30 апреля)"
    ]
    for item in taxes:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Paragraph("✅ 6.3. Дальнейшие действия", subheading_style))
    actions = [
        "Обозначение границ участка (межевание)",
        "Подключение коммуникаций",
        "Получение разрешений на строительство (если планируется)",
        "Регулярное обслуживание участка"
    ]
    for item in actions:
        story.append(Paragraph(f"• {item}", body_style))
    
    # Красные флаги
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("⚠️ КРАСНЫЕ ФЛАГИ - когда стоит отказаться:", heading_style))
    red_flags = [
        "Продавец избегает предоставления документов",
        "Цена значительно ниже рыночной без объяснений",
        "Обнаружены обременения или судебные споры",
        "Несоответствие данных кадастра и реальных границ",
        "Отсутствие доступа к участку",
        "Участок в зоне оползней/наводнений",
        "Невозможность подключения коммуникаций",
        "Продавец требует срочную сделку без проверок"
    ]
    for item in red_flags:
        story.append(Paragraph(f"❌ {item}", body_style))
    
    # Контакты
    story.append(PageBreak())
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("📞 Нужна помощь с покупкой земли?", title_style))
    story.append(Spacer(1, 0.5*cm))
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=8
    )
    
    story.append(Paragraph("<b>DEVENVEST</b> - профессиональное сопровождение сделок", contact_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("📧 Email: contact@devenvest.com", contact_style))
    story.append(Paragraph("💬 Telegram: @Alejandrov2000", contact_style))
    story.append(Paragraph("🌐 Сайт: devenvest.com", contact_style))
    
    story.append(Spacer(1, 1*cm))
    
    services_title = ParagraphStyle(
        'ServicesTitle',
        parent=styles['Normal'],
        fontSize=14,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=12,
        textColor='#191435'
    )
    story.append(Paragraph("Мы предоставляем:", services_title))
    
    services = [
        "✓ Полную юридическую проверку объектов",
        "✓ Независимую оценку участков",
        "✓ Сопровождение сделки от А до Я",
        "✓ Помощь в переговорах с продавцами",
        "✓ Консультации по инвестициям в недвижимость"
    ]
    for item in services:
        story.append(Paragraph(item, contact_style))
    
    # Генерируем PDF
    doc.build(story)
    print(f"✅ PDF успешно создан: {filename}")
    return filename

if __name__ == "__main__":
    try:
        pdf_file = create_checklist_pdf()
        print(f"Файл сохранён: {os.path.abspath(pdf_file)}")
    except Exception as e:
        print(f"Ошибка: {e}")
        print("Установите библиотеку: pip install reportlab")
