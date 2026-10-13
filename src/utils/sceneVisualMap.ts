export interface SceneVisualConfig {
  locationTag: string;
  cameraRig: string;
  videoSrc: string;
  themeColor: string;
  accentGlow: string;
  roleDescription: string;
  atmosphereBadge: string;
}

export const getSceneVisualConfig = (episodeNumber: number, turnIndex?: number): SceneVisualConfig => {
  const cycleEp = Math.max(1, ((Math.abs(episodeNumber) - 1) % 7) + 1);
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
        roleDescription: 'Fintech Founder • First Date',
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
    default:
      return {
        locationTag: 'MOSCONE WEST KEYNOTE STAGE • YC DEMO DAY',
        cameraRig: 'RED MONSTRO 8K • ANAMORPHIC ZOOM',
        videoSrc: turnVideo || '/videos/ep7.mp4',
        themeColor: 'from-violet-900/40 via-indigo-950/60 to-zinc-950',
        accentGlow: 'text-violet-400 border-violet-500/40',
        roleDescription: 'Managing Director • Y Combinator',
        atmosphereBadge: '🚀 11:00 PST • KEYNOTE STAGE',
      };
  }
};

