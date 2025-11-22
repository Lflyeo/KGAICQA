## Design and Evaluation of a Question-answering System Based on Knowledge Graph-augmented Large Language Models in K-12 Artificial Intelligence Curriculum

This is the offcial repo for the paper "[Design and Evaluation of a Question-answering System Based on Knowledge Graph-augmented Large Language Models in K-12 Artificial Intelligence Curriculum]".

<div align="center" style="padding-bottom: 20px">
  <img src="Fig/Evaluation Process.png" title="Evaluation Process">
</div>

###
It is worth noting that our article is still in the review stage.
In order to protect our intellectual property, we do not provide a nanny introduction of system implementation,
only the dataset and core code of evaluation.
Of course, by reading our article, you can see how our system is implemented.

### Requirement
* Python = 3.11.xx;
* Pytorch = 2.3.1+cu121;
* You can run it in the [mynotebook](https://modelscope.cn/my/mynotebook) on modelscope for quick evaluation purposes.

### AI Curriculum Knowledge Graph 
We provide an AI course knowledge map constructed based on the AI textbooks for Grade 3, [Upper](Guangzhou_K-12_AI_Curriculum_Textbooks/Third_Grade_Upper.pdf) and [Lower](Guangzhou_K-12_AI_Curriculum_Textbooks/Third_Grade_Lower.pdf) in Guangzhou, enabling readers to easily replicate our evaluation results and apply them to other research. Including 165 nodes, 459 relationships.
- [AICKG_csv](AI_Curriculum_Knowledge_Graph/AICKG.csv)
- [AICKG_json](AI_Curriculum_Knowledge_Graph/AICKG.json)
<div align="center" style="padding-bottom: 20px">
  <img src="AI_Curriculum_Knowledge_Graph/AICKG.png" title="Evaluation Process">
</div>

### Dataset
We provide the data to make it easy for the reader to reproduce our evaluation results. 

en:
- [AIC_ThirdGrade123_en](Dataset/AIC_ThirdGrade123_en.json)
- [AIC_ThirdGrade1098_en](Dataset/AIC_ThirdGrade1098_en.json)

zh:
- [AIC_ThirdGrade123_zh](Dataset/AIC_ThirdGrade123_zh.json)
- [AIC_ThirdGrade1098_zh](Dataset/AIC_ThirdGrade1098_zh.json)

### Citation
Waiting for the result of the review.
