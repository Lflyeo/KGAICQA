import os
import dashscope
import pandas as pd
from tqdm import tqdm  # 导入tqdm库

def main():
    # Excel文件路径和表名
    group_name = "Qwen2.5"  # 指定组名
    excel_path = group_name + "-问答结构.xlsx"  # 替换为您的Excel文件路径
    sheet_name = 'Sheet1'  # 替换为您的表名

    # 读取Excel文件
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # 定义需要处理的列名
    columns_to_process = [
        "Fluency Structure",
        "Coherence Structure",
        "Topicality Structure",
        "General Quality Structure",
        "Attribute Relevance Structure"
    ]

    # 遍历每一列，逐列处理
    for column in columns_to_process:
        print(f"正在处理列：{column}")
        responses = []
        for index, row in tqdm(df.iterrows(), total=df.shape[0], desc=f"处理进度 - {column}"):
            prompt = row[column]  # 获取当前列的内容
            messages = [
                {'role': 'user', 'content': prompt}
            ]
            try:
                data = dashscope.Generation.call(
                    api_key=os.getenv("DASHSCOPE_API_KEY"),
                    model="deepseek-v3",  # 模型名称
                    messages=messages,
                    result_format='message'
                )
                response = data.output.choices[0].message.content  # 获取响应结果
            except Exception as e:
                print(f"处理列 {column} 时出错: {e}")
                response = "Error"  # 如果出错，记录为 "Error"
            responses.append(response)  # 保存响应结果

        # 将响应结果添加到新的列中，列名为 "response_<column_name>"
        df[f"response_{column}"] = responses

    # 将结果保存到新的Excel文件
    output_path = group_name+"自动评分结果.xlsx"  # 输出文件路径
    df.to_excel(output_path, index=False)
    print(f"处理完成，结果已保存到 {output_path}")


if __name__ == '__main__':
    main()