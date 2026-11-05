import os

vocab_data = {
    1: {
        "theme": "Academic & Analytical Vocabulary (High Frequency L4 / R3 / W2)",
        "words": [
            {
                "word": "Substantial",
                "pos": "adjective",
                "eng_meaning": "Large in size, number, value, or importance.",
                "hindi_meaning": "काफी बड़ा, महत्वपूर्ण (Kaafi bada, mahatvapurna)",
                "collocations": ["substantial increase", "substantial amount", "substantial difference"],
                "example": "There has been a substantial increase in the number of remote employees over the last three years.",
                "ielts_usage": "Essential in Task 2 to replace overused words like 'big' or 'a lot'. Crucial in Listening Section 4 when speakers describe statistical shifts.",
                "nuance_vs_synonyms": "Unlike 'huge' (too informal for Task 2) or 'immense' (used for physical scale/nature), 'substantial' implies measurable, concrete significance."
            },
            {
                "word": "Discrepancy",
                "pos": "noun",
                "eng_meaning": "An unexpected difference between two things that should be the same.",
                "hindi_meaning": "विसंगति, फर्क, अंतर (Visangati, antar)",
                "collocations": ["noticeable discrepancy", "discrepancy between X and Y", "reconcile a discrepancy"],
                "example": "The committee identified a major discrepancy between the reported expenses and the actual bank transactions.",
                "ielts_usage": "High-frequency in Listening Section 3 (academic projects) and GT Task 1 formal complaint letters.",
                "nuance_vs_synonyms": "'Difference' is neutral. 'Discrepancy' implies that something is wrong, conflicting, or inconsistent."
            },
            {
                "word": "Mitigate",
                "pos": "verb",
                "eng_meaning": "To make something less harmful, serious, or severe.",
                "hindi_meaning": "कम करना, शांत करना, प्रभाव घटाना (Kam karna, prabhav ghatana)",
                "collocations": ["mitigate the impact", "mitigate risks", "mitigate climate change"],
                "example": "Implementing flexible working hours can substantially mitigate employee burnout.",
                "ielts_usage": "Band 7+ gold-standard verb for Task 2 Problem/Solution essays and Speaking Part 3.",
                "nuance_vs_synonyms": "Do not confuse with 'eliminate' (to remove completely). Mitigate means reducing the severity, not necessarily destroying it."
            },
            {
                "word": "Feasible",
                "pos": "adjective",
                "eng_meaning": "Possible, practical, and able to be achieved easily or conveniently.",
                "hindi_meaning": "व्यावहारिक, संभव (Vyavaharik, sambhav)",
                "collocations": ["financially feasible", "feasible alternative", "feasible solution"],
                "example": "While solar power is environmentally desirable, installing large-scale panels may not be financially feasible for small businesses.",
                "ielts_usage": "Ideal for Writing Task 2 when assessing proposed policies, and Task 1 when suggesting solutions to a manager.",
                "nuance_vs_synonyms": "'Possible' simply means it can happen; 'feasible' means it makes practical, logical, and financial sense."
            },
            {
                "word": "Prevalent",
                "pos": "adjective",
                "eng_meaning": "Widespread in a particular area or at a particular time.",
                "hindi_meaning": "प्रचलित, व्यापक (Prachalit, vyapak)",
                "collocations": ["widely prevalent", "prevalent attitude", "prevalent condition"],
                "example": "Sedentary lifestyles are increasingly prevalent among urban office workers.",
                "ielts_usage": "Replaces 'common' or 'everywhere' in Writing Task 2 and Speaking Part 3.",
                "nuance_vs_synonyms": "'Popular' implies people like it; 'prevalent' simply means it exists in large numbers (can be positive or negative)."
            },
            {
                "word": "Detrimental",
                "pos": "adjective",
                "eng_meaning": "Tending to cause harm or damage.",
                "hindi_meaning": "हानिकारक, नुकसानदेह (Hanikarak, nuksaandeh)",
                "collocations": ["detrimental effect", "detrimental to health", "highly detrimental"],
                "example": "Excessive screen time has a demonstrably detrimental effect on children's attention spans.",
                "ielts_usage": "High-scoring academic alternative to 'bad' or 'harmful' in Task 2 and Speaking Part 3.",
                "nuance_vs_synonyms": "'Dangerous' implies risk of physical injury. 'Detrimental' implies gradual corrosion, damage, or negative consequence."
            },
            {
                "word": "Imperative",
                "pos": "adjective / noun",
                "eng_meaning": "Of vital importance; crucial.",
                "hindi_meaning": "अति आवश्यक, अनिवार्य (Ati aavashyak, anivarya)",
                "collocations": ["it is imperative that", "economically imperative", "categorical imperative"],
                "example": "It is imperative that municipal authorities invest in clean public transit.",
                "ielts_usage": "Perfect for recommendations and conclusions in Writing Task 2 ('It is therefore imperative that...').",
                "nuance_vs_synonyms": "Stronger than 'important' or 'necessary'. It denotes absolute urgency."
            },
            {
                "word": "Alleviate",
                "pos": "verb",
                "eng_meaning": "To make suffering, deficiency, or a problem less severe.",
                "hindi_meaning": "राहत देना, कम करना (Rahat dena, kam karna)",
                "collocations": ["alleviate poverty", "alleviate congestion", "alleviate stress"],
                "example": "Constructing dedicated bicycle lanes would help alleviate traffic congestion in the city center.",
                "ielts_usage": "Regularly tested in Listening Section 4 and essential for Writing Task 2 solutions.",
                "nuance_vs_synonyms": "Used specifically with negative states (pain, suffering, traffic, poverty). You cannot 'alleviate happiness'."
            },
            {
                "word": "Proponent",
                "pos": "noun",
                "eng_meaning": "A person who advocates a theory, proposal, or project.",
                "hindi_meaning": "समर्थक, पक्षधर (Samarthak, pakshadhar)",
                "collocations": ["leading proponent", "proponents of nuclear energy", "staunch proponent"],
                "example": "Proponents of remote working argue that it boosts employee satisfaction and reduces overhead costs.",
                "ielts_usage": "Essential for Discuss Both Views essays in Task 2 to avoid writing 'people who like this'.",
                "nuance_vs_synonyms": "Opposite is 'opponent' or 'critic'. 'Supporter' is acceptable but 'proponent' is more academic."
            },
            {
                "word": "Exemplify",
                "pos": "verb",
                "eng_meaning": "To be a typical example of something, or to illustrate by giving an example.",
                "hindi_meaning": "उदाहरण देना, मिसाल पेश करना (Udaharan dena, misaal pesh karna)",
                "collocations": ["exemplify the trend", "clearly exemplify", "exemplify the challenges"],
                "example": "Canada's points-based immigration system exemplifies a merit-based approach to international talent recruitment.",
                "ielts_usage": "Replaces the elementary phrase 'shows an example of' in Task 2 body paragraphs.",
                "nuance_vs_synonyms": "'Illustrate' paints a picture; 'exemplify' means being the absolute textbook model of a phenomenon."
            }
        ]
    },
    2: {
        "theme": "Accommodation, Housing, Tenancy & Local Amenities (Section 1 L & R)",
        "words": [
            {
                "word": "Tenancy",
                "pos": "noun",
                "eng_meaning": "Possession of land or property as a tenant; the period of occupying property.",
                "hindi_meaning": "किरायेदारी (Kirayedari)",
                "collocations": ["tenancy agreement", "period of tenancy", "terminate a tenancy"],
                "example": "According to clause 4 of the tenancy agreement, notice must be served one calendar month in advance.",
                "ielts_usage": "GT Reading Section 1 & 2 lease contracts, and Task 1 letters to landlords.",
                "nuance_vs_synonyms": "'Rent' is the payment; 'tenancy' is the legal status and relationship of occupying."
            },
            {
                "word": "Furnished",
                "pos": "adjective",
                "eng_meaning": "Available with furniture already provided.",
                "hindi_meaning": "फर्नीचर सहित (Furniture sahit)",
                "collocations": ["fully furnished", "semi-furnished", "unfurnished apartment"],
                "example": "The rental listing specified that the flat is fully furnished, including white goods in the kitchen.",
                "ielts_usage": "Section 1 Listening form completion (note British term 'white goods' = fridge, washing machine).",
                "nuance_vs_synonyms": "'Equipped' usually refers to machines/tools; 'furnished' refers to living furniture."
            },
            {
                "word": "Deposit",
                "pos": "noun / verb",
                "eng_meaning": "A sum of money paid as a first installment or security against damage.",
                "hindi_meaning": "जमानत राशि, बयाना (Zamanat rashi)",
                "collocations": ["refundable deposit", "security deposit", "pay a deposit"],
                "example": "Tenants are required to lodge a security deposit equivalent to six weeks of rent.",
                "ielts_usage": "Frequent listening answer in Section 1 (e.g. 'How much deposit is required?').",
                "nuance_vs_synonyms": "Distinguish between 'holding deposit' (to reserve) and 'security deposit' (against damages)."
            },
            {
                "word": "Refurbish",
                "pos": "verb",
                "eng_meaning": "To renovate and redecorate something, especially a building.",
                "hindi_meaning": "नवीनीकरण करना, मरम्मत कर नया रूप देना (Navinikaran karna)",
                "collocations": ["recently refurbished", "refurbish the premises", "extensive refurbishment"],
                "example": "The community sports hall was closed throughout March while the gymnasium was refurbished.",
                "ielts_usage": "High frequency in Listening Section 2 (talks on local community centers) and GT Reading Section 1.",
                "nuance_vs_synonyms": "'Repair' means fixing something broken. 'Refurbish' means upgrading aesthetic and structural quality."
            },
            {
                "word": "Proximity",
                "pos": "noun",
                "eng_meaning": "Nearness in space, time, or relationship.",
                "hindi_meaning": "नजदीकी, निकटता (Najdeeki, nikat-ta)",
                "collocations": ["close proximity to", "in the immediate proximity", "proximity of public transit"],
                "example": "One major selling point of the residential complex is its close proximity to the metro station.",
                "ielts_usage": "Essential in GT Reading advertisements and Task 1 letters describing location advantages.",
                "nuance_vs_synonyms": "Used with 'to' ('in proximity to', never 'proximity of' in that sense). Much more formal than 'near'."
            },
            {
                "word": "Spacious",
                "pos": "adjective",
                "eng_meaning": "Having ample space; roomy.",
                "hindi_meaning": "खुला, विशाल, हवादार (Khula, vishaal)",
                "collocations": ["spacious layout", "spacious living room", "remarkably spacious"],
                "example": "Although the cottage looks compact from the exterior, it offers a remarkably spacious interior.",
                "ielts_usage": "Listening Section 1 & Speaking Part 1 when describing accommodation.",
                "nuance_vs_synonyms": "'Big' is bland; 'spacious' indicates pleasant, uncluttered open living space."
            },
            {
                "word": "Utilities",
                "pos": "noun (plural)",
                "eng_meaning": "Basic public services supplied to a property, such as electricity, gas, water, and sewerage.",
                "hindi_meaning": "बुनियादी जनसुविधाएं (बिजली, पानी, गैस) (Bijli, paani, gas)",
                "collocations": ["utilities included", "monthly utility bills", "public utilities"],
                "example": "The monthly rent is $1,400, but tenants are responsible for paying their own utilities.",
                "ielts_usage": "Constant distractor in Section 1 listening (checking whether rent includes utilities or not!).",
                "nuance_vs_synonyms": "Do not confuse with 'facilities' (gym, pool, parking). Utilities are core services."
            },
            {
                "word": "Premises",
                "pos": "noun (plural)",
                "eng_meaning": "A house or building, together with its land and outbuildings, occupied by a business or person.",
                "hindi_meaning": "परिसर, भवन (Parisar, bhavan)",
                "collocations": ["on the premises", "business premises", "vacate the premises"],
                "example": "Smoking is strictly prohibited anywhere on the premises, including the outdoor courtyards.",
                "ielts_usage": "GT Reading Section 1 & 2 safety notices and office regulations.",
                "nuance_vs_synonyms": "Always plural ('the premises are', not 'the premises is'). Refers to the physical grounds."
            },
            {
                "word": "Landlord / Landlady",
                "pos": "noun",
                "eng_meaning": "A person who rents land, a building, or an accommodation to a tenant.",
                "hindi_meaning": "मकान मालिक / मालकिन (Makaan maalik)",
                "collocations": ["private landlord", "dispute with the landlord", "notify the landlord"],
                "example": "I am writing to formally notify my landlord regarding the persistent water leak in the master bathroom.",
                "ielts_usage": "Primary recipient in Task 1 semi-formal complaint or maintenance letters.",
                "nuance_vs_synonyms": "In legal documents, often referred to as the 'lessor'."
            },
            {
                "word": "Disruption",
                "pos": "noun",
                "eng_meaning": "Disturbance or problems which interrupt an event, activity, or process.",
                "hindi_meaning": "बाधा, रुकावट (Baadha, rukawat)",
                "collocations": ["cause disruption", "minimize disruption", "service disruption"],
                "example": "Commuters experienced significant travel disruption following unexpected track maintenance.",
                "ielts_usage": "Frequent in GT Reading timetables and Task 1 letters requesting compensation.",
                "nuance_vs_synonyms": "'Delay' means taking longer; 'disruption' means complete upset or interruption of normal flow."
            }
        ]
    },
    3: {
        "theme": "Workplace, Employment, Contracts & Professional Life (GT Section 2)",
        "words": [
            {
                "word": "Entitlement",
                "pos": "noun",
                "eng_meaning": "The amount to which a person has a right; the official right to do or have something.",
                "hindi_meaning": "हकदारी, अधिकार (Haqdari, adhikar)",
                "collocations": ["annual leave entitlement", "benefit entitlement", "statutory entitlement"],
                "example": "Full-time employees have an entitlement to 25 days of paid annual leave.",
                "ielts_usage": "GT Reading Section 2 workplace contracts and staff handbook passages.",
                "nuance_vs_synonyms": "'Right' is general; 'entitlement' refers to a specific, quantified legal allowance."
            },
            {
                "word": "Remuneration",
                "pos": "noun",
                "eng_meaning": "Money paid for work or a service; financial compensation.",
                "hindi_meaning": "पारिश्रमिक, वेतन (Parishramik, vetan)",
                "collocations": ["remuneration package", "adequate remuneration", "financial remuneration"],
                "example": "The executive remuneration package consists of a base salary, performance bonuses, and stock options.",
                "ielts_usage": "High-scoring academic synonym for 'salary' or 'pay' in Task 2 and GT Reading.",
                "nuance_vs_synonyms": "Formal. 'Salary' is fixed monthly pay; 'remuneration' includes all benefits, perks, and bonuses."
            },
            {
                "word": "Appraisal",
                "pos": "noun",
                "eng_meaning": "An act of assessing something or someone, especially an employee's performance.",
                "hindi_meaning": "मूल्यांकन (Mulyankan)",
                "collocations": ["performance appraisal", "annual appraisal", "appraisal interview"],
                "example": "During her annual appraisal, Maria discussed her professional development goals with her supervisor.",
                "ielts_usage": "Standard workplace topic in GT Reading Section 2 and Speaking Part 1 & 2.",
                "nuance_vs_synonyms": "'Evaluation' is broad. 'Appraisal' specifically denotes a formal workplace performance review."
            },
            {
                "word": "Grievance",
                "pos": "noun",
                "eng_meaning": "A real or imagined cause for complaint, especially unfair treatment.",
                "hindi_meaning": "शिकायत, व्यथा (Shikayat, vyatha)",
                "collocations": ["file a grievance", "grievance procedure", "legitimate grievance"],
                "example": "If an employee feels unfairly treated, they are advised to initiate the company's formal grievance procedure.",
                "ielts_usage": "Key term in GT Reading Section 2 dispute-resolution texts and Task 1 workplace complaint letters.",
                "nuance_vs_synonyms": "'Complaint' is an act of complaining. 'Grievance' is the formal, documented wrong."
            },
            {
                "word": "Probationary",
                "pos": "adjective",
                "eng_meaning": "Relating to a period of testing or trial before someone is admitted to full status.",
                "hindi_meaning": "परिवीक्षाधीन, ट्रायल का समय (Parivikshadhin, trial period)",
                "collocations": ["probationary period", "probationary employee", "six-month probationary contract"],
                "example": "During the three-month probationary period, employment may be terminated with one week's notice.",
                "ielts_usage": "Universal term in GT Reading workplace agreements.",
                "nuance_vs_synonyms": "Do not confuse with 'temporary'; a probationary worker is in line for permanent status if approved."
            },
            {
                "word": "Redundancy",
                "pos": "noun",
                "eng_meaning": "The state of being no longer in employment because there is no more work available.",
                "hindi_meaning": "छंटनी (Chhantani)",
                "collocations": ["voluntary redundancy", "redundancy package", "face redundancy"],
                "example": "Following corporate restructuring, fifty administrative workers were offered voluntary redundancy.",
                "ielts_usage": "British English legal term used in IELTS tests. North American equivalent is 'layoff'.",
                "nuance_vs_synonyms": "Redundancy means the job itself has ceased to exist; it is NOT termination for poor performance."
            },
            {
                "word": "Compliance",
                "pos": "noun",
                "eng_meaning": "The state or fact of according with or meeting rules or standards.",
                "hindi_meaning": "अनुपालन (Anupalan - niyamon ka palan)",
                "collocations": ["regulatory compliance", "in compliance with", "ensure compliance"],
                "example": "All factory managers must ensure strict compliance with federal occupational health regulations.",
                "ielts_usage": "GT Reading workplace health & safety regulations.",
                "nuance_vs_synonyms": "Associated with law, policy, and safety standards."
            },
            {
                "word": "Discretion",
                "pos": "noun",
                "eng_meaning": "The freedom to decide what should be done in a particular situation.",
                "hindi_meaning": "विवेकाधिकार, अपनी मर्जी से निर्णय (Vivekadhikar)",
                "collocations": ["at the manager's discretion", "sole discretion", "exercise discretion"],
                "example": "Granting unpaid compassionate leave remains entirely at the employer's discretion.",
                "ielts_usage": "Tricky reading distractor in GT contracts (means it is not guaranteed by right!).",
                "nuance_vs_synonyms": "'Choice' is casual. 'Discretion' signifies authorized decision-making power."
            },
            {
                "word": "Incentive",
                "pos": "noun",
                "eng_meaning": "A thing that motivates or encourages someone to do something.",
                "hindi_meaning": "प्रोत्साहन, प्रेरक (Protsahan)",
                "collocations": ["financial incentive", "powerful incentive", "tax incentive"],
                "example": "The firm introduced performance-linked bonuses as an incentive for sales personnel.",
                "ielts_usage": "Frequent in Task 2 essays discussing workplace motivation and education policy.",
                "nuance_vs_synonyms": "An incentive encourages action before the fact; a reward is given after completion."
            },
            {
                "word": "Occupational",
                "pos": "adjective",
                "eng_meaning": "Relating to a job or profession.",
                "hindi_meaning": "व्यावसायिक, काम से संबंधित (Vyavasayik)",
                "collocations": ["occupational hazard", "occupational therapy", "occupational health"],
                "example": "Repetitive strain injury is recognized as a serious occupational hazard among computer programmers.",
                "ielts_usage": "High-frequency in GT Reading Section 2 health and safety documents.",
                "nuance_vs_synonyms": "Formal synonym for 'job-related' or 'work-related'."
            }
        ]
    },
    4: {
        "theme": "Education, Analytical Verbs & Academic Research (Section 3 L & R)",
        "words": [
            {
                "word": "Hypothesis",
                "pos": "noun",
                "eng_meaning": "A proposed explanation made on the basis of limited evidence as a starting point for investigation.",
                "hindi_meaning": "परिकल्पना, अनुमान (Parikalpana)",
                "collocations": ["test a hypothesis", "formulate a hypothesis", "support the hypothesis"],
                "example": "The research team conducted three distinct trials to test their initial hypothesis.",
                "ielts_usage": "Section 3 Listening (students discussing projects) and Section 3 Reading.",
                "nuance_vs_synonyms": "Plural is 'hypotheses' (spelled with -es, pronounced -eez). Traps candidates in listening!"
            },
            {
                "word": "Methodology",
                "pos": "noun",
                "eng_meaning": "A system of methods used in a particular area of study or activity.",
                "hindi_meaning": "कार्यप्रणाली, शोध पद्धति (Karyapranali)",
                "collocations": ["research methodology", "robust methodology", "questionable methodology"],
                "example": "The supervisor criticized the study's methodology because the sample size was statistically inadequate.",
                "ielts_usage": "Listening Section 3 dialogues between tutor and student.",
                "nuance_vs_synonyms": "Not just 'method' (a single technique). 'Methodology' is the overarching philosophical framework."
            },
            {
                "word": "Corroborate",
                "pos": "verb",
                "eng_meaning": "To confirm or give support to a statement, theory, or finding.",
                "hindi_meaning": "पुष्टि करना, समर्थन करना (Pushti karna)",
                "collocations": ["corroborate evidence", "findings corroborate", "corroborate the claim"],
                "example": "Subsequent laboratory experiments failed to corroborate the researcher's preliminary claims.",
                "ielts_usage": "Reading Section 3 (academic passages) and Band 8 Writing Task 2.",
                "nuance_vs_synonyms": "Much more precise than 'prove' or 'support'. Implies independent verification."
            },
            {
                "word": "Plagiarism",
                "pos": "noun",
                "eng_meaning": "The practice of taking someone else's work or ideas and passing them off as one's own.",
                "hindi_meaning": "साहित्यिक चोरी, नकल (Sahityik chori)",
                "collocations": ["commit plagiarism", "detect plagiarism", "plagiarism guidelines"],
                "example": "University students face immediate suspension if they are found guilty of academic plagiarism.",
                "ielts_usage": "Listening Section 3 college assignment rules.",
                "nuance_vs_synonyms": "Distinct from 'copyright infringement'; plagiarism is an intellectual fraud."
            },
            {
                "word": "Empirical",
                "pos": "adjective",
                "eng_meaning": "Based on, concerned with, or verifiable by observation or experience rather than pure theory.",
                "hindi_meaning": "अनुभवजन्य, प्रयोगसिद्ध (Anubhavjanya, prayog-siddha)",
                "collocations": ["empirical evidence", "empirical study", "empirical data"],
                "example": "There is substantial empirical evidence demonstrating that bilingualism improves cognitive flexibility.",
                "ielts_usage": "Academic Reading Section 3 and high-scoring Task 2 essays.",
                "nuance_vs_synonyms": "The opposite of 'theoretical' or 'speculative'."
            },
            {
                "word": "Comprehensive",
                "pos": "adjective",
                "eng_meaning": "Complete; including all or nearly all elements or aspects of something.",
                "hindi_meaning": "विस्तृत, व्यापक, सम्पूर्ण (Vistrit, sampurna)",
                "collocations": ["comprehensive review", "comprehensive approach", "comprehensive training"],
                "example": "The department published a comprehensive report detailing national energy consumption.",
                "ielts_usage": "Listening and Reading; replaces 'full' or 'complete' in Task 1 & 2.",
                "nuance_vs_synonyms": "Do not confuse with 'comprehensible' (which means easy to understand)."
            },
            {
                "word": "Synthesize",
                "pos": "verb",
                "eng_meaning": "To combine a number of things into a coherent whole.",
                "hindi_meaning": "संश्लेषण करना, जोड़कर एक करना (Sanshleshan karna)",
                "collocations": ["synthesize data", "synthesize information", "synthesize findings"],
                "example": "Students are required to synthesize information from multiple academic journals for their dissertation.",
                "ielts_usage": "Reading Section 3 and Speaking Part 3.",
                "nuance_vs_synonyms": "'Combine' is physical; 'synthesize' involves intellectual integration to create something new."
            },
            {
                "word": "Rigorous",
                "pos": "adjective",
                "eng_meaning": "Extremely thorough, exhaustive, or accurate.",
                "hindi_meaning": "कठोर, सख्त, बारीकी से किया गया (Kathor, bariki se kiya gaya)",
                "collocations": ["rigorous testing", "rigorous standards", "rigorous analysis"],
                "example": "Before any pharmaceutical drug is approved, it undergoes rigorous clinical trials.",
                "ielts_usage": "High-level modifier for Task 2 and Reading.",
                "nuance_vs_synonyms": "'Strict' usually relates to rules/people; 'rigorous' describes the depth and precision of a process."
            },
            {
                "word": "Ambiguous",
                "pos": "adjective",
                "eng_meaning": "Open to more than one interpretation; having a double meaning; unclear.",
                "hindi_meaning": "अस्पष्ट, अनेकार्थी (Aspasht, anekarthi)",
                "collocations": ["ambiguous statement", "deliberately ambiguous", "morally ambiguous"],
                "example": "The contractual wording was dangerously ambiguous, leading to a prolonged dispute between both parties.",
                "ielts_usage": "Reading Section 3 and Listening Section 3.",
                "nuance_vs_synonyms": "'Vague' means lacking detail; 'ambiguous' means it can be understood in two conflicting ways."
            },
            {
                "word": "Curriculum",
                "pos": "noun",
                "eng_meaning": "The subjects comprising a course of study in a school or college.",
                "hindi_meaning": "पाठ्यक्रम (Pathyakram)",
                "collocations": ["school curriculum", "core curriculum", "curriculum reform"],
                "example": "Critics argue that the modern secondary school curriculum neglects essential financial literacy skills.",
                "ielts_usage": "Common topic in Task 2 education essays and Speaking Part 1 & 3.",
                "nuance_vs_synonyms": "Plural is 'curricula' (or 'curriculums'). 'Syllabus' is the outline for one specific subject; 'curriculum' is the total educational programme."
            }
        ]
    },
    5: {
        "theme": "Environment, Conservation & Urban Ecology (High Frequency L4 / R3 / W2)",
        "words": [
            {
                "word": "Biodiversity",
                "pos": "noun",
                "eng_meaning": "The variety of plant and animal life in the world or in a particular habitat.",
                "hindi_meaning": "जैव विविधता (Jaiv vividhta)",
                "collocations": ["loss of biodiversity", "conserve biodiversity", "rich biodiversity"],
                "example": "Deforestation in the Amazon basin poses an existential threat to global biodiversity.",
                "ielts_usage": "Essential in Listening Section 4 ecological lectures and Task 2 environment essays.",
                "nuance_vs_synonyms": "Broad biological concept; do not write 'variety of animals' when 'biodiversity' is available."
            },
            {
                "word": "Ecosystem",
                "pos": "noun",
                "eng_meaning": "A biological community of interacting organisms and their physical environment.",
                "hindi_meaning": "पारिस्थितिकी तंत्र (Paristhitiki tantra)",
                "collocations": ["fragile ecosystem", "marine ecosystem", "disrupt the ecosystem"],
                "example": "The introduction of invasive species can destabilize entire freshwater ecosystems.",
                "ielts_usage": "Listening Section 4 anchor word.",
                "nuance_vs_synonyms": "'Habitat' is the home of one species; 'ecosystem' is the entire interactive network."
            },
            {
                "word": "Degradation",
                "pos": "noun",
                "eng_meaning": "The process in which the quality or condition of something becomes worse.",
                "hindi_meaning": "क्षरण, गिरावट, ह्रास (Ksharan, girawat)",
                "collocations": ["environmental degradation", "soil degradation", "land degradation"],
                "example": "Intensive agricultural practices have accelerated soil degradation across the arid plains.",
                "ielts_usage": "Academic synonym for 'damage' or 'ruin' in Task 2 and Reading.",
                "nuance_vs_synonyms": "Implies progressive, systemic deterioration over time."
            },
            {
                "word": "Deplete",
                "pos": "verb",
                "eng_meaning": "To use up the supply or resources of something.",
                "hindi_meaning": "समाप्त करना, खत्म कर देना (Samapt karna, khatam karna)",
                "collocations": ["deplete natural resources", "severely depleted", "deplete fish stocks"],
                "example": "Overfishing has severely depleted bluefin tuna populations across the Mediterranean.",
                "ielts_usage": "Listening Section 4 note completion.",
                "nuance_vs_synonyms": "Noun form is 'depletion' (e.g. 'ozone layer depletion')."
            },
            {
                "word": "Renewable",
                "pos": "adjective",
                "eng_meaning": "Capable of being replenished naturally within a human timescale.",
                "hindi_meaning": "नवीकरणीय (Navikaraniya)",
                "collocations": ["renewable energy", "renewable resources", "transition to renewables"],
                "example": "Governments must offer tax subsidies to accelerate the transition to renewable energy sources.",
                "ielts_usage": "Task 2 and Speaking Part 3 on energy policies.",
                "nuance_vs_synonyms": "Opposite is 'non-renewable' or 'finite' (e.g. fossil fuels)."
            },
            {
                "word": "Conservation",
                "pos": "noun",
                "eng_meaning": "The preservation and careful management of the environment and of natural resources.",
                "hindi_meaning": "संरक्षण (Sanrakshan)",
                "collocations": ["wildlife conservation", "energy conservation", "conservation effort"],
                "example": "Community-led conservation efforts have helped stabilize Bengal tiger numbers in India.",
                "ielts_usage": "Listening Section 4 and Reading Section 3.",
                "nuance_vs_synonyms": "'Preservation' means leaving untouched; 'conservation' implies sustainable, wise human management."
            },
            {
                "word": "Sustainable",
                "pos": "adjective",
                "eng_meaning": "Able to be maintained at a certain rate or level without exhausting natural resources.",
                "hindi_meaning": "सतत, टिकाऊ (Satat, tikaau)",
                "collocations": ["sustainable development", "sustainable practices", "environmentally sustainable"],
                "example": "Urban planners must adopt sustainable practices to prevent uncontrolled city sprawl.",
                "ielts_usage": "Standard collocations in Task 2 and Reading Section 3.",
                "nuance_vs_synonyms": "Core global benchmark concept for Express Entry candidates."
            },
            {
                "word": "Urbanization",
                "pos": "noun",
                "eng_meaning": "The process of making an area more urban; the progressive movement of populations into cities.",
                "hindi_meaning": "शहरीकरण (Shahrikaran)",
                "collocations": ["rapid urbanization", "unplanned urbanization", "consequences of urbanization"],
                "example": "Rapid urbanization has put severe strain on municipal water and sanitation infrastructures.",
                "ielts_usage": "High frequency in Reading Section 3 and Writing Task 2.",
                "nuance_vs_synonyms": "Refers to demographic movement and physical expansion of cities."
            },
            {
                "word": "Contamination",
                "pos": "noun",
                "eng_meaning": "The action or state of making something impure by polluting or poisoning.",
                "hindi_meaning": "दूषित होना, संदूषण (Dooshit hona, sandushan)",
                "collocations": ["water contamination", "radioactive contamination", "soil contamination"],
                "example": "Industrial runoff caused widespread chemical contamination of the local drinking supply.",
                "ielts_usage": "Listening Section 4 spelling trap; Reading passages.",
                "nuance_vs_synonyms": "'Pollution' is the broader environmental state; 'contamination' implies foreign hazardous agents entering a specific substance."
            },
            {
                "word": "Habitat",
                "pos": "noun",
                "eng_meaning": "The natural home or environment of an animal, plant, or other organism.",
                "hindi_meaning": "प्राकृतिक आवास (Prakritik aawas)",
                "collocations": ["natural habitat", "habitat destruction", "loss of habitat"],
                "example": "Urban expansion is encroaching upon the natural habitat of migratory birds.",
                "ielts_usage": "Beware singular vs plural: 'habitat' vs 'habitats' in Section 4 listening!",
                "nuance_vs_synonyms": "'Inhabitation' is the act of living; 'habitat' is the actual ecological terrain."
            }
        ]
    },
    6: {
        "theme": "Societal Trends, Technology & Work-Life Balance (Task 2 & Speaking Part 3)",
        "words": [
            {
                "word": "Proliferation",
                "pos": "noun",
                "eng_meaning": "Rapid increase in the number or amount of something.",
                "hindi_meaning": "प्रसार, तेजी से वृद्धि (Prasaar, tezi se vriddhi)",
                "collocations": ["proliferation of smartphones", "nuclear proliferation", "rapid proliferation"],
                "example": "The proliferation of digital communication tools has permanently altered traditional workplace hierarchies.",
                "ielts_usage": "Band 8+ noun in Task 2 introductions to replace 'many people now use'.",
                "nuance_vs_synonyms": "Implies explosive, uncontrolled multiplication."
            },
            {
                "word": "Automation",
                "pos": "noun",
                "eng_meaning": "The use of largely automatic equipment in a system of manufacturing or other production process.",
                "hindi_meaning": "स्वचालन (Svachalan - machines doing human work)",
                "collocations": ["workplace automation", "industrial automation", "rise of automation"],
                "example": "While automation boosts corporate efficiency, it threatens routine administrative employment.",
                "ielts_usage": "Core theme in Canadian PR essays regarding future labor markets.",
                "nuance_vs_synonyms": "'Mechanization' is using physical machines; 'automation' involves software/AI performing decisions."
            },
            {
                "word": "Indispensable",
                "pos": "adjective",
                "eng_meaning": "Absolutely necessary; impossible to be without.",
                "hindi_meaning": "अपरिहार्य, जिसके बिना काम न चले (Apariharya)",
                "collocations": ["indispensable tool", "prove indispensable", "indispensable part of life"],
                "example": "High-speed internet has evolved from a luxury into an indispensable utility for remote workers.",
                "ielts_usage": "Upgraded Band 7+ replacement for 'very important' or 'essential'.",
                "nuance_vs_synonyms": "Spelling trap: note ending is '-able', not '-ible'!"
            },
            {
                "word": "Preoccupied",
                "pos": "adjective",
                "eng_meaning": "Engrossed in thought; distracted.",
                "hindi_meaning": "चिंतित, किसी विचार में खोया हुआ (Chintit, khoya hua)",
                "collocations": ["preoccupied with work", "increasingly preoccupied", "mentally preoccupied"],
                "example": "Modern professionals are often so preoccupied with career advancement that they neglect physical health.",
                "ielts_usage": "Speaking Part 1, 2, and 3 when discussing stress and lifestyles.",
                "nuance_vs_synonyms": "Used with preposition 'with'."
            },
            {
                "word": "Obsolete",
                "pos": "adjective",
                "eng_meaning": "No longer produced or used; out of date.",
                "hindi_meaning": "अप्रचलित, पुराना (Aprachalit, purana)",
                "collocations": ["render obsolete", "become obsolete", "virtually obsolete"],
                "example": "Generative artificial intelligence may render several entry-level coding tasks obsolete.",
                "ielts_usage": "Task 2 technology topics and Reading Section 3.",
                "nuance_vs_synonyms": "'Old' is chronological age; 'obsolete' means useless because a superior replacement exists."
            },
            {
                "word": "Sedentary",
                "pos": "adjective",
                "eng_meaning": "Tending to spend much time seated; somewhat inactive.",
                "hindi_meaning": "गतिहीन, बैठे रहने वाला (Gatiheen, baithe rehne wala)",
                "collocations": ["sedentary lifestyle", "sedentary job", "sedentary habits"],
                "example": "Adopting a sedentary lifestyle dramatically increases susceptibility to cardiovascular disease.",
                "ielts_usage": "High-scoring collocation for health, lifestyle, and work essays.",
                "nuance_vs_synonyms": "Specifically denotes physical stillness or seated posture."
            },
            {
                "word": "Cohesion",
                "pos": "noun",
                "eng_meaning": "The action or fact of forming a united whole; togetherness.",
                "hindi_meaning": "एकजुटता, सामंजस्य (Ekjutta, samanjasya)",
                "collocations": ["social cohesion", "community cohesion", "team cohesion"],
                "example": "Community cultural festivals play an essential role in fostering social cohesion among diverse immigrant populations.",
                "ielts_usage": "Vital for societal essays in Task 2 and Speaking Part 3.",
                "nuance_vs_synonyms": "Also an official IELTS criteria term ('Coherence and Cohesion')."
            },
            {
                "word": "Autonomy",
                "pos": "noun",
                "eng_meaning": "The right or condition of self-government; freedom from external control or influence.",
                "hindi_meaning": "स्वायत्तता, स्वतंत्रता (Swayattata, swatantrata)",
                "collocations": ["greater autonomy", "individual autonomy", "workplace autonomy"],
                "example": "Employees who enjoy schedule autonomy report higher job satisfaction and lower attrition rates.",
                "ielts_usage": "Workplace and management topics in Task 2 and GT Reading.",
                "nuance_vs_synonyms": "'Independence' is general; 'autonomy' specifically means having the authority to make one's own choices."
            },
            {
                "word": "Isolation",
                "pos": "noun",
                "eng_meaning": "The state of being separated from other people or things.",
                "hindi_meaning": "अलगाव, एकांत (Algaav, ekaant)",
                "collocations": ["social isolation", "feelings of isolation", "geographical isolation"],
                "example": "Without regular team interactions, prolonged remote work can inadvertently induce feelings of isolation.",
                "ielts_usage": "Common in Task 2 essays on remote work, aging populations, and urbanization.",
                "nuance_vs_synonyms": "'Solitude' is peaceful being alone; 'isolation' carries a negative, disconnected connotation."
            },
            {
                "word": "Disproportionate",
                "pos": "adjective",
                "eng_meaning": "Too large or too small in comparison with something else.",
                "hindi_meaning": "असंगत, अनुपातहीन (Asangat, anupaat-heen)",
                "collocations": ["disproportionate impact", "disproportionate amount", "disproportionately affected"],
                "example": "Rising public transit fares impose a disproportionate financial burden on low-income households.",
                "ielts_usage": "Essential modifier for Task 2 socio-economic analysis.",
                "nuance_vs_synonyms": "Adverb form 'disproportionately' is exceptional for demonstrating Band 7+ grammatical range."
            }
        ]
    },
    7: {
        "theme": "Week 1 Consolidation, Linking Devices & Discourse Markers",
        "words": [
            {
                "word": "Notwithstanding",
                "pos": "preposition / adverb",
                "eng_meaning": "In spite of; despite.",
                "hindi_meaning": "के बावजूद (Ke baawajood)",
                "collocations": ["notwithstanding the challenges", "notwithstanding the fact that"],
                "example": "Notwithstanding the economic headwinds, the technological sector continued to generate new vacancies.",
                "ielts_usage": "High-scoring formal concession marker for Task 2 body paragraphs.",
                "nuance_vs_synonyms": "Formal alternative to 'despite' or 'in spite of'. Can be placed at the beginning or end of a phrase."
            },
            {
                "word": "Consequently",
                "pos": "adverb",
                "eng_meaning": "As a result.",
                "hindi_meaning": "परिणामस्वरूप (Parinaam-swaroop)",
                "collocations": ["and consequently", "consequently led to"],
                "example": "Fuel prices soared dramatically; consequently, shipping costs increased across all consumer retail goods.",
                "ielts_usage": "Standard Band 7+ cause-and-effect transition marker (replaces simple 'so').",
                "nuance_vs_synonyms": "Follows a semi-colon or starts a new sentence with a comma."
            },
            {
                "word": "Conversely",
                "pos": "adverb",
                "eng_meaning": "Introducing a statement or idea which reverses one that has just been made or referred to.",
                "hindi_meaning": "इसके विपरीत (Iske viprit)",
                "collocations": ["conversely, some argue", "or conversely"],
                "example": "High interest rates encourage saving; conversely, they discourage business borrowing and capital investment.",
                "ielts_usage": "Band 7+ contrast marker in Task 2 discussion essays.",
                "nuance_vs_synonyms": "Unlike 'however', 'conversely' specifically compares two opposing sides of a coin."
            },
            {
                "word": "Furthermore",
                "pos": "adverb",
                "eng_meaning": "In addition to what has already been said; moreover.",
                "hindi_meaning": "इसके अलावा, और भी (Iske alawa)",
                "collocations": ["furthermore, it is evident", "furthermore, research indicates"],
                "example": "Recycling reduces landfill volume; furthermore, it conserves finite energy resources.",
                "ielts_usage": "Used to add an additional supporting argument in Task 2 body paragraphs.",
                "nuance_vs_synonyms": "Do not use 'moreover' and 'furthermore' consecutively in the same paragraph."
            },
            {
                "word": "Predominantly",
                "pos": "adverb",
                "eng_meaning": "Mainly; for the most part.",
                "hindi_meaning": "मुख्य रूप से (Mukhya roop se)",
                "collocations": ["predominantly urban", "predominantly positive", "rely predominantly on"],
                "example": "The local agricultural economy remains predominantly dependent on seasonal monsoon precipitation.",
                "ielts_usage": "Academic qualifier to avoid absolute over-generalizations in Task 2 and Reading.",
                "nuance_vs_synonyms": "Replaces crude generalizations like 'mostly' or 'all'."
            },
            {
                "word": "Invariably",
                "pos": "adverb",
                "eng_meaning": "In every case or on every occasion; always.",
                "hindi_meaning": "हमेशा, बिना अपवाद के (Hamesha, bina apwaad ke)",
                "collocations": ["invariably leads to", "invariably results in", "almost invariably"],
                "example": "Failing to proofread writing submissions almost invariably results in careless mechanical errors.",
                "ielts_usage": "Strengthens conclusion statements in Task 2 and Speaking Part 3.",
                "nuance_vs_synonyms": "Much more sophisticated than 'always'."
            },
            {
                "word": "Subsequent",
                "pos": "adjective",
                "eng_meaning": "Coming after something in time; following.",
                "hindi_meaning": "बाद का, आगामी (Baad ka, aagami)",
                "collocations": ["subsequent research", "subsequent developments", "in subsequent years"],
                "example": "The initial trial was inconclusive, but subsequent testing confirmed the drug's therapeutic efficacy.",
                "ielts_usage": "High-frequency in Reading chronological passages and Task 1 process letters.",
                "nuance_vs_synonyms": "'Next' is casual; 'subsequent' formalizes the temporal sequence."
            },
            {
                "word": "Paradoxically",
                "pos": "adverb",
                "eng_meaning": "In a seemingly absurd or self-contradictory way that may nonetheless be true.",
                "hindi_meaning": "विरोधाभासी रूप से (Virodhabhasi roop se)",
                "collocations": ["paradoxically enough", "paradoxically, the data shows"],
                "example": "Paradoxically, hyper-connectivity through social platforms has made modern citizens feel more socially estranged.",
                "ielts_usage": "Shows high lexical sophistication and critical thinking in Task 2 and Speaking Part 3.",
                "nuance_vs_synonyms": "Highlights a surprising, counter-intuitive reality."
            },
            {
                "word": "Ubiquitous",
                "pos": "adjective",
                "eng_meaning": "Present, appearing, or found everywhere.",
                "hindi_meaning": "सर्वव्यापी, हर जगह मौजूद (Sarvavyapi)",
                "collocations": ["ubiquitous presence", "become ubiquitous", "ubiquitous smartphone"],
                "example": "In contemporary metropolises, high-definition security cameras have become almost ubiquitous.",
                "ielts_usage": "Advanced alternative to 'found everywhere' in modern society essays.",
                "nuance_vs_synonyms": "Stronger and more academic than 'widespread'."
            },
            {
                "word": "Prerequisite",
                "pos": "noun / adjective",
                "eng_meaning": "A thing that is required as a prior condition for something else to happen or exist.",
                "hindi_meaning": "आवश्यक पूर्व शर्त (Aavashyak poorv shart)",
                "collocations": ["essential prerequisite", "prerequisite for success", "prerequisite qualification"],
                "example": "Mastering IELTS listening paraphrasing techniques is an essential prerequisite for achieving Band 8.0.",
                "ielts_usage": "Task 1 workplace letters, Task 2 education essays, and GT Reading policies.",
                "nuance_vs_synonyms": "'Requirement' is general; 'prerequisite' specifically must be fulfilled BEFORE moving forward."
            }
        ]
    }
}

