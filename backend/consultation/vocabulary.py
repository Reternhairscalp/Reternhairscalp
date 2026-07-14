"""Normalized terms used by deterministic consultation extraction."""

GENDER_KEYWORDS: dict[str, tuple[str, ...]] = {
    "female": ("female", "woman", "lady", "girl", "mother", "mum", "mom"),
    "male": ("male", "man", "gentleman", "boy", "father", "dad"),
}

SCALP_PROBLEMS: dict[str, tuple[str, ...]] = {
    "oily_scalp": ("oily scalp", "oily", "greasy scalp", "greasy"),
    "dandruff": ("dandruff", "flaky scalp", "scalp flakes", "flaking"),
    "sensitive_scalp": ("sensitive scalp", "scalp sensitivity", "sensitive"),
    "dry_scalp": ("dry scalp", "scalp dryness"),
    "itchy_scalp": ("itchy scalp", "scalp itch", "itching", "itchy"),
    "scalp_redness": ("scalp redness", "red scalp", "redness"),
    "scalp_inflammation": ("scalp inflammation", "inflamed scalp", "inflammation"),
}

HAIR_LOSS_SYMPTOMS: dict[str, tuple[str, ...]] = {
    "hair_loss": ("hair loss", "losing hair"),
    "hair_fall": ("hair fall", "hair falling", "falling hair"),
    "shedding": ("hair shedding", "shedding hair", "shedding"),
    "thinning": ("hair thinning", "thinning hair", "thin hair", "thinning"),
    "bald_spots": ("bald spot", "bald spots", "patchy hair loss"),
    "receding_hairline": ("receding hairline", "hairline receding"),
    "balding": ("balding",),
}

NUMBER_WORDS: dict[str, str] = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8",
    "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
}

SEVERITY_TERMS: dict[str, tuple[str, ...]] = {
    "mild": ("mild", "slight", "a little", "minor"),
    "moderate": ("moderate", "noticeable", "getting worse"),
    "severe": ("severe", "heavy", "a lot", "extreme", "in clumps", "rapid"),
}

RED_FLAG_TERMS: dict[str, tuple[str, ...]] = {
    "sudden_hair_loss": ("sudden hair loss", "rapid hair loss", "suddenly losing"),
    "bleeding": ("bleeding scalp", "scalp bleeding"),
    "open_wound": ("open wound", "open sore", "scalp wound"),
    "possible_infection": ("pus", "infected scalp", "scalp infection"),
    "severe_pain": ("severe pain", "intense pain"),
    "fever": ("fever",),
}
