"""
AI Coach Safety Monitoring System

This module implements comprehensive safety features to protect athlete well-being,
ensure data integrity, and maintain fair coaching practices.
"""

import time
import re
import math
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum

class SafetyLevel(Enum):
    """Safety alert levels"""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    EMERGENCY = "emergency"

class SafetyCategory(Enum):
    """Categories of safety concerns"""
    OVERTRAINING = "overtraining"
    DATA_INCONSISTENCY = "data_inconsistency"
    LOW_ENGAGEMENT = "low_engagement"
    RESISTANCE = "resistance"
    CREATIVITY_MISUSE = "creativity_misuse"
    MENTAL_HEALTH = "mental_health"
    PERFORMANCE_DROP = "performance_drop"
    TEAM_CONFLICT = "team_conflict"
    REWARD_MISUSE = "reward_misuse"
    LANGUAGE_BARRIER = "language_barrier"
    FALSE_REPORTING = "false_reporting"
    BURNOUT_LAZINESS = "burnout_laziness"

@dataclass
class SafetyAlert:
    """Represents a safety alert"""
    category: SafetyCategory
    level: SafetyLevel
    message: str
    timestamp: float
    user_id: str
    context: Dict[str, Any]
    recommended_action: str
    escalation_required: bool = False

class SafetyMonitor:
    """Comprehensive safety monitoring system for AI coaching"""
    
    def __init__(self):
        self.alerts = []
        self.user_sessions = {}
        self.performance_baselines = {}
        self.engagement_metrics = {}
        self.mental_health_indicators = {}
        
        # Safety thresholds
        self.thresholds = {
            'fatigue_score': 0.8,
            'engagement_drop': 0.3,
            'performance_drop': 0.2,
            'mental_health_risk': 0.7,
            'inconsistency_threshold': 0.4,
            'resistance_threshold': 0.6,
            'burnout_indicators': 0.75
        }
        
        # Language complexity patterns
        self.complexity_patterns = [
            r'\b(?:utilize|implement|facilitate|optimize|leverage)\b',
            r'\b(?:paradigm|methodology|framework|infrastructure)\b',
            r'\b(?:consequently|furthermore|moreover|nevertheless)\b'
        ]
        
        # Mental health risk indicators
        self.mental_health_red_flags = [
            'suicide', 'kill myself', 'end it all', 'not worth living',
            'hopeless', 'worthless', 'burden', 'better off dead',
            'self harm', 'cut myself', 'hurt myself'
        ]
        
        # Overtraining indicators
        self.overtraining_indicators = [
            'exhausted', 'burned out', 'overtrained', 'plateaued',
            'no progress', 'stagnant', 'regressing', 'injured',
            'pain', 'sore', 'tired', 'fatigued', 'drained'
        ]
        
        # Resistance patterns
        self.resistance_patterns = [
            'i can\'t', 'impossible', 'won\'t work', 'tried that',
            'doesn\'t help', 'waste of time', 'stupid', 'pointless',
            'not for me', 'doesn\'t fit', 'too hard', 'too easy'
        ]

    def monitor_message(self, message: str, user_id: str, user_profile: Dict) -> List[SafetyAlert]:
        """Monitor a user message for safety concerns
        
        Args:
            message: User's message
            user_id: Unique user identifier
            user_profile: Current user profile data
            
        Returns:
            List of safety alerts generated
        """
        alerts = []
        message_lower = message.lower()
        
        # 1. Overtraining Detection
        alerts.extend(self._detect_overtraining(message_lower, user_id, user_profile))
        
        # 2. Inconsistent Data Detection
        alerts.extend(self._detect_data_inconsistency(message_lower, user_id, user_profile))
        
        # 3. Low Engagement Detection
        alerts.extend(self._detect_low_engagement(message_lower, user_id, user_profile))
        
        # 4. Resistance Detection
        alerts.extend(self._detect_resistance(message_lower, user_id, user_profile))
        
        # 5. Creativity Misuse Detection
        alerts.extend(self._detect_creativity_misuse(message_lower, user_id, user_profile))
        
        # 6. Mental Health Detection
        alerts.extend(self._detect_mental_health_risks(message_lower, user_id, user_profile))
        
        # 7. Performance Drop Detection
        alerts.extend(self._detect_performance_drop(message_lower, user_id, user_profile))
        
        # 8. Team Conflict Detection
        alerts.extend(self._detect_team_conflict(message_lower, user_id, user_profile))
        
        # 9. Reward Misuse Detection
        alerts.extend(self._detect_reward_misuse(message_lower, user_id, user_profile))
        
        # 10. Language Barrier Detection
        alerts.extend(self._detect_language_barriers(message_lower, user_id, user_profile))
        
        # 11. False Self-Reporting Detection
        alerts.extend(self._detect_false_reporting(message_lower, user_id, user_profile))
        
        # 12. Burnout vs Laziness Detection
        alerts.extend(self._detect_burnout_vs_laziness(message_lower, user_id, user_profile))
        
        # Store alerts
        self.alerts.extend(alerts)
        
        return alerts

    def _detect_overtraining(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect signs of overtraining and fatigue"""
        alerts = []
        
        # Check for overtraining indicators
        fatigue_score = sum(1 for indicator in self.overtraining_indicators 
                          if indicator in message) / len(self.overtraining_indicators)
        
        if fatigue_score > self.thresholds['fatigue_score']:
            alerts.append(SafetyAlert(
                category=SafetyCategory.OVERTRAINING,
                level=SafetyLevel.WARNING,
                message="Signs of overtraining detected. Consider rest and recovery.",
                timestamp=time.time(),
                user_id=user_id,
                context={'fatigue_score': fatigue_score, 'message': message},
                recommended_action="Enforce mandatory rest period and reduce training intensity",
                escalation_required=True
            ))
        
        # Check training frequency vs recovery
        if 'training' in message and 'every day' in message:
            alerts.append(SafetyAlert(
                category=SafetyCategory.OVERTRAINING,
                level=SafetyLevel.INFO,
                message="Daily training without rest days detected.",
                timestamp=time.time(),
                user_id=user_id,
                context={'message': message},
                recommended_action="Recommend rest days and recovery protocols",
                escalation_required=False
            ))
        
        return alerts

    def _detect_data_inconsistency(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect inconsistent or unreliable data"""
        alerts = []
        
        # Check for contradictory performance claims
        performance_metrics = profile.get('performance_metrics', {})
        if performance_metrics:
            # Look for impossible improvements
            if 'improved by' in message and any(metric in message for metric in performance_metrics.keys()):
                # Extract improvement percentage
                improvement_match = re.search(r'improved by (\d+)%', message)
                if improvement_match:
                    improvement = int(improvement_match.group(1))
                    if improvement > 50:  # Suspiciously high improvement
                        alerts.append(SafetyAlert(
                            category=SafetyCategory.DATA_INCONSISTENCY,
                            level=SafetyLevel.WARNING,
                            message="Unusually high performance improvement reported. Please verify data accuracy.",
                            timestamp=time.time(),
                            user_id=user_id,
                            context={'improvement': improvement, 'message': message},
                            recommended_action="Request verification and cross-check with objective measures",
                            escalation_required=False
                        ))
        
        # Check for conflicting statements
        if 'but' in message and ('good' in message or 'bad' in message):
            alerts.append(SafetyAlert(
                category=SafetyCategory.DATA_INCONSISTENCY,
                level=SafetyLevel.INFO,
                message="Conflicting statements detected in user feedback.",
                timestamp=time.time(),
                user_id=user_id,
                context={'message': message},
                recommended_action="Seek clarification and ask specific questions",
                escalation_required=False
            ))
        
        return alerts

    def _detect_low_engagement(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect low engagement and adapt coaching strategy"""
        alerts = []
        
        # Track engagement metrics
        if user_id not in self.engagement_metrics:
            self.engagement_metrics[user_id] = {
                'message_length': [],
                'response_time': [],
                'question_count': 0,
                'enthusiasm_score': []
            }
        
        # Analyze message characteristics
        message_length = len(message.split())
        enthusiasm_score = self._calculate_enthusiasm_score(message)
        
        self.engagement_metrics[user_id]['message_length'].append(message_length)
        self.engagement_metrics[user_id]['enthusiasm_score'].append(enthusiasm_score)
        
        # Check for low engagement patterns
        if message_length < 5:  # Very short responses
            alerts.append(SafetyAlert(
                category=SafetyCategory.LOW_ENGAGEMENT,
                level=SafetyLevel.WARNING,
                message="Very short response detected. User may be disengaged.",
                timestamp=time.time(),
                user_id=user_id,
                context={'message_length': message_length, 'message': message},
                recommended_action="Adapt tone to be more engaging and ask open-ended questions",
                escalation_required=False
            ))
        
        # Check enthusiasm trend
        recent_enthusiasm = self.engagement_metrics[user_id]['enthusiasm_score'][-5:]
        if len(recent_enthusiasm) >= 3 and sum(recent_enthusiasm) / len(recent_enthusiasm) < 0.3:
            alerts.append(SafetyAlert(
                category=SafetyCategory.LOW_ENGAGEMENT,
                level=SafetyLevel.WARNING,
                message="Declining enthusiasm detected over recent interactions.",
                timestamp=time.time(),
                user_id=user_id,
                context={'enthusiasm_trend': recent_enthusiasm, 'message': message},
                recommended_action="Switch to more supportive coaching style and explore motivation barriers",
                escalation_required=False
            ))
        
        return alerts

    def _detect_resistance(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect resistance and provide evidence-based reasoning"""
        alerts = []
        
        resistance_score = sum(1 for pattern in self.resistance_patterns 
                             if pattern in message) / len(self.resistance_patterns)
        
        if resistance_score > self.thresholds['resistance_threshold']:
            alerts.append(SafetyAlert(
                category=SafetyCategory.RESISTANCE,
                level=SafetyLevel.WARNING,
                message="High resistance detected in user response.",
                timestamp=time.time(),
                user_id=user_id,
                context={'resistance_score': resistance_score, 'message': message},
                recommended_action="Provide evidence-based reasoning and address concerns directly",
                escalation_required=False
            ))
        
        return alerts

    def _detect_creativity_misuse(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Validate creative moves before encouragement"""
        alerts = []
        
        # Check for potentially dangerous creative approaches
        dangerous_creativity = [
            'try something new', 'experiment', 'innovative', 'creative',
            'unconventional', 'different approach', 'outside the box'
        ]
        
        creativity_indicators = sum(1 for indicator in dangerous_creativity 
                                  if indicator in message)
        
        if creativity_indicators > 0:
            # Check if it's in a safe context
            if any(risk_word in message for risk_word in ['injury', 'dangerous', 'risky', 'unsafe']):
                alerts.append(SafetyAlert(
                    category=SafetyCategory.CREATIVITY_MISUSE,
                    level=SafetyLevel.CRITICAL,
                    message="Potentially dangerous creative approach detected.",
                    timestamp=time.time(),
                    user_id=user_id,
                    context={'creativity_indicators': creativity_indicators, 'message': message},
                    recommended_action="Validate safety before encouraging creative approaches",
                    escalation_required=True
                ))
            else:
                alerts.append(SafetyAlert(
                    category=SafetyCategory.CREATIVITY_MISUSE,
                    level=SafetyLevel.INFO,
                    message="Creative approach suggested. Validating safety.",
                    timestamp=time.time(),
                    user_id=user_id,
                    context={'creativity_indicators': creativity_indicators, 'message': message},
                    recommended_action="Ensure safety protocols are in place before encouragement",
                    escalation_required=False
                ))
        
        return alerts

    def _detect_mental_health_risks(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect mental health concerns and escalate carefully"""
        alerts = []
        
        # Check for mental health red flags
        red_flag_count = sum(1 for flag in self.mental_health_red_flags 
                           if flag in message)
        
        if red_flag_count > 0:
            alerts.append(SafetyAlert(
                category=SafetyCategory.MENTAL_HEALTH,
                level=SafetyLevel.EMERGENCY,
                message="Critical mental health indicators detected. Immediate escalation required.",
                timestamp=time.time(),
                user_id=user_id,
                context={'red_flag_count': red_flag_count, 'message': message},
                recommended_action="Immediately suggest professional help and provide crisis resources",
                escalation_required=True
            ))
        
        # Check for anxiety/depression indicators
        anxiety_indicators = ['anxious', 'worried', 'stressed', 'overwhelmed', 'panic']
        depression_indicators = ['sad', 'depressed', 'hopeless', 'worthless', 'empty']
        
        anxiety_score = sum(1 for indicator in anxiety_indicators if indicator in message)
        depression_score = sum(1 for indicator in depression_indicators if indicator in message)
        
        mental_health_risk = (anxiety_score + depression_score) / (len(anxiety_indicators) + len(depression_indicators))
        
        if mental_health_risk > self.thresholds['mental_health_risk']:
            alerts.append(SafetyAlert(
                category=SafetyCategory.MENTAL_HEALTH,
                level=SafetyLevel.WARNING,
                message="Signs of anxiety or depression detected. Suggest professional support.",
                timestamp=time.time(),
                user_id=user_id,
                context={'mental_health_risk': mental_health_risk, 'message': message},
                recommended_action="Gently suggest professional mental health support and reduce pressure",
                escalation_required=True
            ))
        
        return alerts

    def _detect_performance_drop(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect sudden performance drops and adjust intensity"""
        alerts = []
        
        # Check for performance decline indicators
        decline_indicators = ['worse', 'declined', 'dropped', 'regressed', 'struggling', 'failing']
        injury_indicators = ['injured', 'hurt', 'pain', 'sore', 'injury', 'hurt']
        
        has_decline = any(indicator in message for indicator in decline_indicators)
        has_injury = any(indicator in message for indicator in injury_indicators)
        
        if has_decline or has_injury:
            level = SafetyLevel.CRITICAL if has_injury else SafetyLevel.WARNING
            alerts.append(SafetyAlert(
                category=SafetyCategory.PERFORMANCE_DROP,
                level=level,
                message="Performance decline or injury detected. Adjusting coaching intensity.",
                timestamp=time.time(),
                user_id=user_id,
                context={'has_decline': has_decline, 'has_injury': has_injury, 'message': message},
                recommended_action="Stop high-intensity advice and focus on recovery/support",
                escalation_required=has_injury
            ))
        
        return alerts

    def _detect_team_conflict(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect team conflicts and motivate fairly"""
        alerts = []
        
        conflict_indicators = ['team', 'teammate', 'coach', 'conflict', 'argument', 'disagreement']
        ego_indicators = ['better than', 'superior', 'best', 'worst', 'inferior']
        
        has_conflict = any(indicator in message for indicator in conflict_indicators)
        has_ego = any(indicator in message for indicator in ego_indicators)
        
        if has_conflict:
            alerts.append(SafetyAlert(
                category=SafetyCategory.TEAM_CONFLICT,
                level=SafetyLevel.WARNING,
                message="Team conflict detected. Focus on fair motivation without ego inflation.",
                timestamp=time.time(),
                user_id=user_id,
                context={'has_conflict': has_conflict, 'has_ego': has_ego, 'message': message},
                recommended_action="Promote team unity and individual growth without comparison",
                escalation_required=False
            ))
        
        return alerts

    def _detect_reward_misuse(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect gaming of reward systems"""
        alerts = []
        
        gaming_indicators = ['easy points', 'quick win', 'gaming', 'cheating', 'shortcut']
        reward_focus = ['reward', 'points', 'achievement', 'badge', 'level']
        
        has_gaming = any(indicator in message for indicator in gaming_indicators)
        has_reward_focus = any(indicator in message for indicator in reward_focus)
        
        if has_gaming or (has_reward_focus and 'easy' in message):
            alerts.append(SafetyAlert(
                category=SafetyCategory.REWARD_MISUSE,
                level=SafetyLevel.WARNING,
                message="Potential reward system gaming detected.",
                timestamp=time.time(),
                user_id=user_id,
                context={'has_gaming': has_gaming, 'has_reward_focus': has_reward_focus, 'message': message},
                recommended_action="Adjust incentives to focus on genuine progress and effort",
                escalation_required=False
            ))
        
        return alerts

    def _detect_language_barriers(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Detect language barriers and simplify instructions"""
        alerts = []
        
        # Check for complex language patterns
        complexity_score = sum(1 for pattern in self.complexity_patterns 
                             if re.search(pattern, message, re.IGNORECASE))
        
        # Check for non-native speaker indicators
        non_native_indicators = ['i am not sure', 'i don\'t understand', 'confused', 'unclear']
        has_confusion = any(indicator in message for indicator in non_native_indicators)
        
        if complexity_score > 2 or has_confusion:
            alerts.append(SafetyAlert(
                category=SafetyCategory.LANGUAGE_BARRIER,
                level=SafetyLevel.INFO,
                message="Language barrier detected. Simplifying instructions.",
                timestamp=time.time(),
                user_id=user_id,
                context={'complexity_score': complexity_score, 'has_confusion': has_confusion, 'message': message},
                recommended_action="Rephrase instructions in simpler language and provide examples",
                escalation_required=False
            ))
        
        return alerts

    def _detect_false_reporting(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Cross-check self-reported ratings against performance"""
        alerts = []
        
        # Look for self-ratings
        rating_patterns = [
            r'rate myself (\d+)/10',
            r'i am (\d+)/10',
            r'my level is (\d+)',
            r'i would say (\d+)'
        ]
        
        for pattern in rating_patterns:
            match = re.search(pattern, message)
            if match:
                self_rating = int(match.group(1))
                
                # Cross-check with performance metrics
                performance_metrics = profile.get('performance_metrics', {})
                if performance_metrics:
                    # Simple heuristic: if self-rating is much higher than performance suggests
                    avg_performance = sum(performance_metrics.values()) / len(performance_metrics)
                    if self_rating > avg_performance * 2:  # Self-rating twice as high
                        alerts.append(SafetyAlert(
                            category=SafetyCategory.FALSE_REPORTING,
                            level=SafetyLevel.WARNING,
                            message="Self-rating appears inflated compared to performance data.",
                            timestamp=time.time(),
                            user_id=user_id,
                            context={'self_rating': self_rating, 'avg_performance': avg_performance, 'message': message},
                            recommended_action="Request objective performance measures and provide honest feedback",
                            escalation_required=False
                        ))
        
        return alerts

    def _detect_burnout_vs_laziness(self, message: str, user_id: str, profile: Dict) -> List[SafetyAlert]:
        """Distinguish between true burnout and poor discipline"""
        alerts = []
        
        # Burnout indicators (genuine fatigue)
        burnout_indicators = [
            'exhausted', 'burned out', 'overwhelmed', 'can\'t continue',
            'mentally drained', 'physically drained', 'no energy'
        ]
        
        # Laziness indicators (avoidance behavior)
        laziness_indicators = [
            'don\'t feel like it', 'too lazy', 'can\'t be bothered',
            'not motivated', 'don\'t want to', 'avoiding'
        ]
        
        burnout_score = sum(1 for indicator in burnout_indicators if indicator in message)
        laziness_score = sum(1 for indicator in laziness_indicators if indicator in message)
        
        if burnout_score > laziness_score and burnout_score > 0:
            alerts.append(SafetyAlert(
                category=SafetyCategory.BURNOUT_LAZINESS,
                level=SafetyLevel.WARNING,
                message="Genuine burnout detected. Prioritize recovery and rest.",
                timestamp=time.time(),
                user_id=user_id,
                context={'burnout_score': burnout_score, 'laziness_score': laziness_score, 'message': message},
                recommended_action="Implement recovery protocols and reduce training load",
                escalation_required=True
            ))
        elif laziness_score > burnout_score and laziness_score > 0:
            alerts.append(SafetyAlert(
                category=SafetyCategory.BURNOUT_LAZINESS,
                level=SafetyLevel.INFO,
                message="Avoidance behavior detected. Address motivation barriers.",
                timestamp=time.time(),
                user_id=user_id,
                context={'burnout_score': burnout_score, 'laziness_score': laziness_score, 'message': message},
                recommended_action="Focus on motivation and discipline strategies",
                escalation_required=False
            ))
        
        return alerts

    def _calculate_enthusiasm_score(self, message: str) -> float:
        """Calculate enthusiasm score from message content"""
        positive_words = ['excited', 'great', 'awesome', 'amazing', 'fantastic', 'love', 'enjoy']
        negative_words = ['boring', 'hate', 'terrible', 'awful', 'disappointed', 'frustrated']
        
        positive_count = sum(1 for word in positive_words if word in message)
        negative_count = sum(1 for word in negative_words if word in message)
        
        total_words = len(message.split())
        if total_words == 0:
            return 0.5
        
        enthusiasm = (positive_count - negative_count) / total_words
        return max(0, min(1, enthusiasm + 0.5))  # Normalize to 0-1

    def get_safety_recommendations(self, user_id: str) -> List[str]:
        """Get safety recommendations for a user based on their alerts"""
        user_alerts = [alert for alert in self.alerts if alert.user_id == user_id]
        
        if not user_alerts:
            return ["No safety concerns detected. Continue normal coaching."]
        
        recommendations = []
        
        # Group by category
        categories = {}
        for alert in user_alerts:
            if alert.category not in categories:
                categories[alert.category] = []
            categories[alert.category].append(alert)
        
        # Generate recommendations
        for category, alerts in categories.items():
            if category == SafetyCategory.OVERTRAINING:
                recommendations.append("Implement mandatory rest periods and reduce training intensity")
            elif category == SafetyCategory.MENTAL_HEALTH:
                recommendations.append("Prioritize mental health support and consider professional referral")
            elif category == SafetyCategory.PERFORMANCE_DROP:
                recommendations.append("Focus on recovery and reduce high-intensity coaching")
            elif category == SafetyCategory.LOW_ENGAGEMENT:
                recommendations.append("Adapt coaching style to be more engaging and supportive")
            elif category == SafetyCategory.RESISTANCE:
                recommendations.append("Provide evidence-based reasoning and address concerns directly")
            elif category == SafetyCategory.CREATIVITY_MISUSE:
                recommendations.append("Validate safety before encouraging creative approaches")
            elif category == SafetyCategory.TEAM_CONFLICT:
                recommendations.append("Promote fair motivation without ego inflation")
            elif category == SafetyCategory.REWARD_MISUSE:
                recommendations.append("Adjust incentives to focus on genuine progress")
            elif category == SafetyCategory.LANGUAGE_BARRIER:
                recommendations.append("Simplify language and provide clear examples")
            elif category == SafetyCategory.FALSE_REPORTING:
                recommendations.append("Request objective measures and provide honest feedback")
            elif category == SafetyCategory.BURNOUT_LAZINESS:
                recommendations.append("Distinguish between burnout and discipline issues")
            elif category == SafetyCategory.DATA_INCONSISTENCY:
                recommendations.append("Verify data accuracy and seek clarification")
        
        return recommendations

    def get_escalation_alerts(self) -> List[SafetyAlert]:
        """Get alerts that require immediate escalation"""
        return [alert for alert in self.alerts if alert.escalation_required]

    def clear_user_alerts(self, user_id: str):
        """Clear alerts for a specific user"""
        self.alerts = [alert for alert in self.alerts if alert.user_id != user_id]


