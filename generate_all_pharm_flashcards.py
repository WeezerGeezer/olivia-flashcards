#!/usr/bin/env python3
"""
Generate complete pharmacy flashcards JSON for all modules
"""

import json

# Module 15: Infectious Diseases Part 2
module_15_steps = [
    {
        "id": "id2-1",
        "stepNumber": 1,
        "title": "What is vancomycin and its mechanism of action?",
        "pageRef": "p.2-3",
        "subSteps": [
            {"id": "1a", "content": "Inhibits bacterial cell wall synthesis by binding to D-Ala-D-Ala"},
            {"id": "1b", "content": "Bactericidal against most Gram-positive organisms"},
            {"id": "1c", "content": "Excellent activity: MRSA, MSSA, Streptococcus, Enterococcus"},
            {"id": "1d", "content": "NO activity: Gram-negative organisms"}
        ],
        "comments": ["Increasing MICs in MRSA ('MIC creep')"]
    },
    {
        "id": "id2-2",
        "stepNumber": 2,
        "title": "What is the dosing and monitoring for vancomycin?",
        "pageRef": "p.3",
        "subSteps": [
            {"id": "2a", "content": "Standard: 15-20 mg/kg IV q8-12h"},
            {"id": "2b", "content": "Loading dose: 25-30 mg/kg for serious infections"},
            {"id": "2c", "content": "Target trough: 15-20 mcg/mL for serious infections"},
            {"id": "2d", "content": "AUC/MIC targeting preferred: target AUC 400-600"}
        ],
        "comments": ["TDM recommended for serious infections", "Adjust dose in renal impairment"]
    },
    {
        "id": "id2-3",
        "stepNumber": 3,
        "title": "What are the adverse effects of vancomycin?",
        "pageRef": "p.3",
        "subSteps": [
            {"id": "3a", "content": "Nephrotoxicity: dose-dependent, risk ↑ with trough >20 mcg/mL"},
            {"id": "3b", "content": "Ototoxicity: rare, associated with high troughs"},
            {"id": "3c", "content": "Red Man Syndrome: histamine-mediated infusion reaction"},
            {"id": "3d", "content": "Thrombophlebitis: common with peripheral IV"}
        ],
        "comments": ["Red Man prevention: slow infusion (≥1 hour per 500 mg), antihistamines"]
    },
    {
        "id": "id2-4",
        "stepNumber": 4,
        "title": "What is daptomycin and its characteristics?",
        "pageRef": "p.3-4",
        "subSteps": [
            {"id": "4a", "content": "Lipopeptide that depolarizes bacterial cell membrane"},
            {"id": "4b", "content": "Concentration-dependent bactericidal activity"},
            {"id": "4c", "content": "Spectrum: Gram-positive only (MRSA, MSSA, VRE, Strep)"},
            {"id": "4d", "content": "NOT effective for pneumonia (inactivated by surfactant)"}
        ]
    },
    {
        "id": "id2-5",
        "stepNumber": 5,
        "title": "What is the dosing and monitoring for daptomycin?",
        "pageRef": "p.4",
        "subSteps": [
            {"id": "5a", "content": "ABSSSI: 4 mg/kg IV q24h"},
            {"id": "5b", "content": "Bacteremia/endocarditis: 6-8 mg/kg q24h (up to 10-12 mg/kg)"},
            {"id": "5c", "content": "Adjust for CrCl <30 mL/min: dose q48h"},
            {"id": "5d", "content": "Monitor CPK weekly"}
        ],
        "comments": ["D/C if CPK >1000 U/L with symptoms or >2000 U/L", "Hold statins during therapy"]
    },
    {
        "id": "id2-6",
        "stepNumber": 6,
        "title": "What is linezolid and its characteristics?",
        "pageRef": "p.4-5",
        "subSteps": [
            {"id": "6a", "content": "Oxazolidinone: inhibits protein synthesis (50S ribosomal subunit)"},
            {"id": "6b", "content": "Spectrum: MRSA, VRE, Strep"},
            {"id": "6c", "content": "Dosing: 600 mg PO/IV q12h"},
            {"id": "6d", "content": "100% oral bioavailability, excellent tissue penetration"}
        ],
        "comments": ["Active against VRE", "Good CNS penetration"]
    },
    {
        "id": "id2-7",
        "stepNumber": 7,
        "title": "What are the adverse effects of linezolid?",
        "pageRef": "p.5",
        "subSteps": [
            {"id": "7a", "content": "Myelosuppression: thrombocytopenia, anemia (monitor CBC weekly if >2 weeks)"},
            {"id": "7b", "content": "Peripheral/optic neuropathy: with prolonged use >28 days"},
            {"id": "7c", "content": "Lactic acidosis: rare"},
            {"id": "7d", "content": "Serotonin syndrome: with SSRIs, SNRIs, MAOIs"}
        ],
        "comments": ["MAO inhibitor activity - avoid tyramine-rich foods"]
    },
    {
        "id": "id2-8",
        "stepNumber": 8,
        "title": "What are treatment options for VRE?",
        "pageRef": "p.5",
        "comments": [
            "Linezolid: first-line for VRE infections",
            "Daptomycin: 8-12 mg/kg q24h (higher doses for endocarditis)",
            "Quinupristin/Dalfopristin: VRE faecium ONLY (not faecalis)",
            "Tigecycline: reserve for limited options"
        ]
    },
    {
        "id": "id2-9",
        "stepNumber": 9,
        "title": "What are the fluoroquinolones and their spectrum?",
        "pageRef": "p.6-7",
        "subSteps": [
            {"id": "9a", "content": "MOA: Inhibit DNA gyrase and topoisomerase IV"},
            {"id": "9b", "content": "Concentration-dependent bactericidal activity"},
            {"id": "9c", "content": "PK/PD target: AUC/MIC >30-40 (Gram-neg), >100 (Strep)"},
            {"id": "9d", "content": "Broad coverage: Gram(+), Gram(-), atypicals"}
        ]
    },
    {
        "id": "id2-10",
        "stepNumber": 10,
        "title": "What are the individual fluoroquinolone agents and their uses?",
        "pageRef": "p.7",
        "subSteps": [
            {"id": "10a", "content": "Levofloxacin: CAP, UTI, ABSSSI, prostatitis (500-750 mg q24h)"},
            {"id": "10b", "content": "Moxifloxacin: CAP, enhanced Gram(+) and anaerobic (400 mg q24h, NOT for UTI)"},
            {"id": "10c", "content": "Ciprofloxacin: Excellent Gram(-) including Pseudomonas, UTI (250-750 mg q12h)"},
            {"id": "10d", "content": "Delafloxacin: ABSSSI including MRSA (300 mg IV or 450 mg PO q12h)"}
        ],
        "comments": ["All ~100% oral bioavailability"]
    },
    {
        "id": "id2-11",
        "stepNumber": 11,
        "title": "What are the Black Box Warnings for fluoroquinolones?",
        "pageRef": "p.7",
        "subSteps": [
            {"id": "11a", "content": "Tendon rupture/tendinitis (especially Achilles)"},
            {"id": "11b", "content": "Peripheral neuropathy (may be permanent)"},
            {"id": "11c", "content": "CNS effects: seizures, increased ICP"},
            {"id": "11d", "content": "Aortic aneurysm/dissection"},
            {"id": "11e", "content": "Myasthenia gravis exacerbation (contraindicated)"}
        ],
        "comments": ["FDA: reserve for serious infections when alternatives unavailable"]
    },
    {
        "id": "id2-12",
        "stepNumber": 12,
        "title": "What are other adverse effects and interactions of fluoroquinolones?",
        "pageRef": "p.7",
        "subSteps": [
            {"id": "12a", "content": "QTc prolongation (greatest with moxifloxacin)"},
            {"id": "12b", "content": "Photosensitivity, GI upset"},
            {"id": "12c", "content": "Dysglycemia, C. difficile"},
            {"id": "12d", "content": "Divalent/trivalent cations: separate by 2-6 hours (antacids, Ca, Fe, Zn)"}
        ],
        "comments": ["Avoid in pregnancy/children (cartilage damage)"]
    },
    {
        "id": "id2-13",
        "stepNumber": 13,
        "title": "What are the aminoglycosides and their characteristics?",
        "pageRef": "p.7-9",
        "subSteps": [
            {"id": "13a", "content": "MOA: Bind 30S ribosomal subunit, inhibit protein synthesis"},
            {"id": "13b", "content": "Concentration-dependent bactericidal (PK/PD: Cmax/MIC 8-10)"},
            {"id": "13c", "content": "Spectrum: Gram-negatives (including Pseudomonas)"},
            {"id": "13d", "content": "NO activity: Anaerobes (require oxygen for uptake)"}
        ],
        "comments": ["Always use in combination", "Synergy with beta-lactams for Gram(+)"]
    },
    {
        "id": "id2-14",
        "stepNumber": 14,
        "title": "What is extended-interval dosing for aminoglycosides?",
        "pageRef": "p.8-9",
        "subSteps": [
            {"id": "14a", "content": "Gentamicin/Tobramycin: 5-7 mg/kg q24h"},
            {"id": "14b", "content": "Amikacin: 15-20 mg/kg q24h"},
            {"id": "14c", "content": "Advantages: enhanced efficacy, reduced toxicity, convenient"},
            {"id": "14d", "content": "Monitoring: random level 6-14 hours post-dose"}
        ],
        "comments": ["Preferred for most indications", "Traditional dosing for endocarditis, pregnancy"]
    },
    {
        "id": "id2-15",
        "stepNumber": 15,
        "title": "What are the adverse effects of aminoglycosides?",
        "pageRef": "p.9",
        "subSteps": [
            {"id": "15a", "content": "Nephrotoxicity (10-25%): usually reversible, monitor SCr/BUN"},
            {"id": "15b", "content": "Ototoxicity: vestibular (vertigo) and cochlear (hearing loss, often permanent)"},
            {"id": "15c", "content": "Neuromuscular blockade: rare"},
            {"id": "15d", "content": "Risk factors: prolonged therapy, high levels, concurrent nephro/ototoxins"}
        ],
        "comments": ["Avoid concurrent vancomycin, NSAIDs, contrast"]
    },
    {
        "id": "id2-16",
        "stepNumber": 16,
        "title": "What are the macrolides and their spectrum?",
        "pageRef": "p.9-10",
        "subSteps": [
            {"id": "16a", "content": "MOA: Bind 50S ribosomal subunit, inhibit protein synthesis"},
            {"id": "16b", "content": "Bacteriostatic (bactericidal at high concentrations)"},
            {"id": "16c", "content": "Spectrum: Gram(+), atypicals (Mycoplasma, Chlamydia, Legionella)"},
            {"id": "16d", "content": "Some Gram(-): H. influenzae (azithromycin)"}
        ]
    },
    {
        "id": "id2-17",
        "stepNumber": 17,
        "title": "What are the individual macrolide agents?",
        "pageRef": "p.9-10",
        "subSteps": [
            {"id": "17a", "content": "Erythromycin: 250-500 mg q6h, poor GI tolerance, significant drug interactions"},
            {"id": "17b", "content": "Clarithromycin: 250-500 mg q12h, better tolerated, strong CYP3A4 inhibitor"},
            {"id": "17c", "content": "Azithromycin: 500 mg x1 then 250 mg q24h x4d (Z-Pak), long half-life (68h)"},
            {"id": "17d", "content": "Azithromycin: once-daily, short courses, fewer interactions, best GI tolerance"}
        ]
    },
    {
        "id": "id2-18",
        "stepNumber": 18,
        "title": "What are the adverse effects of macrolides?",
        "pageRef": "p.10",
        "subSteps": [
            {"id": "18a", "content": "GI: nausea, vomiting, diarrhea (motilin receptor agonist)"},
            {"id": "18b", "content": "QTc prolongation: all macrolides (greatest with azithromycin)"},
            {"id": "18c", "content": "Hepatotoxicity: rare cholestatic hepatitis"},
            {"id": "18d", "content": "CYP3A4 inhibition: erythro > clarithro >> azithro"}
        ],
        "comments": ["FDA warning: increased CV death risk with azithromycin"]
    },
    {
        "id": "id2-19",
        "stepNumber": 19,
        "title": "What is doxycycline and its uses?",
        "pageRef": "p.11-12",
        "subSteps": [
            {"id": "19a", "content": "Tetracycline: binds 30S ribosomal subunit, bacteriostatic"},
            {"id": "19b", "content": "Dosing: 100 mg PO/IV q12h, 90-100% oral bioavailability"},
            {"id": "19c", "content": "Spectrum: Broad (Gram+/-, atypicals, rickettsiae, MRSA)"},
            {"id": "19d", "content": "Uses: CAP, tick-borne diseases, ABSSSI, acne, malaria prophylaxis"}
        ],
        "comments": ["Drug of choice for tick-borne illnesses (Lyme, RMSF, ehrlichiosis)"]
    },
    {
        "id": "id2-20",
        "stepNumber": 20,
        "title": "What is tigecycline and its characteristics?",
        "pageRef": "p.12",
        "subSteps": [
            {"id": "20a", "content": "Glycylcycline (tetracycline derivative)"},
            {"id": "20b", "content": "Broad spectrum: MRSA, VRE, ESBL, anaerobes"},
            {"id": "20c", "content": "NO activity: Pseudomonas, Proteus"},
            {"id": "20d", "content": "Dosing: 100 mg IV x1, then 50 mg IV q12h"}
        ],
        "comments": ["BLACK BOX: increased mortality vs comparators - reserve for limited options", "Very high nausea/vomiting"]
    },
    {
        "id": "id2-21",
        "stepNumber": 21,
        "title": "What are the adverse effects of tetracyclines?",
        "pageRef": "p.12",
        "subSteps": [
            {"id": "21a", "content": "GI: nausea, vomiting, esophagitis (take with water, stay upright)"},
            {"id": "21b", "content": "Photosensitivity: severe sunburn with minimal sun"},
            {"id": "21c", "content": "Tooth discoloration: permanent in children <8 years"},
            {"id": "21d", "content": "Chelation: separate from Ca, Fe, Mg, Al by 2-3 hours"}
        ],
        "comments": ["Contraindicated: pregnancy, breastfeeding, children <8 years"]
    },
    {
        "id": "id2-22",
        "stepNumber": 22,
        "title": "What is clindamycin and its spectrum?",
        "pageRef": "p.13",
        "subSteps": [
            {"id": "22a", "content": "Inhibits protein synthesis (50S), bacteriostatic"},
            {"id": "22b", "content": "Spectrum: Gram(+) cocci (MRSA), anaerobes (B. fragilis)"},
            {"id": "22c", "content": "NO activity: Gram(-), Enterococcus"},
            {"id": "22d", "content": "Dosing: 150-450 mg PO q6-8h, 600-900 mg IV q8h"}
        ],
        "comments": ["Suppresses toxin production", "Excellent bone penetration"]
    },
    {
        "id": "id2-23",
        "stepNumber": 23,
        "title": "What is TMP/SMX and its characteristics?",
        "pageRef": "p.13-14",
        "subSteps": [
            {"id": "23a", "content": "Sequential blockade of folic acid synthesis, bactericidal"},
            {"id": "23b", "content": "Spectrum: MRSA, MSSA, Gram(-), PCP, Stenotrophomonas"},
            {"id": "23c", "content": "Dosing: 1 DS tablet PO q12h (standard), higher for PCP"},
            {"id": "23d", "content": "Uses: UTI (first-line), MRSA ABSSSI, PCP treatment/prophylaxis"}
        ]
    },
    {
        "id": "id2-24",
        "stepNumber": 24,
        "title": "What are the adverse effects of TMP/SMX?",
        "pageRef": "p.14",
        "subSteps": [
            {"id": "24a", "content": "Hyperkalemia: trimethoprim = K-sparing diuretic"},
            {"id": "24b", "content": "Nephrotoxicity: ↑SCr (blocks tubular secretion, not true damage)"},
            {"id": "24c", "content": "Rash: common (3-5%), Stevens-Johnson in severe cases"},
            {"id": "24d", "content": "Drug interactions: warfarin (↑INR), methotrexate, phenytoin"}
        ],
        "comments": ["Monitor K+ and SCr during therapy"]
    },
    {
        "id": "id2-25",
        "stepNumber": 25,
        "title": "What is metronidazole and its uses?",
        "pageRef": "p.14",
        "subSteps": [
            {"id": "25a", "content": "Disrupts DNA, bactericidal against anaerobes"},
            {"id": "25b", "content": "Spectrum: Anaerobes (Bacteroides, Clostridium including C. diff)"},
            {"id": "25c", "content": "Uses: C. diff, intra-abdominal infections, bacterial vaginosis, trichomoniasis"},
            {"id": "25d", "content": "Dosing: 500 mg PO/IV q8h (C. diff), 2g x1 (trich)"}
        ],
        "comments": ["Excellent CNS penetration"]
    },
    {
        "id": "id2-26",
        "stepNumber": 26,
        "title": "What are the adverse effects of metronidazole?",
        "pageRef": "p.14",
        "subSteps": [
            {"id": "26a", "content": "Disulfiram-like reaction: severe with alcohol (avoid during + 3 days after)"},
            {"id": "26b", "content": "Metallic taste: very common"},
            {"id": "26c", "content": "Peripheral neuropathy: prolonged use >2 weeks"},
            {"id": "26d", "content": "Drug interactions: warfarin (↑INR), lithium"}
        ]
    },
    {
        "id": "id2-27",
        "stepNumber": 27,
        "title": "What is rifampin and its uses?",
        "pageRef": "p.15",
        "subSteps": [
            {"id": "27a", "content": "Inhibits bacterial RNA polymerase, bactericidal"},
            {"id": "27b", "content": "ALWAYS combination therapy (rapid resistance if alone)"},
            {"id": "27c", "content": "Uses: TB, Staph prosthetic joint infections, MRSA bacteremia (adjunct)"},
            {"id": "27d", "content": "Meningitis prophylaxis: N. meningitidis, H. influenzae"}
        ]
    },
    {
        "id": "id2-28",
        "stepNumber": 28,
        "title": "What are the adverse effects of rifampin?",
        "pageRef": "p.15",
        "subSteps": [
            {"id": "28a", "content": "Orange discoloration: urine, tears, sweat (warn patients, stains contacts)"},
            {"id": "28b", "content": "Hepatotoxicity: monitor LFTs"},
            {"id": "28c", "content": "Potent CYP3A4 inducer: decreases levels of many drugs"},
            {"id": "28d", "content": "Decreases: oral contraceptives, warfarin, protease inhibitors"}
        ],
        "comments": ["Requires alternative contraception", "Excellent biofilm penetration"]
    },
    {
        "id": "id2-29",
        "stepNumber": 29,
        "title": "What is nitrofurantoin and its uses?",
        "pageRef": "p.15",
        "subSteps": [
            {"id": "29a", "content": "Damages bacterial DNA, bactericidal at urinary concentrations"},
            {"id": "29b", "content": "Spectrum: E. coli, Enterococcus, S. saprophyticus"},
            {"id": "29c", "content": "NO activity: Pseudomonas, Proteus, Serratia, many Klebsiella"},
            {"id": "29d", "content": "Use: Uncomplicated UTI (cystitis) ONLY, NOT pyelonephritis"}
        ],
        "comments": ["Dosing: 100 mg PO q12h x5-7 days"]
    },
    {
        "id": "id2-30",
        "stepNumber": 30,
        "title": "What are the adverse effects and contraindications of nitrofurantoin?",
        "pageRef": "p.15",
        "subSteps": [
            {"id": "30a", "content": "Pulmonary toxicity: acute pneumonitis or chronic fibrosis (risk ↑ with >6 months)"},
            {"id": "30b", "content": "Peripheral neuropathy: especially with renal impairment"},
            {"id": "30c", "content": "Contraindications: CrCl <30 mL/min, pregnancy at term, G6PD deficiency"},
            {"id": "30d", "content": "Take with food to reduce GI upset"}
        ],
        "comments": ["Only achieves therapeutic levels in urine", "Monitor for pulmonary symptoms during long-term use"]
    },
    {
        "id": "id2-31",
        "stepNumber": 31,
        "title": "What are the newer lipoglycopeptides?",
        "pageRef": "p.3",
        "subSteps": [
            {"id": "31a", "content": "Telavancin (Vibativ): 10 mg/kg IV q24h, MRSA skin infections, HAP"},
            {"id": "31b", "content": "Dalbavancin (Dalvance): 1500 mg x1 OR 1000mg + 500mg week later"},
            {"id": "31c", "content": "Oritavancin (Orbactiv): 1200 mg single dose"},
            {"id": "31d", "content": "Advantage: Single-dose therapy for ABSSSI"}
        ],
        "comments": ["Ultra-long half-life", "Outpatient parenteral therapy without IV access maintenance"]
    },
    {
        "id": "id2-32",
        "stepNumber": 32,
        "title": "What is tedizolid?",
        "pageRef": "p.5",
        "subSteps": [
            {"id": "32a", "content": "Second-generation oxazolidinone"},
            {"id": "32b", "content": "Dosing: 200 mg PO/IV q24h x6 days"},
            {"id": "32c", "content": "Indication: ABSSSI"},
            {"id": "32d", "content": "Advantages: Lower myelosuppression, once-daily dosing"}
        ]
    },
    {
        "id": "id2-33",
        "stepNumber": 33,
        "title": "What is amikacin and when is it used?",
        "pageRef": "p.8",
        "subSteps": [
            {"id": "33a", "content": "Aminoglycoside resistant to many modifying enzymes"},
            {"id": "33b", "content": "Reserve for resistant organisms"},
            {"id": "33c", "content": "Dosing: 15-20 mg/kg q24h"},
            {"id": "33d", "content": "Same spectrum and toxicity as gentamicin/tobramycin"}
        ]
    },
    {
        "id": "id2-34",
        "stepNumber": 34,
        "title": "What are the newer tetracyclines?",
        "pageRef": "p.12",
        "subSteps": [
            {"id": "34a", "content": "Eravacycline (Xerava): complicated intra-abdominal, 1 mg/kg IV q12h"},
            {"id": "34b", "content": "Omadacycline (Nuzyra): CAP, ABSSSI, oral and IV formulations"},
            {"id": "34c", "content": "Advantages: less nausea than tigecycline, active against some tigecycline-resistant"}
        ]
    },
    {
        "id": "id2-35",
        "stepNumber": 35,
        "title": "What C. difficile risk does clindamycin have?",
        "pageRef": "p.13",
        "comments": [
            "High risk for C. difficile infection (10-30%)",
            "OR 2.86 for C. diff in meta-analysis",
            "Consider alternatives when possible",
            "Good for: bone infections, ABSSSI, aspiration pneumonia, toxin suppression"
        ]
    }
]

