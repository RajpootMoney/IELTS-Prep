import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_progress_tracker():
    wb = openpyxl.Workbook()
    # Remove default sheet
    default_sheet = wb.active
    
    # Styles
    navy_fill = PatternFill(start_color="1A365D", end_color="1A365D", fill_type="solid")
    blue_fill = PatternFill(start_color="2B6CB0", end_color="2B6CB0", fill_type="solid")
    light_blue_fill = PatternFill(start_color="EBF8FF", end_color="EBF8FF", fill_type="solid")
    gray_fill = PatternFill(start_color="EDF2F7", end_color="EDF2F7", fill_type="solid")
    green_fill = PatternFill(start_color="C6F6D5", end_color="C6F6D5", fill_type="solid")
    yellow_fill = PatternFill(start_color="FEFCBF", end_color="FEFCBF", fill_type="solid")
    
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    title_font = Font(name="Calibri", size=14, bold=True, color="1A365D")
    sub_font = Font(name="Calibri", size=11, bold=True, color="2B6CB0")
    bold_font = Font(name="Calibri", size=10, bold=True)
    normal_font = Font(name="Calibri", size=10)
    
    thin_border = Border(
        left=Side(style='thin', color='CBD5E0'),
        right=Side(style='thin', color='CBD5E0'),
        top=Side(style='thin', color='CBD5E0'),
        bottom=Side(style='thin', color='CBD5E0')
    )
    
    # --- 1. Dashboard Tab ---
    ws_dash = wb.create_sheet(title="Dashboard")
    ws_dash.views.sheetView[0].showGridLines = True
    
    ws_dash["A1"] = "IELTS GENERAL TRAINING - PERFORMANCE DASHBOARD"
    ws_dash["A1"].font = title_font
    ws_dash["A2"] = "Target: Canadian PR (Express Entry) | Required CLB Level: 9/10"
    ws_dash["A2"].font = sub_font
    
    # Summary Table Headers
    headers_dash = ["Module", "Baseline Score", "Current Est. Band", "Target Band", "Required Raw Score", "Express Entry CLB", "Status"]
    for col_idx, h in enumerate(headers_dash, start=1):
        cell = ws_dash.cell(row=4, column=col_idx, value=h)
        cell.fill = navy_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    dash_data = [
        ["Listening", "25 - 31 / 40", 6.5, 8.0, "35 - 36 / 40", "CLB 9", "High Priority"],
        ["Reading (GT)", "~30 / 40", 6.0, 7.0, "34 - 35 / 40", "CLB 9", "Needs +4 Marks"],
        ["Writing", "Diagnostic Pending", "-", 7.0, "Task 1 & 2 Band 7", "CLB 9", "Diagnostic Day 1"],
        ["Speaking", "Diagnostic Pending", "-", 7.0, "Band 7 Across Parts", "CLB 9", "Diagnostic Day 1"],
    ]
    for row_idx, r_data in enumerate(dash_data, start=5):
        for col_idx, val in enumerate(r_data, start=1):
            cell = ws_dash.cell(row=row_idx, column=col_idx, value=val)
            cell.font = normal_font
            cell.border = thin_border
            if col_idx in [3, 4]:
                cell.alignment = Alignment(horizontal="center")
                cell.font = bold_font
            elif col_idx in [6, 7]:
                cell.alignment = Alignment(horizontal="center")
                if "High" in str(val) or "Needs" in str(val):
                    cell.fill = yellow_fill
                else:
                    cell.fill = light_blue_fill
    
    # Reference Conversion Table
    ws_dash["A11"] = "OFFICIAL SCORE CONVERSION REFERENCE (GT READING vs LISTENING)"
    ws_dash["A11"].font = sub_font
    
    conv_headers = ["Band Score", "Listening Raw (/40)", "GT Reading Raw (/40)", "Academic Reading Raw (/40)", "Express Entry CLB"]
    for col_idx, h in enumerate(conv_headers, start=1):
        cell = ws_dash.cell(row=12, column=col_idx, value=h)
        cell.fill = blue_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    conv_data = [
        [9.0, "39 - 40", "40", "39 - 40", "CLB 10+"],
        [8.5, "37 - 38", "39", "37 - 38", "CLB 10"],
        [8.0, "35 - 36", "37 - 38", "35 - 36", "CLB 9 (Listening Target)"],
        [7.5, "32 - 34", "36", "33 - 34", "CLB 9"],
        [7.0, "30 - 31", "34 - 35", "30 - 32", "CLB 9 (Reading Target)"],
        [6.5, "26 - 29", "32 - 33", "27 - 29", "CLB 8"],
        [6.0, "23 - 25", "30 - 31", "23 - 26", "CLB 7 (Baseline)"],
    ]
    for row_idx, r_data in enumerate(conv_data, start=13):
        for col_idx, val in enumerate(r_data, start=1):
            cell = ws_dash.cell(row=row_idx, column=col_idx, value=val)
            cell.font = normal_font
            cell.border = thin_border
            cell.alignment = Alignment(horizontal="center")
            if row_idx in [15, 17]:
                cell.fill = green_fill
                cell.font = bold_font
                
    # --- 2. Listening Tracker Tab ---
    ws_list = wb.create_sheet(title="Listening Tracker")
    ws_list.views.sheetView[0].showGridLines = True
    ws_list["A1"] = "IELTS LISTENING PROGRESS & SECTION BREAKDOWN"
    ws_list["A1"].font = title_font
    
    list_headers = ["Date", "Test / Assignment ID", "Section 1 (/10)", "Section 2 (/10)", "Section 3 (/10)", "Section 4 (/10)", "Raw Score (/40)", "Est. Band", "Target Met?", "Weakest Section", "Key Distractors & Notes"]
    for col_idx, h in enumerate(list_headers, start=1):
        cell = ws_list.cell(row=3, column=col_idx, value=h)
        cell.fill = navy_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Prepopulate historical data
    hist_listening = [
        ["Baseline Test 1", "Practice Test 1", 8, 7, 6, 5, 26, 6.5, "No", "Section 4", "Lost place during academic monologue; spellings missed"],
        ["Baseline Test 2", "Practice Test 2", 9, 8, 7, 6, 30, 7.0, "No", "Section 4", "Struggled with paraphrased terms in Section 3 & 4"],
        ["Baseline Test 3", "Practice Test 3", 7, 7, 6, 5, 25, 6.0, "No", "Section 3 & 4", "Direction changes missed; distractor dates recorded"],
        ["Baseline Best", "Practice Test 4", 9, 8, 8, 6, 31, 7.0, "No", "Section 4", "Strong in Sec 1-2; Sec 4 remains primary obstacle"],
    ]
    for row_idx, r_data in enumerate(hist_listening, start=4):
        for col_idx, val in enumerate(r_data, start=1):
            cell = ws_list.cell(row=row_idx, column=col_idx, value=val)
            cell.font = normal_font
            cell.border = thin_border
            if col_idx in range(3, 10):
                cell.alignment = Alignment(horizontal="center")

    # --- 3. Reading Tracker Tab ---
    ws_read = wb.create_sheet(title="Reading Tracker")
    ws_read.views.sheetView[0].showGridLines = True
    ws_read["A1"] = "IELTS GENERAL TRAINING READING TRACKER"
    ws_read["A1"].font = title_font
    
    read_headers = ["Date", "Test / Assignment ID", "Section 1 (/14)", "Section 2 (/13)", "Section 3 (/13)", "Raw Score (/40)", "Est. Band (GT)", "Target Met?", "Weakest Question Type", "Pacing & Error Observations"]
    for col_idx, h in enumerate(read_headers, start=1):
        cell = ws_read.cell(row=3, column=col_idx, value=h)
        cell.fill = navy_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    hist_reading = [
        ["Recent Baseline", "GT Practice Test 1", 12, 10, 8, 30, 6.0, "No (Need 34)", "TFNG & Headings", "Ran out of time in Section 3; confused False with Not Given"]
    ]
    for row_idx, r_data in enumerate(hist_reading, start=4):
        for col_idx, val in enumerate(r_data, start=1):
            cell = ws_read.cell(row=row_idx, column=col_idx, value=val)
            cell.font = normal_font
            cell.border = thin_border
            if col_idx in range(3, 9):
                cell.alignment = Alignment(horizontal="center")
                
    # --- 4. Writing Tracker Tab ---
    ws_write = wb.create_sheet(title="Writing Tracker")
    ws_write.views.sheetView[0].showGridLines = True
    ws_write["A1"] = "IELTS GENERAL TRAINING WRITING EVALUATIONS"
    ws_write["A1"].font = title_font
    
    write_headers = ["Date", "Task", "Topic / Prompt Summary", "Task Resp / Ach (/9)", "Coh & Cohesion (/9)", "Lexical Resource (/9)", "Grammar & Acc (/9)", "Overall Band", "Word Count", "Priority Corrective Action"]
    for col_idx, h in enumerate(write_headers, start=1):
        cell = ws_write.cell(row=3, column=col_idx, value=h)
        cell.fill = navy_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    # --- 5. Speaking Tracker Tab ---
    ws_speak = wb.create_sheet(title="Speaking Tracker")
    ws_speak.views.sheetView[0].showGridLines = True
    ws_speak["A1"] = "IELTS SPEAKING INTERVIEW EVALUATIONS"
    ws_speak["A1"].font = title_font
    
    speak_headers = ["Date", "Part Evaluated", "Topic Focus", "Fluency & Coh (/9)", "Lexical Res (/9)", "Grammar & Acc (/9)", "Pronunciation (/9)", "Overall Band", "Main Hesitation Blocker", "High-Priority Fix"]
    for col_idx, h in enumerate(speak_headers, start=1):
        cell = ws_speak.cell(row=3, column=col_idx, value=h)
        cell.fill = navy_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    # --- 6. Daily Study Log Tab ---
    ws_log = wb.create_sheet(title="Daily Study Log")
    ws_log.views.sheetView[0].showGridLines = True
    ws_log["A1"] = "DAILY PREPARATION EFFORT & STUDY LOG"
    ws_log["A1"].font = title_font
    
    log_headers = ["Date", "Day #", "Planned Focus", "Actual Minutes", "Listening Done", "Reading Done", "Writing/Speaking Done", "Vocab Words", "Status", "Candidate Notes"]
    for col_idx, h in enumerate(log_headers, start=1):
        cell = ws_log.cell(row=3, column=col_idx, value=h)
        cell.fill = navy_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    # Auto-adjust column widths
    for sheet in wb.worksheets:
        if sheet == default_sheet:
            continue
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or '')
                if len(val) > max_len and len(val) < 60:
                    max_len = len(val)
            sheet.column_dimensions[col_letter].width = max(max_len + 4, 12)
            
    wb.remove(default_sheet)
    wb.save("d:/IELTS-Prep/PROGRESS_TRACKER.xlsx")
    print("PROGRESS_TRACKER.xlsx generated successfully.")

