import re
from typing import Optional

WARNINGS = {
    r'\b(hunty|werk|yass|gawd|kont)\b': 'a word which originates with queer AAVE but has been misappropriated.',
    
    # Ableism and Saneism
    r'\b(stupid|stupidity|stupidness|stupider|stupidest)\b': 'ableist language. Some alternatives: pathetic, uninspiring, vapid, obtuse, silly',
    r'\b(crazy|craziness|crazier|craziest|crazies)\b': 'ableist language. Some alternatives are ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable',
    r'\b(insane|insanity|insanest)\b': 'ableist language. Some alternatives: ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable',
    r'\b(idiot|idiots|idiotic|imbecile|imbeciles|moron|morons|moronic|lunatic|lunatics|lunacy)\b': 'ableist language. Some alternatives: uninformed, ignorant, incorrect, wrong',
    r'\b(cretin|midget|spazzed|spazzing|spaz|bonkers)\b': 'ableist language. check out some alternatives! <http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html> (scroll down)',
    r'\b(ree|reee|reeee|reeeee)\b': 'a slur against autistic people',
    r'\b(derp|hurr|durr|hurrdurr)\b': 'ableist language.',
    r'\b(delusional|deluded)\b': 'ableist language. Some alternatives: misguided, misinformed, ignorant',
    r'\b(mad lad|mad lass|madman)\b': 'ableist language. Some alternatives: wild, chaotic, unbelievable, brave, ill-advised',
    r'\b(narcissistic|narcissist)\b': 'ableist language. Some alternatives: self-centred, egotistical, self-absorbed',
    r'\b(narcissistic abuse)\b': 'ableist language which contributes to an already highly-stigmatised mental condition.',

    r'\b(dumb|dumber|dumbing|dumbasses|dumbass)\b': 'ableist language. Some alternatives: silly, foolish, ignorant, uninformed, ridiculous, pathetic, absurd',
    r'\b(lame|lamer|lamest)\b': 'ableist language. Some alternatives: silly, foolish, ridiculous, pathetic, absurd, uncool',
    r'\b(cripple|crippled|crip|crippling)\b': 'ableist language. Some alternatives: broken, not working',
    r'\b(gimp|gimped|gimping)\b': 'ableist language. Some alternatives: nerf, sabotage. If you were talking about the GNU Image Manipulation Program then please ignore this automated message.',
    r'\b(brain-dead|braindead|smallbrain|small-brained|smallbrained|small-brained)\b': 'ableist language. Some alternatives: thoughtless, ill-planned, ridiculous, uninspired',
    r'\b(special needs|special-needs)\b': 'language rejected by the disabled community. Some alternatives: disabled, developmentally disabled, cognitively disabled, accessibility',
    # Racism and xenophobia
    r'\b(gypsy|gipp|gyp|pikey|piky)\b': 'a racial slur against the Romani people.',
    r'\b(somali)\b': 'a racial slur against Somalian people.',
    r'\b(afghani)\b': 'a racial slur against Afghan people.',
    r'\b(eskimo)\b': 'a racial slur rejected by most Inuit and Yupik communities.',
    r'\b(gusano)\b': 'a racial slur for Cubans that fled the Cuban Revolution',
    r'\b(injun|nitchie|neche|neechee|neejee|nitchy|nitchee|nidge|redskin|squaw)\b': 'a racial slur for Native Americans',
    r'\b(kanaka)\b': 'a racial slur for Pacific Islanders',
    r'\b(lubra)\b': 'a racial slur for Australian Aboriginal people',
    r'\b(mick)\b': 'a slur for people of Irish descent',
    r'\b(polack|polak|polock)\b': 'a slur for people of Polish or Slavic origin',
    r'\b(portagee)\b': 'a slur for people of Portugese origin',
    r'\b(russki)\b': 'a slur for people of Russian origin',
    r'\b(paki|pakki|pak)\b': 'a slur against South Asian people',
    r'\b(jap)\b': 'a slur against Japanese people',
    r'\b(kaffir|kaffer|kafir|kaffre|kuffar)\b': 'a racial slur against black people.',

    r'\b(pc master race)\b': 'a phrase with nazi origins. Consider choosing an alternative.',
    
    r'\b(sold down the river)\b': 'a phrase with antiBlack racist origins. Some alternatives are: abandoned, betrayed, backstabbed',
    r'\b(grandfather clause)\b': 'a phrase with antiBlack racist origins. Some alternatives are: legacy clause, pre-existing arrangement',
    r'\b(lynch mob)\b': 'a phrase with antiBlack racist origins. Some alternatives are: angry mob, outcry',
    
    r'\b(on the warpath)\b': 'a phrase with anti-Indigenous racist origins. Some alternatives are: angry, aggressive, belligerent, enraged',
    r'\b(bury the hatchet)\b': 'a phrase with anti-Indigenous racist origins. Some alternatives are: make peace, forgive, let bygones be bygones',

    r'\b(spirit animal)\b': 'a misappropriated Indigenous concept. Some alternatives are: kin, kintype, saying that you relate to that animal, saying that you are that animal',
    r'\b(savage)\b': "a word that has racist roots in colonial violence against indigenous peoples and shouldn't be used. Some alternatives are: ridiculous, absurd, ruthless, brutal, rough, wild.",
    r'\b(pariah)\b': 'a casteist slur. Some alternatives are: outsider, persona non grata, outcast',
    r'\b(illegal immigrant|illegal alien)\b': 'xenophobic phrasing. Some alternatives are: undocumented immigrant, undocumented person ',

 # catchall ableist (No suggestions)
    r'\b(psycho|psychos|psychotic|psychopath|sociopath|sociopathic|maniac|maniacs|demented)\b': 'ableist language. check out some alternatives! <http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html> (scroll down)',
 # server-specific banned topics
    r'\b(natalie wynn|contrapoints)\b': 'a banned topic on this server.',
    r'\b(chrischan|christine weston chandler|chris chan|chris-chan)\b': 'a banned topic on this server.',
    r'\b(lily cade)\b': 'a banned topic on this server.',
}

#GUYS_RESPONSE = """Many people feel excluded when you refer to a group of people as "Guys".
#Some alternatives if you meant to refer to explicitly men: men, dudes
#Some alternatives if you meant to refer to people in general: all, everyone, friends, folks, people"""


def parse_message(text: str) -> Optional[str]:
    for key in WARNINGS:
        m = re.search(key, text, re.IGNORECASE)
        if m:
            return 'gentle reminder: {} is {}'.format(m.group(0), WARNINGS[key])

   # if re.search(r'\b(hey|hi|you)\W+(guys)\b', text, re.IGNORECASE):
      #  return GUYS_RESPONSE

    return None
