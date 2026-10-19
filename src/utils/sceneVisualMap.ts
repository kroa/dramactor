export interface SceneVisualConfig {
  locationTag: string;
  cameraRig: string;
  videoSrc: string;
  hasAuthenticVideo: boolean;
  themeColor: string;
  accentGlow: string;
  roleDescription: string;
  atmosphereBadge: string;
  genreEmoji: string;
}

interface GenreVisualPreset {
  videoEp: number;
  locationTag: string;
  cameraRig: string;
  themeColor: string;
  accentGlow: string;
  defaultRole: string;
  atmosphereBadge: string;
  genreEmoji: string;
}

export const GENRE_VISUAL_PRESETS: Record<string, GenreVisualPreset> = {
  // 1. Legal Drama
  'Legal Drama': {
    videoEp: 1,
    locationTag: 'MANHATTAN PEARSON HARDMAN • 50F CORNER SUITE',
    cameraRig: 'ARRI ALEXA 35 • ANAMORPHIC 50MM T1.9',
    themeColor: 'from-cyan-900/40 via-blue-950/60 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Senior Partner • Pearson Hardman',
    atmosphereBadge: '🌙 21:45 EST • LATE NIGHT',
    genreEmoji: '⚖️',
  },
  // 2. Silicon Valley Startup
  'Silicon Valley Startup': {
    videoEp: 2,
    locationTag: 'PALO ALTO SAND HILL ROAD • SEQUOIA BOARDROOM',
    cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME PRIME',
    themeColor: 'from-emerald-900/40 via-teal-950/60 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Founding Partner • Horizon Ventures',
    atmosphereBadge: '☀️ 14:15 PST • SEED CLOSING',
    genreEmoji: '🚀',
  },
  // 3. Corporate Empire & M&A
  'Corporate Empire & M&A': {
    videoEp: 3,
    locationTag: 'HUDSON YARDS WAYSTAR • 45F EXECUTIVE PENTHOUSE',
    cameraRig: 'PANAVISION DXL2 • PRIMO 70',
    themeColor: 'from-amber-900/40 via-orange-950/60 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Chief Financial Officer • Global Media',
    atmosphereBadge: '🌅 18:30 EST • SUNSET CRISIS',
    genreEmoji: '🏢',
  },
  // 4. Emergency Medicine
  'Emergency Medicine': {
    videoEp: 4,
    locationTag: 'SEATTLE GRACE HOSPITAL • CHIEF SURGEON SUITE',
    cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
    themeColor: 'from-teal-900/40 via-cyan-950/60 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Chief of Surgery • Trauma Unit',
    atmosphereBadge: '🚨 03:12 PST • EMERGENCY TRAUMA',
    genreEmoji: '🏥',
  },
  // 5. Manhattan Romance & High Society
  'Manhattan Romance & High Society': {
    videoEp: 5,
    locationTag: 'SOHO SKYLIGHT LOUNGE • PRIVATE ROOFTOP CABANA',
    cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
    themeColor: 'from-fuchsia-900/40 via-purple-950/60 to-zinc-950',
    accentGlow: 'text-fuchsia-400 border-fuchsia-500/40',
    defaultRole: 'Julian Vance • Lead Art Curator',
    atmosphereBadge: '🍸 22:30 EST • SOHO TWILIGHT',
    genreEmoji: '🥂',
  },
  // 6. Wall Street Hedge Fund
  'Wall Street Hedge Fund': {
    videoEp: 6,
    locationTag: 'WALL STREET FINANCIAL TOWER • WAR ROOM',
    cameraRig: 'ARRI ALEXA LF • MASTER ANAMORPHIC',
    themeColor: 'from-rose-900/40 via-red-950/60 to-zinc-950',
    accentGlow: 'text-rose-400 border-rose-500/40',
    defaultRole: 'Activist Hedge Fund Principal • M&A',
    atmosphereBadge: '⚡ 02:45 EST • MIDNIGHT TAKEOVER',
    genreEmoji: '📈',
  },
  // 7. Tech Keynote & AI
  'Tech Keynote & AI': {
    videoEp: 7,
    locationTag: 'MOSCONE WEST KEYNOTE STAGE • YC DEMO DAY',
    cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
    themeColor: 'from-violet-900/40 via-indigo-950/60 to-zinc-950',
    accentGlow: 'text-violet-400 border-violet-500/40',
    defaultRole: 'Managing Director • Y Combinator',
    atmosphereBadge: '🚀 11:00 PST • KEYNOTE STAGE',
    genreEmoji: '💻',
  },
  // 8. FBI Criminal Profiling
  'FBI Criminal Profiling': {
    videoEp: 8,
    locationTag: 'QUEENS SAFE HOUSE • INTERROGATION CELL B',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-blue-950/60 via-slate-950/80 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Agent Miller • FBI Lead Investigator',
    atmosphereBadge: '🚨 01:30 EST • LATE NIGHT INTERROGATION',
    genreEmoji: '🔍',
  },
  // 9. White House Politics
  'White House Politics': {
    videoEp: 8,
    locationTag: 'THE WHITE HOUSE SITUATION ROOM • LEVEL -2 BUNKER',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM T1.3',
    themeColor: 'from-slate-950 via-zinc-950 to-red-950/40',
    accentGlow: 'text-red-400 border-red-500/40',
    defaultRole: 'General Hayes • Chairman of Joint Chiefs',
    atmosphereBadge: '🚨 00:04 EST • DEFCON 2 ALERT',
    genreEmoji: '🏛️',
  },
  // 10. Michelin Culinary
  'Michelin Culinary': {
    videoEp: 5,
    locationTag: 'MANHATTAN LE BERNARDIN • 3-STAR SERVICE KITCHEN',
    cameraRig: 'ARRI MINI LF • LEICA SUMMILUX 35MM',
    themeColor: 'from-amber-950/60 via-orange-950/40 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Head Chef • Executive Culinary Director',
    atmosphereBadge: '🔥 19:45 EST • DINNER SERVICE RUSH',
    genreEmoji: '🔪',
  },
  // 11. Broadway Musical Theatre
  'Broadway Musical Theatre': {
    videoEp: 7,
    locationTag: 'RICHARD RODGERS THEATRE • BACKSTAGE GREEN ROOM',
    cameraRig: 'ARRI ALEXA 35 • COOKE S7/i',
    themeColor: 'from-amber-950/60 via-yellow-950/40 to-zinc-950',
    accentGlow: 'text-amber-300 border-amber-400/40',
    defaultRole: 'Tony-Winning Director • Broadway Production',
    atmosphereBadge: '🎭 19:55 EST • FIVE MINUTES TO CURTAIN',
    genreEmoji: '🎭',
  },
  // 12. Sports Agency & Free Agency
  'Sports Agency & Free Agency': {
    videoEp: 7,
    locationTag: 'BEVERLY HILLS CAA HQ • WAR ROOM SUITE',
    cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
    themeColor: 'from-violet-900/40 via-indigo-950/60 to-zinc-950',
    accentGlow: 'text-violet-400 border-violet-500/40',
    defaultRole: 'Managing Director • Elite Sports Division',
    atmosphereBadge: '⚾ 23:55 EST • DEADLINE LOCKOUT',
    genreEmoji: '⚾',
  },
  // 13. Hollywood Talent Agency
  'Hollywood Talent Agency': {
    videoEp: 7,
    locationTag: 'CENTURY CITY TALENT AGENCY • CORNER CORRIDOR',
    cameraRig: 'RED MONSTRO 8K • ZEISS SUPREME',
    themeColor: 'from-indigo-950/50 via-purple-950/40 to-zinc-950',
    accentGlow: 'text-indigo-400 border-indigo-500/40',
    defaultRole: 'Senior Managing Partner • A-List Division',
    atmosphereBadge: '🎬 16:30 PST • PACKAGING CALL',
    genreEmoji: '🎬',
  },
  // 14. Crisis PR Management
  'Crisis PR Management': {
    videoEp: 7,
    locationTag: 'ROCKEFELLER CENTER • STRATEGIC CRISIS SUITE',
    cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
    themeColor: 'from-violet-950/50 via-blue-950/40 to-zinc-950',
    accentGlow: 'text-violet-400 border-violet-500/40',
    defaultRole: 'Principal Crisis Strategist • Media War',
    atmosphereBadge: '📣 07:15 EST • BREAKING NEWS SPIN',
    genreEmoji: '📣',
  },
  // 15. Luxury Real Estate
  'Luxury Real Estate': {
    videoEp: 3,
    locationTag: 'TRIBECA PENTHOUSE • 56 LEONARD SKY SALON',
    cameraRig: 'PANAVISION DXL2 • PRIMO 70',
    themeColor: 'from-amber-950/50 via-yellow-950/40 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Managing Broker • Ultra-Luxury Estates',
    atmosphereBadge: '🍸 17:45 EST • EXCLUSIVE SHOWING',
    genreEmoji: '🏰',
  },
  // 16. 5-Star Hotel Hospitality
  '5-Star Hotel Hospitality': {
    videoEp: 3,
    locationTag: 'THE PLAZA NEW YORK • PRESIDENTIAL SUITE',
    cameraRig: 'PANAVISION DXL2 • COOKE S7/i',
    themeColor: 'from-amber-900/40 via-zinc-950 to-zinc-950',
    accentGlow: 'text-amber-300 border-amber-400/40',
    defaultRole: 'General Manager • Grand Luxury Palace',
    atmosphereBadge: '🛎️ 20:00 EST • VIP INSPECTION',
    genreEmoji: '🛎️',
  },
  // 17. Fine Art Auction & Heist
  'Fine Art Auction & Heist': {
    videoEp: 5,
    locationTag: 'SOTHEBY’S MANHATTAN • HIGH-VALUE VAULT ROOM',
    cameraRig: 'ARRI MINI LF • COOKE S7/i',
    themeColor: 'from-purple-950/50 via-indigo-950/40 to-zinc-950',
    accentGlow: 'text-purple-400 border-purple-500/40',
    defaultRole: 'Senior Art Specialist & Appraiser',
    atmosphereBadge: '🎨 19:00 EST • EVENING SALE',
    genreEmoji: '🎨',
  },
  // 18. Investigative Journalism
  'Investigative Journalism': {
    videoEp: 7,
    locationTag: 'THE WASHINGTON POST • DEEP SOURCE ARCHIVE',
    cameraRig: 'RED MONSTRO 8K • LEICA THALIA',
    themeColor: 'from-indigo-900/40 via-zinc-950 to-zinc-950',
    accentGlow: 'text-indigo-300 border-indigo-400/40',
    defaultRole: 'Investigative Editor • National Desk',
    atmosphereBadge: '🗞️ 01:20 EST • FRONT PAGE DEADLINE',
    genreEmoji: '🗞️',
  },
  // 19. Aerospace & NASA Mission Control
  'Aerospace & NASA Mission Control': {
    videoEp: 2,
    locationTag: 'HOUSTON JOHNSON SPACE CENTER • FLIGHT DIRECTOR CONSOLE',
    cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME',
    themeColor: 'from-sky-950/60 via-blue-950/40 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Flight Director • Orbital Missions',
    atmosphereBadge: '🚀 T-MINUS 04 MIN • ORBITAL GO/NO-GO',
    genreEmoji: '🛰️',
  },
  // 20. Cybercrime & Dark Web Intelligence
  'Cybercrime & Dark Web Intelligence': {
    videoEp: 8,
    locationTag: 'FORT MEADE NSA CYBER COMMAND • AIR-GAPPED VAULT',
    cameraRig: 'ARRI ALEXA MINI • ANAMORPHIC 35MM',
    themeColor: 'from-emerald-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Lead Threat Hunter • Zero-Day Unit',
    atmosphereBadge: '⚡ 03:22 GMT • ZERO-DAY EXPLOIT IN PROGRESS',
    genreEmoji: '💻',
  },
  // 21. High-Stakes Casino Poker
  'High-Stakes Casino Poker': {
    videoEp: 5,
    locationTag: 'BELLAGIO LAS VEGAS • BOBBY’S ROOM HIGH-LIMIT SALON',
    cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
    themeColor: 'from-rose-950/50 via-zinc-950 to-zinc-950',
    accentGlow: 'text-rose-400 border-rose-500/40',
    defaultRole: 'High-Stakes Shark & High-Roller Host',
    atmosphereBadge: '♠️ 04:15 PST • 2.5 MILLION POT',
    genreEmoji: '♠️',
  },
  // 22. Formula 1 Team Principal & Paddock
  'Formula 1 Team Principal & Paddock': {
    videoEp: 7,
    locationTag: 'SILVERSTONE PADDOCK • TEAM PIT WALL TELEMETRY DESK',
    cameraRig: 'RED MONSTRO 8K • ZEISS SUPREME',
    themeColor: 'from-red-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-red-400 border-red-500/40',
    defaultRole: 'Team Principal • Scuderia Strategy Wall',
    atmosphereBadge: '🏎️ LAP 48/52 • UNDER-CUT WINDOW OPEN',
    genreEmoji: '🏎️',
  },
  // 23. Sommelier & Napa Valley Dynasty
  'Sommelier & Napa Valley Dynasty': {
    videoEp: 5,
    locationTag: 'NAPA VALLEY OAKVILLE ESTATE • UNDERGROUND CELLAR VAULT',
    cameraRig: 'ARRI MINI LF • COOKE S7/i',
    themeColor: 'from-purple-950/60 via-amber-950/40 to-zinc-950',
    accentGlow: 'text-purple-300 border-purple-400/40',
    defaultRole: 'Master Sommelier & Vineyard Heir',
    atmosphereBadge: '🍷 19:30 PST • VINTAGE BLIND TASTING',
    genreEmoji: '🍷',
  },
  // 24. Fashion Runway & Haute Couture
  'Fashion Runway & Haute Couture': {
    videoEp: 5,
    locationTag: 'PARIS FASHION WEEK • GRAND PALAIS BACKSTAGE',
    cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
    themeColor: 'from-fuchsia-950/50 via-pink-950/40 to-zinc-950',
    accentGlow: 'text-fuchsia-300 border-fuchsia-400/40',
    defaultRole: 'Creative Director • Haute Couture House',
    atmosphereBadge: '✨ 20:15 CET • RUNWAY CALL',
    genreEmoji: '👗',
  },
  // 25. Architecture & Urban Megaprojects
  'Architecture & Urban Megaprojects': {
    videoEp: 3,
    locationTag: 'HUDSON YARDS TOWER 1 • ARCHITECTURAL OBSERVATORY',
    cameraRig: 'PANAVISION DXL2 • PRIMO 70',
    themeColor: 'from-slate-900/50 via-blue-950/40 to-zinc-950',
    accentGlow: 'text-slate-300 border-slate-400/40',
    defaultRole: 'Pritzker-Winning Principal Architect',
    atmosphereBadge: '📐 15:40 EST • BLUEPRINT REVIEW',
    genreEmoji: '📐',
  },
  // 26. Quantum Computing & Cryptography
  'Quantum Computing & Cryptography': {
    videoEp: 2,
    locationTag: 'YORKTOWN HEIGHTS • CRYOGENIC DILUTION FRIDGE LAB',
    cameraRig: 'RED V-RAPTOR 8K • LEICA THALIA 35MM',
    themeColor: 'from-cyan-950/60 via-indigo-950/40 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Lead Quantum Physicist • 1000-Qubit Core',
    atmosphereBadge: '⚛️ 15 MILLIKELVIN • COHERENCE LOCKED',
    genreEmoji: '⚛️',
  },
  // 27. Diplomatic Summit & Hostage Negotiation
  'Diplomatic Summit & Hostage Negotiation': {
    videoEp: 8,
    locationTag: 'GENEVA PALAIS DES NATIONS • NEUTRAL NEGOTIATION ROOM',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME',
    themeColor: 'from-blue-950/60 via-slate-950 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Chief Hostage Negotiator & Special Envoy',
    atmosphereBadge: '🕊️ 02:10 CET • FINAL EXPIRY DEADLINE',
    genreEmoji: '🕊️',
  },
  // 28. Maritime Salvage & Deep Sea Exploration
  'Maritime Salvage & Deep Sea Exploration': {
    videoEp: 4,
    locationTag: 'NORTH ATLANTIC RESEARCH SHIP • ROV DIVE CONTROL BRIDGE',
    cameraRig: 'SONY VENICE 2 • ZEISS SUPREME',
    themeColor: 'from-teal-950/70 via-slate-950 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Expedition Commander & Deep Salvage Master',
    atmosphereBadge: '⚓ 3,800 METERS • HULL CONTACT VERIFIED',
    genreEmoji: '⚓',
  },
  // 29. Airline Cockpit & Air Traffic Emergency
  'Airline Cockpit & Air Traffic Emergency': {
    videoEp: 8,
    locationTag: 'FLIGHT 842 COCKPIT • FL350 EMERGENCY DESCENT',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-red-950/50 via-slate-950 to-zinc-950',
    accentGlow: 'text-red-400 border-red-500/40',
    defaultRole: 'Captain Reynolds • Pilot in Command',
    atmosphereBadge: '⚠️ 35,000 FT • MAYDAY DECLARED',
    genreEmoji: '✈️',
  },
  // 30. Forensic Pathology & Coroner Inquest
  'Forensic Pathology & Coroner Inquest': {
    videoEp: 4,
    locationTag: 'MANHATTAN MEDICAL EXAMINER • CHIEF AUTOPSY SUITE',
    cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
    themeColor: 'from-cyan-950/70 via-zinc-950 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Chief Medical Examiner • Forensics',
    atmosphereBadge: '🔬 01:15 EST • TOXICOLOGY INQUEST',
    genreEmoji: '🔬',
  },
  // 31. Commercial Espionage & Trade Secrets
  'Commercial Espionage & Trade Secrets': {
    videoEp: 6,
    locationTag: 'ZURICH SECURE SUITE • INDUSTRIAL RECON WAR ROOM',
    cameraRig: 'ARRI ALEXA LF • MASTER ANAMORPHIC',
    themeColor: 'from-slate-950 via-zinc-950 to-emerald-950/40',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Director of Corporate Counter-Intelligence',
    atmosphereBadge: '🕵️ 03:00 CET • EXFILTRATION SIGNAL ACTIVE',
    genreEmoji: '🕵️',
  },
  // 32. Wilderness Search & Mountain Rescue
  'Wilderness Search & Mountain Rescue': {
    videoEp: 4,
    locationTag: 'DENALI BASE CAMP • RANGER COMMAND TENT',
    cameraRig: 'SONY VENICE 2 • ZEISS SUPREME',
    themeColor: 'from-blue-950/60 via-slate-900/50 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Lead Mountain Rescue Commander',
    atmosphereBadge: '🏔️ -28°C BLIZZARD • THERMAL DRONE LOCK',
    genreEmoji: '🏔️',
  },
  // 33. Symphony Orchestra Conductor & Virtuoso
  'Symphony Orchestra Conductor & Virtuoso': {
    videoEp: 7,
    locationTag: 'CARNEGIE HALL • MAIN AUDITORIUM PODIUM',
    cameraRig: 'ARRI ALEXA 35 • ANAMORPHIC 50MM',
    themeColor: 'from-amber-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-amber-300 border-amber-400/40',
    defaultRole: 'Maestro & Music Director • Philharmonic',
    atmosphereBadge: '🎼 FINAL REHEARSAL • MOVEMENT IV CADENZA',
    genreEmoji: '🎼',
  },
  // 34. Space Mining & Asteroid Belt Colony
  'Space Mining & Asteroid Belt Colony': {
    videoEp: 2,
    locationTag: 'CERES MINING RIG ALPHA • EXTRACTION REFINERY DECK',
    cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME',
    themeColor: 'from-indigo-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-indigo-400 border-indigo-500/40',
    defaultRole: 'Station Operations Director • Asteroid Belt',
    atmosphereBadge: '🌌 0.03G • PLATINUM CORE BREACH',
    genreEmoji: '🌌',
  },
  // 35. Private Military Contractor & Security
  'Private Military Contractor & Security': {
    videoEp: 8,
    locationTag: 'DUBAI MARINA SAFE COMPOUND • TACTICAL OPERATIONS HUB',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME',
    themeColor: 'from-amber-950/50 via-slate-950 to-zinc-950',
    accentGlow: 'text-amber-500 border-amber-500/40',
    defaultRole: 'Managing Director • Elite Protection Group',
    atmosphereBadge: '🛡️ DEFCON TACTICAL • VIP MOTORCADE ESCORT',
    genreEmoji: '🛡️',
  },
  // 36. Antiquities Smuggling & Archaeological Recon
  'Antiquities Smuggling & Archaeological Recon': {
    videoEp: 5,
    locationTag: 'CAIRO MUSEUM SECURE ARCHIVE • BASEMENT VAULT',
    cameraRig: 'ARRI MINI LF • COOKE S7/i',
    themeColor: 'from-amber-950/60 via-stone-950 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Chief Antiquities Investigator & Epigrapher',
    atmosphereBadge: '🏺 23:10 EEST • PAPYRUS AUTHENTICATION',
    genreEmoji: '🏺',
  },
  // 37. Artificial Intelligence Ethics & Singularity
  'Artificial Intelligence Ethics & Singularity': {
    videoEp: 2,
    locationTag: 'SAN FRANCISCO MISSION BAY • AI RESEARCH CORE',
    cameraRig: 'RED V-RAPTOR 8K • LEICA THALIA 35MM',
    themeColor: 'from-teal-950/60 via-emerald-900/40 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Chief AI Scientist • Neural Systems',
    atmosphereBadge: '⚡ 23:50 PST • ALIGNMENT AUDIT',
    genreEmoji: '🤖',
  },
  // 38. Pharmaceutical Trial & FDA Approval Battle
  'Pharmaceutical Trial & FDA Approval Battle': {
    videoEp: 4,
    locationTag: 'SILVER SPRING FDA AUDITORIUM • ONCOLOGY ADVISORY PANEL',
    cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
    themeColor: 'from-blue-950/60 via-teal-950/40 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Chief Scientific Officer • Oncology Therapeutics',
    atmosphereBadge: '💊 PHASE III DATA • UNBLINDING IN 10 MIN',
    genreEmoji: '💊',
  },
  // 39. Supreme Court Constitutional Landmark
  'Supreme Court Constitutional Landmark': {
    videoEp: 1,
    locationTag: 'WASHINGTON D.C. SUPREME COURT • CHAMBERS',
    cameraRig: 'ARRI ALEXA 35 • MASTER PRIME 40MM',
    themeColor: 'from-red-950/40 via-blue-950/50 to-zinc-950',
    accentGlow: 'text-amber-300 border-amber-400/40',
    defaultRole: 'Supreme Court Advocate & Constitutional Scholar',
    atmosphereBadge: '⚖️ 10:00 EST • ORAL ARGUMENTS SESSION',
    genreEmoji: '⚖️',
  },
  // 40. Elite University Admissions & Dean Politics
  'Elite University Admissions & Dean Politics': {
    videoEp: 1,
    locationTag: 'HARVARD YARD UNIVERSITY HALL • DEAN OF ADMISSIONS OAK ROOM',
    cameraRig: 'ARRI ALEXA 35 • COOKE S7/i',
    themeColor: 'from-red-950/50 via-zinc-950 to-zinc-950',
    accentGlow: 'text-rose-400 border-rose-500/40',
    defaultRole: 'Dean of Admissions & University Provost',
    atmosphereBadge: '🎓 COMMITTEE CUTOFF • 1.8% ACCEPTANCE RATE',
    genreEmoji: '🎓',
  },
  // 41. International Mega-Event & World Expo Bid
  'International Mega-Event & World Expo Bid': {
    videoEp: 7,
    locationTag: 'LAUSANNE IOC HEADQUARTERS • EXECUTIVE BALLOT AUDITORIUM',
    cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
    themeColor: 'from-blue-950/50 via-indigo-950/40 to-zinc-950',
    accentGlow: 'text-blue-300 border-blue-400/40',
    defaultRole: 'Chairman • Olympic Bid Committee',
    atmosphereBadge: '🏅 ROUND 3 VOTING • 48 DELEGATES REMAINING',
    genreEmoji: '🏅',
  },
  // 42. Disaster Response & Hurricane Command
  'Disaster Response & Hurricane Command': {
    videoEp: 4,
    locationTag: 'MIAMI NATIONAL HURRICANE CENTER • COMMAND WATCH FLOOR',
    cameraRig: 'SONY VENICE 2 • ZEISS SUPREME',
    themeColor: 'from-teal-950/60 via-red-950/40 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'FEMA Regional Director • Storm Operations',
    atmosphereBadge: '🌀 CATEGORY 5 LANDFALL • T-MINUS 3 HOURS',
    genreEmoji: '🌀',
  },
  // 43. High-Frequency Algorithmic Arbitrage
  'High-Frequency Algorithmic Arbitrage': {
    videoEp: 6,
    locationTag: 'SECAUCUS DATA CENTER NY4 • FIBER TERMINATION CAGE',
    cameraRig: 'ARRI ALEXA LF • ZEISS MASTER PRIME',
    themeColor: 'from-emerald-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Lead Quantitative Systems Architect',
    atmosphereBadge: '📈 840 NANOSECONDS • ARBITRAGE WINDOW OPEN',
    genreEmoji: '📈',
  },
  // 44. Sovereign Wealth Fund & Trillion Dollar Deals
  'Sovereign Wealth Fund & Trillion Dollar Deals': {
    videoEp: 6,
    locationTag: 'ZURICH PRIVATE BANKING SUITE • VAULT OFFICE',
    cameraRig: 'ARRI ALEXA LF • COOKE S7/i',
    themeColor: 'from-amber-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Managing Director • Sovereign Allocations',
    atmosphereBadge: '💼 15:30 CET • TRILLION ALLOCATION',
    genreEmoji: '💼',
  },
  // 45. Intelligence Agency Deep Cover Infiltration
  'Intelligence Agency Deep Cover Infiltration': {
    videoEp: 8,
    locationTag: 'LANGLEY CIA HEADQUARTERS • SECURE OPERATIONS VAULT',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-slate-950 via-sky-950/40 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Director of Clandestine Operations • CIA',
    atmosphereBadge: '🛰️ 03:40 EST • BLACK OPS COMS',
    genreEmoji: '🛰️',
  },
  // 46. Olympic Coach & High-Performance Athletic Lab
  'Olympic Coach & High-Performance Athletic Lab': {
    videoEp: 7,
    locationTag: 'COLORADO SPRINGS OLYMPIC TRAINING • BIOMECHANICS TUNNEL',
    cameraRig: 'RED MONSTRO 8K • ZEISS SUPREME',
    themeColor: 'from-blue-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Head Olympic Coach & High-Performance Director',
    atmosphereBadge: '⏱️ 0.02S UNDER WORLD RECORD • FINAL SPLIT',
    genreEmoji: '⏱️',
  },
  // 47. Renewable Energy Titan & Green Grid Gridlock
  'Renewable Energy Titan & Green Grid Gridlock': {
    videoEp: 2,
    locationTag: 'TEXAS ERCOT LOAD CONTROL • 10GW WIND-SOLAR DESK',
    cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME',
    themeColor: 'from-emerald-950/60 via-yellow-950/40 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Chief Grid Strategist • Clean Power Titan',
    atmosphereBadge: '⚡ PEAK SURGE DEMAND • 99.8% CAPACITY',
    genreEmoji: '⚡',
  },
  // 48. Luxury Superyacht Charter & Mediterranean Elite
  'Luxury Superyacht Charter & Mediterranean Elite': {
    videoEp: 5,
    locationTag: 'MONACO PORT HERCULE • 90M SUPERYACHT BRIDGE DECK',
    cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
    themeColor: 'from-blue-950/60 via-teal-950/40 to-zinc-950',
    accentGlow: 'text-sky-300 border-sky-400/40',
    defaultRole: 'Captain & Fleet Commodore • Mediterranean Charter',
    atmosphereBadge: '⚓ 23:45 CEST • GRAND PRIX HARBOR MOORING',
    genreEmoji: '🛥️',
  },
  // 49. Biohacking & Longevity Genome Venture
  'Biohacking & Longevity Genome Venture': {
    videoEp: 4,
    locationTag: 'LA JOLLA BIOTECH CORE • TELOMERE SEQUENCING CLEANROOM',
    cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
    themeColor: 'from-teal-950/60 via-indigo-950/40 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Chief Genome Architect & Longevity Founder',
    atmosphereBadge: '🧬 EPIGENETIC CLOCK AUDIT • AGE REVERSAL MARKER',
    genreEmoji: '🧬',
  },
  // 50. Vatican Secret Archives & Papal Conclave
  'Vatican Secret Archives & Papal Conclave': {
    videoEp: 1,
    locationTag: 'VATICAN CITY ARCHIVIO APOSTOLICO • SALA DEL CONCLAVE',
    cameraRig: 'ARRI ALEXA 35 • MASTER PRIME 40MM',
    themeColor: 'from-red-950/60 via-amber-950/50 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Cardinal Camerlengo • Secret Conclave Overseer',
    atmosphereBadge: '🕯️ EXTRA OMNES • BLACK SMOKE VOTE II',
    genreEmoji: '🕯️',
  },

  // Aliases for historical / alternate titles
  'Biotech Patent War': {
    videoEp: 1,
    locationTag: 'FEDERAL DISTRICT COURT • PATENT LITIGATION CHAMBER',
    cameraRig: 'ARRI ALEXA 35 • MASTER PRIME 40MM',
    themeColor: 'from-cyan-950/60 via-slate-900/40 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Lead Trial Counsel • Biotech IP',
    atmosphereBadge: '⚖️ 10:15 EST • PRE-TRIAL HEARING',
    genreEmoji: '⚖️',
  },
  'Corporate Compliance': {
    videoEp: 1,
    locationTag: 'DOJ SPECIAL INVESTIGATION • INTERROGATION RM 4',
    cameraRig: 'ARRI ALEXA 35 • ANAMORPHIC 50MM',
    themeColor: 'from-blue-950/60 via-slate-900/50 to-zinc-950',
    accentGlow: 'text-blue-400 border-blue-500/40',
    defaultRole: 'Chief Compliance Officer & Counsel',
    atmosphereBadge: '📋 16:30 EST • DEPOSITION CALL',
    genreEmoji: '📋',
  },
  'AI Ethics & Singularity': {
    videoEp: 2,
    locationTag: 'SAN FRANCISCO MISSION BAY • AI RESEARCH CORE',
    cameraRig: 'RED V-RAPTOR 8K • LEICA THALIA 35MM',
    themeColor: 'from-teal-950/60 via-emerald-900/40 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Chief AI Scientist • Neural Systems',
    atmosphereBadge: '⚡ 23:50 PST • ALIGNMENT AUDIT',
    genreEmoji: '⚡',
  },
  'Space Tech & Commercial Launch': {
    videoEp: 2,
    locationTag: 'HAWTHORNE LAUNCH CONTROL • ORBITAL COMMAND',
    cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME',
    themeColor: 'from-indigo-950/60 via-teal-950/40 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Mission Director • Commercial Aerospace',
    atmosphereBadge: '🚀 T-MINUS 12 MIN • COUNTDOWN',
    genreEmoji: '🚀',
  },
  'Family Dynasty Succession': {
    videoEp: 3,
    locationTag: 'WAYSTAR ROYCO HELIPAD • BOARD CHAIR OFFICE',
    cameraRig: 'PANAVISION DXL2 • PRIMO 70',
    themeColor: 'from-amber-950/60 via-orange-950/40 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Board Chairman & Controlling Heir',
    atmosphereBadge: '🌆 19:15 EST • SUCCESSION VOTE',
    genreEmoji: '👑',
  },
  'Neurosurgery Dilemma': {
    videoEp: 4,
    locationTag: 'BOSTON GENERAL • NEUROSURGICAL ICU',
    cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
    themeColor: 'from-cyan-950/60 via-teal-900/40 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Chair of Neurosurgery • Trauma OR',
    atmosphereBadge: '🔬 02:45 EST • EMERGENCY CRANIOTOMY',
    genreEmoji: '🔬',
  },
  'Pandemic Containment': {
    videoEp: 4,
    locationTag: 'CDC ATLANTA • BSL-4 LEVEL QUARANTINE',
    cameraRig: 'SONY VENICE 2 • ZEISS SUPREME',
    themeColor: 'from-teal-950/60 via-emerald-950/40 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Lead Epidemiologist • Task Force Commander',
    atmosphereBadge: '☣️ 05:20 EST • OUTBREAK PROTOCOL',
    genreEmoji: '☣️',
  },
  'Crypto High Frequency Trading': {
    videoEp: 6,
    locationTag: 'CHICAGO BOARD OF TRADE • LOW-LATENCY TRADING DESK',
    cameraRig: 'ARRI ALEXA LF • ZEISS MASTER PRIME',
    themeColor: 'from-red-950/60 via-amber-950/40 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Chief Quant Strategist • HFT Desk',
    atmosphereBadge: '📈 04:00 CST • ASIAN MARKET OPEN',
    genreEmoji: '📊',
  },
  'CIA Covert Espionage': {
    videoEp: 8,
    locationTag: 'LANGLEY CIA HEADQUARTERS • SECURE OPERATIONS VAULT',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-slate-950 via-sky-950/40 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Director of Clandestine Operations • CIA',
    atmosphereBadge: '🛰️ 03:40 EST • BLACK OPS COMS',
    genreEmoji: '🕵️',
  },
  'Aviation Cockpit Emergency': {
    videoEp: 8,
    locationTag: 'FLIGHT 842 COCKPIT • FL350 EMERGENCY DESCENT',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-red-950/50 via-slate-950 to-zinc-950',
    accentGlow: 'text-red-400 border-red-500/40',
    defaultRole: 'Captain Reynolds • Pilot in Command',
    atmosphereBadge: '⚠️ 35,000 FT • MAYDAY DECLARED',
    genreEmoji: '✈️',
  },
};

