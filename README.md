### `README.md`

# Multi-Model Translation Tool

This is a **Streamlit-based Translation Tool** that allows users to translate text between multiple languages using free, open-source models. Users can choose between different translation models like **Helsinki-NLP (OPUS-MT)** and **Facebook M2M-100** for their translations.

---

## Features

- **Multiple Translation Models**:
  - **Helsinki-NLP (OPUS-MT)**: High-quality translation between many language pairs.
  - **Facebook M2M-100**: A multilingual translation model supporting direct translation between 100+ languages.
- **Wide Language Support**:
  - Translate text in languages like English, French, Hindi, Chinese, Russian, Arabic, and many more.
- **User-Friendly Interface**:
  - Select source and target languages from a dropdown.
  - Input text and get translations with the click of a button.
- **Sidebar for Language Reference**:
  - Lists all supported languages for easy reference.

---

## Supported Languages

This tool supports translation between the following languages (and many more):
- English (`en`), French (`fr`), Spanish (`es`), Hindi (`hi`), Chinese (`zh`), Arabic (`ar`), Russian (`ru`), Japanese (`ja`), and many others.

For the complete list, refer to the sidebar in the application.

---

## Requirements

### Python Libraries
To run this tool, the following libraries are required:
- `streamlit`
- `transformers`
- `libretranslatepy`

### Install the Dependencies
Use the following command to install the required libraries:
```bash
pip install streamlit transformers libretranslatepy
```

---

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/PratikMitkar/codealpha_tasks_1.git
cd codealpha_tasks_1
```

### 2. Run the Program
Start the Streamlit app by running:
```bash
streamlit run translation_app_assignment_1.py
```

### 3. Translate Text
- Select the **translation model**.
- Choose the **source language** and the **target language**.
- Enter the text you want to translate in the input box.
- Click the **Translate** button to view the translated text.

---

## How It Works

### Translation Models
1. **Helsinki-NLP (OPUS-MT)**:
   - Translations are performed using pre-trained models available from `Helsinki-NLP/opus-mt-{src}-{tgt}`.
   - Direct language-pair models are used for better accuracy.
2. **Facebook M2M-100**:
   - A multilingual model for direct translation between any pair of 100+ languages.
   - Handles zero-shot translations efficiently.

### Language Selection
- Source and target languages can be chosen from the dropdown menus.
- Only supported language pairs are displayed for user convenience.

### Error Handling
- Checks for empty text input and displays appropriate error messages.
- Ensures valid language pairs and handles unavailable models gracefully.

---

## Customization

### Adding More Translation Models
To integrate additional models:
1. Add the model name to the `model_choice` dropdown:
   ```python
   model_choice = st.selectbox(
       "Choose Translation Model",
       ["Helsinki-NLP (OPUS-MT)", "Facebook M2M-100", "Your Model Here"]
   )
   ```
2. Implement the corresponding function for the model and add it to the button logic.

### Adjusting Language Support
To add or modify supported languages:
1. Update the `LANGUAGES` dictionary:
   ```python
   LANGUAGES = {
       "en": "English",
       "fr": "French",
       # Add new languages here
   }
   ```

---

## Known Issues
- Some language pairs may not be available with the chosen model.
- M2M-100 may have slower performance on resource-constrained systems.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to add new features, improve performance, or expand language support.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Built with [Streamlit](https://streamlit.io/).
- Utilizes [Helsinki-NLP OPUS-MT](https://huggingface.co/Helsinki-NLP) and [Facebook M2M-100](https://huggingface.co/facebook/m2m100_418M).
- Inspired by the growing need for multilingual communication and open-source NLP tools.
