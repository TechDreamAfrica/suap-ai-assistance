import flet as ft
import random
import time
import math

def get_ai_help(query, topic="biology"):
    """Enhanced AI help response for Biology"""
    try:
        responses = {
            "cells": "Cells are the fundamental units of life. Prokaryotic cells (bacteria, archaea) lack membrane-bound organelles and have genetic material freely floating in the cytoplasm. Eukaryotic cells (plants, animals, fungi, protists) have membrane-bound organelles including nucleus, mitochondria, endoplasmic reticulum, and Golgi apparatus. Plant cells additionally have chloroplasts, cell walls, and large vacuoles.",
            "dna": "DNA (deoxyribonucleic acid) is the hereditary material containing genetic instructions. Its double helix structure consists of nucleotides with bases: adenine (A), thymine (T), guanine (G), and cytosine (C). A pairs with T, G pairs with C. DNA replication occurs during S phase of cell cycle. Gene expression involves transcription (DNA to mRNA) and translation (mRNA to proteins).",
            "evolution": "Evolution is the change in heritable traits of biological populations over successive generations. Mechanisms include natural selection, genetic drift, gene flow, and mutation. Natural selection favors individuals with advantageous traits who survive and reproduce more successfully. Evidence includes fossil records, comparative anatomy, molecular biology, biogeography, and direct observation of evolutionary changes.",
            "ecosystem": "Ecosystems are communities of interacting organisms and their physical environment. Energy flows unidirectionally from producers (autotrophs) through primary, secondary, and tertiary consumers. Nutrients cycle through biogeochemical cycles (carbon, nitrogen, phosphorus). Keystone species have disproportionately large effects on ecosystem structure. Human activities significantly impact ecosystem balance through pollution, habitat destruction, and climate change.",
            "photosynthesis": "Photosynthesis converts light energy into chemical energy stored in glucose. The overall equation: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂. It occurs in two stages: light-dependent reactions (photosystems I & II in thylakoids produce ATP and NADPH) and light-independent reactions (Calvin cycle in stroma fixes CO₂ into glucose). Factors affecting rate include light intensity, CO₂ concentration, temperature, and chlorophyll availability.",
            "genetics": "Genetics studies heredity and variation. Mendel's laws describe inheritance patterns: Law of Segregation (alleles separate during gamete formation) and Law of Independent Assortment (different traits are inherited independently). Genetic crosses use Punnett squares to predict offspring ratios. Modern genetics includes molecular genetics, genomics, genetic engineering, and biotechnology applications like CRISPR gene editing.",
            "anatomy": "Human anatomy studies body structure and organization. Major systems include circulatory (heart, blood vessels, blood), respiratory (lungs, trachea, diaphragm), digestive (stomach, intestines, liver, pancreas), nervous (brain, spinal cord, nerves), endocrine (hormones and glands), musculoskeletal (bones, muscles, joints), excretory (kidneys, bladder), and integumentary (skin, hair, nails). Each system has specific functions that work together to maintain homeostasis.",
            "ecology": "Ecology examines relationships between organisms and their environment at multiple levels: individual, population, community, ecosystem, and biosphere. Key concepts include habitat vs niche, predator-prey dynamics, competition, symbiosis (mutualism, commensalism, parasitism), succession, and biodiversity. Conservation biology applies ecological principles to protect species and ecosystems from human impacts.",
            "respiration": "Cellular respiration breaks down glucose to produce ATP energy. Three stages: glycolysis (glucose → pyruvate in cytoplasm), Krebs cycle (pyruvate → CO₂ in mitochondrial matrix), and electron transport chain (produces most ATP in inner mitochondrial membrane). Aerobic respiration requires oxygen and produces ~32 ATP per glucose. Anaerobic respiration (fermentation) produces less ATP but allows survival without oxygen.",
            "mitosis": "Mitosis is nuclear division producing two genetically identical diploid cells for growth and repair. Phases include prophase (chromosomes condense, nuclear envelope breaks down), metaphase (chromosomes align at cell center), anaphase (sister chromatids separate), and telophase (nuclear envelopes reform). Cytokinesis divides the cytoplasm. Cell cycle checkpoints ensure proper DNA replication and chromosome separation.",
            "meiosis": "Meiosis is specialized cell division producing four genetically diverse haploid gametes from one diploid cell. Two divisions occur: meiosis I (homologous chromosomes separate) and meiosis II (sister chromatids separate). Crossing over during prophase I creates genetic recombination. Independent assortment of chromosomes increases genetic diversity. This process is essential for sexual reproduction and genetic variation."
        }
        
        query_lower = query.lower()
        for key, response in responses.items():
            if key in query_lower:
                return f"🔬 Biology AI Tutor: {response}"
        
        return "🔬 Biology AI Tutor: Biology is the study of living organisms and their interactions. I can help with cells, DNA, evolution, ecosystems, photosynthesis, genetics, anatomy, ecology, respiration, mitosis, meiosis, and more. Ask about specific topics for detailed explanations!"
    except Exception:
        return "🔬 Biology AI Tutor: I'm here to help with all aspects of biology! Try asking about cells, genetics, evolution, or any other biological concept."

class BiologyModule:
    def __init__(self, page):
        self.page = page
        self.current_quiz_level = "basic"
        self.quiz_score = 0
        self.quiz_question_index = 0
        
        # Enhanced quiz questions with detailed explanations
        self.quiz_questions = {
            "basic": [
                {
                    "question": "What is the basic unit of life?",
                    "options": ["Atom", "Molecule", "Cell", "Tissue"],
                    "correct": 2,
                    "explanation": "Cells are the basic structural and functional units of life. All living organisms are composed of one or more cells. This concept is fundamental to cell theory, which states that all life is cellular."
                },
                {
                    "question": "What process do plants use to make food from sunlight?",
                    "options": ["Photosynthesis", "Cellular respiration", "Fermentation", "Digestion"],
                    "correct": 0,
                    "explanation": "Photosynthesis is the process by which plants convert light energy, carbon dioxide, and water into glucose and oxygen. This process occurs in chloroplasts and is essential for life on Earth."
                },
                {
                    "question": "Where is DNA primarily located in animal cells?",
                    "options": ["Cytoplasm", "Nucleus", "Cell membrane", "Mitochondria"],
                    "correct": 1,
                    "explanation": "DNA is primarily located in the nucleus of eukaryotic cells, where it's organized into chromosomes. Small amounts of DNA are also found in mitochondria."
                },
                {
                    "question": "Which organelle is known as the 'powerhouse of the cell'?",
                    "options": ["Nucleus", "Ribosome", "Mitochondria", "Endoplasmic reticulum"],
                    "correct": 2,
                    "explanation": "Mitochondria are called the 'powerhouse of the cell' because they produce most of the cell's ATP energy through cellular respiration."
                },
                {
                    "question": "What type of organism can make its own food?",
                    "options": ["Consumer", "Producer", "Decomposer", "Predator"],
                    "correct": 1,
                    "explanation": "Producers (autotrophs) like plants can make their own food through photosynthesis or chemosynthesis, forming the base of food chains."
                }
            ],
            "intermediate": [
                {
                    "question": "During which phase of mitosis do chromosomes align at the cell's equator?",
                    "options": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
                    "correct": 1,
                    "explanation": "During metaphase, chromosomes align at the cell's equatorial plane (metaphase plate). This ensures equal distribution of genetic material to daughter cells."
                },
                {
                    "question": "What is the complementary base pair to adenine in DNA?",
                    "options": ["Guanine", "Cytosine", "Thymine", "Uracil"],
                    "correct": 2,
                    "explanation": "In DNA, adenine (A) pairs with thymine (T), and guanine (G) pairs with cytosine (C). This complementary base pairing is essential for DNA structure and replication."
                },
                {
                    "question": "Which process increases genetic variation in sexually reproducing organisms?",
                    "options": ["Mitosis", "Binary fission", "Crossing over", "Budding"],
                    "correct": 2,
                    "explanation": "Crossing over during meiosis creates genetic recombination by exchanging genetic material between homologous chromosomes, increasing genetic diversity."
                },
                {
                    "question": "What is the primary function of decomposers in ecosystems?",
                    "options": ["Produce oxygen", "Convert sunlight to energy", "Break down dead organic matter", "Control population size"],
                    "correct": 2,
                    "explanation": "Decomposers break down dead organic matter and waste products, recycling nutrients back into the ecosystem and maintaining nutrient cycles."
                },
                {
                    "question": "Which gas is released as a byproduct of photosynthesis?",
                    "options": ["Carbon dioxide", "Nitrogen", "Oxygen", "Methane"],
                    "correct": 2,
                    "explanation": "Oxygen is released as a byproduct of photosynthesis when water molecules are split during the light-dependent reactions. This oxygen is essential for aerobic life."
                }
            ],
            "advanced": [
                {
                    "question": "What is the role of tRNA in protein synthesis?",
                    "options": ["Carries genetic code", "Transfers amino acids", "Forms ribosome structure", "Catalyzes reactions"],
                    "correct": 1,
                    "explanation": "Transfer RNA (tRNA) carries specific amino acids to the ribosome during translation, matching anticodons with codons on mRNA to build proteins in the correct sequence."
                },
                {
                    "question": "In the Calvin cycle, what molecule is used to fix carbon dioxide?",
                    "options": ["Glucose", "RuBP", "ATP", "NADPH"],
                    "correct": 1,
                    "explanation": "RuBP (ribulose bisphosphate) is the carbon dioxide acceptor molecule in the Calvin cycle. CO₂ is fixed to RuBP by the enzyme RuBisCO to form 3-phosphoglycerate."
                },
                {
                    "question": "What is the main difference between prokaryotic and eukaryotic gene expression?",
                    "options": ["Prokaryotes don't have genes", "Eukaryotes process mRNA", "Prokaryotes use different codons", "Eukaryotes don't use ribosomes"],
                    "correct": 1,
                    "explanation": "Eukaryotic mRNA undergoes processing (5' capping, 3' polyadenylation, splicing to remove introns) before translation, while prokaryotic mRNA is translated directly."
                },
                {
                    "question": "Which stage of cellular respiration produces the most ATP?",
                    "options": ["Glycolysis", "Pyruvate oxidation", "Krebs cycle", "Electron transport chain"],
                    "correct": 3,
                    "explanation": "The electron transport chain produces the most ATP (about 26-28 molecules) through oxidative phosphorylation, using energy from NADH and FADH₂ to pump protons and drive ATP synthesis."
                },
                {
                    "question": "What type of selection favors extreme phenotypes?",
                    "options": ["Directional selection", "Stabilizing selection", "Disruptive selection", "Sexual selection"],
                    "correct": 2,
                    "explanation": "Disruptive selection favors individuals at both extremes of a phenotypic range while selecting against intermediate phenotypes, potentially leading to speciation."
                }
            ]
        }
        
        # Virtual lab experiments with detailed procedures
        self.lab_experiments = {
            "microscopy": {
                "title": "Virtual Microscopy Lab",
                "description": "Explore different cell types and structures using virtual microscopy",
                "materials": ["Virtual microscope", "Prepared slides", "Observation sheets"],
                "procedure": [
                    "Select microscope objective lens (4x, 10x, 40x, 100x)",
                    "Choose specimen: onion skin, cheek cells, bacteria, or plant leaf",
                    "Adjust focus using coarse and fine adjustment knobs", 
                    "Observe and identify cellular structures",
                    "Draw detailed diagrams with labels",
                    "Record magnification and observations",
                    "Compare prokaryotic and eukaryotic cell features"
                ],
                "learning_objectives": [
                    "Understand proper microscope usage",
                    "Identify cellular organelles",
                    "Distinguish between cell types",
                    "Practice scientific observation skills"
                ]
            },
            "photosynthesis": {
                "title": "Photosynthesis Rate Investigation",
                "description": "Investigate factors affecting photosynthesis using aquatic plants",
                "materials": ["Aquatic plants", "Light source", "Thermometer", "pH indicator", "Timer"],
                "procedure": [
                    "Set up aquatic plant in clear container with water",
                    "Position light source at various distances (10cm, 20cm, 40cm)",
                    "Count oxygen bubbles produced in 5-minute intervals",
                    "Record temperature and light intensity",
                    "Test different variables: light color, CO₂ concentration, temperature",
                    "Graph results showing relationship between variables",
                    "Calculate photosynthesis rate (bubbles per minute)"
                ],
                "learning_objectives": [
                    "Understand photosynthesis equation",
                    "Identify limiting factors",
                    "Practice experimental design",
                    "Analyze quantitative data"
                ]
            },
            "dna_extraction": {
                "title": "DNA Extraction from Fruit",
                "description": "Extract visible DNA strands using household materials",
                "materials": ["Strawberries", "Salt", "Dish soap", "Cold ethanol", "Coffee filter", "Test tubes"],
                "procedure": [
                    "Mash 2-3 strawberries in a plastic bag",
                    "Mix with salt solution (1 tsp salt in 100ml water)",
                    "Add 2 tablespoons dish soap and mix gently",
                    "Filter mixture through coffee filter into test tube",
                    "Slowly pour cold ethanol down the side of the tube",
                    "Observe white DNA strands forming at the interface",
                    "Use toothpick to extract DNA for closer examination"
                ],
                "learning_objectives": [
                    "Understand DNA structure and properties",
                    "Learn extraction techniques",
                    "Observe macromolecules",
                    "Connect molecular biology to everyday life"
                ]
            },
            "enzyme_activity": {
                "title": "Enzyme Activity Investigation",
                "description": "Study how temperature and pH affect enzyme function",
                "materials": ["Catalase enzyme", "Hydrogen peroxide", "pH buffers", "Thermometer", "Measuring cylinders"],
                "procedure": [
                    "Prepare enzyme solutions at different pH values (5, 7, 9)",
                    "Test enzyme activity at various temperatures (0°C, 20°C, 37°C, 60°C)",
                    "Add hydrogen peroxide to enzyme solutions",
                    "Measure oxygen production rate (bubble formation)",
                    "Record time for reaction completion",
                    "Graph results showing enzyme activity vs temperature/pH",
                    "Identify optimal conditions for enzyme function"
                ],
                "learning_objectives": [
                    "Understand enzyme structure and function",
                    "Explore protein denaturation",
                    "Analyze enzyme kinetics",
                    "Apply scientific method"
                ]
            },
            "genetics_simulation": {
                "title": "Genetics and Inheritance Simulation",
                "description": "Use Punnett squares to predict inheritance patterns",
                "materials": ["Genetic trait cards", "Punnett square worksheets", "Probability calculators"],
                "procedure": [
                    "Choose parental genotypes for specific traits (eye color, height, etc.)",
                    "Set up Punnett square grid",
                    "Fill in all possible gamete combinations",
                    "Calculate phenotypic and genotypic ratios",
                    "Predict offspring characteristics",
                    "Compare predictions with simulated results",
                    "Explore complex inheritance patterns (incomplete dominance, codominance)"
                ],
                "learning_objectives": [
                    "Apply Mendel's laws of inheritance",
                    "Use Punnett squares effectively", 
                    "Calculate genetic probabilities",
                    "Understand genotype vs phenotype"
                ]
            }
        }
        
        # Interactive cell diagrams data
        self.cell_components = {
            "animal_cell": {
                "organelles": [
                    {"name": "Nucleus", "function": "Controls cell activities and contains DNA", "color": ft.Colors.BLUE_400},
                    {"name": "Mitochondria", "function": "Produces ATP energy through cellular respiration", "color": ft.Colors.RED_400},
                    {"name": "Ribosomes", "function": "Synthesizes proteins using mRNA instructions", "color": ft.Colors.PURPLE_400},
                    {"name": "Endoplasmic Reticulum", "function": "Transports materials throughout the cell", "color": ft.Colors.GREEN_400},
                    {"name": "Golgi Apparatus", "function": "Modifies and packages proteins from ER", "color": ft.Colors.ORANGE_400},
                    {"name": "Lysosomes", "function": "Digests waste materials and worn-out organelles", "color": ft.Colors.YELLOW_400},
                    {"name": "Cell Membrane", "function": "Controls what enters and exits the cell", "color": ft.Colors.BROWN_400}
                ]
            },
            "plant_cell": {
                "organelles": [
                    {"name": "Nucleus", "function": "Controls cell activities and contains DNA", "color": ft.Colors.BLUE_400},
                    {"name": "Chloroplasts", "function": "Conducts photosynthesis to make glucose", "color": ft.Colors.GREEN_600},
                    {"name": "Cell Wall", "function": "Provides structural support and protection", "color": ft.Colors.BROWN_600},
                    {"name": "Large Vacuole", "function": "Stores water and maintains turgor pressure", "color": ft.Colors.CYAN_400},
                    {"name": "Mitochondria", "function": "Produces ATP energy through cellular respiration", "color": ft.Colors.RED_400},
                    {"name": "Ribosomes", "function": "Synthesizes proteins using mRNA instructions", "color": ft.Colors.PURPLE_400},
                    {"name": "Cell Membrane", "function": "Controls what enters and exits the cell", "color": ft.Colors.PINK_400}
                ]
            }
        }

    def create_main_view(self):
        return ft.Container(
            ft.Column([
                ft.Text("🌱 Biology Laboratory", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Discover life sciences, from molecules to ecosystems", size=16, color=ft.Colors.TEAL_700, text_align=ft.TextAlign.CENTER),
                ft.Divider(height=30),
                
                # Enhanced navigation buttons
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.HELP, size=30, color=ft.Colors.BLUE_700),
                                ft.Text("AI Tutor", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_ai_help(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.BLUE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.BIOTECH, size=30, color=ft.Colors.GREEN_700),
                                ft.Text("Virtual Lab", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_virtual_lab(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCIENCE, size=30, color=ft.Colors.ORANGE_700),
                                ft.Text("Cell Explorer", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_cell_explorer(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCIENCE, size=30, color=ft.Colors.PURPLE_700),
                                ft.Text("Genetics", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_genetics_tools(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PURPLE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.ResponsiveRow([
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.QUIZ_OUTLINED, size=30, color=ft.Colors.INDIGO_700),
                                ft.Text("Bio Quiz", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_quizzes(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.INDIGO_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.ECO, size=30, color=ft.Colors.LIGHT_GREEN_700),
                                ft.Text("Ecosystems", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_ecosystem_explorer(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.LIGHT_GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.ACCESSIBILITY, size=30, color=ft.Colors.PINK_700),
                                ft.Text("Human Body", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_human_body_systems(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.PINK_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Column([
                                ft.Icon(ft.Icons.TIMELINE, size=30, color=ft.Colors.DEEP_ORANGE_700),
                                ft.Text("Evolution", size=14, weight=ft.FontWeight.BOLD)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            on_click=lambda e: self.show_evolution_timeline(),
                            style=ft.ButtonStyle(padding=15, bgcolor=ft.Colors.DEEP_ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                        ),
                        col={'xs': 12, 'sm': 6, 'md': 3}
                    ),
                ], spacing=10, run_spacing=10),
                
                ft.Divider(height=20),
                
                # Enhanced overview with learning pathways
                ft.Container(
                    ft.Column([
                        ft.Text("🔬 Biology Learning Pathways", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_800),
                        ft.Text("Explore life from molecular mechanisms to global ecosystems through interactive experiences.", size=14),
                        ft.Text("🧬 Core Areas:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                        ft.Column([
                            ft.Text("• Molecular Biology: DNA, proteins, and cellular processes", size=14),
                            ft.Text("• Cell Biology: Structure, function, and division", size=14),
                            ft.Text("• Genetics: Heredity, variation, and evolution", size=14),
                            ft.Text("• Ecology: Interactions and environmental science", size=14),
                            ft.Text("• Physiology: How living systems function", size=14),
                            ft.Text("• Evolution: Change over time and biodiversity", size=14),
                        ], spacing=5),
                        ft.Text("🎯 Learning Features:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700),
                        ft.Text("Interactive virtual labs, cellular simulations, genetic calculators, ecosystem models, and comprehensive assessments", size=14, style=ft.TextStyle(italic=True))
                    ], spacing=10),
                    bgcolor=ft.Colors.TEAL_50,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.TEAL_200)
                )
            ], spacing=20),
            padding=20,
            expand=True
        )

    def show_ai_help(self):
        self.page.views.clear()
        
        query_field = ft.TextField(
            label="Ask about biology concepts...",
            hint_text="e.g., How does DNA replication work? or What is natural selection?",
            multiline=True,
            min_lines=3,
            expand=True
        )
        
        response_text = ft.Text("", size=14, selectable=True)
        
        def handle_query(e):
            if query_field.value:
                response = get_ai_help(query_field.value)
                response_text.value = response
                self.page.update()
        
        # Quick question buttons for common topics
        quick_questions = [
            "Explain photosynthesis process",
            "How do cells divide?",
            "What is natural selection?", 
            "Describe DNA structure",
            "How do enzymes work?",
            "What are the stages of mitosis?",
            "Explain cellular respiration",
            "How does inheritance work?"
        ]
        
        def ask_quick_question(question):
            query_field.value = question
            handle_query(None)
        
        view = ft.View(
            "/biology/ai_help",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Biology AI Tutor"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🔬 Biology AI Tutor", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Get detailed explanations for any biology concept", size=16, color=ft.Colors.TEAL_700),
                        query_field,
                        ft.ElevatedButton(
                            "Get Explanation",
                            on_click=handle_query,
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
                        ),
                        ft.Container(response_text, bgcolor=ft.Colors.GREY_100, border_radius=10, padding=15, expand=True),
                        ft.Text("⚡ Quick Questions:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Wrap([
                            ft.ElevatedButton(
                                question,
                                on_click=lambda e, q=question: ask_quick_question(q),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_100)
                            ) for question in quick_questions
                        ], spacing=10, run_spacing=10)
                    ], spacing=15),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_ecosystem_explorer(self):
        self.page.views.clear()
        
        # Ecosystem types with characteristics
        ecosystems = {
            "Forest": {
                "description": "Complex terrestrial ecosystem with multiple layers",
                "producers": ["Trees", "Shrubs", "Ferns", "Mosses"],
                "primary_consumers": ["Deer", "Rabbits", "Squirrels", "Insects"],
                "secondary_consumers": ["Foxes", "Hawks", "Owls", "Snakes"],
                "tertiary_consumers": ["Bears", "Wolves", "Large birds of prey"],
                "decomposers": ["Bacteria", "Fungi", "Earthworms", "Beetles"],
                "abiotic_factors": ["Sunlight", "Rainfall", "Temperature", "Soil nutrients"]
            },
            "Ocean": {
                "description": "Largest aquatic ecosystem covering 71% of Earth",
                "producers": ["Phytoplankton", "Kelp", "Seaweed", "Marine algae"],
                "primary_consumers": ["Zooplankton", "Small fish", "Krill", "Sea urchins"],
                "secondary_consumers": ["Larger fish", "Squid", "Sea turtles", "Seals"],
                "tertiary_consumers": ["Sharks", "Whales", "Large predatory fish"],
                "decomposers": ["Marine bacteria", "Deep-sea organisms"],
                "abiotic_factors": ["Salinity", "Water pressure", "Temperature", "Ocean currents"]
            },
            "Desert": {
                "description": "Arid ecosystem with specialized drought-adapted organisms",
                "producers": ["Cacti", "Succulents", "Desert grasses", "Shrubs"],
                "primary_consumers": ["Insects", "Small rodents", "Desert rabbits"],
                "secondary_consumers": ["Lizards", "Snakes", "Desert foxes", "Hawks"],
                "tertiary_consumers": ["Coyotes", "Large birds of prey"],
                "decomposers": ["Desert bacteria", "Fungi", "Scavenger insects"],
                "abiotic_factors": ["Low rainfall", "Extreme temperatures", "Sandy soil", "Intense sunlight"]
            }
        }
        
        selected_ecosystem = ft.Dropdown(
            label="Select Ecosystem",
            options=[ft.dropdown.Option(key) for key in ecosystems.keys()],
            value="Forest",
            on_change=lambda e: update_ecosystem_display()
        )
        
        ecosystem_display = ft.Container()
        
        def update_ecosystem_display():
            ecosystem_name = selected_ecosystem.value
            ecosystem_data = ecosystems[ecosystem_name]
            
            # Create food web visualization
            level_displays = []
            levels = [
                ("Tertiary Consumers", ecosystem_data["tertiary_consumers"], ft.Colors.RED_400),
                ("Secondary Consumers", ecosystem_data["secondary_consumers"], ft.Colors.ORANGE_400),
                ("Primary Consumers", ecosystem_data["primary_consumers"], ft.Colors.YELLOW_400),
                ("Producers", ecosystem_data["producers"], ft.Colors.GREEN_400),
                ("Decomposers", ecosystem_data["decomposers"], ft.Colors.BROWN_400)
            ]
            
            for level_name, organisms, color in levels:
                organism_chips = []
                for organism in organisms[:4]:  # Limit display
                    organism_chips.append(
                        ft.Container(
                            ft.Text(organism, size=12, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                            bgcolor=color,
                            border_radius=15,
                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                            margin=2
                        )
                    )
                
                level_displays.append(
                    ft.Container(
                        ft.Column([
                            ft.Text(level_name, size=14, weight=ft.FontWeight.BOLD),
                            ft.Wrap(organism_chips, spacing=5, run_spacing=5)
                        ], spacing=8),
                        bgcolor=ft.Colors.WHITE,
                        border_radius=8,
                        padding=10,
                        border=ft.border.all(1, color),
                        margin=ft.margin.only(bottom=10)
                    )
                )
            
            ecosystem_display.content = ft.Column([
                ft.Text(f"{ecosystem_name} Ecosystem", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.LIGHT_GREEN_900),
                ft.Text(ecosystem_data["description"], size=14, color=ft.Colors.LIGHT_GREEN_700),
                ft.Text("Food Web Structure:", size=16, weight=ft.FontWeight.BOLD),
                ft.Column(level_displays, spacing=0),
                ft.Container(
                    ft.Column([
                        ft.Text("Key Abiotic Factors:", size=14, weight=ft.FontWeight.BOLD),
                        ft.Wrap([
                            ft.Container(
                                ft.Text(factor, size=12),
                                bgcolor=ft.Colors.BLUE_100,
                                border_radius=10,
                                padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                margin=2
                            ) for factor in ecosystem_data["abiotic_factors"]
                        ], spacing=5, run_spacing=5)
                    ], spacing=8),
                    bgcolor=ft.Colors.BLUE_50,
                    border_radius=8,
                    padding=15
                )
            ], spacing=15)
            self.page.update()
        
        view = ft.View(
            "/biology/ecosystem_explorer",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Ecosystem Explorer"),
                    bgcolor=ft.Colors.LIGHT_GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🌍 Ecosystem Explorer", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.LIGHT_GREEN_900),
                        ft.Text("Explore different ecosystems and their food webs", size=16, color=ft.Colors.LIGHT_GREEN_700),
                        
                        selected_ecosystem,
                        ecosystem_display,
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🔗 Ecosystem Principles:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Energy flows in one direction (sun → producers → consumers)", size=14),
                                ft.Text("• Nutrients cycle through the ecosystem (decomposition)", size=14),
                                ft.Text("• Each species has a specific niche (role and habitat)", size=14),
                                ft.Text("• Biodiversity increases ecosystem stability", size=14),
                                ft.Text("• Human activities can disrupt ecosystem balance", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(top=20)
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🤔 Critical Thinking Questions:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• What happens if a keystone species is removed?", size=14),
                                ft.Text("• How do human activities affect food webs?", size=14),
                                ft.Text("• Why are decomposers essential to ecosystems?", size=14),
                                ft.Text("• How does climate change impact different ecosystems?", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.ORANGE_300)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        # Initialize display
        update_ecosystem_display()
        
        self.page.views.append(view)
        self.page.update()

    def show_human_body_systems(self):
        self.page.views.clear()
        
        body_systems = {
            "Circulatory": {
                "function": "Transports blood, nutrients, oxygen, and waste throughout the body",
                "organs": ["Heart", "Blood vessels", "Blood"],
                "key_processes": ["Blood circulation", "Oxygen transport", "Waste removal"],
                "disorders": ["Heart disease", "High blood pressure", "Anemia"],
                "color": ft.Colors.RED_400
            },
            "Respiratory": {
                "function": "Exchanges oxygen and carbon dioxide between body and environment",
                "organs": ["Lungs", "Trachea", "Bronchi", "Diaphragm"],
                "key_processes": ["Breathing", "Gas exchange", "Oxygen transport"],
                "disorders": ["Asthma", "Pneumonia", "Lung cancer"],
                "color": ft.Colors.BLUE_400
            },
            "Digestive": {
                "function": "Breaks down food and absorbs nutrients for energy and growth",
                "organs": ["Stomach", "Intestines", "Liver", "Pancreas"],
                "key_processes": ["Digestion", "Absorption", "Waste elimination"],
                "disorders": ["Ulcers", "IBS", "Food poisoning"],
                "color": ft.Colors.ORANGE_400
            },
            "Nervous": {
                "function": "Controls and coordinates body activities through electrical signals",
                "organs": ["Brain", "Spinal cord", "Nerves"],
                "key_processes": ["Signal transmission", "Reflexes", "Thinking"],
                "disorders": ["Stroke", "Alzheimer's", "Epilepsy"],
                "color": ft.Colors.PURPLE_400
            },
            "Musculoskeletal": {
                "function": "Provides structure, protection, and enables movement",
                "organs": ["Bones", "Muscles", "Joints", "Tendons"],
                "key_processes": ["Movement", "Support", "Protection"],
                "disorders": ["Fractures", "Arthritis", "Muscle strains"],
                "color": ft.Colors.BROWN_400
            },
            "Excretory": {
                "function": "Removes waste products and maintains water balance",
                "organs": ["Kidneys", "Bladder", "Ureters", "Urethra"],
                "key_processes": ["Filtration", "Waste removal", "Water balance"],
                "disorders": ["Kidney stones", "UTIs", "Kidney disease"],
                "color": ft.Colors.YELLOW_700
            }
        }
        
        system_cards = []
        for system_name, system_data in body_systems.items():
            organs_text = ", ".join(system_data["organs"])
            processes_widgets = [ft.Text(f"• {process}", size=12) for process in system_data["key_processes"]]
            disorders_widgets = [ft.Text(f"• {disorder}", size=12, color=ft.Colors.RED_600) for disorder in system_data["disorders"]]
            
            card = ft.Container(
                ft.Column([
                    ft.Row([
                        ft.Container(
                            width=20,
                            height=20,
                            bgcolor=system_data["color"],
                            border_radius=10
                        ),
                        ft.Text(f"{system_name} System", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900)
                    ], spacing=10),
                    ft.Text(system_data["function"], size=14),
                    ft.Text(f"Key Organs: {organs_text}", size=13, weight=ft.FontWeight.W_500),
                    
                    ft.ExpansionTile(
                        title=ft.Text("Key Processes", size=14, weight=ft.FontWeight.BOLD),
                        controls=[
                            ft.Container(
                                ft.Column(processes_widgets, spacing=3),
                                padding=10,
                                bgcolor=ft.Colors.GREEN_50
                            )
                        ]
                    ),
                    
                    ft.ExpansionTile(
                        title=ft.Text("Common Disorders", size=14, weight=ft.FontWeight.BOLD),
                        controls=[
                            ft.Container(
                                ft.Column(disorders_widgets, spacing=3),
                                padding=10,
                                bgcolor=ft.Colors.RED_50
                            )
                        ]
                    )
                ], spacing=10),
                bgcolor=ft.Colors.PINK_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, system_data["color"]),
                margin=ft.margin.only(bottom=15)
            )
            system_cards.append(card)
        
        view = ft.View(
            "/biology/human_body_systems",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Human Body Systems"),
                    bgcolor=ft.Colors.PINK_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🫁 Human Body Systems", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                        ft.Text("Explore how organ systems work together to maintain life", size=16, color=ft.Colors.PINK_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("System Integration:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• All systems work together to maintain homeostasis", size=14),
                                ft.Text("• Circulatory system connects and supports all other systems", size=14),
                                ft.Text("• Nervous system coordinates and controls other systems", size=14),
                                ft.Text("• Disruption in one system affects others", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Column(system_cards, spacing=0),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Health Connection Activity:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("Think about daily activities and which systems are involved:", size=14),
                                ft.Text("• Running: Musculoskeletal, Respiratory, Circulatory", size=13),
                                ft.Text("• Eating: Digestive, Nervous, Circulatory", size=13),
                                ft.Text("• Studying: Nervous, Circulatory, Respiratory", size=13),
                                ft.Text("How can you keep these systems healthy?", size=13, style=ft.TextStyle(italic=True))
                            ], spacing=8),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.GREEN_400)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_evolution_timeline(self):
        self.page.views.clear()
        
        evolution_events = [
            {
                "time": "4.6 billion years ago",
                "event": "Earth Formation",
                "description": "Earth forms from cosmic dust and debris",
                "significance": "Provides the foundation for life to eventually emerge"
            },
            {
                "time": "3.8 billion years ago", 
                "event": "First Life",
                "description": "Simple prokaryotic cells (bacteria) appear",
                "significance": "Beginning of biological evolution on Earth"
            },
            {
                "time": "2.1 billion years ago",
                "event": "Eukaryotic Cells",
                "description": "Complex cells with nuclei and organelles evolve",
                "significance": "Enabled evolution of multicellular organisms"
            },
            {
                "time": "540 million years ago",
                "event": "Cambrian Explosion",
                "description": "Rapid diversification of complex life forms",
                "significance": "Most major animal groups first appear in fossil record"
            },
            {
                "time": "365 million years ago",
                "event": "Land Colonization",
                "description": "Plants and animals move from water to land",
                "significance": "Opened vast new habitats for evolution"
            },
            {
                "time": "230 million years ago",
                "event": "Age of Dinosaurs",
                "description": "Dinosaurs dominate terrestrial ecosystems",
                "significance": "Demonstrates adaptive radiation and extinction"
            },
            {
                "time": "65 million years ago",
                "event": "Mass Extinction",
                "description": "Asteroid impact kills dinosaurs",
                "significance": "Cleared niches for mammalian evolution"
            },
            {
                "time": "7 million years ago",
                "event": "Human Lineage",
                "description": "Human ancestors diverge from other apes",
                "significance": "Beginning of human evolutionary history"
            },
            {
                "time": "200,000 years ago",
                "event": "Modern Humans",
                "description": "Homo sapiens appears in Africa",
                "significance": "Our species begins to spread across the globe"
            }
        ]
        
        timeline_cards = []
        for i, event in enumerate(evolution_events):
            card = ft.Container(
                ft.Row([
                    ft.Container(
                        ft.Text(str(i+1), size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.DEEP_ORANGE_600,
                        width=40,
                        height=40,
                        border_radius=20,
                        alignment=ft.alignment.center
                    ),
                    ft.Expanded(
                        ft.Column([
                            ft.Row([
                                ft.Text(event["event"], size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.DEEP_ORANGE_900),
                                ft.Container(
                                    ft.Text(event["time"], size=12, color=ft.Colors.WHITE),
                                    bgcolor=ft.Colors.DEEP_ORANGE_400,
                                    border_radius=10,
                                    padding=ft.padding.symmetric(horizontal=8, vertical=4)
                                )
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                            ft.Text(event["description"], size=14),
                            ft.Text(f"Significance: {event['significance']}", size=13, 
                                   color=ft.Colors.DEEP_ORANGE_700, style=ft.TextStyle(italic=True))
                        ], spacing=5)
                    )
                ], spacing=15),
                bgcolor=ft.Colors.DEEP_ORANGE_50,
                border_radius=10,
                padding=15,
                border=ft.border.all(1, ft.Colors.DEEP_ORANGE_200),
                margin=ft.margin.only(bottom=10)
            )
            timeline_cards.append(card)
        
        view = ft.View(
            "/biology/evolution_timeline",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Evolution Timeline"),
                    bgcolor=ft.Colors.DEEP_ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🦕 Evolution Timeline", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.DEEP_ORANGE_900),
                        ft.Text("Journey through 4.6 billion years of life on Earth", size=16, color=ft.Colors.DEEP_ORANGE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Evolution Mechanisms:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Natural Selection: Survival of the fittest individuals", size=14),
                                ft.Text("• Genetic Drift: Random changes in allele frequencies", size=14),
                                ft.Text("• Gene Flow: Movement of alleles between populations", size=14),
                                ft.Text("• Mutation: Source of genetic variation", size=14),
                                ft.Text("• Sexual Selection: Traits that aid in reproduction", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Text("📅 Major Events in Evolution:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.DEEP_ORANGE_900),
                        ft.Column(timeline_cards, spacing=0),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🧬 Evidence for Evolution:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Fossil Record: Shows progression of life forms over time", size=14),
                                ft.Text("• Comparative Anatomy: Similar structures in related species", size=14),
                                ft.Text("• Molecular Biology: DNA and protein similarities", size=14),
                                ft.Text("• Biogeography: Distribution patterns match evolutionary history", size=14),
                                ft.Text("• Direct Observation: Evolution happening in real-time", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(top=20)
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🔬 Modern Evolution Research:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("Scientists continue to study evolution through:", size=14),
                                ft.Text("• Genetic sequencing of ancient DNA", size=13),
                                ft.Text("• Observing rapid evolution in bacteria and viruses", size=13),
                                ft.Text("• Computer modeling of evolutionary processes", size=13),
                                ft.Text("• Studying adaptation to climate change", size=13)
                            ], spacing=8),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.PURPLE_300)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_quizzes(self):
        self.page.views.clear()
        
        view = ft.View(
            "/biology/quizzes",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Biology Assessment Center"),
                    bgcolor=ft.Colors.INDIGO_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧪 Biology Assessment Center", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.INDIGO_900),
                        ft.Text("Test your knowledge across all areas of biology", size=16, color=ft.Colors.INDIGO_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("📊 Assessment Levels:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Basic: Fundamental concepts and terminology", size=14),
                                ft.Text("• Intermediate: Process understanding and applications", size=14),
                                ft.Text("• Advanced: Complex mechanisms and analysis", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_ONE, size=30, color=ft.Colors.GREEN_700),
                                        ft.Text("Basic Level", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Cells, DNA, basic processes", size=12, text_align=ft.TextAlign.CENTER),
                                        ft.Text("5 Questions", size=10, color=ft.Colors.GREY_600)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("basic"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.GREEN_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_TWO, size=30, color=ft.Colors.ORANGE_700),
                                        ft.Text("Intermediate", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Genetics, ecology, systems", size=12, text_align=ft.TextAlign.CENTER),
                                        ft.Text("5 Questions", size=10, color=ft.Colors.GREY_600)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("intermediate"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.ORANGE_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.LOOKS_3, size=30, color=ft.Colors.RED_700),
                                        ft.Text("Advanced", size=16, weight=ft.FontWeight.BOLD),
                                        ft.Text("Molecular biology, evolution", size=12, text_align=ft.TextAlign.CENTER),
                                        ft.Text("5 Questions", size=10, color=ft.Colors.GREY_600)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                                    on_click=lambda e: self.start_quiz("advanced"),
                                    style=ft.ButtonStyle(padding=20, bgcolor=ft.Colors.RED_50, shape=ft.RoundedRectangleBorder(radius=10))
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=15, run_spacing=15),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Topics Covered:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Cell structure and function", size=14),
                                ft.Text("• DNA, genetics, and inheritance", size=14),
                                ft.Text("• Evolution and natural selection", size=14),
                                ft.Text("• Ecosystems and environmental biology", size=14),
                                ft.Text("• Human anatomy and physiology", size=14),
                                ft.Text("• Molecular processes and biochemistry", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(top=20)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_quiz(self, level):
        self.current_quiz_level = level
        self.quiz_score = 0
        self.quiz_question_index = 0
        self.show_quiz_question()

    def show_quiz_question(self):
        questions = self.quiz_questions[self.current_quiz_level]
        if self.quiz_question_index >= len(questions):
            self.show_quiz_results()
            return
        
        question = questions[self.quiz_question_index]
        
        option_buttons = []
        for i, option in enumerate(question["options"]):
            option_buttons.append(
                ft.ElevatedButton(
                    option,
                    on_click=lambda e, idx=i: self.answer_question(idx),
                    style=ft.ButtonStyle(
                        padding=15,
                        bgcolor=ft.Colors.TEAL_50,
                        shape=ft.RoundedRectangleBorder(radius=8)
                    ),
                    expand=True
                )
            )
        
        self.page.views.clear()
        view = ft.View(
            "/biology/quiz_question",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_quizzes()),
                    title=ft.Text(f"Question {self.quiz_question_index + 1}"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Row([
                            ft.Text(f"Question {self.quiz_question_index + 1} of {len(questions)}", size=16, color=ft.Colors.GREY_600),
                            ft.Container(
                                ft.Text(f"Level: {self.current_quiz_level.title()}", size=14, color=ft.Colors.TEAL_700),
                                bgcolor=ft.Colors.TEAL_50,
                                border_radius=5,
                                padding=ft.padding.symmetric(horizontal=8, vertical=4)
                            ),
                            ft.Container(
                                ft.Text(f"Score: {self.quiz_score}/{self.quiz_question_index}", size=14, color=ft.Colors.BLUE_700),
                                bgcolor=ft.Colors.BLUE_50,
                                border_radius=5,
                                padding=ft.padding.symmetric(horizontal=8, vertical=4)
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(question["question"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Select the best answer:", size=14, color=ft.Colors.GREY_700),
                        ft.Column(option_buttons, spacing=10)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def answer_question(self, selected_index):
        questions = self.quiz_questions[self.current_quiz_level]
        question = questions[self.quiz_question_index]
        
        is_correct = selected_index == question["correct"]
        if is_correct:
            self.quiz_score += 1
        
        # Show detailed explanation
        self.page.views.clear()
        view = ft.View(
            "/biology/quiz_explanation",
            [
                ft.AppBar(
                    title=ft.Text("Answer Analysis"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Icon(
                            ft.Icons.CHECK_CIRCLE if is_correct else ft.Icons.CANCEL,
                            size=60,
                            color=ft.Colors.GREEN if is_correct else ft.Colors.RED
                        ),
                        ft.Text(
                            "Excellent!" if is_correct else "Not quite right",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.GREEN if is_correct else ft.Colors.RED
                        ),
                        ft.Container(
                            ft.Column([
                                ft.Text("Correct Answer:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                                ft.Text(question['options'][question['correct']], size=16, color=ft.Colors.TEAL_700),
                                ft.Divider(),
                                ft.Text("Explanation:", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                ft.Text(question["explanation"], size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.TEAL_50,
                            border_radius=10,
                            padding=15
                        ),
                        ft.ElevatedButton(
                            "Continue" if self.quiz_question_index + 1 < len(questions) else "View Results",
                            on_click=lambda e: self.next_question(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
                        )
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def next_question(self):
        self.quiz_question_index += 1
        self.show_quiz_question()

    def show_quiz_results(self):
        total_questions = len(self.quiz_questions[self.current_quiz_level])
        percentage = (self.quiz_score / total_questions) * 100
        
        if percentage >= 90:
            message = "Outstanding biological knowledge!"
            color = ft.Colors.GREEN
            emoji = "🏆"
        elif percentage >= 75:
            message = "Strong understanding of biology!"
            color = ft.Colors.BLUE
            emoji = "⭐"
        elif percentage >= 60:
            message = "Good grasp of key concepts!"
            color = ft.Colors.ORANGE
            emoji = "👍"
        else:
            message = "Keep studying and exploring!"
            color = ft.Colors.PURPLE
            emoji = "📚"
        
        self.page.views.clear()
        view = ft.View(
            "/biology/quiz_results",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Assessment Results"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text(f"{emoji} Biology Assessment Complete!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Container(
                            ft.Column([
                                ft.Text(f"Your Score", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text(f"{self.quiz_score}/{total_questions}", size=36, weight=ft.FontWeight.BOLD, color=color),
                                ft.Text(f"{percentage:.0f}%", size=20, color=color),
                                ft.Text(f"Level: {self.current_quiz_level.title()}", size=14, color=ft.Colors.GREY_600)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            bgcolor=ft.Colors.WHITE,
                            border_radius=15,
                            padding=20,
                            border=ft.border.all(3, color)
                        ),
                        ft.Text(message, size=18, color=color, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Row([
                            ft.ElevatedButton(
                                "Try Again",
                                on_click=lambda e: self.start_quiz(self.current_quiz_level),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.TEAL_600, color=ft.Colors.WHITE)
                            ),
                            ft.ElevatedButton(
                                "Different Level",
                                on_click=lambda e: self.show_quizzes()
                            ),
                            ft.ElevatedButton(
                                "Explore Labs",
                                on_click=lambda e: self.show_virtual_lab(),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                            ),
                            ft.ElevatedButton(
                                "Back to Biology",
                                on_click=lambda e: self.page.go("/biology")
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10, wrap=True)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

def biology_page(page: ft.Page):
    page.title = "Biology - Student AI Assistance"
    page.scroll = ft.ScrollMode.AUTO
    
    # Clear page content first
    page.clean()
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
        title=ft.Text("Biology Laboratory"),
        bgcolor=ft.Colors.TEAL_700,
        center_title=True
    )
    
    module = BiologyModule(page)
    page.add(module.create_main_view())

    def show_virtual_lab(self):
        self.page.views.clear()
        
        experiment_cards = []
        for exp_key, exp_data in self.lab_experiments.items():
            materials_text = ", ".join(exp_data["materials"])
            procedure_widgets = [ft.Text(f"{i+1}. {step}", size=13) for i, step in enumerate(exp_data["procedure"])]
            objectives_widgets = [ft.Text(f"• {obj}", size=12, color=ft.Colors.GREEN_700) for obj in exp_data["learning_objectives"]]
            
            card = ft.Container(
                ft.Column([
                    ft.Text(exp_data["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                    ft.Text(exp_data["description"], size=14, color=ft.Colors.GREEN_700),
                    
                    ft.ExpansionTile(
                        title=ft.Text("Materials & Equipment", size=14, weight=ft.FontWeight.BOLD),
                        controls=[
                            ft.Container(
                                ft.Text(materials_text, size=12),
                                padding=10,
                                bgcolor=ft.Colors.BLUE_50,
                                border_radius=5
                            )
                        ]
                    ),
                    
                    ft.ExpansionTile(
                        title=ft.Text("Experimental Procedure", size=14, weight=ft.FontWeight.BOLD),
                        controls=[
                            ft.Container(
                                ft.Column(procedure_widgets, spacing=5),
                                padding=10,
                                bgcolor=ft.Colors.GREEN_50,
                                border_radius=5
                            )
                        ]
                    ),
                    
                    ft.ExpansionTile(
                        title=ft.Text("Learning Objectives", size=14, weight=ft.FontWeight.BOLD),
                        controls=[
                            ft.Container(
                                ft.Column(objectives_widgets, spacing=3),
                                padding=10,
                                bgcolor=ft.Colors.ORANGE_50,
                                border_radius=5
                            )
                        ]
                    ),
                    
                    ft.ElevatedButton(
                        "Start Virtual Experiment",
                        on_click=lambda e, exp_id=exp_key: self.start_virtual_experiment(exp_id),
                        style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                    )
                ], spacing=10),
                bgcolor=ft.Colors.GREEN_50,
                border_radius=12,
                padding=20,
                border=ft.border.all(2, ft.Colors.GREEN_200),
                margin=ft.margin.only(bottom=15)
            )
            experiment_cards.append(card)
        
        view = ft.View(
            "/biology/virtual_lab",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Virtual Biology Laboratory"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧪 Virtual Biology Laboratory", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Conduct interactive experiments safely and repeatedly", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🔬 Laboratory Safety Reminder:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_800),
                                ft.Text("• Always read procedures carefully before starting", size=14),
                                ft.Text("• Record observations accurately and honestly", size=14),
                                ft.Text("• Analyze results using scientific reasoning", size=14),
                                ft.Text("• Consider sources of error and improvements", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.RED_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.RED_300),
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Column(experiment_cards, spacing=0)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def start_virtual_experiment(self, exp_id):
        exp_data = self.lab_experiments[exp_id]
        
        # Create experiment-specific interface
        if exp_id == "microscopy":
            self.show_microscopy_lab()
        elif exp_id == "photosynthesis":
            self.show_photosynthesis_lab()
        elif exp_id == "dna_extraction":
            self.show_dna_extraction_lab()
        elif exp_id == "enzyme_activity":
            self.show_enzyme_lab()
        elif exp_id == "genetics_simulation":
            self.show_genetics_lab()
        else:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"Interactive {exp_data['title']} simulation coming soon!"))
            )

    def show_microscopy_lab(self):
        self.page.views.clear()
        
        # Simulated microscope interface
        current_specimen = ft.Text("No specimen selected", size=16, weight=ft.FontWeight.BOLD)
        current_magnification = ft.Text("Magnification: 4x", size=14)
        observations_field = ft.TextField(
            label="Record your observations...",
            multiline=True,
            min_lines=4,
            max_lines=6
        )
        
        def change_specimen(specimen_name):
            current_specimen.value = f"Viewing: {specimen_name}"
            if specimen_name == "Onion Skin":
                observations_field.value = "Large rectangular cells with visible cell walls and nuclei. No chloroplasts visible."
            elif specimen_name == "Cheek Cells":
                observations_field.value = "Irregular oval cells with prominent nuclei. Cell membrane visible, no cell wall."
            elif specimen_name == "Bacteria":
                observations_field.value = "Very small, simple cellular structures. No visible nucleus or organelles."
            elif specimen_name == "Plant Leaf":
                observations_field.value = "Cells with cell walls, visible chloroplasts, and stomata (pores) for gas exchange."
            self.page.update()
        
        def change_magnification(mag):
            current_magnification.value = f"Magnification: {mag}"
            self.page.update()
        
        view = ft.View(
            "/biology/microscopy_lab",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_virtual_lab()),
                    title=ft.Text("Virtual Microscopy Lab"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🔬 Virtual Microscope", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        
                        ft.ResponsiveRow([
                            # Microscope controls
                            ft.Container(
                                ft.Column([
                                    ft.Text("Specimen Selection:", size=16, weight=ft.FontWeight.BOLD),
                                    ft.ElevatedButton("Onion Skin", on_click=lambda e: change_specimen("Onion Skin")),
                                    ft.ElevatedButton("Cheek Cells", on_click=lambda e: change_specimen("Cheek Cells")),
                                    ft.ElevatedButton("Bacteria", on_click=lambda e: change_specimen("Bacteria")),
                                    ft.ElevatedButton("Plant Leaf", on_click=lambda e: change_specimen("Plant Leaf")),
                                    
                                    ft.Text("Magnification:", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Row([
                                        ft.ElevatedButton("4x", on_click=lambda e: change_magnification("4x")),
                                        ft.ElevatedButton("10x", on_click=lambda e: change_magnification("10x")),
                                        ft.ElevatedButton("40x", on_click=lambda e: change_magnification("40x")),
                                        ft.ElevatedButton("100x", on_click=lambda e: change_magnification("100x"))
                                    ], wrap=True)
                                ], spacing=10),
                                col={'xs': 12, 'md': 4}
                            ),
                            
                            # Viewing area
                            ft.Container(
                                ft.Column([
                                    ft.Text("Microscope View:", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Container(
                                        ft.Column([
                                            current_specimen,
                                            current_magnification,
                                            ft.Container(
                                                ft.Text("Microscope viewing area\n(Simulated specimen view)", 
                                                        text_align=ft.TextAlign.CENTER, size=14),
                                                bgcolor=ft.Colors.BLACK12,
                                                width=300,
                                                height=200,
                                                border_radius=10,
                                                alignment=ft.alignment.center,
                                                border=ft.border.all(2, ft.Colors.GREEN_300)
                                            )
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                                        bgcolor=ft.Colors.GREEN_50,
                                        border_radius=10,
                                        padding=15
                                    )
                                ], spacing=10),
                                col={'xs': 12, 'md': 8}
                            )
                        ], spacing=20),
                        
                        ft.Text("📝 Laboratory Notes:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        observations_field,
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Analysis Questions:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("1. What differences do you observe between plant and animal cells?", size=14),
                                ft.Text("2. How does magnification affect your ability to see cellular details?", size=14),
                                ft.Text("3. Which type of cell appears more complex and why?", size=14),
                                ft.Text("4. What limitations does this virtual microscope have compared to a real one?", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.ElevatedButton(
                            "Complete Lab Report",
                            on_click=lambda e: self.page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Lab report saved! Great observations!"))
                            ),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_photosynthesis_lab(self):
        self.page.views.clear()
        
        # Experimental variables
        light_intensity = ft.Slider(
            min=0, max=100, value=50, label="Light Intensity (%)",
            on_change=lambda e: update_results()
        )
        temperature = ft.Slider(
            min=10, max=40, value=25, label="Temperature (°C)",
            on_change=lambda e: update_results()
        )
        co2_level = ft.Slider(
            min=200, max=1000, value=400, label="CO₂ (ppm)",
            on_change=lambda e: update_results()
        )
        
        results_text = ft.Text("Oxygen production rate: -- bubbles/min", size=16, weight=ft.FontWeight.BOLD)
        
        def update_results():
            # Simple simulation formula
            rate = (light_intensity.value * 0.1) + (temperature.value * 0.05) + (co2_level.value * 0.01)
            rate = max(0, min(rate, 15))  # Cap at reasonable values
            results_text.value = f"Oxygen production rate: {rate:.1f} bubbles/min"
            self.page.update()
        
        view = ft.View(
            "/biology/photosynthesis_lab",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_virtual_lab()),
                    title=ft.Text("Photosynthesis Investigation"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🌿 Photosynthesis Rate Investigation", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Investigate how environmental factors affect photosynthesis", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Photosynthesis Equation:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂", 
                                        size=14, font_family="monospace",
                                        text_align=ft.TextAlign.CENTER),
                                ft.Text("(We measure oxygen production as an indicator)", size=12, style=ft.TextStyle(italic=True))
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Text("🔧 Experimental Controls:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Light Intensity", size=14, weight=ft.FontWeight.BOLD),
                                light_intensity,
                                ft.Text("Temperature", size=14, weight=ft.FontWeight.BOLD),
                                temperature,
                                ft.Text("CO₂ Concentration", size=14, weight=ft.FontWeight.BOLD),
                                co2_level
                            ], spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("📊 Results:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                results_text,
                                ft.Text("(Based on oxygen bubble production rate)", size=12, style=ft.TextStyle(italic=True)),
                                ft.ElevatedButton(
                                    "Record Data Point",
                                    on_click=lambda e: self.page.show_snack_bar(
                                        ft.SnackBar(content=ft.Text("Data point recorded in lab notebook!"))
                                    ),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
                                )
                            ], spacing=10),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🤔 Think About It:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Which factor has the greatest effect on photosynthesis rate?", size=14),
                                ft.Text("• Why might too much heat slow down photosynthesis?", size=14),
                                ft.Text("• How do plants balance the need for CO₂ with water loss?", size=14),
                                ft.Text("• What happens to photosynthesis at night?", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.ElevatedButton(
                            "Generate Lab Report",
                            on_click=lambda e: self.page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Comprehensive lab report generated with all data points!"))
                            ),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_dna_extraction_lab(self):
        self.page.views.clear()
        
        # Lab progress steps
        steps_completed = []
        
        def complete_step(step_num, step_name):
            if step_num not in steps_completed:
                steps_completed.append(step_num)
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"Step {step_num} completed: {step_name}"))
            )
            self.page.update()
        
        view = ft.View(
            "/biology/dna_extraction_lab",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_virtual_lab()),
                    title=ft.Text("DNA Extraction Lab"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧬 DNA Extraction from Strawberries", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Extract and observe DNA using common household materials", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Why Strawberries?", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• Strawberries have 8 copies of each chromosome (octoploid)", size=14),
                                ft.Text("• Large amount of DNA per cell makes extraction easier", size=14),
                                ft.Text("• Soft tissue breaks down easily", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.RED_50,
                            border_radius=8,
                            padding=15,
                            border=ft.border.all(1, ft.Colors.RED_200),
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Text("🧪 Extraction Protocol:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        
                        # Step-by-step procedure with checkboxes
                        ft.Container(
                            ft.Column([
                                ft.Row([
                                    ft.Checkbox(on_change=lambda e: complete_step(1, "Mash strawberries")),
                                    ft.Text("1. Mash 2-3 strawberries in plastic bag", size=14, weight=ft.FontWeight.W_500)
                                ]),
                                ft.Text("This breaks down cell walls and releases cell contents", size=12, color=ft.Colors.GREY_600, style=ft.TextStyle(italic=True)),
                                
                                ft.Row([
                                    ft.Checkbox(on_change=lambda e: complete_step(2, "Add salt solution")),
                                    ft.Text("2. Add salt solution (1 tsp salt in 100ml water)", size=14, weight=ft.FontWeight.W_500)
                                ]),
                                ft.Text("Salt helps DNA precipitate and removes proteins", size=12, color=ft.Colors.GREY_600, style=ft.TextStyle(italic=True)),
                                
                                ft.Row([
                                    ft.Checkbox(on_change=lambda e: complete_step(3, "Add dish soap")),
                                    ft.Text("3. Add 2 tablespoons dish soap, mix gently", size=14, weight=ft.FontWeight.W_500)
                                ]),
                                ft.Text("Soap breaks down lipid membranes around cells and nuclei", size=12, color=ft.Colors.GREY_600, style=ft.TextStyle(italic=True)),
                                
                                ft.Row([
                                    ft.Checkbox(on_change=lambda e: complete_step(4, "Filter mixture")),
                                    ft.Text("4. Filter mixture through coffee filter into test tube", size=14, weight=ft.FontWeight.W_500)
                                ]),
                                ft.Text("Removes solid debris, leaving liquid with dissolved DNA", size=12, color=ft.Colors.GREY_600, style=ft.TextStyle(italic=True)),
                                
                                ft.Row([
                                    ft.Checkbox(on_change=lambda e: complete_step(5, "Add cold ethanol")),
                                    ft.Text("5. Slowly pour cold ethanol down side of tube", size=14, weight=ft.FontWeight.W_500)
                                ]),
                                ft.Text("DNA is not soluble in alcohol and will precipitate out", size=12, color=ft.Colors.GREY_600, style=ft.TextStyle(italic=True)),
                                
                                ft.Row([
                                    ft.Checkbox(on_change=lambda e: complete_step(6, "Observe DNA")),
                                    ft.Text("6. Observe white stringy DNA at the interface", size=14, weight=ft.FontWeight.W_500)
                                ]),
                                ft.Text("White strands are clumps of DNA molecules!", size=12, color=ft.Colors.GREY_600, style=ft.TextStyle(italic=True)),
                            ], spacing=8),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🔬 What You're Seeing:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("The white, stringy material is DNA! Each strand contains millions of nucleotides with the genetic instructions for strawberry characteristics like color, size, and sweetness.", size=14),
                                ft.Text("This same DNA extraction principle is used in:", size=14, weight=ft.FontWeight.W_500),
                                ft.Text("• Forensic investigations", size=13),
                                ft.Text("• Medical diagnosis", size=13),
                                ft.Text("• Genetic research", size=13),
                                ft.Text("• Biotechnology applications", size=13)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.ElevatedButton(
                            "Complete DNA Analysis",
                            on_click=lambda e: self.page.show_snack_bar(
                                ft.SnackBar(content=ft.Text(f"DNA extraction completed! {len(steps_completed)}/6 steps finished."))
                            ),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_enzyme_lab(self):
        self.page.views.clear()
        
        # Enzyme activity simulation
        ph_level = ft.Slider(min=1, max=14, value=7, label="pH Level")
        temp_level = ft.Slider(min=0, max=80, value=37, label="Temperature (°C)")
        
        activity_display = ft.Text("Enzyme Activity: 50%", size=16, weight=ft.FontWeight.BOLD)
        
        def calculate_activity():
            # Simulate catalase enzyme activity
            optimal_ph = 7
            optimal_temp = 37
            
            ph_factor = max(0, 100 - abs(ph_level.value - optimal_ph) * 20)
            temp_factor = max(0, 100 - abs(temp_level.value - optimal_temp) * 2)
            
            # Enzyme denatures at high temperatures
            if temp_level.value > 60:
                temp_factor = max(0, temp_factor - (temp_level.value - 60) * 10)
            
            activity = min(100, (ph_factor + temp_factor) / 2)
            activity_display.value = f"Enzyme Activity: {activity:.0f}%"
            self.page.update()
        
        ph_level.on_change = lambda e: calculate_activity()
        temp_level.on_change = lambda e: calculate_activity()
        
        view = ft.View(
            "/biology/enzyme_lab",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_virtual_lab()),
                    title=ft.Text("Enzyme Activity Lab"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧪 Enzyme Activity Investigation", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Study how pH and temperature affect catalase enzyme activity", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("About Catalase:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("Catalase breaks down hydrogen peroxide (H₂O₂) into water and oxygen:", size=14),
                                ft.Text("2H₂O₂ → 2H₂O + O₂", size=14, font_family="monospace", text_align=ft.TextAlign.CENTER),
                                ft.Text("This enzyme protects cells from damage by toxic peroxide", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Text("🔧 Experimental Variables:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("pH Level (1=very acidic, 7=neutral, 14=very basic)", size=14, weight=ft.FontWeight.BOLD),
                                ph_level,
                                ft.Text("Temperature (°C)", size=14, weight=ft.FontWeight.BOLD),
                                temp_level
                            ], spacing=10),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("📊 Results:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                                activity_display,
                                ft.Text("(Based on oxygen bubble production rate)", size=12, style=ft.TextStyle(italic=True)),
                                ft.ElevatedButton(
                                    "Record Data Point",
                                    on_click=lambda e: self.page.show_snack_bar(
                                        ft.SnackBar(content=ft.Text(f"Recorded: pH {ph_level.value:.1f}, {temp_level.value:.0f}°C, Activity {activity_display.value.split(': ')[1]}"))
                                    ),
                                    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
                                )
                            ], spacing=10),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🧠 Analysis Questions:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• What are the optimal conditions for catalase activity?", size=14),
                                ft.Text("• Why does extreme pH reduce enzyme activity?", size=14),
                                ft.Text("• What happens to enzymes at very high temperatures?", size=14),
                                ft.Text("• How do enzymes speed up chemical reactions?", size=14),
                                ft.Text("• Why are enzymes important for living organisms?", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Row([
                            ft.ElevatedButton(
                                "Reset to Optimal",
                                on_click=lambda e: [
                                    setattr(ph_level, 'value', 7),
                                    setattr(temp_level, 'value', 37),
                                    calculate_activity()
                                ],
                                style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
                            ),
                            ft.ElevatedButton(
                                "Generate Report",
                                on_click=lambda e: self.page.show_snack_bar(
                                    ft.SnackBar(content=ft.Text("Lab report generated with all enzyme activity data!"))
                                ),
                                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_genetics_lab(self):
        self.page.views.clear()
        
        # Punnett square calculator
        parent1_trait = ft.Dropdown(
            label="Parent 1 Genotype",
            options=[
                ft.dropdown.Option("TT", "TT (Tall - homozygous dominant)"),
                ft.dropdown.Option("Tt", "Tt (Tall - heterozygous)"),
                ft.dropdown.Option("tt", "tt (Short - homozygous recessive)")
            ],
            value="TT"
        )
        
        parent2_trait = ft.Dropdown(
            label="Parent 2 Genotype", 
            options=[
                ft.dropdown.Option("TT", "TT (Tall - homozygous dominant)"),
                ft.dropdown.Option("Tt", "Tt (Tall - heterozygous)"),
                ft.dropdown.Option("tt", "tt (Short - homozygous recessive)")
            ],
            value="tt"
        )
        
        results_display = ft.Container(
            ft.Text("Select parent genotypes to see Punnett square results", size=14),
            bgcolor=ft.Colors.GREY_100,
            border_radius=8,
            padding=15
        )
        
        def calculate_cross():
            p1 = parent1_trait.value
            p2 = parent2_trait.value
            
            # Generate all possible combinations
            gametes1 = [p1[0], p1[1]]
            gametes2 = [p2[0], p2[1]]
            
            offspring = []
            for g1 in gametes1:
                for g2 in gametes2:
                    offspring.append(''.join(sorted([g1, g2])))
            
            # Count phenotypes
            tall_count = sum(1 for o in offspring if 'T' in o)
            short_count = len(offspring) - tall_count
            
            # Create Punnett square display
            punnett_grid = ft.Column([
                ft.Text("Punnett Square Results:", size=16, weight=ft.FontWeight.BOLD),
                ft.Text(f"Cross: {p1} × {p2}", size=14),
                ft.Row([
                    ft.Text("", size=14, width=60),
                    ft.Container(ft.Text(gametes2[0], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.BLUE_100),
                    ft.Container(ft.Text(gametes2[1], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.BLUE_100)
                ]),
                ft.Row([
                    ft.Container(ft.Text(gametes1[0], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.BLUE_100),
                    ft.Container(ft.Text(offspring[0], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.GREEN_100),
                    ft.Container(ft.Text(offspring[1], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.GREEN_100)
                ]),
                ft.Row([
                    ft.Container(ft.Text(gametes1[1], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.BLUE_100),
                    ft.Container(ft.Text(offspring[2], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.GREEN_100),
                    ft.Container(ft.Text(offspring[3], size=14, text_align=ft.TextAlign.CENTER), width=60, bgcolor=ft.Colors.GREEN_100)
                ]),
                ft.Text(f"Genotype Ratio: {offspring}", size=14),
                ft.Text(f"Phenotype Ratio: {tall_count} Tall : {short_count} Short", size=14),
                ft.Text(f"Phenotype Percentages: {tall_count/4*100:.0f}% Tall, {short_count/4*100:.0f}% Short", size=14)
            ], spacing=10)
            
            results_display.content = punnett_grid
            self.page.update()
        
        parent1_trait.on_change = lambda e: calculate_cross()
        parent2_trait.on_change = lambda e: calculate_cross()
        
        view = ft.View(
            "/biology/genetics_lab",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_virtual_lab()),
                    title=ft.Text("Genetics Simulation"),
                    bgcolor=ft.Colors.GREEN_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧬 Genetics and Inheritance Simulator", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("Explore Mendel's laws using Punnett squares", size=16, color=ft.Colors.GREEN_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Mendel's Laws:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("1. Law of Segregation: Each parent contributes one allele for each trait", size=14),
                                ft.Text("2. Law of Dominance: Dominant alleles mask recessive alleles", size=14),
                                ft.Text("3. Law of Independent Assortment: Different traits are inherited independently", size=14)
                            ], spacing=5),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=8,
                            padding=15,
                            margin=ft.margin.only(bottom=20)
                        ),
                        
                        ft.Text("👥 Parent Selection:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_900),
                        ft.Text("(Using plant height as example trait: T = Tall, t = short)", size=14, color=ft.Colors.GREY_600),
                        
                        ft.ResponsiveRow([
                            ft.Container(parent1_trait, col={'xs': 12, 'sm': 6}),
                            ft.Container(parent2_trait, col={'xs': 12, 'sm': 6})
                        ]),
                        
                        ft.ElevatedButton(
                            "Calculate Cross",
                            on_click=lambda e: calculate_cross(),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
                        ),
                        
                        results_display,
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🤔 Try These Combinations:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("• TT × tt (What ratio do you expect?)", size=14),
                                ft.Text("• Tt × Tt (Classic monohybrid cross)", size=14),
                                ft.Text("• TT × TT (What happens here?)", size=14),
                                ft.Text("• tt × tt (Homozygous recessive cross)", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.ElevatedButton(
                            "Save Genetic Analysis",
                            on_click=lambda e: self.page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Genetic cross analysis saved to lab notebook!"))
                            ),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_cell_explorer(self):
        self.page.views.clear()
        
        current_cell_type = "animal_cell"
        selected_organelle = None
        
        def switch_cell_type(cell_type):
            nonlocal current_cell_type
            current_cell_type = cell_type
            update_cell_display()
        
        def select_organelle(organelle_name):
            nonlocal selected_organelle
            selected_organelle = organelle_name
            update_organelle_info()
        
        cell_display = ft.Container(
            ft.Text("Cell diagram will appear here", text_align=ft.TextAlign.CENTER),
            bgcolor=ft.Colors.GREY_100,
            width=400,
            height=300,
            border_radius=10,
            alignment=ft.alignment.center,
            border=ft.border.all(2, ft.Colors.TEAL_300)
        )
        
        organelle_info = ft.Container(
            ft.Text("Select an organelle to learn about its function", size=14),
            bgcolor=ft.Colors.TEAL_50,
            border_radius=8,
            padding=15,
            expand=True
        )
        
        def update_cell_display():
            cell_data = self.cell_components[current_cell_type]
            organelle_buttons = []
            
            for organelle in cell_data["organelles"]:
                organelle_buttons.append(
                    ft.ElevatedButton(
                        organelle["name"],
                        on_click=lambda e, org=organelle: select_organelle(org),
                        style=ft.ButtonStyle(
                            bgcolor=organelle["color"],
                            color=ft.Colors.WHITE
                        )
                    )
                )
            
            cell_display.content = ft.Column([
                ft.Text(f"{'Animal' if current_cell_type == 'animal_cell' else 'Plant'} Cell", 
                        size=18, weight=ft.FontWeight.BOLD),
                ft.Text("Click organelles below to explore:", size=12),
                ft.Wrap(organelle_buttons, spacing=5, run_spacing=5)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
            self.page.update()
        
        def update_organelle_info():
            if selected_organelle:
                organelle_info.content = ft.Column([
                    ft.Text(selected_organelle["name"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                    ft.Text("Function:", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(selected_organelle["function"], size=14),
                    ft.Container(
                        bgcolor=selected_organelle["color"],
                        width=50,
                        height=20,
                        border_radius=5
                    )
                ], spacing=8)
                self.page.update()
        
        view = ft.View(
            "/biology/cell_explorer",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Interactive Cell Explorer"),
                    bgcolor=ft.Colors.TEAL_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🔬 Interactive Cell Explorer", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                        ft.Text("Explore the structure and function of different cell types", size=16, color=ft.Colors.TEAL_700),
                        
                        ft.Row([
                            ft.ElevatedButton(
                                "Animal Cell",
                                on_click=lambda e: switch_cell_type("animal_cell"),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.ORANGE_600 if current_cell_type == "animal_cell" else ft.Colors.GREY_300,
                                    color=ft.Colors.WHITE
                                )
                            ),
                            ft.ElevatedButton(
                                "Plant Cell", 
                                on_click=lambda e: switch_cell_type("plant_cell"),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.GREEN_600 if current_cell_type == "plant_cell" else ft.Colors.GREY_300,
                                    color=ft.Colors.WHITE
                                )
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                        
                        ft.ResponsiveRow([
                            ft.Container(cell_display, col={'xs': 12, 'md': 6}),
                            ft.Container(organelle_info, col={'xs': 12, 'md': 6})
                        ], spacing=20),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Cell Comparison Activity:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("Compare animal and plant cells. What structures do they share? What makes each unique?", size=14),
                                ft.Text("Shared structures: nucleus, mitochondria, ribosomes, cell membrane", size=13, color=ft.Colors.BLUE_700),
                                ft.Text("Plant-only structures: cell wall, chloroplasts, large central vacuole", size=13, color=ft.Colors.GREEN_700),
                                ft.Text("Why do plant cells need these extra structures?", size=13, style=ft.TextStyle(italic=True))
                            ], spacing=8),
                            bgcolor=ft.Colors.YELLOW_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.YELLOW_300)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        # Initialize with animal cell
        update_cell_display()
        
        self.page.views.append(view)
        self.page.update()

    def show_genetics_tools(self):
        self.page.views.clear()
        
        view = ft.View(
            "/biology/genetics_tools",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.page.go("/biology")),
                    title=ft.Text("Genetics Tools"),
                    bgcolor=ft.Colors.PURPLE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧬 Genetics Learning Center", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                        ft.Text("Master inheritance patterns and genetic principles", size=16, color=ft.Colors.PURPLE_700),
                        
                        ft.ResponsiveRow([
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.GRID_ON, size=40, color=ft.Colors.GREEN_700),
                                        ft.Text("Punnett Square Calculator", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        ft.Text("Predict offspring ratios", size=12, text_align=ft.TextAlign.CENTER)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                                    on_click=lambda e: self.show_genetics_lab(),
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        bgcolor=ft.Colors.GREEN_50,
                                        shape=ft.RoundedRectangleBorder(radius=12)
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.SCIENCE, size=40, color=ft.Colors.BLUE_700),
                                        ft.Text("DNA Structure Explorer", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        ft.Text("Learn about genetic material", size=12, text_align=ft.TextAlign.CENTER)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                                    on_click=lambda e: self.show_dna_explorer(),
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        bgcolor=ft.Colors.BLUE_50,
                                        shape=ft.RoundedRectangleBorder(radius=12)
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    content=ft.Column([
                                        ft.Icon(ft.Icons.FAMILY_RESTROOM, size=40, color=ft.Colors.ORANGE_700),
                                        ft.Text("Pedigree Analysis", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        ft.Text("Track traits through families", size=12, text_align=ft.TextAlign.CENTER)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                                    on_click=lambda e: self.show_pedigree_tool(),
                                    style=ft.ButtonStyle(
                                        padding=20,
                                        bgcolor=ft.Colors.ORANGE_50,
                                        shape=ft.RoundedRectangleBorder(radius=12)
                                    )
                                ),
                                col={'xs': 12, 'sm': 6, 'md': 4}
                            ),
                        ], spacing=15, run_spacing=15),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🧬 Genetics Fundamentals:", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_900),
                                ft.Text("• Genes are segments of DNA that code for specific traits", size=14),
                                ft.Text("• Alleles are different versions of the same gene", size=14),
                                ft.Text("• Genotype is the genetic makeup (Tt)", size=14),
                                ft.Text("• Phenotype is the observable trait (tall or short)", size=14),
                                ft.Text("• Dominant alleles (T) mask recessive alleles (t)", size=14),
                                ft.Text("• Homozygous means both alleles are the same (TT or tt)", size=14),
                                ft.Text("• Heterozygous means the alleles are different (Tt)", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15,
                            margin=ft.margin.only(top=20)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_dna_explorer(self):
        self.page.views.clear()
        
        view = ft.View(
            "/biology/dna_explorer",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_genetics_tools()),
                    title=ft.Text("DNA Structure Explorer"),
                    bgcolor=ft.Colors.BLUE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("🧬 DNA Structure and Function", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                        ft.Text("Explore the molecule that carries genetic information", size=16, color=ft.Colors.BLUE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("DNA Double Helix:", size=18, weight=ft.FontWeight.BOLD),
                                ft.Text("• Two complementary strands twisted together", size=14),
                                ft.Text("• Sugar-phosphate backbone provides structure", size=14),
                                ft.Text("• Nitrogenous bases carry genetic information", size=14),
                                ft.Text("• Hydrogen bonds hold base pairs together", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Base Pairing Rules:", size=18, weight=ft.FontWeight.BOLD),
                                ft.Row([
                                    ft.Container(
                                        ft.Text("A", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        bgcolor=ft.Colors.RED_400,
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("pairs with", size=14),
                                    ft.Container(
                                        ft.Text("T", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        bgcolor=ft.Colors.ORANGE_400,
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("(Adenine - Thymine)", size=14)
                                ], spacing=10),
                                ft.Row([
                                    ft.Container(
                                        ft.Text("G", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        bgcolor=ft.Colors.GREEN_400,
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("pairs with", size=14),
                                    ft.Container(
                                        ft.Text("C", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                        bgcolor=ft.Colors.BLUE_400,
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("(Guanine - Cytosine)", size=14)
                                ], spacing=10)
                            ], spacing=15),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("DNA Functions:", size=18, weight=ft.FontWeight.BOLD),
                                ft.Text("🔄 Replication: DNA copies itself before cell division", size=14),
                                ft.Text("📝 Transcription: DNA codes for RNA messages", size=14),
                                ft.Text("🧪 Translation: RNA codes for protein synthesis", size=14),
                                ft.Text("🧬 Inheritance: DNA passes traits to offspring", size=14),
                                ft.Text("⚡ Mutation: Changes in DNA create variation", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.PURPLE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("🎯 Interactive Challenge:", size=16, weight=ft.FontWeight.BOLD),
                                ft.Text("If one DNA strand has the sequence: ATGCGA", size=14),
                                ft.Text("What would the complementary strand be?", size=14),
                                ft.Text("Answer: TACGCT", size=14, color=ft.Colors.GREEN_700, weight=ft.FontWeight.BOLD),
                                ft.Text("(Remember: A-T and G-C pairing)", size=12, style=ft.TextStyle(italic=True))
                            ], spacing=5),
                            bgcolor=ft.Colors.YELLOW_50,
                            border_radius=10,
                            padding=15,
                            border=ft.border.all(2, ft.Colors.YELLOW_400)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        self.page.views.append(view)
        self.page.update()

    def show_pedigree_tool(self):
        self.page.views.clear()
        
        view = ft.View(
            "/biology/pedigree_tool",
            [
                ft.AppBar(
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: self.show_genetics_tools()),
                    title=ft.Text("Pedigree Analysis"),
                    bgcolor=ft.Colors.ORANGE_700
                ),
                ft.Container(
                    ft.Column([
                        ft.Text("👪 Pedigree Analysis Tool", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_900),
                        ft.Text("Track genetic traits through family trees", size=16, color=ft.Colors.ORANGE_700),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Pedigree Symbols:", size=18, weight=ft.FontWeight.BOLD),
                                ft.Row([
                                    ft.Container(
                                        ft.Text("♂", size=24),
                                        bgcolor=ft.Colors.BLUE_100,
                                        width=40,
                                        height=40,
                                        border_radius=5,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("= Male (square)", size=14)
                                ], spacing=10),
                                ft.Row([
                                    ft.Container(
                                        ft.Text("♀", size=24),
                                        bgcolor=ft.Colors.PINK_100,
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("= Female (circle)", size=14)
                                ], spacing=10),
                                ft.Row([
                                    ft.Container(
                                        ft.Text("●", size=24),
                                        bgcolor=ft.Colors.BLACK,
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("= Affected individual (filled)", size=14)
                                ], spacing=10),
                                ft.Row([
                                    ft.Container(
                                        ft.Text("○", size=24),
                                        bgcolor=ft.Colors.WHITE,
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        border=ft.border.all(2, ft.Colors.BLACK),
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Text("= Unaffected individual (empty)", size=14)
                                ], spacing=10)
                            ], spacing=10),
                            bgcolor=ft.Colors.ORANGE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Reading Pedigrees:", size=18, weight=ft.FontWeight.BOLD),
                                ft.Text("• Horizontal lines connect mates", size=14),
                                ft.Text("• Vertical lines connect parents to children", size=14),
                                ft.Text("• Each generation is numbered (I, II, III)", size=14),
                                ft.Text("• Individuals in each generation are numbered", size=14),
                                ft.Text("• Look for patterns to determine inheritance mode", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.BLUE_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.Container(
                            ft.Column([
                                ft.Text("Inheritance Patterns:", size=18, weight=ft.FontWeight.BOLD),
                                ft.Text("🔵 Autosomal Dominant:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
                                ft.Text("• Trait appears in every generation", size=14),
                                ft.Text("• Affected parents can have unaffected children", size=14),
                                ft.Text("• Males and females equally affected", size=14),
                                
                                ft.Text("🔴 Autosomal Recessive:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
                                ft.Text("• Trait may skip generations", size=14),
                                ft.Text("• Unaffected parents can have affected children", size=14),
                                ft.Text("• Consanguinity (related parents) increases risk", size=14),
                                
                                ft.Text("💜 X-linked Recessive:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_700),
                                ft.Text("• More males affected than females", size=14),
                                ft.Text("• Affected males cannot pass to sons", size=14),
                                ft.Text("• Carrier mothers can pass to children", size=14)
                            ], spacing=8),
                            bgcolor=ft.Colors.GREEN_50,
                            border_radius=10,
                            padding=15
                        ),
                        
                        ft.ElevatedButton(
                            "Practice Pedigree Analysis",
                            on_click=lambda e: self.page.show_snack_bar(
                                ft.SnackBar(content=ft.Text("Interactive pedigree practice problems coming soon!"))
                            ),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.ORANGE_600, color=ft.Colors.WHITE)
                        )
                    ], spacing=20),
                    padding=20,
                    expand=True
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )