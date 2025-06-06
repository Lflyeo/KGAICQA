import os
import dashscope
import pandas as pd
from tqdm import tqdm

def main():
    # Excel file path and table name
    group_name = "Qwen-Control-Group"
    excel_path = group_name + "-QA-Structure.xlsx"
    sheet_name = 'Sheet1'

    # Read the Excel file
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Define the column names to be processed
    columns_to_process = [
        "Fluency Structure",
        "Coherence Structure",
        "Topicality Structure",
        "General Quality Structure",
        "Attribute Relevance Structure"
    ]

    # Process each column one by one
    for column in columns_to_process:
        print(f"Processing column: {column}")
        responses = []
        for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"Progress - {column}"):
            prompt = row[column]  # Get content from the current column
            messages = [
                {'role': 'user', 'content': prompt}
            ]
            try:
                data = dashscope.Generation.call(
                    api_key=os.getenv("DASHSCOPE_API_KEY"),
                    model="deepseek-v3",  # Model name
                    messages=messages,
                    result_format='message'
                )
                response = data.output.choices[0].message.content  # Extract the response
            except Exception as e:
                print(f"Error while processing column {column}: {e}")
                response = "Error"  # Record as "Error" if an exception occurs
            responses.append(response)  # Save the response

        # Add the response results to a new column named "response_<column_name>"
        df[f"response_{column}"] = responses

    # Save the result to a new Excel file
    output_path = group_name + "_Auto-Scoring-Results.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Processing complete. Results saved to {output_path}")

if __name__ == '__main__':
    main()
