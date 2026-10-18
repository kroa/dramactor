export interface SceneVisualConfig {
  locationTag: string;
  cameraRig: string;
  videoSrc: string;
  themeColor: string;
  accentGlow: string;
  roleDescription: string;
  atmosphereBadge: string;
}

interface GenreVisualPreset {
  videoEp: number;
  locationTag: string;
  cameraRig: string;
  themeColor: string;
  accentGlow: string;
  defaultRole: string;
  atmosphereBadge: string;
}

const GENRE_VISUAL_PRESETS: Record<string, GenreVisualPreset> = {
  // 1. Legal / Patent / Compliance
  'Legal Drama': {
    videoEp: 1,
    locationTag: 'MANHATTAN PEARSON HARDMAN • 50F CORNER SUITE',
    cameraRig: 'ARRI ALEXA 35 • ANAMORPHIC 50MM T1.9',
    themeColor: 'from-cyan-900/40 via-blue-950/60 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Senior Partner • Pearson Hardman',
    atmosphereBadge: '🌙 21:45 EST • LATE NIGHT',
  },
  'Biotech Patent War': {
    videoEp: 1,
    locationTag: 'FEDERAL DISTRICT COURT • PATENT LITIGATION CHAMBER',
    cameraRig: 'ARRI ALEXA 35 • MASTER PRIME 40MM',
    themeColor: 'from-cyan-950/60 via-slate-900/40 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Lead Trial Counsel • Biotech IP',
    atmosphereBadge: '⚖️ 10:15 EST • PRE-TRIAL HEARING',
  },
  'Corporate Compliance': {
    videoEp: 1,
    locationTag: 'DOJ SPECIAL INVESTIGATION • INTERROGATION RM 4',
    cameraRig: 'ARRI ALEXA 35 • ANAMORPHIC 50MM',
    themeColor: 'from-blue-950/60 via-slate-900/50 to-zinc-950',
    accentGlow: 'text-blue-400 border-blue-500/40',
    defaultRole: 'Chief Compliance Officer & Counsel',
    atmosphereBadge: '📋 16:30 EST • DEPOSITION CALL',
  },

  // 2. Silicon Valley / Tech / AI / Venture
  'Silicon Valley Startup': {
    videoEp: 2,
    locationTag: 'PALO ALTO SAND HILL ROAD • SEQUOIA BOARDROOM',
    cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME PRIME',
    themeColor: 'from-emerald-900/40 via-teal-950/60 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Founding Partner • Horizon Ventures',
    atmosphereBadge: '☀️ 14:15 PST • SEED CLOSING',
  },
  'AI Ethics & Singularity': {
    videoEp: 2,
    locationTag: 'SAN FRANCISCO MISSION BAY • AI RESEARCH CORE',
    cameraRig: 'RED V-RAPTOR 8K • LEICA THALIA 35MM',
    themeColor: 'from-teal-950/60 via-emerald-900/40 to-zinc-950',
    accentGlow: 'text-emerald-400 border-emerald-500/40',
    defaultRole: 'Chief AI Scientist • Neural Systems',
    atmosphereBadge: '⚡ 23:50 PST • ALIGNMENT AUDIT',
  },
  'Space Tech & Commercial Launch': {
    videoEp: 2,
    locationTag: 'HAWTHORNE LAUNCH CONTROL • ORBITAL COMMAND',
    cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME',
    themeColor: 'from-indigo-950/60 via-teal-950/40 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Mission Director • Commercial Aerospace',
    atmosphereBadge: '🚀 T-MINUS 12 MIN • COUNTDOWN',
  },

  // 3. Corporate Empire / Executive / Luxury
  'Corporate Empire & M&A': {
    videoEp: 3,
    locationTag: 'HUDSON YARDS WAYSTAR • 45F EXECUTIVE PENTHOUSE',
    cameraRig: 'PANAVISION DXL2 • PRIMO 70',
    themeColor: 'from-amber-900/40 via-orange-950/60 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Chief Financial Officer • Global Media',
    atmosphereBadge: '🌅 18:30 EST • SUNSET CRISIS',
  },
  'Luxury Real Estate': {
    videoEp: 3,
    locationTag: 'TRIBECA PENTHOUSE • 56 LEONARD SKY SALON',
    cameraRig: 'PANAVISION DXL2 • PRIMO 70',
    themeColor: 'from-amber-950/50 via-yellow-950/40 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Managing Broker • Ultra-Luxury Estates',
    atmosphereBadge: '🍸 17:45 EST • EXCLUSIVE SHOWING',
  },
  '5-Star Hotel Hospitality': {
    videoEp: 3,
    locationTag: 'THE PLAZA NEW YORK • PRESIDENTIAL SUITE',
    cameraRig: 'PANAVISION DXL2 • COOKE S7/i',
    themeColor: 'from-amber-900/40 via-zinc-950 to-zinc-950',
    accentGlow: 'text-amber-300 border-amber-400/40',
    defaultRole: 'General Manager • Grand Luxury Palace',
    atmosphereBadge: '🛎️ 20:00 EST • VIP INSPECTION',
  },
  'Family Dynasty Succession': {
    videoEp: 3,
    locationTag: 'WAYSTAR ROYCO HELIPAD • BOARD CHAIR OFFICE',
    cameraRig: 'PANAVISION DXL2 • PRIMO 70',
    themeColor: 'from-amber-950/60 via-orange-950/40 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Board Chairman & Controlling Heir',
    atmosphereBadge: '🌆 19:15 EST • SUCCESSION VOTE',
  },

  // 4. Emergency Medicine / Hospital / Trauma
  'Emergency Medicine': {
    videoEp: 4,
    locationTag: 'SEATTLE GRACE HOSPITAL • CHIEF SURGEON SUITE',
    cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
    themeColor: 'from-teal-900/40 via-cyan-950/60 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Chief of Surgery • Trauma Unit',
    atmosphereBadge: '🚨 03:12 PST • EMERGENCY TRAUMA',
  },
  'Neurosurgery Dilemma': {
    videoEp: 4,
    locationTag: 'BOSTON GENERAL • NEUROSURGICAL ICU',
    cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
    themeColor: 'from-cyan-950/60 via-teal-900/40 to-zinc-950',
    accentGlow: 'text-cyan-400 border-cyan-500/40',
    defaultRole: 'Chair of Neurosurgery • Trauma OR',
    atmosphereBadge: '🔬 02:45 EST • EMERGENCY CRANIOTOMY',
  },
  'Pandemic Containment': {
    videoEp: 4,
    locationTag: 'CDC ATLANTA • BSL-4 LEVEL QUARANTINE',
    cameraRig: 'SONY VENICE 2 • ZEISS SUPREME',
    themeColor: 'from-teal-950/60 via-emerald-950/40 to-zinc-950',
    accentGlow: 'text-teal-400 border-teal-500/40',
    defaultRole: 'Lead Epidemiologist • Task Force Commander',
    atmosphereBadge: '☣️ 05:20 EST • OUTBREAK PROTOCOL',
  },

  // 5. Romance / Nightlife / Cuisine / Fashion / Fine Art
  'Manhattan Romance & High Society': {
    videoEp: 5,
    locationTag: 'SOHO SKYLIGHT LOUNGE • PRIVATE ROOFTOP CABANA',
    cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
    themeColor: 'from-fuchsia-900/40 via-purple-950/60 to-zinc-950',
    accentGlow: 'text-fuchsia-400 border-fuchsia-500/40',
    defaultRole: 'Julian Vance • Lead Art Curator',
    atmosphereBadge: '🍸 22:30 EST • SOHO TWILIGHT',
  },
  'Michelin Culinary': {
    videoEp: 5,
    locationTag: 'MANHATTAN LE BERNARDIN • 3-STAR SERVICE KITCHEN',
    cameraRig: 'ARRI MINI LF • LEICA SUMMILUX 35MM',
    themeColor: 'from-rose-950/50 via-amber-950/40 to-zinc-950',
    accentGlow: 'text-rose-400 border-rose-500/40',
    defaultRole: 'Head Chef • Executive Culinary Director',
    atmosphereBadge: '🔥 19:45 EST • DINNER SERVICE RUSH',
  },
  'Haute Couture Fashion': {
    videoEp: 5,
    locationTag: 'PARIS FASHION WEEK • GRAND PALAIS BACKSTAGE',
    cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
    themeColor: 'from-fuchsia-950/50 via-pink-950/40 to-zinc-950',
    accentGlow: 'text-fuchsia-300 border-fuchsia-400/40',
    defaultRole: 'Creative Director • Haute Couture House',
    atmosphereBadge: '✨ 20:15 CET • RUNWAY CALL',
  },
  'Fine Art Auction & Heist': {
    videoEp: 5,
    locationTag: 'SOTHEBY’S MANHATTAN • HIGH-VALUE VAULT ROOM',
    cameraRig: 'ARRI MINI LF • COOKE S7/i',
    themeColor: 'from-purple-950/50 via-indigo-950/40 to-zinc-950',
    accentGlow: 'text-purple-400 border-purple-500/40',
    defaultRole: 'Senior Art Specialist & Appraiser',
    atmosphereBadge: '🎨 19:00 EST • EVENING SALE',
  },

  // 6. Wall Street / Hedge Fund / Trading
  'Wall Street Hedge Fund': {
    videoEp: 6,
    locationTag: 'WALL STREET FINANCIAL TOWER • WAR ROOM',
    cameraRig: 'ARRI ALEXA LF • MASTER ANAMORPHIC',
    themeColor: 'from-rose-900/40 via-red-950/60 to-zinc-950',
    accentGlow: 'text-rose-400 border-rose-500/40',
    defaultRole: 'Activist Hedge Fund Principal • M&A',
    atmosphereBadge: '⚡ 02:45 EST • MIDNIGHT TAKEOVER',
  },
  'Crypto High Frequency Trading': {
    videoEp: 6,
    locationTag: 'CHICAGO BOARD OF TRADE • LOW-LATENCY TRADING DESK',
    cameraRig: 'ARRI ALEXA LF • ZEISS MASTER PRIME',
    themeColor: 'from-red-950/60 via-amber-950/40 to-zinc-950',
    accentGlow: 'text-amber-400 border-amber-500/40',
    defaultRole: 'Chief Quant Strategist • HFT Desk',
    atmosphereBadge: '📈 04:00 CST • ASIAN MARKET OPEN',
  },
  'Sovereign Wealth Fund': {
    videoEp: 6,
    locationTag: 'ZURICH PRIVATE BANKING SUITE • VAULT OFFICE',
    cameraRig: 'ARRI ALEXA LF • COOKE S7/i',
    themeColor: 'from-rose-950/60 via-zinc-950 to-zinc-950',
    accentGlow: 'text-rose-400 border-rose-500/40',
    defaultRole: 'Managing Director • Sovereign Allocations',
    atmosphereBadge: '💼 15:30 CET • TRILLION ALLOCATION',
  },

  // 7. Media / PR / Sports / Keynote / Entertainment
  'Sports Agency & Free Agency': {
    videoEp: 7,
    locationTag: 'BEVERLY HILLS CAA HQ • WAR ROOM SUITE',
    cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
    themeColor: 'from-violet-900/40 via-indigo-950/60 to-zinc-950',
    accentGlow: 'text-violet-400 border-violet-500/40',
    defaultRole: 'Managing Director • Elite Sports Division',
    atmosphereBadge: '⚾ 23:55 EST • DEADLINE LOCKOUT',
  },
  'Hollywood Talent Agency': {
    videoEp: 7,
    locationTag: 'CENTURY CITY TALENT AGENCY • CORNER CORRIDOR',
    cameraRig: 'RED MONSTRO 8K • ZEISS SUPREME',
    themeColor: 'from-indigo-950/50 via-purple-950/40 to-zinc-950',
    accentGlow: 'text-indigo-400 border-indigo-500/40',
    defaultRole: 'Senior Managing Partner • A-List Division',
    atmosphereBadge: '🎬 16:30 PST • PACKAGING CALL',
  },
  'Crisis PR Management': {
    videoEp: 7,
    locationTag: 'ROCKEFELLER CENTER • STRATEGIC CRISIS SUITE',
    cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
    themeColor: 'from-violet-950/50 via-blue-950/40 to-zinc-950',
    accentGlow: 'text-violet-400 border-violet-500/40',
    defaultRole: 'Principal Crisis Strategist • Media War',
    atmosphereBadge: '📣 07:15 EST • BREAKING NEWS SPIN',
  },
  'Investigative Journalism': {
    videoEp: 7,
    locationTag: 'THE WASHINGTON POST • DEEP SOURCE ARCHIVE',
    cameraRig: 'RED MONSTRO 8K • LEICA THALIA',
    themeColor: 'from-indigo-900/40 via-zinc-950 to-zinc-950',
    accentGlow: 'text-indigo-300 border-indigo-400/40',
    defaultRole: 'Investigative Editor • National Desk',
    atmosphereBadge: '🗞️ 01:20 EST • FRONT PAGE DEADLINE',
  },

  // 8. Government / Defense / Intelligence / Crisis Command
  'White House Politics': {
    videoEp: 8,
    locationTag: 'THE WHITE HOUSE SITUATION ROOM • LEVEL -2 BUNKER',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM T1.3',
    themeColor: 'from-slate-950 via-zinc-950 to-red-950/40',
    accentGlow: 'text-red-400 border-red-500/40',
    defaultRole: 'General Hayes • Chairman of Joint Chiefs',
    atmosphereBadge: '🚨 00:04 EST • DEFCON 2 ALERT',
  },
  'FBI Criminal Profiling': {
    videoEp: 8,
    locationTag: 'QUEENS SAFE HOUSE • INTERROGATION CELL B',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-blue-950/60 via-slate-950/80 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Agent Miller • FBI Lead Investigator',
    atmosphereBadge: '🚨 01:30 EST • LATE NIGHT INTERROGATION',
  },
  'CIA Covert Espionage': {
    videoEp: 8,
    locationTag: 'LANGLEY CIA HEADQUARTERS • SECURE OPERATIONS VAULT',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-slate-950 via-sky-950/40 to-zinc-950',
    accentGlow: 'text-sky-400 border-sky-500/40',
    defaultRole: 'Director of Clandestine Operations • CIA',
    atmosphereBadge: '🛰️ 03:40 EST • BLACK OPS COMS',
  },
  'Aviation Cockpit Emergency': {
    videoEp: 8,
    locationTag: 'FLIGHT 842 COCKPIT • FL350 EMERGENCY DESCENT',
    cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
    themeColor: 'from-red-950/50 via-slate-950 to-zinc-950',
    accentGlow: 'text-red-400 border-red-500/40',
    defaultRole: 'Captain Reynolds • Pilot in Command',
    atmosphereBadge: '⚠️ 35,000 FT • MAYDAY DECLARED',
  },
};

