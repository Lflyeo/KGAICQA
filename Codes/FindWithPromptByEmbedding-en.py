import json
from sentence_transformers import SentenceTransformer
import neo4j
import pandas as pd
from tqdm import tqdm  # Import tqdm

# Initialize Neo4j driver and SentenceTransformer model
URI = 'bolt://localhost:7687'
AUTH = ('name', 'password')
DB_NAME = 'neo4j'
driver = neo4j.GraphDatabase.driver(URI, auth=AUTH)
driver.verify_connectivity()
model = SentenceTransformer('shibing624/text2vec-base-chinese')


def find_aikps_by_embedding(query_embedding):
    """
    Retrieve related AIKP nodes from the Neo4j database based on similarity to the query embedding.
    """
    related_aikps, _, _ = driver.execute_query('''
                   CALL db.index.vector.queryNodes('AIKP', 3, $queryEmbedding)
                   YIELD node, score
                   RETURN 
                       node.uri AS uri, 
                       node.description AS description, 
                       node.number AS number, 
                       node.difficultyLevel AS difficultyLevel, 
                       node.evaluationType AS evaluationType,
                       score
                   ''', queryEmbedding=query_embedding, database_=DB_NAME)
    return related_aikps


def save_to_json(output_file, results):
    """
    Save results to a JSON file.
    """
    results_json = json.dumps(results, ensure_ascii=False, indent=4)

    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(results_json)


def main():
    """
    Main function:
    - Read the Excel file
    - Process each row
    - Query related AIKP nodes
    - Save results to a JSON file
    """
    # Load the Excel file
    input_file = "Grade3_Questions.xlsx"  # Path to input Excel file
    sheet_name = 'Sheet1'                # Name of the Excel sheet
    output_file = "Grade3_Questions_AIKP.json"  # Output JSON file path
    df = pd.read_excel(input_file, sheet_name)

    # List to store all results
    all_results = []

    # Process each row in the DataFrame
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc='Processing rows'):
        query_prompt = row['problem']
        query_embedding = model.encode(query_prompt)

        related_aikps = find_aikps_by_embedding(query_embedding)

        # Create a dictionary to store the current query prompt and related records
        query_result = {
            'query_prompt': query_prompt,
            'AIKPs': []
        }

        for record in related_aikps:
            # Create a new dictionary containing required fields
            record_data = {
                'uri': record['uri']
            }
            if record['description'] is not None:
                record_data['description'] = record['description']
            if record['number'] is not None:
                record_data['number'] = record['number']
            if record['difficultyLevel'] is not None:
                record_data['difficultyLevel'] = record['difficultyLevel']
            if record['evaluationType'] is not None:
                record_data['evaluationType'] = record['evaluationType']
            query_result['AIKPs'].append(record_data)

        all_results.append(query_result)

    # Save all results to a JSON file
    save_to_json(output_file, all_results)


if __name__ == '__main__':
    main()