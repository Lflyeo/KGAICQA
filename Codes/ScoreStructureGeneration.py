import pandas as pd

# 读取Excel文件
def read_excel(file_path, sheet_name=0, header=0):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=header)  # 指定表头
        print(f"成功读取Excel文件：{file_path}，表单：{sheet_name}")
        return df
    except Exception as e:
        print(f"读取Excel文件时出错: {e}")
        return None


# 生成新的流畅度评分结构
def generate_fluency_structure(question, response):
    fluency_structure = f"""
###任务介绍：
将为您提供一个人工智能领域的问题。您的任务是依据一个指标对这个问题的答案进行评分。请确保您仔细阅读并理解这些说明。请在评分时保持此文档打开，并根据需要参考。

###评分标准：
流畅度（1-5）答案的流畅度如何？ 
    1分 - 文本存在大量语法错误，语句结构混乱，严重影响理解。表达冗余重复严重，逻辑断裂明显。
    2分 - 语法错误较多，部分句子不够通顺。存在冗余表述和重复内容，需要读者反复揣摩才能理解主要意思。
    3分 - 基本符合语法规范但偶有错误，整体结构完整但局部衔接生硬。存在少量冗余表述或重复内容，不影响核心信息获取。
    4分 - 语法准确表达清晰，语句通顺连贯。逻辑结构合理，仅在个别地方存在轻微重复或不必要的表述，不影响整体阅读体验。
    5分 - 语法完全正确，表达精炼准确。结构严谨逻辑流畅，用词简洁得当，无任何冗余重复内容，具备专业文本的流畅性和可读性。

###评分步骤：
    1. 全面了解答案的内容和结构。
    2. 根据评分标准，分配1至5的流畅度分数，其中1是最低，而5是最高的。
    3. 请你以批判性思维思考20次，并给出最终的分数以及给出该分数的概率。
    4. 请只输出评分与概率，不要输出其他内容。

###问题：
{question}

###答案：
{response}

###评分表单（仅评分）：
- 流畅度：
"""
    return fluency_structure


# 生成新的连贯性评分结构
def generate_coherence_structure(question, response):
    coherence_structure = f"""
###任务介绍：
将为您提供一个人工智能领域的问题。您的任务是依据一个指标对这个问题的答案进行评分。请确保您仔细阅读并理解这些说明。请在评分时保持此文档打开，并根据需要参考。

###评分标准：
连贯性（1-5）答案的连贯性如何？ 
    1分 - 文本语言风格不统一，句子之间缺乏明显的因果或时间顺序，整体缺乏逻辑结构，导致阅读困难。
    2分 - 文本语言风格存在不一致，句子之间的因果或时间关系不明确，逻辑结构松散，影响理解。
    3分 - 文本语言风格基本统一，句子之间有一定的因果或时间顺序，逻辑结构尚可，但仍有改进空间。
    4分 - 文本语言风格统一，句子之间因果或时间关系清晰，逻辑结构合理，易于理解。
    5分 - 文本语言风格高度统一，句子之间因果或时间关系紧密，逻辑结构严谨，阅读流畅，信息传达清晰。

###评分步骤：
    1. 全面了解答案的内容和结构。
    2. 根据评分标准，分配1至5的连贯性分数，其中1是最低，而5是最高的。
    3. 请你以批判性思维思考20次，并给出最终的分数以及给出该分数的概率。
    4. 请只输出评分与概率，不要输出其他内容。

###问题：
{question}

###答案：
{response}

###评分表单（仅评分）：
- 连贯性：
"""
    return coherence_structure


# 生成新的主题性评分结构
def generate_topicality_structure(question, response):
    topicality_structure = f"""
###任务介绍：
将为您提供一个人工智能领域的问题。您的任务是依据一个指标对这个问题的答案进行评分。请确保您仔细阅读并理解这些说明。请在评分时保持此文档打开，并根据需要参考。

###评分标准：
主题性（1-5）答案的主题性如何？ 
    1分 - 答案完全偏离问题的主题，未能针对问题的核心进行回应，内容与问题几乎无关。
    2分 - 答案偏离主题较远，虽然部分内容可能与问题相关，但大部分内容没有紧密围绕核心展开，未能有效解答问题。
    3分 - 答案在一定程度上围绕问题展开，但可能存在少量跑题或偏离核心的情况。整体内容与问题基本相关，尚可接受。
    4分 - 答案基本围绕问题核心展开，内容与问题高度相关，偏离主题的部分较少，能够较好解答问题。
    5分 - 答案紧密围绕问题的核心展开，内容完全与问题相关，没有任何偏离，且能够全面、深入地解答问题。

###评分步骤：
    1. 全面了解答案的内容和结构。
    2. 根据评分标准，分配1至5的主题性分数，其中1是最低，而5是最高的。
    3. 请你以批判性思维思考20次，并给出最终的分数以及给出该分数的概率。
    4. 请只输出评分与概率，不要输出其他内容。

###问题：
{question}

###答案：
{response}

###评分表单（仅评分）：
- 主题性：
"""
    return topicality_structure


