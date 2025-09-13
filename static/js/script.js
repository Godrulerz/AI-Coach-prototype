// AI Coaching Agent - Frontend Script

// DOM Elements
const chatMessages = document.getElementById('chat-messages');
const messageForm = document.getElementById('message-form');
const userMessageInput = document.getElementById('user-message');
const coachingStyleSelect = document.getElementById('coaching-style');
const goalsList = document.getElementById('goals-list');
const insightsList = document.getElementById('insights-list');
const addGoalForm = document.getElementById('add-goal-form');
const newGoalInput = document.getElementById('new-goal');

// Safety elements
const safetyIndicator = document.getElementById('safety-indicator');
const safetyIcon = safetyIndicator.querySelector('.safety-icon');
const safetyText = safetyIndicator.querySelector('.safety-text');
const safetyDetails = document.getElementById('safety-details');
const toggleSafetyDetails = document.getElementById('toggle-safety-details');
const totalAlerts = document.getElementById('total-alerts');
const recentAlerts = document.getElementById('recent-alerts');
const criticalAlerts = document.getElementById('critical-alerts');
const recommendationsList = document.getElementById('recommendations-list');

// User ID - In a real app, this would be from authentication
const userId = 'user_' + Math.random().toString(36).substr(2, 9);

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    // Set up event listeners
    messageForm.addEventListener('submit', handleMessageSubmit);
    addGoalForm.addEventListener('submit', handleAddGoal);
    coachingStyleSelect.addEventListener('change', handleStyleChange);
    toggleSafetyDetails.addEventListener('click', handleToggleSafetyDetails);
    
    // Focus on message input
    userMessageInput.focus();
});

// Handle message submission
async function handleMessageSubmit(event) {
    event.preventDefault();
    
    const messageText = userMessageInput.value.trim();
    if (!messageText) return;
    
    // Add user message to chat
    addMessageToChat('user', messageText);
    
    // Clear input
    userMessageInput.value = '';
    
    // Get coaching style
    const coachingStyle = coachingStyleSelect.value;
    
    try {
        // Send message to backend
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: messageText,
                user_id: userId,
                coaching_style: coachingStyle
            })
        });
        
        const data = await response.json();
        
        // Add coach response to chat
        addMessageToChat('coach', data.response);
        
        // Update UI with user profile data
        updateUserProfileUI(data.user_profile);
        
        // Update safety status if available
        if (data.user_profile.safety_status) {
            updateSafetyStatus(data.user_profile.safety_status);
        }
        
    } catch (error) {
        console.error('Error sending message:', error);
        addMessageToChat('coach', 'Sorry, there was an error processing your message. Please try again.');
    }
    
    // Scroll to bottom of chat
    scrollToBottom();
}

// Add message to chat
function addMessageToChat(role, content) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', role);
    
    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');
    contentDiv.textContent = content;
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    scrollToBottom();
}

// Scroll to bottom of chat
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Handle adding a goal
function handleAddGoal(event) {
    event.preventDefault();
    
    const goalText = newGoalInput.value.trim();
    if (!goalText) return;
    
    addGoal(goalText);
    newGoalInput.value = '';
}

// Add a goal to the goals list
function addGoal(goalText) {
    // Remove empty list message if present
    const emptyMessage = goalsList.querySelector('.empty-list-message');
    if (emptyMessage) {
        goalsList.removeChild(emptyMessage);
    }
    
    const goalItem = document.createElement('li');
    goalItem.textContent = goalText;
    goalsList.appendChild(goalItem);
    
    // In a real app, we would send this to the backend
    // to update the user's profile
}

// Add an insight to the insights list
function addInsight(insightText) {
    // Remove empty list message if present
    const emptyMessage = insightsList.querySelector('.empty-list-message');
    if (emptyMessage) {
        insightsList.removeChild(emptyMessage);
    }
    
    const insightItem = document.createElement('li');
    insightItem.textContent = insightText;
    insightsList.appendChild(insightItem);
}

// Handle coaching style change
function handleStyleChange() {
    const style = coachingStyleSelect.value;
    
    // Add a system message about the style change
    let styleMessage = '';
    
    switch (style) {
        case 'supportive':
            styleMessage = 'Coaching style changed to Supportive. I\'ll focus on encouraging and positive feedback.';
            break;
        case 'challenging':
            styleMessage = 'Coaching style changed to Challenging. I\'ll push you to do better and question your assumptions.';
            break;
        case 'analytical':
            styleMessage = 'Coaching style changed to Analytical. I\'ll focus on data, patterns, and insights.';
            break;
    }
    
    addMessageToChat('coach', styleMessage);
    
    // In a real app, we would send this to the backend
    // to update the coaching style for this user
}

