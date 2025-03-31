import json
from sentence_transformers import SentenceTransformer
import neo4j
import pandas as pd
from tqdm import tqdm  # 导入tqdm

# 初始化Neo4j驱动和模型
URI = 'bolt://localhost:7687'
AUTH = ('Lflyeo', '123456789')
DB_NAME = 'neo4j'
driver = neo4j.GraphDatabase.driver(URI, auth=AUTH)
driver.verify_connectivity()
model = SentenceTransformer('shibing624/text2vec-base-chinese')


def find_aikps_by_embedding(query_embedding):
    """
    根据查询向量的相似度，从neo4j数据库中查询相关的AIKP节点
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
    将结果保存到JSON文件
    """
    # 将结果转换为JSON字符串
    results_json = json.dumps(results, ensure_ascii=False, indent=4)

    # 保存到JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(results_json)


def main():
    """
    主函数，读取表格文件，逐行处理表格中的每一行，查询相关的AIKP节点，并保存结果到JSON文件
    """
    # 读取表格文件
    input_file = "三年级题目.xlsx"  # 输入Excel文件的路径
    sheet_name = 'Sheet1'  # Excel工作表名称
    output_file = "三年级题目_AIKP.json"  # 输出json文件的路径
    df = pd.read_excel(input_file, sheet_name)

    # 创建一个空的列表来存储所有结果
    all_results = []

    # 逐行处理表格中的每一行
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc='Processing rows'):
        query_prompt = row['problem']
        query_embedding = model.encode(query_prompt)

        related_aikps = find_aikps_by_embedding(query_embedding)

        # 创建一个字典来存储当前query_prompt及其相关的records
        query_result = {
            'query_prompt': query_prompt,
            'AIKPs': []
        }

        for record in related_aikps:
            # 创建一个新的字典，包含需要的字段
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

    # 保存所有结果到JSON文件
    save_to_json(output_file, all_results)


if __name__ == '__main__':
    main()
