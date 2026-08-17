import os
import re

template_file = "product-acytron-forte.html"

with open(template_file, "r", encoding="utf-8") as f:
    template_content = f.read()

products = [
    {
        "filename": "product-himract-pro.html",
        "title": "Himract Pro - Himeros Pharma Ltd.",
        "name": "Himract Pro",
        "category_badges": '<span class="inline-block px-3 py-1 bg-brand-100 text-brand-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Andrology</span>\n                        <span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Male Sexual Dysfunction & Infertility",
        "image": "items/himract-pro.jpeg",
        "description_short": "A synergistic combination of HIMRACT PRO works through a multi-targeted mechanism designed to address the vascular, hormonal, neurological, and psychological components of male sexual dysfunction.",
        "description_long": "A synergistic combination of HIMRACT PRO works through a multi-targeted mechanism designed to address the vascular, hormonal, neurological, and psychological components of male sexual dysfunction. It enhances nitric oxide synthesis, promoting vasodilation, improved penile blood flow, and erection, boosts endogenous testosterone production, libido, stamina, and sexual performance. Improving microcirculation and cavernosal blood supply. And, modulates stress-related neurotransmitter imbalance, improving mood and sexual confidence. Himract Pro supports Erection, Rigidity, Duration, Orgasm, Satisfaction in Male supperfing from Sexual Dysfunction..",
        "composition": "L-arginine + Tribulus Terrestris + Fenugreek Extract + Hypericum Perforatum + Mucuna Pruriens + Gingko Biloba + Zinc + Vitamin B6",
        "packaging": "One Sachet of 5 gms",
        "indications": "Low Libido, Erectile Dysfunction, Premature Ejaculation, Anorgasmia"
    },
    {
        "filename": "product-himract-gold.html",
        "title": "Himract Gold - Himeros Pharma Ltd.",
        "name": "Himract Gold",
        "category_badges": '<span class="inline-block px-3 py-1 bg-brand-100 text-brand-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Andrology</span>\n                        <span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Advanced Male Sexual Performance",
        "image": "items/Himract Gold med.png",
        "description_short": "A scientifically designed multi-mechanistic formulation that supports male sexual performance, vitality, and reproductive wellness through vascular, hormonal, neurological, and metabolic pathways.",
        "description_long": "A scientifically designed multi-mechanistic formulation that supports male sexual performance, vitality, and reproductive wellness through vascular, hormonal, neurological, and metabolic pathways. It enhances nitric oxide production and blood flow, supports endothelial function and antioxidant protection. Boost testosterone balance, libido, stamina, mood, and orgasmic response. Himract Gold also improves nutrient absorption, making the formulation a comprehensive support therapy for male sexual dysfunction and performance enhancement, with Power of 12 solid components acting as the most upgraded product in Male Sexual Dysfunction.",
        "composition": "L-arginine + L-citrulline + Bioperine (Black Pepper Exxtract) + Alga Ecklonia Bicyclis + Tribulus Terrestris + Pine Bark Extract + Fenugreek Extract + Hypericum Perforatum + Mucuna Pruriens + Gingko Biloba + Zinc + Vitamin D2 + Yohimbe Bark Extract",
        "packaging": "1*15 Tablets/ Strip",
        "indications": "Low Libido, Erectile Dysfunction, Premature Ejaculation, Anorgasmia"
    },
    {
        "filename": "product-androwin.html",
        "title": "Androwin - Himeros Pharma Ltd.",
        "name": "Androwin",
        "category_badges": '<span class="inline-block px-3 py-1 bg-brand-100 text-brand-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Andrology</span>\n                        <span class="inline-block px-3 py-1 bg-pink-100 text-pink-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">IVF</span>',
        "subtitle": "Male Infertility & IVF Support",
        "image": "items/androwin.jpeg",
        "description_short": "A scientifically formulated antioxidant and mitochondrial support therapy designed to improve male fertility by enhancing sperm energy metabolism, motility, and cellular protection.",
        "description_long": "A scientifically formulated antioxidant and mitochondrial support therapy designed to improve male fertility by enhancing sperm energy metabolism, motility, and cellular protection. Androwin improves mitochondrial function and ATP production, supporting sperm vitality and motility. It  provides potent antioxidant protection against oxidative stress and DNA damage, while supports testosterone balance, spermatogenesis, and sperm quality. Together, the formulation offers comprehensive support for sperm count, motility, morphology, and overall reproductive health in male infertility management.",
        "composition": "Ubiquinol Acetate (Reduced CoQ10) + L-Carnitine L-Tartrate 10% + Zinc Sulphate Monohydrate + Lycopene 6%",
        "packaging": "1 x 10 Cap/ strip",
        "indications": "the management of Male Infertility"
    },
    {
        "filename": "product-erectlong.html",
        "title": "Erectlong - Himeros Pharma Ltd.",
        "name": "Erectlong",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Premature Ejaculation",
        "image": "items/Erectlong.jpeg",
        "description_short": "A scientifically balanced neurohormonal formulation designed to support ejaculatory control, sexual confidence, and overall male sexual wellness in premature ejaculation.",
        "description_long": "A scientifically balanced neurohormonal formulation designed to support ejaculatory control, sexual confidence, and overall male sexual wellness in premature ejaculation. It supports dopaminergic pathways involved in sexual response and pleasure, while it also helps modulate stress, anxiety, and neurotransmitter balance associated with performance-related dysfunction. Erectlong also supports stress adaptation, stamina, and hormonal balance, improve vitality, energy metabolism, and reproductive strength. Together, the formulation provides comprehensive support for ejaculatory control, sexual endurance, emotional well-being, and overall male reproductive health.",
        "composition": "Mucuna Pruriens + Hypericum Perforatum + Withania Somnifera + Asphaltum Punja",
        "packaging": "1*10 Tablets/Strip",
        "indications": "Premature Ejaculation"
    },
    {
        "filename": "product-tadox-2-5.html",
        "title": "Tadox 2.5 - Himeros Pharma Ltd.",
        "name": "Tadox 2.5",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Erectile Dysfunction",
        "image": "items/tadox-2\'5.jpeg",
        "description_short": "Tadox 2.5 is a low-dose tadalafil-based therapy designed to provide continuous support in erectile dysfunction (ED) and premature ejaculation (PME) through improved penile hemodynamics.",
        "description_long": "2.5 is a low-dose tadalafil-based therapy designed to provide continuous support in erectile dysfunction (ED) and premature ejaculation (PME) through improved penile hemodynamics and sexual performance stability. By inhibiting PDE-5, it enhances nitric oxide-mediated vasodilation, improving penile blood flow, erection quality, and erectile sustainability. Daily low-dose therapy also helps reduce performance anxiety, improve sexual confidence, and enhance ejaculatory control by supporting consistent erectile function and prolonged sexual performance. Its long-acting profile makes it suitable for sustained, spontaneous, and long-term management of ED and PME.",
        "composition": "Micronized Tadalafil",
        "packaging": "1*10 Tablets/Strip",
        "indications": "Penile Vascular Health"
    },
    {
        "filename": "product-tadox-dp.html",
        "title": "Tadox DP - Himeros Pharma Ltd.",
        "name": "Tadox DP",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "PE + ED Dual Therapy",
        "image": "items/tadox-dp.jpeg",
        "description_short": "A dual-action formulation combining Dapoxetine Hydrochloride and Tadalafil designed to provide comprehensive management of premature ejaculation (PME) and erectile dysfunction (ED).",
        "description_long": "A dual-action formulation combining Dapoxetine Hydrochloride and Tadalafil designed to provide comprehensive management of premature ejaculation (PME) and erectile dysfunction (ED). Dapoxetine, a short-acting SSRI, helps improve ejaculatory control and increase intravaginal ejaculatory latency time (IELT) by modulating serotonin pathways, while Tadalafil enhances nitric oxide-mediated penile blood flow, improving erection quality and sustainability. Together, the combination supports improved sexual confidence, erection maintenance, ejaculatory control, and overall sexual satisfaction, making it an effective integrated therapy for men experiencing both PME and ED simultaneously.",
        "composition": "Dapoxetine Hydrochloride + Tadalafil",
        "packaging": "1*4 Tablets/Strip",
        "indications": "Premature Ejaculation / Erectile Dysfunction"
    },
    {
        "filename": "product-himract-gel.html",
        "title": "Himract Gel - Himeros Pharma Ltd.",
        "name": "Himract Gel",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>\n                        <span class="inline-block px-3 py-1 bg-pink-100 text-pink-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Gynecology</span>',
        "subtitle": "Topical Nitric Oxide Therapy",
        "image": "items/himrect gel.jpeg",
        "description_short": "L-Arginine Gel 5% w/w is a topical nitric oxide-enhancing therapy designed to support erectile function and sexual performance in men and sensory enhancement in women.",
        "description_long": "L-Arginine Gel 5% w/w is a topical nitric oxide-enhancing therapy designed to support erectile function and sexual performance in men with erectile dysfunction (ED) and premature ejaculation (PME). By increasing local nitric oxide availability, it promotes vasodilation, improved penile blood circulation, enhanced sensitivity, and erection quality. For females, it helps improve genital blood flow, tissue engorgement, lubrication, and sensory responsiveness by enhancing nitric oxide-mediated vascular relaxation. Increased local circulation promotes greater arousal, comfort, and sensitivity during intimacy.",
        "composition": "L-Arginine Gel 5% w/w",
        "packaging": "One tube: 20 gm",
        "indications": "Erectile Dysfunction, Sensory & Microcirculatory Enhancement in Females"
    },
    {
        "filename": "product-durahim-gel.html",
        "title": "Durahim Gel - Himeros Pharma Ltd.",
        "name": "Durahim Gel",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Premature Ejaculation Management",
        "image": "items/durahim-gel.jpeg",
        "description_short": "DURAHIM Gel features a synergistic dual-anesthetic formula combining Lidocaine Hydrochloride and Prilocaine. Indicated for Premature Ejaculation (PME).",
        "description_long": "DURAHIM Gel features a synergistic dual-anesthetic formula combining Lidocaine Hydrochloride IP 2.5% w/w and Prilocaine IP 2.5% w/w. Indicated for Premature Ejaculation (PME), it provides rapid, localized desensitization to prolong latency time. When paired with pro-erectile treatments like HIMRACT Gel , it forms a comprehensive therapy for overlapping PME and Erectile Dysfunction (ED)—simultaneously sustaining optimal penile blood flow while delaying the ejaculatory reflex for complete sexual performance management.",
        "composition": "Lidocaine Hydrochloride IP 2.5% w/w, Prilocaine IP 2.5% w/w",
        "packaging": "One Tube: 8 gm",
        "indications": "Premature Ejaculation"
    },
    {
        "filename": "product-durahim-30.html",
        "title": "Durahim 30 - Himeros Pharma Ltd.",
        "name": "Durahim 30",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Premature Ejaculation Therapy (30 mg)",
        "image": "items/durahim-30.jpeg",
        "description_short": "DURAHIM 30 contains Dapoxetine Hydrochloride IP 30 mg, the gold standard fast-acting oral treatment approved for Premature Ejaculation (PE).",
        "description_long": "DURAHIM 30 contains Dapoxetine Hydrochloride IP 30 mg, the gold standard fast-acting oral treatment specifically approved for Premature Ejaculation (PE). Taken 1–2 hours before sexual activity, it regulates central ejaculatory control mechanisms, significantly extending intravaginal latency time, enhancing control, and reducing performance distress.",
        "composition": "Dapoxetine Hydrochloride IP 30 mg",
        "packaging": "1*10 Tablets/Strip",
        "indications": "Premature Ejaculation"
    },
    {
        "filename": "product-durahim-60.html",
        "title": "Durahim 60 - Himeros Pharma Ltd.",
        "name": "Durahim 60",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Premature Ejaculation Therapy (60 mg)",
        "image": "items/durahim.jpeg",
        "description_short": "DURAHIM 60 contains Dapoxetine Hydrochloride IP 60 mg, a higher-strength fast-acting oral formulation for advanced management of Premature Ejaculation (PE).",
        "description_long": "DURAHIM 60 contains Dapoxetine Hydrochloride IP 60 mg, a higher-strength fast-acting oral treatment specifically approved for Premature Ejaculation (PE). Taken 1–2 hours before sexual activity, it regulates central ejaculatory control mechanisms, significantly extending intravaginal latency time, enhancing control, and reducing performance distress for complete sexual performance management.",
        "composition": "Dapoxetine Hydrochloride IP 60 mg",
        "packaging": "1*10 Tablets/Strip",
        "indications": "Premature Ejaculation"
    },
    {
        "filename": "product-himdriol.html",
        "title": "Himdriol - Himeros Pharma Ltd.",
        "name": "Himdriol",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>',
        "subtitle": "Hypogonadism & Low Libido",
        "image": "items/himdriol.jpeg",
        "description_short": "HIMDRIOL softgel capsules contain Testosterone Undecanoate 40 mg, an oral testosterone replacement therapy formulated to correct hypogonadism and improve overall sexual function.",
        "description_long": "HIMDRIOL softgel capsules contain Testosterone Undecanoate 40 mg, an oral testosterone replacement therapy formulated to correct hypogonadism and improve overall sexual function. While primarily targeting testosterone deficiency, it plays a vital role in comprehensive sexual health management. Low testosterone is heavily linked to reduced libido, erectile issues, and secondary ejaculatory dysfunction; by sustaining physiological hormone levels, HIMDRIOL restores sexual desire, improves metabolic and vascular performance, and supports erectile structural health, offering foundational hormonal therapy that complements specific PME treatments.",
        "composition": "Testosterone Undecanoate Soft Gelatin Capsules",
        "packaging": "1*10 Softgel Capsule /Strip",
        "indications": "Primary & Secondary Hypogonadism, Low Libido"
    },
    {
        "filename": "product-tadox-5.html",
        "title": "Tadox 5 - Himeros Pharma Ltd.",
        "name": "Tadox 5",
        "category_badges": '<span class="inline-block px-3 py-1 bg-brand-100 text-brand-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Andrology</span>',
        "subtitle": "BPH / LUTS Management",
        "image": "items/tadox-5.jpeg",
        "description_short": "TADOX 5 contains Micronized Tadalafil 5 mg, a highly effective once-daily oral formulation specifically approved for managing Benign Prostatic Hyperplasia (BPH) and Lower Urinary Tract Symptoms (LUTS).",
        "description_long": "TADOX 5 contains Micronized Tadalafil 5 mg, a highly effective once-daily oral formulation specifically approved for managing Benign Prostatic Hyperplasia (BPH) and Lower Urinary Tract Symptoms (LUTS), whether presenting with or without concurrent Erectile Dysfunction (ED). It offers a comprehensive, dual-action therapy by significantly improving total International Prostate Symptom Score (IPSS) and BPH Impact Index (BII) scores, while simultaneously reducing intraprostatic inflammation. By treating both urological blockages and sexual health complications, it delivers unified, continuous symptom relief and improves the overall Sexual Encounter Profile (SEP) score.",
        "composition": "Tadalafil",
        "packaging": "1*10 Tablets/Strip",
        "indications": "BPH / LUTS"
    },
    {
        "filename": "product-himtam-d.html",
        "title": "HIMTAM-D - Himeros Pharma Ltd.",
        "name": "HIMTAM-D",
        "category_badges": '<span class="inline-block px-3 py-1 bg-brand-100 text-brand-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Andrology</span>',
        "subtitle": "BPH / LUTS Dual Therapy",
        "image": "items/hitam-d.jpeg",
        "description_short": "HIMTAM-D is a powerful fixed-dose combination capsule pairing Tamsulosin Hydrochloride Prolonged-Release with Dutasteride. Engineered for Benign Prostatic Hyperplasia (BPH).",
        "description_long": "HIMTAM-D is a powerful fixed-dose combination capsule pairing Tamsulosin Hydrochloride Prolonged-Release with Dutasteride. Engineered for Benign Prostatic Hyperplasia (BPH), this formulation delivers complete therapy by targeting both the dynamic and structural components of the disease. HIMTAM-D offers rapid, functional relief from urinary blockages by relaxing the bladder neck, and addresses the underlying cause by shrinking the enlarged prostate gland over time. Together, they effectively control BPH progression, minimize the risk of acute urinary retention, and significantly alleviate Lower Urinary Tract Symptoms (LUTS).",
        "composition": "Tamsulosin Hydrochloride Prolonged-Release & Dutasteride",
        "packaging": "1*15 Capsules/Strip",
        "indications": "BPH / LUTS"
    },
    {
        "filename": "product-librt-tablet.html",
        "title": "Librt Tablet - Himeros Pharma Ltd.",
        "name": "Librt Tablet",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>\n                        <span class="inline-block px-3 py-1 bg-pink-100 text-pink-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Gynecology</span>',
        "subtitle": "Hypoactive Sexual Desire Support",
        "image": "items/librt capsule.jpeg",
        "description_short": "This advanced nutraceutical formula combines L-Arginine, Horny Goat Weed Extract, and Maca Extract to deliver a complete therapy for both Erectile Dysfunction (ED) and Premature Ejaculation (PME).",
        "description_long": "This advanced nutraceutical formula combines L-Arginine, Horny Goat Weed Extract, and Maca Extract to deliver a complete, dual-action therapy for both Erectile Dysfunction (ED) and Premature Ejaculation (PME) in males, and Hypoactive Sexual Desire Disorder (HSDD) in females. Librt synergistically optimize pelvic blood flow and nitric oxide pathways to restore robust erectile function and firmness. Simultaneously, It acts adaptogenically to balance neuroendocrine function, enhance stamina, and improve ejaculatory control.",
        "composition": "L-Arginine, Horny Goat Weed Extract & Maca Extract",
        "packaging": "1*10 tablets/Strip",
        "indications": "Hypoactive Sexual Desire Disorder"
    },
    {
        "filename": "product-librt-pro.html",
        "title": "Librt Pro - Himeros Pharma Ltd.",
        "name": "Librt Pro",
        "category_badges": '<span class="inline-block px-3 py-1 bg-purple-100 text-purple-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Sexology</span>\n                        <span class="inline-block px-3 py-1 bg-pink-100 text-pink-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Gynecology</span>',
        "subtitle": "Advanced Female Sexual Wellness",
        "image": "items/librt-pro.jpeg",
        "description_short": "LIBRT PRO is an advanced female sexual wellness formulation developed to support women experiencing Hypoactive Sexual Desire Disorder (HSDD), reduced arousal, and diminished sexual responsiveness.",
        "description_long": "LIBRT PRO is an advanced female sexual wellness formulation developed to support women experiencing Hypoactive Sexual Desire Disorder (HSDD), reduced arousal, and diminished sexual responsiveness. As an upgraded formulation, it combines higher-strength L-Arginine (3 g), Horny Goat Weed Extract, and Maca Extract to target vascular, hormonal, neurological, and energy-related aspects of female sexual health. By supporting genital blood flow, sensitivity, libido, and emotional well-being, LIBRT PRO offers comprehensive support for female sexual desire, arousal, intimacy, and overall sexual satisfaction.",
        "composition": "L-Arginine (3g), Horny Goat Weed Extract & Maca Extract",
        "packaging": "One sachet",
        "indications": "Hypoactive Sexual Arousal Disorder"
    },
    {
        "filename": "product-prokd.html",
        "title": "Pro KD-45 / 15 - Himeros Pharma Ltd.",
        "name": "Pro KD-45 / 15",
        "category_badges": '<span class="inline-block px-3 py-1 bg-green-100 text-green-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Nephrology</span>',
        "subtitle": "Gut-Kidney Synbiotic Therapy",
        "image": "items/Pro-kd45.jpeg",
        "description_short": "Pro-KD 45 / 15 features a balanced synbiotic formula combining specific probiotic strains with prebiotic to protect the gut-kidney metabolism.",
        "description_long": "Pro-KD 45 / 15 features a balanced synbiotic formula combining specific probiotic strains with prebiotic. Specially designed to protect the gut-kidney metabolism, it provides a complete adjuvant therapy for chronic kidney disease and End-Stage Renal Disease (ESRD). By balancing the microbiome, strengthening gut defense, and actively removing systemic nitrogenous wastes through the stools, it dramatically lowers the toxic burden (reducing BUN up to 63% and creatinine up to 43%) to successfully delay progression to ESRD.",
        "composition": "Streptococcus Thermophilus, Lactobacillus Acidophilus, Bifidobacterium Longum, Bacillus Coagulans, Fructo Oligosaccharides",
        "packaging": "1*10 Capsules/Strip",
        "indications": "Gut-Kidney metabolism"
    },
    {
        "filename": "product-alpha-kd.html",
        "title": "AlphaKD / DS - Himeros Pharma Ltd.",
        "name": "AlphaKD / DS",
        "category_badges": '<span class="inline-block px-3 py-1 bg-green-100 text-green-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Nephrology</span>',
        "subtitle": "Chronic Kidney Disease Support",
        "image": "items/aplha-kd.jpeg",
        "description_short": "Alpha-KD / Alpha-KD DS consists of a highly specialized formula of Alpha Ketoanalogues of Amino Acids. Indicated for Chronic Kidney Disease (CKD).",
        "description_long": "Alpha-KD / Alpha-KD DS consists of a highly specialized formula of Alpha Ketoanalogues of Amino Acids. Indicated for Chronic Kidney Disease (CKD), it serves as a complete nutritional and metabolic therapy to manage and delay progression to End-Stage Renal Disease (ESRD). When paired with a protein-restricted diet, it preserves essential nutritional status while recycling systemic wastes. By actively reducing the nitrogen load—lowering Blood Urea Nitrogen (BUN), urea, ammonia, creatinine, and harmful acids—it prevents uremic complications, maintains ideal amino acid balance, and effectively delays the initiation of dialysis.",
        "composition": "Alpha Ketoanalogue of Amino Acid",
        "packaging": "1*10 Tablets/Strip",
        "indications": "Chronic Kidney Disease"
    },
    {
        "filename": "product-acytron-kd.html",
        "title": "Acytron KD - Himeros Pharma Ltd.",
        "name": "Acytron KD",
        "category_badges": '<span class="inline-block px-3 py-1 bg-green-100 text-green-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Nephrology</span>',
        "subtitle": "CKD Progression Therapy",
        "image": "items/acytron-kd.jpeg",
        "description_short": "Acytron-KD features an advanced dual-active formula combining N-acetyl L-cysteine (NAC) and Taurine, delivered via specialized Tablet-in-Tablet Technology.",
        "description_long": "Acytron-KD features an advanced dual-active formula combining N-acetyl L-cysteine (NAC) and Taurine, delivered via specialized Tablet-in-Tablet Technology. Formulated to slow down Chronic Kidney Disease (CKD) progression, it provides a complete therapeutic approach to delay the onset of End-Stage Renal Disease (ESRD). The synergistic formulation targets the root drivers of renal decline by drastically mitigating oxidative stress, preserving vulnerable renal microvasculature, suppressing critical inflammatory mediators, and maintaining stable serum creatinine and eGFR levels to optimize remaining kidney function.",
        "composition": "N-acetyl L-cysteine + Taurine",
        "packaging": "1*1*10 Tablets/Strip",
        "indications": "Chronic Kidney Disease Progression"
    },
    {
        "filename": "product-stoxlate.html",
        "title": "Stoxlate - Himeros Pharma Ltd.",
        "name": "Stoxlate",
        "category_badges": '<span class="inline-block px-3 py-1 bg-green-100 text-green-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">Nephrology</span>',
        "subtitle": "Kidney Stones Management",
        "image": "items/pro-kd15.jpeg",
        "description_short": "STOXLATE is a specialized probiotic capsule containing 5 Billion CFUs of specific probiotic strains formulated specifically to reduce the formation of oxalate stones.",
        "description_long": "STOXLATE is a specialized probiotic capsule containing 5 Billion CFUs of Oxalobacter formigenesis, Lactobacillus acidophilus, Bifidobacterium lactis, and Bacillus coagulans. While formulated specifically to reduce the formation of oxalate stones, it plays a vital protective role in chronic kidney disease and End-Stage Renal Disease (ESRD) management. Since up to 50% of urinary oxalate originates from intestinal absorption, hyperoxaluria represents a major driver of renal calcification and nephron loss. By degrading dietary oxalate within the gut, STOXLATE prevents systemic absorption, reducing the risk of crystalline nephropathy and secondary renal deterioration.",
        "composition": "Oxalobacter Formingenesis + Lactobacillus Acidophilus + Bifidobacterium Lactis + Bacillus Coagulans",
        "packaging": "1*10 Capsules/Strip",
        "indications": "Kidney Stones"
    },
    {
        "filename": "product-curepcos.html",
        "title": "CurePCOS-M - Himeros Pharma Ltd.",
        "name": "CurePCOS-M",
        "category_badges": '<span class="inline-block px-3 py-1 bg-pink-100 text-pink-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">IVF / Gynecology</span>',
        "subtitle": "PCOS Induced Infertility Support",
        "image": "items/foliguard.jpeg",
        "description_short": "CurePcos M features a comprehensive combination of Myo-Inositol, D-Chiro-Inositol, Metformin Hydrochloride, L-Methylfolate, Calcium, and Mecobalamin.",
        "description_long": "CurePcos M features a comprehensive combination of Myo-Inositol, D-Chiro-Inositol, Metformin Hydrochloride, L-Methylfolate, Calcium, and Mecobalamin. Specifically engineered for PCOS-induced infertility, it acts as a complete, multi-targeted therapy. The formula corrects the core pathophysiological drivers of the disorder by simultaneously reversing insulin resistance, lowering fasting insulin levels, and balancing hormonal disruption. By improving oocyte quality, regulating ovulation rates, restoring menstrual regularity, and controlling damaging homocysteine levels, it systematically optimizes the metabolic and uterine environment to enhance conception success.",
        "composition": "Myo-Inositol BP + D-Chiro-Inositol + Metformin Hydrochloride IP + L-Methylfolate Calcium + Mecobalmin IP",
        "packaging": "1*10 Tablets/Strip",
        "indications": "PCOS induced Infertility"
    },
    {
        "filename": "product-foliguard.html",
        "title": "Foliguard - Himeros Pharma Ltd.",
        "name": "Foliguard",
        "category_badges": '<span class="inline-block px-3 py-1 bg-pink-100 text-pink-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">IVF / Gynecology</span>',
        "subtitle": "Fertility Support Formulation",
        "image": "items/foliguard.jpeg",
        "description_short": "Foliguard is a scientifically balanced fertility-support formulation designed to address metabolic, hormonal, oxidative, and reproductive disturbances.",
        "description_long": "Foliguard is a scientifically balanced fertility-support formulation designed to address metabolic, hormonal, oxidative, and reproductive disturbances commonly associated with female infertility and PCOS-related complications. CurePCOS helps improve insulin sensitivity and ovarian function, supports DNA synthesis and ovulatory health. It also acts as a antioxidant and endocrine support, helping improve oocyte quality, hormonal balance, follicular development, and reproductive wellness. Together, the formulation offers comprehensive support for ovulation, fertility potential, metabolic regulation, and healthy reproductive function.",
        "composition": "Myo-Inositol + D-Chiro-Inositol + L-Methylfolate + Calcium + Vitamin D3 + Melatonin with Zinc & Selenium",
        "packaging": "1*10 Tablets",
        "indications": "PCOS complications"
    },
    {
        "filename": "product-embry-s.html",
        "title": "Embryoshield - Himeros Pharma Ltd.",
        "name": "Embryoshield",
        "category_badges": '<span class="inline-block px-3 py-1 bg-pink-100 text-pink-700 text-[10px] font-semibold uppercase tracking-wider rounded-full">IVF / Gynecology</span>',
        "subtitle": "Maternal Nutrition & Vascular Support",
        "image": "items/embry-s.jpeg",
        "description_short": "Embryoshield is a scientifically designed maternal nutrition and vascular support formulation developed to support placental health, fetal growth, and healthy pregnancy outcomes.",
        "description_long": "Embryoshield is a scientifically designed maternal nutrition and vascular support formulation developed to support placental health, fetal growth, and healthy pregnancy outcomes in conditions such as IUGR, pre-eclampsia, and risk of premature birth. It enhances nitric oxide-mediated placental blood flow and nutrient delivery, it supports protein synthesis, fetal tissue development, and placental growth. Together, the formulation provides comprehensive support for uteroplacental circulation, fetal nourishment, angiogenesis, and healthy intrauterine development, helping improve fetal growth parameters and maternal-fetal wellness during high-risk pregnancies.",
        "composition": "L-Arginine & Leucine",
        "packaging": "One sachet",
        "indications": "Placental Health, IUGR, Premature Birth, Pre-Eclampsia"
    }
]

import re

def replace_content(html, product):
    # Replace Title
    html = re.sub(r'<title>.*?</title>', f'<title>{product["title"]}</title>', html)
    
    # Replace Breadcrumb Product Name
    html = re.sub(r'<span class="text-gray-800 font-medium">.*?</span>', f'<span class="text-gray-800 font-medium">{product["name"]}</span>', html)
    
    # Replace Image
    html = re.sub(r'<img src="items/[^"]+" alt="[^"]+" class="product-detail-img w-full h-full object-contain">', f'<img src="{product["image"]}" alt="{product["name"]}" class="product-detail-img w-full h-full object-contain">', html)
    
    # Replace Category Badges
    badges_regex = r'<div class="inline-flex items-center gap-2 mb-4">.*?</div>'
    html = re.sub(badges_regex, f'<div class="inline-flex items-center gap-2 mb-4">\n                        {product["category_badges"]}\n                    </div>', html, flags=re.DOTALL)
    
    # Replace Product Name H1
    html = re.sub(r'<h1 class="text-3xl lg:text-4xl font-bold text-gray-900 mb-3">.*?</h1>', f'<h1 class="text-3xl lg:text-4xl font-bold text-gray-900 mb-3">{product["name"]}</h1>', html)
    
    # Replace Subtitle
    html = re.sub(r'<p class="text-lg text-gray-500 mb-6">.*?</p>', f'<p class="text-lg text-gray-500 mb-6">{product["subtitle"]}</p>', html)
    
    # Remove Description Short if present
    html = re.sub(r'\s*<p class="text-gray-600 leading-relaxed mb-8">\s*.*?\s*</p>', '', html, flags=re.DOTALL)
    
    # Product Info (Description Long)
    info_desc_regex = r'<h3 class="text-lg font-bold text-gray-900 mb-4">Description</h3>\s*<p class="text-gray-600 leading-relaxed">.*?</p>'
    html = re.sub(info_desc_regex, f'<h3 class="text-lg font-bold text-gray-900 mb-4">Description</h3>\n                        <p class="text-gray-600 leading-relaxed">\n                            {product["description_long"]}\n                        </p>', html, flags=re.DOTALL)
    
    # Key Benefits (replace with Composition and Packaging)
    benefits_regex = r'<h3 class="text-lg font-bold text-gray-900 mb-4">Key Benefits</h3>\s*<ul class="space-y-3">.*?</ul>'
    benefits_replacement = f"""<h3 class="text-lg font-bold text-gray-900 mb-4">Composition & Packaging</h3>
                        <div class="space-y-4">
                            <div>
                                <h4 class="font-semibold text-gray-800">Composition:</h4>
                                <p class="text-gray-600 mt-1">{product["composition"]}</p>
                            </div>
                            <div>
                                <h4 class="font-semibold text-gray-800">Packaging:</h4>
                                <p class="text-gray-600 mt-1">{product["packaging"]}</p>
                            </div>
                        </div>"""
    html = re.sub(benefits_regex, benefits_replacement, html, flags=re.DOTALL)
    
    # Usage
    usage_regex = r'<strong>Usage:</strong>.*?</p>'
    html = re.sub(usage_regex, f'<strong>Usage:</strong> Management of {product["indications"]}.\n                        </p>', html, flags=re.DOTALL)
    
    return html

for product in products:
    print(f"Generating {product['filename']}...")
    new_html = replace_content(template_content, product)
    with open(product['filename'], 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Done.")
