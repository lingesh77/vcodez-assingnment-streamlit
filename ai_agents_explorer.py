import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="AI Agents Explorer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #1E3A8A;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #1E40AF;
        margin: 1rem 0;
        border-bottom: 3px solid #3B82F6;
        padding-bottom: 0.5rem;
    }
    
    .agent-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #3B82F6;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        color: #1F2937;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F3F4F6 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #3B82F6;
        color: #1F2937;
    }
    
    .callout-info {
        background-color: #FFFFFF;
        border: 2px solid #3B82F6;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: #1F2937;
        box-shadow: 0 2px 4px rgba(59, 130, 246, 0.1);
    }
    
    .callout-success {
        background-color: #FFFFFF;
        border: 2px solid #10B981;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: #1F2937;
        box-shadow: 0 2px 4px rgba(16, 185, 129, 0.1);
    }
    
    .callout-warning {
        background-color: #FFFFFF;
        border: 2px solid #F59E0B;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: #1F2937;
        box-shadow: 0 2px 4px rgba(245, 158, 11, 0.1);
    }
    
    .sidebar-section {
        padding: 0.5rem 0;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 0.5rem;
    }
    
    /* Ensure good text contrast in all elements */
    .agent-card h3, .agent-card p, .agent-card strong {
        color: #1F2937 !important;
    }
    
    .callout-info h3, .callout-info p {
        color: #1F2937 !important;
    }
    
    .callout-success h3, .callout-success p {
        color: #1F2937 !important;
    }
    
    .metric-card h2, .metric-card p {
        color: #1F2937 !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 🧭 Navigation")
sections = [
    ("🏠 Home", "home"),
    ("🤖 Types of AI Agents", "types"),
    ("🌍 Applications", "applications"),
    ("📊 Comparison", "comparison"),
    ("ℹ️ About", "about")
]

# Create sidebar navigation
selected_section = st.sidebar.radio("Select a section:", [section[0] for section in sections], key="navigation")
current_section = next(section[1] for section in sections if section[0] == selected_section)

# Helper function to create agent cards
def create_agent_card(title, icon, definition, examples, characteristics):
    st.markdown(f"""
    <div class="agent-card">
        <h3>{icon} {title}</h3>
        <p><strong>Definition:</strong> {definition}</p>
        <p><strong>Examples:</strong> {examples}</p>
        <p><strong>Key Characteristics:</strong> {characteristics}</p>
    </div>
    """, unsafe_allow_html=True)

# Home Section
if current_section == "home":
    st.markdown('<h1 class="main-header">🤖 AI Agents Explorer</h1>', unsafe_allow_html=True)
    
    # Banner area
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Create a simple banner placeholder
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%); 
                    padding: 3rem; border-radius: 20px; text-align: center; color: white; margin: 2rem 0;">
            <h2>🚀 Explore the World of AI Agents</h2>
            <p style="font-size: 1.2rem; margin-top: 1rem;">Discover different types of intelligent agents and their applications</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Introduction
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="callout-info">
            <h3 style="color: #1E40AF;">🎯 What are AI Agents?</h3>
            <p style="color: #374151; font-size: 1rem; line-height: 1.6;">AI agents are autonomous entities that perceive their environment through sensors and act upon 
            that environment through actuators to achieve specific goals. They can range from simple reactive 
            systems to complex learning entities.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="callout-success">
            <h3 style="color: #059669;">✨ Why Learn About AI Agents?</h3>
            <p style="color: #374151; font-size: 1rem; line-height: 1.6;">Understanding AI agents is crucial for anyone working in AI/ML, robotics, or automation. 
            They form the backbone of intelligent systems in various industries from healthcare to finance.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown('<h2 class="section-header">📈 Quick Stats</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2 style="color: #3B82F6;">5</h2>
            <p>Types of Agents</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2 style="color: #10B981;">50+</h2>
            <p>Applications</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2 style="color: #F59E0B;">10+</h2>
            <p>Industries</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2 style="color: #EF4444;">∞</h2>
            <p>Possibilities</p>
        </div>
        """, unsafe_allow_html=True)

# Types of AI Agents Section
elif current_section == "types":
    st.markdown('<h1 class="main-header">🤖 Types of AI Agents</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="callout-info">
        <p style="color: #374151; font-size: 1.1rem; line-height: 1.6;">AI agents can be classified into different types based on their capabilities, architecture, and behavior. 
        Each type has unique characteristics that make them suitable for specific applications.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Agent types with expandable sections
    agent_types = [
        {
            "title": "Reactive Agents",
            "icon": "⚡",
            "definition": "Simple agents that respond directly to environmental stimuli without internal state representation.",
            "examples": "Thermostats, simple chatbots, reflex-based game NPCs",
            "characteristics": "Fast response, no memory, condition-action rules",
            "diagram": "Sensors → Condition-Action Rules → Actuators"
        },
        {
            "title": "Model-based Agents",
            "icon": "🧠",
            "definition": "Agents that maintain an internal model of the world to make informed decisions.",
            "examples": "Navigation systems, autonomous vehicles, smart home systems",
            "characteristics": "Internal world model, state tracking, predictive capabilities",
            "diagram": "Sensors → World Model → Decision Logic → Actuators"
        },
        {
            "title": "Goal-based Agents",
            "icon": "🎯",
            "definition": "Agents that work towards achieving specific goals using planning and reasoning.",
            "examples": "Path-finding algorithms, automated planning systems, game AI",
            "characteristics": "Goal representation, planning algorithms, flexible behavior",
            "diagram": "Goals → Planning → Actions → Environment"
        },
        {
            "title": "Utility-based Agents",
            "icon": "⚖️",
            "definition": "Agents that maximize utility functions to make optimal decisions among alternatives.",
            "examples": "Trading algorithms, resource optimization systems, recommendation engines",
            "characteristics": "Utility functions, optimization, decision theory",
            "diagram": "Options → Utility Calculation → Optimal Choice → Action"
        },
        {
            "title": "Learning Agents",
            "icon": "📚",
            "definition": "Agents that improve their performance over time through experience and learning.",
            "examples": "Neural networks, reinforcement learning agents, adaptive systems",
            "characteristics": "Learning algorithms, performance improvement, adaptation",
            "diagram": "Experience → Learning → Knowledge Update → Better Performance"
        }
    ]
    
    for agent in agent_types:
        with st.expander(f"{agent['icon']} {agent['title']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Definition:** {agent['definition']}")
                st.markdown(f"**Examples:** {agent['examples']}")
                st.markdown(f"**Key Characteristics:** {agent['characteristics']}")
            
            with col2:
                st.markdown("**Architecture:**")
                st.code(agent['diagram'], language=None)
                
                # Add a simple performance metric visualization
                if agent['title'] == "Learning Agents":
                    performance_data = np.random.exponential(scale=2, size=100).cumsum()
                    fig = px.line(x=range(len(performance_data)), y=performance_data, 
                                title="Learning Curve Example")
                    fig.update_layout(height=200, margin=dict(l=0, r=0, t=30, b=0))
                    st.plotly_chart(fig, use_container_width=True)

# Applications Section
elif current_section == "applications":
    st.markdown('<h1 class="main-header">🌍 Real-World Applications</h1>', unsafe_allow_html=True)
    
    # Create tabs for different application domains
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🤖 Robotics", "💰 Finance", "🏥 Healthcare", "📚 Education", "📞 Customer Service"])
    
    with tab1:
        st.markdown("### Robotics Applications")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Manufacturing Robots (Model-based)**
            - Assembly line automation
            - Quality control systems
            - Predictive maintenance
            
            **Service Robots (Goal-based)**
            - Cleaning robots (Roomba)
            - Delivery drones
            - Personal assistants
            """)
        
        with col2:
            st.markdown("""
            **Autonomous Vehicles (Utility-based)**
            - Self-driving cars
            - Traffic optimization
            - Route planning
            
            **Exploration Robots (Learning)**
            - Mars rovers
            - Deep-sea exploration
            - Search and rescue
            """)
    
    with tab2:
        st.markdown("### Finance Applications")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Trading Systems (Utility-based)**
            - Algorithmic trading
            - Risk management
            - Portfolio optimization
            
            **Fraud Detection (Learning)**
            - Pattern recognition
            - Anomaly detection
            - Real-time monitoring
            
            **Customer Service (Reactive)**
            - Chatbots for banking
            - Automated responses
            - Basic query handling
            """)
        
        with col2:
            # Create a pie chart for finance applications
            finance_data = {
                'Application': ['Trading', 'Fraud Detection', 'Customer Service', 'Risk Analysis', 'Others'],
                'Percentage': [30, 25, 20, 15, 10]
            }
            fig = px.pie(finance_data, values='Percentage', names='Application', 
                        title='AI Agent Distribution in Finance')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### Healthcare Applications")
        
        healthcare_apps = {
            'Agent Type': ['Reactive', 'Model-based', 'Goal-based', 'Utility-based', 'Learning'],
            'Healthcare Application': [
                'Vital sign monitors',
                'Diagnostic imaging',
                'Treatment planning',
                'Drug discovery',
                'Personalized medicine'
            ],
            'Impact Score': [7, 8, 9, 8, 10]
        }
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            df_health = pd.DataFrame(healthcare_apps)
            st.dataframe(df_health, hide_index=True)
        
        with col2:
            fig = px.bar(healthcare_apps, x='Agent Type', y='Impact Score', 
                        title='Impact Score by Agent Type in Healthcare')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.markdown("### Education Applications")
        st.markdown("""
        **Adaptive Learning Systems (Learning Agents)**
        - Personalized curriculum
        - Performance tracking
        - Skill gap analysis
        
        **Intelligent Tutoring (Goal-based)**
        - Interactive problem solving
        - Guided learning paths
        - Assessment systems
        
        **Administrative Automation (Reactive)**
        - Enrollment processing
        - Scheduling systems
        - Basic student queries
        """)
        
        # Education metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Student Engagement", "85%", "+12%")
        with col2:
            st.metric("Learning Efficiency", "78%", "+25%")
        with col3:
            st.metric("Cost Reduction", "45%", "+8%")
    
    with tab5:
        st.markdown("### Customer Service Applications")
        
        # Interactive chart showing customer service agent evolution
        cs_evolution = {
            'Year': [2020, 2021, 2022, 2023, 2024, 2025],
            'Reactive Agents': [60, 55, 45, 35, 25, 20],
            'Learning Agents': [10, 15, 25, 35, 45, 50],
            'Hybrid Systems': [30, 30, 30, 30, 30, 30]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=cs_evolution['Year'], y=cs_evolution['Reactive Agents'], 
                                mode='lines+markers', name='Reactive Agents'))
        fig.add_trace(go.Scatter(x=cs_evolution['Year'], y=cs_evolution['Learning Agents'], 
                                mode='lines+markers', name='Learning Agents'))
        fig.add_trace(go.Scatter(x=cs_evolution['Year'], y=cs_evolution['Hybrid Systems'], 
                                mode='lines+markers', name='Hybrid Systems'))
        
        fig.update_layout(title='Evolution of Customer Service AI Agents',
                         xaxis_title='Year', yaxis_title='Usage Percentage (%)')
        st.plotly_chart(fig, use_container_width=True)

# Comparison Section
elif current_section == "comparison":
    st.markdown('<h1 class="main-header">📊 Agent Types Comparison</h1>', unsafe_allow_html=True)
    
    # Comprehensive comparison table
    comparison_data = {
        'Agent Type': ['Reactive', 'Model-based', 'Goal-based', 'Utility-based', 'Learning'],
        'Complexity': ['Low', 'Medium', 'Medium-High', 'High', 'Very High'],
        'Memory Usage': ['None', 'Medium', 'High', 'Medium', 'High'],
        'Adaptability': ['None', 'Low', 'Medium', 'Medium', 'High'],
        'Performance': ['Fast', 'Medium', 'Medium', 'Optimal', 'Improving'],
        'Implementation Cost': ['Low', 'Medium', 'High', 'High', 'Very High'],
        'Maintenance': ['Easy', 'Medium', 'Hard', 'Hard', 'Complex'],
        'Best Use Case': ['Simple tasks', 'Known environments', 'Planning problems', 'Optimization', 'Dynamic environments']
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    
    # Display the comparison table with custom styling
    st.markdown("### 🔍 Detailed Comparison Table")
    st.dataframe(df_comparison, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Feature comparison charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ⚡ Performance Characteristics")
        performance_data = {
            'Agent Type': ['Reactive', 'Model-based', 'Goal-based', 'Utility-based', 'Learning'],
            'Speed': [9, 7, 6, 5, 4],
            'Accuracy': [6, 7, 8, 9, 8],
            'Flexibility': [2, 4, 7, 6, 9]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=performance_data['Speed'], theta=performance_data['Agent Type'], 
                                     fill='toself', name='Speed'))
        fig.add_trace(go.Scatterpolar(r=performance_data['Accuracy'], theta=performance_data['Agent Type'], 
                                     fill='toself', name='Accuracy'))
        fig.add_trace(go.Scatterpolar(r=performance_data['Flexibility'], theta=performance_data['Agent Type'], 
                                     fill='toself', name='Flexibility'))
        
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 💰 Cost vs Benefit Analysis")
        cost_benefit = {
            'Agent Type': ['Reactive', 'Model-based', 'Goal-based', 'Utility-based', 'Learning'],
            'Development Cost': [1, 3, 5, 7, 9],
            'Business Value': [3, 5, 7, 8, 10],
            'ROI Score': [3, 1.67, 1.4, 1.14, 1.11]  # Value/Cost ratio
        }
        
        fig = px.scatter(cost_benefit, x='Development Cost', y='Business Value', 
                        size='ROI Score', hover_name='Agent Type',
                        title='Cost vs Benefit Analysis',
                        labels={'Development Cost': 'Development Cost (1-10)', 
                               'Business Value': 'Business Value (1-10)'})
        st.plotly_chart(fig, use_container_width=True)
    
    # Decision matrix
    st.markdown("### 🤔 Decision Matrix: Which Agent Type to Choose?")
    
    decision_scenarios = {
        'Scenario': [
            'Simple automation task',
            'Known environment with changes',
            'Complex problem solving',
            'Resource optimization',
            'Continuous improvement needed'
        ],
        'Recommended Agent': [
            'Reactive Agent ⚡',
            'Model-based Agent 🧠',
            'Goal-based Agent 🎯',
            'Utility-based Agent ⚖️',
            'Learning Agent 📚'
        ],
        'Reasoning': [
            'Fast, simple, cost-effective',
            'Can handle environmental changes',
            'Planning capabilities required',
            'Need to maximize objectives',
            'Environment is dynamic/unknown'
        ]
    }
    
    df_decision = pd.DataFrame(decision_scenarios)
    st.table(df_decision)

# About Section
elif current_section == "about":
    st.markdown('<h1 class="main-header">ℹ️ About This App</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="callout-info">
            <h3>🚀 AI Agents Explorer</h3>
            <p>This interactive web application was designed to provide a comprehensive overview of different 
            types of AI agents, their characteristics, and real-world applications. Whether you're a student, 
            researcher, or industry professional, this tool offers valuable insights into the world of 
            intelligent agents.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Features")
        st.markdown("""
        - **Interactive Navigation**: Easy-to-use sidebar navigation
        - **Comprehensive Coverage**: All major agent types explained
        - **Real-world Applications**: Practical examples across industries
        - **Visual Comparisons**: Charts and tables for easy understanding
        - **Modern Design**: Clean, responsive interface
        - **Educational Focus**: Perfect for learning and teaching
        """)
        
        st.markdown("### 🛠️ Built With")
        tech_col1, tech_col2 = st.columns(2)
        
        with tech_col1:
            st.markdown("""
            - **Streamlit** - Web framework
            - **Plotly** - Interactive charts
            - **Pandas** - Data manipulation
            - **NumPy** - Numerical computing
            """)
        
        with tech_col2:
            st.markdown("""
            - **Python** - Core language
            - **CSS** - Custom styling
            - **HTML** - Structure
            - **JavaScript** - Interactivity
            """)
    
    with col2:
        st.markdown("""
        <div class="callout-success">
            <h3>👨‍💻 About the Creator</h3>
            <p><strong>AI Development Team</strong></p>
            <p>Passionate about making AI education accessible and engaging for everyone.</p>
            
            <h4>🔗 Useful Links</h4>
            <ul>
                <li><a href="https://streamlit.io" target="_blank">Streamlit Documentation</a></li>
                <li><a href="https://plotly.com/python/" target="_blank">Plotly Python</a></li>
                <li><a href="https://pandas.pydata.org" target="_blank">Pandas Documentation</a></li>
                <li><a href="https://github.com" target="_blank">Source Code</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # App statistics
        st.markdown("### 📈 App Statistics")
        stat_col1, stat_col2 = st.columns(2)
        
        with stat_col1:
            st.metric("Lines of Code", "400+")
            st.metric("Interactive Charts", "8")
        
        with stat_col2:
            st.metric("Agent Types", "5")
            st.metric("Application Examples", "20+")
    
    st.markdown("---")
    
    # Feedback section
    st.markdown("### 💬 Feedback & Suggestions")
    
    feedback_col1, feedback_col2 = st.columns([2, 1])
    
    with feedback_col1:
        feedback = st.text_area("Share your thoughts about this app:", 
                               placeholder="Your feedback helps us improve...")
        
        if st.button("Submit Feedback", type="primary"):
            if feedback:
                st.success("Thank you for your feedback! 🙏")
            else:
                st.warning("Please enter some feedback before submitting.")
    
    with feedback_col2:
        st.markdown("""
        <div style="background: #F0FDF4; padding: 1rem; border-radius: 8px; border: 1px solid #22C55E;">
            <h4>🌟 Rate this App</h4>
            <p>How would you rate your experience?</p>
        </div>
        """, unsafe_allow_html=True)
        
        rating = st.select_slider("", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
        
        if st.button("Submit Rating"):
            st.balloons()
            st.success(f"Thanks for rating us {rating}!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; padding: 2rem 0;">
    <p>Made with ❤️ using Streamlit | © 2025 AI Agents Explorer</p>
    <p><em>"Understanding AI Agents, One Type at a Time"</em></p>
</div>
""", unsafe_allow_html=True)