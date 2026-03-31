from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def create_quiz_pdf():
    filename = "../Quiz2_Predicted_Questions.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter,
                           topMargin=0.75*inch, bottomMargin=0.75*inch,
                           leftMargin=0.75*inch, rightMargin=0.75*inch)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#003366'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#003366'),
        spaceAfter=8,
        alignment=TA_CENTER
    )
    
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#CC0000'),
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#003366'),
        leftIndent=10,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    answer_style = ParagraphStyle(
        'Answer',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#006633'),
        leftIndent=20,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    memo_style = ParagraphStyle(
        'Memo',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#CC6600'),
        leftIndent=10,
        fontName='Helvetica-Bold',
        spaceAfter=12
    )
    
    # Title page
    story.append(Paragraph("MUS 262 – Quiz 2", title_style))
    story.append(Paragraph("Predicted Questions & Complete Answers", subtitle_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Quick Memorization Guide", subtitle_style))
    story.append(Paragraph("Weeks 5-7: Hard Bop, Modal Jazz, Free Jazz", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Critical notice box
    critical_data = [[Paragraph("<b>⚠️ CRITICAL: ~30% of Quiz 2 = THREE-WAY COMPARISONS</b><br/><br/>"
                                "Focus Area: Be able to compare Hard Bop vs Modal vs Free Jazz on ANY dimension.<br/>"
                                "See Section 3 (Comparison Tables) for memory snapshot.", answer_style)]]
    critical_table = Table(critical_data, colWidths=[6.5*inch])
    critical_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.yellow),
        ('BOX', (0, 0), (-1, -1), 2, colors.orange),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(critical_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Section 1: Musical Influences
    story.append(Paragraph("SECTION 1: MUSICAL INFLUENCES QUESTIONS", section_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("Predicted Question 1A:", question_style))
    story.append(Paragraph("<b>Q:</b> What is one characteristic of gospel music that influenced hard bop? "
                          "What is one characteristic of impressionist classical music that influenced modal jazz?", 
                          answer_style))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("<b>ANSWER:</b>", answer_style))
    story.append(Paragraph("• <b>Gospel → Hard Bop:</b> Call-and-response patterns between instruments (like preacher "
                          "and congregation); strong syncopated rhythms creating 'churchy' feel; soulful emotional "
                          "expression rooted in Black church tradition; blues scale and 'bent' notes.", answer_style))
    story.append(Paragraph("• <b>Impressionist classical → Modal Jazz:</b> Colorful, ambiguous harmonies (like Debussy/Ravel); "
                          "pedal tones creating static, floating harmonic textures; spacious arrangements emphasizing "
                          "atmosphere and mood; voicings that blur major/minor tonality.", answer_style))
    story.append(Spacer(1, 0.1*inch))
    
    answer_box = [[Paragraph("<b>2-SENTENCE ANSWER:</b> Gospel music influenced hard bop through call-and-response patterns, "
                            "syncopated rhythms, and soulful emotional expression rooted in Black church music. Impressionist "
                            "classical music influenced modal jazz through colorful, ambiguous harmonies and pedal tones that "
                            "create static, floating textures.", answer_style)]]
    answer_table = Table(answer_box, colWidths=[6.5*inch])
    answer_table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.green),
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(answer_table))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("MEMORIZATION: Hard Bop = <b>Church Soul</b>; Modal Jazz = <b>French Colors</b> (Debussy/Ravel)", 
                          memo_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Q1B
    story.append(Paragraph("Predicted Question 1B:", question_style))
    story.append(Paragraph("<b>Q:</b> How did Eastern/Indian music influence modal jazz in the 1960s?", answer_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>ANSWER:</b>", answer_style))
    story.append(Paragraph("• <b>Drone/pedal point:</b> Indian music's sustained drone notes inspired modal jazz's static harmony", 
                          answer_style))
    story.append(Paragraph("• <b>Repetition and meditation:</b> Extended improvisation over single modes created trance-like quality "
                          "(like Indian ragas)", answer_style))
    story.append(Paragraph("• <b>Spiritual seeking:</b> Coltrane's interest in Eastern philosophy led to spiritual jazz "
                          "(<i>A Love Supreme</i>)", answer_style))
    story.append(Paragraph("• <b>Hypnotic quality:</b> 'My Favorite Things' uses repeated vamp similar to Indian cyclical structure", 
                          answer_style))
    story.append(Spacer(1, 0.1*inch))
    
    answer_box2 = [[Paragraph("<b>2-SENTENCE ANSWER:</b> Eastern music influenced modal jazz through the use of drones/pedal points "
                             "and repetitive modal patterns that created meditative, trance-like qualities. This spiritual seeking "
                             "reflected Eastern philosophy, particularly in Coltrane's work.", answer_style)]]
    answer_table2 = Table(answer_box2, colWidths=[6.5*inch])
    answer_table2.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.green),
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(answer_table2)
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("MEMORIZATION: Modal + India = <b>Trance Meditation Drone</b>", memo_style))
    
    story.append(PageBreak())
    
    # Section 2: Reading Concepts
    story.append(Paragraph("SECTION 2: READING CONCEPTS QUESTIONS", section_style))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("Predicted Question 2A:", question_style))
    story.append(Paragraph("<b>Q:</b> What does Ingrid Monson mean by 'saying something' in jazz, as described in "
                          "<i>Saying Something</i>, Chapter 3?", answer_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>ANSWER:</b> Monson describes how jazz musicians <b>communicate meaning</b> through their playing. "
                          "'Saying something' means:", answer_style))
    story.append(Paragraph("• <b>Musical language:</b> Playing with emotional depth and conversational quality – musicians literally "
                          "'talk' to each other through instruments", answer_style))
    story.append(Paragraph("• <b>Cultural references:</b> Incorporating African American cultural identity and social commentary", 
                          answer_style))
    story.append(Paragraph("• <b>Interactive conversation:</b> Musicians listen and respond to each other, creating dialogue through "
                          "improvisation", answer_style))
    story.append(Paragraph("• <b>Authenticity:</b> Playing with genuine feeling and personal voice, not just technical display", 
                          answer_style))
    story.append(Spacer(1, 0.1*inch))
    
    answer_box3 = [[Paragraph("<b>2-SENTENCE ANSWER:</b> 'Saying something' means jazz musicians communicate emotional depth, "
                             "cultural references, and personal identity through their playing. It's about musical conversation where "
                             "instruments 'speak' to each other with meaning beyond just notes.", answer_style)]]
    answer_table3 = Table(answer_box3, colWidths=[6.5*inch])
    answer_table3.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.green),
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(answer_table3)
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("MEMORIZATION: Monson = <b>Music as Language</b> (instruments talking with meaning)", memo_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Q2B
    story.append(Paragraph("Predicted Question 2B:", question_style))
    story.append(Paragraph("<b>Q:</b> What does Paul Berliner mean by 'thinking in jazz' in his book <i>Thinking in Jazz</i>, "
                          "Chapter 3 ('A Very Structured Thing')?", answer_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>ANSWER:</b> Berliner describes how jazz musicians develop an <b>internalized vocabulary</b> of "
                          "musical patterns. 'Thinking in jazz' means:", answer_style))
    story.append(Paragraph("• <b>Mental library:</b> Musicians have a vast collection of phrases, patterns, and harmonic concepts "
                          "stored in memory", answer_style))
    story.append(Paragraph("• <b>Second nature:</b> Through intensive practice and listening, these ideas become automatic and "
                          "spontaneous", answer_style))
    story.append(Paragraph("• <b>Recombination:</b> During improvisation, musicians recall and recombine learned vocabulary in new ways", 
                          answer_style))
    story.append(Paragraph("• <b>'A Very Structured Thing':</b> Despite sounding spontaneous, jazz improvisation is built on learned "
                          "structures", answer_style))
    story.append(Spacer(1, 0.1*inch))
    
    answer_box4 = [[Paragraph("<b>2-SENTENCE ANSWER:</b> 'Thinking in jazz' means developing an internalized vocabulary of patterns, "
                             "phrases, and harmonic concepts that become second nature through intensive practice and listening. "
                             "Musicians spontaneously recall and recombine this mental library during improvisation.", answer_style)]]
    answer_table4 = Table(answer_box4, colWidths=[6.5*inch])
    answer_table4.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.green),
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(answer_table4)
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("MEMORIZATION: Berliner = <b>Mental Library + Automatic</b> (learned patterns become spontaneous)", 
                          memo_style))
    
    story.append(PageBreak())
    
    # Section 3: THREE-WAY COMPARISONS (Critical!)
    story.append(Paragraph("SECTION 3: THREE-WAY COMPARISON QUESTIONS ⭐", section_style))
    story.append(Spacer(1, 0.1*inch))
    
    critical_data2 = [[Paragraph("<b>🔥 CRITICAL SECTION – 30% OF QUIZ 🔥</b><br/><br/>"
                                 "Most important section! Master these comparisons. You must be able to compare ANY two of the "
                                 "three periods on ANY dimension.", answer_style)]]
    critical_table2 = Table(critical_data2, colWidths=[6.5*inch])
    critical_table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFE6E6')),
        ('BOX', (0, 0), (-1, -1), 2, colors.red),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(critical_table2)
    story.append(Spacer(1, 0.2*inch))
    
    # Q3A
    story.append(Paragraph("Predicted Question 3A:", question_style))
    story.append(Paragraph("<b>Q:</b> How does Hard Bop (Week 5) differ from Modal Jazz (Week 6)? Name two differences.", 
                          answer_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>COMPLETE ANSWER (choose any 2):</b>", answer_style))
    story.append(Paragraph("<b>1. Harmony:</b> Hard Bop uses complex, rapid chord changes (like bebop); Modal Jazz uses minimal "
                          "harmony – one or two modes per section with static harmony", answer_style))
    story.append(Paragraph("<b>2. Rhythm/Feel:</b> Hard Bop has strong, locked-in groove with driving rhythm section; Modal Jazz has "
                          "spacious, floating feel that's more open and contemplative", answer_style))
    story.append(Paragraph("<b>3. Influences:</b> Hard Bop: gospel, blues, R&B, Black church music; Modal Jazz: impressionist classical "
                          "(Debussy/Ravel), Eastern/Indian music", answer_style))
    story.append(Paragraph("<b>4. Improvisation:</b> Hard Bop navigates complex chord changes + blues scale; Modal Jazz improvises on "
                          "modes/scales for extended periods", answer_style))
    story.append(Spacer(1, 0.1*inch))
    
    answer_box5 = [[Paragraph("<b>QUICK 2-POINT ANSWER:</b> (1) Harmony: Hard Bop uses complex, rapid chord changes; Modal Jazz uses "
                             "minimal harmony (one or two modes per section). (2) Rhythm/Feel: Hard Bop emphasizes strong, locked-in "
                             "groove; Modal Jazz has more spacious, floating feel.", answer_style)]]
    answer_table5 = Table(answer_box5, colWidths=[6.5*inch])
    answer_table5.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.green),
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(answer_table5)
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("MEMORIZATION: <b>Hard Bop</b> = Complex Chords + Strong Groove; <b>Modal</b> = Simple Modes + Floating Space", 
                          memo_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Q3B
    story.append(Paragraph("Predicted Question 3B:", question_style))
    story.append(Paragraph("<b>Q:</b> What are two musical differences between Modal Jazz (Week 6) and Free Jazz (Week 7)?", 
                          answer_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>COMPLETE ANSWER (choose any 2):</b>", answer_style))
    story.append(Paragraph("<b>1. Harmony:</b> Modal Jazz uses modes/scales as harmonic structure with tonal center; Free Jazz has no "
                          "predetermined harmony and is atonal (no tonal center)", answer_style))
    story.append(Paragraph("<b>2. Form/Structure:</b> Modal Jazz still has structure (modes, pulse, head-solos-head); Free Jazz abandons "
                          "all predetermined forms with collective improvisation", answer_style))
    story.append(Paragraph("<b>3. Rhythm:</b> Modal Jazz has steady pulse and meter (though spacious); Free Jazz often has no steady "
                          "pulse – 'free time'", answer_style))
    story.append(Paragraph("<b>4. Accessibility:</b> Modal Jazz is very accessible, beautiful, contemplative; Free Jazz is very "
                          "challenging, confrontational, chaotic, intense", answer_style))
    story.append(Spacer(1, 0.1*inch))
    
    answer_box6 = [[Paragraph("<b>QUICK 2-POINT ANSWER:</b> (1) Harmony: Modal Jazz uses modes/scales as structure with tonal center; "
                             "Free Jazz has no predetermined harmony and is atonal. (2) Form: Modal Jazz still has structure (modes, pulse); "
                             "Free Jazz abandons all predetermined forms.", answer_style)]]
    answer_table6 = Table(answer_box6, colWidths=[6.5*inch])
    answer_table6.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.green),
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(answer_table6)
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("MEMORIZATION: <b>Modal</b> = Structure with Modes; <b>Free</b> = NO Structure, NO Rules", memo_style))
    
    story.append(PageBreak())
    
    # MEMORY SNAPSHOT TABLES
    story.append(Paragraph("MEMORY SNAPSHOT: THREE-WEEK COMPARISON", section_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Big Picture box
    big_picture_data = [[Paragraph("<b>THE BIG PICTURE: Progressive Liberation</b><br/><br/>"
                                   "<b>Week 5 (Hard Bop):</b> Freed jazz from pure intellectualism by adding SOUL<br/><br/>"
                                   "<b>Week 6 (Modal Jazz):</b> Freed jazz from constant chord changes by using MODES<br/><br/>"
                                   "<b>Week 7 (Free Jazz):</b> Freed jazz from ALL rules – complete FREEDOM", answer_style)]]
    big_picture_table = Table(big_picture_data, colWidths=[6.5*inch])
    big_picture_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#E6F2FF')),
        ('BOX', (0, 0), (-1, -1), 2, colors.blue),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(big_picture_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Quick Identification Table
    story.append(Paragraph("<b>Quick Identification Guide</b>", question_style))
    story.append(Spacer(1, 0.1*inch))
    
    id_data = [
        ['Element', 'HARD BOP', 'MODAL JAZZ', 'FREE JAZZ'],
        ['Can you tap\na steady beat?', 'YES\nStrong groove', 'YES\nFloating pulse', 'NO\nFree time'],
        ['Chord changes?', 'MANY\nRapid, complex', 'FEW\nStatic (1-2 modes)', 'NONE\nAtonal'],
        ['Overall vibe?', 'Funky, soulful,\ngrooving', 'Meditative,\nspacious, floating', 'Chaotic, intense,\nconfrontational'],
        ['Sounds like?', 'Church + blues\n+ dance', 'Classical\nimpressionism\n+ Eastern\nmeditation', 'Breaking all rules\n+ screaming chaos']
    ]
    
    id_table = Table(id_data, colWidths=[1.3*inch, 1.7*inch, 1.7*inch, 1.8*inch])
    id_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    story.append(id_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Essential Comparison Table
    story.append(Paragraph("<b>The Essential Comparison Table</b>", question_style))
    story.append(Spacer(1, 0.1*inch))
    
    comp_data = [
        ['Dimension', 'Week 5: HARD BOP', 'Week 6: MODAL JAZZ', 'Week 7: FREE JAZZ'],
        ['HARMONY', 'Complex, rapid\nchord changes\n(bebop-style)', 'Minimal – 1-2 modes\nper section;\nstatic', 'NONE –\ncompletely atonal'],
        ['RHYTHM/\nTEMPO', 'Strong, locked-in\ngroove;\nmedium-fast', 'Spacious, floating\nfeel;\nslow-medium', 'Variable or\nFREE TIME –\nno pulse'],
        ['FORM', 'Traditional\n(AABA,\n12-bar blues)', 'Simplified forms;\nlong vamps', 'NO predetermined\nforms'],
        ['BASS\nROLE', 'Walking bass\nkeeping time', 'Pedal tones\nor ostinatos', 'Melodic,\nfree lines'],
        ['DRUMS\nROLE', 'Driving,\ninteractive\n(Art Blakey)', 'Subtle,\nsupportive;\nbrushwork', 'Textural,\nnon-metrical'],
        ['INFLUENCES', 'Gospel, blues,\nR&B, church', 'Impressionism\n(Debussy),\nEastern', 'Avant-garde\nclassical'],
        ['SOUND', 'Funky, earthy,\nswinging, soulful', 'Floating, meditative,\ncontemplative', 'Intense, chaotic,\nconfrontational']
    ]
    
    comp_table = Table(comp_data, colWidths=[1.3*inch, 1.8*inch, 1.8*inch, 1.6*inch])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#FFCCCC')),
        ('BACKGROUND', (1, 1), (1, -1), colors.HexColor('#FFE6E6')),
        ('BACKGROUND', (2, 1), (2, -1), colors.HexColor('#CCE6FF')),
        ('BACKGROUND', (3, 1), (3, -1), colors.HexColor('#E6CCFF')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    story.append(comp_table)
    
    story.append(PageBreak())
    
    # Final Memory Aid
    story.append(Paragraph("FINAL MEMORY AID: THE 3-WORD SUMMARY", section_style))
    story.append(Spacer(1, 0.2*inch))
    
    final_data = [[Paragraph("<b>If you forget everything else, remember these 3-word descriptions:</b><br/><br/>"
                            "<b>Hard Bop</b> = <b>Church Soul Groove</b><br/><br/>"
                            "<b>Modal Jazz</b> = <b>Modes Space Meditation</b><br/><br/>"
                            "<b>Free Jazz</b> = <b>No Rules Chaos</b><br/><br/>"
                            "Use these to build any comparison on the quiz!", answer_style)]]
    final_table = Table(final_data, colWidths=[6.5*inch])
    final_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#CCFFCC')),
        ('BOX', (0, 0), (-1, -1), 3, colors.HexColor('#009900')),
        ('PADDING', (0, 0), (-1, -1), 20),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(final_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Comparison shortcuts
    story.append(Paragraph("<b>Comparison Shortcuts:</b>", question_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("• <b>Hard Bop vs Modal:</b> Complex changes vs simple modes; Strong groove vs floating space", 
                          answer_style))
    story.append(Paragraph("• <b>Modal vs Free:</b> Still has structure vs no structure; Tonal vs atonal", answer_style))
    story.append(Paragraph("• <b>Hard Bop vs Free:</b> Groove + form vs no groove + no form; Accessible vs confrontational", 
                          answer_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("<b>The 30-Second Memory Drill</b>", question_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Close your eyes and recall:", answer_style))
    story.append(Paragraph("1. <b>HARD BOP:</b> Church soul, complex changes, strong groove, funky", answer_style))
    story.append(Paragraph("2. <b>MODAL JAZZ:</b> Modes not changes, floating space, meditation, beautiful", answer_style))
    story.append(Paragraph("3. <b>FREE JAZZ:</b> No rules at all, chaos freedom, can't tap foot, screaming", answer_style))
    story.append(Spacer(1, 0.5*inch))
    
    story.append(Paragraph("🎵 <b>You've got this!</b> 🎵", title_style))
    
    # Build PDF
    doc.build(story)
    print(f"✅ PDF created successfully: {filename}")
    print(f"📄 Location: /Users/skyler/Library/CloudStorage/OneDrive-Personal/Desktop/Current Project/Canvas/MUS262/study/")

if __name__ == "__main__":
    create_quiz_pdf()
