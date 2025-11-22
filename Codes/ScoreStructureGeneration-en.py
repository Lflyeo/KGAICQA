import pandas as pd

# Read Excel file
def read_excel(file_path, sheet_name=0, header=0):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=header)  # Specify header row
        print(f"Successfully read Excel file: {file_path}, sheet: {sheet_name}")
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None


# Generate fluency evaluation structure
def generate_fluency_structure(question, response):
    fluency_structure = f"""
###Task Description:
You will be given a question related to the field of artificial intelligence. Your task is to evaluate the answer based on a specific metric. Please make sure you read and understand these instructions carefully. Keep this document open while scoring and refer to it when necessary.

###Scoring Criteria:
Fluency (1–5): How fluent is the answer?
    1 - The text contains many grammatical errors, chaotic sentence structure, and serious comprehension issues. Redundancy and repetition are severe, with obvious logical breaks.
    2 - The text contains several grammatical errors and some sentences are not smooth. Redundant and repetitive expressions appear, requiring effort to understand the main idea.
    3 - The text is mostly grammatically correct with occasional errors. Overall structure is complete but some transitions are awkward. Minor redundancies exist but do not hinder comprehension.
    4 - Grammar is accurate and expression is clear. Sentences are smooth and coherent. Logical structure is sound with only minor unnecessary expressions, not affecting readability.
    5 - Grammar is completely correct and expression is concise and accurate. Structure is rigorous, logic is fluent, wording is precise, and no redundancies exist. Reads like a professional text.

###Scoring Steps:
    1. Fully understand the content and structure of the answer.
    2. Assign a fluency score from 1 to 5 (1 = lowest, 5 = highest).
    3. Think critically for 20 rounds and provide the final score as well as the probability of that score.
    4. Only output the score and the probability; do not output anything else.

###Question:
{question}

###Answer:
{response}

###Scoring Form (Score Only):
- Fluency:
"""
    return fluency_structure


# Generate coherence evaluation structure
def generate_coherence_structure(question, response):
    coherence_structure = f"""
###Task Description:
You will be given a question related to the field of artificial intelligence. Your task is to evaluate the answer based on a specific metric. Please make sure you read and understand these instructions carefully. Keep this document open while scoring and refer to it when necessary.

###Scoring Criteria:
Coherence (1–5): How coherent is the answer?
    1 - Language style is inconsistent and sentences lack causal or temporal order. Logical structure is missing, making reading difficult.
    2 - Minor inconsistencies in language style; causal or temporal relations between sentences are unclear, weakening logical flow.
    3 - Language style is mostly consistent; sentences follow some causal or temporal order, but overall logic still needs improvement.
    4 - Language style is consistent; causal or temporal relations are clear; logical structure is reasonable and easy to follow.
    5 - Language style is highly consistent; strong causal or temporal links between sentences; logic is rigorous and information flows smoothly.

###Scoring Steps:
    1. Fully understand the answer.
    2. Assign a coherence score from 1 to 5.
    3. Think critically for 20 rounds and give the final score and its probability.
    4. Only output the score and the probability.

###Question:
{question}

###Answer:
{response}

###Scoring Form (Score Only):
- Coherence:
"""
    return coherence_structure


# Generate topicality evaluation structure
def generate_topicality_structure(question, response):
    topicality_structure = f"""
###Task Description:
You will be given a question related to the field of artificial intelligence. Your task is to evaluate the answer based on a specific metric. Please make sure you read and understand these instructions carefully. Keep this document open while scoring and refer to it when necessary.

###Scoring Criteria:
Topicality (1–5): How relevant is the answer to the topic?
    1 - The answer is completely off-topic; it does not address the core of the question and is nearly unrelated.
    2 - The answer is largely off-topic with only small portions related to the question; fails to address the core issue effectively.
    3 - The answer is somewhat related to the question but contains minor digressions. Overall relevance is acceptable.
    4 - The answer is strongly relevant to the core question with minimal deviation.
    5 - The answer is entirely on-topic, deeply addressing all aspects of the question with no deviation.

###Scoring Steps:
    1. Fully understand the answer.
    2. Assign a topicality score from 1 to 5.
    3. Think critically for 20 rounds and output the final score and its probability.
    4. Only output the score and the probability.

###Question:
{question}

###Answer:
{response}

###Scoring Form (Score Only):
- Topicality:
"""
    return topicality_structure


