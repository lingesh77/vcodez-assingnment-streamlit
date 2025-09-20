import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI Agents Explained", 
    page_icon="🤖", 
    layout="centered"
)

# Enhanced CSS styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 3rem;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        color: #1F2937;
        border-left: 5px solid #3B82F6;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
    }
    
    .agent-card {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.1);
        border: 2px solid #93C5FD;
        color: #1F2937;
    }
    
    .example-box {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #22C55E;
        color: #1F2937;
    }
    
    .feature-box {
        background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #F59E0B;
        color: #92400E;
        font-weight: 500;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #F3F4F6 0%, #E5E7EB 100%);
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        min-width: 100px;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #3B82F6;
    }
    
    .stat-label {
        color: #6B7280;
        font-size: 0.9rem;
    }
    
    .highlight {
        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #EF4444;
        margin: 1rem 0;
        color: #7F1D1D;
    }
    
    .comparison-table {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main title with emoji
st.markdown('<h1 class="main-title">🤖 AI Agents: A Complete Guide</h1>', unsafe_allow_html=True)

# Introduction section
st.markdown('''
<div class="card">
    <h2>🎯 What is an AI Agent?</h2>
    <p style="font-size: 1.1rem; line-height: 1.6;">
        An AI agent is a <strong>smart system</strong> that can perceive its environment, make decisions, 
        and take actions to achieve specific goals. Think of them as digital assistants that can 
        <em>sense, think, and act</em> autonomously!
    </p>
    <div class="feature-box">
        💡 <strong>Fun Fact:</strong> AI agents can be as simple as a thermostat controlling temperature 
        or as complex as self-driving cars navigating busy streets!
    </div>
</div>
''', unsafe_allow_html=True)

# Quick stats
st.markdown('''
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">4</div>
        <div class="stat-label">Main Types</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">100+</div>
        <div class="stat-label">Applications</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">∞</div>
        <div class="stat-label">Possibilities</div>
    </div>
</div>
''', unsafe_allow_html=True)

# Types of AI Agents section
st.markdown('''
<div class="card">
    <h2>🔧 Types of AI Agents</h2>
    <p style="color: #4B5563; margin-bottom: 1.5rem;">
        Each type of AI agent has unique capabilities and is designed for specific tasks:
    </p>
</div>
''', unsafe_allow_html=True)

# Agent types with examples
agent_data = {
    "Reactive": {
        "emoji": "⚡",
        "description": "React instantly to current situations without memory",
        "examples": ["Smart thermostats", "Basic chatbots", "Automatic doors", "Fire alarms"],
        "pros": ["Very fast response", "Simple to build", "Low cost"],
        "cons": ["No learning", "Limited intelligence", "Can't handle complex tasks"]
    },
    "Model-based": {
        "emoji": "🧠",
        "description": "Use internal models to understand and predict the world",
        "examples": ["GPS navigation", "Weather prediction", "Smart home systems", "Medical diagnosis"],
        "pros": ["Handles uncertainty", "Better decisions", "Works in complex environments"],
        "cons": ["More complex", "Requires good models", "Higher computational cost"]
    },
    "Goal-based": {
        "emoji": "🎯",
        "description": "Plan and execute actions to achieve specific objectives",
        "examples": ["Chess AI", "Route planning", "Project management tools", "Game NPCs"],
        "pros": ["Flexible behavior", "Can plan ahead", "Achieves complex goals"],
        "cons": ["Computationally expensive", "May be slow", "Complex to design"]
    },
    "Learning": {
        "emoji": "📚",
        "description": "Improve performance over time through experience",
        "examples": ["Netflix recommendations", "Email spam filters", "Voice assistants", "Trading bots"],
        "pros": ["Gets better over time", "Adapts to changes", "Handles new situations"],
        "cons": ["Unpredictable", "Requires training data", "Can be biased"]
    }
}

# Interactive agent selector
st.markdown("### 🔍 Explore Each Agent Type")
agent_type = st.selectbox(
    "Choose an agent type to learn more:",
    ["Reactive", "Model-based", "Goal-based", "Learning"],
    help="Select different types to see detailed information about each one"
)

# Display detailed information for selected agent
if agent_type in agent_data:
    agent_info = agent_data[agent_type]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f'''
        <div class="agent-card">
            <h3>{agent_info["emoji"]} {agent_type} Agents</h3>
            <p style="font-size: 1.1rem; margin-bottom: 1rem;">{agent_info["description"]}</p>
            
            <h4>✅ Advantages:</h4>
            <ul>
                {"".join([f"<li>{pro}</li>" for pro in agent_info["pros"]])}
            </ul>
            
            <h4>❌ Limitations:</h4>
            <ul>
                {"".join([f"<li>{con}</li>" for con in agent_info["cons"]])}
            </ul>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 🌟 Real Examples:")
        for example in agent_info["examples"]:
            st.markdown(f'''
            <div class="example-box">
                🔸 {example}
            </div>
            ''', unsafe_allow_html=True)

# How AI Agents Work section
st.markdown('''
<div class="card">
    <h2>⚙️ How Do AI Agents Work?</h2>
    <p>AI agents follow a simple but powerful cycle:</p>
</div>
''', unsafe_allow_html=True)

# Interactive workflow
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('''
    <div style="text-align: center; padding: 1rem; background: #EFF6FF; border-radius: 10px; margin: 0.5rem;">
        <h3>👁️</h3>
        <h4>Perceive</h4>
        <p>Gather information from environment</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div style="text-align: center; padding: 1rem; background: #F0FDF4; border-radius: 10px; margin: 0.5rem;">
        <h3>🤔</h3>
        <h4>Think</h4>
        <p>Process information and make decisions</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown('''
    <div style="text-align: center; padding: 1rem; background: #FEF3C7; border-radius: 10px; margin: 0.5rem;">
        <h3>⚡</h3>
        <h4>Act</h4>
        <p>Take action based on decisions</p>
    </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown('''
    <div style="text-align: center; padding: 1rem; background: #FEE2E2; border-radius: 10px; margin: 0.5rem;">
        <h3>📈</h3>
        <h4>Learn</h4>
        <p>Improve from results (some agents)</p>
    </div>
    ''', unsafe_allow_html=True)

# Applications section
st.markdown('''
<div class="card">
    <h2>🌍 Where Do We Find AI Agents?</h2>
    <p>AI agents are everywhere in our daily lives! Here are some common applications:</p>
</div>
''', unsafe_allow_html=True)

# Application categories
applications = {
    "🏠 Home": ["Smart speakers (Alexa, Google)", "Smart thermostats", "Robot vacuums", "Security systems"],
    "📱 Technology": ["Smartphone assistants", "Email filters", "Recommendation systems", "Search engines"],
    "🚗 Transportation": ["GPS navigation", "Self-driving cars", "Traffic management", "Ride-sharing apps"],
    "🏥 Healthcare": ["Medical diagnosis", "Drug discovery", "Patient monitoring", "Surgery robots"],
    "💼 Business": ["Customer service bots", "Fraud detection", "Trading systems", "Project management"]
}

tabs = st.tabs(list(applications.keys()))

for i, (category, items) in enumerate(applications.items()):
    with tabs[i]:
        for item in items:
            st.markdown(f'''
            <div class="example-box">
                🤖 <strong>{item}</strong> - Uses AI agents to automate and improve performance
            </div>
            ''', unsafe_allow_html=True)

# Comparison table
st.markdown('''
<div class="card">
    <h2>📊 Quick Comparison</h2>
    <div class="comparison-table">
''', unsafe_allow_html=True)

comparison_data = {
    'Agent Type': ['Reactive ⚡', 'Model-based 🧠', 'Goal-based 🎯', 'Learning 📚'],
    'Speed': ['Very Fast', 'Fast', 'Medium', 'Medium'],
    'Intelligence': ['Low', 'Medium', 'High', 'Very High'],
    'Complexity': ['Simple', 'Medium', 'Complex', 'Very Complex'],
    'Cost': ['Low', 'Medium', 'High', 'High'],
    'Best For': ['Simple tasks', 'Known environments', 'Planning', 'Adaptation']
}

df = pd.DataFrame(comparison_data)
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# Future section
st.markdown('''
<div class="card">
    <h2>🚀 The Future of AI Agents</h2>
    <p>AI agents are becoming more sophisticated and will soon be able to:</p>
    <ul>
        <li>🧠 <strong>Think more like humans</strong> with advanced reasoning</li>
        <li>🤝 <strong>Collaborate better</strong> with humans and other agents</li>
        <li>🌐 <strong>Work across multiple domains</strong> simultaneously</li>
        <li>🎯 <strong>Achieve complex goals</strong> with minimal human input</li>
        <li>🔒 <strong>Operate safely and ethically</strong> in all situations</li>
    </ul>
</div>
''', unsafe_allow_html=True)

# Why important section
st.markdown('''
<div class="highlight">
    <h3>🎯 Why Are AI Agents Important?</h3>
    <p>AI agents are revolutionizing how we interact with technology. They help us:</p>
    <ul>
        <li><strong>Save time</strong> by automating repetitive tasks</li>
        <li><strong>Make better decisions</strong> with data-driven insights</li>
        <li><strong>Solve complex problems</strong> that humans can't handle alone</li>
        <li><strong>Improve quality of life</strong> through personalized experiences</li>
    </ul>
</div>
''', unsafe_allow_html=True)

# Interactive quiz section
st.markdown("### 🧠 Test Your Knowledge!")

quiz_question = st.radio(
    "Which type of AI agent would be best for a chess-playing program?",
    ["Reactive Agent - for quick responses", 
     "Model-based Agent - for understanding the board", 
     "Goal-based Agent - for planning moves to win",
     "Learning Agent - for improving over time"],
    help="Think about what a chess program needs to do to play well"
)

if st.button("Check Answer"):
    if "Goal-based Agent" in quiz_question:
        st.success("🎉 Correct! Goal-based agents are perfect for chess because they can plan multiple moves ahead to achieve the goal of winning!")
        st.balloons()
    else:
        st.error("❌ Not quite! While other agents have their uses, goal-based agents are best for chess because they can plan strategic moves to achieve the goal of winning the game.")

# Interactive examples
st.markdown("### 🎮 Try It Yourself!")

example_type = st.selectbox(
    "Choose a scenario to see which AI agent would work best:",
    ["Smart Home Temperature Control", 
     "Email Spam Detection", 
     "GPS Route Planning", 
     "Movie Recommendations"]
)

scenarios = {
    "Smart Home Temperature Control": {
        "agent": "Reactive Agent ⚡",
        "reason": "Perfect for simple if-then rules: if temperature > 75°F, turn on AC",
        "color": "#EFF6FF"
    },
    "Email Spam Detection": {
        "agent": "Learning Agent 📚", 
        "reason": "Gets better at detecting new spam patterns over time",
        "color": "#F0FDF4"
    },
    "GPS Route Planning": {
        "agent": "Model-based Agent 🧠",
        "reason": "Uses maps and traffic models to find optimal routes", 
        "color": "#FEF3C7"
    },
    "Movie Recommendations": {
        "agent": "Learning Agent 📚",
        "reason": "Learns your preferences and improves suggestions over time",
        "color": "#FEE2E2"
    }
}

if example_type in scenarios:
    scenario = scenarios[example_type]
    st.markdown(f'''
    <div style="background: {scenario["color"]}; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
        <h4>Best Choice: {scenario["agent"]}</h4>
        <p><strong>Why?</strong> {scenario["reason"]}</p>
    </div>
    ''', unsafe_allow_html=True)

# Footer with call to action
st.markdown("---")
st.markdown('''
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%); 
           border-radius: 15px; color: white; margin: 2rem 0;">
    <h3>🌟 Ready to Dive Deeper?</h3>
    <p>AI agents are shaping the future of technology. Understanding them today will help you navigate tomorrow's world!</p>
    <p style="font-style: italic;">"The best way to predict the future is to create it with AI agents."</p>
</div>
''', unsafe_allow_html=True)

# Feedback section
with st.expander("💬 Share Your Thoughts"):
    feedback = st.text_area("What did you think about this guide?", placeholder="Your feedback helps us improve...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Helpful", use_container_width=True):
            st.success("Thanks for the positive feedback! 😊")
    with col2:
        if st.button("📝 Submit Feedback", use_container_width=True):
            if feedback:
                st.success("Thank you for your detailed feedback! 🙏")
            else:
                st.warning("Please enter some feedback first!")