# 生成新的一般质量评分结构
def generate_general_quality_structure(question, response):
    general_quality_structure = f"""
###任务介绍：
将为您提供一个人工智能领域的问题。您的任务是依据一个指标对这个问题的答案进行评分。请确保您仔细阅读并理解这些说明。请在评分时保持此文档打开，并根据需要参考。

###评分标准：
一般质量（1-5）答案的一般质量如何？ 
    1分 - 答案缺乏常识性，表达单一、陈腐，词汇极其简单，缺乏多样性。文本难以理解或表达不清晰。
    2分 - 答案在常识性方面存在明显问题，表达较为单一，词汇运用有限，缺乏丰富的表达方式，可能影响理解。
    3分 - 答案基本符合常识，表达较为简单但有效，词汇使用相对丰富，具备一定的表达多样性，能够清晰传达意思。
    4分 - 答案内容符合常识，表达流畅且多样，词汇运用较为丰富，文本具有一定的语言深度，且能够吸引读者。
    5分 - 答案表现出极强的常识性，语言表达多样、富有创意，词汇丰富且精准，能够清晰、深刻地传递信息，阅读体验良好。

###评分步骤：
    1. 全面了解答案的内容和结构。
    2. 根据评分标准，分配1至5的一般质量分数，其中1是最低，而5是最高的。
    3. 请你以批判性思维思考20次，并给出最终的分数以及给出该分数的概率。
    4. 请只输出评分与概率，不要输出其他内容。

###问题：
{question}

###答案：
{response}

###评分表单（仅评分）：
- 一般质量：
"""
    return general_quality_structure


# 生成新的属性相关性评分结构
def generate_attribute_relevance_structure(question, response):
    attribute_relevance_structure = f"""
###任务介绍：
将为您提供一个人工智能领域的问题。您的任务是依据一个指标对这个问题的答案进行评分。请确保您仔细阅读并理解这些说明。请在评分时保持此文档打开，并根据需要参考。

###评分标准：
属性相关性（1-5）答案的属性相关性如何？ 
    1分 - 答案与人工智能领域无关，内容完全不涉及人工智能的概念、技术或应用。
    2分 - 答案与人工智能领域有少量关联，可能提及人工智能的某些方面，但整体内容与人工智能的关系较弱。
    3分 - 答案与人工智能领域有明显关联，涵盖了人工智能的基本概念或技术，但可能缺乏深入的讨论或细节。
    4分 - 答案与人工智能领域紧密相关，详细讨论了人工智能的关键概念、技术或应用，体现了对该领域的深入理解。
    5分 - 答案与人工智能领域高度相关，全面且深入地探讨了人工智能的各个方面，展示了对该领域的深刻洞察和专业知识。 

###评分步骤：
    1. 全面了解答案的内容和结构。
    2. 根据评分标准，分配1至5的属性相关性分数，其中1是最低，而5是最高的。
    3. 请你以批判性思维思考20次，并给出最终的分数以及给出该分数的概率。
    4. 请只输出评分与概率，不要输出其他内容。

###问题：
{question}

###答案：
{response}

###评分表单（仅评分）：
- 属性相关性：
"""
    return attribute_relevance_structure


# 将新的文本结构存储到Excel中
def save_to_excel(data, output_file_path):
    try:
        # 修改列名以匹配数据结构
        columns = ["Fluency Structure", "Coherence Structure", "Topicality Structure",
                   "General Quality Structure", "Attribute Relevance Structure"]
        df = pd.DataFrame(data, columns=columns)
        df.to_excel(output_file_path, index=False)
        print(f"数据已成功保存到 {output_file_path}")
    except Exception as e:
        print(f"保存到Excel文件时出错: {e}")


# 主程序
def main(input_file_path, output_file_path, sheet_name=0, question_column="问题", response_column="回答"):
    df = read_excel(input_file_path, sheet_name=sheet_name, header=0)
    if df is not None:
        # 检查指定的列是否存在
        if question_column not in df.columns or response_column not in df.columns:
            print(f"指定的列名不存在于表头中：{df.columns.tolist()}")
            return

        # 创建一个空列表来存储新的文本结构
        structures = []
        for index, row in df.iterrows():
            question = row[question_column]  # 根据列名获取问题
            response = row[response_column]  # 根据列名获取回答
            fluency_structure = generate_fluency_structure(question, response)
            coherence_structure = generate_coherence_structure(question, response)
            topicality_structure = generate_topicality_structure(question, response)
            general_quality_structure = generate_general_quality_structure(question, response)
            attribute_relevance_structure = generate_attribute_relevance_structure(question, response)

            structures.append([fluency_structure, coherence_structure, topicality_structure, general_quality_structure,
                               attribute_relevance_structure])

        # 将生成的文本结构保存到新的Excel文件中
        save_to_excel(structures, output_file_path)


# 示例调用
input_file_path = "汇总.xlsx"  # 输入文件路径
group_name = "GLM-对照组"  # 指定组名
output_file_path = group_name+"-问答结构.xlsx"  # 输出文件路径
sheet_name = "核对更新-组1"  # 指定表单名称或索引
question_column = "Question"  # 指定问题列的列名
response_column = group_name  # 指定回答列的列名

main(input_file_path, output_file_path, sheet_name=sheet_name, question_column=question_column, response_column=response_column)