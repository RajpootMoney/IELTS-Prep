import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Color Palette
PRIMARY = colors.HexColor("#1A365D")    # Dark Navy
SECONDARY = colors.HexColor("#2B6CB0")  # Slate Blue
ACCENT = colors.HexColor("#2C7A7B")     # Teal
DARK_TEXT = colors.HexColor("#2D3748")  # Charcoal
LIGHT_BG = colors.HexColor("#F7FAFC")   # Soft Off-white
BORDER_COL = colors.HexColor("#CBD5E0") # Border Gray
GREEN_COL = colors.HexColor("#276749")  # Forest Green
RED_COL = colors.HexColor("#9B2C2C")    # Crimson

def get_custom_styles():
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=PRIMARY,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=SECONDARY,
        spaceAfter=10
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=PRIMARY,
        spaceBefore=10,
        spaceAfter=6
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=SECONDARY,
        spaceBefore=6,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=DARK_TEXT,
        spaceAfter=4
    )
    
    bold_body = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    instruction_style = ParagraphStyle(
        'Instruction',
        parent=body_style,
        fontName='Helvetica-Oblique',
        textColor=colors.HexColor("#4A5568")
    )
    
    box_style = ParagraphStyle(
        'BoxText',
        parent=body_style,
        fontSize=8.5,
        leading=12
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'h1': h1_style,
        'h2': h2_style,
        'body': body_style,
        'bold': bold_body,
        'instruction': instruction_style,
        'box': box_style
    }

