# 🤖 AI职业发展助手 - 大学生智能职业规划平台

![Python](https://img.shields.io/badge/Python-3.14.2%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.53.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

<p align="center">
  <img src="logo.png" alt="AI Career Assistant Logo" width="350">
</p>

## 📖 项目简介

**AI职业发展助手**是一款专为大学生设计的智能职业规划工具。面对毕业季的职业迷茫，我们结合人工智能技术，提供个性化的职业咨询、技能分析、学习路径规划和模拟面试等一站式服务，帮助学生清晰规划职业道路。

> 🎯 **核心价值**：用AI技术降低职业探索成本，让每个学生都能获得个性化的职业发展指导。

## ✨ 功能亮点

| 功能模块 | 特色 | 技术实现 |
|---------|------|----------|
| **💬 智能职业咨询** | 对话式交互，理解用户背景与困惑 | 大语言模型 + 自然语言处理 |
| **📊 岗位匹配分析** | 可视化匹配度，清晰展示技能缺口 | 向量相似度计算 + 图表可视化 |
| **🎯 学习路径规划** | 个性化学习路线，分阶段目标设定 | 知识图谱 + 推荐算法 |
| **🎤 AI模拟面试** | 真实场景模拟，即时反馈建议 | 语音交互 + 评估模型 |
| **📈 技能成长追踪** | 进度可视化，学习效果量化 | 数据持久化 + 进度跟踪 |

## 🎥 运行效果

<p align="center">
  <img src="demo.gif" alt="AI职业发展助手演示" width="800">
  <br>
  <em>完整功能演示</em>
</p>

## 🚀 快速开始

### 环境要求
- **Python 3.14.2+**
- **pip** 包管理器
- 现代浏览器（Chrome/Firefox/Edge）

### 安装步骤

#### 方法一：一键安装（推荐）
```bash
# 克隆项目
git clone https://github.com/Connie0122/AI-Career-Assistant.git
cd AI-Career-Assistant

# 一键安装（Windows）
run.bat

# 或手动安装
pip install -r requirements.txt
streamlit run career_ai.py
```

#### 方法二：手动安装
```bash
# 1. 创建虚拟环境（可选但推荐）
python -m venv venv

# Windows激活
venv\Scripts\activate
# Mac/Linux激活
source venv/bin/activate

# 2. 安装依赖
pip install streamlit pandas plotly numpy

# 3. 运行应用
streamlit run career_ai.py
```

### 访问应用
安装完成后，浏览器会自动打开：  
🌐 **http://localhost:8501**

如果未自动打开，请手动在浏览器中输入上述地址。

## 📁 项目结构

```
AI-Career-Assistant/
├── 📄 career_ai.py              # 主程序文件
├── 📄 requirements.txt          # Python依赖库列表
├── 📄 README.md                # 项目说明文档
├── 📄 logo.png             # 项目logo
├── 📄 demo.gif                  # 演示动图
```

### 核心文件说明
- **career_ai.py**：应用主程序，包含所有业务逻辑和界面设计
- **requirements.txt**：项目依赖，确保环境一致性

## 🤝 贡献指南

我们欢迎任何形式的贡献！以下是参与方式：

### 如何贡献
1. **Fork 本仓库**
2. **创建功能分支**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **提交更改**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **推送到分支**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **提交 Pull Request**

### 开发规范
- 遵循 PEP 8 Python代码规范
- 为新增功能添加测试用例
- 更新相关文档
- 提交清晰的commit信息

### 待开发功能
- [ ] 接入真实招聘数据API
- [ ] 增加多语言支持
- [ ] 开发移动端应用
- [ ] 添加用户账户系统
- [ ] 集成在线学习资源

## 📄 许可证

本项目采用 **MIT 许可证** - 查看 [LICENSE](LICENSE) 文件了解详情。

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

## 👥 联系方式

### 项目维护者
- **姓名**：Connie
- **邮箱**：yu_kangning@outlook.com
- **GitHub**: [@your-username](https://github.com/your-username)

### 反馈与支持
- 📧 **问题反馈**：通过GitHub Issues提交
- 💬 **技术讨论**：欢迎在Discussions区交流
- 🐛 **Bug报告**：请提供详细的重现步骤

<p align="center">
  <sub>用 ❤️ 构建 | 让技术服务于人 | 开源共享</sub>
</p>