export const getSceneVisualConfig = (
  episodeNumber: number,
  turnIndex?: number,
  episode?: { genre?: string; title?: string },
  _turn?: { speaker?: string; avatarEmoji?: string }
): SceneVisualConfig => {
  const TOTAL_PRODUCED = 8;

  // 1. If explicit genre preset exists, use high-fidelity scenario mapping
  if (episode?.genre && GENRE_VISUAL_PRESETS[episode.genre]) {
    const preset = GENRE_VISUAL_PRESETS[episode.genre];
    const turnVideo = turnIndex ? `/videos/ep${preset.videoEp}_turn${turnIndex}.mp4` : null;

    return {
      locationTag: preset.locationTag,
      cameraRig: preset.cameraRig,
      videoSrc: turnVideo || `/videos/ep${preset.videoEp}.mp4`,
      themeColor: preset.themeColor,
      accentGlow: preset.accentGlow,
      roleDescription: preset.defaultRole,
      atmosphereBadge: preset.atmosphereBadge,
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
        themeColor: 'from-cyan-900/40 via-blue-950/60 to-zinc-950',
        accentGlow: 'text-cyan-400 border-cyan-500/40',
        roleDescription: 'Senior Partner • Pearson Hardman',
        atmosphereBadge: '🌙 21:45 EST • LATE NIGHT',
      };
    case 2:
      return {
        locationTag: 'PALO ALTO SAND HILL ROAD • SEQUOIA BOARDROOM',
        cameraRig: 'RED V-RAPTOR 8K • ZEISS SUPREME PRIME',
        videoSrc: turnVideo || '/videos/ep2.mp4',
        themeColor: 'from-emerald-900/40 via-teal-950/60 to-zinc-950',
        accentGlow: 'text-emerald-400 border-emerald-500/40',
        roleDescription: 'Founding Partner • Horizon Ventures',
        atmosphereBadge: '☀️ 14:15 PST • SEED CLOSING',
      };
    case 3:
      return {
        locationTag: 'HUDSON YARDS WAYSTAR • 45F EXECUTIVE PENTHOUSE',
        cameraRig: 'PANAVISION DXL2 • PRIMO 70',
        videoSrc: turnVideo || '/videos/ep3.mp4',
        themeColor: 'from-amber-900/40 via-orange-950/60 to-zinc-950',
        accentGlow: 'text-amber-400 border-amber-500/40',
        roleDescription: 'Chief Financial Officer • Global Media',
        atmosphereBadge: '🌅 18:30 EST • SUNSET CRISIS',
      };
    case 4:
      return {
        locationTag: 'SEATTLE GRACE HOSPITAL • CHIEF SURGEON SUITE',
        cameraRig: 'SONY VENICE 2 • COOKE ANAMORPHIC /i',
        videoSrc: turnVideo || '/videos/ep4.mp4',
        themeColor: 'from-teal-900/40 via-cyan-950/60 to-zinc-950',
        accentGlow: 'text-teal-400 border-teal-500/40',
        roleDescription: 'Chief of Surgery • Trauma Unit',
        atmosphereBadge: '🚨 03:12 PST • EMERGENCY TRAUMA',
      };
    case 5:
      return {
        locationTag: 'SOHO SKYLIGHT LOUNGE • PRIVATE ROOFTOP CABANA',
        cameraRig: 'ARRI MINI LF • LEICA NOCTILUX 50MM',
        videoSrc: turnVideo || '/videos/ep5.mp4',
        themeColor: 'from-fuchsia-900/40 via-purple-950/60 to-zinc-950',
        accentGlow: 'text-fuchsia-400 border-fuchsia-500/40',
        roleDescription: 'Julian Vance • Lead Art Curator',
        atmosphereBadge: '🍸 22:30 EST • SOHO TWILIGHT',
      };
    case 6:
      return {
        locationTag: 'WALL STREET FINANCIAL TOWER • WAR ROOM',
        cameraRig: 'ARRI ALEXA LF • MASTER ANAMORPHIC',
        videoSrc: turnVideo || '/videos/ep6.mp4',
        themeColor: 'from-rose-900/40 via-red-950/60 to-zinc-950',
        accentGlow: 'text-rose-400 border-rose-500/40',
        roleDescription: 'Activist Hedge Fund Principal • M&A',
        atmosphereBadge: '⚡ 02:45 EST • MIDNIGHT TAKEOVER',
      };
    case 7:
      return {
        locationTag: 'MOSCONE WEST KEYNOTE STAGE • YC DEMO DAY',
        cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
        videoSrc: turnVideo || '/videos/ep7.mp4',
        themeColor: 'from-violet-900/40 via-indigo-950/60 to-zinc-950',
        accentGlow: 'text-violet-400 border-violet-500/40',
        roleDescription: 'Managing Director • Y Combinator',
        atmosphereBadge: '🚀 11:00 PST • KEYNOTE STAGE',
      };
    case 8:
    default:
      return {
        locationTag: 'QUEENS SAFE HOUSE • INTERROGATION CELL B',
        cameraRig: 'ARRI ALEXA MINI • ZEISS MASTER PRIME 35MM',
        videoSrc: turnVideo || '/videos/ep8.mp4',
        themeColor: 'from-blue-950/60 via-slate-950/80 to-zinc-950',
        accentGlow: 'text-sky-400 border-sky-500/40',
        roleDescription: 'Agent Miller • FBI Lead Investigator',
        atmosphereBadge: '🚨 01:30 EST • LATE NIGHT INTERROGATION',
      };
  }
};

