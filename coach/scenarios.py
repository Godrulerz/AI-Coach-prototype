# Coaching scenarios and conversation flows

# Common coaching topics and their associated responses for different coaching styles
COACHING_SCENARIOS = {
    "goal_setting": {
        "keywords": ["goal", "objective", "target", "aim", "aspiration"],
        "responses": {
            "supportive": [
                "That's a wonderful goal! I believe in your ability to achieve it. What's the first small step you can take toward this goal?",
                "I'm excited about this goal for you! Breaking it down into smaller steps will make it more manageable. What would be a good first step?",
                "This goal aligns well with your strengths. How can you leverage those strengths to make progress?"
            ],
            "challenging": [
                "Is this goal challenging enough for you? What would make it stretch your capabilities even further?",
                "How will you measure success for this goal? What specific metrics will tell you you've achieved it?",
                "What obstacles do you anticipate in pursuing this goal, and how will you overcome them?"
            ],
            "analytical": [
                "Let's analyze this goal using the SMART framework. Is it Specific, Measurable, Achievable, Relevant, and Time-bound?",
                "What data points will you track to measure progress toward this goal? How will you collect and analyze that data?",
                "Based on your past performance patterns, what strategies are most likely to help you succeed with this goal?"
            ]
        }
    },
    "obstacle_handling": {
        "keywords": ["obstacle", "challenge", "difficulty", "problem", "barrier", "stuck"],
        "responses": {
            "supportive": [
                "Facing obstacles shows you're pushing your boundaries. What resources or support could help you overcome this challenge?",
                "It's normal to encounter difficulties on your journey. What has helped you overcome similar challenges in the past?",
                "You have the inner strength to overcome this. What would make this obstacle feel more manageable?"
            ],
            "challenging": [
                "What's the worst that could happen if you fail to overcome this obstacle? And how likely is that outcome, really?",
                "How might this obstacle actually be pointing you toward a better approach or solution?",
                "If your best friend faced this same challenge, what advice would you give them? Why aren't you taking that advice yourself?"
            ],
            "analytical": [
                "Let's break down this obstacle into its component parts. Which specific element is causing the most difficulty?",
                "On a scale of 1-10, how significant is this obstacle to your overall progress? What data supports that rating?",
                "What patterns do you notice in the obstacles that typically challenge you? How does this one fit those patterns?"
            ]
        }
    },
    "motivation": {
        "keywords": ["motivation", "inspired", "energized", "drive", "passion", "enthusiasm", "unmotivated", "procrastinating"],
        "responses": {
            "supportive": [
                "Remember why you started this journey. Connecting with your purpose can reignite your motivation. What initially inspired you?",
                "It's okay to have fluctuations in motivation. What small action could you take today that would feel good to complete?",
                "Your past successes show your capability. What achievement are you most proud of, and how can that energy help you now?"
            ],
            "challenging": [
                "What's the cost of remaining unmotivated? What opportunities are you missing by not taking action?",
                "If motivation is what you're waiting for, you might be waiting a long time. How can you act despite not feeling motivated?",
                "Who are you letting down by not pursuing this goal with full energy? Yourself? Others who believe in you?"
            ],
            "analytical": [
                "Let's track your motivation levels throughout the day. When are they highest? How can you leverage those peak times?",
                "What patterns do you notice in activities that energize versus drain you? How can you restructure your approach based on this data?",
                "Consider the environmental factors affecting your motivation. What specific changes to your environment could support higher motivation?"
            ]
        }
    },
    "progress_review": {
        "keywords": ["progress", "improvement", "advancement", "growth", "development", "milestone"],
        "responses": {
            "supportive": [
                "You've made meaningful progress! Each step forward is worth celebrating. What aspect of your growth are you most proud of?",
                "I notice significant improvement in how you're approaching this. What do you think has contributed most to your progress?",
                "Your persistence is paying off. How does it feel to see the progress you've made so far?"
            ],
            "challenging": [
                "This is good progress, but where could you have pushed yourself further? What's still left on the table?",
                "How does this progress compare to your original timeline and expectations? Are you truly satisfied with the pace?",
                "What would it take to double your rate of progress from here? What would need to change?"
            ],
            "analytical": [
                "Looking at your progress metrics, I notice patterns in your rate of improvement. What factors accelerated progress in these areas?",
                "Let's compare your progress against industry or domain benchmarks. How does your growth rate compare to typical expectations?",
                "The data shows variable progress across different aspects of your goal. What might explain these variations?"
            ]
        }
    },
    "decision_making": {
        "keywords": ["decision", "choice", "option", "alternative", "path", "direction", "crossroads"],
        "responses": {
            "supportive": [
                "You have good instincts. When you quiet external noise, what is your intuition telling you about this decision?",
                "All of these options have merit. Which one aligns most closely with your core values and what matters most to you?",
                "You've made good decisions before. What approach to decision-making has served you well in the past?"
            ],
            "challenging": [
                "What's the real risk in this decision? Are you overestimating the downside or underestimating your ability to handle consequences?",
                "If you were advising someone else facing this exact choice, what would you tell them? Why the difference in how you approach it for yourself?",
                "Fast forward one year: which decision would your future self thank you for making today?"
            ],
            "analytical": [
                "Let's create a decision matrix with your options and key criteria. How would you weight each factor in importance?",
                "What additional data would make this decision clearer? How can you gather that information efficiently?",
                "Looking at historical data from similar decisions, what patterns emerge that might inform this choice?"
            ]
        }
    },
    "work_life_balance": {
        "keywords": ["balance", "burnout", "overwhelmed", "stress", "overworked", "boundaries", "self-care"],
        "responses": {
            "supportive": [
                "Your wellbeing matters. What small self-care practice could you incorporate into your daily routine?",
                "Setting boundaries is an act of self-respect. Which boundary would most support your wellbeing right now?",
                "It takes courage to acknowledge when things are out of balance. What would a more balanced life look and feel like for you?"
            ],
            "challenging": [
                "What's driving this imbalance? What beliefs or fears make it difficult for you to step back when needed?",
                "Who are you trying to prove something to by maintaining this pace? What would happen if you prioritized your wellbeing instead?",
                "How sustainable is your current approach? What's the long-term cost of continuing this way?"
            ],
            "analytical": [
                "Let's track how you're allocating hours across different life domains. Where are the biggest imbalances in time allocation?",
                "On a scale of 1-10, how would you rate your energy levels throughout the typical week? What patterns do you notice?",
                "What metrics beyond productivity could you track to measure your overall wellbeing and life satisfaction?"
            ]
        }
    },
    "skill_development": {
        "keywords": ["skill", "learn", "develop", "improve", "master", "practice", "training"],
        "responses": {
            "supportive": [
                "Learning new skills takes courage. What aspect of this skill development journey excites you the most?",
                "Everyone starts as a beginner. What small win in your practice recently shows you're making progress?",
                "Your dedication to growth is admirable. How can you make the learning process more enjoyable?"
            ],
            "challenging": [
                "How are you pushing beyond your comfort zone in practicing this skill? Where could you add more deliberate challenge?",
                "Who are the masters in this field that you're studying? What specifically are you adapting from their approach?",
                "What feedback have you sought on your current skill level? How are you systematically addressing improvement areas?"
            ],
            "analytical": [
                "Research shows that deliberate practice with feedback loops accelerates skill development. How are you structuring your practice sessions?",
                "Let's break down this skill into its component sub-skills. Which specific elements need the most development?",
                "What metrics are you using to track your skill improvement? How can we make these measurements more objective?"
            ]
        }
    }
}

# Helper function to identify scenario from message
def identify_scenario(message):
    """Identify which coaching scenario matches the user's message
    
    Args:
        message (str): The user's message
        
    Returns:
        str: The identified scenario key, or None if no match
    """
    message_lower = message.lower()
    
    for scenario, data in COACHING_SCENARIOS.items():
        for keyword in data["keywords"]:
            if keyword in message_lower:
                return scenario
    
    return None

# Helper function to get appropriate response for a scenario and coaching style
def get_scenario_response(scenario, coaching_style):
    """Get an appropriate response for the identified scenario and coaching style
    
    Args:
        scenario (str): The identified coaching scenario
        coaching_style (str): The coaching style to use
        
    Returns:
        str: A coaching response appropriate for the scenario and style
    """
    import random
    
    if scenario not in COACHING_SCENARIOS:
        return None
    
    # Default to supportive if coaching style not found
    if coaching_style not in COACHING_SCENARIOS[scenario]["responses"]:
        coaching_style = "supportive"
    
    responses = COACHING_SCENARIOS[scenario]["responses"][coaching_style]
    return random.choice(responses)