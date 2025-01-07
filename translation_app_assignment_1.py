import streamlit as st
from transformers import pipeline
from libretranslatepy import LibreTranslateAPI

# Supported Languages
LANGUAGES = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "zh": "Chinese (Simplified)",
    "hi": "Hindi",
    "ar": "Arabic",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "sv": "Swedish",
    "da": "Danish",
    "no": "Norwegian",
    "fi": "Finnish",
    "el": "Greek",
    "tr": "Turkish",
    "pl": "Polish",
    "he": "Hebrew",
    "th": "Thai",
    "cs": "Czech",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "id": "Indonesian",
    "ro": "Romanian",
    "hu": "Hungarian",
    "bg": "Bulgarian",
    "fa": "Persian",
    "mr": "Marathi",
}

# Cache the translation pipelines
@st.cache_resource
def load_huggingface_pipeline(src, tgt, model_name):
    try:
        return pipeline("translation", model=model_name)
    except Exception:
        return None

# Translation Models
def translate_with_helsinki(text, src, tgt):
    model_name = f"Helsinki-NLP/opus-mt-{src}-{tgt}"
    translator = load_huggingface_pipeline(src, tgt, model_name)
    if translator:
        result = translator(text, max_length=512)
        return result[0]["translation_text"]
    else:
        return "Model not available for this language pair."

def translate_with_m2m100(text, src, tgt):
    model_name = "facebook/m2m100_418M"
    translator = load_huggingface_pipeline("multilingual", "multilingual", model_name)
    if translator:
        result = translator(text, src_lang=src, tgt_lang=tgt)
        return result[0]["translation_text"]
    else:
        return "Model not available for this language pair."


# Streamlit App
st.title("Multi-Model Translation Tool")
st.write("Translate text using different free models and choose between them.")

# Select Model
model_choice = st.selectbox(
    "Choose Translation Model",
    ["Helsinki-NLP (OPUS-MT)", "Facebook M2M-100",]
)

# User selects source and target languages
source_lang = st.selectbox("Select Source Language", list(LANGUAGES.keys()), format_func=lambda x: LANGUAGES[x])
target_lang = st.selectbox(
    "Select Target Language",
    [lang for lang in LANGUAGES if lang != source_lang],
    format_func=lambda x: LANGUAGES[x],
)

# User inputs text for translation
text = st.text_area("Enter the text to translate", placeholder="Type your text here...")

# Perform translation
if st.button("Translate"):
    if not text.strip():
        st.error("Please enter text to translate.")
    else:
        st.spinner("Translating...")
        if model_choice == "Helsinki-NLP (OPUS-MT)":
            translated_text = translate_with_helsinki(text, source_lang, target_lang)
        elif model_choice == "Facebook M2M-100":
            translated_text = translate_with_m2m100(text, source_lang, target_lang)
        else:
            translated_text = "Invalid model choice."

        st.success("Translation completed!")
        st.text_area("Translated Text", translated_text, height=200)

# Sidebar for language reference
st.sidebar.title("Supported Languages")
st.sidebar.write("This tool supports translations for the following languages:")
for lang_code, lang_name in LANGUAGES.items():
    st.sidebar.write(f"{lang_code}: {lang_name}")
