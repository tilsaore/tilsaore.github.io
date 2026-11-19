"""Spanish translation of index.html: (english, spanish) pairs."""

PAIRS = [
    # Head
    ("<title>Tilsa Oré Mónago | Energy &amp; Competition Economist</title>",
     "<title>Tilsa Oré Mónago | Economista de energía y competencia</title>"),
    ('content="Tilsa Oré Mónago | Energy &amp; Competition Economist"',
     'content="Tilsa Oré Mónago | Economista de energía y competencia"'),
    ("Tilsa Oré Mónago is a Lecturer in the Department of Economics at Rice University and a Fellow in Energy and Market Design at the Baker Institute's Center for Energy Studies. Research on electricity retail markets, critical minerals, green hydrogen, and competition policy.",
     "Tilsa Oré Mónago es docente del Departamento de Economía de Rice University y Fellow en Energía y Diseño de Mercados del Centro de Estudios Energéticos del Instituto Baker. Investiga mercados minoristas de electricidad, minerales críticos, hidrógeno verde y política de competencia."),
    ("Lecturer in Economics at Rice University and Fellow in Energy and Market Design at the Baker Institute. Electricity retail markets, critical minerals, green hydrogen, and competition policy.",
     "Docente de Economía en Rice University y Fellow en Energía y Diseño de Mercados en el Instituto Baker. Mercados minoristas de electricidad, minerales críticos, hidrógeno verde y política de competencia."),

    # Link-preview card
    ("https://tilsaore.com/images/social-card.jpg", "https://tilsaore.com/images/social-card-es.jpg"),
    ('content="Tilsa Oré Mónago, Energy and Competition Economist, Rice University and Baker Institute for Public Policy"',
     'content="Tilsa Oré Mónago, economista de energía y competencia, Rice University e Instituto Baker de Políticas Públicas"'),

    # Navigation and sidebar
    (">Skip to main content</a>", ">Saltar al contenido principal</a>"),
    ('alt="Rice University\'s Baker Institute for Public Policy"',
     'alt="Instituto Baker de Políticas Públicas de Rice University"'),
    ("Fellow in Energy and Market Design, Center for Energy Studies, Baker Institute for Public Policy<br>Lecturer, Department of Economics, Rice University",
     "Fellow en Energía y Diseño de Mercados, Centro de Estudios Energéticos, Instituto Baker de Políticas Públicas<br>Docente, Departamento de Economía, Rice University"),
    (">Curriculum vitae (PDF)</a>", ">Currículum vitae (PDF, en inglés)</a>"),
    (">Résumé, 2 pages (PDF)</a>", ">Resumen curricular, 2 páginas (PDF, en inglés)</a>"),
    (">Baker Institute profile</a>", ">Perfil en el Instituto Baker</a>"),
    (">Center for Energy Studies</a>", ">Centro de Estudios Energéticos</a>"),

    # Introduction
    ("I am a Lecturer in the Department of Economics at Rice University and a Fellow in Energy and Market Design at the Center for Energy Studies of Rice University's Baker Institute for Public Policy. My research is in industrial organization, competition policy, and game theory, and I currently work on renewable energy, green hydrogen, electricity retail markets, and critical minerals for the energy transition.",
     "Soy docente del Departamento de Economía de Rice University y Fellow en Energía y Diseño de Mercados del Centro de Estudios Energéticos del Instituto Baker de Políticas Públicas de Rice University. Mi investigación se centra en organización industrial, política de competencia y teoría de juegos, y actualmente trabajo en energías renovables, hidrógeno verde, mercados minoristas de electricidad y minerales críticos para la transición energética."),
    ("I teach in Rice's Master of Energy Economics, the Online Master of Data Science, and the undergraduate economics program. Previously I was a consultant with the World Bank Group's Markets and Competition Global Team, a tenure-track assistant professor at the Universidad de Piura in Peru, and Senior Economist and Head of the Economic Research Unit at INDECOPI, Peru's competition authority. I received my PhD in Economics from Stony Brook University.",
     "Enseño en las maestrías Master of Energy Economics y Online Master of Data Science de Rice, así como en el programa de pregrado en Economía. Anteriormente fui consultora del Equipo Global de Mercados y Competencia del Grupo Banco Mundial, profesora asistente (tenure-track) en la Universidad de Piura, en el Perú, y Economista Senior y Jefa de la Unidad de Investigación Económica del INDECOPI, la autoridad de competencia del Perú. Obtuve mi doctorado (PhD) en Economía en Stony Brook University."),
    ("I am also a co-founder of <a href=\"https://locupix.com\">Locupix</a>, an early-stage language-learning company that supports 20+ languages, where I have contributed to company formation, tax-related administration, business strategy, and administrative approvals.",
     "También soy cofundadora de <a href=\"https://locupix.com\">Locupix</a>, una empresa emergente de aprendizaje de idiomas que ofrece más de 20 idiomas, donde he contribuido a la constitución de la empresa, la administración tributaria, la estrategia de negocio y la obtención de aprobaciones administrativas."),

    # Section headings
    ("<h2>Areas of expertise</h2>", "<h2>Áreas de especialización</h2>"),
    ("<h2>Work at the Baker Institute</h2>", "<h2>Trabajo en el Instituto Baker</h2>"),
    ("<h2>Media and talks</h2>", "<h2>Medios y conferencias</h2>"),
    ("<h2>Other selected work</h2>", "<h2>Otros trabajos seleccionados</h2>"),
    (">Experience</h2>", ">Experiencia</h2>"),
    (">Teaching at Rice</h2>", ">Docencia en Rice</h2>"),
    (">Education</h2>", ">Formación académica</h2>"),

    # Areas of expertise
    ("Industrial organization and game theory: market structure, pricing strategies, and switching costs in network industries.",
     "Organización industrial y teoría de juegos: estructura de mercado, estrategias de precios y costos de cambio en industrias de red."),
    ("Electricity markets: price dispersion and competition in retail electricity.",
     "Mercados de electricidad: dispersión de precios y competencia en el mercado minorista de electricidad."),
    ("Energy transition: green hydrogen, critical minerals and trade, clean energy goals, and climate finance.",
     "Transición energética: hidrógeno verde, minerales críticos y comercio, metas de energía limpia y financiamiento climático."),
    ("Competition policy and regulation: product market regulation, competitive neutrality, and competition chapters in trade agreements.",
     "Política de competencia y regulación: regulación de mercados de productos, neutralidad competitiva y capítulos de competencia en acuerdos comerciales."),
    ("Applied econometrics and data science: Python (including MLOps and LLMOps), R, Stata, Hugging Face, and Claude Code.",
     "Econometría aplicada y ciencia de datos: Python (incluidos MLOps y LLMOps), R, Stata, Hugging Face y Claude Code."),

    # Work at the Baker Institute
    ('<div class="gray">Baker Institute for Public Policy, 2024</div>',
     '<div class="gray">Instituto Baker de Políticas Públicas, 2024</div>'),
    ("Latin America's role in supplying copper and lithium for the energy transition, and how lengthy permitting processes and mining conflicts create supply risk.",
     "El papel de América Latina en el suministro de cobre y litio para la transición energética, y cómo los largos procesos de permisos y los conflictos mineros generan riesgos de suministro."),
    ("In <em>Energy Insights 2026</em>, Center for Energy Studies, October 2026. Also covered by ",
     "En <em>Energy Insights 2026</em>, Centro de Estudios Energéticos, octubre de 2026. También reseñado por "),
    ("In <em>Energy Insights 2025</em>, Center for Energy Studies, October 2025.",
     "En <em>Energy Insights 2025</em>, Centro de Estudios Energéticos, octubre de 2025."),
    ("In <em>Energy and Resilience: Policy Briefs 2025</em>, Baker Institute, June 2025.",
     "En <em>Energy and Resilience: Policy Briefs 2025</em>, Instituto Baker, junio de 2025."),
    ("Working paper with M. Michot Foss, B. Cortés Leiss, and F. J. Monaldi. Center for Energy Studies, December 2024.",
     "Documento de trabajo con M. Michot Foss, B. Cortés Leiss y F. J. Monaldi. Centro de Estudios Energéticos, diciembre de 2024."),
    ("With B. Leiss, L. Maxwell, and C. White-Nockleby. Center for Energy Studies, 2023.",
     "Con B. Leiss, L. Maxwell y C. White-Nockleby. Centro de Estudios Energéticos, 2023."),

    # Media and talks
    ("<em>BBC News Mundo</em>, March 2026. Interviewed on U.S. and Chinese competition for Latin American critical minerals.",
     "<em>BBC News Mundo</em>, marzo de 2026. Entrevista sobre la competencia entre Estados Unidos y China por los minerales críticos de América Latina."),
    ("Covers the <em>Energy Insights 2026</em> article on Texas's competitive retail electricity market.",
     "Reseña el artículo de <em>Energy Insights 2026</em> sobre el mercado minorista competitivo de electricidad de Texas."),
    ("Featured Q&amp;A, <em>Energy Advisor</em>, Inter-American Dialogue, May 9, 2025. Commentary on U.S. trade with Mexico and South America in critical minerals.",
     "Pregunta destacada, <em>Energy Advisor</em>, Diálogo Interamericano, 9 de mayo de 2025. Comentario sobre el comercio de minerales críticos de Estados Unidos con México y América del Sur."),
    (">Speaker, VIII World Forum on Energy Regulation</a>. <span class=\"gray\">Lima, Peru, 2023.</span>",
     ">Ponente, VIII Foro Mundial de Regulación de la Energía (WFER)</a>. <span class=\"gray\">Lima, Perú, 2023.</span>"),

    # Other selected work
    ("<span class=\"gray\">With B. Choe. Chapter 7 in <em>",
     "<span class=\"gray\">Con B. Choe. Capítulo 7 en <em>"),
    ("<li>Clean Power Implementation Index: measuring GCC countries' fulfillment of clean energy goals. <span class=\"gray\">With J. Krane, C. Li, and F. Arifurrahman. Working paper.</span>",
     "<li><span lang=\"en\">Clean Power Implementation Index: measuring GCC countries' fulfillment of clean energy goals.</span> <span class=\"gray\">Con J. Krane, C. Li y F. Arifurrahman. Documento de trabajo.</span>"),
    ("<li>Price dispersion and competition in retail electricity markets. <span class=\"gray\">With J. Kim and S. Kim. Work in progress.</span>",
     "<li><span lang=\"en\">Price dispersion and competition in retail electricity markets.</span> <span class=\"gray\">Con J. Kim y S. Kim. Trabajo en curso.</span>"),
    (">Full list of publications in the CV (PDF)</a>",
     ">Lista completa de publicaciones en el CV (PDF, en inglés)</a>"),

    # Experience: official position titles kept in the institution's language
    ("–present</th>", "–presente</th>"),
    ("<td>Lecturer, Department of Economics, Rice University</td>",
     '<td lang="en">Lecturer, Department of Economics, Rice University</td>'),
    ("<td>Fellow in Energy and Market Design, Center for Energy Studies, Rice University's Baker Institute for Public Policy</td>",
     "<td lang=\"en\">Fellow in Energy and Market Design, Center for Energy Studies, Rice University's Baker Institute for Public Policy</td>"),
    ("<td>Co-founder, <a href=\"https://locupix.com\">Locupix</a>, an early-stage language-learning company that supports 20+ languages</td>",
     "<td>Cofundadora, <a href=\"https://locupix.com\">Locupix</a>, empresa emergente de aprendizaje de idiomas que ofrece más de 20 idiomas</td>"),
    ("<td>Lecturer, Online Master of Data Science Program, Department of Computer Science, Rice University</td>",
     '<td lang="en">Lecturer, Online Master of Data Science Program, Department of Computer Science, Rice University</td>'),
    ("<td>Adjunct Lecturer, Master of Energy Economics Program, Department of Economics, Rice University</td>",
     '<td lang="en">Adjunct Lecturer, Master of Energy Economics Program, Department of Economics, Rice University</td>'),
    ("<td>Assistant Professor (tenure-track), Department of Economics, Universidad de Piura, Peru; Undergraduate Program Director, Lima campus (2020–2021)</td>",
     "<td>Profesora asistente (tenure-track), Departamento de Economía, Universidad de Piura, Perú; directora del programa de pregrado, campus Lima (2020–2021)</td>"),
    ("<td>Adjunct Professorial Lecturer, Department of Economics, American University</td>",
     '<td lang="en">Adjunct Professorial Lecturer, Department of Economics, American University</td>'),
    ("<td>Consultant, Markets and Competition Global Team, World Bank Group</td>",
     '<td lang="en">Consultant, Markets and Competition Global Team, World Bank Group</td>'),
    ("<td>Senior Economist and Head of the Economic Research Unit (2007–2010); Economic Analyst (2006–2007), Department of Economic Studies, INDECOPI, Peru</td>",
     "<td>Economista Senior y Jefa de la Unidad de Investigación Económica (2007–2010); Analista Económica (2006–2007), Gerencia de Estudios Económicos, INDECOPI, Perú</td>"),
    ("<td>Economic Adviser, Secretariat of Communications, Ministry of Transportation and Communications, Peru</td>",
     "<td>Asesora Económica, Secretaría de Comunicaciones, Ministerio de Transportes y Comunicaciones, Perú</td>"),

    # Teaching (official course titles stay in English)
    ("<td>Industrial Organization and Energy Sector</td>", "<td lang=\"en\">Industrial Organization and Energy Sector</td>"),
    ("<td>Statistics and Applied Econometrics for Energy Markets</td>", "<td lang=\"en\">Statistics and Applied Econometrics for Energy Markets</td>"),
    ("<td>Probability and Statistics for Computing and Data Science</td>", "<td lang=\"en\">Probability and Statistics for Computing and Data Science</td>"),
    ("<td>Applied Econometrics</td>", "<td lang=\"en\">Applied Econometrics</td>"),
    ("<td>Game Theory</td>", "<td lang=\"en\">Game Theory</td>"),
    ("<td>Global Governance and International Business Environment</td>", "<td lang=\"en\">Global Governance and International Business Environment</td>"),

    # Education
    ("PhD in Economics, Stony Brook University<br><span class=\"gray\">Advisors: ",
     "Doctorado (PhD) en Economía, Stony Brook University<br><span class=\"gray\">Asesores de tesis: "),
    ("</a> and <a href=\"https://www.stonybrook.edu/commcms/economics/people/_bios/BRUSCO.php\">",
     "</a> y <a href=\"https://www.stonybrook.edu/commcms/economics/people/_bios/BRUSCO.php\">"),
    ("MA in Applied Economics, University of Oklahoma (Fulbright Fellow)",
     "Maestría (MA) en Economía Aplicada, University of Oklahoma (becaria Fulbright)"),
    ("MA in International Trade and Economic Cooperation, Kyung Hee University",
     "Maestría (MA) en Comercio Internacional y Cooperación Económica, Kyung Hee University"),
    ("BSc in Economics, Pontificia Universidad Católica del Perú",
     "Bachillerato (BSc) en Economía, Pontificia Universidad Católica del Perú"),
]