// Update UI with user profile data
function updateUserProfileUI(userProfile) {
    // Update goals list
    updateGoalsList(userProfile.goals, userProfile.progress);
    
    // Update insights list
    updateInsightsList(userProfile.insights);
    
    // Update performance metrics
    updatePerformanceMetrics(userProfile.performance_metrics);
    
    // Update mental state metrics
    updateMentalStateMetrics(userProfile.mental_state);
    
    // Update safety status if available
    if (userProfile.safety_status) {
        updateSafetyStatus(userProfile.safety_status);
    }
}

// Update goals list in UI
function updateGoalsList(goals, progress) {
    // Clear current goals list
    goalsList.innerHTML = '';
    
    if (!goals || goals.length === 0) {
        // Add empty message if no goals
        const emptyItem = document.createElement('li');
        emptyItem.classList.add('empty-list-message');
        emptyItem.textContent = 'No goals set yet';
        goalsList.appendChild(emptyItem);
        return;
    }
    
    // Add each goal with progress
    goals.forEach(goal => {
        const goalItem = document.createElement('li');
        
        // Create goal text with progress
        const progressPercent = Math.round((progress[goal] || 0) * 100);
        goalItem.innerHTML = `
            <div class="goal-text">${goal}</div>
            <div class="goal-progress">
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${progressPercent}%"></div>
                </div>
                <div class="progress-text">${progressPercent}%</div>
            </div>
        `;
        
        goalsList.appendChild(goalItem);
    });
}

// Update insights list in UI
function updateInsightsList(insights) {
    // Clear current insights list
    insightsList.innerHTML = '';
    
    if (!insights || insights.length === 0) {
        // Add empty message if no insights
        const emptyItem = document.createElement('li');
        emptyItem.classList.add('empty-list-message');
        emptyItem.textContent = 'No insights yet';
        insightsList.appendChild(emptyItem);
        return;
    }
    
    // Add last 5 insights (most recent first)
    insights.slice(-5).reverse().forEach(insight => {
        const insightItem = document.createElement('li');
        insightItem.textContent = insight.content;
        insightsList.appendChild(insightItem);
    });
}

// Update safety status in UI
function updateSafetyStatus(safetyStatus) {
    // Update safety indicator
    updateSafetyIndicator(safetyStatus);
    
    // Update safety stats
    totalAlerts.textContent = safetyStatus.total_alerts || 0;
    recentAlerts.textContent = safetyStatus.recent_alerts || 0;
    criticalAlerts.textContent = safetyStatus.critical_alerts || 0;
    
    // Update recommendations
    updateSafetyRecommendations(safetyStatus.recommendations || []);
}

// Update safety indicator based on status
function updateSafetyIndicator(safetyStatus) {
    // Remove existing status classes
    safetyIndicator.classList.remove('warning', 'critical', 'emergency');
    
    if (safetyStatus.escalation_required) {
        // Emergency or critical status
        safetyIcon.textContent = '🚨';
        safetyText.textContent = 'URGENT: Immediate Attention Required';
        safetyIndicator.classList.add('emergency');
    } else if (safetyStatus.critical_alerts > 0) {
        // Critical status
        safetyIcon.textContent = '⚠️';
        safetyText.textContent = 'Critical Alerts Detected';
        safetyIndicator.classList.add('critical');
    } else if (safetyStatus.recent_alerts > 0) {
        // Warning status
        safetyIcon.textContent = '⚠️';
        safetyText.textContent = 'Safety Alerts Detected';
        safetyIndicator.classList.add('warning');
    } else {
        // All clear
        safetyIcon.textContent = '🟢';
        safetyText.textContent = 'All Clear';
    }
}

// Update safety recommendations list
function updateSafetyRecommendations(recommendations) {
    // Clear current recommendations
    recommendationsList.innerHTML = '';
    
    if (!recommendations || recommendations.length === 0) {
        const emptyItem = document.createElement('li');
        emptyItem.classList.add('empty-list-message');
        emptyItem.textContent = 'No recommendations';
        recommendationsList.appendChild(emptyItem);
        return;
    }
    
    // Add each recommendation
    recommendations.forEach(rec => {
        const recItem = document.createElement('li');
        recItem.textContent = rec;
        recommendationsList.appendChild(recItem);
    });
}

// Handle toggle safety details
function handleToggleSafetyDetails() {
    if (safetyDetails.classList.contains('hidden')) {
        safetyDetails.classList.remove('hidden');
        toggleSafetyDetails.textContent = 'Hide Details';
    } else {
        safetyDetails.classList.add('hidden');
        toggleSafetyDetails.textContent = 'Show Details';
    }
}
