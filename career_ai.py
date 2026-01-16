import streamlit as st
import pandas as pd
import json
import requests
from datetime import datetime
import plotly.express as px

# 页面配置
st.set_page_config(
    page_title="AI职业发展助手",
    page_icon="🎯",
    layout="wide"
)

# 初始化session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}

# 模拟API调用（实际使用时替换为真实API）
def call_ai_api(prompt, history=[]):
    """模拟AI API调用"""
    # 这里应该是实际的API调用代码
    # response = requests.post(API_URL, json={"messages": messages})
    # return response.json()["choices"][0]["message"]["content"]
    
    # 模拟响应
    mock_responses = {
        "职业测评": "基于您的兴趣和技能，我建议您考虑以下方向：数据分析师、产品经理、UX设计师。数据分析师需要SQL、Python和统计知识；产品经理需要沟通、市场分析和原型设计能力。",
        "岗位匹配": "为您匹配到以下岗位：1. 初级数据分析师（匹配度85%），2. 产品助理（匹配度78%），3. 用户体验设计师（匹配度72%）。",
        "学习路径": "数据分析师学习路径：第1-2月学习SQL和Python基础，第3-4月学习统计分析和可视化，第5-6月完成实战项目。推荐课程：Coursera的数据科学专项课程。",
        "面试模拟": "请回答：'请介绍一下你最大的优点和缺点。' 建议回答结构：优点与岗位相关+具体例子；缺点真实但可改进+改进措施。"
    }
    return mock_responses.get(prompt.split(":")[0] if ":" in prompt else prompt, "我理解您的需求，正在为您分析...")

# 侧边栏
with st.sidebar:
    st.header("🎯 职业发展助手")
    st.markdown("---")
    
    user_major = st.text_input("您的专业", placeholder="计算机科学、金融、设计等")
    user_interest = st.multiselect("您的兴趣", ["技术开发", "产品设计", "市场营销", "数据分析", "人力资源", "运营管理"])
    experience_level = st.selectbox("经验水平", ["在校生", "应届生", "1-3年经验", "3-5年经验"])
    
    st.markdown("---")
    uploaded_file = st.file_uploader("上传简历（PDF/DOCX）", type=['pdf', 'docx'])
    if uploaded_file:
        st.success("简历上传成功！")

# 主界面
st.title("🤖 AI职业发展助手")
st.caption("为大学生提供个性化职业规划、技能提升和求职指导")

# 创建选项卡
tab1, tab2, tab3, tab4 = st.tabs(["智能对话", "职业匹配", "学习路径", "面试模拟"])

with tab1:
    st.subheader("💬 智能职业咨询")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_input = st.text_area("请描述您的困惑或需求：", 
                                 placeholder="例如：我是计算机专业学生，但对编程兴趣一般，更适合什么方向？",
                                 height=100)
        
        if st.button("获取AI建议", type="primary"):
            if user_input:
                with st.spinner("AI正在思考..."):
                    response = call_ai_api(user_input, st.session_state.conversation)
                    
                    # 保存对话
                    st.session_state.conversation.append({"role": "user", "content": user_input})
                    st.session_state.conversation.append({"role": "assistant", "content": response})
                    
                    # 显示响应
                    st.info("AI建议：")
                    st.write(response)
    
    with col2:
        st.markdown("### 快捷提问")
        quick_questions = [
            "帮我分析适合的职业方向",
            "当前市场热门岗位有哪些？",
            "如何提升简历竞争力？",
            "模拟产品经理面试"
        ]
        
        for q in quick_questions:
            if st.button(q, use_container_width=True):
                with st.spinner("思考中..."):
                    response = call_ai_api(q)
                    st.session_state.conversation.append({"role": "user", "content": q})
                    st.session_state.conversation.append({"role": "assistant", "content": response})
                    st.rerun()
    
    # 显示对话历史
    if st.session_state.conversation:
        st.markdown("---")
        st.subheader("对话历史")
        for i, msg in enumerate(st.session_state.conversation[-6:]):  # 显示最近6条
            if msg["role"] == "user":
                st.markdown(f"**您**：{msg['content']}")
            else:
                st.markdown(f"**助手**：{msg['content']}")
                st.markdown("---")

