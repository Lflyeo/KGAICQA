## Design and Evaluation of a Question-answering System Based on Knowledge Graph-augmented Large Language Models in K-12 Artificial Intelligence Curriculum

This is the offcial repo for the paper "[Design and Evaluation of a Question-answering System Based on Knowledge Graph-augmented Large Language Models in K-12 Artificial Intelligence Curriculum]".

<div align="center" style="padding-bottom: 100px">
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
We provide the constructed AI Curriculum Knowledge Graph to enable readers to easily reproduce our evaluation results and utilize it for other research.
<div align="center" style="padding-bottom: 100px">
  <svg src="AI Curriculum Knowledge Graph/AICKG.svg" title="Evaluation Process">
</div>

- [CSV](AI Curriculum Knowledge Graph/AICKG.csv)
- [JSON](AI Curriculum Knowledge Graph/AICKG.json)

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
