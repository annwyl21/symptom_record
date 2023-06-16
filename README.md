# Symptom Logger Application

This application facilitates the logging of symptoms in free text, such as headaches or hip pain, over time. The accumulated symptom data can be concisely summarised, using a [metaprompt](./application/metaprompt.py) by AI for healthcare professionals or VETs. I used the **open ai playground** to experiment with 2 AI models; text-curie-001 and text-davinci-003, and develop my prompt. It was a really useful tool to compare the AI tools aswell as manipulating my prompt.

## Purpose

The tool addresses the need for busy individuals, like parents or pet owners, to accurately record and convey symptoms during brief medical consultations. As AI increasingly aids in diagnosis, precise symptom reporting becomes paramount. This tool offers a solution to this challenge.

### Run
- Install the requirements
```bash
pip install -r requirements.txt
```
- Run the app.py file to start the site locally
```bash
python -m flask run
```

## Challenges Overcome
- When experimenting with the text-curie-001 AI model, I encountered a potential problem. The model returned a superior summary but it did not return what I had asked for and it made an inference about the symptoms which, while accurate, is unacceptable as that inference should be made by a qualified doctor or medical AI tool and never by a symptom sumarizer. The text-davinci-003 AI model was superior in that it completed the task in a wholly acceptable manner.
- Developing the model was enjoyable and took time, I had to change the intention text in order to narrow the response appropriately, something I had not anticipated. My original intention text was *This summary is intended to be read by a doctor or a VET in order to make a diagnosis, an onward referral or prescribe treatment from these symptoms.* but that was eventually modified to *This concise summary is intended to be spoken by a person trying to convey their symptoms using easy to understand language without clauses.*.
- Getting the model to handle time also required some thought and I added the specific text *with a focus on change over time in symptoms, eg which are worsening or improving and whether the person experiences pain every day* to my prompt in order to get the model to comment on symptoms over time.

___
### Key Considerations for App Development
- **Accuracy (Meta-prompt)**: 
    Current AI isn't infallible in summarizing reports, making knowledge of meta-prompts crucial for producing truthful and precise summaries.
- **User Engagement (UX)**: 
    Ensuring user-friendly and secure interfaces is essential to encourage comprehensive symptom reporting, thus enhancing user engagement and trust.
- **Data Privacy and Security Enforcement**: 
    Considering the sensitivity of health data, adherence to privacy regulations such as GDPR, HIPAA, among others, is critical. The deployment of robust encryption techniques and the following of data security best practices are required.
- **Accessibility Optimization**: 
    The app must cater to diverse user capabilities. This can be achieved by integrating accessible designs (including large text options and colorblind-friendly palettes) and supporting voice inputs.
- **Multilingual Support Expansion**: 
    To facilitate effective communication, the tool should also accommodate multiple languages.

### Limitiations
- **No Diagnostic Role**: This application merely facilitates patient-doctor communication and does not provide diagnoses or generate symptom-related information.
- **Non-medical Model**: The tool uses a language summarizing model, not medically trained, implying any medical expertise should come from the healthcare provider, not the application.
- **No Error Propagation**: Despite potential integration with medically trained AI, the tool aims to ensure clear patient-doctor communication, averting any risk of miscommunication akin to a 'Chinese Whispers' scenario.