def create_box_table(content_list, bg_color=LIGHT_BG, border_color=BORDER_COL, width=540):
    flowables = []
    for item in content_list:
        flowables.append(item)
    t = Table([[flowables]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

# Day Metadata & Specific Content Definitions
def get_day_data(day_num):
    data = {
        1: {
            "title": "Day 01: Initial Comprehensive Diagnostic Assessment",
            "focus": "Baseline calibration across Listening, Reading, Writing, and Speaking",
            "time_reg": "90 Minutes",
            "time_busy": "45 Minutes (Listening + Strategy priority)",
            "listening_title": "Listening Diagnostic (10 Questions)",
            "listening_audio": "audio_track.wav (Tracks 1 & 2)",
            "listening_instructions": "Questions 1-5: Write NO MORE THAN TWO WORDS AND/OR A NUMBER. Questions 6-10: Write NO MORE THAN ONE WORD.",
            "listening_questions": [
                ("1", "Full Name: Julian ____________"),
                ("2", "Contact Mobile: ____________"),
                ("3", "Chosen Study Day: ____________ evening"),
                ("4", "Course Commences On: ____________"),
                ("5", "Discounted Tuition Fee: £ ____________"),
                ("6", "Traditional grids suffer from high transmission ____________ over distances."),
                ("7", "Microgrids generate clean power predominantly through rooftop ____________ panels."),
                ("8", "Surplus power during daylight is captured inside centralized ____________ units."),
                ("9", "The greatest barrier to city adoption is the high ____________ expenditure."),
                ("10", "Municipalities must modernize outdated ____________ regulations.")
            ],
            "reading_title": "General Training Reading Diagnostic (10 Questions)",
            "reading_text_1": """<b>Section 1: City Central Library & Digital Hub Regulations</b><br/>
Membership to the Central Library is free of charge to all regional residents upon presenting valid proof of municipal address and photo identification. Non-residents may obtain an annual visitor pass for a nominal fee of $25.<br/>
Members are entitled to borrow up to ten physical volumes simultaneously for a standard loan period of three weeks. Audiobooks and digital multimedia items may be retained for fourteen days. Standard book loans may be renewed up to two consecutive times, provided no outstanding hold request has been lodged by another borrower.<br/>
The facility provides complimentary high-speed wireless connectivity throughout all indoor reading rooms and group study carrels; however, coverage does not extend to the outdoor garden terraces. Portable computer tablets are available for hire at the ground-floor helpdesk for use strictly on the premises and must be returned 30 minutes prior to closing time (8:00 PM on weekdays). Printing credits can be added online via the member portal or at the automated kiosk adjacent to the reception.""",
            "reading_q_1": [
                ("1", "Non-residents must pay an annual fee to borrow library materials. (TRUE / FALSE / NOT GIVEN)"),
                ("2", "Digital audiobooks may be borrowed for three consecutive weeks. (TRUE / FALSE / NOT GIVEN)"),
                ("3", "Free Wi-Fi is available in both indoor carrels and the library's outdoor terraces. (TRUE / FALSE / NOT GIVEN)"),
                ("4", "Borrowers can extend standard book loans for up to [ __________ ] additional times."),
                ("5", "Printing credit can be purchased at an automated [ __________ ] on the ground floor.")
            ],
            "reading_text_2": """<b>Section 2: Workplace Flexible Working & Core Hours Directive</b><br/>
Apex Global Logistics supports a hybrid working model to facilitate work-life equilibrium. Under this scheme, eligible full-time staff may request up to two remote working days per working week, subject to departmental head authorization.<br/>
All employees, regardless of location, must remain accessible and logged into corporate communication channels during designated 'core collaboration hours', which run from 10:00 AM to 3:00 PM daily. Outside these core hours, staff have the discretion to structure their remaining daily hours between 7:00 AM and 7:00 PM.<br/>
Prior to participating in external client conference calls from home, employees must ensure a professional, distraction-free environment and use noise-cancelling audio headsets. To maintain team alignment, fortnightly virtual check-ins are mandatory for all remote teams. Flexible work arrangements are evaluated on a quarterly basis and may be revoked if performance metrics decline.""",
            "reading_q_2": [
                ("6", "Staff are required to be available online between 10:00 AM and [ __________ ]."),
                ("7", "Employees may choose to work remotely for three days every week without approval. (TRUE / FALSE / NOT GIVEN)"),
                ("8", "Flexible arrangements can be cancelled if an employee's output drops. (TRUE / FALSE / NOT GIVEN)"),
                ("9", "Overtime worked during flexible hours is compensated at double pay. (TRUE / FALSE / NOT GIVEN)"),
                ("10", "Before client meetings, remote employees are required to equip themselves with [ __________ ] headsets.")
            ],
            "writing_task": """<b>Diagnostic Writing Tasks (Choose one or attempt both):</b><br/>
<b>Task 1 (General Training Letter — 150+ Words):</b><br/>
You recently attended a two-day professional project management conference. However, several scheduled seminars were cancelled, the audio-visual equipment failed repeatedly, and the catering was unacceptable.<br/>
Write a formal letter to the Conference Organizer. In your letter:<br/>
• Explain why you enrolled in the conference.<br/>
• Describe the specific shortcomings you experienced.<br/>
• State what compensation or action you expect from the organizers.<br/><br/>
<b>Task 2 (Essay — 250+ Words):</b><br/>
<i>Some people believe that working from home brings significant benefits to both employees and employers, while others argue that operating from a traditional workplace is far more advantageous. Discuss both views and give your own opinion.</i>""",
            "speaking_task": """<b>Diagnostic Speaking Interview:</b><br/>
• <b>Part 1:</b> 1. What is your current profession or field of study? 2. Why did you choose this career? 3. Do you plan to continue in this line of work in Canada? 4. What do you like most about your hometown?<br/>
• <b>Part 2 (Cue Card):</b> Describe a complex problem you had to solve at work or in your daily life. You should say: what the problem was, how you analyzed it, what action you took, and explain how you felt once it was resolved.<br/>
• <b>Part 3:</b> 1. Do you think machines and artificial intelligence will replace human decision-making in the workplace? 2. How can employers effectively reduce stress among their workforce?""",
            "strategy": """<b>Examiner Strategy: The 30-Second Pre-Listening Prediction Protocol</b><br/>
Never read questions passively before audio plays! For every blank, immediately identify the <b>Grammatical Form</b> (Noun, Date, Number, Adjective) and the <b>Contextual Category</b>.<br/>
<i>Example:</i> If preceded by 'at £', expect a price. If followed by a plural verb 'are', the missing word MUST be plural. Always check if you are writing words or numbers.""",
            "answers": {
                "L": [
                    ("1", "Bancroft", "Spelling: B-A-N-C-R-O-F-T. Julian Bancroft."),
                    ("2", "07892 441832", "Distractor: 07700 was his previous home phone; 07892 441832 is current mobile."),
                    ("3", "Tuesday", "Distractor: Hoped for Thursday, but work forced Tuesday."),
                    ("4", "14th November / 14 November / November 14", "Explicit date mentioned: 'begins on the 14th of November'."),
                    ("5", "420", "Distractor: Standard fee is £480; early registration discount price is £420."),
                    ("6", "loss / losses", "Audio: 'suffer from significant transmission loss'."),
                    ("7", "solar", "Audio: 'predominantly utilizing rooftop solar installations'."),
                    ("8", "battery", "Audio: 'integration of centralized battery storage facilities'."),
                    ("9", "capital", "Audio: 'greatest impediment is the initial capital expenditure'."),
                    ("10", "zoning", "Audio: 'must update outdated zoning regulations'.")
                ],
                "R": [
                    ("1", "TRUE", "Text: 'Non-residents may obtain an annual visitor pass for a nominal fee of $25.' Matches statement."),
                    ("2", "FALSE", "Text: 'Audiobooks and digital multimedia items may be retained for fourteen days.' 14 days = 2 weeks, not 3 weeks. Contradicts statement."),
                    ("3", "FALSE", "Text: 'coverage does not extend to the outdoor garden terraces.' Statement says it is available in both."),
                    ("4", "two / 2", "Text: 'may be renewed up to two consecutive times.'"),
                    ("5", "kiosk", "Text: 'at the automated kiosk adjacent to the reception.'"),
                    ("6", "3:00 PM / 3 pm", "Text: 'core collaboration hours, which run from 10:00 AM to 3:00 PM daily.'"),
                    ("7", "FALSE", "Text: 'may request up to two remote working days per working week, subject to departmental head authorization.' 3 days contradicts 'up to two', and approval is required."),
                    ("8", "TRUE", "Text: 'may be revoked if performance metrics decline.' 'Revoked' = cancelled, 'metrics decline' = output drops."),
                    ("9", "NOT GIVEN", "The text discusses flexible hours, but never mentions overtime pay rates or double pay."),
                    ("10", "noise-cancelling / noise cancelling", "Text: 'use noise-cancelling audio headsets.'")
                ],
                "writing_model": """<b>Band 8.5 Model Letter (Task 1 Formal):</b><br/>
Dear Sir or Madam,<br/><br/>
I am writing to formally express my profound disappointment regarding the Executive Project Management Conference held at your convention center on the 3rd and 4th of November, which I attended as a registered delegate.<br/><br/>
I enrolled in this seminar primarily to acquire advanced certifications in agile workflow optimization, as advertised extensively in your promotional brochure. Regrettably, the event failed to satisfy even basic professional standards. Firstly, two of the keynote speakers cancelled without prior notification or replacement. Furthermore, the multimedia projection equipment in Seminar Hall B malfunctioned repeatedly, causing an hour-long disruption. To compound matters, the luncheon provided was of substandard quality and failed to accommodate dietary requests.<br/><br/>
Given that the conference failed to deliver the curriculum promised, I request a 50% refund of my £650 registration fee, alongside formal written access to the digital workshop recordings.<br/><br/>
I anticipate your prompt resolution of this matter.<br/><br/>
Yours faithfully,<br/>
[Candidate Name]"""
            }
        },
        2: {
            "title": "Day 02: Listening Section 1 & GT Reading Section 1 Focus",
            "focus": "Form completion, spelling/number precision, and rapid advert scanning",
            "time_reg": "75 Minutes",
            "time_busy": "30 Minutes (Listening + Vocab)",
            "listening_title": "Listening Section 1: Storage Unit Rental Form",
            "listening_audio": "audio_track.wav",
            "listening_instructions": "Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
            "listening_questions": [
                ("1", "Customer Last Name: Vance (Spelled: ____________)"),
                ("2", "Postal Code: ____________"),
                ("3", "Unit Size Selected: ____________ square metres"),
                ("4", "Standard Weekly Rental Rate: £ ____________"),
                ("5", "Standard Insurance Value Included: up to £ ____________"),
                ("6", "Enhanced insurance cost per week: £ ____________"),
                ("7", "Scheduled Move-in Date: ____________"),
                ("8", "Access Gate Opens At: ____________ AM"),
                ("9", "Access Gate Closes At: ____________ PM"),
                ("10", "Provisional Security PIN Code: ____________")
            ],
            "reading_title": "GT Reading Section 1: Community Facility Notices",
            "reading_text_1": """<b>Notice A: Greenfield Community Allotments</b><br/>
Greenfield Council offers plots of land to local residents interested in growing organic vegetables and flowers. Standard plots measure 100 square metres and cost £60 annually. Water troughs are situated across the grounds; however, hosepipes connected directly to mains are strictly prohibited to prevent water wastage. Gardeners must maintain their plot in a tidy state and ensure weeds do not seed onto neighboring areas. A £30 refundable key deposit is mandatory upon signing the annual allotment lease.<br/>
<b>Notice B: Riverside Tool Sharing Cooperative</b><br/>
Why purchase expensive gardening equipment when you can borrow it? The Tool Cooperative operates every Saturday from 9:00 AM to 1:00 PM. Members pay a £20 annual subscription and enjoy free loans of hand tools, wheelbarrows, and hedge trimmers. Power tools incur a £5 maintenance charge per weekend. All borrowed items must be cleaned and returned by the following Friday afternoon.""",
            "reading_q_1": [
                ("1", "Greenfield allotment holders are allowed to use hosepipes attached to taps. (TRUE / FALSE / NOT GIVEN)"),
                ("2", "A deposit must be paid for the allotment key. (TRUE / FALSE / NOT GIVEN)"),
                ("3", "Greenfield plots are allocated on a first-come, first-served basis. (TRUE / FALSE / NOT GIVEN)"),
                ("4", "The Tool Cooperative is open to members on Sundays. (TRUE / FALSE / NOT GIVEN)"),
                ("5", "Borrowing motorized power tools involves a small additional fee. (TRUE / FALSE / NOT GIVEN)")
            ],
            "reading_text_2": """<b>Notice C: Westwood Sports Complex Pass Regulations</b><br/>
Westwood Leisure Centre offers multiple pass tiers for community members:<br/>
• Morning Pass (£25/month): Access to gym and swimming pool between 6:00 AM and 11:30 AM on weekdays only.<br/>
• Unlimited Pass (£45/month): Unrestricted entry seven days a week, plus free booking of squash courts.<br/>
Lockers operate using a £1 coin return mechanism. Lockers must be cleared every evening; padlocks left overnight will be clipped by security staff at 10:30 PM, and confiscated items stored at the lost property desk for 14 days.""",
            "reading_q_2": [
                ("6", "Morning pass holders may use the gym on Saturday mornings. (TRUE / FALSE / NOT GIVEN)"),
                ("7", "Unlimited pass holders have access to squash courts at no extra charge. (TRUE / FALSE / NOT GIVEN)"),
                ("8", "The cost of locker rental is £1 per week. (TRUE / FALSE / NOT GIVEN)"),
                ("9", "Unclaimed locker contents are retained by security for [ __________ ] days."),
                ("10", "Personal locks remaining overnight will be removed at [ __________ ] PM.")
            ],
            "writing_task": """<b>Task 1 Tone Drill:</b><br/>
Identify whether the following situations demand a FORMAL, SEMI-FORMAL, or INFORMAL letter, and write the opening sentence for each:<br/>
1. Writing to your apartment landlord regarding a leaking radiator in your living room.<br/>
2. Writing to an airline customer service manager requesting compensation for lost luggage.<br/>
3. Writing to a former coworker inviting them to your housewarming party.""",
            "speaking_task": """<b>Speaking Part 1 Drill (The 3-Sentence Extension Formula):</b><br/>
Answer each question using: 1. Direct answer, 2. Reason, 3. Example/Detail.<br/>
• Do you live in a house or an apartment?<br/>
• What is your favorite room in your home?<br/>
• How well do you know your neighbors?""",
            "strategy": """<b>Examiner Strategy: Recognizing Speaker Distractors</b><br/>
Speakers in Section 1 and 2 frequently state an incorrect fact first, then correct themselves.<br/>
<i>Pattern:</i> 'It is forty-five pounds... oh wait, that excludes tax, it is fifty-four.'<br/>
<i>Golden Rule:</i> Never commit to an answer until you hear the speaker confirm or move to the next item!""",
            "answers": {
                "L": [
                    ("1", "Vance", "Spelling provided: V-A-N-C-E."),
                    ("2", "SW4 9LH", "Postcode: Sierra Whiskey four, nine Lima Hotel."),
                    ("3", "25 / twenty-five", "Distractor: Manager suggests 35 sqm, but client insists 25 sqm is plenty."),
                    ("4", "45 / forty-five", "Standard weekly rate is £45."),
                    ("5", "5,000 / 5000", "Includes insurance up to £5,000."),
                    ("6", "8 / eight", "Enhanced cover is an extra £8/week."),
                    ("7", "18th November / 18 November / November 18", "Scheduled move-in date."),
                    ("8", "7:00 / 7:00 AM", "Gates open at 7:00 AM."),
                    ("9", "8:30 / 8:30 PM", "Gates close at 8:30 PM."),
                    ("10", "9420", "Provisional security code 9-4-2-0.")
                ],
                "R": [
                    ("1", "FALSE", "Text: 'hosepipes connected directly to mains are strictly prohibited'."),
                    ("2", "TRUE", "Text: 'A £30 refundable key deposit is mandatory'."),
                    ("3", "NOT GIVEN", "No mention of how plots are prioritized or allocated."),
                    ("4", "FALSE", "Text: 'The Tool Cooperative operates every Saturday... returned by the following Friday'. Not open Sunday."),
                    ("5", "TRUE", "Text: 'Power tools incur a £5 maintenance charge per weekend'."),
                    ("6", "FALSE", "Text: 'weekdays only' for Morning Pass."),
                    ("7", "TRUE", "Text: 'plus free booking of squash courts'."),
                    ("8", "FALSE", "Text: 'Lockers operate using a £1 coin return mechanism.' It is a refundable coin deposit, not a weekly fee."),
                    ("9", "14 / fourteen", "Text: 'stored at the lost property desk for 14 days'."),
                    ("10", "10:30", "Text: 'clipped by security staff at 10:30 PM'.")
                ],
                "writing_model": """<b>Tone & Opening Sentence Models:</b><br/>
1. <b>Semi-Formal (Landlord):</b> <i>Dear Mr. Henderson, I am writing to formally notify you of a maintenance defect regarding the central heating radiator in my living room.</i><br/>
2. <b>Formal (Airline Manager):</b> <i>Dear Sir or Madam, I am writing to lodge an official complaint and claim for compensation regarding baggage misplaced during flight AC842 from London to Toronto on the 12th of October.</i><br/>
3. <b>Informal (Former Colleague/Friend):</b> <i>Dear David, I hope you're doing well! I'm writing because I've finally settled into my new flat and would love for you to come over to my housewarming dinner next Saturday.</i>"""
            }
        },
        3: {
            "title": "Day 03: Section 2 Listening & GT Reading Section 2 Workplace Text",
            "focus": "Monologue distractors, workplace contracts, and Task 2 thesis statements",
            "time_reg": "80 Minutes",
            "time_busy": "30 Minutes (Workplace Reading + Vocab)",
            "listening_title": "Listening Section 2: Riverside Community Centre Tour",
            "listening_audio": "audio_track.wav",
            "listening_instructions": "Choose the correct letter A, B, or C, or complete sentences with NO MORE THAN TWO WORDS.",
            "listening_questions": [
                ("1", "The centre was closed for refurbishment for: A) 3 months, B) 6 months, C) 1 year"),
                ("2", "The renovated gymnasium now overlooks the: A) Car park, B) River, C) Botanical gardens"),
                ("3", "Adult lane swimming takes place between: A) 6:30 and 8:30 AM, B) 7:00 and 9:00 AM, C) 8:00 and 10:00 AM"),
                ("4", "The ground-floor creche facility operates on: A) Weekends only, B) Monday to Friday, C) Everyday"),
                ("5", "Bronze tier members can access facilities during: A) Peak hours, B) Off-peak hours, C) Weekends"),
                ("6", "Which tier includes free weekend fitness classes? A) Bronze, B) Silver, C) Gold"),
                ("7", "Annual members receive a free sports bag and a: [ __________ ]"),
                ("8", "Outdoor [ __________ ] is strictly forbidden in squash courts."),
                ("9", "The pool length is [ __________ ] metres."),
                ("10", "The eastern wing houses the [ __________ ] pool.")
            ],
            "reading_title": "GT Reading Section 2: Workplace Health, Safety & Annual Leave",
            "reading_text_1": """<b>Staff Policy Document: Annual Leave & Sickness Absence Protocol</b><br/>
1. Annual Leave Entitlement:<br/>
Permanent salaried staff are entitled to 28 days of paid annual leave per fiscal year, inclusive of the eight recognized statutory bank holidays. Leave entitlement accrues on a pro-rata basis from the initial start date of employment. Employees must submit holiday requests via the employee intranet at least two weeks in advance for absences spanning three or more consecutive working days. During the busy fourth quarter (October to December), a maximum of two team members per department may take leave concurrently.<br/>
2. Sickness Notification Procedure:<br/>
In the event of unanticipated illness, staff must telephone their immediate line supervisor by 8:30 AM on the first day of absence. Text messages or emails are deemed unacceptable methods of initial notification. If illness persists for up to seven consecutive calendar days, employees must complete a Self-Certification Sickness Form upon returning to the office. For absences exceeding seven consecutive days, a formal 'Fit Note' signed by a registered medical practitioner is legally mandated.""",
            "reading_q_1": [
                ("1", "The 28 days of annual leave does not include statutory bank holidays. (TRUE / FALSE / NOT GIVEN)"),
                ("2", "Employees wishing to take five days of leave must apply at least two weeks beforehand. (TRUE / FALSE / NOT GIVEN)"),
                ("3", "During November, up to four staff members from one department may take leave together. (TRUE / FALSE / NOT GIVEN)"),
                ("4", "Staff may notify their supervisor of illness via a text message if sent before 8:30 AM. (TRUE / FALSE / NOT GIVEN)"),
                ("5", "A medical doctor's note is required if an employee is absent due to illness for six days. (TRUE / FALSE / NOT GIVEN)")
            ],
            "reading_text_2": """<b>Section 2B: Display Screen Equipment (DSE) Regulations</b><br/>
Under the Health and Safety (Display Screen Equipment) Regulations, the company is obligated to conduct workstation ergonomic assessments for all employees who habitually use visual monitors for significant portions of the workday. The company covers the full cost of an annual optical examination for qualifying computer users. Furthermore, where an optician prescribes corrective lenses specifically and exclusively for VDU/computer operation, the organization will reimburse up to £75 toward the cost of basic spectacle frames.""",
            "reading_q_2": [
                ("6", "The company pays for an annual eye test for regular display screen users. (TRUE / FALSE / NOT GIVEN)"),
                ("7", "Workers can receive up to £75 reimbursement for any kind of designer sunglasses. (TRUE / FALSE / NOT GIVEN)"),
                ("8", "Workstation ergonomic evaluations are performed [ __________ ] for every computer operator."),
                ("9", "Corrective lenses must be prescribed exclusively for [ __________ ] use to be reimbursed."),
                ("10", "Reimbursement applies toward basic [ __________ ] up to the £75 limit.")
            ],
            "writing_task": """<b>Task 2 Introduction & Thesis Formula:</b><br/>
Learn the 2-Sentence Introduction blueprint: Sentence 1: Paraphrase topic; Sentence 2: Clear thesis.<br/>
<i>Prompt:</i> Some people believe that governments should spend money on public railways rather than building new roads. To what extent do you agree or disagree?<br/>
Write an introduction satisfying Band 7+ criteria with a definitive position.""",
            "speaking_task": """<b>Speaking Part 1 Fluency Extension:</b><br/>
Topic: Hobbies & Leisure Time.<br/>
1. What do you enjoy doing in your spare time?<br/>
2. Did you have a different hobby when you were a child?<br/>
3. Do you prefer indoor or outdoor activities? Why?""",
            "strategy": """<b>Examiner Strategy: The True vs False vs Not Given Triad Rule</b><br/>
• <b>TRUE:</b> Explicitly confirmed by synonyms.<br/>
• <b>FALSE:</b> Text directly contradicts the prompt statement (makes it impossible).<br/>
• <b>NOT GIVEN:</b> Text does not provide enough information. Never assume something is true just because it sounds normal in daily life!""",
            "answers": {
                "L": [
                    ("1", "B", "Audio: 'following six months of extensive refurbishment'."),
                    ("2", "C", "Audio: 'now overlooks the outdoor botanical gardens rather than the car park'."),
                    ("3", "A", "Audio: 'between 6:30 and 8:30 AM every weekday'."),
                    ("4", "B", "Audio: 'operates Monday to Friday, from 9:00 AM until 1:00 PM'."),
                    ("5", "B", "Audio: 'Bronze tier offers access... only during off-peak hours'."),
                    ("6", "C", "Audio: 'Gold package, which additionally grants complimentary access to all weekend fitness classes'."),
                    ("7", "water bottle", "Audio: 'complimentary sports bag and a water bottle'."),
                    ("8", "footwear", "Audio: 'outdoor footwear is strictly prohibited'."),
                    ("9", "25 / twenty-five", "Audio: 'twenty-five metre heated swimming pool'."),
                    ("10", "heated / swimming", "Audio: 'eastern wing is our twenty-five metre heated swimming pool'.")
                ],
                "R": [
                    ("1", "FALSE", "Text: 'inclusive of the eight recognized statutory bank holidays'."),
                    ("2", "TRUE", "Text: 'at least two weeks in advance for absences spanning three or more consecutive working days'."),
                    ("3", "FALSE", "Text: 'a maximum of two team members per department may take leave concurrently'."),
                    ("4", "FALSE", "Text: 'must telephone... Text messages or emails are deemed unacceptable'."),
                    ("5", "FALSE", "Text: 'exceeding seven consecutive days... doctor note mandated'. For 6 days, self-certification is used."),
                    ("6", "TRUE", "Text: 'covers the full cost of an annual optical examination'."),
                    ("7", "FALSE", "Text: 'specifically and exclusively for VDU/computer operation... basic spectacle frames'. Not sunglasses."),
                    ("8", "ergonomic", "Text: 'conduct workstation ergonomic assessments'."),
                    ("9", "VDU / computer", "Text: 'prescribes corrective lenses specifically and exclusively for VDU/computer operation'."),
                    ("10", "spectacle frames / frames", "Text: 'toward the cost of basic spectacle frames'.")
                ],
                "writing_model": """<b>Band 8.0 Task 2 Introduction Model:</b><br/>
It is frequently argued that state funding should be allocated towards modernizing railway infrastructure instead of constructing additional motorway networks. I completely agree with this view because expanded rail transport drastically curtails vehicular carbon emissions and provides a more cost-effective long-term solution for intercity passenger transit."""
            }
        },
        4: {
            "title": "Day 04: Section 3 Multi-Speaker Dynamics & GT Reading Headings",
            "focus": "Multi-speaker dialogue, academic projects, and matching paragraph headings",
            "time_reg": "85 Minutes",
            "time_busy": "30 Minutes (Reading Headings + Vocab)",
            "listening_title": "Listening Section 3: Retail Marketing Research Project",
            "listening_audio": "audio_track.wav",
            "listening_instructions": "Answer Questions 1-10 with NO MORE THAN TWO WORDS AND/OR A NUMBER.",
            "listening_questions": [
                ("1", "Initial survey sample size: ____________ shoppers"),
                ("2", "Originally predicted top impulse item: confectionary and ____________"),
                ("3", "Over 60% of unplanned purchases were actually household ____________"),
                ("4", "Shopper navigation tracking methodology used: observational ____________"),
                ("5", "Duration of observational tracking: ____________ days"),
                ("6", "Primary ethical requirement: customer identities had to be ____________"),
                ("7", "Medium used for recording observations: ____________ recordings"),
                ("8", "Where statistical analysis must be located in report: ____________ section"),
                ("9", "Section where stats should NOT be relegated: the ____________"),
                ("10", "Project topic: retail ____________ in supermarkets")
            ],
            "reading_title": "GT Reading Section 3: The Evolution of Modern Office Design",
            "reading_text_1": """<b>Paragraph A:</b> For much of the twentieth century, white-collar workplace architecture was dominated by cellular layouts. Individual offices with solid walls and closed doors were considered the hallmark of professional status and focused intellect. Acoustic privacy was prioritized above all else, ensuring that managerial deliberation occurred in seclusion while junior clerks performed repetitive accounting in separate typing pools.<br/>
<b>Paragraph B:</b> The 1960s witnessed the inception of the open-plan office, originally conceived in Germany as 'Bürolandschaft' (office landscape). Proponents contended that dismantling physical partitions would democratize corporate hierarchies, inspire organic interaction, and dramatically curtail construction and maintenance costs. By the late 1990s, cubicle grids and open desks had become the ubiquitous standard across global corporate headquarters.<br/>
<b>Paragraph C:</b> In recent years, however, extensive empirical research has revealed the unintended shortcomings of open-plan workspaces. Far from fostering seamless collaboration, open designs frequently induce cognitive exhaustion and heightened anxiety. Constant acoustic interruptions—ringing telephones, conversational chatter, and mechanical hums—severely diminish employee attention spans. Studies demonstrate that face-to-face interactions actually decreased by roughly 70% in open environments, as workers retreated into noise-cancelling headphones and internal messaging software.<br/>
<b>Paragraph D:</b> In response to these shortcomings, modern architects are championing 'activity-based working' (ABW). Rather than assigning fixed desks, the contemporary workplace is segregated into modular zones tailored to distinct occupational functions. Quiet focus pods provide acoustic isolation for intensive cognitive tasks, communal lounges facilitate spontaneous brainstorming, and soundproofed booths accommodate virtual teleconferencing. This hybrid architectural paradigm acknowledges that workplace productivity demands a dynamic equilibrium between solitude and social synergy.""",
            "reading_q_1": [
                ("1", "Match Heading for Paragraph A: (Choose: i. Financial drawbacks of partitions / ii. The cellular status era / iii. The rise of hybrid layouts)"),
                ("2", "Match Heading for Paragraph B: (Choose: iv. The democratic promise of open plans / v. Acoustic engineering solutions)"),
                ("3", "Match Heading for Paragraph C: (Choose: vi. Counterproductive consequences of openness / vii. Telecommuting trends)"),
                ("4", "Match Heading for Paragraph D: (Choose: viii. Activity-based zoning for modern balance / ix. Eliminating shared spaces)"),
                ("5", "Face-to-face interaction in open-plan offices dropped by approximately [ __________ ] percent.")
            ],
            "reading_text_2": """<b>Questions 6-10: Sentence Completion:</b><br/>
• Early cellular offices valued acoustic [ 6. __________ ] above other architectural features.<br/>
• The open-plan concept was originally developed in [ 7. __________ ].<br/>
• Employees in noisy open environments often cope by wearing [ 8. __________ ] headphones.<br/>
• Under activity-based working, employees do not have [ 9. __________ ] desks.<br/>
• Quiet focus pods are specifically designed to provide acoustic [ 10. __________ ].""",
            "reading_q_2": [
                ("6", "Complete Question 6"),
                ("7", "Complete Question 7"),
                ("8", "Complete Question 8"),
                ("9", "Complete Question 9"),
                ("10", "Complete Question 10")
            ],
            "writing_task": """<b>Task 1 Bullet Point Balancing Drill:</b><br/>
<i>Prompt:</i> You have rented a flat through an estate agent, but upon moving in, you discovered multiple issues. Write a letter to the agency manager.<br/>
• Explain the terms of your rental agreement.<br/>
• Describe the specific defects found in the property.<br/>
• Outline what corrective steps you require within 48 hours.<br/>
Write an outline showing how you balance all 3 bullet points with 2 specific details each.""",
            "speaking_task": """<b>Speaking Part 2 (Cue Card Practice — 2 Minutes):</b><br/>
Describe an educational course or training program that you found particularly useful.<br/>
You should say:<br/>
• What the course was and where you took it<br/>
• What skills or knowledge you acquired<br/>
• How the teacher or instructor delivered the content<br/>
• And explain why this course was beneficial to your career.""",
            "strategy": """<b>Examiner Strategy: Matching Headings Without Reading Every Word</b><br/>
Do not read the whole paragraph 3 times! Read sentences 1-2 to identify the topic sentence, scan the final sentence for conclusions, and ask: <i>What is the main point?</i> Eliminate headings that only capture one minor detail.""",
            "answers": {
                "L": [
                    ("1", "200 / two hundred", "Audio: 'data from two hundred shoppers'."),
                    ("2", "snacks", "Audio: 'confectionary and snacks'."),
                    ("3", "toiletries", "Audio: 'unplanned basket additions were actually discounted household toiletries'."),
                    ("4", "heat-mapping / heat mapping", "Audio: 'observational heat-mapping over a three-day period'."),
                    ("5", "3 / three", "Audio: 'over a three-day period'."),
                    ("6", "anonymized / anonymous", "Audio: 'individual customer identities were completely anonymized'."),
                    ("7", "video", "Audio: 'in our video recordings'."),
                    ("8", "discussion", "Audio: 'integrated directly into your discussion section'."),
                    ("9", "appendix", "Audio: 'rather than relegated to an appendix'."),
                    ("10", "psychology", "Audio: 'supermarket retail psychology'.")
                ],
                "R": [
                    ("1", "ii. The cellular status era", "Paragraph A focuses on cellular offices as status symbols and acoustic privacy."),
                    ("2", "iv. The democratic promise of open plans", "Paragraph B explains how open plan promised to democratize hierarchy and cut costs."),
                    ("3", "vi. Counterproductive consequences of openness", "Paragraph C details the fatigue, anxiety, and 70% drop in interaction."),
                    ("4", "viii. Activity-based zoning for modern balance", "Paragraph D explains modular zones (ABW) balancing solitude and synergy."),
                    ("5", "70 / seventy", "Text: 'decreased by roughly 70% in open environments'."),
                    ("6", "privacy", "Text: 'Acoustic privacy was prioritized above all else'."),
                    ("7", "Germany", "Text: 'originally conceived in Germany'."),
                    ("8", "noise-cancelling / noise cancelling", "Text: 'retreated into noise-cancelling headphones'."),
                    ("9", "fixed", "Text: 'Rather than assigning fixed desks'."),
                    ("10", "isolation", "Text: 'provide acoustic isolation for intensive cognitive tasks'.")
                ],
                "writing_model": """<b>Task 1 Balanced Bullet Point Blueprint:</b><br/>
• <b>Bullet 1 (Agreement terms):</b> Signed 12-month lease on 1st Nov for Apartment 4B; agreed fully-furnished with working appliances and professional cleaning.<br/>
• <b>Bullet 2 (Defects found):</b> Washing machine fails to drain during cycle; master bedroom window latch broken preventing secure locking.<br/>
• <b>Bullet 3 (Action within 48h):</b> Dispatch a licensed technician to repair appliance by Thursday; replace window lock to ensure tenant security, or deduct repair costs from next month's rent."""
            }
        },
        5: {
            "title": "Day 05: Section 4 Monologue Mastery & Body Paragraph Architecture",
            "focus": "Academic monologues, signposting cues, and the PEEL paragraph formula",
            "time_reg": "85 Minutes",
            "time_busy": "35 Minutes (Listening Section 4 + Strategy)",
            "listening_title": "Listening Section 4: Coral Reef Restoration Engineering",
            "listening_audio": "audio_track.wav",
            "listening_instructions": "Complete the notes below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
            "listening_questions": [
                ("1", "Coral reefs cover under [ 1. __________ ] percent of ocean floor."),
                ("2", "They provide a habitat for over [ 2. __________ ] percent of marine life."),
                ("3", "Primary stress factor: rising sea surface [ 3. __________ ]."),
                ("4", "Corals expel symbiotic [ 4. __________ ] during temperature spikes."),
                ("5", "Loss of algae deprives corals of their color and primary source of [ 5. __________ ]."),
                ("6", "Historic artificial reefs used old ships or [ 6. __________ ] blocks."),
                ("7", "Modern projects utilize advanced [ 7. __________ ] matrices."),
                ("8", "Intricate micro-crevices are manufactured using [ 8. __________ ] technology."),
                ("9", "Micro-crevices protect juvenile fish from apex [ 9. __________ ]."),
                ("10", "Fish biodiversity rose by 40% in [ 10. __________ ] months in Caribbean trials.")
            ],
            "reading_title": "GT Reading Section 2: Workplace Ergonomics & Training Policy",
            "reading_text_1": """<b>Corporate Training & Professional Development Policy</b><br/>
BrightPath Financial actively fosters internal talent advancement through our Continuing Professional Development (CPD) programme. All permanent staff members who have concluded their six-month probationary period are eligible to apply for an annual professional educational subsidy of up to $2,500.<br/>
Qualifying programs must align directly with the employee's current occupational role or clear career trajectory within the corporate hierarchy. Approved courses include accredited industry certifications, university extension modules, and specialized data analysis bootcamps. Self-directed recreational courses (e.g. general language studies not required for business operations) do not qualify for company funding.<br/>
To receive reimbursement, candidates must submit a formal Learning Agreement endorsed by their department manager prior to course enrollment. Tuition fees are reimbursed in two equal tranches: 50% upon verified enrollment, and the remaining 50% upon presenting an official transcript demonstrating a passing grade. If an employee resigns within twelve months of receiving funding, the subsidy must be repaid in full.""",
            "reading_q_1": [
                ("1", "Probationary employees are immediately eligible for the $2,500 education subsidy. (TRUE / FALSE / NOT GIVEN)"),
                ("2", "Employees may use the subsidy to take conversational Italian courses for leisure. (TRUE / FALSE / NOT GIVEN)"),
                ("3", "Tuition reimbursement is disbursed in two separate stages. (TRUE / FALSE / NOT GIVEN)"),
                ("4", "Workers who leave the company ten months after course completion must return the funds. (TRUE / FALSE / NOT GIVEN)"),
                ("5", "The educational subsidy increases to $3,500 after five years of service. (TRUE / FALSE / NOT GIVEN)")
            ],
            "reading_text_2": """<b>Summary Completion: Questions 6-10:</b><br/>
Employees must conclude their [ 6. __________ ] before applying for financial support. The maximum annual grant available is [ 7. $__________ ]. Prior to enrolling, staff must submit a formal [ 8. __________ ] signed by their supervisor. The final reimbursement payment requires proof of a [ 9. __________ ] grade. If a worker resigns within [ 10. __________ ] months, they must repay the entire amount.""",
            "reading_q_2": [
                ("6", "Complete Question 6"),
                ("7", "Complete Question 7"),
                ("8", "Complete Question 8"),
                ("9", "Complete Question 9"),
                ("10", "Complete Question 10")
            ],
            "writing_task": """<b>Task 2 PEEL Body Paragraph Construction:</b><br/>
Construct one Band 7+ Body Paragraph responding to the following essay prompt:<br/>
<i>Prompt: Some people believe that governments should impose heavy taxes on junk food to encourage healthy eating. To what extent do you agree or disagree?</i><br/>
Follow the PEEL blueprint: Point (Topic sentence), Explanation, Example, Link.""",
            "speaking_task": """<b>Speaking Part 2 (The 1-Minute Note-Taking Grid):</b><br/>
Topic: Describe an environmental problem in your home city.<br/>
Use the 4-quadrant note grid during your 60-second prep:<br/>
[ What is the problem? ] | [ What causes it? ]<br/>
[ How does it impact people? ] | [ How can it be mitigated? ]""",
            "strategy": """<b>Examiner Strategy: Section 4 Monologue Survival</b><br/>
Lecturers speak continuously. If you miss Question 34, do NOT dwell on it! The lecturer is already speaking towards Question 35. Read ahead, look for transition signposts ('Moving on to...', 'In addition...'), and keep moving.""",
            "answers": {
                "L": [
                    ("1", "1 / one", "Audio: 'occupy less than one percent of the ocean floor'."),
                    ("2", "25 / twenty-five", "Audio: 'sustain more than twenty-five percent of all marine species'."),
                    ("3", "temperatures", "Audio: 'primarily driven by rising sea surface temperatures'."),
                    ("4", "algae", "Audio: 'expel the symbiotic algae residing in their tissues'."),
                    ("5", "nutrition", "Audio: 'their primary source of nutrition'."),
                    ("6", "concrete", "Audio: 'decommissioned steel ships or concrete blocks'."),
                    ("7", "ceramic", "Audio: 'utilize advanced ceramic matrices'."),
                    ("8", "3D printing / 3-D printing", "Audio: 'incorporating three-dimensional printing technology'."),
                    ("9", "predators", "Audio: 'protecting them from apex predators'."),
                    ("10", "12 / twelve", "Audio: 'within just twelve months'.")
                ],
                "R": [
                    ("1", "FALSE", "Text: 'All permanent staff members who have concluded their six-month probationary period are eligible'. Probationary staff cannot apply."),
                    ("2", "FALSE", "Text: 'Self-directed recreational courses... do not qualify for company funding'."),
                    ("3", "TRUE", "Text: 'reimbursed in two equal tranches: 50% upon enrollment, 50% upon transcript'."),
                    ("4", "TRUE", "Text: 'If an employee resigns within twelve months... must be repaid in full.' 10 months is within 12 months."),
                    ("5", "NOT GIVEN", "The text mentions a $2,500 limit, but does not discuss whether it increases after 5 years."),
                    ("6", "probationary period", "Text: 'concluded their six-month probationary period'."),
                    ("7", "2,500 / 2500", "Text: 'subsidy of up to $2,500'."),
                    ("8", "Learning Agreement", "Text: 'submit a formal Learning Agreement'."),
                    ("9", "passing", "Text: 'transcript demonstrating a passing grade'."),
                    ("10", "12 / twelve", "Text: 'within twelve months of receiving funding'.")
                ],
                "writing_model": """<b>Band 8.5 PEEL Body Paragraph Model:</b><br/>
<b>(Point)</b> Imposing substantial levies on ultra-processed and sugary foods provides a potent financial deterrent that curbs harmful consumption patterns. <b>(Explanation)</b> Because consumer purchasing decisions are predominantly price-sensitive, inflating the retail cost of junk food encourages shoppers to substitute high-calorie processed items with nutritious whole foods such as vegetables and grains. <b>(Example)</b> For instance, when Mexico introduced an excise tax on sugary beverages in 2014, national soda purchases dropped by nearly ten percent within two years, while water consumption rose commensurately. <b>(Link)</b> Consequently, fiscal taxation serves as an efficacious mechanism to mitigate national obesity rates and reduce long-term healthcare expenditure."""
            }
        },
        6: {
            "title": "Day 06: Synonyms, Paraphrases & Counter-Arguments",
            "focus": "Synonym mapping, general interest reading passages, and Task 2 nuance",
            "time_reg": "85 Minutes",
            "time_busy": "30 Minutes (Reading Passage + Vocab)",
            "listening_title": "Listening Masterclass: Paraphrase Decryption (Vertical Farming)",
            "listening_audio": "audio_track.wav",
            "listening_instructions": "Answer Questions 1-10 with NO MORE THAN TWO WORDS AND/OR A NUMBER.",
            "listening_questions": [
                ("1", "Conventional agriculture is constrained by shortages of arable land and [ 1. __________ ]."),
                ("2", "Vertical crops are grown inside [ 2. __________ ] buildings."),
                ("3", "Closed-loop aeroponic systems reduce water consumption by up to [ 3. __________ ] percent."),
                ("4", "Indoor crop production remains steady across all four [ 4. __________ ]."),
                ("5", "A major ecological benefit is eliminating runoff from agricultural [ 5. __________ ]."),
                ("6", "Indoor farms consume massive amounts of [ 6. __________ ] energy for lighting."),
                ("7", "Artificial lighting is provided by [ 7. __________ ] grids."),
                ("8", "Without green power, vertical farming's [ 8. __________ ] footprint can exceed soil farming."),
                ("9", "Future profitability depends on improvements in lighting and automated [ 9. __________ ] tools."),
                ("10", "Cultivation occurs in vertically [ 10. __________ ] layers.")
            ],
            "reading_title": "GT Reading Section 3: The Psychology of Urban Commuting",
            "reading_text_1": """<b>The Psychological Toll of the Daily Transit Grind</b><br/>
For millions of urban professionals, the morning commute is an unavoidable daily ritual. However, behavioural psychologists increasingly view commuting not merely as dead transit time, but as one of the single most detrimental activities affecting subjective human happiness. Clinical research conducted across major metropolitan centers consistently links prolonged commutes with elevated cortisol production, chronic musculoskeletal tension, and acute feelings of helplessness.<br/>
The fundamental determinant of commute-induced stress is not geographical distance, but unpredictable variance. When commuters embark on a journey with a predictable 45-minute duration, cognitive stress remains moderate because individuals psychologically budget for the duration. Conversely, when transit systems are prone to erratic signal failures or vehicular gridlock, commuters experience acute loss of control. It is this perception of helplessness, rather than transit duration alone, that triggers somatic stress reactions.<br/>
Interestingly, active commuting—such as cycling or brisk walking—exerts the diametric opposite effect on psychological well-being. Individuals who walk or cycle to work report feelings of alertness, autonomy, and elevated vitality. Even individuals who utilize public transit report higher life satisfaction than solo car drivers, primarily because rail passengers can reclaim their travel time for passive recreation, reading, or mindfulness, whereas drivers must maintain uninterrupted, vigilance-demanding visual focus.""",
            "reading_q_1": [
                ("1", "Long commutes are identified as a major cause of increased cortisol and physical stress. (TRUE / FALSE / NOT GIVEN)"),
                ("2", "Geographical distance is a bigger source of commuter stress than unpredictable travel delays. (TRUE / FALSE / NOT GIVEN)"),
                ("3", "Commuters experience lower stress when their trip length is consistent and expected. (TRUE / FALSE / NOT GIVEN)"),
                ("4", "Solo car drivers experience less psychological strain than passengers on suburban trains. (TRUE / FALSE / NOT GIVEN)"),
                ("5", "Bicycle commuters report higher levels of daily vitality than motorists. (TRUE / FALSE / NOT GIVEN)")
            ],
            "reading_text_2": """<b>Sentence Completion: Questions 6-10:</b><br/>
• Behavioural psychologists consider commuting to be highly [ 6. __________ ] to human happiness.<br/>
• Erratic transit delays trigger acute feelings of [ 7. __________ ] among travelers.<br/>
• Active commuters who walk or cycle experience greater feelings of [ 8. __________ ] and energy.<br/>
• Train passengers are able to use transit time for passive [ 9. __________ ] or reading.<br/>
• Unlike transit riders, automobile drivers must sustain continuous, vigilance-demanding [ 10. __________ ] focus.""",
            "reading_q_2": [
                ("6", "Complete Question 6"),
                ("7", "Complete Question 7"),
                ("8", "Complete Question 8"),
                ("9", "Complete Question 9"),
                ("10", "Complete Question 10")
            ],
            "writing_task": """<b>Task 2 Counter-Argument & Refutation Drill:</b><br/>
Band 7+ essays often address a counter-argument and refute it. Study the formula:<br/>
<i>'While opponents argue that [Counter-argument], this reasoning is flawed because [Refutation].'</i><br/>
Write one full paragraph using this structure on the topic: <i>Should university education be completely free for all citizens?</i>""",
            "speaking_task": """<b>Speaking Part 3 (Abstract PREP Reasoning):</b><br/>
1. How has modern technology altered the way people spend their leisure time?<br/>
2. Do you believe individuals in the past enjoyed a better work-life balance than modern citizens?<br/>
Apply PREP: Point, Reason, Example, Perspective.""",
            "strategy": """<b>Examiner Strategy: The 15-20-25 GT Reading Time Allocation Clock</b><br/>
Section 1: 15 mins (easy texts, do not linger!).<br/>
Section 2: 20 mins (workplace notices, precise answers).<br/>
Section 3: 25 mins (academic/journal text, requires careful reading).<br/>
Never spend more than 90 seconds stuck on a single question! Guess and flag it.""",
            "answers": {
                "L": [
                    ("1", "freshwater", "Audio: 'arable land availability and freshwater consumption'."),
                    ("2", "climate-controlled / climate controlled", "Audio: 'layers inside climate-controlled buildings'."),
                    ("3", "95 / ninety-five", "Audio: 'reduce freshwater utilization by up to ninety-five percent'."),
                    ("4", "seasons", "Audio: 'crop yields remain consistent throughout all four seasons'."),
                    ("5", "pesticide / pesticides", "Audio: 'eliminating agricultural pesticide runoff'."),
                    ("6", "electrical", "Audio: 'demand substantial electrical energy'."),
                    ("7", "LED", "Audio: 'power artificial LED illumination grids'."),
                    ("8", "carbon", "Audio: 'operational carbon footprint of vertical farms'."),
                    ("9", "robotic harvesting / harvesting", "Audio: 'automated robotic harvesting mechanisms'."),
                    ("10", "stacked", "Audio: 'cultivating crops in vertically stacked layers'.")
                ],
                "R": [
                    ("1", "TRUE", "Text: 'links prolonged commutes with elevated cortisol production, chronic musculoskeletal tension'."),
                    ("2", "FALSE", "Text: 'fundamental determinant of commute-induced stress is not geographical distance, but unpredictable variance.' Contradicts statement."),
                    ("3", "TRUE", "Text: 'predictable 45-minute duration, cognitive stress remains moderate'."),
                    ("4", "FALSE", "Text: 'passengers on public transit report higher life satisfaction than solo car drivers... drivers must maintain focus'."),
                    ("5", "TRUE", "Text: 'Individuals who walk or cycle to work report feelings of alertness, autonomy, and elevated vitality'."),
                    ("6", "detrimental", "Text: 'one of the single most detrimental activities affecting subjective human happiness'."),
                    ("7", "helplessness", "Text: 'triggers an acute loss of control... perception of helplessness'."),
                    ("8", "autonomy", "Text: 'report feelings of alertness, autonomy, and elevated vitality'."),
                    ("9", "recreation", "Text: 'time for passive recreation, reading, or mindfulness'."),
                    ("10", "visual", "Text: 'drivers must maintain uninterrupted, vigilance-demanding visual focus'.")
                ],
                "writing_model": """<b>Band 8.5 Counter-Argument & Refutation Model:</b><br/>
While opponents argue that providing universal free university education would overburden government budgets and lead to excessive taxation, this reasoning is fundamentally short-sighted. Investing national funds in higher education yields substantial long-term economic dividends, as highly educated graduates generate greater productivity, earn higher salaries, and subsequently contribute vastly more income tax over their professional careers. Therefore, public funding for tertiary education represents a profitable strategic investment rather than a fiscal drain."""
            }
        },
        7: {
            "title": "Day 07: Week 1 Assessment & Consolidation Mini-Mock",
            "focus": "Comprehensive multi-skill assessment, error audit, and Week 2 calibration",
            "time_reg": "120 Minutes (Deep Dive Session)",
            "time_busy": "45 Minutes (Mini-Mock Listening & Vocab)",
            "listening_title": "Weekly Listening Mini-Mock (15 Questions)",
            "listening_audio": "audio_track.wav",
            "listening_instructions": "Answer Questions 1-15 with NO MORE THAN TWO WORDS AND/OR A NUMBER.",
            "listening_questions": [
                ("1", "Caller Last Name: ____________ (Spelled: P-E-N-D-E-L-T-O-N)"),
                ("2", "Tour Type: ____________ trail tour"),
                ("3", "Number of Cyclists: ____________"),
                ("4", "Tour Date: Saturday, ____________ November"),
                ("5", "Price per Cyclist: £ ____________"),
                ("6", "Package includes bike hire and safety: ____________"),
                ("7", "Cyclists must stay strictly on designated: ____________"),
                ("8", "In bad weather, proceed to emergency shelter at: ____________ Ridge"),
                ("9", "Century of canal expansion: ____________ century"),
                ("10", "Canals revolutionized internal ____________ transport."),
                ("11", "Canals were superseded by steam: ____________"),
                ("12", "Emergency shelter name: ____________ Pass"),
                ("13", "Intermediate tour fee for two cyclists: £ ____________"),
                ("14", "Safety gear provided: ____________"),
                ("15", "Primary competitor to canal freight: steam ____________")
            ],
            "reading_title": "Weekly GT Reading Mini-Mock (15 Questions)",
            "reading_text_1": """<b>Section 1: Metro Transit Fare & Penalty Fares Notice</b><br/>
Passengers boarding the Metro light rail system must validate a valid travel ticket or smart transit card prior to entering the ticket barrier zone. Failure to present a validated fare upon inspection by an authorized revenue protection officer will incur an immediate Penalty Fare of £50, reduced to £25 if settled within 14 calendar days.<br/>
Registered university students and apprentices under the age of 25 are eligible for an Academic Transit Pass, granting a 30% reduction across all non-peak off-peak services. Pass holders must carry their institutional identification card at all times. Lost or damaged transit smart cards can be reissued at the central station customer service kiosk upon payment of an administrative processing fee of £5.""",
            "reading_q_1": [
                ("1", "Passengers can purchase tickets after boarding the train carriage. (TRUE / FALSE / NOT GIVEN)"),
                ("2", "The penalty fare is halved if paid within a fortnight. (TRUE / FALSE / NOT GIVEN)"),
                ("3", "University students receive a 30% discount on peak morning rush-hour trains. (TRUE / FALSE / NOT GIVEN)"),
                ("4", "Student pass holders must possess their student ID while traveling. (TRUE / FALSE / NOT GIVEN)"),
                ("5", "Replacing a lost smart card costs [ £ __________ ].")
            ],
            "reading_text_2": """<b>Section 2: Workplace Dispute Resolution Protocol</b><br/>
When interpersonal conflicts or disputes arise in the workplace, staff are urged to attempt informal resolution through constructive dialogue with their colleague. However, if the matter remains unresolved or involves severe allegations such as bullying or discrimination, the employee should trigger the formal Stage 1 Grievance Procedure.<br/>
To initiate Stage 1, the complainant must submit a detailed written statement to their human resources representative within ten working days of the contested incident. An independent investigating officer will be assigned within five working days. The employee possesses the legal right to be accompanied to all grievance meetings by a certified trade union official or a workplace peer. Following the inquiry, the investigating officer will issue a formal determination letter within fifteen working days.""",
            "reading_q_2": [
                ("6", "Informal discussion must always be attempted even in cases of severe discrimination. (TRUE / FALSE / NOT GIVEN)"),
                ("7", "Stage 1 grievances must be submitted in writing within ten working days. (TRUE / FALSE / NOT GIVEN)"),
                ("8", "Employees may be accompanied to meetings by a practicing attorney or lawyer. (TRUE / FALSE / NOT GIVEN)"),
                ("9", "An investigator is appointed within [ __________ ] working days of submission."),
                ("10", "A final decision letter is delivered within [ __________ ] working days of the investigation conclusion.")
            ],
            "writing_task": """<b>Weekly Writing Evaluation: Full Timed Task 1 or Task 2</b><br/>
Choose one task to submit for line-by-line examiner assessment:<br/>
<b>Option A (Task 1 Letter):</b> You recently rented a vehicle from an airport car rental agency. Shortly after driving onto the motorway, the brakes malfunctioned and you were forced to wait three hours for emergency roadside assistance. Write a formal letter of complaint to the customer relations director.<br/>
<b>Option B (Task 2 Essay):</b> In many modern nations, an increasing proportion of consumer shopping is conducted over the internet rather than in traditional high-street shops. Do the advantages of this development outweigh the disadvantages?""",
            "speaking_task": """<b>Weekly Speaking Mock Interview (Full 14-Minute Simulation):</b><br/>
• Part 1: Transportation, daily routines, and internet usage.<br/>
• Part 2 (Cue Card): Describe an online service or mobile application that has made your life significantly easier.<br/>
• Part 3: The future of artificial intelligence in daily services, privacy concerns with digital algorithms, and the impact of automation on local retail jobs.""",
            "strategy": """<b>Consolidation Strategy: Error Log Audit & Spaced Repetition</b><br/>
Today, open `ERROR_LOG.xlsx`. Group your week's errors by category. If Paraphrasing or Distractors caused more than 2 mistakes, schedule 15 minutes of targeted Section 3/4 listening drills for Week 2.""",
            "answers": {
                "L": [
                    ("1", "Pendelton", "Spelling: P-E-N-D-E-L-T-O-N."),
                    ("2", "intermediate", "Audio: 'book the intermediate trail tour'."),
                    ("3", "2 / two", "Audio: 'for two people'."),
                    ("4", "25th / 25", "Audio: 'Saturday, 25th of November'."),
                    ("5", "75 / seventy-five", "Audio: 'fee is 75 pounds per cyclist'."),
                    ("6", "helmets", "Audio: 'bike hire and safety helmets'."),
                    ("7", "bridleways", "Audio: 'remain on designated bridleways'."),
                    ("8", "High Pass", "Audio: 'shelter located at High Pass Ridge'."),
                    ("9", "nineteenth / 19th", "Audio: 'During the nineteenth century'."),
                    ("10", "freight", "Audio: 'revolutionized internal freight transport'."),
                    ("11", "railways", "Audio: 'superseded by the rapid construction of steam railways'."),
                    ("12", "High", "Audio: 'located at High Pass Ridge'."),
                    ("13", "150", "Math: 2 cyclists x £75 = £150."),
                    ("14", "helmets", "Audio: 'helmets'."),
                    ("15", "railways", "Audio: 'steam railways'.")
                ],
                "R": [
                    ("1", "FALSE", "Text: 'must validate... prior to entering the ticket barrier zone'."),
                    ("2", "TRUE", "Text: 'reduced to £25 if settled within 14 calendar days' (14 days = fortnight)."),
                    ("3", "FALSE", "Text: 'reduction across all non-peak off-peak services'. Not peak morning rush."),
                    ("4", "TRUE", "Text: 'Pass holders must carry their institutional identification card at all times'."),
                    ("5", "5", "Text: 'processing fee of £5'."),
                    ("6", "FALSE", "Text: 'However, if the matter... involves severe allegations such as bullying or discrimination, the employee should trigger the formal Stage 1 Grievance Procedure'."),
                    ("7", "TRUE", "Text: 'submit a detailed written statement... within ten working days'."),
                    ("8", "FALSE", "Text: 'accompanied... by a certified trade union official or a workplace peer'. Lawyers not permitted."),
                    ("9", "5 / five", "Text: 'assigned within five working days'."),
                    ("10", "15 / fifteen", "Text: 'issue a formal determination letter within fifteen working days'.")
                ],
                "writing_model": """<b>Band 8.5 Task 2 Advantages Outweigh Disadvantages Model:</b><br/>
The rapid ascendancy of e-commerce platforms has fundamentally transformed global consumer behavior, with a substantial majority of retail transactions now conducted over digital marketplaces rather than in conventional brick-and-mortar storefronts. While this digital shift poses legitimate threats to local high-street commerce, I firmly contend that the unparalleled economic efficiency and consumer convenience it delivers substantially outweigh these drawbacks.<br/><br/>
Admittedly, the migration toward online retail exerts considerable economic strain on physical retail establishments. As foot traffic declines, independent local boutiques frequently struggle to maintain profitability against overwhelming overhead costs, leading to high-street vacancies and job losses among shop assistants. Furthermore, online purchasing eliminates the tactile verification of merchandise, occasionally leading to consumer dissatisfaction and increased product returns.<br/><br/>
Nevertheless, the transformative advantages of digital commerce are undeniable. Foremost among these is unprecedented consumer convenience and price transparency. E-commerce enables consumers to compare prices globally, access wider selections of goods, and have products delivered directly to their doorsteps, thereby saving immense time for working professionals. Moreover, online commerce drastically reduces barriers to entry for small entrepreneurs, who can now market specialized products to an international audience without incurring the exorbitant capital costs of prime commercial real estate.<br/><br/>
In conclusion, although the contraction of traditional retail creates localized commercial challenges, the pervasive societal benefits of e-commerce—namely enhanced accessibility, consumer autonomy, and global market reach—render this development overwhelmingly advantageous."""
            }
        }
    }
    return data[day_num]

def build_daily_task_pdf(day_num, filepath):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    styles = get_custom_styles()
    story = []
    data = get_day_data(day_num)
    
    # Header block
    story.append(Paragraph(f"<b>IELTS GENERAL TRAINING PREPARATION SYSTEM</b>", styles['subtitle']))
    story.append(Paragraph(data['title'], styles['title']))
    story.append(Paragraph(f"<b>Focus:</b> {data['focus']} | <b>Regular Time:</b> {data['time_reg']} | <b>Busy Day:</b> {data['time_busy']}", styles['instruction']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=4, spaceAfter=8))
    
    # Strategy Box
    strat_p = [
        Paragraph("<b>EXAMINATION STRATEGY OF THE DAY</b>", styles['h2']),
        Paragraph(data['strategy'], styles['box'])
    ]
    story.append(create_box_table(strat_p, bg_color=colors.HexColor("#EBF8FF"), border_color=SECONDARY))
    story.append(Spacer(1, 8))
    
    # Listening Section
    story.append(Paragraph(f"MODULE 1: {data['listening_title']}", styles['h1']))
    story.append(Paragraph(f"<b>Audio File:</b> <code>{data['listening_audio']}</code> (Located in this day's folder) | <i>{data['listening_instructions']}</i>", styles['instruction']))
    story.append(Spacer(1, 4))
    
    # Listening Questions Table
    q_table_data = []
    for q_num, q_text in data['listening_questions']:
        q_table_data.append([
            Paragraph(f"<b>Q{q_num}</b>", styles['bold']),
            Paragraph(q_text, styles['body'])
        ])
    t_list = Table(q_table_data, colWidths=[35, 505])
    t_list.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_list)
    story.append(Spacer(1, 8))
    
    # Reading Section
    story.append(Paragraph(f"MODULE 2: {data['reading_title']}", styles['h1']))
    story.append(Paragraph("<b>Passage 1:</b>", styles['h2']))
    story.append(create_box_table([Paragraph(data['reading_text_1'], styles['box'])], bg_color=LIGHT_BG))
    story.append(Spacer(1, 4))
    
    r_table_data_1 = []
    for q_num, q_text in data['reading_q_1']:
        r_table_data_1.append([
            Paragraph(f"<b>Q{q_num}</b>", styles['bold']),
            Paragraph(q_text, styles['body'])
        ])
    t_r1 = Table(r_table_data_1, colWidths=[35, 505])
    t_r1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_r1)
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("<b>Passage 2:</b>", styles['h2']))
    story.append(create_box_table([Paragraph(data['reading_text_2'], styles['box'])], bg_color=LIGHT_BG))
    story.append(Spacer(1, 4))
    
    r_table_data_2 = []
    for q_num, q_text in data['reading_q_2']:
        r_table_data_2.append([
            Paragraph(f"<b>Q{q_num}</b>", styles['bold']),
            Paragraph(q_text, styles['body'])
        ])
    t_r2 = Table(r_table_data_2, colWidths=[35, 505])
    t_r2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_r2)
    story.append(Spacer(1, 8))
    
    # Writing Section
    story.append(Paragraph("MODULE 3: WRITING PRACTICE", styles['h1']))
    story.append(create_box_table([Paragraph(data['writing_task'], styles['box'])], bg_color=colors.HexColor("#FFF5F5"), border_color=colors.HexColor("#FEB2B2")))
    story.append(Spacer(1, 8))
    
    # Speaking Section
    story.append(Paragraph("MODULE 4: SPEAKING PRACTICE", styles['h1']))
    story.append(create_box_table([Paragraph(data['speaking_task'], styles['box'])], bg_color=colors.HexColor("#F0FFF4"), border_color=colors.HexColor("#9AE6B4")))
    story.append(Spacer(1, 8))
    
    # Checklist & Completion
    chk_content = [
        Paragraph("<b>DAILY COMPLETION CHECKLIST:</b>", styles['bold']),
        Paragraph("[  ] Completed Listening using <code>audio_track.wav</code> without checking answers prematurely.<br/>[  ] Completed Reading questions within the designated time window.<br/>[  ] Drafted Writing response or recorded Speaking audio.<br/>[  ] Compared answers against <code>Answer_Key.pdf</code>.<br/>[  ] Logged all incorrect answers into <code>ERROR_LOG.xlsx</code> with root cause classification.<br/>[  ] Submitted writing/speaking in chat for formal line-by-line examiner assessment.", styles['box'])
    ]
    story.append(create_box_table(chk_content, bg_color=colors.HexColor("#FEFCBF"), border_color=colors.HexColor("#D69E2E")))
    
    doc.build(story)

