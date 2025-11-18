"""Constants used across the application"""

# Intent types
INTENT_TYPES = {
    'SUMMARY': 'SUMMARY',
    'COMPARE': 'COMPARE',
    'QNA': 'QNA',
    'UNKNOWN': 'UNKNOWN'
}

# Intent color indicators (for UI display)
INTENT_COLORS = {
    "SUMMARY": "",
    "COMPARE": "",
    "QNA": "",
    "UNKNOWN": ""
}

# LLM Providers
LLM_PROVIDERS = {
    'OPENAI': 'openai',
    'AZURE': 'azure'
}

# Default models
DEFAULT_MODELS = {
    'OPENAI': 'gpt-4o-mini',
    'AZURE': 'gpt-4'
}