def create_error_log():
    wb = openpyxl.Workbook()
    default_sheet = wb.active
    
    navy_fill = PatternFill(start_color="1A365D", end_color="1A365D", fill_type="solid")
    blue_fill = PatternFill(start_color="2B6CB0", end_color="2B6CB0", fill_type="solid")
    red_fill = PatternFill(start_color="FED7D7", end_color="FED7D7", fill_type="solid")
    gray_fill = PatternFill(start_color="EDF2F7", end_color="EDF2F7", fill_type="solid")
    
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    title_font = Font(name="Calibri", size=14, bold=True, color="1A365D")
    sub_font = Font(name="Calibri", size=11, bold=True, color="2B6CB0")
    bold_font = Font(name="Calibri", size=10, bold=True)
    normal_font = Font(name="Calibri", size=10)
    
    thin_border = Border(
        left=Side(style='thin', color='CBD5E0'),
        right=Side(style='thin', color='CBD5E0'),
        top=Side(style='thin', color='CBD5E0'),
        bottom=Side(style='thin', color='CBD5E0')
    )
    
    # 1. Error Log Master Tab
    ws_log = wb.create_sheet(title="Error Log")
    ws_log.views.sheetView[0].showGridLines = True
    ws_log["A1"] = "IELTS ERROR AUDIT & ROOT CAUSE TRACKER"
    ws_log["A1"].font = title_font
    ws_log["A2"] = "Every mistake is a data point. Classify root cause and re-test via spaced repetition."
    ws_log["A2"].font = sub_font
    
    log_headers = [
        "Error ID", "Date", "Module", "Test / Assignment", "Q #", "Question Type", 
        "Candidate Answer", "Official Correct Answer", "Root Cause Category", 
        "Detailed Root Cause (Why did I fail?)", "Examiner Rule / Correct Technique", 
        "Spaced Review Date", "Status"
    ]
    for col_idx, h in enumerate(log_headers, start=1):
        cell = ws_log.cell(row=4, column=col_idx, value=h)
        cell.fill = navy_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    # Sample historical errors pre-populated to illustrate system
    sample_errors = [
        ["ERR-001", "Baseline", "Listening", "Practice Test 1", "34", "Note Completion (Sec 4)", "enviroment", "environment", "SPELLING_WORD_LIMIT", "Dropped the 'n' in the middle of environment under speed pressure", "Check academic high-frequency spelling list daily", "Day 3", "Pending"],
        ["ERR-002", "Baseline", "Listening", "Practice Test 2", "18", "Multiple Choice (Sec 2)", "B (Friday)", "C (Monday)", "DISTRACTOR", "Fell for self-correction: speaker mentioned Friday then said 'postponed to Monday'", "Never write the first date heard; wait for transitional cues (However/Actually)", "Day 3", "Pending"],
        ["ERR-003", "Baseline", "Reading", "GT Practice 1", "7", "True/False/Not Given", "False", "Not Given", "LOGIC_ASSUMPTION", "Assumed company does not provide health insurance because text only mentioned dental; assumed absence meant False", "If the text does NOT explicitly state the opposite, it is NOT GIVEN. Do not extrapolate.", "Day 4", "Pending"],
        ["ERR-004", "Baseline", "Listening", "Practice Test 3", "38", "Note Completion (Sec 4)", "price", "expenditure", "PARAPHRASING", "Waited to hear the word 'price', but speaker used 'annual capital expenditure'", "Before audio plays, brainstorm 2-3 synonyms for every keyword prompt", "Day 5", "Pending"]
    ]
    for row_idx, r_data in enumerate(sample_errors, start=5):
        for col_idx, val in enumerate(r_data, start=1):
            cell = ws_log.cell(row=row_idx, column=col_idx, value=val)
            cell.font = normal_font
            cell.border = thin_border
            if col_idx in [1, 2, 3, 5, 9, 12, 13]:
                cell.alignment = Alignment(horizontal="center")
                if col_idx == 9:
                    cell.fill = red_fill
                    
    # 2. Category Analysis Tab
    ws_cat = wb.create_sheet(title="Category Analysis")
    ws_cat.views.sheetView[0].showGridLines = True
    ws_cat["A1"] = "ROOT CAUSE CATEGORY DISTRIBUTION"
    ws_cat["A1"].font = title_font
    
    cat_headers = ["Root Cause Category", "Description", "Listening Errors", "Reading Errors", "Writing/Speaking Errors", "Total Count", "Priority"]
    for col_idx, h in enumerate(cat_headers, start=1):
        cell = ws_cat.cell(row=3, column=col_idx, value=h)
        cell.fill = blue_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    categories = [
        ["PARAPHRASING", "Failed to connect audio/text synonym to question prompt", 1, 0, 0, "=SUM(C4:E4)", "CRITICAL"],
        ["DISTRACTOR", "Trapped by speaker self-correction or reading red herring", 1, 0, 0, "=SUM(C5:E5)", "HIGH"],
        ["SPELLING_WORD_LIMIT", "Misspelled word or violated word count constraints", 1, 0, 0, "=SUM(C6:E6)", "CRITICAL"],
        ["LOGIC_ASSUMPTION", "Brought outside world knowledge; confused False with Not Given", 0, 1, 0, "=SUM(C7:E7)", "CRITICAL"],
        ["CONCENTRATION", "Lost thread during continuous Section 4 monologue", 0, 0, 0, "=SUM(C8:E8)", "HIGH"],
        ["VOCABULARY", "Unknown definition in prompt or passage", 0, 0, 0, "=SUM(C9:E9)", "MEDIUM"],
        ["TIME_MANAGEMENT", "Ran out of time or panicked under clock pressure", 0, 0, 0, "=SUM(C10:E10)", "HIGH"],
        ["QUESTION_INTERPRETATION", "Misunderstood what the prompt specifically demanded", 0, 0, 0, "=SUM(C11:E11)", "MEDIUM"],
        ["GRAMMATICAL_ACCURACY", "Tense inconsistency, agreement error, or article omission", 0, 0, 0, "=SUM(C12:E12)", "HIGH"],
        ["STRUCTURE_IDEA", "Weak paragraph flow, lack of extension, poor cohesion", 0, 0, 0, "=SUM(C13:E13)", "HIGH"]
    ]
    for row_idx, r_data in enumerate(categories, start=4):
        for col_idx, val in enumerate(r_data, start=1):
            cell = ws_cat.cell(row=row_idx, column=col_idx, value=val)
            cell.font = normal_font
            cell.border = thin_border
            if col_idx in [1, 3, 4, 5, 6, 7]:
                cell.alignment = Alignment(horizontal="center")
                if col_idx == 7 and val == "CRITICAL":
                    cell.fill = red_fill
                    cell.font = bold_font
                    
    # Auto-adjust column widths
    for sheet in wb.worksheets:
        if sheet == default_sheet:
            continue
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or '')
                if len(val) > max_len and len(val) < 60:
                    max_len = len(val)
            sheet.column_dimensions[col_letter].width = max(max_len + 4, 12)
            
    wb.remove(default_sheet)
    wb.save("d:/IELTS-Prep/ERROR_LOG.xlsx")
    print("ERROR_LOG.xlsx generated successfully.")

if __name__ == "__main__":
    create_progress_tracker()
    create_error_log()

