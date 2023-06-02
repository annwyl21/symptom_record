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

### Constraints
- **No Diagnostic Role**: This application merely facilitates patient-doctor communication and does not provide diagnoses or generate symptom-related information.
- **Non-medical Model**: The tool uses a language summarizing model, not medically trained, implying any medical expertise should come from the healthcare provider, not the application.
- **No Error Propagation**: Despite potential integration with medically trained AI, the tool aims to ensure clear patient-doctor communication, averting any risk of miscommunication akin to a 'Chinese Whispers' scenario.