def build_answer_sheet_pdf(day_num, filepath):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    styles = get_custom_styles()
    story = []
    data = get_day_data(day_num)
    
    story.append(Paragraph("<b>IELTS GENERAL TRAINING CANDIDATE RESPONSE SHEET</b>", styles['subtitle']))
    story.append(Paragraph(f"{data['title']} — CANDIDATE ANSWER SHEET", styles['title']))
    story.append(Paragraph("Write your answers clearly in the designated spaces below. Do not refer to the Answer Key until finished.", styles['instruction']))
    story.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=4, spaceAfter=8))
    
    # Candidate details bar
    cand_info = [
        [Paragraph("<b>Candidate Name:</b>", styles['body']), Paragraph("____________________________________", styles['body']),
         Paragraph("<b>Date:</b>", styles['body']), Paragraph("____________________", styles['body'])],
        [Paragraph("<b>Listening Raw Score:</b>", styles['body']), Paragraph("_____ / 10", styles['body']),
         Paragraph("<b>Reading Raw Score:</b>", styles['body']), Paragraph("_____ / 10", styles['body'])]
    ]
    t_info = Table(cand_info, colWidths=[120, 160, 100, 160])
    t_info.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 10))
    
    # 2-Column Answer Grids: Left = Listening, Right = Reading
    l_rows = [["Q#", "Listening Candidate Answer"]]
    for q_num, _ in data['listening_questions']:
        l_rows.append([f"Q{q_num}", "__________________________________________________"])
    t_l_grid = Table(l_rows, colWidths=[35, 225])
    t_l_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COL),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ]))
    
    # Reading rows
    all_reading_q = data['reading_q_1'] + data['reading_q_2']
    r_rows = [["Q#", "Reading Candidate Answer"]]
    for q_num, _ in all_reading_q:
        r_rows.append([f"Q{q_num}", "__________________________________________________"])
    t_r_grid = Table(r_rows, colWidths=[35, 225])
    t_r_grid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COL),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ]))
    
    # Combined side by side
    side_table = Table([[t_l_grid, t_r_grid]], colWidths=[265, 265])
    side_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(side_table)
    story.append(Spacer(1, 10))
    
    # Writing / Speaking notes space
    story.append(Paragraph("<b>WRITING RESPONSE DRAFT / SPEAKING OUTLINE SPACE:</b>", styles['h2']))
    notes_lines = []
    for _ in range(16):
        notes_lines.append(Paragraph("____________________________________________________________________________________________________", styles['body']))
    story.append(create_box_table(notes_lines, bg_color=colors.white, border_color=BORDER_COL))
    
    doc.build(story)