module_15 = {
    "id": "infectious-diseases-2",
    "name": "Infectious Diseases Part 2",
    "shortName": "ID Part 2",
    "totalSteps": 35,
    "steps": module_15_steps
}

# Module 16: Selected Treatment Guidelines - High-yield cards
module_16_steps = [
    {
        "id": "tg-1",
        "stepNumber": 1,
        "title": "What are the usual organisms in skin and soft tissue infections?",
        "pageRef": "p.1",
        "comments": [
            "S. aureus (most common)",
            "S. pyogenes (Group A Strep)",
            "Common disease states: Impetigo, Erysipelas (think strep!), Cellulitis"
        ]
    },
    {
        "id": "tg-2",
        "stepNumber": 2,
        "title": "What is the treatment for S. pyogenes?",
        "pageRef": "p.1",
        "subSteps": [
            {"id": "2a", "content": "Drug of choice: Penicillin (nearly universally susceptible)"},
            {"id": "2b", "content": "Narrow spectrum therapy"},
            {"id": "2c", "content": "Most Gram(+) agents cover (EXCEPT doxycycline)"},
            {"id": "2d", "content": "Clindamycin has resistance issues"}
        ]
    },
    {
        "id": "tg-3",
        "stepNumber": 3,
        "title": "When should MRSA be covered in cellulitis?",
        "pageRef": "p.1",
        "comments": [
            "Routine coverage: purulent cellulitis and abscesses",
            "Usually NOT warranted in systemic infections without these characteristics",
            "Increase in community-acquired (CA) MRSA"
        ]
    },
    {
        "id": "tg-4",
        "stepNumber": 4,
        "title": "What are the oral options for S. aureus?",
        "pageRef": "p.1-2",
        "subSteps": [
            {"id": "4a", "content": "MSSA: Cephalexin, Amoxicillin/clavulanate, Dicloxacillin"},
            {"id": "4b", "content": "MRSA: TMP/SMX, Doxycycline, Linezolid"},
            {"id": "4c", "content": "All cover S. pyogenes EXCEPT doxycycline"},
            {"id": "4d", "content": "Follow up at 24-48 hours prudent"}
        ]
    },
    {
        "id": "tg-5",
        "stepNumber": 5,
        "title": "What is the treatment for severe cellulitis?",
        "pageRef": "p.2",
        "subSteps": [
            {"id": "5a", "content": "Defined by: failure of oral abx + debridement, systemic symptoms"},
            {"id": "5b", "content": "MSSA/Strep only: Nafcillin or Cefazolin"},
            {"id": "5c", "content": "MRSA: Vancomycin or Daptomycin"},
            {"id": "5d", "content": "Duration: 5-7 days (guideline: 7 days), up to 14 days if started IV"}
        ]
    },
    {
        "id": "tg-6",
        "stepNumber": 6,
        "title": "What is the treatment for animal bites?",
        "pageRef": "p.3",
        "subSteps": [
            {"id": "6a", "content": "Must cover Pasteurella multocida (has beta-lactamase)"},
            {"id": "6b", "content": "DOC: Amoxicillin/clavulanic acid"},
            {"id": "6c", "content": "IV: Ampicillin/sulbactam or 3G cephalosporin"},
            {"id": "6d", "content": "Alternatives (PCN allergy): Doxycycline, Moxifloxacin"}
        ],
        "comments": ["Cat bites more likely to get infected than dog bites", "Average 5 organisms per bite"]
    },
    {
        "id": "tg-7",
        "stepNumber": 7,
        "title": "What is the treatment for diabetic foot ulcers?",
        "pageRef": "p.3",
        "subSteps": [
            {"id": "7a", "content": "Organisms: S. aureus (MRSA) predominate; Gram(-) in deep ulcers"},
            {"id": "7b", "content": "Uninfected ulcers: do NOT treat"},
            {"id": "7c", "content": "Empiric: Vancomycin +/- Ceftriaxone (varies)"},
            {"id": "7d", "content": "Duration: 1-2 wk mild; 2-4 wk moderate; 4-6 wk if bone involvement"}
        ],
        "comments": ["Do not treat until ulcer heals - just until infection resolves"]
    },
    {
        "id": "tg-8",
        "stepNumber": 8,
        "title": "What is the treatment for uncomplicated cystitis?",
        "pageRef": "p.4",
        "subSteps": [
            {"id": "8a", "content": "Target: E. coli (based on local susceptibility)"},
            {"id": "8b", "content": "3 days: TMP/SMX, Fluoroquinolones (not moxifloxacin)"},
            {"id": "8c", "content": "5 days: Nitrofurantoin"},
            {"id": "8d", "content": "7 days: Beta-lactams"}
        ]
    },
    {
        "id": "tg-9",
        "stepNumber": 9,
        "title": "What is fosfomycin and its use?",
        "pageRef": "p.4",
        "subSteps": [
            {"id": "9a", "content": "MOA: Inhibits enolpyruvate transferase (peptidoglycan synthesis)"},
            {"id": "9b", "content": "Dosing: 3g PO x1 for cystitis"},
            {"id": "9c", "content": "Safe for pregnancy"},
            {"id": "9d", "content": "Recent evidence: inferior to nitrofurantoin, consider second-line"}
        ]
    },
    {
        "id": "tg-10",
        "stepNumber": 10,
        "title": "What defines a complicated UTI?",
        "pageRef": "p.4",
        "subSteps": [
            {"id": "10a", "content": "Structural/functional abnormality: obstruction, foreign body, males"},
            {"id": "10b", "content": "Pyelonephritis"},
            {"id": "10c", "content": "Recent guidelines: extending beyond the bladder"},
            {"id": "10d", "content": "Extends duration to 7+ days"}
        ]
    },
    {
        "id": "tg-11",
        "stepNumber": 11,
        "title": "What is the treatment for community-acquired pyelonephritis?",
        "pageRef": "p.4",
        "subSteps": [
            {"id": "11a", "content": "Oral: FQ, TMP/SMX (first-line)"},
            {"id": "11b", "content": "NOT appropriate: Nitrofurantoin, Fosfomycin (inadequate tissue levels)"},
            {"id": "11c", "content": "IV: FQ, Aminoglycosides, Ceftriaxone, Carbapenems (if resistant)"},
            {"id": "11d", "content": "Duration: 7-14 days (7 days standard, even with bacteremia)"}
        ]
    },
    {
        "id": "tg-12",
        "stepNumber": 12,
        "title": "What are 'The Big 6' CAP bacterial pathogens?",
        "pageRef": "p.6",
        "subSteps": [
            {"id": "12a", "content": "S. pneumoniae, H. influenzae, M. catarrhalis"},
            {"id": "12b", "content": "M. pneumoniae, C. pneumoniae, L. pneumophilia"},
            {"id": "12c", "content": "Others: S. aureus (CA-MRSA, post-influenza)"},
            {"id": "12d", "content": "Anaerobes: only cover for empyema, lung abscess"}
        ]
    },
    {
        "id": "tg-13",
        "stepNumber": 13,
        "title": "What is outpatient treatment for CAP?",
        "pageRef": "p.6-7",
        "subSteps": [
            {"id": "13a", "content": "Healthy adults: Amoxicillin or Doxycycline (macrolides NO longer recommended)"},
            {"id": "13b", "content": "With comorbidities/recent abx: Beta-lactam + (Doxy or Macrolide)"},
            {"id": "13c", "content": "Alternative: Respiratory fluoroquinolone"},
            {"id": "13d", "content": "Duration: minimum 5 days (some data: 3 days sufficient)"}
        ]
    },
    {
        "id": "tg-14",
        "stepNumber": 14,
        "title": "What is inpatient treatment for CAP?",
        "pageRef": "p.7",
        "subSteps": [
            {"id": "14a", "content": "Non-severe (floor): Beta-lactam + (Doxy or Macrolide) OR Respiratory FQ"},
            {"id": "14b", "content": "Severe (ICU): Same as above, tetracyclines not listed"},
            {"id": "14c", "content": "Consider vancomycin (not guideline recommendation)"},
            {"id": "14d", "content": "Can transition to oral when stable"}
        ]
    },
    {
        "id": "tg-15",
        "stepNumber": 15,
        "title": "What happened to HCAP?",
        "pageRef": "p.7",
        "comments": [
            "HCAP (healthcare-associated pneumonia) went away in 2016",
            "Now: previous microbiology is primary driver for MRSA, Pseudomonas coverage",
            "Recent hospitalization/SNF + broad-spectrum abx also considered",
            "Detailed history, personalized approach is key"
        ]
    },
    {
        "id": "tg-16",
        "stepNumber": 16,
        "title": "What are the organisms and empiric therapy for HAP/VAP?",
        "pageRef": "p.7-8",
        "subSteps": [
            {"id": "16a", "content": "Organisms: S. aureus (MRSA), P. aeruginosa, Enterobacteriaceae, ESBL"},
            {"id": "16b", "content": "Empiric: Vancomycin or Linezolid + Anti-pseudomonal beta-lactam"},
            {"id": "16c", "content": "Plus/minus: Anti-pseudomonal FQ or Aminoglycoside"},
            {"id": "16d", "content": "De-escalate! Duration: 7 days (historically 14-21)"}
        ]
    },
    {
        "id": "tg-17",
        "stepNumber": 17,
        "title": "What is COVID-19 outpatient treatment?",
        "pageRef": "p.9",
        "subSteps": [
            {"id": "17a", "content": "Goal: Stop progression to hospital/death"},
            {"id": "17b", "content": "Nirmatrelvir/ritonavir (Paxlovid): protease inhibitor, MANY drug interactions"},
            {"id": "17c", "content": "Remdesivir: RNA polymerase inhibitor, IV only"},
            {"id": "17d", "content": "Molnupiravir: contraindication in pregnant/pregnancy potential"}
        ]
    },
    {
        "id": "tg-18",
        "stepNumber": 18,
        "title": "What is COVID-19 hospitalized treatment?",
        "pageRef": "p.9",
        "subSteps": [
            {"id": "18a", "content": "Room air (moderate): supportive care, consider outpatient therapies if high risk"},
            {"id": "18b", "content": "Hypoxia (moderate-severe): Remdesivir, dexamethasone, +/- tocilizumab or baricitinib"},
            {"id": "18c", "content": "Mechanical ventilation (critical): Dexamethasone, tocilizumab or baricitinib"}
        ]
    },
    {
        "id": "tg-19",
        "stepNumber": 19,
        "title": "What is influenza treatment?",
        "pageRef": "p.9",
        "comments": [
            "Vaccination is key (less efficacious than COVID vaccines)",
            "Treatment modestly effective, must start early",
            "Oseltamivir: mainstay, 5 days (longer for critically ill)",
            "Baloxavir: single dose, recent approval"
        ]
    },
    {
        "id": "tg-20",
        "stepNumber": 20,
        "title": "When should acute bronchitis be treated with antibiotics?",
        "pageRef": "p.10",
        "subSteps": [
            {"id": "20a", "content": "Vast majority viral - antimicrobials NOT warranted"},
            {"id": "20b", "content": "Exceptions: B. pertussis (macrolides), Influenza (oseltamivir)"},
            {"id": "20c", "content": "Mycoplasma/Chlamydia: macrolide, doxycycline"},
            {"id": "20d", "content": "Symptomatic treatment is mainstay"}
        ]
    },
    {
        "id": "tg-21",
        "stepNumber": 21,
        "title": "What is treatment for COPD exacerbation?",
        "pageRef": "p.10",
        "subSteps": [
            {"id": "21a", "content": "Who gets abx: 3 cardinal symptoms (dyspnea, sputum volume, purulence) or 2 if purulence"},
            {"id": "21b", "content": "Oral: Amoxicillin/clavulanate, Doxycycline, Macrolides, Respiratory FQs"},
            {"id": "21c", "content": "IV: For risk factors (comorbidities, severe COPD, frequent exacerbations)"},
            {"id": "21d", "content": "Duration: 5-7 days"}
        ]
    },
    {
        "id": "tg-22",
        "stepNumber": 22,
        "title": "When should sinusitis be treated with antibiotics?",
        "pageRef": "p.10",
        "subSteps": [
            {"id": "22a", "content": "Usually viral - only treat if:"},
            {"id": "22b", "content": "1. Persistence >10 days with no improvement"},
            {"id": "22c", "content": "2. Severe symptoms (fever >39 + purulent discharge/facial pain ≥3-4 days)"},
            {"id": "22d", "content": "3. Worsening symptoms"},
            {"id": "22e", "content": "Treatment: Amoxicillin/clavulanate, Doxycycline, FQ; Duration: 5-7 days"}
        ]
    },
    {
        "id": "tg-23",
        "stepNumber": 23,
        "title": "What are the empiric regimens for bacterial meningitis by age?",
        "pageRef": "p.11",
        "subSteps": [
            {"id": "23a", "content": "<1 month: Ampicillin + gentamicin (or cefotaxime, avoid ceftriaxone)"},
            {"id": "23b", "content": "1-23 months & 2-50 years: Vancomycin + 3G cephalosporin"},
            {"id": "23c", "content": ">50 years: Vancomycin + 3G cephalosporin + ampicillin (for Listeria)"},
            {"id": "23d", "content": "Dexamethasone 10mg q6h x4 days (give PRIOR to first abx)"}
        ]
    },
    {
        "id": "tg-24",
        "stepNumber": 24,
        "title": "What antibiotics have good CNS penetration?",
        "pageRef": "p.11",
        "subSteps": [
            {"id": "24a", "content": "Sufficient: 3rd/4th gen cephalosporins, Penicillin, Ampicillin"},
            {"id": "24b", "content": "Vancomycin, TMP/SMX, Fluoroquinolones, Metronidazole"},
            {"id": "24c", "content": "Insufficient: Tetracyclines, Aminoglycosides, Polymyxins"},
            {"id": "24d", "content": "Use IV at maximal doses, bactericidal preferred"}
        ]
    },
    {
        "id": "tg-25",
        "stepNumber": 25,
        "title": "What is the treatment for Listeria meningitis?",
        "pageRef": "p.11",
        "subSteps": [
            {"id": "25a", "content": "DOC: Ampicillin (HELPS bug)"},
            {"id": "25b", "content": "Alternatives: TMP/SMX (good efficacy), Meropenem"},
            {"id": "25c", "content": "Gentamicin sometimes added (but 'silly' per notes)"},
            {"id": "25d", "content": "Risk: >50 yo, pregnant, immunocompromised"}
        ]
    },
    {
        "id": "tg-26",
        "stepNumber": 26,
        "title": "What is meningitis prophylaxis?",
        "pageRef": "p.12",
        "subSteps": [
            {"id": "26a", "content": "N. meningitidis: household contacts, oral secretion exposure"},
            {"id": "26b", "content": "Treatment: Ciprofloxacin x1 (alternatives: Rifampin 2d, Ceftriaxone IM)"},
            {"id": "26c", "content": "H. influenzae: everyone in household with unvaccinated children"},
            {"id": "26d", "content": "Treatment: Rifampin"}
        ]
    },
    {
        "id": "tg-27",
        "stepNumber": 27,
        "title": "What is the treatment for SBP (spontaneous bacterial peritonitis)?",
        "pageRef": "p.13",
        "subSteps": [
            {"id": "27a", "content": "Common in cirrhosis → ascites"},
            {"id": "27b", "content": "Organisms: E. coli, Streptococcus, Klebsiella"},
            {"id": "27c", "content": "Treatment: 3rd generation cephalosporins"},
            {"id": "27d", "content": "Duration: 5-7 days"},
            {"id": "27e", "content": "Prophylaxis (high risk/history): TMP/SMX 5d/wk or Cipro weekly"}
        ]
    },
    {
        "id": "tg-28",
        "stepNumber": 28,
        "title": "What is the treatment for intra-abdominal infections?",
        "pageRef": "p.13",
        "subSteps": [
            {"id": "28a", "content": "Organisms: B. fragilis, E. coli"},
            {"id": "28b", "content": "Community-acquired: Cephalosporin + metronidazole OR Cefoxitin"},
            {"id": "28c", "content": "Nosocomial/critically ill: Cefepime/MTZ, Pip/tazo, Carbapenem"},
            {"id": "28d", "content": "Duration: 4-5 days with source control (guideline recommendation)"}
        ]
    },
    {
        "id": "tg-29",
        "stepNumber": 29,
        "title": "What is the current treatment for C. difficile?",
        "pageRef": "p.14",
        "subSteps": [
            {"id": "29a", "content": "D/C broad-spectrum abx and acid-suppressive agents if possible"},
            {"id": "29b", "content": "Fidaxomicin (superior but costly) or Oral vancomycin"},
            {"id": "29c", "content": "Metronidazole almost never recommended (inferior)"},
            {"id": "29d", "content": "Duration: 10-14 days; recurrence common (consider FMT)"}
        ]
    },
    {
        "id": "tg-30",
        "stepNumber": 30,
        "title": "What is the treatment for chlamydia?",
        "pageRef": "p.15",
        "subSteps": [
            {"id": "30a", "content": "Doxycycline 100 mg PO BID x7 days (first-line per 2021 guidelines)"},
            {"id": "30b", "content": "Azithromycin 1g x1"},
            {"id": "30c", "content": "Doxycycline superior for rectal chlamydia in MSM"},
            {"id": "30d", "content": "Partners: evaluate if sexual contact in last 60 days; abstain x7 days"}
        ]
    },
    {
        "id": "tg-31",
        "stepNumber": 31,
        "title": "What is the treatment for gonorrhea?",
        "pageRef": "p.15-16",
        "subSteps": [
            {"id": "31a", "content": "Uncomplicated: Ceftriaxone 500mg IM x1 (≥150kg = 1g)"},
            {"id": "31b", "content": "PLUS Doxycycline 100mg PO x7 days (unless chlamydia ruled out)"},
            {"id": "31c", "content": "Disseminated (septic arthritis, endocarditis): Full-dose 3G ceph IV"},
            {"id": "31d", "content": "Duration depends on site"}
        ]
    },
    {
        "id": "tg-32",
        "stepNumber": 32,
        "title": "What is the treatment for syphilis by stage?",
        "pageRef": "p.15",
        "subSteps": [
            {"id": "32a", "content": "Penicillin preferred for ALL stages"},
            {"id": "32b", "content": "Primary/Secondary: Benzathine penicillin IM x1"},
            {"id": "32c", "content": "Latent (late): 3 doses at 1-week intervals"},
            {"id": "32d", "content": "Neurosyphilis: High-dose IV penicillin"}
        ]
    },
    {
        "id": "tg-33",
        "stepNumber": 33,
        "title": "What is the treatment for bacterial vaginosis and trichomoniasis?",
        "pageRef": "p.16",
        "subSteps": [
            {"id": "33a", "content": "Bacterial vaginosis (anaerobes): Metronidazole x7 days"},
            {"id": "33b", "content": "Trichomoniasis: Metronidazole 2g PO x1 dose"},
            {"id": "33c", "content": "Candidiasis: Fluconazole 150mg x1 (or topicals)"}
        ]
    },
    {
        "id": "tg-34",
        "stepNumber": 34,
        "title": "What is the treatment for pelvic inflammatory disease?",
        "pageRef": "p.16",
        "subSteps": [
            {"id": "34a", "content": "Organisms: N. gonorrhea, C. trachomatis, Gram(-), anaerobes"},
            {"id": "34b", "content": "Empiric: Cefoxitin + doxycycline"},
            {"id": "34c", "content": "Can transition to oral if mild-moderate or clinical response"},
            {"id": "34d", "content": "Cover same organisms"}
        ]
    },
    {
        "id": "tg-35",
        "stepNumber": 35,
        "title": "What is the treatment for genital herpes?",
        "pageRef": "p.14-15",
        "subSteps": [
            {"id": "35a", "content": "First episode: Valacyclovir or Acyclovir x7-10 days"},
            {"id": "35b", "content": "Suppressive (≥6 episodes/yr): Valacyclovir daily (reduces freq 70-80%)"},
            {"id": "35c", "content": "Episodic: 5-day course"},
            {"id": "35d", "content": "Severe (disseminated): IV acyclovir 5-10 mg/kg q8h, then PO to complete 10d"}
        ],
        "comments": ["Valacyclovir offers twice-daily dosing", "Drugs do NOT eradicate latent virus"]
    }
]

