import os
import dashscope
import pandas as pd
from tqdm import tqdm  # Import tqdm for progress bars

def main():
    # Excel file path and worksheet name
    group_name = ""  # Specify group name
    excel_path = group_name + "-QA-Structure.xlsx"  # Replace with your Excel file path
    sheet_name = 'Sheet1'  # Replace with your worksheet name

    # Read the Excel file
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Columns to process
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
            prompt = row[column]  # Get the content of the current column
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
                response = data.output.choices[0].message.content  # Extract model response
            except Exception as e:
                print(f"Error occurred while processing column {column}: {e}")
                response = "Error"  # Record "Error" if an exception occurs
            responses.append(response)  # Save the response

        # Add the responses to a new column named "response_<column_name>"
        df[f"response_{column}"] = responses

    # Save results to a new Excel file
    output_path = group_name + "-Automatic-Scoring.xlsx"  # Output file path
    df.to_excel(output_path, index=False)
    print(f"Processing completed. Results saved to {output_path}")


if __name__ == '__main__':
    main()