def build_answer_key_pdf(day_num, filepath):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    styles = get_custom_styles()
    story = []
    data = get_day_data(day_num)
    
    story.append(Paragraph("<b>OFFICIAL IELTS EXAMINER EVALUATION & ANSWER KEY</b>", styles['subtitle']))
    story.append(Paragraph(f"{data['title']} — DETAILED ANSWER KEY", styles['title']))
    story.append(Paragraph("Review every answer carefully. Identify the root cause for any missed questions and update ERROR_LOG.xlsx immediately.", styles['instruction']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=4, spaceAfter=8))
    
    # Listening Answers Table
    story.append(Paragraph("MODULE 1: LISTENING ANSWERS & EXPLANATIONS", styles['h1']))
    l_key_rows = [["Q#", "Official Answer", "Examiner Explanation & Distractor Analysis"]]
    for q_num, ans, exp in data['answers']['L']:
        l_key_rows.append([
            Paragraph(f"<b>Q{q_num}</b>", styles['bold']),
            Paragraph(f"<b>{ans}</b>", styles['bold']),
            Paragraph(exp, styles['body'])
        ])
    t_l_key = Table(l_key_rows, colWidths=[35, 130, 375])
    t_l_key.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COL),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_l_key)
    story.append(Spacer(1, 10))
    
    # Reading Answers Table
    story.append(Paragraph("MODULE 2: READING ANSWERS & SYNONYM MAPPING", styles['h1']))
    r_key_rows = [["Q#", "Official Answer", "Text Citation & Paraphrase Analysis"]]
    for q_num, ans, exp in data['answers']['R']:
        r_key_rows.append([
            Paragraph(f"<b>Q{q_num}</b>", styles['bold']),
            Paragraph(f"<b>{ans}</b>", styles['bold']),
            Paragraph(exp, styles['body'])
        ])
    t_r_key = Table(r_key_rows, colWidths=[35, 130, 375])
    t_r_key.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COL),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_r_key)
    story.append(Spacer(1, 10))
    
    # Writing Band 8.5 Model
    story.append(Paragraph("MODULE 3: EXAMINER MODEL RESPONSE & CRITERIA BREAKDOWN", styles['h1']))
    model_content = [
        Paragraph(data['answers']['writing_model'], styles['box']),
        Spacer(1, 4),
        Paragraph("<b>Official Band Criteria Analysis:</b><br/>• <b>Task Achievement / Response:</b> All bullet points / prompt requirements fully extended with relevant circumstantial evidence.<br/>• <b>Coherence & Cohesion:</b> Natural paragraph progression without forced, mechanical linking markers.<br/>• <b>Lexical Resource:</b> Precise, context-appropriate academic collocations (e.g. <i>'profound disappointment'</i>, <i>'remedial action'</i>, <i>'substandard quality'</i>).<br/>• <b>Grammatical Range & Accuracy:</b> Mixture of conditionals, passive voice, and complex subordinate clauses with zero mechanical punctuation errors.", styles['instruction'])
    ]
    story.append(create_box_table(model_content, bg_color=colors.HexColor("#F0FFF4"), border_color=colors.HexColor("#68D391")))
    
    doc.build(story)