for day_num, data in vocab_data.items():
    md_content = f"# IELTS GT Vocabulary Bank — Day {day_num:02d}\n"
    md_content += f"### Theme: {data['theme']}\n\n"
    md_content += "Study these 10 targeted words. Memorize the collocations, Hinglish nuance, and IELTS exam usage.\n\n---\n\n"
    
    for idx, item in enumerate(data['words'], start=1):
        md_content += f"## {idx}. {item['word']} *({item['pos']})*\n"
        md_content += f"- **English Meaning:** {item['eng_meaning']}\n"
        md_content += f"- **Hindi / Hinglish Nuance:** {item['hindi_meaning']}\n"
        md_content += f"- **Collocations:** `{', '.join(item['collocations'])}`\n"
        md_content += f"- **Example Sentence:** *\"{item['example']}\"*\n"
        md_content += f"- **IELTS Exam Application:** {item['ielts_usage']}\n"
        md_content += f"- **Trap / Nuance Distinction:** {item['nuance_vs_synonyms']}\n\n"
        md_content += "---\n\n"
        
    filepath = f"d:/IELTS-Prep/VOCABULARY/DAILY_WORDS/DAY_{day_num:02d}_VOCAB.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

# Week 1 Revision List
rev_content = "# Week 1 Vocabulary Master Spaced Repetition List (70 High-Yield Terms)\n\n"
rev_content += "Use this list for active recall on Day 7. Cover the definition column and test your recall!\n\n"
rev_content += "| Day | Term | Part of Speech | Core Meaning | Key Collocation | IELTS Context |\n"
rev_content += "|:---:|---|:---:|---|---|---|\n"

for day_num, data in vocab_data.items():
    for item in data['words']:
        colloc = item['collocations'][0] if item['collocations'] else "-"
        rev_content += f"| Day {day_num:02d} | **{item['word']}** | *{item['pos']}* | {item['eng_meaning'][:45]}... | `{colloc}` | {item['ielts_usage'][:35]}... |\n"

with open("d:/IELTS-Prep/VOCABULARY/REVISION_LIST/WEEK_01_REVISION_LIST.md", "w", encoding="utf-8") as f:
    f.write(rev_content)

print("Vocabulary files generated successfully for Days 01 to 07.")

