from sentence_transformers import SentenceTransformer
import neo4j

URI = 'bolt://localhost:7687'
AUTH = ('name', 'password')
DB_NAME = 'neo4j'  # examples: 'recommendations-50', 'neo4j'


def main():
    driver = neo4j.GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    model = SentenceTransformer('shibing624/text2vec-base-chinese')  # vector size 384

    batch_size = 100
    batch_n = 1
    owl__NamedIndividuals_with_embeddings = []
    with driver.session(database=DB_NAME) as session:
        # Fetch `owl__NamedIndividual` nodes
        result = session.run('''
        MATCH (n:owl__NamedIndividual) 
        RETURN n.uri as uri, n.description as description, n.number as number, 
               n.difficultyLevel as difficultyLevel, n.evaluationType as evaluationType
        ''')
        for record in result:
            uri = record.get('uri')
            description = record.get('description')
            number = record.get('number')
            difficultyLevel = record.get('difficultyLevel')
            evaluationType = record.get('evaluationType')

            # 过滤出不为 None 的字段
            fields = {
                'uri': uri,
                'description': description,
                'number': number,
                'difficultyLevel': difficultyLevel,
                'evaluationType': evaluationType
            }
            non_none_fields = {k: v for k, v in fields.items() if v is not None}

            # 如果有有效的字段，创建嵌入向量
            if non_none_fields:
                # 构造嵌入向量的输入字符串
                embedding_input = '\n'.join(f"{k}: {v}" for k, v in non_none_fields.items())
                embedding = model.encode(embedding_input)

                # 保存结果，只包含不为 None 的字段
                owl__NamedIndividuals_with_embeddings.append({
                    **non_none_fields,
                    'embedding': embedding,
                })

            # Import when a batch of owl__NamedIndividuals has embeddings ready; flush buffer
            if len(owl__NamedIndividuals_with_embeddings) == batch_size:
                import_batch(driver, owl__NamedIndividuals_with_embeddings, batch_n)
                owl__NamedIndividuals_with_embeddings = []
                batch_n += 1

        # 导入最后一批数据（如果有的话）
        if owl__NamedIndividuals_with_embeddings:
            import_batch(driver, owl__NamedIndividuals_with_embeddings, batch_n)

    # Import complete, show counters
    records, _, _ = driver.execute_query('''
    MATCH (m:owl__NamedIndividual WHERE m.embedding IS NOT NULL)
    RETURN count(*) AS countMoviesWithEmbeddings, size(m.embedding) AS embeddingSize
    ''', database_=DB_NAME)
    print(f"""
        Embeddings generated and attached to nodes.
        owl__NamedIndividual nodes with embeddings: {records[0].get('countMoviesWithEmbeddings')}.
        Embedding size: {records[0].get('embeddingSize')}.
    """)


def import_batch(driver, nodes_with_embeddings, batch_n):
    # Add embeddings to owl__NamedIndividual nodes
    driver.execute_query('''
    UNWIND $owl__NamedIndividuals as owl__NamedIndividual
    MATCH (n:owl__NamedIndividual {uri: owl__NamedIndividual.uri})
    SET n.embedding = owl__NamedIndividual.embedding
    ''', owl__NamedIndividuals=nodes_with_embeddings, database_=DB_NAME)
    print(f'Processed batch {batch_n}.')


if __name__ == '__main__':
    main()

'''
Embeddings generated and attached to nodes.
        owl__NamedIndividual nodes with embeddings: 165.
        Embedding size: 768.
'''