with tab2:
    st.subheader("📊 岗位匹配分析")
    
    # 模拟岗位数据
    jobs_data = {
        "岗位名称": ["初级数据分析师", "产品助理", "UX设计师", "市场营销专员", "软件开发工程师"],
        "匹配度": [85, 78, 72, 65, 90],
        "薪资范围": ["8-12K", "7-10K", "9-13K", "6-9K", "10-15K"],
        "技能要求": ["SQL, Python, Excel", "Axure, 竞品分析", "Figma, 用户研究", "文案, 社交媒体", "Java, Spring, MySQL"],
        "经验要求": ["应届生/1年", "应届生", "1-2年", "应届生", "1-3年"]
    }
    
    df_jobs = pd.DataFrame(jobs_data)
    
    # 可视化匹配度
    fig = px.bar(df_jobs, x='岗位名称', y='匹配度', 
                 color='匹配度', title='岗位匹配度分析',
                 color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示详细岗位信息
    st.dataframe(df_jobs, use_container_width=True, hide_index=True)
    
    # 技能分析
    st.subheader("📈 您的技能分析")
    
    skills = {
        "技术技能": ["Python", "SQL", "数据分析", "机器学习"],
        "软技能": ["沟通能力", "团队协作", "问题解决", "项目管理"],
        "当前水平": [3, 2, 4, 2],  # 1-5分
        "目标水平": [5, 4, 5, 4]
    }
    
    df_skills = pd.DataFrame(skills)
    
    # 技能雷达图数据准备
    categories = skills["技术技能"] + skills["软技能"]
    current = skills["当前水平"] * 2  # 简化处理
    target = skills["目标水平"] * 2
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("平均技能匹配度", "76%", "↗︎ 8%")
    with col2:
        st.metric("推荐学习时长", "120小时", "约3个月")

with tab3:
    st.subheader("🎯 个性化学习路径")
    
    # 学习路径时间轴
    timeline_data = {
        "阶段": ["基础学习", "技能提升", "实战项目", "求职准备"],
        "开始时间": ["2024-03", "2024-05", "2024-07", "2024-09"],
        "结束时间": ["2024-05", "2024-07", "2024-09", "2024-10"],
        "主要内容": ["Python基础、SQL入门", "数据分析方法、可视化", "完成2个真实项目", "简历优化、模拟面试"],
        "资源推荐": ["Coursera Python课程", "Kaggle学习路径", "阿里天池比赛", "牛客网面试题库"]
    }
    
    df_timeline = pd.DataFrame(timeline_data)
    
    # 显示时间轴
    for idx, row in df_timeline.iterrows():
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{row['阶段']}**")
                st.caption(f"{row['开始时间']} - {row['结束时间']}")
            with col2:
                st.markdown(f"**内容**：{row['主要内容']}")
                st.markdown(f"**资源**：{row['资源推荐']}")
            st.markdown("---")
    
    # 学习资源推荐
    st.subheader("📚 推荐学习资源")
    
    resources = [
        {"平台": "Coursera", "课程": "数据科学专项课程", "时长": "6个月", "难度": "中级"},
        {"平台": "Udemy", "课程": "Python数据分析实战", "时长": "30小时", "难度": "初级"},
        {"平台": "Kaggle", "课程": "机器学习入门", "时长": "自主学习", "难度": "初级"},
        {"平台": "牛客网", "课程": "笔试面试题库", "时长": "持续更新", "难度": "实战"}
    ]
    
    for res in resources:
        st.markdown(f"**{res['平台']}** - {res['课程']}")
        st.progress(0.7 if res['难度'] == '中级' else 0.4 if res['难度'] == '初级' else 0.9)
        st.caption(f"时长：{res['时长']} | 难度：{res['难度']}")

with tab4:
    st.subheader("🎤 AI模拟面试")
    
    interview_mode = st.radio("选择面试模式", ["产品经理", "数据分析师", "软件开发", "市场营销"])
    
    # 面试问题库
    questions_db = {
        "产品经理": [
            "请介绍一下你最喜欢的一款产品",
            "如何确定产品需求的优先级？",
            "如果开发资源有限，你会如何取舍功能？"
        ],
        "数据分析师": [
            "如何处理缺失数据？",
            "请解释一下A/B测试的原理",
            "如何向非技术人员解释复杂的分析结果？"
        ]
    }
    
    selected_questions = questions_db.get(interview_mode, ["请做个自我介绍"])
    
    # 模拟面试过程
    if "interview_step" not in st.session_state:
        st.session_state.interview_step = 0
        st.session_state.user_answers = []
    
    if st.session_state.interview_step < len(selected_questions):
        current_q = selected_questions[st.session_state.interview_step]
        
        st.markdown(f"### 问题 {st.session_state.interview_step + 1}/{len(selected_questions)}")
        st.info(f"**面试官**：{current_q}")
        
        user_answer = st.text_area("您的回答：", height=150, 
                                  key=f"answer_{st.session_state.interview_step}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("提交答案", type="primary"):
                if user_answer:
                    st.session_state.user_answers.append({
                        "question": current_q,
                        "answer": user_answer
                    })
                    st.session_state.interview_step += 1
                    st.rerun()
        with col2:
            if st.button("请求提示"):
                st.warning("提示：尝试用STAR法则（情境-任务-行动-结果）来组织答案")
    
    else:
        st.success("🎉 模拟面试完成！")
        
        # AI反馈
        st.subheader("📝 AI反馈报告")
        
        feedback_cols = st.columns(3)
        with feedback_cols[0]:
            st.metric("回答完整性", "82%", "良好")
        with feedback_cols[1]:
            st.metric("结构化程度", "75%", "需改进")
        with feedback_cols[2]:
            st.metric("岗位契合度", "88%", "优秀")
        
        st.markdown("### 改进建议")
        st.markdown("""
        1. **结构化表达**：多使用STAR法则，让回答更有条理
        2. **具体案例**：每个观点都配上一个实际例子
        3. **岗位关联**：将个人经历与目标岗位要求更紧密结合
        4. **简洁性**：避免冗长，核心观点前置
        """)
        
        if st.button("重新开始面试"):
            st.session_state.interview_step = 0
            st.session_state.user_answers = []
            st.rerun()

# 页脚
st.markdown("---")
st.caption("AI职业发展助手 Demo Version 1.0 | 数据仅供参考，建议结合个人实际情况使用")