# Generate general quality evaluation structure
def generate_general_quality_structure(question, response):
    general_quality_structure = f"""
###Task Description:
You will be given a question related to the field of artificial intelligence. Your task is to evaluate the answer based on a specific metric. Please make sure you read and understand these instructions carefully. Keep this document open while scoring and refer to it when necessary.

###Scoring Criteria:
General Quality (1–5): How is the overall quality of the answer?
    1 - Lacks common sense; expression is poor and overly simplistic. Text is unclear or hard to understand.
    2 - Shows some problems with common sense; expression is limited and vocabulary lacks richness.
    3 - Generally reasonable and clear; vocabulary is moderately rich and expression is functional.
    4 - Content aligns with common sense; expression is fluent and diverse; vocabulary is rich and the text is engaging.
    5 - Demonstrates excellent common-sense reasoning; expression is creative and diverse; vocabulary is precise and rich; conveys information clearly and deeply.

###Scoring Steps:
    1. Fully understand the answer.
    2. Assign a general quality score from 1 to 5.
    3. Think critically for 20 rounds and provide the final score and its probability.
    4. Only output the score and the probability.

###Question:
{question}

###Answer:
{response}

###Scoring Form (Score Only):
- General Quality:
"""
    return general_quality_structure


# Generate attribute relevance evaluation structure
def generate_attribute_relevance_structure(question, response):
    attribute_relevance_structure = f"""
###Task Description:
You will be given a question related to the field of artificial intelligence. Your task is to evaluate the answer based on a specific metric. Please make sure you read and understand these instructions carefully. Keep this document open while scoring and refer to it when necessary.

###Scoring Criteria:
Attribute Relevance (1–5): How relevant is the answer to AI attributes?
    1 - Answer is unrelated to AI; contains no AI concepts, technologies, or applications.
    2 - Answer contains slight relevance; mentions AI but lacks meaningful connection.
    3 - Answer includes essential AI concepts or techniques but lacks depth.
    4 - Answer is closely related to AI with detailed discussions of key concepts, techniques, or applications.
    5 - Answer demonstrates strong and deep relevance to AI; thoroughly covers AI-related aspects with insight.

###Scoring Steps:
    1. Fully understand the answer.
    2. Assign an attribute relevance score from 1 to 5.
    3. Think critically for 20 rounds and provide the final score and its probability.
    4. Only output the score and the probability.

###Question:
{question}

###Answer:
{response}

###Scoring Form (Score Only):
- Attribute Relevance:
"""
    return attribute_relevance_structure


# Save new text structures to Excel
def save_to_excel(data, output_file_path):
    try:
        columns = [
            "Fluency Structure",
            "Coherence Structure",
            "Topicality Structure",
            "General Quality Structure",
            "Attribute Relevance Structure"
        ]
        df = pd.DataFrame(data, columns=columns)
        df.to_excel(output_file_path, index=False)
        print(f"Data successfully saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving to Excel: {e}")


# Main program
def main(input_file_path, output_file_path, sheet_name=0, question_column="Question", response_column="Answer"):
    df = read_excel(input_file_path, sheet_name=sheet_name, header=0)
    if df is not None:
        # Check if required columns exist
        if question_column not in df.columns or response_column not in df.columns:
            print(f"Specified column names do not exist. Available columns: {df.columns.tolist()}")
            return

        structures = []
        for index, row in df.iterrows():
            question = row[question_column]
            response = row[response_column]
            fluency_structure = generate_fluency_structure(question, response)
            coherence_structure = generate_coherence_structure(question, response)
            topicality_structure = generate_topicality_structure(question, response)
            general_quality_structure = generate_general_quality_structure(question, response)
            attribute_relevance_structure = generate_attribute_relevance_structure(question, response)

            structures.append([
                fluency_structure,
                coherence_structure,
                topicality_structure,
                general_quality_structure,
                attribute_relevance_structure
            ])

        # Save results to Excel
        save_to_excel(structures, output_file_path)


# Example usage
input_file_path = "output.xlsx"
group_name = "GLM-Control-Group"
output_file_path = group_name + "-QA-Structure.xlsx"
sheet_name = "Review-Update-Group1"
question_column = "Question"
response_column = group_name

main(input_file_path, output_file_path, sheet_name=sheet_name,
     question_column=question_column, response_column=response_column)