def generate_markdown_content(day_num, filepath):
    data = get_day_data(day_num)
    md = f"# {data['title']}\n"
    md += f"**Focus:** {data['focus']}  \n"
    md += f"**Estimated Time:** Regular Day: {data['time_reg']} | Busy Day: {data['time_busy']}  \n\n"
    md += "---\n\n"
    
    md += "## Strategy of the Day\n"
    md += f"{data['strategy']}\n\n"
    md += "---\n\n"
    
    md += f"## Module 1: {data['listening_title']}\n"
    md += f"**Audio:** `{data['listening_audio']}`  \n"
    md += f"*{data['listening_instructions']}*\n\n"
    for q_num, q_text in data['listening_questions']:
        md += f"- **Q{q_num}:** {q_text}\n"
    md += "\n---\n\n"
    
    md += f"## Module 2: {data['reading_title']}\n\n"
    md += "### Passage 1:\n"
    md += f"{data['reading_text_1']}\n\n"
    for q_num, q_text in data['reading_q_1']:
        md += f"- **Q{q_num}:** {q_text}\n"
    md += "\n### Passage 2:\n"
    md += f"{data['reading_text_2']}\n\n"
    for q_num, q_text in data['reading_q_2']:
        md += f"- **Q{q_num}:** {q_text}\n"
    md += "\n---\n\n"
    
    md += "## Module 3: Writing Practice\n\n"
    md += f"{data['writing_task']}\n\n"
    md += "---\n\n"
    
    md += "## Module 4: Speaking Practice\n\n"
    md += f"{data['speaking_task']}\n\n"
    md += "---\n\n"
    
    md += "## Submission & Evaluation Instructions\n"
    md += "1. Complete questions on `Answer_Sheet.pdf` or directly in text.\n"
    md += "2. Check Listening and Reading against `Answer_Key.pdf`.\n"
    md += "3. Paste your Writing draft or Speaking response directly in chat for line-by-line examiner scoring.\n"
    md += "4. Log any errors in `ERROR_LOG.xlsx`.\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

def generate_all_days():
    for d in range(1, 8):
        day_dir = f"d:/IELTS-Prep/DAILY_ASSIGNMENTS/WEEK_01/DAY_{d:02d}"
        os.makedirs(day_dir, exist_ok=True)
        
        task_pdf = os.path.join(day_dir, "Daily_Task.pdf")
        sheet_pdf = os.path.join(day_dir, "Answer_Sheet.pdf")
        key_pdf = os.path.join(day_dir, "Answer_Key.pdf")
        content_md = os.path.join(day_dir, f"DAY_{d:02d}_CONTENT.md")
        
        build_daily_task_pdf(d, task_pdf)
        build_answer_sheet_pdf(d, sheet_pdf)
        build_answer_key_pdf(d, key_pdf)
        generate_markdown_content(d, content_md)
        print(f"Generated PDFs and Markdown for Day {d:02d}")

if __name__ == "__main__":
    generate_all_days()