export const getSceneVisualConfig = (
  episodeNumber: number,
  turnIndex?: number,
  episode?: { genre?: string; title?: string },
  _turn?: { speaker?: string; avatarEmoji?: string }
): SceneVisualConfig => {
  const TOTAL_PRODUCED = 8;
  const hasAuthenticVideo = episodeNumber <= TOTAL_PRODUCED;

  // 1. If explicit genre preset exists, use high-fidelity scenario mapping
  if (episode?.genre && GENRE_VISUAL_PRESETS[episode.genre]) {
    const preset = GENRE_VISUAL_PRESETS[episode.genre];
    const turnVideo = turnIndex ? `/videos/ep${preset.videoEp}_turn${turnIndex}.mp4` : null;

    return {
      locationTag: preset.locationTag,
      cameraRig: preset.cameraRig,
      videoSrc: turnVideo || `/videos/ep${preset.videoEp}.mp4`,
      hasAuthenticVideo,
      themeColor: preset.themeColor,
      accentGlow: preset.accentGlow,
      roleDescription: preset.defaultRole,
      atmosphereBadge: preset.atmosphereBadge,
      genreEmoji: preset.genreEmoji,
    };
  }

  // 2. Fallback to resilient cyclic baseline (ensures 100% backward compatibility)
  const cycleEp = Math.max(1, ((Math.abs(episodeNumber) - 1) % TOTAL_PRODUCED) + 1);
  const turnVideo = turnIndex ? `/videos/ep${cycleEp}_turn${turnIndex}.mp4` : null;

  switch (cycleEp) {
    case 1:
      return {
        locationTag: 'MANHATTAN PEARSON HARDMAN • 50F CORNER SUITE',
        cameraRig: 'ARRI ALEXA 35 • ANAMORPHIC 50MM T1.9',
        videoSrc: turnVideo || '/videos/ep1.mp4',
        hasAuthenticVideo,
        themeColor: 'from-cyan-900/40 via-blue-950/60 to-zinc-950',
        accentGlow: 'text-cyan-400 border-cyan-500/40',
        roleDescription: 'Senior Partner • Pearson Hardman',
        atmosphereBadge: '🌙 21:45 EST • LATE NIGHT',
        genreEmoji: '⚖️',
      };
    case 2:
      return {
        locationTag: 'PALO ALTO SAND HILL ROAD • SEQUOIA BOARDROOM',
        cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME PRIME',
        videoSrc: turnVideo || '/videos/ep2.mp4',
        hasAuthenticVideo,
        themeColor: 'from-emerald-900/40 via-teal-950/60 to-zinc-950',
        accentGlow: 'text-emerald-400 border-emerald-500/40',
        roleDescription: 'Founding Partner • Horizon Ventures',
        atmosphereBadge: '☀️ 14:15 PST • SEED CLOSING',
        genreEmoji: '🚀',
      };
    case 3:
      return {
        locationTag: 'HUDSON YARDS WAYSTAR • 45F EXECUTIVE PENTHOUSE',
        cameraRig: 'PANAVISION DXL2 • PRIMO 70',
        videoSrc: turnVideo || '/videos/ep3.mp4',
        hasAuthenticVideo,
        themeColor: 'from-amber-900/40 via-orange-950/60 to-zinc-950',
        accentGlow: 'text-amber-400 border-amber-500/40',
        roleDescription: 'Chief Financial Officer • Global Media',
        atmosphereBadge: '🌅 18:30 EST • SUNSET CRISIS',
        genreEmoji: '🏢',
      };
    case 4:
      return {
        locationTag: 'SEATTLE GRACE HOSPITAL • CHIEF SURGEON SUITE',
        cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
        videoSrc: turnVideo || '/videos/ep4.mp4',
        hasAuthenticVideo,
        themeColor: 'from-teal-900/40 via-cyan-950/60 to-zinc-950',
        accentGlow: 'text-teal-400 border-teal-500/40',
        roleDescription: 'Chief of Surgery • Trauma Unit',
        atmosphereBadge: '🚨 03:12 PST • EMERGENCY TRAUMA',
        genreEmoji: '🏥',
      };
    case 5:
      return {
        locationTag: 'SOHO SKYLIGHT LOUNGE • PRIVATE ROOFTOP CABANA',
        cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
        videoSrc: turnVideo || '/videos/ep5.mp4',
        hasAuthenticVideo,
        themeColor: 'from-fuchsia-900/40 via-purple-950/60 to-zinc-950',
        accentGlow: 'text-fuchsia-400 border-fuchsia-500/40',
        roleDescription: 'Julian Vance • Lead Art Curator',
        atmosphereBadge: '🍸 22:30 EST • SOHO TWILIGHT',
        genreEmoji: '🥂',
      };
    case 6:
      return {
        locationTag: 'WALL STREET FINANCIAL TOWER • WAR ROOM',
        cameraRig: 'ARRI ALEXA LF • MASTER ANAMORPHIC',
        videoSrc: turnVideo || '/videos/ep6.mp4',
        hasAuthenticVideo,
        themeColor: 'from-rose-900/40 via-red-950/60 to-zinc-950',
        accentGlow: 'text-rose-400 border-rose-500/40',
        roleDescription: 'Activist Hedge Fund Principal • M&A',
        atmosphereBadge: '⚡ 02:45 EST • MIDNIGHT TAKEOVER',
        genreEmoji: '📈',
      };
    case 7:
      return {
        locationTag: 'MOSCONE WEST KEYNOTE STAGE • YC DEMO DAY',
        cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
        videoSrc: turnVideo || '/videos/ep7.mp4',
        hasAuthenticVideo,
        themeColor: 'from-violet-900/40 via-indigo-950/60 to-zinc-950',
        accentGlow: 'text-violet-400 border-violet-500/40',
        roleDescription: 'Managing Director • Y Combinator',
        atmosphereBadge: '🚀 11:00 PST • KEYNOTE STAGE',
        genreEmoji: '💻',
      };
    case 8:
    default:
      return {
        locationTag: 'QUEENS SAFE HOUSE • INTERROGATION CELL B',
        cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
        videoSrc: turnVideo || '/videos/ep8.mp4',
        hasAuthenticVideo,
        themeColor: 'from-blue-950/60 via-slate-950/80 to-zinc-950',
        accentGlow: 'text-sky-400 border-sky-500/40',
        roleDescription: 'Agent Miller • FBI Lead Investigator',
        atmosphereBadge: '🚨 01:30 EST • LATE NIGHT INTERROGATION',
        genreEmoji: '🔍',
      };
  }
};
