import win32com.client
import os
import time

def generate_day_audio(day_num, script_lines, voice_name=None):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    stream = win32com.client.Dispatch("SAPI.SpFileStream")
    
    out_dir = f"d:/IELTS-Prep/DAILY_ASSIGNMENTS/WEEK_01/DAY_{day_num:02d}"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "audio_track.wav")
    
    # Select voice if specified
    if voice_name:
        for v in speaker.GetVoices():
            if voice_name.lower() in v.GetDescription().lower():
                speaker.Voice = v
                break
                
    speaker.Rate = -1 # Clear IELTS test pace
    stream.Open(out_path, 3) # SSFMCreateForWrite
    speaker.AudioOutputStream = stream
    
    for line in script_lines:
        speaker.Speak(line)
        time.sleep(0.1)
        
    stream.Close()
    print(f"Generated Day {day_num:02d} audio: {out_path} ({os.path.getsize(out_path)} bytes)")

# Audio Scripts
scripts = {
    1: [
        "International English Language Testing System. Week 1, Day 1 Diagnostic Listening Assessment.",
        "You will hear two short audio recordings. Recording 1 is a conversation regarding course registration. Recording 2 is an academic lecture on urban energy systems.",
        "First, you have some time to look at Questions 1 to 5.",
        "Now listen carefully and answer Questions 1 to 5.",
        "Good morning, Central Continuing Education office. How may I assist you today?",
        "Hello. I'd like to enroll in the advanced project management evening course, please.",
        "Certainly. May I take your full name first?",
        "Yes, it's Julian... Julian Bancroft. That's B-A-N-C-R-O-F-T.",
        "Thank you, Mr. Bancroft. And your contact telephone number?",
        "It's 0-7-7-0-0... wait, that's my previous home number. My current mobile is 0-7-8-9-2, 4-4-1, 8-3-2.",
        "Got it. Now, the course is offered on two different days: Tuesday evenings or Thursday evenings.",
        "I originally hoped for Thursday, but due to my work commitments, Tuesday will have to be the one.",
        "Understood. The course begins on the 14th of November. You will need to bring your own laptop. Software licenses are provided by the college.",
        "And what is the total tuition fee?",
        "The standard fee is 480 pounds, but with the early registration discount applied today, it comes to 420 pounds.",
        "Now listen to Recording 2 and answer Questions 6 to 10.",
        "Good afternoon, everyone. Today we are examining urban microgrids and localized renewable energy infrastructure.",
        "Traditional electrical grids suffer from significant transmission loss when electricity travels across long geographical distances.",
        "In contrast, modern smart microgrids generate power directly within urban neighborhoods, predominantly utilizing rooftop solar installations.",
        "A critical breakthrough in this technology has been the integration of centralized battery storage facilities.",
        "These batteries store surplus energy generated during peak daylight hours. Then, during the evening peak demand, this stored electricity is automatically released into local households.",
        "However, researchers note that the greatest impediment to widespread urban adoption is not technical feasibility, but rather the initial capital expenditure required for installation.",
        "Furthermore, municipal authorities must update outdated zoning regulations to permit shared energy trading between private property owners.",
        "That concludes the listening recording for Day 1."
    ],
    2: [
        "IELTS General Training Listening. Week 1, Day 2. Section 1 Practice: Form Completion.",
        "You will hear a telephone conversation between a customer and a manager at Apex Self-Storage.",
        "First, look at Questions 1 to 10.",
        "Now listen carefully and answer Questions 1 to 10.",
        "Good morning, Apex Self-Storage. David speaking. How can I help you?",
        "Hello, I am looking to rent a storage unit for some household furniture and personal boxes for about two months.",
        "Certainly, madam. May I have your name, please?",
        "Yes, it is Eleanor Vance. That is V-A-N-C-E.",
        "Thank you, Ms. Vance. And your current postcode?",
        "It is SW4 9LH. That's Sierra Whiskey four, nine Lima Hotel.",
        "Great. Now, in terms of volume, how much are you looking to store?",
        "Well, I have the contents of a one-bedroom flat. Mostly a double bed, sofa, dining table, and roughly fifteen cardboard boxes.",
        "Right. For that volume, our standard twenty-five square metre unit would be ideal. Though if you have extra appliances, you might consider the thirty-five square metre space.",
        "No, twenty-five square metres should be plenty.",
        "Now, regarding pricing: the standard rate for that unit is forty-five pounds per week.",
        "Wait, does that include insurance cover?",
        "Good question. The basic forty-five pounds includes standard insurance up to five thousand pounds of value. If you need enhanced cover up to fifteen thousand, it is an extra eight pounds per week.",
        "Standard cover will be adequate. And when would you like to move your belongings in?",
        "Next Saturday, which will be the 18th of November.",
        "Perfect. Please note our vehicle access gates open at 7:00 AM and close strictly at 8:30 PM. To access the facility, every customer is assigned a security PIN code.",
        "Your provisional access code will be 9-4-2-0. Please keep that confidential.",
        "Understood. Thank you very much.",
        "That is the end of Section 1."
    ],
    3: [
        "IELTS Listening. Week 1, Day 3. Section 2: Monologue on Community Amenities.",
        "You will hear the manager of the newly refurbished Riverside Community and Leisure Centre giving a welcome talk.",
        "First, look at Questions 1 to 10.",
        "Good morning and welcome to the Riverside Community Centre. We are thrilled to finally reopen our doors following six months of extensive refurbishment.",
        "Let me highlight some of our upgraded amenities. To your left as you enter through the main foyer, you will find our newly expanded cardiovascular gymnasium.",
        "Unlike the old layout, the gym now overlooks the outdoor botanical gardens rather than the car park, providing a much more relaxing atmosphere while working out.",
        "Directly across from the gym, on the eastern wing, is our twenty-five metre heated swimming pool. Please note that lane swimming is reserved for adults between 6:30 and 8:30 AM every weekday.",
        "For families with young children, we have introduced a dedicated creche facility on the ground floor. It operates Monday to Friday, from 9:00 AM until 1:00 PM.",
        "Now, regarding our membership tiers: the Bronze tier offers access to gym facilities only during off-peak hours.",
        "The Silver tier includes full gym and swimming access at any time.",
        "However, most of our members opt for the Gold package, which additionally grants complimentary access to all weekend fitness classes and personal coaching clinics.",
        "Annual members receive a complimentary sports bag and a water bottle upon registering at the reception desk.",
        "Please remember that outdoor footwear is strictly prohibited inside the dance studios and squash courts.",
        "Thank you for your time, and enjoy exploring the facility today."
    ],
    4: [
        "IELTS Listening. Week 1, Day 4. Section 3: Academic Discussion.",
        "You will hear two university students, Mark and Sarah, discussing their group project on consumer purchasing habits with their tutor, Dr. Harrison.",
        "First, look at Questions 1 to 10.",
        "Come in, Mark, Sarah. Have a seat. How is your project on supermarket retail psychology progressing?",
        "Well, Dr. Harrison, we have gathered most of our preliminary survey data from two hundred shoppers.",
        "That is a respectable sample size. What did you discover regarding impulse purchasing near checkouts?",
        "Interestingly, Sarah and I initially predicted that confectionary and snacks would be the most common impulse purchase.",
        "Yes, but the data showed something quite different. Over sixty percent of unplanned basket additions were actually discounted household toiletries rather than food.",
        "Fascinating. And what methodology did you employ to track customer navigation through the aisles?",
        "We used observational heat-mapping over a three-day period.",
        "Did you encounter any ethical dilemmas while observing shoppers?",
        "We did. We had to ensure that individual customer identities were completely anonymized in our video recordings.",
        "Excellent. Now, for your final written report, remember that the statistical analysis must be integrated directly into your discussion section, rather than relegated to an appendix.",
        "We will make sure to do that. Thank you, Dr. Harrison."
    ],
    5: [
        "IELTS Listening. Week 1, Day 5. Section 4: Academic Monologue.",
        "You will hear an environmental sciences lecturer discussing global coral reef degradation and artificial reef engineering.",
        "First, look at Questions 1 to 10.",
        "Welcome to today's lecture on marine conservation engineering. Today, we will examine the restoration of tropical coral reef ecosystems.",
        "Coral reefs occupy less than one percent of the ocean floor, yet they sustain more than twenty-five percent of all marine species.",
        "In recent decades, these fragile habitats have faced acute stress, primarily driven by rising sea surface temperatures.",
        "When ocean temperatures exceed seasonal averages by even one or two degrees Celsius, corals expel the symbiotic algae residing in their tissues, a devastating process known as coral bleaching.",
        "Without these algae, corals lose not only their vibrant coloration, but also their primary source of nutrition, leading to widespread mortality.",
        "To mitigate this crisis, marine biologists have pioneered artificial reef engineering.",
        "Early artificial reefs frequently utilized decommissioned steel ships or concrete blocks.",
        "However, modern projects utilize advanced ceramic matrices. Ceramic is chemically inert and closely mimics the natural limestone composition of calcium carbonate.",
        "Furthermore, scientists are now incorporating three-dimensional printing technology to fabricate intricate micro-crevices within the artificial structures.",
        "These crevices provide essential shelter for juvenile fish, protecting them from apex predators and dramatically accelerating ecological colonization.",
        "Recent fieldwork in the Caribbean indicates that fish biodiversity near 3D-printed reefs increased by forty percent within just twelve months.",
        "Nevertheless, researchers emphasize that artificial structures are merely a localized intervention, not a panacea.",
        "Long-term conservation fundamentally hinges upon aggressive reductions in global greenhouse gas emissions."
    ],
    6: [
        "IELTS Listening. Week 1, Day 6. Paraphrase and Synonym Masterclass.",
        "Listen to this presentation on urban agriculture and vertical farming techniques.",
        "First, look at Questions 1 to 10.",
        "As global population centers expand, conventional open-field agriculture faces acute constraints, particularly concerning arable land availability and freshwater consumption.",
        "Vertical farming offers a transformative alternative. By cultivating crops in vertically stacked layers inside climate-controlled buildings, growers achieve remarkable resource efficiency.",
        "For instance, closed-loop aeroponic systems reduce freshwater utilization by up to ninety-five percent compared to traditional soil cultivation.",
        "Moreover, because these indoor facilities operate independent of external weather anomalies, crop yields remain consistent throughout all four seasons.",
        "Eliminating agricultural pesticide runoff is another profound environmental advantage.",
        "However, critics correctly highlight that indoor vertical farms demand substantial electrical energy to power artificial LED illumination grids.",
        "Unless powered by localized solar or wind installations, the operational carbon footprint of vertical farms can paradoxically exceed that of field agriculture.",
        "Economic viability therefore depends on continuous efficiency gains in LED lighting and automated robotic harvesting mechanisms."
    ],
    7: [
        "IELTS Listening. Week 1, Day 7. Weekly Assessment Mini-Mock.",
        "This is your end-of-week listening review test, consisting of 15 questions covering form completion, multiple choice, and academic note completion.",
        "Listen carefully to the recording and answer all questions on your answer sheet.",
        "Part 1: Customer booking a weekend cycling tour in the Lake District.",
        "Good morning, Lakeland Cycle Adventures. May I take your details?",
        "Yes, my name is Arthur Pendelton, that is P-E-N-D-E-L-T-O-N. I would like to book the intermediate trail tour for two people on Saturday, 25th of November.",
        "The standard fee is 75 pounds per cyclist, which includes bike hire and safety helmets.",
        "Part 2: Guide explaining mountain safety rules.",
        "All riders must remain on designated bridleways. In the event of sudden mountain fog, proceed immediately to the nearest marked emergency shelter located at High Pass Ridge.",
        "Part 3: Academic lecture on historical transport infrastructure.",
        "During the nineteenth century, the expansion of the canal network revolutionized internal freight transport before being superseded by the rapid construction of steam railways.",
        "That concludes the weekly listening assessment recording."
    ]
}

def generate_all_audio():
    for day_num, lines in scripts.items():
        generate_day_audio(day_num, lines)

if __name__ == "__main__":
    generate_all_audio()