module_16 = {
    "id": "treatment-guidelines",
    "name": "Selected Treatment Guidelines",
    "shortName": "Treatment Guidelines",
    "totalSteps": 35,
    "steps": module_16_steps
}

# Now read the existing modules and combine all
print("Generating complete pharmacy flashcard set...")

# Load existing Module 13 (Women's Health)
with open('/Users/mitchellcarter/Documents/Github/olivia-flashcards/app/src/data/pharm-exams.json', 'r') as f:
    existing = json.load(f)

# Load Module 14
with open('/Users/mitchellcarter/Documents/Github/olivia-flashcards/pharm-module-14.json', 'r') as f:
    module_14_data = json.load(f)
    module_14 = module_14_data['exams'][0]

# Combine all modules
all_exams = {
    "exams": [
        existing['exams'][0],  # Module 13
        module_14,              # Module 14
        module_15,              # Module 15
        module_16               # Module 16
    ]
}

# Save complete file
with open('/Users/mitchellcarter/Documents/Github/olivia-flashcards/app/src/data/pharmacy-exams.json', 'w') as f:
    json.dump(all_exams, f, indent=2)

print(f"✓ Module 13 (Women's Health): {existing['exams'][0]['totalSteps']} cards")
print(f"✓ Module 14 (ID Part 1): {module_14['totalSteps']} cards")
print(f"✓ Module 15 (ID Part 2): {module_15['totalSteps']} cards")
print(f"✓ Module 16 (Treatment Guidelines): {module_16['totalSteps']} cards")
print(f"\nTotal: {sum([existing['exams'][0]['totalSteps'], module_14['totalSteps'], module_15['totalSteps'], module_16['totalSteps']])} flashcards")
print("\nSaved to: app/src/data/pharmacy-exams.json")
