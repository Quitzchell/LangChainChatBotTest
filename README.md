# Studybuddy v0.1 local setup tutorial

Follow these steps to set up and run Studybuddy v0.1 on your local environment:

1. **Install Requirements**: Make sure you have all the necessary dependencies installed. If not, install them using:

```bash
pip install -r requirements.txt
```

2. **Configure Environment Variables**:
   - Copy the provided `.env.example` file and rename it to `.env`.
   - Open the `.env` file and set the HuggingFace API KEY.


3. **Start the Project**: Run the following command in your terminal to start the Studybuddy project:

```bash
streamlit run app.py
```

Now you're all set to use Studybuddy v0.1 locally! Access the app through your browser at the provided URL (usually `http://localhost:8501`).

---
This project is based on Alejandro AO his tutorial: https://youtu.be/dXxQ0LR-3Hg?si=o-zDdaTWjhwymIva


## BenchMarking

question: "What is the title?"
- OpenAI: "The title of the text is "HBO-i-domeinbeschrijving 2018" -> 2.16 seconds
- HuggingFaceApi:
# with GPU Numba package on AMD Radeon RX 5700 XT
- Local orca-mini
- Local wizard-lm: