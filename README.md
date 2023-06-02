# Symptom Logger Application

This application facilitates the logging of symptoms in free text, such as headaches or hip pain, over time. The accumulated data can be integrated with AI to generate a concise symptom summary for healthcare professionals or VETs.

## [Purpose](./application/templates/index.html)

The tool addresses the need for busy individuals, like parents or pet owners, to accurately record and convey symptoms during brief medical consultations. As AI increasingly aids in diagnosis, precise symptom reporting becomes paramount. This tool offers a solution to this challenge.

### Key Considerations for App Development
- **Accuracy ([Meta-prompt](./application/metaprompt.py))**: 
    Current AI isn't infallible in summarizing reports, making knowledge of meta-prompts crucial for producing truthful and precise summaries.
- **User Engagement (UX)**: 
    Ensuring user-friendly and secure interfaces is essential to encourage comprehensive symptom reporting, thus enhancing user engagement and trust.
- **Data Privacy and Security Enforcement**: 
    Considering the sensitivity of health data, adherence to privacy regulations such as GDPR, HIPAA, among others, is critical. The deployment of robust encryption techniques and the following of data security best practices are required.
- **Accessibility Optimization**: 
    The app must cater to diverse user capabilities. This can be achieved by integrating accessible designs (including large text options and colorblind-friendly palettes) and supporting voice inputs.
- **Multilingual Support Expansion**: 
    To facilitate effective communication, the tool should also accommodate multiple languages.

### Limitations
- **Diagnosis**:
    At no point will this application suggest a diagnosis or generate symptoms designed to guide a diagnosis or a specific treatment. It is a summarizing tool designed to support communication between patient and medic/ VET.
- **Not build using a medically trained model**:
    This application will be built using an LLM trained to summarize language, it will not use a medically trained model to support disgnosis or to rephrase symptoms using medical phrasing to support diagnosis. All medical knowledge will be expected to be provided by the GP or VET and never from this application.
- **Pass it on**:
    It is expected that with the development of medically trained AI, that this tool may eventually speak directly to a medically trained AI, however every step has been taken to try to ensure that this tool is purely to facilitate communication between patient and doctor and not to pass on errors in messages in order to prevent a game of '_pass it on_' developing between doctor and patient (also historically known as _Chinese Whispers_, or _Russian Telephone_).
