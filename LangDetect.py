
import streamlit as st
from langdetect import detect_langs

# Function to get the full name of a language from its ISO code
def get_language_name(code):
    # You can define a dictionary to map ISO language codes to full names
    language_names = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'nl': 'Dutch',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'zh': 'Chinese',
    'ar': 'Arabic',
    'ko': 'Korean',
    'tr': 'Turkish',
    'sv': 'Swedish',
    'da': 'Danish',
    'no': 'Norwegian',
    'fi': 'Finnish',
    'el': 'Greek',
    'pl': 'Polish',
    'hu': 'Hungarian',
    'cs': 'Czech',
    'th': 'Thai',
    'hi': 'Hindi',
    'he': 'Hebrew',
    'id': 'Indonesian',
    'ms': 'Malay',
    'vi': 'Vietnamese',
    'bg': 'Bulgarian',
    'ro': 'Romanian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'uk': 'Ukrainian',
    'ca': 'Catalan',
    'hr': 'Croatian',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'et': 'Estonian',
    'sr': 'Serbian',
    'sq': 'Albanian',
    'mk': 'Macedonian',
    'bs': 'Bosnian',
    'cy': 'Welsh',
    'eu': 'Basque',
    'gl': 'Galician',
    'ga': 'Irish',
    'is': 'Icelandic',
    'lb': 'Luxembourgish',
    'mt': 'Maltese',
    'fa': 'Persian',
    'ur': 'Urdu'
}

    return language_names.get(code, "Unknown")

# Streamlit UI
st.title("Language Detection App")
text = st.text_input("Enter any text:")
if text:
    detected_languages = detect_langs(text)
    st.write("Detected Language(s):")
    for language in detected_languages:
        language_name = get_language_name(language.lang)
        st.write(f"{language_name} ({language.lang}) with probability {language.prob}")
